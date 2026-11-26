#!/usr/bin/env python3
"""The AOP estate's canonical changelog tool.

    changelog.py add <repo> <version> <date> <entry-file>
    changelog.py verify <repo>

The authoritative source is maintained in aop-governance. Estate consumers
must pin this file to an immutable governance commit and verify its SHA-256
digest before execution. See tools/CHANGELOG-VERIFIER.md.
"""
import re, sys
from pathlib import Path

def parse(text):
    return re.findall(r'^## \[(Unreleased|v?\d+\.\d+\.\d+)\]', text, re.M)

def norm(v): return v.lstrip('v')

def load(repo):
    return Path(repo, 'CHANGELOG.md').read_text()

def readme_version(repo):
    m = re.search(r'^\|\s*Version\s*\|\s*(\S+)\s*\|', Path(repo, 'README.md').read_text(), re.M)
    return m.group(1) if m else None

def verify(repo, quiet=False):
    text, problems = load(repo), []
    heads = parse(text)
    if heads.count('Unreleased') != 1: problems.append('expected exactly one [Unreleased] heading, found %d' % heads.count('Unreleased'))
    elif heads[0] != 'Unreleased': problems.append('[Unreleased] is not the first section')
    rel = [h for h in heads if h != 'Unreleased']
    def key(v): return tuple(int(x) for x in norm(v).split('.'))
    if rel != sorted(rel, key=key, reverse=True): problems.append('release sections are not in descending order: %s' % rel)
    refs = set(re.findall(r'^\[(v?[0-9]+\.[0-9]+\.[0-9]+|Unreleased)\]:', text, re.M))
    for h in rel:
        if h not in refs and norm(h) not in refs: problems.append('section [%s] has no link reference' % h)
    if rel and 'Unreleased' not in refs: problems.append('section [Unreleased] has no link reference')
    for r in refs:
        if r != 'Unreleased' and r not in rel and norm(r) not in [norm(x) for x in rel]: problems.append('dangling link reference [%s]' % r)
    dupe = [h for h in set(rel) if rel.count(h) > 1]
    if dupe: problems.append('duplicate release sections: %s' % dupe)
    rv = readme_version(repo)
    if rel and rv and norm(rel[0]) != norm(rv): problems.append('README Version %s != newest release %s' % (rv, rel[0]))
    if not quiet:
        for p in problems: print('  FAIL %s: %s' % (Path(repo).name, p))
    return not problems

def add(repo, version, date, entry_file):
    if verify(repo, quiet=True) is False:
        sys.exit('refusing to add: %s/CHANGELOG.md is structurally broken; repair it first (run verify)' % repo)
    text = load(repo)
    version = norm(version)
    if version in [norm(h) for h in parse(text)]:
        sys.exit('refusing to add: version %s already has a section' % version)
    entry = Path(entry_file).read_text().strip('\n')
    prev = [h for h in parse(text) if h != 'Unreleased']
    prev_v = norm(prev[0]) if prev else None
    slug = Path(repo).name
    text = text.replace('## [Unreleased]\n', '## [Unreleased]\n\n## [%s] - %s\n\n%s\n' % (version, date, entry), 1)
    text = re.sub(r'^\[Unreleased\]: .*$', '[Unreleased]: https://github.com/agentic-operating-procedure/%s/compare/v%s...HEAD' % (slug, version), text, flags=re.M)
    newref = '[%s]: https://github.com/agentic-operating-procedure/%s/compare/%s' % (
        version, slug, ('v%s...v%s' % (prev_v, version)) if prev_v else ('v%s...v%s' % ('0.0.0', version)))
    if prev_v is None:
        newref = '[%s]: https://github.com/agentic-operating-procedure/%s/releases/tag/v%s' % (version, slug, version)
    else:
        newref = '[%s]: https://github.com/agentic-operating-procedure/%s/compare/v%s...v%s' % (version, slug, prev_v, version)
    text = re.sub(r'^\[v(\d+\.\d+\.\d+)\]:', r'[\1]:', text, flags=re.M)
    text = text.rstrip('\n') + '\n' + newref + '\n'
    Path(repo, 'CHANGELOG.md').write_text(text)
    rp = Path(repo, 'README.md'); r = rp.read_text()
    r2 = re.sub(r'^(\|\s*Version\s*\|\s*)\S+(\s*\|)', r'\g<1>%s\g<2>' % version, r, count=1, flags=re.M)
    if r2 != r: rp.write_text(r2)
    ok = verify(repo)
    print('%s %s: added [%s]; structure %s' % (Path(repo).name, 'OK' if ok else 'BROKEN', version, 'verified' if ok else 'FAILED'))
    return 0 if ok else 1

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'verify':
        bad = 0
        for repo in sys.argv[2:]:
            if not verify(repo): bad += 1
        sys.exit(1 if bad else 0)
    elif cmd == 'add':
        sys.exit(add(*sys.argv[2:6]))
