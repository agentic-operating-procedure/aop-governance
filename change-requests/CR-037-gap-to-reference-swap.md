# CR-037: The Gap-to-Reference Swap for the Published Metric Records

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-08 |
| Owner | Emmanuel A. Otchere |
| Layer | Demonstration |
| Depends on | CR-036 (merged), the DEA catalog publications (metrics PR #17, processes PR #233, both merged 2026-11-07) |

## 1. Problem statement

The two lodged metric records were published by the metrics catalog with the proposed identifiers, and the process contribution was accepted into the business-processes catalog. Per CG-PA-4 and NM-INT-5, the declared gaps in the exemplar manifest must now be replaced with the canonical references, so the AOP artefacts carry references rather than gaps.

## 2. Objective

Execute the swap: metric gaps to canonical references; the process gap updated to its true state (contribution accepted, canonical entity assignment pending the catalog's maintainer reclassification); the exemplar AOPs recompiled and all gates re-run.

## 3. Scope

`aop-examples` only: `manifests/ran-anomaly.json` (the two metric gaps become `dea:metric-mttr-anomaly-p50-ran-operations` and `dea:metric-first-pass-anomaly-resolution-ran-operations`; the process gap text records the accepted-contribution state); the dev-cohort manifest aligned; the compiled AOPs recompiled; the walkthrough section 6c; the README metric-bindings row; version 0.4.0.

## 4. Acceptance criteria

- All five metric bindings are canonical references; none remain as gaps.
- The process gap states the true pending state rather than claiming assignment.
- The lint, the adapter self-test and the Wave 6 reproduction gate all pass on the recompiled artefacts.
- L1 clean.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A2 to A10 | IN SCOPE, no change |
| B2 | IN SCOPE: the swap exercises NM-INT-5 exactly as written; no clause changes |
| D1 | IN SCOPE, no change: the substrate's alignment rules are consumed |
| K1, K2 | IN SCOPE: the walkthrough and the reproduction path updated and re-run green |
| B1, B3 to C7, D2 to J4 | N/A or no change |
| L1, L4 | IN SCOPE: met |

## 6. What this CR is not

It is not the process-reference swap: that completes when the catalog's maintainer reclassification assigns the canonical `processes:process-*` entity, and a follow-up CR records it. It is not a new publication claim: the references cite what the catalogs published, no more.

## 7. Implementation

Implemented in aop-examples v0.4.0.
