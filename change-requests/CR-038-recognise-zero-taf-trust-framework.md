# CR-038: Recognise Zero-TAF as the Trust Framework Whose Runtime Realisation AOP Profiles

| Field | Value |
|---|---|
| Status | Implemented |
| Date | 2026-11-23 |
| Owner | Emmanuel A. Otchere |
| Layer | Estate |
| Depends on | ADR-0001 (polyrepo estate), ADR-0006 (decision-rights ladder), ADR-0007 (standards sourcing) |

## 1. Problem statement

The estate formalises decision rights, authority checks outside the model context, escalation with evidence bundles, and the append-only case record — but has no recognised counterpart framework for the trust architecture those mechanisms operationalise. The Zero-Trust Agent Framework programme (`github.com/Zero-TAF`) now exists and defines that architecture: no agent, tool, delegation, or action implicitly trusted; the protected unit is the decision; identity minted per task under signed mandate chains; the decision point outside the model context; per-action enforcement; capability containment; graded assurance (Tough Grades, scored on the same five risk axes as ADR-0006). Absent a recorded relationship, the two estates risk silent divergence and duplicative claims.

## 2. Objective

The repository map (§5, Relationship to sibling organisations) records Zero-TAF as the trust framework whose runtime realisation AOP profiles: Zero-TAF defines the trust semantics; this programme binds them into procedural execution. The mapping direction is stated one-way from each side and neither estate copies the other.

## 3. Scope

`aop-governance` only: this CR; the CR register row; one new bullet in §5 of `plans/aop-repository-map-org-scope.md`. No specification, architecture, or clause text changes. The reciprocal record on the Zero-TAF side is its ADR-ZTAF-0006, which cites this CR by number.

## 4. Acceptance criteria

- The repository map records the relationship and the direction-of-authority statement.
- ADR-0004 remains in force and untouched: Zero-TAF is a distinct framework, not an AOP security repository; ADR-0004's revival trigger is not tripped by this CR.
- No AOP clause text is altered by this CR.
- The register carries the CR-038 row.

## 5. Cascade audit

Checked against `plans/aop-org-cascade-checklist-org-scope.md`.

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A4 | IN SCOPE: §5 of the repository map updated; the ladder itself unchanged |
| A2, A3, A5 to A10 | IN SCOPE, no change |
| B1 to C7 | IN SCOPE, no change: no clause, schema, boundary, or threat-model change |
| D1 to L4 | N/A or no change |
| L1 | IN SCOPE: met — the relationship is recorded before any artefact moves |

## 6. What this CR is not

It is not the creation of any repository in this estate. It is not a conformance change: no AOP document profile or harness behaviour changes. It is not a merge of programmes: Zero-TAF remains a separate organisation; this CR records consumption and realisation direction only. It is not the detailed clause-level binding (ZT ↔ SEC ↔ TG): that lands later in the Zero-TAF programme's `ztaf-bindings`, mirrored by a future AOP-side CR when it exists.

## 7. Implementation and evidence

Implemented in `aop-governance` by [PR #22](https://github.com/agentic-operating-procedure/aop-governance/pull/22), merged at `4ececd6329f6775c44820736065eaa90f532ace3`. The PR changed this CR, the CR register and the repository map; the register already records CR-038 as Implemented. The reciprocal Zero-TAF ADR-ZTAF-0006 is recorded in FND-001. The CR file's former Proposed status was inconsistent with the merged implementation record and register entry; this update reconciles it.