# CR-009-1: Trust-Classed Case Facts (Normative Spec and Harness)

Parent: CR-009. Review item: CR-1. Reconciliation: genuine gap. Class: normative + implementation.

## Problem

The guardrail sits outside the model's context, but the case facts it evaluates can originate in model output or attacker-influenced content. A manipulated fact can steer a case into a variant whose rules authorise the action.

## Change (landed in block 1)

- NM-CTX-5: every context element carries a trust class: system-attested, derived, model-asserted, or untrusted-content.
- NM-STR-16: matching and authority evaluation use only system-attested and derived facts. Model-asserted and untrusted-content facts are advisory to the executor and invisible to the policy decision point.
- NM-STR-17: where a condition reads an attested fact absent from the snapshot, the condition is unknown and routes to escalation; it never defaults to true.
- The guardrail builds its decision context from the attested and derived elements only. Poisoning a model-asserted fact cannot change a verdict.
- Acceptance: must-fail fixture where an authority-bearing rule is grounded in a model-asserted element (validator rejects); runtime check where a poisoned untrusted fact leaves the verdict identical (harness profile HAR-8).
