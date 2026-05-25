# BA Knowledge Source

The original `BA/` folder is not tracked in git because it contains large source documents.

Runtime use does not need the source folder. `BA-agent` searches the packaged index in:

```text
BA-agent/knowledge-index/chunks.jsonl
BA-agent/knowledge-index/manifest.json
```

Rebuild requires a local copy of the external source pack:

```powershell
python .\BA-agent\scripts\build_knowledge_index.py --source <path-to-BA-folder>
```

After rebuilding, commit only the updated files under `BA-agent/knowledge-index/` and the source manifest if the source pack changed.
