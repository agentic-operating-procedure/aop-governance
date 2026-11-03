# AOP Org Cascade Checklist: Governance, Concept, Specification, Architecture, Substrate, Tooling, Runtime, Registry, Assurance, Evaluation, Adoption Levels (Org Scope)

_Published as the programme's authoritative plan. Work items are tracked on the programme board and mirrored in the organisation roadmap project.

## How to use this checklist

1. A structural change is proposed as a change request in `aop-governance`.
2. The change is traced through this checklist top to bottom. Every line
   marked `IN SCOPE` is audited explicitly, even when the answer is no
   change is needed.
3. The cross-check stage re-reads the change request against this checklist
   and confirms every `IN SCOPE` line was addressed.
4. A change that skips an `IN SCOPE` line does not land.

Legend: `IN SCOPE` means the line must be audited for this change.
`N/A` means the line was considered and requires no action, with the reason
recorded in the change request.

## A. Governance and concept

| # | Check | Scope | Audit question |
|---|---|---|---|
| A1 | `aop-governance`: a change request exists, numbered, with a status | IN SCOPE | Is the change recorded before any artefact moves? |
| A2 | `aop-governance`: the decisions log entry is updated | IN SCOPE | Does the log reflect the decision and its rationale? |
| A3 | `aop-governance`: the programme plan phase and gate mapping is updated | IN SCOPE | Does the change alter a phase gate or a dependency? |
| A4 | `aop-governance`: the cascade section of the repository map is still accurate | IN SCOPE | Does this change alter the ladder itself? |
| A5 | `aop-foundations`: the conceptual hierarchy is unchanged, or a foundational ADR records the change | IN SCOPE | Does the change alter what an AOP is, or the relationship between AOP, skill, harness and agent? |
| A6 | `aop-foundations`: the glossary is unchanged, or the new term is added with a stable identifier | IN SCOPE | Does the change introduce a term that must resolve against existing vocabulary? |
| A7 | `aop-foundations`: the non-goals list is unchanged, or the change explicitly reopens one | IN SCOPE | Does the change pull the programme toward being a framework, a workflow engine, or a model-evaluation suite? |
| A8 | `aop-landscape`: the differentiation table is unchanged, or updated with a citation | IN SCOPE | Does the change alter the claim about what AOP is not? |
| A9 | `.github`: the profile README statement of the concept is unchanged, or updated | IN SCOPE | Does the change alter the public one-paragraph description? |
| A10 | `.github`: the repository list in the profile is current | IN SCOPE | Does the change create, rename or retire a repository? |

## B. Specification

| # | Check | Scope | Audit question |
|---|---|---|---|
| B1 | `aop-spec`: the eight-dimension model is unchanged, or the change is normative text | IN SCOPE | Does the change alter Intent, Context, Constraints, Authority, Capabilities, Coordination, Control or Assurance? |
| B2 | `aop-spec`: the identifier scheme is unchanged, or new identifier forms are registered | IN SCOPE | Does the change introduce a new kind of artefact needing an identifier? |
| B3 | `aop-spec`: the versioning and provenance model is unchanged, or updated | IN SCOPE | Does the change alter what version history means for an AOP? |
| B4 | `aop-spec`: the machine-readable schema is regenerated and the reference validator still passes | IN SCOPE | Does the schema change? If so, is the validator updated and re-run? |
| B5 | `aop-spec`: the conformance clauses are unchanged, or the affected clause is revised | IN SCOPE | Does the change alter what a conforming AOP must satisfy? |
| B6 | `aop-spec`: the Agent Skill contract annex is unchanged, or updated | IN SCOPE | Does the change alter what a skill must declare to be composable? |
| B7 | `aop-spec`: the normative security clauses are unchanged, or updated | IN SCOPE | Does the change alter the rule that authority is checked outside the model context? |
| B8 | `aop-spec`: the rule that the harness is the top-level AOP for its domain is unchanged, or updated | IN SCOPE | Does the change alter the harness-procedure relationship? |

## C. Architecture

