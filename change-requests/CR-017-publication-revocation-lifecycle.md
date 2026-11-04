# CR-017: Publication, Revocation, Rollback and Compatibility Lifecycle

| Field | Value |
|---|---|
| Estate ID | CR-017 (Review 2, item 8) |
| Class | Normative + Architecture |
| Priority | P1 |
| Depends on | CR-012 |
| State | New |

## Problem

Immutable digest publication, ref resolution, verified provenance, the three-dimension lifecycle status (including suspended, superseded, retired) and the release policy exist. Operating a changing fleet needs the remainder: revocation propagation and its speed, active-run behaviour on suspension or revocation, rollback semantics, and compatibility rules across schema, skills, harnesses and registry resolution.

## Change

Specify per-scope suspension and revocation that never mutates historical records; active-run behaviour by action class (stop, continue under pinned prior authorization, or safe hold); rollback to a prior verified version with a recorded reason that does not implicitly restore withdrawn credentials or obsolete policy; compatibility rules for schema evolution and dependency resolution; emergency suspension and recovery exercises; propagation verification that a control reached every enforcement point.

## Acceptance

- Active-run behaviour on revocation is defined and tested per action class.
- A historical case remains interpretable after a schema or registry change.
- Reconciles with: NM-VER-4/5 (lifecycle statuses; approval, release and operational authorisation already distinct), SEC-15 (domain-wide emergency stop; this CR adds per-AOP scope control) and CR-025 (incident lifecycle).
