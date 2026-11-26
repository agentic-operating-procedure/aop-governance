# CR-042: Reconcile Governance State and Restore Estate Integrity Controls

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-26 |
| Owner | Emmanuel A. Otchere |
| Layer | Governance |
| Depends on | FND-001 (merged); CR-034 to CR-041 (reconciliation subjects) |

## 1. Problem statement

The AOP programme's governance records, repository boundaries, release evidence and automated integrity controls no longer provide one consistent and executable account of the programme.

FND-001 established that CR-034 to CR-039 have merged governance records and differing levels of implementation evidence, while their lifecycle states remain unresolved; CR-040 is referenced but has no record in the current CR directory; the `site` repository is not classified against the fourteen-repository estate; and governance README, register, changelog and site claims are stale.

A deeper post-FND-001 verification found that all thirteen versioned repositories in the formal estate have a Git tag matching their current changelog version, but the latest `verify-changelog` workflow runs failed in twelve repositories. In the inspected `aop-foundations` run, the failure occurred while fetching the shared verifier from `site`; the verification step was skipped. The governance repository's latest run passed. Therefore the existence of tags and workflow files does not establish a working estate-wide verification control.

The programme also lacks a single automated integrity gate that reconciles CR files with register entries and statuses, validates dependencies, checks repository inventory claims, and prevents stale governance summaries from being published.

## 2. Objective

Restore a verifiable governance baseline in which:

1. Every CR from CR-034 onward has a recoverable record, an evidence-backed lifecycle disposition, resolved dependencies and a register entry consistent with its source record.
2. CR-040 is recovered from provenance if possible; otherwise a retrospective reconstruction is explicitly labelled as such and does not invent historical approval, authorship or implementation evidence.
3. The `site` repository has an explicit and accepted authority boundary relative to the fourteen-repository core estate.
4. The changelog verifier is maintained by an authoritative AOP repository and consumed by immutable, integrity-checked references rather than a mutable `site/main` URL.
5. The changelog and governance workflows execute successfully across the formal estate.
6. Governance CI detects missing or duplicate CR records, file/register status drift, unresolved CR dependencies, stale CR-range claims, inconsistent repository inventory and release/tag mismatches.
7. Public governance and site claims accurately distinguish implemented controls, failed or unverified controls, synthetic demonstrations and operational evidence.

## 3. Scope

### 3.1 Governance records

- `change-requests/CR-034` through `CR-041`, `docs/cr-register.md`, `README.md`, `CHANGELOG.md`, `docs/change-model.md`, the repository map and the relevant ADR set.
- Add the missing CR-040 record only after a provenance search. If the original cannot be recovered, create a retrospective reconstruction with explicit evidence, uncertainty and approval fields.
- Reconcile CR states against both implementation evidence and the programme's approval requirements. A merged proposal or an implementation claim in a CR is not, by itself, proof of acceptance.
- Introduce a lifecycle disposition for partial implementation. Use it only where an accepted CR has some, but not all, acceptance criteria satisfied. Do not use it to bypass the programme-owner approval requirement.
- Correct the CR-036 implementation version reference to the version evidenced by the aop-examples changelog, after checking the corresponding tag and artefacts.
- Keep CR-041 Proposed unless it is separately accepted through the change model.

### 3.2 Repository authority and site boundary

- Adopt or supersede ADR-0011 to classify `agentic-operating-procedure/site` as a programme publication and interactive experience surface outside the fourteen-repository core authority estate.
- State that the site may publish, visualise and demonstrate authoritative artefacts, but does not create or override normative AOP definitions, specification clauses, schemas, runtime policy or conformance results.
- Record the site's upstream dependencies, publication responsibilities, tool ownership, versioning and cascade obligations in the repository map.
- Do not silently expand ADR-0001's fourteen-repository estate. Any future promotion of the site into the core estate requires a separate structural CR.

### 3.3 Verification tooling and CI

- Move the authoritative changelog verification utility from the site-owned dependency path into `aop-governance`, which owns the programme-wide change and release policy.
- Publish the verifier through an immutable commit or release reference and pin every consumer to that reference. Include a digest or equivalent integrity check.
- Update the thirteen versioned repositories' workflows and any site workflow that consumes the verifier.
- Establish a governance integrity verifier covering:
  - CR file existence, unique identifiers and register coverage;
  - CR status agreement between source record and register;
  - dependency resolution and cycle detection;
  - valid lifecycle states and partial-implementation semantics;
  - README and changelog CR-range agreement;
  - repository inventory agreement with ADR-0001 and the accepted site-boundary decision;
  - release heading, README version and Git tag agreement;
  - explicit, evidence-backed implementation claims.
- Ensure workflow failures are visible and fail closed. A failed fetch, skipped verifier or unavailable dependency must not be reported as a passing integrity check.

### 3.4 Publication and claims

