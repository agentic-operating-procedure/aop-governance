#!/usr/bin/env python3
"""Canonical AOP estate changelog utility.

Commands:
    changelog.py add <repo> <version> <date> <entry-file>
    changelog.py verify <repo>

The authoritative source is maintained in aop-governance. Estate consumers
must pin this file to an immutable governance commit and verify its SHA-256
digest before execution. See tools/CHANGELOG-VERIFIER.md.
"""
import re
import sys
from pathlib import Path


def parse(text):
    return re.findall(r'^## \\[(Unreleased|v?\\d+\\.\\d+\\.\\d+)\\]', text, re.M)


def norm(version):
    return version.lstrip("v")


def load(repo):
    return Path(repo, "CHANGELOG.md").read_text(encoding="utf-8")


def readme_version(repo):
    match = re.search(
        r'^\\|\\s*Version\\s*\\|\\s*(\\S+)\\s*\\|',
        Path(repo, "README.md").read_text(encoding="utf-8"),
        re.M,
    )
    return match.group(1) if match else None


def verify(repo, quiet=False):
    text, problems = load(repo), []
    headings = parse(text)
    if headings.count("Unreleased") != 1:
        problems.append(
            "expected exactly one [Unreleased] heading, found %d"
            % headings.count("Unreleased")
        )
    elif headings[0] != "Unreleased":
        problems.append("[Unreleased] is not the first section")

    releases = [heading for heading in headings if heading != "Unreleased"]

    def version_key(version):
        return tuple(int(part) for part in norm(version).split("."))

    if releases != sorted(releases, key=version_key, reverse=True):
        problems.append(
            "release sections are not in descending order: %s" % releases
        )

    refs = set(
        re.findall(r'^\\[(v?[0-9]+\\.[0-9]+\\.[0-9]+|Unreleased)\\]:', text, re.M)
    )
    for heading in releases:
        if heading not in refs and norm(heading) not in refs:
            problems.append("section [%s] has no link reference" % heading)

    if releases and "Unreleased" not in refs:
        problems.append("section [Unreleased] has no link reference")

    for ref in refs:
        if ref != "Unreleased" and ref not in releases and norm(ref) not in [
            norm(release) for release in releases
        ]:
            problems.append("dangling link reference [%s]" % ref)

    duplicates = [heading for heading in set(releases) if releases.count(heading) > 1]
    if duplicates:
        problems.append("duplicate release sections: %s" % duplicates)

    readme = readme_version(repo)
    if releases and readme and norm(releases[0]) != norm(readme):
        problems.append(
            "README Version %s != newest release %s" % (readme, releases[0])
        )

    if not quiet:
        for problem in problems:
            print("  FAIL %s: %s" % (Path(repo).name, problem))
    return not problems


def add(repo, version, date, entry_file):
    if not verify(repo, quiet=True):
        sys.exit(
            "refusing to add: %s/CHANGELOG.md is structurally broken; "
            "repair it first (run verify)" % repo
        )

    text = load(repo)
    version = norm(version)
    if version in [norm(heading) for heading in parse(text)]:
        sys.exit("refusing to add: version %s already has a section" % version)

    entry = Path(entry_file).read_text(encoding="utf-8").strip("\\n")
    previous = [heading for heading in parse(text) if heading != "Unreleased"]
    previous_version = norm(previous[0]) if previous else None
    slug = Path(repo).name

    text = text.replace(
        "## [Unreleased]\\n",
        "## [Unreleased]\\n\\n## [%s] - %s\\n\\n%s\\n"
        % (version, date, entry),
        1,
    )
    text = re.sub(
        r'^\\[Unreleased\\]: .*$',
        "[Unreleased]: https://github.com/agentic-operating-procedure/%s/compare/v%s...HEAD"
        % (slug, version),
        text,
        flags=re.M,
    )

    if previous_version is None:
        new_reference = (
            "[%s]: https://github.com/agentic-operating-procedure/%s/releases/tag/v%s"
            % (version, slug, version)
        )
    else:
        new_reference = (
            "[%s]: https://github.com/agentic-operating-procedure/%s/compare/v%s...v%s"
            % (version, slug, previous_version, version)
        )

    text = re.sub(r'^\\[v(\\d+\\.\\d+\\.\\d+)\\]:', r'[\\1]:', text, flags=re.M)
    text = text.rstrip("\\n") + "\\n" + new_reference + "\\n"
    Path(repo, "CHANGELOG.md").write_text(text, encoding="utf-8")

    readme_path = Path(repo, "README.md")
    readme = readme_path.read_text(encoding="utf-8")
    updated_readme = re.sub(
        r'^(\\|\\s*Version\\s*\\|\\s*)\\S+(\\s*\\|)',
        r'\\g<1>%s\\g<2>' % version,
        readme,
        count=1,
        flags=re.M,
    )
    if updated_readme != readme:
        readme_path.write_text(updated_readme, encoding="utf-8")

    valid = verify(repo)
    print(
        "%s %s: added [%s]; structure %s"
        % (
            Path(repo).name,
            "OK" if valid else "BROKEN",
            version,
            "verified" if valid else "FAILED",
        )
    )
    return 0 if valid else 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage: changelog.py verify <repo> | add <repo> <version> <date> <entry-file>")
    command = sys.argv[1]
    if command == "verify":
        failures = 0
        for repository in sys.argv[2:]:
            if not verify(repository):
                failures += 1
        sys.exit(1 if failures else 0)
    elif command == "add":
        if len(sys.argv) != 6:
            sys.exit("usage: changelog.py add <repo> <version> <date> <entry-file>")
        sys.exit(add(*sys.argv[2:6]))
    else:
        sys.exit("unknown command: %s" % command)
