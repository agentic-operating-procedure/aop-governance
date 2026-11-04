# CR-025: Security Incident Response and In-Flight Run Recovery

| Field | Value |
|---|---|
| Estate ID | CR-025 (Review 2, item 16) |
| Class | Architecture + Normative |
| Priority | P1 |
| Depends on | CR-011, CR-017 |
| State | New |

## Problem

Recovery strategies and attempts, safe states, hold semantics (SEC-14) and the emergency stop (SEC-15) exist. What is missing is the end-to-end operational contract: detection through containment through recovery for agent, tool, observation, credential and AOP incidents, and the semantics for active cases when a procedure or credential must be withdrawn mid-flight.

## Change

Define the Detect/Respond/Recover lifecycle with incident classes, severity, detection signals, accountable roles and response objectives per deployment profile; suspension and revocation by scope with propagation verification; active-case options by action class (safe hold, cancel, continue under pinned version, migrate), where migration creates a linked new run and never rewrites the original record; approval invalidation on material change; recovery requiring integrity checks, restored policy and identity, evidence reconciliation and an explicit resumption decision.

## Acceptance

- End-to-end exercises cover compromised tool, leaked credential, malicious AOP, observation tampering, policy-service outage and partially completed side effect.
- Reconciles with: SEC-14/15 and the recovery model (extends them into an operational lifecycle), CR-017 (lifecycle states).
