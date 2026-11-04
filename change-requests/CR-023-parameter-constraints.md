# CR-023: Parameter-Level Action Constraints at Enforcement Time

| Field | Value |
|---|---|
| Estate ID | CR-023 (Review 2, item 14) |
| Class | Normative |
| Priority | P1 |
| Depends on | CR-011, CR-016 |
| State | New |

## Problem

Permitted sets, rule thresholds and action classes constrain which actions may run; an action can be in a permitted class and still unsafe because of its target, amount, scope, duration or parameter values. There is no portable contract for constraining the canonical payload that actually reaches the enforcement point.

## Change

Define typed action schemas: required and optional fields, types, units, bounds, target scope, prohibited values, explicit defaults that cannot be implicitly supplied by model or adapter, canonicalisation ownership, and null handling. The enforcement point validates the canonical payload after all adapter transformations and binds its decision and the approval to the payload digest; unknown fields, ambiguous units, coercions and out-of-range values fail closed or escalate per the risk profile.

## Acceptance

- Conformance fixtures tamper parameters between proposal, approval and execution; all tampering is caught.
- Cumulative effects across a case cross-reference the CR-009-3 budgets.
