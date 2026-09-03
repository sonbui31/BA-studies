#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(process.argv[2] || process.cwd());
const docsDir = path.join(root, 'docs');
const staticDir = path.join(root, 'static');
const minLines = Number(process.env.MIN_DOC_LINES || 48);

const imageExt = new Set(['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']);
const docExt = new Set(['.md', '.mdx']);
const requiredRootFiles = ['package.json', 'docusaurus.config.js', 'sidebars.js'];
const defaultBannedTerms = [
  'Sidebar ->',
  'Sidebar →',
  'Docsify',
  'docsify',
  'Quyền truy cập: Yêu cầu quyền',
];
const extraBannedTerms = (process.env.DOCS_BANNED_TERMS || '')
  .split(',')
  .map((term) => term.trim())
  .filter(Boolean);
const bannedTerms = [...defaultBannedTerms, ...extraBannedTerms];
const placeholders = [
  '[Tên hệ thống]',
  '{{SYSTEM_NAME}}',
  '{{PACKAGE_NAME}}',
  '{{GITHUB_OWNER}}',
  '{{GITHUB_REPO}}',
  '{{VERSION}}',
  '{{ONE_SENTENCE_VALUE_PROP}}',
  '[Tên chức năng]',
  '[module]',
  '[Vai trò',
  '[đối tượng]',
  '[Nhóm]',
  '[Chức năng]',
];
const sensitivePatterns = [
  { label: 'possible email address', pattern: /\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i },
  { label: 'possible Vietnamese phone number', pattern: /\b(?:\+?84|0)(?:\s|\.)?(?:3|5|7|8|9)(?:\d(?:\s|\.)?){8}\b/ },
  { label: 'possible bearer token', pattern: /\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b/i },
  { label: 'possible API key or secret assignment', pattern: /\b(?:api[_-]?key|secret|token|password|passwd|pwd)\s*[:=]\s*["']?[^"'\s]{8,}/i },
  { label: 'possible Vietnamese citizen ID', pattern: /\b\d{12}\b/ },
  { label: 'possible production/internal URL', pattern: /https?:\/\/(?!example\.|localhost|127\.0\.0\.1)[^\s)>'"]+/i },
];
const technicalPatterns = [
  { label: 'possible raw permission code', pattern: /\b[a-z][a-z0-9-]*:[a-z][A-Za-z0-9-]*\b/ },
  { label: 'old arrow navigation term', pattern: /\bSidebar\s*(?:->|→)/ },
];

const findings = [];

function add(type, message) {
  findings.push({ type, message });
}

function exists(filePath) {
  try {
    fs.accessSync(filePath);
    return true;
  } catch {
    return false;
  }
}

function read(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

function walk(dir, predicate = () => true, acc = []) {
  if (!exists(dir)) return acc;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, predicate, acc);
    else if (predicate(full)) acc.push(full);
  }
  return acc;
}

function posixRel(from, to) {
  return path.relative(from, to).split(path.sep).join('/');
}

function isExternal(target) {
  return /^(https?:)?\/\//.test(target) || /^(mailto|tel):/.test(target) || target.startsWith('#');
}

function stripAnchorAndQuery(target) {
  return target.split('#')[0].split('?')[0];
}

function parseMarkdownLinks(content) {
  const links = [];
  const imageRe = /!\[[^\]]*]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
  const linkRe = /(?<!!)\[[^\]]+]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
  let match;
  while ((match = imageRe.exec(content))) links.push({ kind: 'image', target: match[1] });
  while ((match = linkRe.exec(content))) links.push({ kind: 'link', target: match[1] });
  return links;
}

function candidateDocPaths(rawPath) {
  const clean = decodeURI(stripAnchorAndQuery(rawPath)).replace(/^\/docs\/?/, '');
  if (!clean) return [];
  const base = path.join(docsDir, clean);
  const ext = path.extname(base).toLowerCase();
  if (docExt.has(ext)) return [base];
  return [
    `${base}.md`,
    `${base}.mdx`,
    path.join(base, `${path.basename(base)}.md`),
    path.join(base, `${path.basename(base)}.mdx`),
    path.join(base, 'index.md'),
    path.join(base, 'index.mdx'),
    path.join(base, 'README.md'),
    path.join(base, 'README.mdx'),
  ];
}

