# CR-015: Conformance Expansion: Adversarial, Interoperability, Tiers

| Field | Value |
|---|---|
| Estate ID | CR-015 (Review 2, item 6 + CR-009-7, merged) |
| Class | Evidence |
| Priority | P1 |
| Depends on | CR-011, CR-012 |
| State | New |

## Problem

Profiles AOP-DOC-1 and HAR-1, must-fail fixtures, poisoned-context and chain-tamper tests, and certificates exist and are credited. A single reference implementation passing its own suite does not establish that independent implementations enforce the same meaning or resist realistic attacks and fault modes at breadth.

## Change

Implement the settled tier vocabulary (Validated, Enforced, Adversarially Tested, Assured) as cumulative binary suites; build the adversarial suite (injection, stale or malicious AOPs, compromised tools, credential replay, authority widening, scope violations, audit tampering, escalation flooding, enforcement outage, stale context, races, recovery); publish the machine-readable requirement-to-fixture coverage map stating what is not covered; byte-pin fixtures; require two independently implemented verifiers before any portability claim; version profiles separately with required and optional capabilities; certificates identify digests, versions, environment and exclusions.

## Acceptance

- Positive and must-fail cases exist for every mechanically testable MUST.
- A third party runs the suite offline and reproduces the results.
- Certification is never presented as proof of task quality or safety outside the tested envelope.
