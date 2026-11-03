# ADR-0002: Repository Naming Uses the aop- Prefix

_Status: Accepted_

## Context

The estate lives alongside sibling discipline organisations in the same
account.

## Decision

Repository names use the `aop-` prefix, the short form of
`agentic-operating-procedure`, followed by a role noun. The sole exception
is `.github`, whose name the platform fixes.

## Rationale

This is the convention already in force across the sibling organisations:
`enterprise-semantics-spec`, `enterprise-semantics-governance`,
`enterprise-semantics-docs`, `dea-governance`, `dea-metamodel`. Adopting it
keeps the estate legible as one programme to a reader who knows the
conventions, without requiring that reader to learn a new one.

## Consequences

No repository name may be changed without a change request, because every
artefact, board card and project item references repositories by name.
