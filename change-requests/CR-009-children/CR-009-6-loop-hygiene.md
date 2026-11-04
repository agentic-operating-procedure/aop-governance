# CR-009-6: Loop Hygiene (Substrate and Evaluation)

Parent: CR-009. Review item: CR-6. Reconciliation: genuine gap. Class: substrate + evaluation. Status: Proposed, block 2.

## Problem

Execution feeds observation (ARC-P5), so agent behaviour contaminates the baseline it is measured against.

## Change (planned)

- Every case carries its origin: human, agent or mixed (substrate case schema).
- Baseline mining excludes agent-originated cases by default (evaluation).
- A protected human-baseline reservoir is maintained for drift detection (substrate).
- Recompilation requires human review; a recompile cannot ratify itself (extends NM-AUT-7: ratification is a human act on a human-reviewed corpus).
- Acceptance: drift detection runs against the reservoir, and the shadow report separates the reservoir from agent-originated cases.
