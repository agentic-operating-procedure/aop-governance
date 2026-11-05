# CR-034: Governance Reconciliation: The Register, the Plan Addendum and the Independence Layer

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-06 |
| Owner | Emmanuel A. Otchere |
| Layer | Governance |
| Depends on | CR-033 (merged) |

## 1. Problem statement

The governance artefacts have not caught up with the hardening programme. The programme plan ends at the original Wave 6 with no mention of the hardening waves H1 to H5 or the estate's current state; thirty-three change requests exist with no register index; and the reviewer-independence layer (GI-1 to GI-10, landed with CR-032) is not wired into the change model, so a reader of the change model alone would not know the second-approval requirement exists. The cascade's cross-artifact-consistency rule (M4) requires all four to describe the same estate.

## 2. Objective

Reconcile the governance artefacts with the landed programme: the CR register, the programme plan addendum, and the change-model wiring of the independence layer.

## 3. Scope

- `docs/cr-register.md`: the index of CR-001 to CR-033, one line each, with landing states and the honest remainders (in-progress items named, not smoothed).
- `plans/aop-programme-plan-programme-scope.md`: section 7a, the hardening-programme addendum: the wave table (H1 to H5 plus the closure CR), the estate state summary (certifications, coverage map, the held-out result), and the live-by-nature remainder list.
- `docs/change-model.md` (v0.1.1): the CR section records the independence requirement for normative CRs (GI-1, GI-2, GI-4, GI-5) with a pointer to the layer document.
- `README.md`: a change-record section indexing the three artefacts.

## 4. Acceptance criteria

- Every CR from 001 to 033 appears in the register exactly once (children of CR-009 shown as their own rows where they landed independently).
- The plan addendum states the estate's state without claiming what is not demonstrated (no live claim, no independent reproduction claimed).
- The change model states the second-approval requirement for normative CRs.
- L1 clean; gates unaffected (no code or schema change).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A2 | IN SCOPE, no change: no ADR touched; the addendum records state, it does not ratify |
| A3 | IN SCOPE: the programme plan gains the addendum without altering the original phases or gates |
| A4 to A10 | IN SCOPE, no change: the ladder, concept, glossary, non-goals, positioning, public description and repository set are unchanged |
| B to K | N/A: no specification, architecture, substrate, tooling, runtime, registry, assurance, evaluation, adoption or demonstration artefact changes |
| L1 | IN SCOPE: met (one em dash caught and fixed in the register) |
| L4 | IN SCOPE: met; the register's internal references resolve |
| L7, L8 | IN SCOPE: this CR is the reconciliation the board and project need |

## 6. What this CR is not

It is not a claims publication: the estate-state summary restates what the certificates and reports already say, under the claims-discipline rules (GI-7). It is not the exercise of the independence layer: from the next normative CR onward, the second approval is recorded per the change model; this CR is governance housekeeping, not a normative change.

## 7. Implementation

Implemented in aop-governance: the register, the plan addendum, the change-model wiring and the README index.
