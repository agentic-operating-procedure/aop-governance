# AOP Programme Plan: Concept, Specification, Architecture, Substrate, Tooling, Runtime, Registry, Assurance, Evaluation, Adoption, Governance Levels (Programme Scope)

_Mirrors the board at http://192.168.50.160:7000/board/75 (project 75, `AOPORG`).
Origin: Discord guild `1496909480783249428`, parent channel `1567014161659985992`,
thread `1567023253774671914` (`#agntic-operating-procedure`)._

## 1. Purpose

This plan organises the Agentic Operating Procedure (AOP) programme into an
exhaustive, phased structure that can be executed as a repository estate. It
is the source of truth for what gets built, in what order, and against which
gates.

The programme is derived from two seed documents supplied by the programme
owner on 2026-11-03:

- "From Standard Operating Procedures to Agentic Operating Procedures"
  (the concept framing: what an AOP is, how it relates to skills and
  harnesses, how the discipline of Agentic Operating Engineering emerges).
- "From SOP to AOP: Writing the Operating Standard for Agentic Operations"
  (the engineering framing: why SOP-grounded agents hit an agency ceiling,
  how procedures become network-native, the observe/model/compile/execute
  pipeline, the bounded-execution trust architecture).

Both documents are treated as seed input, not as settled architecture. Where
they disagree or leave gaps, this plan states the resolution in the decisions
log.

### 1.1 The problem this programme exists to solve

An SOP-grounded agent's useful agency is bounded by exactly one thing: the
decision specificity and coverage of the document it reads. Three failure
modes define that ceiling: prose semantics rather than execution semantics,
coverage decay between document revisions, and the happy-path fallacy where
the documented path accounts for only a minority of real cases.

The programme's response is a different class of object. An AOP is an
executable, decision-aware, observed-rather-than-imagined operating standard
that governs an agent's authority, constraints, capabilities, coordination,
controls and evidence obligations.

### 1.2 Non-goals for this programme

- Not an AI framework, not a workflow engine, not an agent SDK.
- Not a prompt library, not a RAG system, not a model-evaluation suite.
- Not a replacement for existing SOP libraries. SOPs are source material and
  lineage, not an execution substrate.

## 2. Conceptual model

The programme holds six levels. Every artefact, repo, and card maps to
exactly one level or spans an explicitly declared contiguous range of them.

| # | Concept | Architectural responsibility |
|---|---|---|
| 1 | Agentic Operating Engineering | The discipline |
| 2 | Agentic Operating Procedure | The operational specification |
| 3 | Agent Skill | The reusable capability |
| 4 | Domain Agent Harness | The controlled execution environment |
| 5 | Agent | The execution actor |
| 6 | Agentic Operations | The broader operating mode |

Two further relationships govern the estate:

- A domain-specific agent harness is the top-level AOP for its domain. It
  sets the operating boundaries within which individual AOPs and skills are
  executed, and it is documented with the same rigour as any other AOP.
- Lower-level AOPs and agent skills run inside that harness under its rules.

### 2.1 The eight AOP dimensions

Every AOP specification must populate all eight. Each maps to a normative
clause in the specification repo.

| Dimension | What the AOP establishes |
|---|---|
| Intent | The operational objective and desired outcome |
| Context | The information and environmental state relevant to execution |
| Constraints | Policies, rules, boundaries and prohibited actions |
| Authority | Decisions an agent may make independently versus those requiring approval |
| Capabilities | The skills, tools and operational capabilities available |
| Coordination | How agents, humans and external systems interact |
| Control | Monitoring, validation, intervention and exception handling |
| Assurance | Evidence required to establish that execution was correct and outcomes achieved |

### 2.2 The procedure governs the agent, not the other way around

The procedure is authoritative. The agent operates within the authority,
constraints and assurance requirements the AOP establishes. The agent cannot
self-authorise: the authority check runs outside the model context.

## 3. Repository estate

Fourteen repositories, grouped into eleven tiers. The full rationale,
ownership, dependency and seed manifest for each repo is in the companion
repository map. The summary here is the authority ladder and the landing
order.

