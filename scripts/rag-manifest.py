#!/usr/bin/env python3
"""Build a deterministic, heading-based Markdown catalog; never embed content."""
import fnmatch, hashlib, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/_meta/rag-manifest.jsonl'

def ignored(path):
    rules = (ROOT / '.ragignore').read_text(encoding='utf-8').splitlines()
    result = False
    for raw in rules:
        raw = raw.strip()
        if not raw or raw.startswith('#'): continue
        negate = raw.startswith('!')
        rule = raw[1:] if negate else raw
        anchored = rule.startswith('/')
        rule = rule.lstrip('/')
        directory = rule.endswith('/')
        rule = rule.rstrip('/')
        parts = path.split('/')
        matches = (any(fnmatch.fnmatchcase('/'.join(parts[:i]), rule) or fnmatch.fnmatchcase(parts[i-1], rule) for i in range(1, len(parts)+1)) if directory else fnmatch.fnmatchcase(path, rule) or (not anchored and '/' not in rule and any(fnmatch.fnmatchcase(p, rule) for p in parts)))
        if matches: result = not negate
    return result

def main():
    tracked = subprocess.check_output(['git', 'ls-files', '--cached', '-z'], cwd=ROOT).decode().split('\0')
    records = []
    for name in sorted(set(tracked)):
        if not name.lower().endswith('.md') or ignored(name): continue
        path = ROOT / name
        if not path.is_file() or path.is_symlink(): continue
        data = path.read_text(encoding='utf-8')
        front = data.split('---', 2)[1] if data.startswith('---\n') and data.count('---') >= 2 else ''
        if re.search(r'(?im)^sensitivity:\s*["\']?secret\b', front): continue
        lang = re.search(r'(?im)^lang:\s*["\']?([\w-]+)', front)
        sensitivity = re.search(r'(?im)^sensitivity:\s*["\']?([\w-]+)', front)
        tag = re.search(r'(?im)^tags:\s*\[([^\]]*)\]', front)
        tags = [x.strip().strip('"\'') for x in tag.group(1).split(',') if x.strip()] if tag else []
        sha = hashlib.sha256(data.encode()).hexdigest()[:8]
        headings = [(i, m.group(2).strip()) for i, line in enumerate(data.splitlines(), 1) if (m := re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', line))]
        if not headings: headings = [(1, path.stem)]
        for line, heading in headings:
            ident = hashlib.sha256(f'{name}:{line}:{heading}'.encode()).hexdigest()[:16]
            records.append(dict(id=ident, path=name, heading=heading, sha8=sha, tags=tags, lang=lang.group(1) if lang else 'und', sensitivity=sensitivity.group(1) if sensitivity else 'internal'))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True)+'\n' for r in records), encoding='utf-8')
    print(f'{len(records)} chunks')
if __name__ == '__main__': main()
