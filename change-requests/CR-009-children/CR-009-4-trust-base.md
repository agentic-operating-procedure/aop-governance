# CR-009-4: The Trust Base (Architecture and Normative Spec)

Parent: CR-009. Review item: CR-4. Reconciliation: partially covered (SEC-7, ARC-R3, SEC-8, T3). Class: architecture decision + normative clauses.

## Change (landed in block 1)

- ARC-TB-1 to ARC-TB-4: signed versioned policy bundles with rollback; key custody and external anchoring of the case record as named deployment obligations; separation of duties among AOP author, ratifier and harness operator; the emergency-stop semantics.
- SEC-14: on enforcement unavailability the harness holds and escalates; it never proceeds. SEC-15: a named role may halt all runs in the domain; the halt is recorded; resumption requires the accountable owner.
- NM-GOV-1: every AOP names its accountable owner (governance.accountable_owner).
- Threat model gains T6 (policy or guardrail compromise) and T7 (log truncation and tampering), each with a testable mitigation.
- Acceptance: the harness profile exercises the emergency stop and the hold path (HAR-9); the threat model entries exist.