| # | Repository | Tier | Authority | Landing wave |
|---|---|---|---|---|
| 1 | `aop-governance` | Governance | Process: ADRs, change requests, findings, lifecycle | Wave 1 |
| 2 | `aop-foundations` | Concept | Definition, conceptual hierarchy, principles, glossary | Wave 1 |
| 3 | `aop-landscape` | Concept | Positioning against adjacent disciplines and standards | Wave 1 |
| 4 | `aop-spec` | Specification | Normative AOP model, identifiers, versioning, conformance clauses | Wave 2 |
| 5 | `aop-architecture` | Architecture | Layered reference architecture, trust architecture, topologies | Wave 2 |
| 6 | `aop-context-graph` | Substrate | Context Graph of Work, case stitching, drift detection | Wave 3 |
| 7 | `aop-toolkit` | Tooling | SOP parser, AOP linter, decision-rule compiler, SDK | Wave 4 |
| 8 | `aop-reference-harness` | Runtime | Executable harness: runtime loop, guardrail, evidence | Wave 4 |
| 9 | `aop-registry` | Registry | Versioned catalogue of AOPs, skills, provenance, discovery | Wave 4 |
| 10 | `aop-conformance` | Assurance | Conformance profiles for AOP documents and harnesses | Wave 5 |
| 11 | `aop-evaluation` | Evaluation | Baselines, shadow-mode evaluation, agent-versus-human metrics | Wave 5 |
| 12 | `aop-adoption` | Adoption | Migration playbook, maturity model, worked exemplars | Wave 6 |
| 13 | `.github` | Governance | Org profile, templates, community files | Wave 1 |
| 14 | `aop-examples` | Adoption | End-to-end reference exemplars (deferred to Wave 6, see D-010) | Wave 6 |

Rejected repo candidates, and the trigger that would revive each, are listed
in the repository map under "Rejected candidates".

## 4. Phases, gates and breakdown

Each phase has an entry gate, an exit gate, and named task families. A phase
does not close on code volume; it closes on its exit gate.

### Phase 0: Programme foundation

Entry: none. Exit: the estate exists, the concept is ratified, and the
org-level GitHub surface renders.

- P0.1 Create the org-level project space and the local programme workspace.
- P0.2 Ratify the concept hierarchy, the eight dimensions and the terminology
  set through a foundational ADR set.
- P0.3 Stand up the governance repo with the change model: ADR, change
  request, finding, lifecycle, contribution rules.
- P0.4 Publish the org profile and the issue and pull-request templates.
- Gate: every Wave 1 repo is created, public, with a seeded README, a
  licence commit, and CODEOWNERS.

### Phase 1: Concept and governance surface

Entry: Phase 0 exit. Exit: a reader can state what an AOP is, what it is
not, and how the programme decides what changes.

- P1.1 Foundational paper: the concept, its boundaries, its relationship to
  SOP, to skills, to harnesses.
- P1.2 Terminology and glossary with a stable identifier per defined term.
- P1.3 Landscape map: adjacent disciplines, standards landscape, and the
  programme's differentiating claim for each.
- P1.4 Governance process: change classes, lifecycle states, decision
  rights, release policy.
- Gate: concept ADR set ratified, landscape map published, governance
  process accepted with at least one exercise change request.

### Phase 2: Normative specification

Entry: Phase 1 exit. Exit: a conformant AOP document can be written and
machine-validated.

- P2.1 The AOP model: eight dimensions, network-native procedure structure
  (variants, decision points, exception edges, rework loops), the authority
  and constraint model.
- P2.2 Identifier scheme and versioning model, including procedure
  provenance and lineage from source SOP.
- P2.3 Machine-readable schema and reference validator.
- P2.4 The normative agent skill contract (interface, metadata, invocation
  semantics, capability declaration).
- P2.5 Conformance clauses for AOP documents.
- Gate: a specimen AOP validates against the schema; the validator fails
  correctly on a deliberately broken specimen.

