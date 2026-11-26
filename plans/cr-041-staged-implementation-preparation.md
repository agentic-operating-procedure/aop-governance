# CR-041 staged implementation preparation

**State:** Preparation proposal; CR-041 remains Proposed pending formal owner acceptance.  
**Reconciled:** 2026-11-26  
**Origin:** AO-WE-001 worked-example integration, Agentic-Operation PR #14 merged.

## Decision and evidence

- CR-041 is present in the AOP governance register with status Proposed.
- The CR covers temporal/corpus semantics, procedure branches, authority and human escalation, action/skill coverage, deterministic validation, conformance and replay.
- The toolkit README explicitly says the corpus validator is diagnostic and the source corpus remains unresolved.
- The case schema and stitching documents already normatively define elapsed cycle time as end minus start, deterministic stitching, case identity and provenance. Stage 1 must not redundantly redefine these; it must identify missing precision and reconcile conflicting diagnostic counts against a pinned source revision.
- AOP governance distinguishes ADR decision, CR proposal, and finding evidence. This preparation is not ratification.

## Work-package sequencing

| WP | Owner repo | Scope | Depends | Gate / evidence |
|---|---|---|---|---|
| WP-0 | aop-governance | Formal CR-041 acceptance, owner ledger, dependencies | Owner decision | Ratified ADR or equivalent |
| WP-1 | aop-context-graph | Temporal semantics disposition: timezone/format, event vs capture timestamps, ordering dimensions, boundary exceptions, cycle-time unit | WP-0 | Normative decision + schema/doc mapping + tests or test contract |
| WP-2 | aop-toolkit | Corpus diagnosis and validator against WP-1; fixture repair only after semantic adjudication | WP-1 | Pinned input digest, change rationale, deterministic validation |
| WP-3 | aop-toolkit; aop-spec conditional | SOP branch semantics, action/skill map, authority decision rules | WP-0; domain decisions | Valid/invalid examples; explicit unbound actions |
| WP-4 | aop-reference-harness; aop-conformance | Enforcement, negative tests, human escalation route | WP-3 | Fail-closed tests and evidence |
| WP-5 | OpenDEA catalogue owner (separate) | Process identity/applicability disposition | Process owner input | Separate OpenDEA CR or decision; no AOP unilateral catalog edits |
| WP-6 | aop-registry/aop-evaluation/aop-examples conditional | Version publication, reproducible replay, consumer example synchronization | WP-2 to WP-5 | Pinned artefacts, logs, digest, limitations |

## Known discrepancy to resolve before corpus mutation

CR-041's own reported counts (36 later than end, 35 earlier than start, 36 non-monotonic, 40 duration mismatch) differ from previous independent diagnostics recorded in AO-WE-001 (including 40/40 duration mismatches and different boundary/order counts). Do not treat either count set as authoritative until the exact corpus blob, diagnostic definition, timezone assumptions, and code version are pinned and rerun.

## First technical deliverable

Prepare an investigation-only aop-context-graph change request/PR documenting temporal/event semantics and traceability to existing normative rules. It must not alter fixture data, introduce new assumptions, or silently change schema compatibility. The proposed deliverable should distinguish:
- event time vs capture/observation time;
- chronology vs procedural order vs source sequence;
- timezone/offset and precision requirements;
- case interval boundary and exception event classes;
- elapsed cycle duration vs active work duration and metric units;
- provenance for adjudicated event inclusion/exclusion.

## Open owner decisions

1. Domain owner adjudicates valid dispatch/resolution branches and parallelism.
2. Domain owner confirms dispatch authority minimum and restrictive-rule precedence.
3. Human escalation route and prohibited action representation are approved.
4. Actions without governed skill/tool bindings are non-executable.
5. OpenDEA process owner decides applicable process record(s); AOP does not create them.
