# ADR-0012 (Draft): Authorize staged implementation of CR-041

| Field | Value |
|---|---|
| Status | Draft for programme-owner decision; not ratified |
| Date | 2026-11-26 |
| Decision owner | AOP programme owner |
| Related CR | CR-041 |
| Origin | AO-WE-001, Agentic-Operation PR #14 merged |

## Context

CR-041 proposes restoration of fault-management reference-fixture integrity and execution-policy consistency. It is currently **Proposed**. Evidence identifies defects in temporal consistency, sequence/branch semantics, authority and escalation consistency, and permitted-action/skill coverage. Before implementation, acceptance must be recorded through the AOP governance process. Counts reported in the CR and independent diagnostics differ and must be reconciled against a pinned corpus revision before any fixture correction.

## Decision requested

Accept CR-041 for staged implementation, subject to repository-scoped review and the CR's acceptance criteria. This draft does not itself constitute acceptance, implementation authorization, or ratification.

## Staged work and boundaries

1. **Governance coordination (aop-governance):** upon ratification, record acceptance, owner/work-package ledger, dependency and evidence requirements. Keep CR status Proposed until acceptance is formally recorded.
2. **Temporal/event semantics (aop-context-graph):** reconcile event timestamp meaning, capture timestamp/provenance, timezone/format, procedural ordering vs chronology, concurrency, case-boundary membership, delayed/pre/post events, and cycle-time unit/derivation. Map requirements to existing clauses first; change only genuine gaps.
3. **Corpus/tooling (aop-toolkit):** after stage 2 decisions are approved, validator and positive/negative fixtures; adjudicate source corpus; regenerate/correct only with source provenance and pinned digest. Do not normalize timestamps or reorder steps mechanically.
4. **Procedure/authority (aop-toolkit; conditional aop-spec):** domain-owner decision on valid branches, dispatch minimum authority, escalation/handoff and action/skill bindings. Escalation is not an executable agent action.
5. **Enforcement/conformance (aop-reference-harness, aop-conformance; conditional aop-spec):** enforce approved authority/handoff contracts and negative cases; only add normative clauses where a demonstrated gap exists.
6. **Process alignment (OpenDEA catalogue owner, separate governance):** disposition the applicable process identity. AOP must not create or approve OpenDEA catalogue entries.
7. **Replay/closure (aop-registry, aop-evaluation, aop-examples as conditional):** pinned versions and repeatable logs; no performance or production claims absent evidence.

## Guardrails

- Each repository owner retains repository-level change authority.
- No PR in this coordination proposal directly modifies downstream repositories.
- No fixture edits, runtime enablement, credentials, dispatch authority, or live external actions are authorized by this draft.
- Preserve superseded artefacts and provenance; publish corpus digest and validator results.
- Report partial implementation by repository; CR-041 closure requires all acceptance criteria and reproducible cross-repository gate.

## Consequences if accepted

Creates a sequenced, owner-bounded remediation programme and avoids parallel edits before semantics are resolved. The first implementation dependency is a reviewed temporal-semantics disposition in aop-context-graph. Open questions and fixture discrepancies remain explicit until evidence and domain-owner decisions resolve them.

## Ratification

Programme owner decision: **Pending**  
Approval evidence / meeting / review reference: **Pending**  
Ratified date: **Pending**
