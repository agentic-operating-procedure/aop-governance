# CR-039: Repair the Estate's Version Records and Guard Them in CI

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-24 |
| Owner | Emmanuel A. Otchere |
| Layer | Estate |
| Depends on | CR-038 (merged) |

## 1. Problem statement

An audit of all 13 versioned repositories found that 9 carried defective version records, caused by a defective release-bump script used during the hardening waves: its string replacement was a no-op once a repository's `## [Unreleased]` heading was absent, so release entries were silently skipped while README version rows and link references were still updated. The defect classes: four lost release entries in `aop-spec` (0.3.0 to 0.6.0), two lost in `aop-evaluation` (0.2.0, 0.3.0), one duplicate section in `aop-toolkit`, missing link references in six repositories, v-prefixed heading inconsistencies, committed `__pycache__` artefacts in `aop-spec`, and no git tags on any repository despite every changelog link referencing tags. Separately, `aop-governance` carried 39 change requests of content with no release record at all.

## 2. Objective

Repair every defective record from commit evidence, create the missing tags, record governance's first release, and guard the record with CI so the defect class cannot recur.

## 3. Scope

All 14 repositories. The repair content:

- `aop-spec`: the four lost release entries rebuilt from the actual commit diffs (0.3.0 trust classes and ratification gate; 0.4.0 run/action semantics and replay levels; 0.5.0 approval object, parameters, revocation, entity register; 0.6.0 attestation, identity, erasure, migration, points 3 and 4 dispositions), structure restored, pyc caches removed and ignored.
- `aop-evaluation`: the two lost entries rebuilt (0.2.0 origin filtering; 0.3.0 the independent evaluation protocol and cohort module).
- `aop-toolkit`: the byte-identical duplicate 0.2.0 section removed; its date corrected to the landing date (2026-11-04).
- Six repositories: link references rebuilt; v-prefixed headings normalised.
- `aop-governance`: release 0.2.0 recorded (the independence layer, the register, the reconciliation closures, CR-038, the plan addendum).
- All 14 repositories: the current version tagged on origin (v0.1.0 to v0.6.0), and a `verify-changelog` workflow that checks structure and README agreement on every PR and push. The verification tool lives in the site repository (`site/tools/changelog.py`) and is fetched read-only by the workflows.

## 4. Acceptance criteria

- The verification tool reports zero structural failures across all 13 versioned repositories.
- README version rows agree with the newest release section everywhere.
- Every release section has a matching link reference; no dangling references; no duplicates; exactly one `[Unreleased]` per file, first.
- Tags exist on origin for every repository's current version.
- The workflows run on every PR and push.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A3 | IN SCOPE, no change: the phase gates are untouched |
| A4 | IN SCOPE, no change: the ladder is unchanged |
| A5 to A10 | IN SCOPE, no change: concept, glossary, non-goals, positioning, public description and repository set unchanged |
| B1 to B8 | IN SCOPE, no change: no clause, schema or validator text changes; the records describe the same landed content |
| C1 to D5 | N/A or no change |
| E6 | IN SCOPE, no change: the toolkit SDK surface unchanged; records only |
| F to K | N/A or no change |
| L1 | IN SCOPE: met |
| L4 | IN SCOPE: strengthened; the compare links now resolve to real tags |
| L7, L8 | IN SCOPE: the register and plan addendum already describe the landed content; this CR repairs the per-repo records |

## 6. What this CR is not

It is not a content change: every restored entry describes content that already landed and was verified at landing time; only the record was missing. It is not a re-versioning: no version number changes meaning; the numbers now match the record. It is not retroactive tagging of every historical version: only current versions are tagged; the older compare links resolve against tags as they are progressively created.

## 7. Implementation

Implemented across all 14 repositories. The verification tool is `site/tools/changelog.py` (created with the site repository, CR-040) and the workflows reference it by raw URL.