### Phase 3: Reference architecture

Entry: Phase 2 exit. Exit: the architecture fixes the interfaces that
Phases 4 and 5 implement against.

- P3.1 Layered reference architecture: AOP, skill, harness, agent, run.
- P3.2 Trust architecture: prevent, verify, oversee, audit, with the
  enforcement point outside the model context.
- P3.3 The observe, model, compile, execute pipeline and the feedback loop
  from execution back into the substrate.
- P3.4 Deployment topologies: single-harness, multi-harness, brownfield.
- Gate: interfaces named for the context graph, the toolkit, the harness,
  the registry and the conformance suite.

### Phase 4: Substrate, tooling and runtime

Entry: Phase 3 exit. Exit: an end-to-end path exists from observed work to
governed execution with evidence.

- P4.1 Context Graph of Work: schema, case stitching, decision and
  exception extraction, drift detection.
- P4.2 SOP intake and translation: parse to intent hypothesis, reconcile
  intent against observation, classify differences.
- P4.3 Compile: variant mining with frequencies, rule extraction with
  thresholds, exception and escalation patterns, governance bounds,
  provenance, versioning.
- P4.4 Runtime loop: snapshot, match, authorise, execute, record, emit.
- P4.5 Guardrail: permitted-action check, authority threshold check,
  exception pattern check, scoped credentials, escalation dispatch.
- P4.6 Evidence: append-only case record with inputs, context snapshot,
  rule, provenance, decision, approver, outcome.
- P4.7 Registry: publish, version, discover, provenance chain.
- P4.8 Toolkit clients: linter, decision-rule compiler, SDK.
- Gate: one procedure compiles end to end and executes under the guardrail
  with a complete case record.

### Phase 5: Assurance and evaluation

Entry: Phase 4 exit. Exit: conformance and value are demonstrable, not
asserted.

- P5.1 Conformance profile for AOP documents: completeness, decision
  specificity, authority coverage, provenance.
- P5.2 Conformance profile for harnesses: fail-closed behaviour, authority
  enforcement outside the context, credential scoping, audit completeness.
- P5.3 Baseline extraction from observed human execution.
- P5.4 Shadow-mode evaluation: agent choices compared with human choices,
  discrepancy review.
- P5.5 Metrics: cycle time, first-pass resolution, exception rate, escalation
  precision, drift detection latency.
- Gate: a harness passes the conformance suite; a shadow-mode run reports
  agreement against the human baseline.

### Phase 6: Adoption

Entry: Phase 5 exit. Exit: an adopter can migrate a procedure unaided.

- P6.1 Six-stage procedural engineering playbook: decomposition, grounding,
  autonomy disposition, specification, harness engineering, verification.
- P6.2 Maturity model from human-operated through agentic to autonomous
  operations.
- P6.3 Adoption scenarios: pilot, brownfield, regulated and high-risk.
- P6.4 Worked exemplars: fault management, customer refund.
- P6.5 Organisational change guidance: roles, decision rights, the shift
  from corridor execution to exception ownership.
- Gate: a pilot procedure is migrated by a team other than the programme
  stewards.

## 5. Dependency graph

```
Phase 0  Programme foundation
   |
   v
Phase 1  Concept and governance surface
   |
   v
Phase 2  Normative specification  ---------+
   |                                     |
   v                                     |
Phase 3  Reference architecture          |
   |                                     |
   v                                     |
Phase 4  Substrate, tooling, runtime     |
   |                                     |
   v                                     |
Phase 5  Assurance and evaluation <------+
   |
   v
Phase 6  Adoption
```

Two cross-phase constraints hold regardless of the phase order:

- The specification is the contract. No repo in Phases 3 to 6 may define an
  interface the specification has not already fixed. An interface that the
  specification does not carry is a change request against the specification,
  not a local decision.
- Assurance is not deferred to the end. The evidence model is fixed in
  Phase 4 because the runtime cannot be built without it.

## 6. Decisions log

