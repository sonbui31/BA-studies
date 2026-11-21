#!/usr/bin/env node
// Render a BPMN 2.0 file (.bpmn) to PNG or SVG with bpmn-js, the bpmn.io renderer.
//
// Usage: node bpmn_render.mjs <in.bpmn> <out.png|out.svg> [--scale 2] [--browser <chrome/edge path>]
//
// Needs bpmn-js and puppeteer-core (or puppeteer) in a node_modules folder:
//   npm install --prefix <dir> bpmn-js@17 puppeteer-core@23
// Point to it with BA_BPMN_NODE_MODULES=<dir>/node_modules (default: next to this script, then cwd).
// The browser comes from --browser, BA_MERMAID_BROWSER, PUPPETEER_EXECUTABLE_PATH, or puppeteer's own.
// Exit codes: 0 ok, 1 import error or BPMN warnings, 2 bad arguments or missing dependencies.
import { createRequire } from "node:module";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const args = process.argv.slice(2);
const option = (name, fallback) => {
  const index = args.indexOf(name);
  if (index === -1) return fallback;
  const value = args[index + 1];
  args.splice(index, 2);
  return value;
};
const scale = Number(option("--scale", "2"));
const browserPath = option("--browser", process.env.BA_MERMAID_BROWSER || process.env.PUPPETEER_EXECUTABLE_PATH);
const [input, output] = args;
if (!input || !output || !/\.(png|svg)$/i.test(output)) {
  console.error("Usage: node bpmn_render.mjs <in.bpmn> <out.png|out.svg> [--scale 2] [--browser PATH]");
  process.exit(2);
}

const here = path.dirname(fileURLToPath(import.meta.url));
const candidates = [process.env.BA_BPMN_NODE_MODULES, path.join(here, "node_modules"), path.join(process.cwd(), "node_modules")].filter(Boolean);
const modulesDir = candidates.find((dir) => existsSync(path.join(dir, "bpmn-js")));
if (!modulesDir) {
  console.error("Missing bpmn-js. Run: npm install --prefix <dir> bpmn-js@17 puppeteer-core@23 and set BA_BPMN_NODE_MODULES=<dir>/node_modules");
  process.exit(2);
}
const require = createRequire(path.join(modulesDir, "noop.js"));
let puppeteer;
try {
  puppeteer = require("puppeteer-core");
} catch {
  try {
    puppeteer = require("puppeteer");
  } catch {
    console.error("Missing puppeteer-core in " + modulesDir);
    process.exit(2);
  }
}
const dist = path.join(modulesDir, "bpmn-js", "dist");
const xml = readFileSync(input, "utf8");

const launchOptions = { headless: true, args: ["--no-sandbox"] };
if (browserPath) launchOptions.executablePath = browserPath;
const browser = await puppeteer.launch(launchOptions);
try {
  const page = await browser.newPage();
  await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0"><div id="canvas" style="width:3000px;height:2000px"></div></body></html>');
  for (const css of ["diagram-js.css", "bpmn-js.css", "bpmn-font/css/bpmn-embedded.css"]) {
    await page.addStyleTag({ path: path.join(dist, "assets", css) });
  }
  await page.addScriptTag({ path: path.join(dist, "bpmn-viewer.production.min.js") });
  const result = await page.evaluate(async (diagramXml) => {
    const viewer = new window.BpmnJS({ container: "#canvas" });
    try {
      const { warnings } = await viewer.importXML(diagramXml);
      const { svg } = await viewer.saveSVG();
      return { svg, warnings: warnings.map((w) => w.message) };
    } catch (error) {
      return { error: String(error && error.message ? error.message : error) };
    }
  }, xml);
  if (result.error) {
    console.error("BPMN import failed: " + result.error);
    process.exitCode = 1;
  } else if (/\.svg$/i.test(output)) {
    writeFileSync(output, result.svg, "utf8");
  } else {
    const size = result.svg.match(/width="([\d.]+)" height="([\d.]+)"/);
    const width = Math.ceil(Number(size ? size[1] : 1200));
    const height = Math.ceil(Number(size ? size[2] : 800));
    await page.setViewport({ width, height, deviceScaleFactor: scale });
    await page.setContent(`<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;background:#fff">${result.svg}</body></html>`);
    const element = await page.$("svg");
    await element.screenshot({ path: output, omitBackground: false });
  }
  if (!result.error) {
    for (const warning of result.warnings) console.error("BPMN warning: " + warning);
    console.log(`OK: ${output}`);
    process.exitCode = result.warnings.length ? 1 : 0;
  }
} finally {
  await browser.close();
}
