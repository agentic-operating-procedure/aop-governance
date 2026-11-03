# ADR-0004: Security and Trust Live in Specification and Architecture, Not a Separate Repository

_Status: Accepted_

## Context

The programme's central technical claim is that authority is enforced
outside the model context. That claim needs a threat model and a normative
rule set.

## Decision

The normative security clauses live in `aop-spec`. The threat model and
the trust-boundary diagrams live in `aop-architecture`. There is no
`aop-security` repository.

## Rationale

A separate security repository fragments the guardrail. The guarantee is
only meaningful when the rule, the boundary it describes and the component
that enforces it are read together. Separating them creates the failure
mode the programme argues against: a policy document and an implementation
that drift apart without anyone noticing, because nobody reads both.

## Consequences

Revival trigger: an independent security review body takes ownership of
the programme's security posture, or the threat model outgrows a single
chapter of the architecture repository.
