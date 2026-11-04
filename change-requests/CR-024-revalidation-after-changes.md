# CR-024: Revalidation After Model, Tool or Runtime Changes

| Field | Value |
|---|---|
| Estate ID | CR-024 (Review 2, item 15) |
| Class | Normative + Evidence |
| Priority | P1 |
| Depends on | CR-014, CR-015, CR-017 |
| State | New |

## Problem

Runs pin the AOP version (NM-STR-11), which controls procedure drift. Behaviour also changes when the model, prompt or template, tool, adapter, policy engine, harness, provider configuration or dependencies change; nothing defines which of those changes trigger which revalidation before continued operation.

## Change

Define the change-impact matrix and revalidation policy: run records carrying immutable identifiers for every behaviour-affecting component; changes classified into named gates (document conformance, harness security conformance, shadow evaluation, human approval, full re-promotion); material component changes cannot inherit prior evaluation claims without evidence the envelope still applies; rollback, canary and emergency pinning to a known-good component set; certificates and promotion records naming the exact component matrix.

## Acceptance

- Fixtures simulate component changes and verify the right gate blocks or permits rollout.
- Hosted models with mutable aliases are handled by digest or configuration pinning, not by name.
