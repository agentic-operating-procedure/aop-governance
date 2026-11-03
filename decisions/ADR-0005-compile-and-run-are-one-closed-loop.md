# ADR-0005: Compile and Run Are One Closed Loop

_Status: Accepted_

## Context

The pipeline is often described as four stages: observe, model, compile,
execute.

## Decision

The pipeline is specified as a closed loop. Execution feeds observed cases
back into the substrate, which re-mines variants and re-derives rules, which
can produce a new version of the AOP.

## Rationale

A procedure is a claim about how work happens. Every execution either
confirms the claim or falsifies it. If the loop does not close, the AOP
becomes a static document with a runtime attached, which is the SOP failure
mode wearing a new name. The loop closing is what makes drift detectable
and what makes an AOP self-correcting under governance.

## Consequences

The runtime, the substrate and the toolkit are mutually dependent across
repositories. This is the one place where the estate's upward dependency
flow is deliberately broken, and it is broken through a published interface
contract in `aop-architecture`, not through a direct code dependency.