- Reconcile the governance README and changelog with the actual register and merged changes.
- Reconcile the site homepage and repository inventory with the accepted site-boundary decision.
- Narrow or substantiate the site parity claims. A validator fixture test must not be represented as guardrail/reference-harness parity unless the guardrail decisions are actually compared against the reference implementation.
- Preserve the distinction between schema validity, semantic validity, authority validity, execution evidence, outcome verification and attributable organisational value.

## 4. Acceptance criteria

### A. CR lifecycle and provenance

- Every CR-034 to CR-041 record has been checked against its acceptance criteria, implementation PRs, changed files, releases, tags, tests and required approval evidence.
- The CR register and each CR's status field agree.
- No CR is marked Implemented solely because its proposal PR merged or because its own implementation section asserts completion.
- The missing CR-040 record is either recovered with provenance or reconstructed retrospectively with uncertainty explicitly stated; no historical approval is fabricated.
- Partial implementation is represented by a defined lifecycle state and cannot be confused with Accepted or Implemented.
- CR-041 remains Proposed unless separately accepted.

### B. Repository boundary

- ADR-0011 is accepted or superseded by a new accepted ADR.
- The repository map, README and organisation inventory distinguish the fourteen-repository core estate from the site publication/interaction surface.
- The site authority statement explicitly prohibits normative or conformance authority from being inferred from publication or browser-side implementation.

### C. Verification controls

- The authoritative verifier is hosted in `aop-governance` and every consumer uses an immutable, integrity-checked reference.
- All thirteen versioned repositories execute the verifier successfully on their default branch.
- A deliberate negative test proves that a missing CR file, status mismatch, unresolved dependency, stale repository count and release/tag mismatch each fail the appropriate gate.
- The workflow reports distinguish a verifier pass from a fetch, setup or dependency failure.
- The site parity claim is either backed by a reproducible guardrail-to-reference-harness comparison or narrowed to the tests actually executed.

### D. Governance publication

- Governance README, register and changelog agree on the CR range and current lifecycle state.
- Site publication pages agree with the accepted estate boundary and do not overstate verification coverage.
- The changelog records the implementation of this CR only after its acceptance criteria have been met.

## 5. Cascade audit

| Area | Outcome |
|---|---|
| A1-A4: Governance and repository map | IN SCOPE: CR lifecycle, register, README, changelog, change model, ADR and map are reconciled |
| A5-A10: Foundations, landscape and public profile | IN SCOPE, no conceptual change: public statements must remain aligned with the accepted site and estate boundary |
| B1-B8: Specification | IN SCOPE, no normative clause or schema change; specification remains authoritative |
| C1-C7: Architecture | IN SCOPE: tool trust boundary and publication/runtime separation are documented; no execution architecture redesign |
| D1-D5: Context Graph | N/A: no context model or observation semantics change |
| E1-E6: Tooling | IN SCOPE: verifier ownership, immutable dependency and governance-integrity checks |
| F1-F*: Runtime | IN SCOPE, no runtime policy or harness behaviour change |
| G-H: Registry and assurance | IN SCOPE, no registry or conformance authority transfer |
| I-J: Evaluation and adoption | IN SCOPE, no evaluation claims are upgraded; evidence boundaries are clarified |
| K1-K2: Examples and publication | IN SCOPE: published claims and parity evidence are corrected |
| L1-L8: Programme integrity | IN SCOPE: records, dependencies, versioning, evidence and cascade traceability are verified |

## 6. What this CR is not

- It is not a change to the eight AOP dimensions, the six-level conceptual model or the normative AOP schema.
- It is not acceptance or implementation of CR-041.
- It is not permission for the site repository to become a competing specification, validator or runtime authority.
- It is not a claim that all historical CRs were properly approved. Missing approval evidence must remain visible.
- It is not the full cross-repository knowledge architecture and outcome traceability redesign. That work should be proposed separately after this governance baseline is restored.
- It does not authorise changes to Zero-TAF or any other sibling programme.

## 7. Implementation evidence and disposition

This section is completed during implementation. Each reconciled CR must cite its source PRs, commits, tags, tests and approval record. A status change requires evidence and the programme-owner decision required by the change model.

Initial verification evidence, 2026-11-26:

- FND-001 merged as governance PR #25, merge commit `7007a71967561eb28126597b7e0d08c84d5ee2fc`.
- Current version tags were confirmed for all thirteen versioned core repositories.
- Latest `verify-changelog` runs failed in twelve repositories; the inspected aop-foundations run failed while fetching the site-hosted verifier, and the verifier step was skipped.
- The latest aop-governance `verify-changelog` run passed.
- CR-040 file was not found in the current `change-requests/` directory.
- CR-035 point 3 remains incompletely documented in the current aop-spec mapping; the mapping says the Stage 01 decision “should be cited” rather than recording the completed reconciliation.
- CR-036 implementation is recorded in aop-examples v0.4.0, while the CR still says v0.3.1.

These observations are baseline evidence, not proof that the acceptance criteria of this CR have been met.
