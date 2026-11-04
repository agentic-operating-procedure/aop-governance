# CR-011: Runtime Action, Retry, Concurrency and Recovery Semantics

| Field | Value |
|---|---|
| Estate ID | CR-011 (Review 2, item 2) |
| Class | Normative + Architecture |
| Priority | P0 |
| Depends on | CR-010 |
| State | In progress (normative text + digest binding, duplicates, budgets, irreversibility landed under CR-028) |

## Problem

The runtime loop, fail-closed matching, bounded rework loops and immutable AOP binding are normative and implemented. There is no interoperable contract for the operational behaviour of side effects: timeouts with uncertain completion, retries, duplicate delivery, concurrent runs, partial success across external systems, cancellation, and compensation when rollback is impossible.

## Change

Define the run state machine and the side-effecting action contract: stable action identifiers, idempotency and duplicate-submission behaviour, retry classification (safe to retry versus requires reconciliation), authorization bound to the action payload and context version (stale authorization cannot authorize a changed action), concurrency safeguards for shared resources, partial-success and compensation semantics, and enumerated degraded modes that never widen authority.

## Acceptance

- The normative run state machine covers start through terminal disposition including retry, cancellation and recovery.
- Authorization binds to an action digest; changed payload invalidates it.
- Reference fixtures exercise timeout, duplicate, race, cancellation, partial success and recovery cases.
- Reconciles with: SEC-14/15 (hold and emergency stop) and CR-009-3 budgets; does not reopen fail-closed or loop-bound rules.

## Landing note (2026-11-05)

Landed under CR-028: RA-1 to RA-14 normative; the harness implements action digests (RA-5 to RA-7), duplicate answering (RA-10), budget verdicts (NM-CRD-4), irreversibility verdicts (NM-AUT-8), hold semantics (SEC-14). Remainder: race and partial-success fixtures, timeout/retry exercise fixtures, concurrency enforcement tests.