| # | Check | Scope | Audit question |
|---|---|---|---|
| C1 | `aop-architecture`: layer definitions are unchanged, or updated | IN SCOPE | Does the change move a responsibility between AOP, skill, harness, agent and run? |
| C2 | `aop-architecture`: trust boundaries are unchanged, or updated | IN SCOPE | Does the change move the boundary between what the agent controls and what it does not? |
| C3 | `aop-architecture`: the four assurance mechanisms (prevent, verify, oversee, audit) are unchanged, or updated | IN SCOPE | Does the change add or remove an assurance mechanism? |
| C4 | `aop-architecture`: the observe, model, compile, execute pipeline is unchanged, or updated | IN SCOPE | Does the change add, remove or reorder a pipeline stage? |
| C5 | `aop-architecture`: the feedback path from execution back into the substrate is unchanged, or updated | IN SCOPE | Does the change break the loop that turns execution into evidence? |
| C6 | `aop-architecture`: deployment topologies are unchanged, or updated | IN SCOPE | Does the change alter the single-harness, multi-harness or brownfield topology? |
| C7 | `aop-architecture`: the threat model is updated for the change | IN SCOPE | Does the change introduce a new attack surface, such as a new external input to the procedure? |

## D. Substrate

| # | Check | Scope | Audit question |
|---|---|---|---|
| D1 | `aop-context-graph`: the entity model is unchanged, or updated | IN SCOPE | Does the change add or alter an entity type (CASE, TASK, STEP, ACTOR, APPLICATION, DECISION, RULE, EXCEPTION, ESCALATION, OUTCOME)? |
| D2 | `aop-context-graph`: the graph schema is regenerated and validates | IN SCOPE | Does the schema change? |
| D3 | `aop-context-graph`: case stitching behaviour is unchanged, or updated | IN SCOPE | Does the change alter how fragmented events are reassembled into cases? |
| D4 | `aop-context-graph`: drift detection behaviour is unchanged, or updated | IN SCOPE | Does the change alter what counts as drift and how fast it is detected? |
| D5 | `aop-context-graph`: the privacy posture of observation is unchanged, or updated | IN SCOPE | Does the change increase the personal data captured from work activity? |

## E. Tooling

| # | Check | Scope | Audit question |
|---|---|---|---|
| E1 | `aop-toolkit`: the SOP parser is unchanged, or updated with its fixture set re-run | IN SCOPE | Does the change alter how an SOP is read into an intent hypothesis? |
| E2 | `aop-toolkit`: variant mining is unchanged, or updated | IN SCOPE | Does the change alter how variants are identified or their frequencies counted? |
| E3 | `aop-toolkit`: decision-rule extraction is unchanged, or updated | IN SCOPE | Does the change alter how rules and their thresholds are derived? |
| E4 | `aop-toolkit`: the compiler is unchanged, or updated, with output validated against the schema | IN SCOPE | Does the change alter what a compiled AOP contains? |
| E5 | `aop-toolkit`: the linter is unchanged, or updated, with the broken-specimen set still failing | IN SCOPE | Does the change alter what counts as a lint failure? |
| E6 | `aop-toolkit`: the SDK is unchanged, or updated with a version bump | IN SCOPE | Does the change alter the client-facing surface? |

## F. Runtime

| # | Check | Scope | Audit question |
|---|---|---|---|
| F1 | `aop-reference-harness`: the runtime loop steps are unchanged, or updated | IN SCOPE | Does the change alter the sequence of snapshot, match, authorise, act, record, emit? |
| F2 | `aop-reference-harness`: the guardrail runs outside the model context | IN SCOPE | Is the authority check still performed by a component the agent cannot influence? |
| F3 | `aop-reference-harness`: the harness fails closed on an unmatched variant | IN SCOPE | Does the change allow an action on a variant that is not in the AOP? |
| F4 | `aop-reference-harness`: credential scoping is unchanged, or updated | IN SCOPE | Does the change widen the credential scope available to an action? |
| F5 | `aop-reference-harness`: the escalation threshold and dispatch are unchanged, or updated | IN SCOPE | Does the change alter when a human is asked to decide? |
| F6 | `aop-reference-harness`: the approver evidence bundle is unchanged, or updated | IN SCOPE | Does the change alter what an approver sees before deciding? |
| F7 | `aop-reference-harness`: the case record is complete and append-only | IN SCOPE | Does the change lose any of inputs, context, rule, provenance, decision, approver or outcome? |
| F8 | `aop-reference-harness`: the harness contains its own top-level AOP, and it is current | IN SCOPE | Does the harness boundary still match the AOP that describes it? |

## G. Registry

| # | Check | Scope | Audit question |
|---|---|---|---|
| G1 | `aop-registry`: publication and versioning rules are unchanged, or updated | IN SCOPE | Does the change alter how an AOP is published or versioned? |
| G2 | `aop-registry`: the provenance chain still reaches the observed cases | IN SCOPE | Can a published AOP still be traced to the cases it was compiled from? |
| G3 | `aop-registry`: dependency resolution between AOPs is unchanged, or updated | IN SCOPE | Does the change introduce a dependency between AOPs? |
| G4 | `aop-registry`: the catalogue reflects every current repository and artefact | IN SCOPE | Is the catalogue consistent with the estate after the change? |

