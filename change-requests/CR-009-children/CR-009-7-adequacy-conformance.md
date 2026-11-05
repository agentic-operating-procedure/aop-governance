# CR-009-7: Conformance From Presence to Adequacy

**MERGED 2026-11-05 into CR-015** (conformance expansion: adversarial, interoperability, tiers) per the comprehensive CR plan (`plans/aop-comprehensive-cr-plan-programme-scope.md`). This child remains as the review-1 record; its content lives on in the estate CR.

Parent: CR-009. Review item: CR-7. Reconciliation: partially covered (must-fail fixtures and several semantic lints exist). Class: assurance. Status: Proposed, block 3. Owner decision taken 2026-11-05: tiered claims over binary suites (the certification process document carries the tier vocabulary; the metamodel L0 to L4 cross-maps informatively; reconciliation point 6 is settled). Block 3 implements the adversarial suite as the third tier's suite, the coverage map, byte pinning and the second verifier.

## Already covered (reconciled)

The must-fail fixture discipline; semantic lints for prose thresholds, authority coverage and escalation-without-target-role; the validator's normative checks.

## Change (planned)

- Semantic lint rules join the document profile: unreachable decisions, authority without a constraint, a constraint that cannot be evaluated outside the executor. Tiering is settled: named tiers over binary suites (Validated, Enforced, Adversarially Tested, Assured); no graduated conformance semantics.
- The adversarial suite covering CR-009-1 and CR-009-3, named must-reject fixtures tied to spec sections.
- The machine-readable requirement-to-fixture map stating what is not covered; byte-pinned fixtures; a second independent verifier.
- Acceptance: a third party can run the suite offline and reproduce the results.