function resolveTarget(markdownFile, item) {
  const clean = decodeURI(stripAnchorAndQuery(item.target));
  if (!clean || isExternal(clean)) return [];

  if (item.kind === 'image') {
    if (clean.startsWith('/')) return [path.join(staticDir, clean.replace(/^\/+/, ''))];
    return [path.resolve(path.dirname(markdownFile), clean)];
  }

  if (clean.startsWith('/docs/')) return candidateDocPaths(clean);
  if (clean.startsWith('/')) return [];

  const resolved = path.resolve(path.dirname(markdownFile), clean);
  const ext = path.extname(resolved).toLowerCase();
  if (docExt.has(ext) || imageExt.has(ext)) return [resolved];
  return [];
}

function anyExists(paths) {
  return paths.some((filePath) => exists(filePath));
}

if (!exists(docsDir)) {
  console.error(`Missing docs directory: ${docsDir}`);
  process.exit(2);
}

for (const file of requiredRootFiles) {
  if (!exists(path.join(root, file))) add('MISSING_DOCUSAURUS_FILE', `${file} does not exist`);
}

if (!exists(path.join(staticDir, '.nojekyll'))) {
  add('MISSING_NOJEKYLL', 'static/.nojekyll does not exist; GitHub Pages can drop files/folders that start with "_"');
}

if (!exists(path.join(root, 'handoff-notes.md'))) {
  add('MISSING_HANDOFF_NOTES', 'handoff-notes.md does not exist; unresolved facts and role/source mapping should be tracked outside user docs');
}

if (exists(path.join(root, 'index.html'))) {
  add('DOCSIFY_LEFTOVER', 'index.html exists at manual root; Docusaurus should use src/pages/index.js');
}

if (exists(path.join(docsDir, '_sidebar.md'))) {
  add('DOCSIFY_LEFTOVER', 'docs/_sidebar.md exists; Docusaurus should use sidebars.js and _category_.json');
}

const packageFile = path.join(root, 'package.json');
if (exists(packageFile)) {
  try {
    const pkg = JSON.parse(read(packageFile));
    const deps = { ...(pkg.dependencies || {}), ...(pkg.devDependencies || {}) };
    for (const dep of ['@docusaurus/core', '@docusaurus/preset-classic']) {
      if (!deps[dep]) add('MISSING_DEPENDENCY', `package.json is missing ${dep}`);
      else if (!/3\./.test(deps[dep])) add('DOCUSAURUS_VERSION', `${dep} should target Docusaurus 3.x, found ${deps[dep]}`);
    }
  } catch (error) {
    add('INVALID_PACKAGE_JSON', `package.json could not be parsed: ${error.message}`);
  }
}

