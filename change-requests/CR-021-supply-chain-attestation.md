# CR-021: Supply-Chain Attestation for AOPs, Compiler and Skills

| Field | Value |
|---|---|
| Estate ID | CR-021 (Review 2, item 12) |
| Class | Architecture + Security |
| Priority | P1 |
| Depends on | CR-015, CR-017 |
| State | In progress (NM-VER-7 + SK-12 + build attestation + registry unsigned-effective refusal landed under CR-030; signing scheme remains the deployment obligation) |

## Problem

ARC-TB1 signs policy bundles; the registry publishes content digests and provenance chains; the skill contract exists. A digest does not establish who built an artefact, which compiler and dependencies produced it, or whether a skill update changed behaviour or access.

## Change

Define attestations binding published artefacts to source inputs (SOP, corpus digest, manifest), builder identity, toolchain versions, review record and digest; unsigned or invalid artefacts cannot reach operationally authorised state; compiler-emitted build provenance; skill declarations carrying immutable version, maintainer, required tools, data and egress; skill updates as new versions that trigger review when access or behaviour changes; registry resolution verifying attestations and exposing revocation state.

## Acceptance

- Fixtures reject tampered artefacts, mismatched attestations, unpinned dependencies and dependency substitution.
- Reconciles with: ARC-TB1 (extends signing from bundles to the whole supply chain), SK-1..SK-11 (extends the skill contract with lineage), CR-017 (owns suspension and revocation behaviour).

## Landing note (2026-11-05)

Landed under CR-030. See the landing CR for the full audit.
