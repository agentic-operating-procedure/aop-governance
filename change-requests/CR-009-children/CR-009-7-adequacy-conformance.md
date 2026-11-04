# CR-009-7: Conformance From Presence to Adequacy

Parent: CR-009. Review item: CR-7. Reconciliation: partially covered (must-fail fixtures and several semantic lints exist). Class: assurance. Status: Proposed, block 3, with an owner decision.

## Already covered (reconciled)

The must-fail fixture discipline; semantic lints for prose thresholds, authority coverage and escalation-without-target-role; the validator's normative checks.

## Change (planned)

- Tiered profiles with semantic lint rules: unreachable decisions, authority without a constraint, a constraint that cannot be evaluated outside the executor. Note: graduated conformance levels are open reconciliation point 6 and remain an owner decision.
- The adversarial suite covering CR-009-1 and CR-009-3, named must-reject fixtures tied to spec sections.
- The machine-readable requirement-to-fixture map stating what is not covered; byte-pinned fixtures; a second independent verifier.
- Acceptance: a third party can run the suite offline and reproduce the results.