const configFile = path.join(root, 'docusaurus.config.js');
if (exists(configFile)) {
  const config = read(configFile);
  if (!/baseUrl\s*:/.test(config)) add('MISSING_CONFIG', 'docusaurus.config.js is missing baseUrl');
  if (!/trailingSlash\s*:/.test(config)) add('MISSING_CONFIG', 'docusaurus.config.js is missing trailingSlash');
  if (/baseUrl\s*:\s*['"]\/['"]/.test(config) && /projectName\s*:\s*['"](?![^'"]+\.github\.io)/.test(config)) {
    add('POSSIBLE_BASEURL', 'baseUrl is "/" but projectName is not a *.github.io root Pages repo');
  }
  if (/url\s*:\s*['"]https:\/\/[^'"]+\.github\.io['"]/.test(config) && !/baseUrl\s*:\s*['"]\/[^'"]+\/['"]/.test(config) && !/projectName\s*:\s*['"][^'"]+\.github\.io['"]/.test(config)) {
    add('POSSIBLE_BASEURL', 'GitHub Pages project sites should use a repo-prefixed baseUrl such as /repo-name/');
  }
}

const homePage = path.join(root, 'src', 'pages', 'index.js');
if (!exists(homePage)) {
  add('MISSING_HOME_PAGE', 'src/pages/index.js does not exist; Docusaurus manuals need a product introduction Home page');
} else {
  const home = read(homePage);
  if (/<Redirect\b|from ['"]@docusaurus\/router['"]/.test(home)) {
    add('REDIRECT_HOME_PAGE', 'src/pages/index.js appears to be redirect-only; create a product introduction Home page instead');
  }
  if (!/\/docs\/intro/.test(home)) {
    add('HOME_DOCS_CTA', 'src/pages/index.js should link to /docs/intro');
  }
  if (!/\/img\/screenshots\//.test(home)) {
    add('HOME_SCREENSHOT', 'src/pages/index.js should use a real product screenshot from /img/screenshots/');
  }
}

const markdownFiles = walk(docsDir, (file) => docExt.has(path.extname(file).toLowerCase()));
const referencedImages = new Set();

for (const file of markdownFiles) {
  const rel = posixRel(root, file);
  const content = read(file);
  const lines = content.split(/\r?\n/);

  if (lines.length < minLines) {
    add('SHORT', `${rel} has ${lines.length} lines`);
  }

  for (const term of bannedTerms) {
    if (content.includes(term)) add('TERM', `${rel} contains "${term}"`);
  }

  for (const placeholder of placeholders) {
    if (content.includes(placeholder)) add('PLACEHOLDER', `${rel} contains "${placeholder}"`);
  }

  for (const { label, pattern } of sensitivePatterns) {
    if (pattern.test(content)) add('SENSITIVE_DATA', `${rel} contains ${label}`);
  }

  for (const { label, pattern } of technicalPatterns) {
    if (pattern.test(content)) add('TECHNICAL_TERM', `${rel} contains ${label}`);
  }

  if (/^::::/m.test(content)) {
    add('ADMONITION_SYNTAX', `${rel} contains four-colon admonition syntax`);
  }

  if (/^:::(note|tip|info|warning|danger|caution)[ \t]+[^\[\s].*$/m.test(content)) {
    add('ADMONITION_TITLE', `${rel} uses old title syntax; use :::tip[Title]`);
  }

  if (/<!--\s*!\[[\s\S]*?]\(/.test(content)) {
    add('COMMENTED_IMAGE', `${rel} contains a commented-out image`);
  }

  for (const item of parseMarkdownLinks(content)) {
    const resolvedTargets = resolveTarget(file, item);
    if (resolvedTargets.length === 0) continue;

    if (item.kind === 'image') {
      for (const target of resolvedTargets) referencedImages.add(path.resolve(target));
    }

    if (!anyExists(resolvedTargets)) {
      add(item.kind === 'image' ? 'BROKEN_IMAGE' : 'BROKEN_LINK', `${rel} -> ${item.target}`);
    }
  }

  if (/docs\/workflows\//.test(rel) && !/!\[[^\]]*]\(/.test(content)) {
    add('WORKFLOW_NO_SCREENSHOT', `${rel} has no screenshot; workflow pages should show the real list/form/approval states or explain the gap in handoff-notes.md`);
  }
}

for (const image of walk(staticDir, (file) => imageExt.has(path.extname(file).toLowerCase()))) {
  if (!referencedImages.has(path.resolve(image))) {
    add('ORPHAN_IMAGE', posixRel(root, image));
  }
}

const screenshotCount = walk(path.join(staticDir, 'img', 'screenshots'), (file) => imageExt.has(path.extname(file).toLowerCase())).length;

if (findings.length === 0) {
  console.log(`Documentation audit passed. Pages: ${markdownFiles.length}. Screenshots: ${screenshotCount}.`);
  process.exit(0);
}

console.log(`Documentation audit found ${findings.length} issue(s). Pages: ${markdownFiles.length}. Screenshots: ${screenshotCount}.`);
for (const finding of findings) {
  console.log(`${finding.type}: ${finding.message}`);
}
process.exit(1);
