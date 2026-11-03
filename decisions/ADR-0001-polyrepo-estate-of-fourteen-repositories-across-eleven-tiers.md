# ADR-0001: Polyrepo Estate of Fourteen Repositories Across Eleven Tiers

_Status: Accepted_

## Context

The programme must produce an engineering estate for a concept that spans
concept, specification, architecture, substrate, tooling, runtime,
catalogue, assurance, evaluation and adoption. The question is whether that
is one repository or several.

## Decision

The estate is a polyrepo of fourteen repositories across eleven tiers.

## Rationale

A monorepo would couple the rate of change of the concept to the rate of
change of the runtime, which is the coupling that produced most of the
failure modes the concept exists to correct. The tier structure preserves a
single authority per concern while letting each repository carry its own
lifecycle and its own review cadence.

Each repository was checked against a single question: does it have an
independent failure mode? Where two candidates fail together they were
merged. Where two candidates change at different rates they were split.

## Consequences

A cross-repository change requires the full cascade audit in
`plans/aop-org-cascade-checklist-org-scope.md`. This is the cost, accepted
deliberately: the cascade is the mechanism that keeps the authority ladder
honest.
