# CR-040: Retrospective Reconstruction of the Site Repository and Changelog Verification Tooling

| Field | Value |
|---|---|
| Status | Proposed |
| Record type | Retrospective reconstruction; not the recovered original CR |
| Reconstruction date | 2026-11-26 |
| Original date | Unknown; not recoverable from the evidence reviewed |
| Original author / approver | Unknown; not recoverable from the evidence reviewed |
| Retrospective recorder | Programme governance reconciliation |
| Layer | Governance tooling / publication surface |
| Depends on | ADR-0001; CR-039; CR-042 |

## 1. Provenance notice

This record restores the missing CR-040 identifier in the current governance register. It is not represented as the original CR-040, and it does not establish the original author, date, scope, approval, implementation decision or merge history. No historical approval is inferred from the existence of the `site` repository or from CR-039's later reference to it.

The original CR-040 file is absent from the current `change-requests/` directory. FND-001 records that no CR-040 commit was found in the scoped commit search. The available evidence supports only a narrow retrospective description of the site repository and its changelog verification tool.

## 2. Reconstructed purpose (limited to evidenced facts)

The available records indicate that a repository named `agentic-operating-procedure/site` was created to host the programme's publication and interactive experience surface. CR-039 explicitly refers to CR-040 as the record for creating the site repository and its changelog tool. The current site repository contains `tools/changelog.py`, and CR-039 states that the estate's `verify-changelog` workflows fetch that tool.

The current site has since accumulated additional publication, synchronisation, interactive validator/guardrail and parity functionality. This reconstruction does not assert that all current site capabilities belonged to the original CR-040 scope.

## 3. Evidence available

- [CR-039](./CR-039-repair-version-records-and-guard.md) identifies CR-040 as the record for creating the site repository and changelog verifier.
- [FND-001](../findings/FND-001-aop-governance-knowledge-and-tooling-integrity.md) records the missing original CR file and the absence of a recovered CR-040 commit in the scoped search.
- [Site repository](https://github.com/agentic-operating-procedure/site) currently contains [tools/changelog.py](https://github.com/agentic-operating-procedure/site/blob/main/tools/changelog.py).
- The site README describes the publication, interactive tooling, estate synchronisation and shared changelog-verification roles. Those are current-state facts, not proof of original scope or approval.
- CR-039's merged governance record relies on the site-hosted verifier.

## 4. Reconstructed change boundary

This retrospective record documents only the minimum historical relationship needed to explain the extant repository and the later CR-039 dependency:

1. A site repository exists as a programme publication and interactive experience surface.
2. The site repository contains the changelog verification utility consumed by the estate's workflows.
3. The site repository is additional to the fourteen-repository estate defined by ADR-0001; this record does not amend that ADR or establish a new core-estate tier.

The site's normative authority boundary is not decided here. That is the subject of ADR-0011 and CR-042.

## 5. Acceptance criteria for this retrospective record

- The record is clearly labelled as a retrospective reconstruction, not an original recovered CR.
- Unknown original provenance fields remain explicitly unknown.
- Every reconstructed statement is traceable to extant repository artefacts or CR-039.
- No original approval, date, author, merge or broader scope is invented.
- The CR register links this record and preserves its Proposed status pending programme-owner review.

## 6. What this record does not establish

- It does not prove when or by whom the site repository was created.
- It does not prove that the original site creation was approved through the CR process.
- It does not ratify ADR-0011 or decide the site's present authority boundary.
- It does not establish that the current site feature set was part of the original CR-040.
- It does not validate CR-039's current CI implementation or make the mutable verifier dependency acceptable.

## 7. Reconciliation status

Proposed retrospective reconstruction. The programme owner must decide whether this reconstruction is an acceptable governance record for the missing identifier, whether additional historical evidence exists outside the scoped repository history, and whether the site repository's present scope should be recorded solely through ADR-0011 and CR-042.