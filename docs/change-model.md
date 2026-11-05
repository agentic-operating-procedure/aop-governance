# Change Model: Decision, Change Request, Finding

| Field | Value |
|---|---|
| Version | 0.1.1 |
| Status | Stable |
| Owner | Emmanuel A. Otchere |
| Authority | `aop-governance` |

This document defines the three artefact classes through which the programme changes, the lifecycle states they pass through, and who decides.

## 1. Why three classes

A programme that changes needs to distinguish between a decision, a proposal, and an investigation. Conflating them is how programmes end up with a log of discussions that nobody can audit. Each class answers a different question and has a different approver.

## 2. Architectural decision record (ADR)

**Answers:** what was decided, and why.

An ADR is immutable once accepted. Superseding a ratified decision creates a new ADR that references the one it replaces. An ADR is never edited to reflect a later change of mind.

| Attribute | Rule |
|---|---|
| Location | `decisions/` |
| Naming | `ADR-NNNN-short-title.md` |
| Statuses | Proposed, Accepted, Superseded |
| Approver | Programme owner |
| Landing condition | The record merges, and the decision takes effect on that merge |

## 3. Change request (CR)

**Answers:** a proposed change to the estate, the model, or a published artefact.

A CR is the mechanism through which the estate changes shape. Repository creation, retirement, renaming, and tier reassignment are CRs, not direct edits.

| Attribute | Rule |
|---|---|
| Location | `change-requests/` |
| Naming | `CR-NNN-short-title.md` |
| Statuses | Proposed, Accepted, Implemented, Superseded, Rejected |
| Approver | Programme owner |
| Landing condition | The implementing record merges and the CR is marked Implemented |

A CR for the estate carries a cascade audit against `plans/aop-org-cascade-checklist-org-scope.md`, and states the items it deliberately does not change.

From the reviewer-independence layer (2026-11-05): a normative CR records review from at least one implementer or domain reviewer outside the authoring path (GI-1), with conflicts declared (GI-2) and dissent recorded where it exists (GI-5). The programme owner's approval remains the decision; the independent review is the second recorded approval (GI-4). See `docs/reviewer-independence-and-claims-discipline-governance-scope.md`.

## 4. Finding (FND)

**Answers:** what an investigation found, and what evidence supports it.

A finding is the record of a reconnaissance, a test, a comparison, or an audit. Findings are how the programme distinguishes what it has verified from what it has asserted.

| Attribute | Rule |
|---|---|
| Location | `findings/` |
| Naming | `FND-NNN-short-title.md` |
| Statuses | Open, Closed, Superseded |
| Approver | Programme owner |
| Landing condition | The finding record merges |

## 5. Lifecycle states

Programme artefacts move through one ladder. The five lifecycle labels on every repository in the estate name the stage of an artefact, never the stage of the repository.

| State | Meaning |
|---|---|
| `research-proposal` | Hypothesis stated, method described, no data collected |
| `draft-spec` | Normative content in drafting, open for comment |
| `release-candidate` | Content frozen, awaiting final acceptance review |
| `stable` | Versioned, governed, released |
| `deprecated` | Superseded, with a shim naming the successor |

A label classifies the lifecycle stage of an artefact. It is not a verification claim. Whether an artefact has been independently verified is a separate question, answered by the conformance and evaluation surfaces of the estate.

## 6. Decision rights

| Change | Decided by | Recorded as |
|---|---|---|
| The definition of the concept | Programme owner | ADR |
| The normative model | Programme owner | ADR, then CR |
| The shape of the estate | Programme owner | CR |
| The scope of a repository | Owner of that repository | CR in this repository |
| The content of a repository | Owner of that repository | Record in that repository |

## 7. Release policy

- A repository releases on a semantic version. The major version moves when an authority boundary moves. The minor version moves when normative content is added. The patch version moves for corrections that do not change meaning.
- The release note is the changelog entry. The changelog is the release history. Both live in the repository that released.
- A normative artefact reaches `stable` only after it has cleared the governance review window and an acceptance record has merged.
- A deprecated artefact carries a one-paragraph shim that names its successor. A bare deprecation is debt.

## 8. What a change does not need

Not every edit is a CR. A typo fix, a broken link, a formatting correction, and a changelog update are patches to the repository that holds the artefact. Anything that changes meaning, scope, boundary, or structure is a record.
