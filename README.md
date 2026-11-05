# AOP Governance

`aop-governance` is the single authority for how the Agentic Operating Procedure programme changes. It holds the architectural decision records, the change requests, the findings, the lifecycle model, the release policy, the contributor rules, and the programme plan itself.

| Field | Value |
|---|---|
| Authority | Programme change control, and the published plan |
| Tier | Governance |
| Landing wave | 1 |
| Version | 0.1.0 |
| Status | Stable |
| Licence | MIT |

## What this repository owns

- The architectural decision record (ADR) set: `decisions/`.
- The change request (CR) set: `change-requests/`.
- The finding (FND) set: `findings/`.
- The lifecycle model and the release policy: `docs/`.
- The contributor rules and the artefact templates: `docs/`, `templates/`.
- The programme plan, the repository map, the cascade checklist, and the concept model: `plans/`.

## What this repository does not own

- The definition of an Agentic Operating Procedure. That is `aop-foundations`.
- The normative model, the identifier scheme, and the conformance clauses. That is `aop-spec`.
- The change control of any other repository in the estate. Every repository owns its own change control. This repository governs the estate, not the repositories.

## How the programme changes

Three artefact classes, one authority each. The full model is in `docs/change-model.md`.

| Class | Answers | Lands in | Approval |
|---|---|---|---|
| ADR | What was decided, and why | `decisions/` | Programme owner |
| CR | A proposed change to the estate or the model | `change-requests/` | Programme owner, via an ADR |
| Finding | An investigation that produced evidence | `findings/` | Programme owner |

A change lands only when it has a record. Structural change to the estate, including repository creation, retirement, renaming, and tier reassignment, is a CR. It is audited against the cascade checklist in `plans/aop-org-cascade-checklist-org-scope.md` before it lands.

## The change record

- [Change request register](./docs/cr-register.md): one line per CR, CR-001 to CR-033, with landing states
- [Reviewer independence and claims discipline](./docs/reviewer-independence-and-claims-discipline-governance-scope.md): the GI layer
- [Programme plan addendum](./plans/aop-programme-plan-programme-scope.md): the hardening waves H1 to H5 and the estate's current state

## The estate at a glance

The full rationale, ownership boundaries, and landing order are in `plans/aop-repository-map-org-scope.md`.

| Repository | Tier | Authority | Wave |
|---|---|---|---|
| `aop-governance` | Governance | Change control and the plan | 1 |
| `aop-foundations` | Concept | What an AOP is, and what it is not | 1 |
| `aop-landscape` | Concept | How AOP differs from what already exists | 1 |
| `.github` | Governance | Org profile, templates, community files | 1 |
| `aop-spec` | Specification | The normative model, identifiers, conformance clauses | 2 |
| `aop-architecture` | Architecture | Layering, trust boundaries, the pipeline | 2 |
| `aop-context-graph` | Substrate | The entity model of observed work, drift | 3 |
| `aop-toolkit` | Tooling | Mining, extraction, compilation, linting | 4 |
| `aop-reference-harness` | Runtime | A working harness, guardrail, evidence record | 4 |
| `aop-registry` | Registry | Publication, versioning, provenance, discovery | 4 |
| `aop-conformance` | Assurance | Whether a document or a harness conforms | 5 |
| `aop-evaluation` | Evaluation | Whether the method produces a measured result | 5 |
| `aop-adoption` | Adoption | How an organisation moves from SOP to AOP | 6 |
| `aop-examples` | Adoption | A complete, reproducible demonstration | 6 |

The authority ladder descends: a repository depends on the tier below it, never on the tier above it. A change at one tier is audited down the ladder.

## Repository layout

```
aop-governance/
  README.md            # this file
  CHANGELOG.md         # release notes
  CODEOWNERS           # ownership
  LICENSE              # MIT
  change-requests/     # proposed changes to the estate or the model
  decisions/           # architectural decision records
  docs/                # lifecycle model, release policy, contributor rules
  findings/            # investigation records
  plans/               # programme plan, repository map, cascade checklist, concept model
  templates/           # artefact templates
```

## Contributing

The contribution guide, the code of conduct, and the issue and pull-request templates live in the organisation profile repository, `.github`. Every change that lands on `main` needs a corresponding record in this repository.

## Licence

MIT. See `LICENSE`.
