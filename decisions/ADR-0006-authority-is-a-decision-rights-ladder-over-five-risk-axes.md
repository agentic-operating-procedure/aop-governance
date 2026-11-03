# ADR-0006: Authority Is a Decision-Rights Ladder Over Five Risk Axes

_Status: Accepted_

## Context

An AOP must state what an agent may decide alone and what it must escalate.

## Decision

Authority is modelled as a decision-rights ladder with five rungs, assigned
per decision class by scoring five risk axes: reversibility, blast radius,
data sensitivity, regulatory exposure and confidence in the observed
evidence.

## Rationale

A binary allow or deny cannot express the real operating requirement, which
is a spectrum from execute-and-report to refuse-and-escalate. A flat
per-action permission list does not scale to a procedure with hundreds of
decision points. Scoring five axes produces a repeatable assignment that a
reviewer can challenge on the evidence rather than on preference.

## Consequences

Every AOP must carry an authority assignment for each of its decision
points. The `aop-conformance` AOP document profile checks authority
coverage as a pass or fail condition.
