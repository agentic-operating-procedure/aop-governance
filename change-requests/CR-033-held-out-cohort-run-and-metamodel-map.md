# CR-033: The Held-Out Cohort Run and the Metamodel Map Closure

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-06 |
| Owner | Emmanuel A. Otchere |
| Layer | Concept, Evaluation, Demonstration |
| Depends on | CR-032 (merged), CR-014 (protocol landed), CR-010 (partially landed) |

## 1. Problem statement

Two remainders from the landed waves are addressable without a live pilot: CR-014's protocol exists but has never been exercised on a genuinely held-out cohort, and CR-010's mapping deliverable (the one normative six-level-to-four-scope alignment) is still open. The held-out exercise matters because the estate's only published shadow result is rule fidelity on the compilation corpus; until a held-out run exists, the protocol is untested machinery.

## 2. Objective

Exercise the CR-014 protocol end to end on the 5G exemplar: deterministic cohort split, development-only recompile, held-out shadow evaluation with the correct claim class; and publish the normative hierarchy-and-metamodel map.

## 3. Scope

- `aop-examples` v0.3.0: the cohort split (seed `ran-cohort-2026-11`, 25 percent held out: 33 development, 12 held-out, every rule family present in development); the development-only compile `AP-RAN-014@v0.2.0` with the support floor scaled proportionately (4/45 to 3/33) and declared in the evaluation manifest; the held-out shadow evaluation (agreement 1.0, zero authority violations, ten conservative deviations, claim class generalisation-held-out); the dev-cohort run labelled rule-fidelity; the walkthrough section stating the honest limit (unseen cases of the same synthetic generator, not live traffic; the prospective cohort remains the pilot's); the cohort files and the evaluation manifest published.
- `aop-foundations` v0.2.0: the hierarchy and metamodel map: the normative six-to-four alignment, the classification rule HM-1 to HM-3, the closure of the harness recursion (a composition rule, not a metaphor), settling reconciliation point 1's mapping deliverable.

## 4. Acceptance criteria

- The held-out cases demonstrably did not feed the compile (the split is deterministic and the compile consumed the development file only; the lint and the digests attest it).
- The claims are labelled: development run rule-fidelity, held-out run generalisation (held-out).
- The walkthrough states what the held-out result does and does not prove.
- The map carries stable identifiers and the classification rule yields no contradictory classifications.
- All estate gates pass; L1 clean.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; no ratified decision is superseded |
| A5 | IN SCOPE: the map is the normative alignment the hierarchy document lacked; the hierarchy itself is unchanged |
| A6 to A9 | IN SCOPE, no change |
| A10 | IN SCOPE, no change |
| B1 to B8 | IN SCOPE, no change: the evaluation manifest declares its support-floor scaling per NM-STR-18 |
| C1 to C7 | IN SCOPE, no change |
| D1 to D5 | IN SCOPE, no change: the cohort files follow the substrate case schema |
| E1 to E6 | IN SCOPE, no change: the toolchain is consumed; the ratification gate's refusal on the unscaled floor is the gate working as designed |
| F1 to F8 | IN SCOPE, no change: the harness is consumed by the evaluation |
| G1 to G4 | IN SCOPE, no change |
| H1 to H4 | IN SCOPE, no change |
| I1 to I4 | IN SCOPE: the protocol is exercised; the cohort labels carry the claims |
| J1 to J4 | IN SCOPE, no change: the promotion gates consume such records unchanged |
| K1 to K2 | IN SCOPE: the walkthrough is extended with the held-out section |
| L1 to L8 | IN SCOPE: met |

## 6. What this CR is not

It is not a live-generalisation claim: the held-out cohort is synthetic and generator-bounded, and the walkthrough says so. It is not CR-014's completion: the prospective cohort and the independent reproduction remain. It is not the CR-010 register completion: E26 to E40 remain unpinned pending the Stage 03 and 05 sources.

## 7. Implementation

Implemented in aop-examples v0.3.0 and aop-foundations v0.2.0. The evaluation outputs are recorded in the walkthrough and the reports directory.
