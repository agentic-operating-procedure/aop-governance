# AOP Concept Model: Agentic Operating Engineering, Agentic Operating Procedure, Agent Skill, Domain Agent Harness, Agent, Agentic Operations Levels (Concept Scope)

_Mirrors the board at http://192.168.50.160:7000/board/75 (project 75, `AOPORG`).
The conceptual spine of the programme. Every repository, artefact and board
card in the estate resolves to exactly one level or to an explicitly declared
contiguous range of levels in this ladder._

## 1. The hierarchy

Six levels. Each level names a concept and states the architectural
responsibility that concept carries. The ladder is descending in scope and
ascending in specificity.

| # | Concept | Architectural responsibility |
|---|---|---|
| 1 | Agentic Operating Engineering | The discipline |
| 2 | Agentic Operating Procedure | The operational specification |
| 3 | Agent Skill | The reusable capability |
| 4 | Domain Agent Harness | The controlled execution environment |
| 5 | Agent | The execution actor |
| 6 | Agentic Operations | The broader operating mode |

Read top to bottom as a discipline: the concept governs how the discipline
is practised, the procedure specifies the operating intent, the skill
packages the reusable capability, the harness controls the execution
environment, the agent acts, and the operating mode is the regime those
actions produce.

Read bottom to top as a containment: the operating mode contains agents,
agents run inside a harness, a harness is governed by an AOP, an AOP
invokes skills, and the whole apparatus is an expression of the discipline.

## 2. The governing principle

**The procedure governs the agent, not the other way around.**

The agent operates within the authority, the constraints and the assurance
requirements that the AOP establishes. It cannot self-authorise. The
authority check is performed by a component outside the model context, so
the agent cannot influence the outcome of the check that governs it.

This is the single technical commitment on which the rest of the programme
rests. Every other design decision is downstream of it.

## 3. The five artefacts and what distinguishes them

### 3.1 Agentic Operating Procedure

The operational specification. An AOP is a versioned, machine-readable
operating standard that states:

- **Intent**: the operational objective and the desired outcome.
- **Context**: the information and environmental state relevant to execution.
- **Constraints**: policies, rules, boundaries and prohibited actions.
- **Authority**: which decisions the agent may take alone, and which
  require approval.
- **Capabilities**: the skills, tools and operational capabilities available.
- **Coordination**: how agents, humans and external systems interact.
- **Control**: monitoring, validation, intervention and exception handling.
- **Assurance**: the evidence required to establish that execution was
  correct and that outcomes were achieved.

All eight are mandatory. A document that omits any of them is not a
degraded AOP, it is not an AOP.

An AOP is also network-native in structure. It is not a linear document.
It contains variants (the observed paths through the work), decision points
(where a choice is made and on what rule), exception edges (where the work
leaves the anticipated path) and rework loops (where it returns). A linear
procedure is a special case that happens to have one variant and no
exceptions, and it is precisely the case the concept was built to escape.

### 3.2 Agent Skill

The reusable capability. A skill is atomic, well-scoped, tool-agnostic,
composable and independently testable. It declares what it does, what it
needs, what it must not do, and how it reports. The normative contract lives
in `aop-spec` as an annex.

### 3.3 Domain Agent Harness

The controlled execution environment. A harness is the top-level AOP for
its domain: it sets the boundary conditions under which the agents inside
it operate. It defines what the agent may and may not do, what tools it
may call, what credentials it may hold, how it escalates, and how its work
is verified.

A harness that has not itself been specified as an AOP is not a harness. It
is a runtime.

### 3.4 Agent

The execution actor. The agent consumes an AOP, a skill and a context
snapshot, and produces actions and evidence. The agent has no authority of
its own. Everything it is permitted to do, it is permitted to do because the
AOP said so.

### 3.5 Agentic Operations

The broader operating mode. Agentic operations is the regime in which
agents hold delegated authority over defined operational surface, and humans
hold exception ownership rather than corridor execution. The maturity path
runs from human-operated, through assisted, to agentic, to autonomous.

## 4. Why this is not SOP automation

The distinction is not a matter of emphasis. It is structural, and it
appears in four places.

**Source.** An SOP is authored from intent: someone decided what should
happen and wrote it down. An AOP is compiled from observation: the work was
observed, cases were stitched, variants were mined, rules were extracted
with their thresholds, and the document is the output of that process, with
provenance back to the observed cases. The SOP is a hypothesis. The AOP is
a measurement.

**Structure.** An SOP is linear prose describing a corridor. An AOP is a
network of variants, decision points and exception edges. The corridor is
the exception case in the AOP, not the normal case.

