# BA Knowledge Source

The original `BA/` folder is not tracked in git. It holds third-party books, study guides and slide decks.

## What is tracked

- `BA-agent/BA-document-rule/references/ba-knowledge-cards.json` and `ba-knowledge-base.md`: distilled knowledge, searched with `python BA-agent/scripts/knowledge_search.py "<topic>"`.
- `BA-agent/knowledge-source/*.md`: BABOK v3 framework, 50 techniques, estimation guide (written for this project).
- `BA-agent/knowledge-index/manifest.json`: build statistics only.

## What is local-only

`BA-agent/knowledge-index/chunks.jsonl` (and `knowledge-index/semantic/`) hold text extracted from the source pack. They are gitignored. Do not commit them: the text comes from copyrighted material.

`python BA-agent/scripts/knowledge_index_search.py` works only on machines that have built this file.

## Rebuild (local machines with the source pack)

```powershell
python .\BA-agent\scripts\build_knowledge_index.py --source <path-to-BA-folder>
```

Do not commit the generated `chunks.jsonl`.
