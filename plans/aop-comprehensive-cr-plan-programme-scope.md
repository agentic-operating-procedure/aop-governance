# AOP Comprehensive CR Plan: The Unified Change Programme (Programme Scope)

_Published as the programme's authoritative plan for the hardening and evidence programme. It reconciles the two external reviews into one numbered CR set with one sequencing._

## 1. Sources and the numbering rule

Two external reviews were provided by the programme owner:

- **Review 1** (2026-11-04, `CRs/AOP Robustness Hardening Umbrella Change Request.md`): nine items. Reconciled and filed as **CR-009** with children CR-009-1 to CR-009-9 (PR #10). Block 1 of it is landed: children 1 (trust classes), 2 (ratification gate), 4 (trust base), 9 (disambiguation and crosswalks).
- **Review 2** (2026-11-04, `CRs/aop-review-change-request-set_2.md`): eighteen items, already cross-reviewed by its author against the published repositories, with narrowed dispositions.

The estate numbering owns CR-001 to CR-008 (landed) and CR-009 (open). Review 2's numbering therefore **renumbers to estate CR-010 to CR-027**, and four of its items merge with pending CR-009 children because they describe the same work. The mapping table below is the single authority for which review item became which estate CR.

## 2. The numbering map

| Estate CR | Source | Title | Class | Priority | Depends on | State |
|---|---|---|---|---|---|---|
| CR-009 | Review 1 | Robustness hardening umbrella | Umbrella | — | CR-002..008 | Open (PR #10); children 1, 2, 4, 9 landed |
| CR-009-3 | Review 1 item 3 | Cumulative authority, budgets, delegation attenuation | Normative | P1 | CR-009 | Pending |
| CR-010 | Review 2 item 1 | Close the metamodel reconciliation | Foundational + Normative | P1 | — | New |
| CR-011 | Review 2 item 2 | Runtime action, retry, concurrency, recovery semantics | Normative + Architecture | P0 | CR-010 | New |
| CR-012 | Review 2 item 3 | Replayable evidence and reproducibility boundaries | Normative + Architecture | P0 | CR-011 | New |
| CR-013 | Review 2 item 4 + CR-009-6 | Observation data governance and loop hygiene | Normative + Architecture | P1 | CR-010 | New (merged) |
| CR-014 | Review 2 item 5 + CR-009-8 | Independent out-of-sample evaluation; earning Demonstrated | Evidence | P0 | CR-013 | New (merged) |
| CR-015 | Review 2 item 6 + CR-009-7 | Conformance expansion: adversarial, interoperability, tiers | Evidence | P1 | CR-011, CR-012 | New (merged) |
| CR-016 | Review 2 item 7 + CR-009-5 | Approval binding and oversight quality | Normative + Architecture | P1 | CR-011 | New (merged) |
| CR-017 | Review 2 item 8 | Publication, revocation, rollback, compatibility lifecycle | Normative + Architecture | P1 | CR-012 | New |
| CR-018 | Review 2 item 9 | Independent governance and claims discipline | Governance | P2 | CR-014, CR-015 | New |
| CR-019 | Review 2 item 10 | Risk-tiered adoption and promotion gates | Adoption + Evidence | P2 | CR-014 to CR-017 | New |
| CR-020 | Review 2 item 11 | Observation plane and Context Graph security | Architecture + Security | P1 | CR-013, CR-015 | New |
| CR-021 | Review 2 item 12 | Supply-chain attestation for AOPs, compiler, skills | Architecture + Security | P1 | CR-015, CR-017 | New |
| CR-022 | Review 2 item 13 | Workload identity and controlled egress | Normative + Architecture + Security | P1 | CR-015, CR-016 | New |
| CR-023 | Review 2 item 14 | Parameter-level action constraints at enforcement time | Normative | P1 | CR-011, CR-016 | New (cross-ref CR-009-3) |
| CR-024 | Review 2 item 15 | Revalidation after model, tool, or runtime changes | Normative + Evidence | P1 | CR-014, CR-015, CR-017 | New |
| CR-025 | Review 2 item 16 | Incident response and in-flight run recovery | Architecture + Normative | P1 | CR-011, CR-017 | New (extends SEC-14/15) |
| CR-026 | Review 2 item 17 | Erasure-compatible audit evidence | Normative + Architecture | P1 | CR-012, CR-013, CR-017 | New |
| CR-027 | Review 2 item 18 | Optional Pi harness adapter | Implementation + Adoption | P2 | CR-011, CR-015, CR-019 | New |

Merges, with the reasons:

- **CR-013** absorbs CR-009-6: both govern the observation-to-baseline loop (origin tagging, the human reservoir, corpus representativeness, contestability). One owner, one corpus.
- **CR-014** absorbs CR-009-8: independent held-out and prospective evaluation *is* the evidence that earns Demonstrated, including pre-registration, replication invitation and negative results.
- **CR-015** absorbs CR-009-7: the adversarial suite, fault injection, cross-implementation tests, coverage map and the settled tier vocabulary are one conformance expansion.
- **CR-016** absorbs CR-009-5: approval quality and oversight quality are one contract (binding, expiry, independence, metrics, rubber-stamp detection).

## 3. Implementation waves

Supersedes the block sequencing inside CR-009. Priorities follow review 2; dependencies may pull a CR earlier than its priority suggests.

- **Wave H1: foundational (P0)** — CR-010, CR-011, CR-012, plus CR-009-3 (carried from review 1, P1, small enough to ride along).
- **Wave H2: integrity (P1)** — CR-013, CR-016, CR-017, CR-023, CR-020.
- **Wave H3: security and lifecycle (P1)** — CR-021, CR-022, CR-024, CR-025, CR-026.
- **Wave H4: evidence (gates everything)** — CR-014 (P0), CR-015.
- **Wave H5: maturity (P2)** — CR-018, CR-019, CR-027.

## 4. What is already done, credited

Review 2's own cross-review is adopted as the reconciliation baseline: the harness relationship and eight dimensions are normative and not reopened; fail-closed and loop bounds are not re-specified; replay requirements exist and the remainder is the replay *definition*; the privacy posture and governance boundary exist and the remainder is corpus quality and contestability; profiles, fixtures and certificates exist and the remainder is breadth and interop; immutable publication, lifecycle status and provenance exist and the remainder is revocation, active runs, rollback and compatibility. To review 1's credit: trust classes, the ratification gate, the trust base (signed bundles, hold, emergency stop, T6/T7), and the disambiguation crosswalks are landed and gated.

## 5. The review outcome sought (adopted verbatim as the programme's bar)

Independent teams can interpret AOP consistently, implement its stated safety and evidence guarantees, and demonstrate useful performance on representative live work. The cross-CR review checklist from review 2 (authority, scope, unknowns, side effects, human oversight, evidence, learning, evaluation, portability, lifecycle, claims) is the standing assessment lens for every CR in this plan.

## 6. Governance

This plan is filed under the umbrella PR with the CR files CR-010 to CR-027. Each CR carries the reconciliation notes crediting existing coverage, per review 2's method. No CR in this plan reopens a settled decision: D-007 stands (regulation and guidance rows are mapped, not sourced), the specification-layer claim is evidenced, tiers are named claims over binary suites, and the metamodel reconciliation point 6 is settled.
