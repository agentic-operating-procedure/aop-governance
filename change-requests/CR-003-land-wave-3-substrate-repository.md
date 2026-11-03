# CR-003: Land the Wave 3 Substrate Repository

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Substrate |
| Depends on | CR-002 |

## 1. Problem statement

The repository map places `aop-context-graph` before tooling, runtime and registry, because everything above the substrate is downstream of the observation capability: without it there is no variant mining, no reconciliation of intent against reality, and no way to know that a procedure has drifted. No substrate repository exists, so `aop-toolkit` (Wave 4) would have to invent the graph it mines from.

## 2. Objective

Create and seed `aop-context-graph` (tier: substrate) per the repository map: the Context Graph of Work entity model, the case schema, the case stitching semantics, the Digital Twin of Operations, the drift detection obligations, and the observation posture, with machine-readable schemas for the graph export and the stitched case.

## 3. Scope

`aop-context-graph` only:

- Entity model: the ten entities (CASE, TASK, STEP, ACTOR, APPLICATION, DECISION, RULE, EXCEPTION, ESCALATION, OUTCOME), ten relationships with cardinalities, the evidence obligation (CG-2), role-not-person modelling (CG-1), and the alignment mapping to the staged metamodel's runtime (E61 to E75), exception (E76 to E86) and governance (E87 to E103) vocabularies.
- Case schema: the stitched case as the unit of compilation, provenance and evaluation, with the closed outcome dispositions shared with `aop-spec` (NM-STR-14) and the domain metric set fed to `aop-evaluation`.
- Stitching: domain correlation keys as case identity (CG-S1 to CG-S2), join and anti-join rules, handoff integrity, quarantine of unstitchable events (CG-S10), and deterministic versioned stitching (CG-S13 to CG-S14).
- Twin: the five aspects, the distinction from a knowledge graph, the freshness obligation (ARC-D2).
- Drift: five drift classes including coverage drift (the observation of the observation), declared drift profiles, detection latency as a measured metric, and the recalibration trigger that hands drift to governance without mutating any AOP (CG-D6).
- Observation posture: declared capture surface (CG-O1), at-source exclusion of personal content classes (CG-O3), role projection (CG-O5), minimisation, retention and access rules, binding runtime case records equally (CG-O8).
- Schemas: `schema/context-graph.schema.json` and `schema/case-record.schema.json`, smoke-tested against the shared reference validator in `aop-spec`, which receives a guard fix so its AOP-specific normative checks do not fire on non-AOP documents.

Out of scope: the stitcher implementation, the miners and the compiler (`aop-toolkit`, Wave 4); the runtime that emits execution evidence (`aop-reference-harness`, Wave 4); event schemas of specific capture sources (estate-specific configuration).

## 4. Acceptance criteria

- The repository is public, with a README stating authority in one sentence, a licence commit, CODEOWNERS, a changelog entry, and the local-only doctrine exclusion (ADR-0008).
- The ten-entity model and the closed relation set are published with cardinalities.
- Both schemas parse and validate a valid fixture through the shared reference validator.
- The drift classes, the stitching rules and the posture rules carry stable CG-* identifiers.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

Traced top to bottom against `plans/aop-org-cascade-checklist-org-scope.md`.

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this change request, numbered, recorded before artefacts land |
| A2 | IN SCOPE, no change: no decision is ratified or superseded; D-001 to D-010 all still hold |
| A3 | IN SCOPE, no change: no phase gate or dependency alters; the landing advances the estate within the existing plan |
| A4 | IN SCOPE, no change: the ladder is unchanged; the substrate rung is populated |
| A5 | IN SCOPE, no change: the six-level hierarchy is unchanged; the substrate maps to it, it does not alter it |
| A6 | IN SCOPE, no change: no new term enters the glossary; the substrate reuses ratified vocabulary and carries CG-* identifiers of its own |
| A7 | IN SCOPE, no change: nothing pulls toward a framework, workflow engine or evaluation suite; the observation posture in particular keeps the estate out of surveillance |
| A8 | IN SCOPE, no change: no external positioning claim changes |
| A9 | IN SCOPE, no change: the public one-paragraph description is unchanged |
| A10 | IN SCOPE: the profile repository list gains `aop-context-graph` when it is created |
| B1 to B3, B5 to B8 | IN SCOPE, no change: the normative model is consumed, not altered; the `cg://` scheme is used as defined |
| B4 | IN SCOPE, no change: the aop-spec schema is untouched; the shared validator receives a guard fix (skip AOP-specific checks where the document declares no AOP structure), and the full aop-spec gate was re-run unchanged after the fix |
| C1 to C7 | IN SCOPE, no change: the pipeline and trust documents in `aop-architecture` cite the substrate; this landing implements the substrate side of ARC-P1, ARC-P2, ARC-P5 and ARC-D2 without altering them |
| D1 to D5 | IN SCOPE: this is the landing of the substrate tier; D1 (entity model) and D2 (graph schema) are satisfied by the new artefacts, D3 (stitching), D4 (drift) and D5 (privacy posture) likewise |
| E1 to E6 | N/A: `aop-toolkit` does not exist yet; the graph it will mine is now fixed |
| F1 to F8 | N/A: `aop-reference-harness` does not exist yet; CG-O8 and the case-record modelling bind it in advance |
| G1 to G4 | N/A: `aop-registry` does not exist yet |
| H1 to H4 | N/A: `aop-conformance` does not exist yet |
| I1 to I4 | N/A: `aop-evaluation` does not exist yet; the metric names it will register are now defined at the substrate |
| J1 to J4, K1 to K2 | N/A: Wave 6 repositories do not exist |
| L1 | IN SCOPE: met |
| L2 | IN SCOPE: met; MIT licence, no third-party quoted material |
| L3 | IN SCOPE: met; fixtures use synthetic identifiers and no tokens, keys or internal addresses |
| L4 | IN SCOPE: met; all new internal links resolve within the repository and to `aop-spec` and `aop-architecture` artefacts that exist |
| L5 | IN SCOPE: met; `aop-` prefix and the `<topic>-<scope>.md` convention |
| L6 | IN SCOPE: met; the repository can be retired without data loss |
| L7 | IN SCOPE: board cards raised for the landing and the schema smoke test |
| L8 | IN SCOPE: organisation project updated with the landing in stage and status |

## 6. What this CR is not

It is not an implementation of the stitcher or the miners; the substrate lands as specification and schema, and the executables are Wave 4. It is not a privacy legal review: CG-O1 to CG-O8 require each estate's own privacy review to approve its capture surface declaration. It is not a reconciliation decision on the staged metamodel; the alignment mapping is informative and the open points from CR-002 remain open.

## 7. Implementation

Implemented in the `v0.1.0` landing of `aop-context-graph`. Schema smoke test output recorded in the cross-check stage.