**Semantics.** An SOP states what should happen. An AOP states what happens,
what the agent is authorised to decide about it, and what evidence will
demonstrate that it did. The third element has no counterpart in SOP form.

**Control.** An SOP is read by a person who may notice something the
document missed. An AOP is executed by an agent that cannot notice, so the
authority to adapt, and the boundary beyond which it must escalate, must be
written down in advance.

SOP automation preserves the document and extends its coverage with
software. AOP is a different artefact class that observes the work first
and specifies it second. Automation of an SOP inherits the happy-path
fallacy; it does not fix it.

## 5. The failure modes the concept addresses

Three failure modes bound the agency of any agent that reads prose.

**Prose semantics.** Natural language admits multiple readings. Two
operators reading the same SOP can act differently and both be right. An
agent cannot resolve ambiguity at execution time because it has no
authority to do so.

**Coverage decay.** The document and the work diverge as soon as either
moves. The gap widens silently, because the document is not tested against
the work.

**Happy-path fallacy.** The documented path is a minority of real cases.
The stated coverage is the coverage of the proposal, not the coverage of
the operation.

The AOP answers all three with the same move: compile the procedure from
observed work rather than authoring it from intent, then govern the agent
with what was observed.

## 6. The compile and run loop

```
   observe ──▶ model ──▶ compile ──▶ execute
      ▲                                 │
      │                                 ▼
      └──────── observed cases ◀──── evidence
```

**Observe.** Capture work activity as events. This is a
privacy-constrained activity: personal data is excluded by default, and the
capture surface is a declared subset of the work surface.

**Model.** Stitch events into cases, then into a Context Graph of Work with
entities for cases, tasks, steps, actors, applications, decisions, rules,
exceptions, escalations and outcomes. Detect drift: where the work has
diverged from the last known shape.

**Compile.** Mine variants with their observed frequencies. Extract decision
rules with their thresholds. Extract exception and escalation patterns.
Attach governance bounds. Produce a versioned AOP with provenance.

**Execute.** At run time: take a context snapshot, match it to a variant,
check authority against the AOP, act, record, emit. The authority check is
outside the model context and fails closed on an unmatched variant.

**Feed back.** The evidence from execution becomes observed cases for the
next compile. The loop closes, and the AOP remains true to the work.

## 7. The trust architecture

Four mechanisms, and the order matters.

**Prevent.** The agent cannot exceed its authority, because the check is
performed by a component the agent cannot influence. This is the primary
mechanism and it is structural, not behavioural.

**Verify.** Independently check the outcome of a completed action against
the intent the AOP recorded. Catches the case where an authorised action
produces a wrong result.

**Oversee.** Escalate to a human at a defined threshold, with an evidence
bundle containing the context snapshot, the matched variant, the rule that
applied, the proposed action and the options. The human decides; the agent
does not proceed on its own judgement.

**Audit.** Every case carries an append-only record of inputs, context
snapshot, rule applied, provenance, decision, approver where relevant, and
outcome.

## 8. Levels of authority

The programme's credibility ultimately rests on whether a reader can check
a claim. Three levels of authority are distinguished, and each has a
different burden of proof.

| Level | Claim | Burden of proof | Verified by |
|---|---|---|---|
| Declared | This is what the programme says AOP means | Internal consistency and reasoning | `aop-governance`, `aop-foundations` |
| Certified | This document conforms to the AOP specification | Machine validation against the schema and the conformance clauses | `aop-conformance`, `aop-spec` |
| Demonstrated | This works, and here is the evidence | Reproduction by a third party from published artefacts | `aop-evaluation`, `aop-examples` |

An authoritative concept needs all three. A concept with only the first is
an opinion. A concept with the first two is a standard. A concept with all
three is a discipline that others can build on without asking permission.

## 9. How the levels map to the estate

| Concept | Architectural responsibility | Primary home | Supporting homes |
|---|---|---|---|
| Agentic Operating Engineering | The discipline | `aop-foundations` | `aop-landscape`, `.github` |
| Agentic Operating Procedure | The operational specification | `aop-spec` | `aop-architecture`, `aop-governance` |
| Agent Skill | The reusable capability | `aop-spec` annex | `aop-toolkit`, `aop-registry`, `aop-context-graph` |
| Domain Agent Harness | The controlled execution environment | `aop-reference-harness` | `aop-architecture`, `aop-conformance` |
| Agent | The execution actor | `aop-reference-harness` | `aop-evaluation` |
| Agentic Operations | The broader operating mode | `aop-adoption` | `aop-examples`, `aop-landscape` |
