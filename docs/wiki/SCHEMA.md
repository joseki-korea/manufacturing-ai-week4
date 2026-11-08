# Wiki schema

Raw sources remain in the repository; do not copy source files into the wiki. Each page covers one topic and has the required front matter: id, title, summary, domain, tags, owner, status, created, updated, source, lang, sensitivity, related. Names use lowercase kebab-case; titles may be Korean. Never create secret pages or include personal data or internal company figures.

## Ingest

Read the actual source, cite each claim as `[source: path#Lline @sha8]` using the source commit, update affected pages and the index, append an ingest entry to log.md, then regenerate the manifest and run the linter. Keep sections concise and tables headed.

## Query

Start at index.md, read the relevant page and its cited source lines, and report uncertainty rather than inventing an answer. Save an answer only when supported by repository evidence.

## Lint

Run `python3 scripts/wiki-lint.py` from the repository root. Resolve missing metadata, orphan pages, uncited content, stale sources, and broken links. Review source meaning and confidentiality independently; automated checks cannot prove either.

## Page types

Use overview for the repository, modules for folder or module roles and dependencies, concepts for recurring terminology, entities for models, APIs, screens or services, howto for verified tasks, and faq for evidenced questions.
