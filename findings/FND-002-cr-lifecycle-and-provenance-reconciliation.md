# FND-002: CR Lifecycle and Provenance Reconciliation

| Field | Value |
|---|---|
| Status | Open |
| Date | 2026-11-26 |
| Scope | AOP governance CR-034 to CR-040; associated implementation evidence in aop-spec, aop-examples and site |
| Parent | FND-001; CR-042 |
| Purpose | Reconcile recorded CR lifecycle states against merged governance records, owning-repository artefacts, release records and available verification evidence |

## 1. Finding

The CR-034 to CR-040 register entries were not a reliable lifecycle ledger. Some changes are implemented and supported by merged records and current owning-repository artefacts; one is only partially reflected in the authoritative specification; one is partially implemented but its CI acceptance criterion is not met; and CR-040's original governance record is missing.

This reconciliation distinguishes:
- a proposal-record PR from an implementation record;
- source artefacts present on the default branch from a passing test run;
- a release/changelog assertion from independently reproduced execution evidence;
- a retrospective reconstruction from recovery of an original historical record.

No conclusion in this finding treats a merged proposal-only PR as implementation evidence.

## 2. Evidence method and limits

The review inspected the current governance CR files and register, merged PR metadata and changed-file lists, the current aop-spec mapping and changelog, the aop-examples generator, mixed-origin corpus, manifests, changelog and reproduction gate, the site changelog verifier, and the earlier FND-001 / CR-042 evidence.

PR merge metadata and changed-file lists were checked directly. Owning-repository source and changelog artefacts were inspected on their current default branches. Historical gate output was not independently replayed during this reconciliation. Where a prior PR body or changelog reports a passing test, this finding identifies it as a recorded result rather than a fresh run.

## 3. CR-by-CR reconciliation

