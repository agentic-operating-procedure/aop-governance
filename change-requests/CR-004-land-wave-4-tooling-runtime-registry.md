# CR-004: Land the Wave 4 Tooling, Runtime and Registry Repositories

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Tooling, Runtime, Registry |
| Depends on | CR-002, CR-003 |

## 1. Problem statement

The specification (Wave 2) and the substrate (Wave 3) are published, but nothing executes. The programme plan places tooling, runtime and registry in Wave 4, and the Phase 4 exit gate requires that one procedure compile end to end and execute under the guardrail with a complete case record. No Wave 4 repository exists, so the gate cannot be met.

## 2. Objective

Create and seed `aop-toolkit` (tier: tooling), `aop-reference-harness` (tier: runtime) and `aop-registry` (tier: registry) per the repository map, and meet the Phase 4 exit gate.

## 3. Scope

- `aop-toolkit`: the SOP parser (intent hypothesis, NM-INT-3), the variant miner with frequencies, triggers and provenance (NM-STR-1 to NM-STR-3), the decision-rule extractor with thresholds and manifest-carried authority failing closed to prohibited (NM-STR-4 to NM-STR-5, NM-AUT-3), the compiler with the governance boundary (observation supplies structure, the owner supplies bounds, TK-1 to TK-6), the linter reusing the shared `aop-spec` validator, and the CLI. Fixtures: source SOP `RB-LINE-001@v12`, a deterministic 40-case observed corpus, the governance manifest, and the compiled fixture AOP.
- `aop-reference-harness`: the runtime loop (snapshot, match, authorise, execute, record, emit), the guardrail outside the model context with applies_to rule scoping and fail-closed unknown conditions (SEC-1 to SEC-7), the scoped credential broker (ARC-C1 to ARC-C3), the escalation dispatch and evidence bundles (SEC-9), the hash-chained append-only case record with chain verification (SEC-8, SEC-10), the harness's own conformant top-level AOP (SEC-11), and the scripted reference agent. The gate script `gate/end_to_end.py`.
- `aop-registry`: immutable versioned publication with content digests, ref resolution, and provenance chain verification against the case corpus (NM-PRV-4).
- `aop-spec` v0.2.1 (landed alongside): identifier pattern accepts the harness form (HR-) beside the procedure form (AP-); variant identifiers may carry hyphens; decision rules may carry the optional applies_to action scope.

Out of scope: conformance profiles and fixtures (`aop-conformance`, Wave 5), baselines and shadow-mode evaluation (`aop-evaluation`, Wave 5), adoption content.

## 4. Acceptance criteria

- All three repositories are public, with authority-stating READMEs, licence commits, CODEOWNERS, changelog entries, and the local-only doctrine exclusion (ADR-0008).
- The Phase 4 gate passes: the fixture procedure compiles from SOP + cases + manifest, lints clean against the schema, publishes immutably with a matching content digest, resolves, carries a provenance chain that verifies against the corpus, and executes all 40 cases under the guardrail producing complete, chain-verified case records with complete evidence bundles on every dispatched approval.
- The guardrail decision semantics are verified per profile: above-threshold and priority-outage dispatches require approval, below-threshold dispatch executes autonomously, the prohibited escalation threshold blocks dispatch, diagnostics execute autonomously throughout.
- The harness's own top-level AOP validates against the schema (SEC-11, F8).
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

Traced top to bottom against `plans/aop-org-cascade-checklist-org-scope.md`.

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this change request, numbered, recorded before artefacts land |
| A2 | IN SCOPE, no change: no decision is ratified or superseded; D-001 to D-010 all still hold |
| A3 | IN SCOPE, no change: no phase gate or dependency alters; the landing meets the existing Phase 4 gate |
| A4 | IN SCOPE, no change: the ladder is unchanged; three rungs are populated |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and the public description are unchanged |
| A10 | IN SCOPE: the profile repository list gains the three new repositories when they are created |
| B1 to B8 | IN SCOPE: the specification is consumed, not altered; the v0.2.1 schema corrections are recorded in its changelog and are additive (HR- form, hyphenated variant ids, applies_to scope) |
| C1 to C7 | IN SCOPE, no change: the runtime implements the published architecture; the threat model needed no change because no new external input surface was introduced |
| D1 to D5 | IN SCOPE, no change: the substrate is consumed (case corpus shape); its v0.2.0 alignment additions are recorded under CR-005 |
| E1 to E6 | IN SCOPE: this landing satisfies E1 (parser), E2 (variant mining), E3 (rule extraction), E4 (compiler with validated output), E5 (linter), E6 (CLI as the v0.1.0 SDK surface) |
| F1 to F8 | IN SCOPE: this landing satisfies F1 (loop sequence), F2 (guardrail outside the context), F3 (fail closed on unmatched variant), F4 (credential scoping), F5 (escalation threshold and dispatch), F6 (evidence bundle), F7 (complete append-only record), F8 (harness's own top-level AOP, validated) |
| G1 to G4 | IN SCOPE: G1 (publication and versioning rules), G2 (provenance chain verified), G3 (no cross-AOP dependency yet), G4 (catalogue reflects the current artefacts) |
| H1 to H4 | N/A: `aop-conformance` does not exist yet; the clauses it will test are implemented and gate-verified here |
| I1 to I4 | N/A: `aop-evaluation` does not exist yet; the metric names flow from the corpus and the human baseline |
| J1 to J4, K1 to K2 | N/A: Wave 6 repositories do not exist |
| L1 | IN SCOPE: met |
| L2 | IN SCOPE: met; MIT licence, no third-party quoted material |
| L3 | IN SCOPE: met; fixtures use synthetic identifiers, generated tokens are per-run and never committed |
| L4 | IN SCOPE: met; internal links resolve within the three repositories and to the published aop-spec artefacts |
| L5 | IN SCOPE: met; `aop-` prefix and the established document naming convention |
| L6 | IN SCOPE: met; the repositories can be retired without data loss |
| L7 | IN SCOPE: board cards raised for the landing and the gate run |
| L8 | IN SCOPE: organisation project updated with the landing in stage and status |

## 6. What this CR is not

It is not a conformance claim: the harness profile and the certification process are Wave 5. It is not an evaluation claim: no baseline or shadow-mode comparison is asserted here. It is not a production deployment: the approver is a policy object behind the dispatch interface, and the observation capture surfaces are fixtures.

## 7. Implementation

Implemented in the `v0.1.0` landings of `aop-toolkit`, `aop-reference-harness` and `aop-registry`, with `aop-spec` v0.2.1. The gate output is recorded in the cross-check stage.
