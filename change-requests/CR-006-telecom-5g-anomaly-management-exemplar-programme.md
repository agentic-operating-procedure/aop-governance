# CR-006: Commit the Telecom 5G Anomaly Management Exemplar Programme

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Adoption, Demonstration |
| Depends on | CR-004, CR-005 |

## 1. Problem statement

The programme's Demonstrated-level authority (the third level in the concept model) requires a complete, reproducible demonstration: an adopter following published artefacts from a classic SOP through compilation to governed execution with evidence. No such demonstration exists. The programme owner directs a holistic walkthrough in a concrete, demanding scenario: a telecom service provider managing a complex 5G mobile network, with humans and AI agents working the anomaly management domain, converting classic SOPs into AOPs and delivering measurable performance and business value.

## 2. Objective

Produce the end-to-end exemplar set for a 5G telecom service provider's anomaly management domain, in `aop-examples` (Wave 6) with adoption guidance cross-linked from `aop-adoption`, leveraging the OpenDEA catalogs of `technehub-labs` so the demonstration reads against the enterprise architecture and lands its metrics in the canonical catalog.

## 3. Scope

The exemplar programme covers, for the scenario domain (mobile network anomaly management; candidates: alarm correlation and triage, cell outage management, RAN anomaly detection follow-up, KPI degradation investigation):

1. **SOP intake.** Two to three classic telecom SOPs (anomaly triage, escalation, outage communication), parsed to intent hypotheses with `aop-toolkit`.
2. **Observation.** A synthetic but realistic 5G anomaly case corpus stitched under the substrate semantics, with human and AI-agent actors drawn from `technehub-labs/dea-catalog-actors` (which covers human, team, system and AI-agent performers).
3. **Compilation.** SOPs compiled to AOPs: variants with observed frequencies, decision rules with thresholds (for example, anomaly severity scores, escalation thresholds, outage impact classes), exception and escalation patterns, governance bounds.
4. **Governed execution.** The compiled AOPs running inside the reference harness: agents proposing actions, the guardrail enforcing authority, human approvals for high-impact actions (crew dispatch, customer communication), case records and evidence bundles throughout. Where the scenario needs anomaly detection capability, the AI/ML model and its deployment reference `technehub-labs/dea-catalog-ai-ml-models` and `dea-catalog-model-deployments`.
5. **Metrics and business value.** Before-and-after comparison against the human baseline: mean time to detect, triage time, first-pass resolution, escalation precision, drift detection latency. Every metric binds to a canonical `dea:metric-*` record in `technehub-labs/dea-catalog-metrics` where one exists; where none exists, the gap is lodged as a metric contribution to that catalog (per NM-INT-5 and CG-PA-5 to CG-PA-6) and tracked to closure. Known gaps already identified: p50 mean time to restore and first-pass fix rate have no canonical metric records.
6. **Process alignment.** The scenario's processes and their activity and task decomposition lodged as contributions to `technehub-labs/dea-catalog-business-processes` (no canonical network fault or anomaly management process record exists in the catalog yet), with the published `processes:process-*` references then adopted by the AOPs and the case corpus per CG-PA-1 to CG-PA-4.
7. **Reproducibility.** Narrated walkthroughs and reproduction scripts per the `aop-examples` charter, runnable from the published Wave 4 toolchain.

## 4. Acceptance criteria

- A reader can take the published artefacts and reproduce the walkthrough unaided: SOP in, governed agent execution and case records out, metrics compared against the human baseline.
- Every metric in the walkthrough resolves to a `dea:metric-*` reference or a tracked, lodged gap in `dea-catalog-metrics`.
- Every process in the walkthrough resolves to a `processes:process-*` reference or a tracked, lodged gap in `dea-catalog-business-processes`.
- The Wave 6 gate holds: the pilot procedure is migrated by a team other than the programme stewards, or the walkthrough is explicitly marked steward-run until that happens.
- The walkthrough states plainly what is synthetic (the observation corpus) and what the demonstration does and does not prove.

## 5. Cascade audit

This CR commits future work; the audit runs again when the exemplar lands. Forward audit: the exemplars touch K1 to K2 (demonstration), J1 to J4 (adoption, cross-linked), I1 to I4 (metrics measured against the baseline), and G4 (catalogue reflects the exemplar AOPs). No concept, model, architecture or substrate change is expected; any that emerges arrives as its own change request.

## 6. What this CR is not

It is not a Wave 6 landing now: `aop-examples` and `aop-adoption` land after Waves 5 (conformance and evaluation) per D-010. It is not a change to the DEA catalogs; contributions follow those catalogs' own processes. It is not a production deployment on a live 5G network; the scenario is a demonstration estate.

## 7. Implementation

To be implemented across `aop-examples` and `aop-adoption` at Wave 6, with the DEA catalog contributions lodged as they are identified so the canonical references exist by landing time.
