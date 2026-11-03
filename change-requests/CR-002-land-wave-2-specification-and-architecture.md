# CR-002: Land the Wave 2 Specification and Architecture Repositories

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Specification, Architecture |
| Depends on | CR-001 |

## 1. Problem statement

The programme plan places Phase 2 (normative specification) and Phase 3 (reference architecture) before any substrate, tooling or runtime work, and the cross-phase constraint binds every later repository to interfaces the specification fixes first. No specification or architecture repository exists, so nothing downstream can be built without inventing unratified interfaces.

## 2. Objective

Create and seed `aop-spec` (tier: specification) and `aop-architecture` (tier: architecture) per the repository map, satisfying the Phase 2 exit gate: a specimen AOP validates against the machine-readable schema, and the reference validator fails correctly on a deliberately broken specimen.

## 3. Scope

- `aop-spec`: the eight-dimension normative model as clauses, the network-native procedure structure, the identifier and versioning model with three-dimension lifecycle status, the Agent Skill contract annex (D-003), the normative security clauses (D-004), the conformance clauses, the machine-readable schemas (AOP document, Agent Skill declaration, evidence bundle), the reference validator, and the fixture set. The source metamodel documents supplied by the programme owner are mapped onto the normative model, with the open reconciliation points surfaced rather than decided.
- `aop-architecture`: the layered reference architecture, the trust architecture (prevent, verify, oversee, audit, with the guardrail decision flow, the credential model and the recovery model), the compile-and-run pipeline with the shadow-mode bridge and the feedback path, the three deployment topologies, and the threat model.
- `aop-governance`: this change request. No other governance artefact changes: the estate shape, the phase gates and the repository map are unchanged by this landing.

Out of scope: `aop-context-graph`, `aop-toolkit`, `aop-reference-harness`, `aop-registry`, and all Wave 5 and 6 repositories. Reconciliation of the open metamodel mapping points (see `aop-spec/docs/aop-metamodel-mapping-specification-scope.md`, section 5) is decided by the programme owner in later change requests.

## 4. Acceptance criteria

- Both repositories are public, with a README stating authority in one sentence, a licence commit, CODEOWNERS, a changelog entry, and the local-only doctrine exclusion (ADR-0008).
- The specimen AOP document validates against `aop-spec/schema/aop-document.schema.json` with the reference validator.
- At least five deliberately broken specimens, each generated from the valid specimen with exactly one defect, fail with a diagnostic naming the violated clause.
- The Agent Skill contract and the normative security clauses are published as normative text in `aop-spec` (D-003, D-004).
- `aop-architecture` names the interfaces that Phases 4 and 5 implement against.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

Traced top to bottom against `plans/aop-org-cascade-checklist-org-scope.md`.

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this change request, numbered, recorded before artefacts land |
| A2 | IN SCOPE, no change: no decision is ratified or superseded; D-001 to D-010 all still hold. The landing implements them |
| A3 | IN SCOPE, no change: no phase gate or dependency alters; the landing advances Phases 2 and 3 within their existing gates |
| A4 | IN SCOPE, no change: the ladder is unchanged; two existing rungs are populated |
| A5 | IN SCOPE, no change: the six-level hierarchy is cited, not altered; open hierarchy questions are surfaced, not decided |
| A6 | IN SCOPE, no change: no new term enters the glossary; the normative model reuses ratified vocabulary |
| A7 | IN SCOPE, no change: nothing in the landing pulls toward a framework, workflow engine or evaluation suite; the non-goals hold |
| A8 | IN SCOPE, no change: no external positioning claim changes |
| A9 | IN SCOPE, no change: the public one-paragraph description is unchanged |
| A10 | IN SCOPE: the profile repository list gains `aop-spec` and `aop-architecture` when they are created |
| B1 to B8 | IN SCOPE: this is the landing of the specification tier; every line is satisfied by the new artefacts rather than changed |
| C1 to C7 | IN SCOPE: satisfied by the new architecture artefacts; the threat model is published in the same landing that introduces the surfaces |
| D1 to D5 | N/A: `aop-context-graph` does not exist yet; the substrate interfaces it will satisfy are named in `aop-architecture` |
| E1 to E6 | N/A: `aop-toolkit` does not exist yet; the schema it will compile against is now fixed |
| F1 to F8 | N/A: `aop-reference-harness` does not exist yet; the runtime clauses it will implement are now normative |
| G1 to G4 | N/A: `aop-registry` does not exist yet; the identifier scheme it will resolve is now fixed |
| H1 to H4 | N/A: `aop-conformance` does not exist yet; the clauses it will test are now fixed |
| I1 to I4 | N/A: `aop-evaluation` does not exist yet; the human baseline obligation is now normative in the Assurance dimension |
| J1 to J4, K1 to K2 | N/A: Wave 6 repositories do not exist |
| L1 | IN SCOPE: met; published artefacts avoid em dashes, ellipsis glyphs and vendor references |
| L2 | IN SCOPE: met; MIT licence in both repositories, no third-party quoted material |
| L3 | IN SCOPE: met; fixtures use synthetic identifiers and no tokens, keys or internal addresses |
| L4 | IN SCOPE: met; all new internal links resolve within the two repositories and to `aop-governance` plan files |
| L5 | IN SCOPE: met; names follow `aop-` prefix and the `<topic>-<scope>.md` document convention |
| L6 | IN SCOPE: met; both repositories can be retired without data loss; the estate predates the landing unchanged |
| L7 | IN SCOPE: board cards raised for the landing and the validation run |
| L8 | IN SCOPE: organisation project updated with the landing in stage and status |

## 6. What this CR is not

It is not a reconciliation decision on the staged metamodel. The mapping document surfaces seven open points; each reaches the owner as its own change request if pursued. It is not a Phase 2 exit claim until the validation output is recorded in this repository by the cross-check stage. It does not create any repository beyond the two named.

## 7. Implementation

Implemented in the `v0.1.0` landings of `aop-spec` and `aop-architecture`. Validation run recorded in the cross-check stage output.
