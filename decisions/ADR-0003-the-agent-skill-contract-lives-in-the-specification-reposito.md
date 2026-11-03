# ADR-0003: The Agent Skill Contract Lives in the Specification Repository

_Status: Accepted_

## Context

The Agent Skill contract is a candidate for its own repository. It defines
what a reusable capability must declare to be composable and independently
testable.

## Decision

The skill contract is a normative annex of `aop-spec`, not a separate
repository.

## Rationale

A skill is consumed by an AOP, and an AOP is defined by the specification.
If the contract lived elsewhere, every specification change would require
a cross-repository contract change, and the two would drift. The contract
and the AOP model are specified against each other and must version
together.

The skill contract is still independently versioned within the
specification, so that the cost of the merge is bounded.

## Consequences

Revival trigger: the skill contract acquires an implementation ecosystem
independent of any AOP implementation, at which point it earns its own
repository.
