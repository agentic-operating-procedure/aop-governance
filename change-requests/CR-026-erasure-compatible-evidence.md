# CR-026: Erasure-Compatible Audit Evidence

| Field | Value |
|---|---|
| Estate ID | CR-026 (Review 2, item 17) |
| Class | Normative + Architecture |
| Priority | P1 |
| Depends on | CR-012, CR-013, CR-017 |
| State | In progress (NM-ASR-7 + payload externalisation, shredding, tombstones, narrowed replay claims landed under CR-030; backup/replica propagation remains) |

## Problem

Append-only evidence, minimisation and retention declarations exist (SEC-8, CG-O5, CG-O6). They can conflict when deletion obligations require personal or regulated data to be removed while the audit trail must remain verifiable. The standard should support erasure without sensitive payloads living indefinitely in an immutable log.

## Change

Separate minimal integrity and accountability metadata from sensitive payloads eligible for deletion or externalised storage; define retention and deletion across source events, cases, derived graphs, compiler intermediates, provenance references, approvals and runtime records; deletion executed and independently verified across linked stores without breaking unrelated chains; tombstones or cryptographic erasure preserving ordering and the deletion fact while making content unrecoverable; replay claims narrowed explicitly when supporting data is erased; jurisdiction-specific timelines left to deployment profiles.

## Acceptance

- Tests cover deletion propagation, key destruction, backup and replica handling, and tamper detection after erasure.
- The record states what can still be reconstructed after erasure, and what claims are withdrawn.

## Landing note (2026-11-05)

Landed under CR-030. See the landing CR for the full audit.
