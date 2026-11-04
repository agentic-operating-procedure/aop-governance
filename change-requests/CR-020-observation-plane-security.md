# CR-020: Observation Plane and Context Graph Security

| Field | Value |
|---|---|
| Estate ID | CR-020 (Review 2, item 11) |
| Class | Architecture + Security |
| Priority | P1 |
| Depends on | CR-013, CR-015 |
| State | New |

## Problem

The threat model states the substrate must not be writable by observed agents (T5 answers frequency manipulation through governance), and the posture constrains capture. The trust boundary needs to extend over the whole observation plane: capture connectors, normalisation, stitching, graph storage, compiler reads, administrators and exports, with identity, integrity and tamper-response controls that are tested rather than assumed.

## Change

Specify and test: authenticated source identity for capture connectors with key rotation and revocation; integrity metadata sufficient to detect forgery, replay, deletion and unauthorised relinking; stitching integrity checks for joins, handoffs, source ordering and cross-tenant contamination; quarantine or fail-closed compilation on provenance failure; independent tests attempting event forgery, replay, record deletion, poisoned linkage, unauthorised export and agent-originated graph mutation.

## Acceptance

- One agent cannot raise its own behaviour's frequency or authority in the corpus.
- An auditor can distinguish missing observation from a true absence of a path.
- Reconciles with: T5, CG-O posture, CG-S stitching; adds enforcement and tests to the stated assumption.