## H. Assurance

| # | Check | Scope | Audit question |
|---|---|---|---|
| H1 | `aop-conformance`: the AOP document profile is unchanged, or updated | IN SCOPE | Does the change alter what a conforming document must contain? |
| H2 | `aop-conformance`: the harness profile is unchanged, or updated | IN SCOPE | Does the change alter what a conforming harness must do? |
| H3 | `aop-conformance`: the broken fixtures still fail | IN SCOPE | Does the change make a deliberately invalid document pass? |
| H4 | `aop-conformance`: the certification process is unchanged, or updated | IN SCOPE | Does the change alter what a published conformance claim means? |

## I. Evaluation

| # | Check | Scope | Audit question |
|---|---|---|---|
| I1 | `aop-evaluation`: the metric definitions are unchanged, or updated | IN SCOPE | Does the change alter what cycle time, first-pass resolution, exception rate, escalation precision or drift latency mean? |
| I2 | `aop-evaluation`: published results are re-run or explicitly marked stale | IN SCOPE | Does the change invalidate a published result? |
| I3 | `aop-evaluation`: the reproducibility protocol is unchanged, or updated | IN SCOPE | Does the change alter what a third party must be able to reproduce? |
| I4 | `aop-evaluation`: the shadow-mode comparison is unchanged, or updated | IN SCOPE | Does the change alter how agent choices are compared with human choices? |

## J. Adoption

| # | Check | Scope | Audit question |
|---|---|---|---|
| J1 | `aop-adoption`: the six-stage playbook is unchanged, or updated | IN SCOPE | Does the change alter a stage of procedural engineering? |
| J2 | `aop-adoption`: the maturity model is unchanged, or updated | IN SCOPE | Does the change alter what an agentic stage requires? |
| J3 | `aop-adoption`: the adoption scenarios are unchanged, or updated | IN SCOPE | Does the change alter the pilot, brownfield or regulated paths? |
| J4 | `aop-adoption`: the organisational change guidance is unchanged, or updated | IN SCOPE | Does the change alter the shift from corridor execution to exception ownership? |

## K. Demonstration

| # | Check | Scope | Audit question |
|---|---|---|---|
| K1 | `aop-examples`: the walkthroughs are re-run and still reproduce | IN SCOPE | Does the change invalidate a published demonstration? |
| K2 | `aop-examples`: the reproduction scripts are unchanged, or updated | IN SCOPE | Does the change break a reproduction path? |

## L. Cross-cutting gates

These apply to every structural change regardless of which repositories are
touched.

| # | Gate | Scope | Audit question |
|---|---|---|---|
| L1 | Documentation language rules | IN SCOPE | Does every published artefact avoid em dashes, ellipsis glyphs and prohibited vendor references? |
| L2 | Licence and attribution | IN SCOPE | Is the licence correct and is any quoted third-party material attributed? |
| L3 | Credential hygiene | IN SCOPE | Does any artefact contain a token, key, password or internal address that should not be published? |
| L4 | Link integrity | IN SCOPE | Do all new internal links resolve to existing artefacts? |
| L5 | Naming consistency | IN SCOPE | Do new repository and artefact names follow the established convention exactly? |
| L6 | Reversibility | IN SCOPE | Can this change be rolled back without data loss, and is that path recorded? |
| L7 | Board reconciliation | IN SCOPE | Does the programme board reflect the change, with a card per action, decision and artefact? |
| L8 | Project reconciliation | IN SCOPE | Does the organisation project reflect the change in stage and status? |

## M. Cross-check stage

The cross-check stage is not a checklist line. It is the procedure that runs
the checklist.

1. **Trace.** Read the change request. For each of A1 to L8, record `IN SCOPE`
   with an outcome, or `N/A` with a reason. No line may be left blank.
2. **Verify.** For every line marked as changed, confirm the change is
   present in the working tree and not merely asserted in the change
   request. A line that claims a change that does not exist in the artefact
   fails the cross-check.
3. **Re-run.** For every line that names a validation, the validation is
   re-run in this session and its real output recorded. A validator that was
   run earlier in the session and has since been affected by the change is
   re-run.
4. **Cross-artifact consistency.** The repository map, the programme plan,
   the cascade checklist and the board must all describe the same estate. A
   change that lands in one and not the others fails.
5. **Publish.** Only then does the change land, and the board card moves to
   Review with the cross-check output attached.
