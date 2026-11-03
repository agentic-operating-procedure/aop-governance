# AOP Repository Map: Governance, Concept, Specification, Architecture, Substrate, Tooling, Runtime, Registry, Assurance, Evaluation, Adoption Levels (Org Scope)

_Published as the programme's authoritative plan. Work items are tracked on the programme board and mirrored in the organisation roadmap project.

## 1. Design rules applied

Five rules decided the shape of the estate before any repository was named.

**R1: One authority per concern.** A repository is the single authority for
exactly one class of artefact. Where two concerns would need to change
together at the same rate, they are one repository. Where they would change
at different rates, they are two. This is the only reason the estate is
split at all.

**R2: Authority flows downward, dependency flows upward.** A consumer of a
lower repository does not depend on the consumer of a higher one. The
specification does not know who implements it. The reference harness does
not know who evaluates it. This keeps every repository independently
testable.

**R3: A repository earns its place by having an independent failure mode.**
If two candidates fail together, they belong together. A specification and
its validator fail together only if the validator is generated from the
specification, which it is not: the validator is written independently and
fails when the specification is wrong. A concept paper and a concept
glossary fail together, so they are one repository.

**R4: Naming is `<org-short>-<role>`.** The sibling discipline
organisations in this estate use `<org-short>-<role>` exactly
(`enterprise-semantics-spec`, `enterprise-semantics-governance`,
`dea-governance`, `dea-metamodel`). The `aop-` prefix is the same
convention applied to the `agentic-operating-procedure` short form. The
`.github` repository is the only exception, because GitHub fixes that name.

**R5: Every repository is public and every repository has a README that
states its authority in one sentence.** An authority claim that is not
stated is not a claim.

## 2. The estate

Fourteen repositories. The tier is the repository's position in the
authority ladder: lower tiers are depended upon by higher tiers.

### Wave 1: Governance and concept

These four repositories exist before any engineering, because they fix what
is being built and who decides.

#### `aop-governance` (tier: governance)

The process repository. Owns architectural decision records, change
requests, findings, the lifecycle model, the release policy, the contributor
rules, and the programme plan itself under `plans/`.

It is the repository where the owner of the concept holds decision rights.
Nothing else in the estate is permitted to change the meaning of a term, the
shape of the model, or the boundaries of the programme. Those changes arrive
here as a change request and leave here as a decision.

Owns: ADRs, CRs, findings, the plan, the decisions log, programme-wide
vocabulary governance.
Does not own: the definitions themselves (those live in `aop-foundations`
and `aop-spec`; governance governs their change, not their content).

The plan files live here under `plans/`, which is where the local programme
workspace at a local authoring workspace is eventually published.

#### `aop-foundations` (tier: concept)

The concept repository. Owns the definition of an Agentic Operating
Procedure, the distinction from a Standard Operating Procedure, the
conceptual hierarchy, the discipline of Agentic Operating Engineering, the
glossary, and the explicit non-goals.

Owns: the founding paper, the conceptual hierarchy, the glossary, the
misconception ladder, the six-level conceptual hierarchy that the whole estate is
indexed by.
Does not own: the machine-readable model (that is `aop-spec`).

The hierarchy this repository fixes:

| # | Concept | Architectural responsibility |
|---|---|---|
| 1 | Agentic Operating Engineering | The discipline |
| 2 | Agentic Operating Procedure | The operational specification |
| 3 | Agent Skill | The reusable capability |
| 4 | Domain Agent Harness | The controlled execution environment |
| 5 | Agent | The execution actor |
| 6 | Agentic Operations | The broader operating mode |

#### `aop-landscape` (tier: concept)

The positioning repository. Owns the comparison of AOP against adjacent
disciplines and against what already exists: workflow engines, business
process management, orchestration frameworks, policy engines, runbook and
playbook tooling, and the operational management literature. It also owns
the standards landscape survey.

This repository exists because the single hardest obstacle to the concept
becoming authoritative is not building it. It is establishing, in public and
with citations, that it is not a relabelling of something that already
exists. A discipline that cannot state its difference credibly cannot hold
authority.

Owns: comparative position papers, the prior-art survey, the standards
landscape, the claim-by-claim differentiation table.
Does not own: the concept itself.

#### `.github` (tier: governance)

