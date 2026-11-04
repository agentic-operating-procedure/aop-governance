# CR-008: Land the Wave 6 Adoption and Exemplar Repositories

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Adoption, Demonstration |
| Depends on | CR-004, CR-005, CR-006, CR-007 |

## 1. Problem statement

The estate is functionally complete through Wave 5 (twelve repositories, Phases 0 to 5 gates passed), but the programme is incomplete without adoption and demonstration surfaces: an adopter cannot migrate a procedure unaided, and the programme's Demonstrated-level authority has no worked demonstration. CR-006 committed the telecom 5G anomaly management exemplar programme; it lands here.

## 2. Objective

Create and seed `aop-adoption` (tier: adoption) and `aop-examples` (tier: adoption, deferred to Wave 6 per D-010), delivering the six-stage playbook, the maturity model, the adoption scenarios, the organisational change guidance, the adopter checklists, and the 5G anomaly management exemplar with its reproduction gate.

## 3. Scope

- `aop-adoption` v0.1.0: the six-stage procedural engineering playbook (decomposition, operational grounding, autonomy disposition, AOP specification, harness engineering, verification and assurance), each stage with a gate and evidence obligations; the four-stage maturity model with the honest-stage rule and regression reporting; the three adoption scenarios (pilot, brownfield, regulated and high-risk); the organisational change guidance (roles, decision rights, corridor execution to exception ownership); the per-stage adopter checklists, steward-free.
- `aop-examples` v0.1.0: the 5G RAN anomaly management walkthrough per CR-006, leveraging the technehub-labs catalogs as directed: the deterministic 45-case corpus (5 anomaly profiles; human and AI-agent roles per `dea-catalog-actors` vocabulary), the governance manifest, the compiled `AP-RAN-014@v0.1.0`, governed execution in the harness, the shadow evaluation, the DEA contribution drafts (one process, two metrics, prepared for lodging), and the reproduction gate.
- Accompanying patches, recorded in their own repositories: `aop-toolkit` v0.1.1 (observed decision conditions kept verbatim; truncating compound conditions dropped guards), `aop-evaluation` v0.1.1 (the shadow comparator measures authority fidelity: conservative deviations surfaced separately from violations; per-action comparison; approver roles from approval-kind handoffs), `aop-spec` v0.2.2 (coordination handoffs may carry kind: approval or informational; default approval).

## 4. Acceptance criteria

- Both repositories are public, with authority-stating READMEs, licence commits, CODEOWNERS, changelog entries, and the local-only doctrine exclusion (ADR-0008).
- The reproduction gate passes: corpus determinism, compilation, lint, registry publication with verified provenance, AOP-DOC-1 conformance, 45 cases executed under the guardrail (245 actions, 10 approvals, 20 prohibited, complete chain-verified case records), shadow agreement 1.0 with zero authority violations and 25 conservative deviations.
- The walkthrough states its status plainly: steward-run, synthetic corpus, rule fidelity and mechanism correctness claimed, adoption and live performance not claimed.
- Every metric in the walkthrough resolves to a canonical `dea:metric-*` reference or a prepared contribution draft; the process gap carries its prepared contribution draft.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: recorded here; no decision is ratified or superseded; the estate shape is complete as mapped (D-010's deferral now discharged) |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and public description unchanged |
| A10 | IN SCOPE: the profile repository list gains the two new repositories when created, completing the fourteen |
| B1 to B8 | IN SCOPE: the specification is consumed; v0.2.2 adds the handoff kind as additive schema |
| C1 to C7 | IN SCOPE, no change: the exemplar deploys the published topologies and mechanisms; nothing architectural is added |
| D1 to D5 | IN SCOPE, no change: the corpus follows the substrate schemas and posture |
| E1 to E6 | IN SCOPE, no change: the toolchain is consumed; v0.1.1 corrects condition truncation found by this chain, recorded in its changelog |
| F1 to F8 | IN SCOPE, no change: the harness is consumed as published |
| G1 to G4 | IN SCOPE, no change: the exemplar AOP is published through the registry in the gate run |
| H1 to H4 | IN SCOPE, no change: AOP-DOC-1 is run on the exemplar document in the gate |
| I1 to I4 | IN SCOPE: metric definitions are consumed; the baseline and shadow method is applied as published; v0.1.1 refines the comparator per its changelog |
| J1 to J4 | IN SCOPE: this landing satisfies the adoption tier (playbook, maturity, scenarios, change guidance) |
| K1 to K2 | IN SCOPE: the walkthrough and the reproduction gate are published and re-runnable |
| L1 to L8 | IN SCOPE: met, same audit method as CR-007 |

## 6. What this CR is not

It is not the Wave 6 exit claim: the gate requires a pilot migrated by a team other than the programme stewards, and the walkthrough states steward-run plainly. It is not a live-performance or business-value claim: the improvement claim is deliberately absent until the live pilot measures against the published baseline. It does not lodge the DEA contributions: the drafts are prepared and await lodging through the catalogs' own processes.

## 7. Implementation

Implemented in the `v0.1.0` landings of `aop-adoption` and `aop-examples`, with the accompanying patches to `aop-toolkit` (v0.1.1), `aop-evaluation` (v0.1.1) and `aop-spec` (v0.2.2). The gate output is recorded in the cross-check stage.
