# CR-032: Land Wave H5 of the Comprehensive CR Plan

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Governance, Adoption, Implementation |
| Depends on | CR-031 (merged), CR-018, CR-019, CR-027 |

## 1. Problem statement

The comprehensive CR plan sequences Wave H5 as the maturity wave: independent governance and claims discipline (CR-018), risk-tiered adoption and promotion gates (CR-019), and the optional Pi harness adapter (CR-027). Until these land, reviews depend solely on the authoring path, adoption has no progressive operating model tied to independent evidence, and the estate's implementation-neutrality claim has no third-party harness demonstration.

## 2. Objective

Land Wave H5: the reviewer independence and claims discipline document, the operating modes and promotion gates, and the experimental Pi adapter with its self-test, completing the comprehensive CR plan's waves.

## 3. Scope

- `aop-governance` v0.2.0: the reviewer independence and claims discipline document (CR-018): reviewer eligibility and conflicts (GI-1 to GI-3), quorum with recorded dissent and appeals (GI-4 to GI-6), claims discipline with correction and withdrawal (GI-7 to GI-9), and stewardship succession (GI-10). The programme owner's decision rights are unchanged; the independence layer sits on top.
- `aop-adoption` v0.2.0: the operating modes and promotion gates document (CR-019): five modes per action class (observe-only, recommend, approval-gated, bounded, expanded) with entry, promotion, demotion and stop criteria; promotion consumes the evaluation protocol's pre-registered gates and promotion records; the explicit distinction between a conformant AOP and an operationally authorised one; the mapping onto the maturity model.
- `aop-examples` v0.2.0: the optional Pi adapter (CR-027), labelled EXPERIMENTAL: Pi reasons and proposes; the external guardrail enforces; shell, filesystem, network and credential routes are denied by default; the self-test runs the acceptance behaviours (bypass attempts, flood, duplicate delivery) without Pi installed. Not a normative dependency.

## 4. Acceptance criteria

- The governance document states the independence layer with stable identifiers (GI-1 to GI-10) and the proportionality it can honestly run at draft scale.
- The operating modes document binds modes to authority (never widened), promotion to the evaluation protocol, and demotion/stop criteria to measurable triggers.
- The Pi adapter self-test passes 5/5: shell and unregistered routes denied, in-authority proposals pass the enforcement point, floods gated, duplicate delivery answered.
- All estate gates pass; L1 clean.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; no ratified decision is superseded |
| A5 | IN SCOPE, no change: the hierarchy and glossary are unchanged |
| A6 | IN SCOPE, no change: no new glossary term |
| A7 | IN SCOPE, no change: the non-goals hold (the adapter is optional; the governance layer adds review, not shared decision rights) |
| A8, A9 | IN SCOPE, no change: positioning and the public description unchanged |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE, no change: the specification is untouched in this wave |
| C1 to C7 | IN SCOPE, no change: the adapter consumes the published enforcement sequence |
| D1 to D5 | IN SCOPE, no change: the substrate is untouched |
| E1 to E6 | IN SCOPE, no change: the toolchain is untouched |
| F1 to F8 | IN SCOPE, no change: the harness is consumed by the adapter, not altered |
| G1 to G4 | IN SCOPE, no change |
| H1 to H4 | IN SCOPE, no change: the conformance tier is untouched |
| I1 to I4 | IN SCOPE, no change: the promotion gates consume the protocol, not change it |
| J1 to J4 | IN SCOPE: the adoption tier gains the modes and promotion gates (CR-019's deliverable) |
| K1 to K2 | IN SCOPE: the exemplar estate carries the adapter demonstration |
| L1 to L8 | IN SCOPE: met, same audit method as CR-031 |

## 6. What this CR is not

It is not shared governance: the owner's decision rights stand; the independence layer reviews, dissents and disciplines claims (GI-4). It is not a Pi endorsement: the adapter is optional, experimental, and carries no certificate. It is not the completion of the uncovered items in the coverage map (two independent verifiers, egress enforcement tests, baseline adequacy), which remain tracked in the plan.

## 7. Implementation

Implemented in aop-governance v0.2.0, aop-adoption v0.2.0 and aop-examples v0.2.0. The adapter self-test output is recorded in the cross-check stage.