The organisation profile and shared community files. Owns `profile/README.md`,
which is the public front door and must state the concept in one paragraph
and link the authority ladder. Also owns issue and pull-request templates,
the code of conduct, and the contribution guide.

Per GitHub platform rules this repository must be public or the profile
README does not render.

### Wave 2: Specification and architecture

#### `aop-spec` (tier: specification)

The normative specification. This is the authority the entire estate is
built against, and the single most important repository in the programme.

Owns: the eight-dimension AOP model (Intent, Context, Constraints,
Authority, Capabilities, Coordination, Control, Assurance), the network-native
procedure structure (variants, decision points, exception edges, rework
loops), the identifier scheme, the versioning and provenance model, the
machine-readable schema, the normative annex for the Agent Skill contract,
and the conformance clauses an AOP document must satisfy.

It also owns the normative security clauses: the rule that the authority
check runs outside the model context, and the rule that the harness is the
top-level AOP for its domain.

Owns: the schema, the identifier registry, the conformance clauses, the
normative annexes.
Does not own: implementations of the schema, or the prose rationale for the
model (that is `aop-foundations`).

#### `aop-architecture` (tier: architecture)

The reference architecture. Owns the layered view of the system (AOP, skill,
harness, agent, run), the trust architecture, the compile-and-run pipeline,
and the deployment topologies.

Trust architecture is the four-mechanism model the runtime is built against:
**prevent** (the agent cannot exceed its authority because the check is
outside its context), **verify** (independent checking of a completed
action), **oversee** (human escalation with a threshold and a bundle), and
**audit** (an append-only case record). It also owns the threat model:
a malicious or confused AOP, a compromised agent, a credential leak, and a
prompt-injection path into the procedure.

Owns: layer diagrams, trust boundaries, pipeline topology, deployment
topologies, the threat model.
Does not own: the normative text that binds implementations (that is
`aop-spec`).

### Wave 3: Substrate

#### `aop-context-graph` (tier: substrate)

The substrate repository. Owns the Context Graph of Work: the entity model
(CASE, TASK, STEP, ACTOR, APPLICATION, DECISION, RULE, EXCEPTION,
ESCALATION, OUTCOME), the graph schema, case stitching, the digital twin of
operations, and drift detection.

This is the repository that answers the hardest question in the whole
programme: how does the system know what actually happens, as opposed to
what a document claims happens? Everything above it in the ladder is
downstream of this observation capability. Without it there is no variant
mining, no reconciliation of intent against reality, and therefore no way to
know that a procedure has drifted.

Owns: the graph entity model, the stitcher, the twin, the drift detector,
the case schema.
Does not own: the compiler that consumes the graph (that is `aop-toolkit`).

### Wave 4: Tooling, runtime, registry

#### `aop-toolkit` (tier: tooling)

The tooling repository. Owns the SOP parser, the AOP linter, the variant
miner, the decision-rule extractor, the decision-rule compiler, the AOP
generator, the version-control integration, and the client SDK.

This is where the observe, model, compile, execute pipeline becomes
executable. The variant miner produces a variant inventory with observed
frequencies. The rule extractor produces decision rules with their
thresholds. The compiler turns those into an executable AOP with
provenance and version.

Owns: the parsers, the miners, the extractors, the compiler, the linter,
the SDK.
Does not own: the schema being compiled to (that is `aop-spec`) or the
graph being mined (that is `aop-context-graph`).

#### `aop-reference-harness` (tier: runtime)

The reference runtime repository. Owns a working domain agent harness: the
runtime loop (context snapshot, variant match, authority check, action,
record, emit), the guardrail implementation, scoped credential issuance,
the escalation dispatch, the approver evidence bundle, and the append-only
case record.

A harness is itself the top-level AOP for its domain, so this repository
contains an AOP as well as code that runs one. The harness boundary defines
what the agent may and may not do; the AOPs running inside it define the
work.

Owns: the runtime, the guardrail, the credential broker, the escalation
dispatch, the evidence bundle, the case record writer.
Does not own: the model of what it runs (that is `aop-spec`) or the
evaluation of how well it runs (that is `aop-evaluation`).

#### `aop-registry` (tier: registry)

The catalogue repository. Owns the versioned catalogue of AOPs, skills and
harnesses: publication, versioning, discovery, dependency resolution
between AOPs, and the provenance chain from a published AOP back to the
observed cases it was compiled from.

