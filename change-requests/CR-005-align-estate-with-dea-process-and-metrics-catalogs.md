# CR-005: Align the Estate with the OpenDEA Process and Metrics Catalogs

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Substrate, Specification |
| Depends on | CR-002, CR-003 |

## 1. Problem statement

The estate's observed work (cases, tasks, steps) and its operating procedures carry no association with the enterprise's own process architecture or its canonical performance metrics. The programme owner directs an association between the substrate's TASK entity and the process levels of `technehub-labs/dea-catalog-business-processes`, and requires that performance and business value metrics reference the canonical metrics in `technehub-labs/dea-catalog-metrics` or lodge an explicit gap for that catalog to fill. Without the association, AOP work cannot be read against the enterprise architecture, and baseline metrics float free of the catalog that binds metrics to `dea:BusinessProcess`.

## 2. Objective

Associate the substrate's CASE, TASK and STEP entities with the DEA Business Process Catalog levels by reference or declared gap, and bind the AOP's human baseline metrics to canonical `dea:metric-*` records by reference or declared gap, with invented identifiers prohibited on both sides.

## 3. Scope

- `aop-context-graph` v0.2.0: the process alignment rules (CG-PA-1 to CG-PA-6) in `docs/aop-process-alignment-substrate-scope.md`; the case record schema carries optional `process_ref` on the case (process or activity level) and on tasks (activity or task level), the `process_alignment_gap` declaration, and `process_catalog_version` in provenance. The mapping: CASE to `processes:process-*`, TASK to `processes:activity-*`, STEP to `processes:task-*` where the catalog's decomposition reaches that level.
- `aop-spec` v0.2.0: NM-INT-4 (an AOP SHOULD carry a process alignment block: catalog reference or declared gap, plus the catalog version; association by reference and never by copy; inventing an identifier prohibited) and NM-INT-5 (human baseline metrics bound to canonical `dea:metric-*` records or declared as gaps to lodge as contributions to `dea-catalog-metrics`); the optional `process_alignment` schema block; matching validator semantic checks; the specimen demonstrates both sides: three canonical metric references (`dea:metric-mean-time-to-detect`, `dea:metric-ai-incident-escalation-compliance`, `dea:metric-cell-outage-rate`) and two declared metric gaps plus a declared process gap.
- The compiler (`aop-toolkit`, CR-004) passes the alignment block through and invents nothing.

Out of scope: lodging the contributions themselves (the gaps are the work queue; lodging happens in the DEA catalogs' own contribution processes, tracked under CR-006); any change to the DEA catalogs.

## 4. Acceptance criteria

- The alignment rules carry stable identifiers (CG-PA-1 to CG-PA-6) and the reference-or-gap rule is stated with the prohibition on invented identifiers.
- The case record schema validates a case carrying `process_ref`, `process_alignment_gap` and `process_catalog_version`.
- The specimen AOP validates with its alignment block, and the validator rejects an alignment block with neither reference nor gap, and a metric binding with neither metric_ref nor gap.
- Catalog versions are recorded wherever references are.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: recorded here; no decision, gate, or ladder change |
| A5, A6 | IN SCOPE, no change: the hierarchy and glossary are unchanged; CG-PA and NM-INT identifiers extend the substrate and specification clause families |
| A7, A8, A9 | IN SCOPE, no change: no non-goal shifts (the association is by reference; no framework pull), no positioning claim changes, no public description change |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B3 | IN SCOPE: NM-INT-4 and NM-INT-5 are new normative text within the Intent dimension (B1); no identifier form or versioning change (B2, B3) |
| B4 | IN SCOPE: the aop-spec schema gained the optional block; the validator was extended and the full fixture gate re-run unchanged |
| B5 to B8 | IN SCOPE, no change: conformance clauses, skill contract and security clauses untouched |
| C1 to C7 | IN SCOPE, no change: architecture documents already cite the substrate and the `cg://` scheme; no layer, boundary, mechanism, stage or topology changes |
| D1 to D5 | IN SCOPE: D1 (entity model: attributes added, entity types unchanged), D2 (case schema regenerated and validated), D3 to D5 (stitching, drift, privacy posture unchanged) |
| E1 to E6 | IN SCOPE, no change at CR-003 time; the compiler passes the block through as recorded under CR-004 |
| F1 to F8, G1 to G4, H1 to H4, I1 to I4, J1 to J4, K1 to K2 | N/A with the reasons recorded in CR-003 and CR-004 |
| L1 to L8 | IN SCOPE: met, same audit method as CR-003 |

## 6. What this CR is not

It is not a change to the DEA catalogs and asserts no authority over them: the catalog remains the single authority for what the enterprise's processes and metrics are, and the mapping direction is AOP to those standards, never a copy into this estate. It does not resolve any of the open metamodel reconciliation points from CR-002.

## 7. Implementation

Implemented in `aop-context-graph` v0.2.0 and `aop-spec` v0.2.0, with the v0.2.1 schema corrections recorded separately under CR-004.
