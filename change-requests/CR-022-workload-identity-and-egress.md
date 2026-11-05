# CR-022: Workload Identity and Controlled Egress

| Field | Value |
|---|---|
| Estate ID | CR-022 (Review 2, item 13) |
| Class | Normative + Architecture + Security |
| Priority | P1 |
| Depends on | CR-015, CR-016 |
| State | In progress (SEC-16/17 + ARC-WS1/2 + workload identity with cross-workload refusal landed under CR-030; egress enforcement tests belong to deployment profiles) |

## Problem

The enforcement point and credential broker are normative and implemented. A robust deployment must also guarantee that the process making tool calls is a distinct authenticated workload that cannot route around enforcement through a shell, browser, direct API call or alternate network path. Reviewed public material does not establish this as a portable conformance requirement.

## Change

Define workload identity bound to AOP version, tenant or case, action class and credential issuance; deny-by-default egress profiles with declared per-profile allowlists (never blanket denial); host tools, shells, plugins and child processes inheriting or narrowing the boundary; conformance tests for identity spoofing, credential replay, direct egress, alternate invocation and enforcement-outage behaviour.

## Acceptance

- All external side effects pass through an enforcement point that validates identity, action, target and decision; bypass paths are blocked and tested.
- Credentials are unavailable to the model context and unusable across workloads, runs, tenants or action classes.

## Landing note (2026-11-05)

Landed under CR-030. See the landing CR for the full audit.