A registry is what turns a collection of documents into a body of practice
that other people can adopt without re-deriving it. It is also what makes
the programme's claims falsifiable: anyone can pull a published AOP and
check its provenance.

Owns: the catalogue, the publication workflow, the provenance chain, the
discovery API.
Does not own: the content of the AOPs it catalogues (that is `aop-spec`
and the domain repositories).

### Wave 5: Assurance and evaluation

#### `aop-conformance` (tier: assurance)

The assurance repository. Owns two conformance profiles: one for AOP
documents (completeness across the eight dimensions, decision specificity,
authority coverage, provenance) and one for harnesses (fail-closed
behaviour, authority enforcement outside the model context, credential
scoping, audit completeness).

It also owns the test fixtures, including deliberately broken AOP documents
that must fail, and the certification process that turns a conformance
result into a published claim.

Owns: the profiles, the suite, the fixtures, the certification process.
Does not own: the model being tested against.

#### `aop-evaluation` (tier: evaluation)

The evaluation repository. Owns baseline extraction from observed human
execution, shadow-mode evaluation comparing agent choices against human
choices, the metric definitions (cycle time, first-pass resolution, exception
rate, escalation precision, drift detection latency), and the reproducibility
protocol.

This repository carries the programme's burden of proof. The claim that AOP
delivers value is a testable claim, and this is where it is tested. Without
it, the concept is an argument rather than a result.

Owns: baselines, the shadow-mode harness, the metric definitions, the
reproducibility protocol, the published results.
Does not own: the harness being evaluated, or the metrics that are properties
of a specific domain rather than of the method.

### Wave 6: Adoption

#### `aop-adoption` (tier: adoption)

The adoption repository. Owns the six-stage procedural engineering playbook
(decomposition, operational grounding, autonomy disposition, AOP
specification, harness engineering, verification and assurance), the
migration path from SOP to AOP, the maturity model from human-operated
through assisted to agentic to autonomous operations, the three adoption
scenarios (pilot, brownfield, regulated and high-risk), and the
organisational change guidance for the shift from corridor execution to
exception ownership.

This repository exists for the adopter, not for the programme. It is written
for a team that has an SOP and a desire to operate it with an agent, and it
must be usable without the programme stewards in the room.

Owns: the playbook, the maturity model, the scenarios, the change guidance,
the adopter-facing checklists.
Does not own: the tooling that implements the steps (that is `aop-toolkit`).

#### `aop-examples` (tier: adoption, deferred to Wave 6)

The exemplar repository. Owns complete worked examples: a fault management
procedure taken end to end from SOP through compilation to executed and
audited agent action, and a customer refund procedure likewise.

The decision to defer this repository is recorded as D-010. An exemplar is
worth nothing until the parts it demonstrates exist, so it lands last. It is
listed in the estate because the programme is incomplete without it: an
authoritative concept needs at least one complete, reproducible demonstration.

Owns: the worked examples, the reproduction scripts, the narrated walkthroughs.
Does not own: any reusable component, which belongs upstream.

## 3. Rejected candidates

Naming what was considered and refused is part of the map. Each entry states
the trigger that would revive it.

| Candidate | Rejected because | Revival trigger |
|---|---|---|
| `aop-ops` | The runtime is reference-quality but domain-specific. A separate operations repository implies a production estate the programme does not yet have. | A named production domain adopts an AOP and needs a deployed, monitored harness. |
| `aop-security` | The trust model is architectural, not a separate discipline. A dedicated repository fragments the guardrail, which must be read against the runtime that enforces it. | A separate security review board takes ownership, or the threat model outgrows one chapter. |
| `aop-docs` | A documentation repository without an authority behind it becomes a second, drifting source of truth. | The estate exceeds roughly fifteen repositories and a reader-facing site earns its own build pipeline. |
| `aop-ontology` | An ontology for AOP concepts would duplicate the entity model already owned by `aop-spec` and the graph model owned by `aop-context-graph`. | A formal OWL or RDF publication becomes a separate interoperability commitment. |
| `aop-benchmark` | Benchmarks are results, not engines. Splitting them from the evaluation method separates the claim from the method that produced it. | Benchmarks are published independently under a separate licence or steward. |
| `aop-cli` | The CLI is a client of the toolkit and the registry. Separating it forks the release cadence for no isolation benefit. | The CLI acquires consumers outside the AOP programme and needs independent versioning. |
| `aop-marketplace` | A marketplace implies a commercial exchange between independent vendors. That is a different organisation and a different governance problem. | Third-party AOP vendors appear and require a neutral listing body. |
| `aop-agent` | An agent implementation is the least authoritative and most replaceable part of the estate. It would attract the most attention and hold the least authority. | A reference agent is needed for conformance testing against the harness profile. |
| `aop-workshop` | Facilitation material is adoption content. | Pilot delivery reveals a distinct facilitation practice that adoption does not cover. |
| `aop-certification` | Certification is a process over conformance results, not a separate artefact class. | A certification body independent of the programme is constituted. |

