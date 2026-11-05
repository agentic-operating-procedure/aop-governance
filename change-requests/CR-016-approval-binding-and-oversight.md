# CR-016: Approval Binding and Oversight Quality

| Field | Value |
|---|---|
| Estate ID | CR-016 (Review 2, item 7 + CR-009-5, merged) |
| Class | Normative + Architecture |
| Priority | P1 |
| Depends on | CR-011 |
| State | In progress (the approval object, four outcomes, canaries, oversight metrics, SLA routing landed under CR-029) |

## Problem

Evidence bundles (action, rule, provenance, baseline, context), approval-before-credential for high-risk classes, and the dispatch interface exist. What the human approves is not yet bound verifiably to the exact payload; approvals do not expire or revoke; approver identity, eligibility and independence are interface-level, not contractual; oversight quality is unmeasured.

## Change

Define the approval object bound to an immutable action payload digest, target, context version, triggering rule, AOP version and expiry; material change invalidates and requires a new decision; approver eligibility, prohibited self-approval, delegation and quorum; the four-outcome interface (approve, reject, request changes, defer; no response is never approval); re-check at credential issuance and at execution; oversight metrics (approval rate, time-to-approve, override rate) and injected test escalations to detect rubber-stamping; escalation SLAs with defined non-response routing that never auto-approves.

## Acceptance

- The reference harness emits oversight metrics and raises a failing-approver alert under an injected approval pattern.
- Reconciles with: SEC-9 bundles and ARC-C2 (approval-gated credentials); extends them with binding and revocation.

## Landing note (2026-11-05)

the approval object, four outcomes, canaries, oversight metrics, SLA routing landed under CR-029. See CR-029 for the full audit.
