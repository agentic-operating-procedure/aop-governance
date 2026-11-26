# CR-041: Restore Fault-Management Fixture Integrity and Execution-Policy Consistency

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-26 |
| Owner | Emmanuel A. Otchere |
| Layer | Model |
| Depends on | AO-WE-001 (Agentic-Operation, merged); reconcile against CR-011, CR-016, CR-018, CR-020 and the current AOP specification/conformance clauses before implementation |

## 1. Problem statement

The AOP fault-management reference fixture is not currently a reliable basis for validating execution semantics or deriving operational measures. The 40-case corpus contains material inconsistencies between case boundaries, event timestamps, event ordering and the declared `outcome.cycle_time`. The SOP and governance manifest also disagree on the authority required to dispatch external resources and on the treatment of on-call escalation. Finally, the manifest declares `resolve-fault` and `reconcile-inventory` as permitted actions without corresponding skill declarations.

The defects are not isolated documentation issues. They undermine the integrity of the reference scenario as an input to compilation, conformance, replay and evaluation. A successful parser or harness run against these inputs would not establish that the procedure's timing, authority or action contracts are coherent.

The findings are recorded in the merged Agentic-Operation worked example, [AO-WE-001](https://github.com/Agentic-Operation/.github/blob/main/docs/examples/AO-WE-001-fault-management-opendea-aop-worked-example.md), particularly Sections 7, 8, 10 and 11.

## 2. Objective

Restore the fault-management reference scenario to a semantically coherent, fail-closed and reproducibly verifiable state, such that:

1. case timing and event-order semantics are explicit, machine-checkable and consistent with the case data;
2. the SOP, governance manifest and runtime authority enforcement express one unambiguous decision-rights model;
3. human escalation is represented as a governed handoff, distinct from an agent-executable action;
4. every permitted side-effecting action has an explicit, governed skill/tool binding, or is not executable;
5. deterministic validation and negative conformance tests prevent recurrence; and
6. the corrected scenario can be compiled, conformance-checked and replayed with pinned source artefacts and reproducible evidence.

This CR repairs the reference scenario and its validation contract. It does not assert that the scenario is a production deployment or that its fixture values represent measured enterprise performance.

## 3. Scope

### 3.1 Case-corpus semantics and integrity

**Owners:** `aop-context-graph` (case model and stitching semantics), `aop-toolkit` (fixture, parser/linter and deterministic validation), with `aop-evaluation` consulted where metric semantics are affected.

- Define the meaning, unit, timezone and boundary semantics of `started_at`, `ended_at`, step timestamps and `outcome.cycle_time`.
- Define whether step-array order represents procedural order, event order, capture order or another ordering. If more than one order is needed, represent them separately rather than overloading array position.
- Define how concurrent, delayed, pre-run and post-run events are represented. An event outside the declared run interval must be explained by its event class and provenance, or rejected by validation.
- Define `cycle_time` as a named duration with an explicit unit and derivation. If it means elapsed run duration, reconcile it to `ended_at - started_at`. If it means active processing time or another measure, rename or qualify it and define the calculation, exclusions and source fields.
- Correct or regenerate the 40-case fixture against the agreed semantics. Preserve source provenance and record the resulting corpus digest.
- Add deterministic corpus validation to the toolkit and ensure invalid cases fail with actionable diagnostics.

The observed mechanical findings to be reconciled are: 36/40 cases contain an event later than `ended_at`; 35/40 contain an event earlier than `started_at`; 36/40 have non-monotonic step timestamps; and 40/40 have a declared `outcome.cycle_time` that differs from the direct start/end interval. These counts describe the inspected corpus revision, not a normative assumption about what every event must mean.

### 3.2 Procedure sequence and branch semantics

**Owners:** `aop-toolkit` for the fault-management fixture and compilation; `aop-spec` if the current procedure-structure clauses do not adequately express the required branch semantics.

- Reconcile the SOP's stated order (`resolve-fault` before `dispatch-field-crew`) with the observed fixture sequence, which frequently records dispatch before resolution.
- Determine whether dispatch-before-resolution is a legitimate branch, a parallel activity, a human-led intervention path or a fixture defect.
- Encode the selected path as explicit decision/exception/precedence semantics. Do not rely on an ambiguous list order to imply both workflow precedence and event chronology.
- Add positive and negative fixtures covering the valid branches and invalid orderings.

The CR does not prescribe that all cases must follow one linear sequence. The domain owner must establish the intended operational branches from the source procedure and valid observations.

### 3.3 Authority consistency and human escalation

**Owners:** `aop-toolkit` for the fault-management SOP and manifest; `aop-reference-harness` for enforcement; `aop-spec` and `aop-conformance` only where a normative clause or conformance profile is missing.

- Reconcile the decision-rights ladder, authority map and SOP decision rules for `dispatch-field-crew`.
- Treat dispatch of external resources as requiring at least the authority class specified by the decision-rights ladder. A lower repair-time estimate must not silently reduce a more restrictive minimum authority requirement.
- Define deterministic combination and precedence when multiple authority conditions apply. The effective authority must be the most restrictive applicable requirement; a default or threshold rule must not override a stricter applicable rule.
- Preserve the priority-customer/active-outage approval condition and define how it combines with the dispatch minimum.
- Distinguish the prohibited agent action `engage-on-call-engineer` from a permitted human escalation/handoff to the on-call engineer. If the intended behaviour is human escalation, represent it as a coordination/escalation route enforced by the harness, not as permission for the agent to perform a prohibited action.
- Fail closed when the applicable authority is unknown, conflicting or cannot be externally enforced.

The exact authority policy remains a domain-owner decision. This CR requires consistency and enforceability; it does not authorize an agent to dispatch or contact an engineer.

### 3.4 Permitted-action and skill coverage

**Owners:** `aop-toolkit` for the manifest and fixture; `aop-spec` for the Agent Skill contract if necessary; `aop-conformance` for coverage tests.

- Reconcile every action in `permitted_actions` with a declared, versioned skill/tool binding and its contract.
- In particular, resolve `resolve-fault` and `reconcile-inventory`, which are currently permitted without corresponding skill declarations.
- For each executable binding, declare the action identity, skill identity/version, input/output contract, credential class, scope, side-effect classification, authority requirement and evidence obligation as required by the existing Agent Skill contract.
- If an action cannot be bound and governed, remove it from the executable permitted set or retain it as a non-executable proposal. Do not create placeholder skills merely to satisfy a count.
- Ensure credentials are least-privilege and issued only after the external authority check succeeds.

### 3.5 Validation, conformance and replay

**Owners:** `aop-toolkit`, `aop-conformance` and `aop-reference-harness`, each within its existing repository authority.

Add or extend deterministic checks so that the fault-management reference cannot pass its relevant gate when any of the following is true:

- required timestamp, duration, timezone or event-order semantics are missing or violated;
- a case contains an unexplained event outside its declared run boundaries;
- a duration field is inconsistent with its declared derivation;
- the SOP, manifest and effective authority decision conflict;
- an action is permitted but lacks a governed skill/tool binding;
- a prohibited action is exposed as an executable skill;
- a human escalation route is represented as an agent-executable action;
- a fixture violates the declared procedure branch/precedence semantics.

The negative fixtures must prove that each defect class is detected. The corrected corpus, SOP, manifest, compiled AOP, schemas, validator/harness versions and test results must be pinned by commit or content digest in the replay record.

After remediation, run the documented multi-repository reference gate in a controlled workspace and retain its logs and artefact digests. A passing fixture gate demonstrates internal consistency and successful reference execution only; it does not establish production deployment, live service availability or business improvement.

## 4. Acceptance criteria

This CR is complete only when all of the following are evidenced:

1. The case schema or accompanying normative documentation defines timestamp, interval, ordering, timezone and duration semantics without ambiguity.
2. All 40 reference cases pass the agreed corpus validator, or any intentionally exceptional case is explicitly typed, justified and tested.
3. The `cycle_time` field has a defined unit and derivation; no metric is inferred from a field whose semantics remain ambiguous.
4. The SOP and fixture encode explicit, valid procedure branches for resolution and dispatch; observed event chronology and procedural precedence are not conflated.
5. The authority map, decision-rights ladder and SOP agree on dispatch, escalation and rule precedence.
6. A dispatch action cannot execute below its approved minimum authority, including when a lower-threshold rule or default would otherwise suggest autonomy.
7. Human on-call escalation is represented as a harness-enforced human handoff, while prohibited agent actions remain prohibited.
8. Every permitted executable action has a valid, versioned skill/tool binding and least-privilege credential declaration; otherwise it is excluded from the permitted set.
9. Positive and negative tests cover each defect class in Sections 3.1–3.4.
10. The reference AOP compiles and passes the applicable conformance checks, and the end-to-end reference gate completes with reproducible logs and pinned artefact digests.
11. The fault-management example and any published conformance/evaluation references identify the corrected source revisions. Superseded fixture revisions remain traceable.
12. Claims about measured MTTR, p50, first-pass performance or enterprise outcomes remain withheld unless the corrected data and metric definitions independently support them.

## 5. Cascade audit

| Tier / repository | Disposition |
|---|---|
| `aop-governance` | IN SCOPE: this CR and its implementation/closure record |
| `aop-foundations` | NO CHANGE: no change to the definition or conceptual hierarchy of AOP |
| `aop-landscape` | NO CHANGE: no change to external positioning |
| `aop-spec` | CONDITIONAL: update only if the current schema, skill contract or normative clauses cannot express the required semantics; do not duplicate existing clauses |
| `aop-architecture` | NO CHANGE unless implementation reveals a genuine trust-boundary defect; no architecture redesign is presumed |
| `aop-context-graph` | IN SCOPE: clarify case/event semantics and validation contract where owned |
| `aop-toolkit` | IN SCOPE: correct fixture and manifest, add corpus and action-coverage validation, preserve provenance |
| `aop-reference-harness` | IN SCOPE: enforce the effective authority and human-handoff contract; add tests where needed |
| `aop-registry` | CONDITIONAL: publish corrected versions and provenance only after the upstream artefacts pass their gates |
| `aop-conformance` | IN SCOPE: add or extend positive/negative fixtures and checks for the identified defect classes |
| `aop-evaluation` | CONSULTED: ensure duration and outcome measures are not conflated; no performance result is published by this CR |
| `aop-adoption` | NO CHANGE unless the corrected reference process changes adopter guidance |
| `aop-examples` | CONDITIONAL: synchronize the fault-management worked example only after the upstream reference artefacts are corrected |
| Agentic-Operation | CONSUMER: update AO-WE-001 and AO-ATP-002 references after upstream implementation; no authority over AOP-owned source |

The cascade is deliberately conditional where the owning repository's existing contract may already cover the requirement. The implementation must first map each proposed check to current clauses and tests, then add only the missing coverage.

## 6. What this CR is not

- It is not authorization to modify AOP-owned repositories from Agentic-Operation or to bypass the AOP governance process.
- It is not a new AOP concept, dimension, identifier scheme or trust architecture.
- It is not a change to OpenDEA's metamodel, business-process catalogue, system catalogues or metric catalogue. Those remain under OpenDEA governance.
- It is not a decision to admit a new network fault-management Business Process or to bind candidate OpenDEA records.
- It is not a claim that the 40 cases are production observations or a statistically valid baseline.
- It is not a claim that the AOP reference harness is deployed in an enterprise environment.
- It does not prescribe one linear operational sequence where the domain evidence supports legitimate branches.
- It does not permit the agent to perform prohibited human escalation or external-resource dispatch without the required authority.

## 7. Implementation and closure

The AOP programme owner should accept or reject this CR through the programme's ADR/change-control process. Once accepted, each repository owner implements only the changes within that repository's authority and records the resulting PRs, commits, versions and test evidence.

The CR may be marked Implemented only after the acceptance criteria are met and the cross-repository gate is reproducible. Partial implementation must be recorded by repository and must not be represented as closure of the whole CR.

The merged Agentic-Operation artefact [AO-WE-001](https://github.com/Agentic-Operation/.github/blob/main/docs/examples/AO-WE-001-fault-management-opendea-aop-worked-example.md) is the originating evidence and consumer reference. It should be updated after the upstream corrections land, not used as a substitute for them.
