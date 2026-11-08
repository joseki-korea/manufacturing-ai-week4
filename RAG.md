# RAG ingestion

## LLM wiki

Repository sources are the raw layer; `docs/wiki/` contains the wiki and its schema. Run `python3 scripts/rag-manifest.py` to refresh the heading catalog and `python3 scripts/wiki-lint.py` to check the wiki. Vector indexes are generated locally and are not committed.