Full rationale for each entry is in `decisions/`. Decisions are numbered and
immutable once ratified; superseding a ratified decision creates a new entry.

| ID | Decision | Status |
|---|---|---|
| D-001 | The estate is a polyrepo of fourteen repositories across eleven tiers, not a monorepo | Ratified |
| D-002 | Repository naming uses the `aop-` prefix, the `aop` abbreviation for the org short form | Ratified |
| D-003 | The normative agent skill contract lives in the specification repo as a normative annex | Ratified |
| D-004 | The security and trust model is normative text in the specification repo, with the threat model in the architecture repo | Ratified |
| D-005 | The compile-and-run pipeline is a single closed loop; execution feeds the substrate | Ratified |
| D-006 | Authority is modelled as a decision-rights ladder over five risk axes | Ratified |
| D-007 | Standards sourcing cites ITU-T M.3050.x, ETSI TS, ISO/IEC and NIST only | Ratified |
| D-008 | Per-repository agent doctrine files are local-only and excluded from published content | Ratified |
| D-009 | Programme plan files live in the governance repository under `plans/` | Ratified |
| D-010 | Exemplars are a dedicated repository, deferred to Wave 6 | Provisional |

## 7. Governance of this programme

- Decision authority for structural change rests with the programme owner.
  Agents surface options with consequences; they do not decide.
- Every change to the estate is recorded as a change request against the
  governance repository, including repository creation, retirement, renaming
  and tier reassignment.
- The board at http://192.168.50.160:7000/board/75 is the audit trail for
  work items on this channel. Every action, decision, recon, test and
  artefact produced on this channel raises a card.
- The org-level GitHub Project is the public cross-repo view. The board is
  the internal working record. The two are reconciled on every phase gate.

## 8. Machine-readable summary

```yaml
programme: agentic-operating-procedure
org: agentic-operating-procedure
programme_scope: >-
  Define, expand and expound Agentic Operating Procedure as an authoritative
  engineering discipline, with a full estate of specifications, tooling,
  runtime, assurance and adoption surfaces.
board:
  url: http://192.168.50.160:7000/board/75
  project_id: 75
  identifier: AOPORG
  columns: { backlog: 301, in_progress: 302, review: 303, done: 304 }
discord:
  guild_id: "1496909480783249428"
  parent_channel_id: "1567014161659985992"
  thread_id: "1567023253774671914"
  channel: agntic-operating-procedure
repositories:
  - { name: aop-governance,        tier: governance,  wave: 1 }
  - { name: aop-foundations,       tier: concept,     wave: 1 }
  - { name: aop-landscape,         tier: concept,     wave: 1 }
  - { name: aop-spec,              tier: specification, wave: 2 }
  - { name: aop-architecture,      tier: architecture, wave: 2 }
  - { name: aop-context-graph,    tier: substrate,   wave: 3 }
  - { name: aop-toolkit,           tier: tooling,    wave: 4 }
  - { name: aop-reference-harness, tier: runtime,     wave: 4 }
  - { name: aop-registry,          tier: registry,   wave: 4 }
  - { name: aop-conformance,       tier: assurance,  wave: 5 }
  - { name: aop-evaluation,        tier: evaluation, wave: 5 }
  - { name: aop-adoption,          tier: adoption,   wave: 6 }
  - { name: aop-examples,          tier: adoption,   wave: 6 }
  - { name: .github,               tier: governance,  wave: 1 }
phases:
  - { id: 0, name: Programme foundation,           gate: estate_exists_and_readable }
  - { id: 1, name: Concept and governance surface, gate: concept_ratified }
  - { id: 2, name: Normative specification,        gate: specimen_validates }
  - { id: 3, name: Reference architecture,         gate: interfaces_fixed }
  - { id: 4, name: Substrate tooling and runtime,  gate: end_to_end_executes }
  - { id: 5, name: Assurance and evaluation,       gate: conformance_and_baseline_measured }
  - { id: 6, name: Adoption,                       gate: pilot_migrated_unaided }
open_decisions: [ D-010 ]
```
