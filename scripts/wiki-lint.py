#!/usr/bin/env python3
"""Check wiki metadata, indexed pages, citations and local Markdown links."""
import re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / 'docs/wiki'
FIELDS = ('id','title','summary','domain','tags','owner','status','created','updated','source','lang','sensitivity','related')
CITE = re.compile(r'\[source: ([^\]\n]+?)#L(\d+) @([0-9a-f]{8})\]')
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
errors = []
def error(path, msg): errors.append(f'{path.relative_to(ROOT)}: {msg}')
def main():
    pages = sorted((WIKI / 'pages').rglob('*.md'))
    index = (WIKI / 'index.md').read_text(encoding='utf-8')
    for path in pages:
        text = path.read_text(encoding='utf-8')
        if not re.fullmatch(r'[a-z0-9-]+', path.stem): error(path, 'filename must be kebab-case')
        if text.count('---\n') < 2 or not text.startswith('---\n'):
            error(path, 'front matter missing'); continue
        front, body = text[4:].split('---\n', 1)
        fields = dict(re.findall(r'(?m)^([a-z]+):\s*(.+)$', front))
        for key in FIELDS:
            if not fields.get(key): error(path, f'missing {key}')
        if fields.get('sensitivity', '').strip('"\'').lower() == 'secret': error(path, 'secret page forbidden')
        rel = path.relative_to(WIKI).as_posix()
        if f']({rel})' not in index: error(path, 'orphan: not in index')
        in_fence = False
        for no, line in enumerate(body.splitlines(), 1):
            if line.strip().startswith('```'): in_fence = not in_fence; continue
            if in_fence or not line.strip() or line.lstrip().startswith(('#', '| ---', '<!--')): continue
            if not CITE.search(line): error(path, f'uncited content near body line {no}')
        for source, line, sha in CITE.findall(text):
            file = ROOT / source
            if not file.is_file(): error(path, f'missing source {source}'); continue
            try:
                old = subprocess.check_output(['git','show',f'{sha}:{source}'], cwd=ROOT, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                error(path, f'invalid revision {sha}:{source}'); continue
            if old != file.read_bytes(): error(path, f'stale source {source} @{sha}')
            if int(line) < 1 or int(line) > len(old.splitlines()): error(path, f'invalid line {source}#L{line}')
        for target in LINK.findall(body):
            target = unquote(target.split(' ',1)[0])
            if target.startswith(('https:', 'http:', 'mailto:', '#')): continue
            file = (path.parent / target.split('#')[0]).resolve()
            if not file.exists(): error(path, f'broken link {target}')
    for document in sorted(WIKI.rglob('*.md')):
        content = document.read_text(encoding='utf-8')
        for target in LINK.findall(content):
            target = unquote(target.split(' ', 1)[0])
            if target.startswith(('https:', 'http:', 'mailto:')): continue
            location, _, fragment = target.partition('#')
            dest = (document.parent / location).resolve() if location else document
            if not dest.is_file():
                error(document, f'broken link {target}'); continue
            if fragment and dest.suffix.lower() == '.md':
                headings = re.findall(r'(?m)^#{1,6}\s+(.+?)\s*#*\s*$', dest.read_text(encoding='utf-8'))
                slugs = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
                if fragment not in slugs: error(document, f'broken anchor {target}')
    links = re.findall(r'\]\((pages/[^)#]+\.md)\)', index)
    if len(links) != len(pages) or len(set(links)) != len(pages): error(WIKI/'index.md', 'index count or duplicates')
    if errors:
        print('\n'.join(errors)); print(f'FAIL: {len(errors)} errors'); sys.exit(1)
    print(f'PASS: {len(pages)} pages')
if __name__ == '__main__': main()