## 4. The cascade

Structural change to the estate is not a single edit. The authority ladder
means a change at one level forces changes at every level below it that
consumes it.

```
aop-governance      (decision)
      |
      v
aop-foundations     (concept: does the change alter what AOP is?)
      |
      v
aop-spec            (model: does the change alter the eight dimensions,
      |              the identifier scheme, or the conformance clauses?)
      v
aop-architecture    (architecture: does the change alter a layer, a trust
      |              boundary, or the pipeline?)
      v
aop-context-graph   (substrate: does the change alter the entity model,
      |              the stitcher, or the drift detector?)
      v
aop-toolkit         (tooling: does the change alter the miners, the
      |              extractors, the compiler, or the linter?)
      v
aop-reference-harness (runtime: does the change alter the loop, the
      |              guardrail, the credential broker, or the evidence?)
      v
aop-registry        (catalogue: does the change alter publication,
      |              versioning, or provenance?)
      v
aop-conformance     (assurance: does the change alter a profile or a
      |              fixture?)
      v
aop-evaluation      (evidence: does the change alter a metric or invalidate
      |              a published result?)
      v
aop-adoption        (adoption: does the change alter a playbook step or a
      |              maturity stage?)
      v
aop-examples        (demonstration: does the change invalidate a walkthrough?)
```

`aop-landscape` sits beside `aop-foundations` and is affected only when the
change alters the programme's external positioning. `.github` is affected
only when the ladder or the repository set itself changes.

The exhaustive item-level checklist for this cascade is the companion
artefact `plans/aop-org-cascade-checklist-org-scope.md`. Every structural change is
audited against it at the cross-check stage before the change lands.

## 5. Relationship to sibling organisations

This programme is not self-contained and does not pretend to be.

- **Semantic interoperability.** The entity vocabulary of AOPs and the
  relationships between them map onto the semantic standards defined by the
  `Enterprise-Semantics` and `OpenDEA` organisations. The mapping direction
  is AOP to those standards, never a copy of them into this estate. Those
  organisations remain the authority for enterprise semantics; this
  programme consumes them.
- **Governance precedent.** The change model in `aop-governance` follows the
  established ADR, change-request and finding pattern used by the sibling
  discipline organisations rather than inventing a new one.
- **Execution discipline.** The repository, review and release conventions
  are the ones already in force across this estate: one logical change per
  branch, review before merge, an auditable history.

## 6. Authority ladder summary

| Order | Repository | What it is authoritative for |
|---|---|---|
| 1 | `aop-foundations` | What an AOP is, and what it is not |
| 2 | `aop-spec` | The formal model, identifiers, versioning, conformance clauses |
| 3 | `aop-architecture` | Layering, trust boundaries, the compile-and-run pipeline |
| 4 | `aop-context-graph` | The entity model of observed work, case stitching, drift |
| 5 | `aop-toolkit` | Mining, extraction, compilation, linting |
| 6 | `aop-reference-harness` | A working harness, guardrail, and evidence record |
| 7 | `aop-registry` | Publication, versioning, provenance, discovery |
| 8 | `aop-conformance` | Whether a document or a harness conforms |
| 9 | `aop-evaluation` | Whether the method produces a measured result |
| 10 | `aop-adoption` | How an organisation moves from SOP to AOP |
| 11 | `aop-examples` | A complete, reproducible demonstration |
| 12 | `aop-landscape` | How the concept differs from what already exists |
| 13 | `aop-governance` | How the programme changes |
| 14 | `.github` | The public front door and contribution mechanics |
