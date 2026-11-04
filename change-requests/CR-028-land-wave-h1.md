# CR-028: Land Wave H1 of the Comprehensive CR Plan

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Foundational, Normative, Architecture, Assurance |
| Depends on | CR-009 (merged), CR-010 to CR-027 (filed), CR-009-3 |

## 1. Problem statement

The comprehensive CR plan sequences Wave H1 as the foundational spine: CR-010 (close the metamodel reconciliation), CR-011 (runtime action, retry, concurrency and recovery semantics), CR-012 (replayable evidence boundaries), and CR-009-3 (cumulative authority). Until these land, the P0 contracts that everything downstream depends on do not exist, and the CR-009 addendum (the comprehensive plan and CR-010 to CR-027) is stranded on the merged PR branch.

## 2. Objective

Land Wave H1: publish the CR-009 addendum on main, close reconciliation points 1, 2, 5 (in part) and 7 with the entity register and the source errata, publish the run and action semantics and the replay levels as normative text, publish the cumulative authority clauses, and implement the digest binding, retry classes, duplicate answering, budget enforcement, irreversibility verdicts and the replay module in the reference harness, with conformance fixtures.

## 3. Scope

- `aop-governance`: the CR-009 addendum landed (the comprehensive CR plan under `plans/`, the CR-010 to CR-027 files, the merge banners on children 5 to 8, the CR-009-9 decision records); this landing CR.
- `aop-spec` v0.4.0: the run and action semantics (RA-1 to RA-14), the evidence and replay semantics (RP-1 to RP-7), NM-CRD-4, NM-AUT-8, NM-AUT-9, NM-ASR-5, NM-CTL-5, CC-25; schema additions (reversibility_classes, delegation_attenuation, aggregate_limits, replay_level, context element key); validator CC-25 with the default-class fall-through check; two new must-fail fixtures (irreversible-autonomous, compensable-without-path); the metamodel entity register (reconciliation point 7, with the transcription caveat: E26 to E40 unpinned); the mapping document's corrected stage table and the dispositions for points 1, 2, 5 (in part) and 7.
- `aop-foundations` v0.1.1: the source errata document (reconciliation point 2).
- `aop-reference-harness` v0.3.0: action digests with digest-scoped credentials, duplicate delivery answered from the record (RA-10), budget verdicts beside the authority check (NM-CRD-4), irreversibility verdicts (NM-AUT-8), and the replay module (R1, R2, third-party verification; R3 deliberately unimplemented).
- `aop-conformance` v0.2.0: HAR-10 (digest sensitivity), HAR-11 counters, HAR-12 (third-party R1/R2 verification), HAR-13 (budget enforcement); certificates carry the tier (Validated, Enforced).

## 4. Acceptance criteria

- The addendum is on main: the comprehensive plan, CR-010 to CR-027, the banners, the decision records.
- The reconciliation points 1, 2, 5 (in part) and 7 carry final dispositions; points 3, 4, 6 were already settled; the register is published with the caveat recorded.
- The spec gate passes with twelve fixtures (ten must-fail behaving); the Phase 4 gate passes; the Wave 6 gate passes; the harness profile certifies with thirteen checks; both profiles certify with tiers.
- Duplicate delivery demonstrably answers from the record without a second external effect; a changed payload yields a different digest; the budget verdict escalates on exhaustion and passes within budget.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; the comprehensive plan is published under plans per D-009; no ratified decision is superseded |
| A5 | IN SCOPE: the source errata document reconciles the sources to the ratified estate; the hierarchy and glossary are unchanged |
| A6 | IN SCOPE, no change: no new glossary term; the register cites the metamodel's own vocabulary |
| A7 to A9 | IN SCOPE, no change: non-goals, positioning and the public description unchanged |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE: new normative text (RA, RP, NM-CRD-4, NM-AUT-8/9, NM-ASR-5, NM-CTL-5, CC-25); schema additive; validator extended; gates re-run |
| C1 to C7 | IN SCOPE: the trust architecture gains the digest binding and the budget enforcement point; the threat model needed no new entries (T1 to T7 already cover the surfaces exercised) |
| D1 to D5 | IN SCOPE, no change: the substrate is untouched in this wave |
| E1 to E6 | IN SCOPE: the manifest gains rule_ratifications, minimum_support, confidence_floor, critical_variants, reversibility and accountability inputs (landed with CR-009 block 1 and consumed here); the compiler is unchanged in this wave |
| F1 to F8 | IN SCOPE: the harness gains the digest binding, budget verdicts, irreversibility verdicts and the replay module; all existing obligations re-verified by the gate |
| G1 to G4 | IN SCOPE, no change: the registry is unchanged |
| H1 to H4 | IN SCOPE: HAR-10 to HAR-13 added; the must-fail discipline holds (five document fixtures fail; the two new spec fixtures fail); certificates carry tiers |
| I1 to I4 | IN SCOPE, no change: the evaluation tier is untouched in this wave |
| J1 to J4, K1 to K2 | IN SCOPE, no change: adoption and examples are untouched; the 5G gate re-runs green |
| L1 to L8 | IN SCOPE: met, same audit method as CR-008 |

## 6. What this CR is not

It is not the CR-010 completion: points 3 and 4 were settled earlier and points 1, 2, 5, 7 are now settled, but the normative six-level to four-scope diagram and glossary map refinement is the CR-010 remainder, tracked in the plan. It is not CR-011 or CR-012 completion either: the run state machine's fixtures for race and partial-success cases and the R3 sandbox profile are the follow-up remainder, tracked in the plan. It does not implement CR-013 to CR-027.

## 7. Implementation

Implemented in aop-spec v0.4.0, aop-foundations v0.1.1, aop-reference-harness v0.3.0 and aop-conformance v0.2.0. All gate outputs recorded in the cross-check stage.
