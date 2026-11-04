# CR-009-5: Oversight Quality (Normative Spec and Harness)

Parent: CR-009. Review item: CR-5. Reconciliation: partially covered. Class: normative + implementation. Status: Proposed, block 2.

## Already covered (reconciled)

Evidence bundles carry the baseline comparison (SEC-9); ruling latency is already a named metric in the adoption change guidance.

## Change (planned)

- Escalation SLAs and defined timeout behaviour (route to fallback role on non-response, recorded; never auto-approve on timeout).
- Approver-independence rules: the approver of a ruling is not the actor that requested it and not the author of the triggering rule.
- Oversight metrics emitted by the harness: approval rate, time-to-approve, override rate.
- Sampled audit of auto-approved cases and injected test escalations to detect rubber-stamping.
- Acceptance: the harness emits the oversight metrics and raises a failing-approver alert under an injected approval pattern.
