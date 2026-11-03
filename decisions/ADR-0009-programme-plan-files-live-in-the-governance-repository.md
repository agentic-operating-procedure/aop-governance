# ADR-0009: Programme Plan Files Live in the Governance Repository

_Status: Accepted_

## Context

The programme plan, the repository map and the cascade checklist must be
versioned and reviewed.

## Decision

They live in `aop-governance` under `plans/`.

## Rationale

The plan is a governance artefact, not an engineering one. Placing it in
the governance repository means the plan changes under the same change
model as everything else, which is what stops the plan and the estate from
drifting apart silently.

## Consequences

The local workspace at a local authoring workspace is the authoring
surface. It is published into `aop-governance` on the wave 1 landing.