| CR | Merged governance record | Current implementation evidence | Reconciled disposition |
|---|---|---|---|
| CR-034 | [PR #17](https://github.com/agentic-operating-procedure/aop-governance/pull/17), merge `a974cd3ddf30dbae73667e90dac6b563279f8edf`; five changed governance files | The PR changed the CR, register, README, change model and programme plan addendum. The stated acceptance criteria are represented in those merged artefacts. | Implemented. CR file status corrected from Proposed. |
| CR-035 | [PR #18](https://github.com/agentic-operating-procedure/aop-governance/pull/18), merge `e96e588f1418fce76aa434e3ffee63a38ef1d6bb`; CR record only | Current aop-spec mapping resolves point 4. Point 3 still says the Stage 01 decision "should be cited". The aop-spec 0.6.0 changelog says both points are closed, so the authoritative mapping does not meet the CR's point-3 acceptance criterion. | Proposed; partially evidenced. Point 3 must be completed before implementation can be accepted. |
| CR-036 | [PR #19](https://github.com/agentic-operating-procedure/aop-governance/pull/19), merge `75b98658a47857f02f4df5352f22eb12ef938256`; CR record only | The aop-examples generator emits `origin` and `--agent-fraction`; the mixed-origin corpus and held-out artefacts exist. The v0.4.0 changelog records the CR-036 work. The CR's v0.3.1 implementation reference is incorrect. PR #19 and the changelog report the 13-case exclusion and passing reproduction gate. | Implemented; correct the implementation version to v0.4.0. Historical gate result is recorded, not freshly replayed here. |
| CR-037 | [PR #20](https://github.com/agentic-operating-procedure/aop-governance/pull/20), merge `7b1464520e9f7673543623646cb8848d5804fac5`; CR record only | The aop-examples v0.4.0 changelog records five canonical metric bindings, the process contribution's accepted-but-unassigned state, recompiled AOPs, and passing lint, adapter self-test and reproduction gate. Current manifests contain the canonical metric identifiers. | Implemented. The pending process entity assignment is explicitly outside this CR's completion criteria. Historical test outputs are not freshly replayed here. |
| CR-038 | [PR #22](https://github.com/agentic-operating-procedure/aop-governance/pull/22), merge `4ececd6329f6775c44820736065eaa90f532ace3`; CR, register and repository map changed | The repository map records the one-way Zero-TAF/AOP relationship; the register already says Implemented; FND-001 records the reciprocal Zero-TAF ADR-ZTAF-0006. | Implemented. CR file status corrected to agree with the merged record and register. |
| CR-039 | [PR #23](https://github.com/agentic-operating-procedure/aop-governance/pull/23), merge `e1f594e262dcdad583290abaaad141b8da84c742`; CR record only | The verifier exists in site; workflows exist in the thirteen formal repositories; current version tags were confirmed during CR-042 preparation. However, the latest verifier runs failed in twelve repositories and passed in governance only. The inspected aop-foundations run failed while fetching the shared verifier and skipped verification. | Proposed; partially implemented, acceptance not met. Requires verifier relocation/pinning and successful estate-wide execution. |
| CR-040 | No original CR file or recovered CR-040 commit found in the scoped investigation recorded by FND-001 | CR-039 names CR-040 as the site-repository and changelog-tool creation record. The site repository and `tools/changelog.py` exist today. Current site capabilities do not establish original scope, author, date or approval. | Retrospective reconstruction added as Proposed. Original provenance remains unknown; this is not represented as recovery of the original CR. |

CR-041 remains Proposed and is not part of this lifecycle disposition. CR-042 remains the parent remediation proposal and is not implemented by this finding.

## 4. Evidence register

### 4.1 Governance PR records

- CR-034: [PR #17](https://github.com/agentic-operating-procedure/aop-governance/pull/17), merge commit `a974cd3ddf30dbae73667e90dac6b563279f8edf`; changed files: README, CR-034, change model, CR register, programme plan addendum.
- CR-035: [PR #18](https://github.com/agentic-operating-procedure/aop-governance/pull/18), merge commit `e96e588f1418fce76aa434e3ffee63a38ef1d6bb`; changed file: CR-035 only.
- CR-036: [PR #19](https://github.com/agentic-operating-procedure/aop-governance/pull/19), merge commit `75b98658a47857f02f4df5352f22eb12ef938256`; changed file: CR-036 only.
- CR-037: [PR #20](https://github.com/agentic-operating-procedure/aop-governance/pull/20), merge commit `7b1464520e9f7673543623646cb8848d5804fac5`; changed file: CR-037 only.
- CR-038: [PR #22](https://github.com/agentic-operating-procedure/aop-governance/pull/22), merge commit `4ececd6329f6775c44820736065eaa90f532ace3`; changed files: CR-038, CR register, repository map.
- CR-039: [PR #23](https://github.com/agentic-operating-procedure/aop-governance/pull/23), merge commit `e1f594e262dcdad583290abaaad141b8da84c742`; changed file: CR-039 only.

These changed-file lists matter: PRs #18, #19, #20 and #23 are governance record submissions, not owning-repository implementation PRs. Their implementation claims must be checked against the artefacts they identify.

### 4.2 Owning-repository artefacts

- [aop-spec metamodel mapping](https://github.com/agentic-operating-procedure/aop-spec/blob/main/docs/aop-metamodel-mapping-specification-scope.md): point 4 is resolved; point 3 still has prospective wording.
- [aop-spec changelog](https://github.com/agentic-operating-procedure/aop-spec/blob/main/CHANGELOG.md): v0.6.0 reports points 3 and 4 closed, creating a record-to-source inconsistency.
- [aop-examples origin generator](https://github.com/agentic-operating-procedure/aop-examples/blob/main/corpus/generate_ran_cases.py): emits `origin: human` and supports `--agent-fraction`.
- [aop-examples mixed-origin corpus](https://github.com/agentic-operating-procedure/aop-examples/blob/main/corpus/ran-mixed-origin-cases.jsonl): published mixed-origin sample.
- [aop-examples v0.4.0 changelog](https://github.com/agentic-operating-procedure/aop-examples/blob/main/CHANGELOG.md): records both CR-036 and CR-037 implementation under v0.4.0.
- [aop-examples manifest](https://github.com/agentic-operating-procedure/aop-examples/blob/main/manifests/ran-anomaly.json): current source for the canonical metric and process bindings.
- [site changelog verifier](https://github.com/agentic-operating-procedure/site/blob/main/tools/changelog.py): current shared verifier source.
- [site repository README](https://github.com/agentic-operating-procedure/site/blob/main/README.md): current publication, interactive tooling and verifier role; not proof of the original CR-040 scope.

### 4.3 CI and release evidence

CR-039's current version tags were confirmed across all thirteen versioned repositories during CR-042 preparation. The latest `verify-changelog` workflow runs checked at that time failed in twelve repositories; the aop-governance run passed. The aop-foundations failure showed the site-hosted verifier fetch failing before the verifier step, which was skipped.

The tag check and workflow-file presence do not satisfy the zero-failure verifier acceptance criterion. The current shared verifier is fetched from mutable site `main`, so the dependency is not immutable. The detailed run evidence and its limits are recorded in FND-001 and CR-042.

## 5. CR-040 retrospective reconstruction decision boundary

The new CR-040 file is deliberately labelled as a retrospective reconstruction. Its reconstruction date is the date of this reconciliation. The original date, author, approver, approval decision, original scope and original implementation commit remain unknown. The reconstructed scope is limited to the minimum evidenced relationship between the site repository and the changelog verifier.

The record does not:
- claim that the original CR-040 has been recovered;
- infer approval from the existence of the repository;
- infer the original site scope from the current feature set;
- add site to the fourteen-repository core estate; or
- ratify ADR-0011.

The programme owner must decide whether the retrospective record is acceptable or whether additional historical evidence should be sought.

## 6. Unresolved decisions and required follow-up

1. **CR-035:** complete point 3 in the aop-spec mapping, then reconcile its changelog statement and run the relevant documentation/specimen checks.
2. **CR-039:** relocate the authoritative verifier into governance, pin consumers to an immutable revision with integrity verification, repair the fetch path, and demonstrate passing runs across all thirteen versioned repositories.
3. **CR-040:** accept or amend the retrospective reconstruction; preserve unknown original provenance fields unless new evidence is found.
4. **CR-036 / CR-037:** retain the v0.4.0 implementation reference. If independent reproduction is required for historical test claims, rerun the relevant gates in a pinned environment and attach output; do not describe that as having happened in this reconciliation.
5. **CR-034 / CR-038:** the merged implementation records and source artefacts support Implemented; their CR-file statuses and register rows are reconciled accordingly.
6. **Lifecycle model:** CR-039 demonstrates the need for a formally defined partial-implementation disposition. This finding does not add a new lifecycle state; CR-042 must govern that change before it is used elsewhere.

## 7. Explicit exclusions

- No change to CR-041 or its fault-management fixture.
- No changes to AOP normative clauses, schemas, architecture, runtime or tool behaviour.
- No change to ADR-0001's fourteen-repository core estate.
- No acceptance of ADR-0011.
- No claim that synthetic corpus results represent live operational performance.
- No claim that a passing changelog structure check establishes AOP conformance, execution validity, outcome achievement or attributable enterprise value.

## 8. Closure criteria

FND-002 remains Open until:
- the programme owner reviews the CR-040 retrospective reconstruction;
- CR-035's point-3 inconsistency is corrected or formally dispositioned;
- CR-039's CI acceptance gap is tracked to the relevant remediation and evidence;
- CR register rows agree with the CR file statuses and linked implementation evidence; and
- no unresolved historical approval is represented as known.
