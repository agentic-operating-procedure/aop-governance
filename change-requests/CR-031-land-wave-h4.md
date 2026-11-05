# CR-031: Land Wave H4 of the Comprehensive CR Plan

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Evidence, Assurance, Evaluation |
| Depends on | CR-030 (merged), CR-014, CR-015 |

## 1. Problem statement

The comprehensive CR plan sequences Wave H4 as the evidence wave: independent out-of-sample evaluation (CR-014, the review's highest-value open item) and conformance expansion into adversarial and interoperability testing (CR-015). Until these land, the evaluation tier cannot distinguish a generalisation claim from a rule-fidelity claim, there is no adversarial suite, no requirement-to-fixture coverage map, and fixtures are not byte-pinned.

## 2. Objective

Land Wave H4: the independent evaluation protocol with cohort separation and pre-registration, labelled shadow claims, the adversarial suite with behavioural checks, the machine-readable coverage map, and byte-pinned fixtures.

## 3. Scope

- `aop-evaluation` v0.3.0: the independent evaluation protocol (EV-P1 to EV-P11: cohort separation, pre-registration with falsifiers, the extended metric set including adjudicated correctness and uncertainty, promotion records with residual risks and the risk acceptor, independence defined, negative results published); the cohort module (deterministic seeded split, pre-registration records, promotion records); shadow reports carrying the cohort label and the claim class so a development-corpus result cannot pass as a generalisation claim.
- `aop-conformance` v0.5.0: the adversarial suite (three document must-rejects: untrusted-grounded authority, republished unratified rules, append-only retracted; two behavioural checks: HAR-24 prohibited-value smuggling, HAR-25 hostile-proposer flood containment); the machine-readable requirement-to-fixture coverage map (28 covered, 3 uncovered with the gaps stated); byte-pinned fixtures with a verified pin manifest.

## 4. Acceptance criteria

- Shadow reports carry the cohort and claim class; a development-corpus run labels itself rule-fidelity (demonstrated live).
- The seeded cohort split is deterministic and reproducible (demonstrated: 28 development, 17 held-out on the exemplar corpus).
- The adversarial document fixtures are must-reject; HAR-24 and HAR-25 pass; the hostile-proposer flood is contained with the chain intact.
- The coverage map is machine-readable, states 28 covered and 3 uncovered with reasons; the pin manifest verifies.
- All estate gates pass; both profiles certify.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; no ratified decision is superseded |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and the public description unchanged |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE, no change: the specification is untouched; the evaluation and assurance tiers extend |
| C1 to C7 | IN SCOPE, no change: HAR-24/25 exercise existing mechanisms |
| D1 to D5 | IN SCOPE, no change: cohort provenance cites CG-S16 facts |
| E1 to E6 | IN SCOPE, no change: the toolchain is untouched |
| F1 to F8 | IN SCOPE, no change: the harness is exercised (hostile proposer), not altered |
| G1 to G4 | IN SCOPE, no change |
| H1 to H4 | IN SCOPE: the adversarial suite, the coverage map, byte pinning, and the certificate content are the CR-015 deliverables |
| I1 to I4 | IN SCOPE: the evaluation tier gains the protocol, the cohort split, the labels and the promotion records |
| J1 to J4, K1 to K2 | IN SCOPE: adoption gains the promotion-gate alignment hook (CR-019 binds to it); the exemplar's shadow run now labels itself rule-fidelity explicitly |
| L1 to L8 | IN SCOPE: met, same audit method as CR-030 |

## 6. What this CR is not

It is not a generalisation claim: the live and held-out cohorts exist as protocol and tooling; the prospective run is the adoption pilot's (CR-006, CR-019). It is not interoperability: the two-independent-verifier requirement remains uncovered, stated in the coverage map, tracked in the plan. The uncovered items are named in the map by design, which is the CR-015 acceptance: the map states what is not covered.

## 7. Implementation

Implemented in aop-evaluation v0.3.0 and aop-conformance v0.5.0. All gate outputs recorded in the cross-check stage.
