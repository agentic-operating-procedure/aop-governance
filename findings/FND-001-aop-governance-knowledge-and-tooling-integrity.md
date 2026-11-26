# FND-001: AOP Governance, Knowledge and Tooling Integrity Reconciliation

| Field | Value |
|---|---|
| Status | Open |
| Date | 2026-11-26 |
| Owner | Emmanuel A. Otchere |
| Scope | AOP programme governance, repository estate, concept/specification traceability, publication site and shared verification tooling |

## 1. Finding

The AOP programme has a substantial and coherent foundation: concept, normative specification, architecture, operational context, tooling, runtime, registry, assurance, evaluation, adoption and worked examples have distinct repository authorities. The eight-dimension AOP model and the observe/model/compile/execute lifecycle provide a credible basis for governed, outcome-oriented agent execution.

The current governance and publication records do not yet provide one internally consistent account of that foundation. The principal findings are:

1. CR-034 to CR-039 have merged governance PRs and, in several cases, implementation evidence in their owning repositories, but their CR files and register rows remain marked Proposed.
2. CR-035 is only partially reflected in the current specification mapping: point 4 is explicitly resolved, while point 3 still contains unresolved wording, despite the CR-035 implementation claim and the aop-spec 0.6.0 changelog stating both points are closed.
3. CR-036's implementation is present in the example generator and corpus, but its stated implementation version (aop-examples v0.3.1) does not match the current changelog, which records the CR-036 work under v0.4.0 alongside CR-037.
4. CR-040 is referenced as the record for creating the `site` repository and its changelog tooling, but no CR-040 file exists in the current `change-requests/` directory and no CR-040 commit was found by the scoped commit search.
5. The organisation contains the fourteen repositories accepted by ADR-0001 plus a fifteenth repository, `site`, which is not represented in the formal estate map. The site is not merely a static publication surface: it hosts interactive tools, JavaScript engine ports, estate synchronisation, parity checks and the changelog verifier consumed by the estate's CI.
6. The shared changelog workflow fetches `site/tools/changelog.py` from the mutable `main` branch. This creates an unpinned, cross-repository CI dependency. The verifier checks changelog structure and README version agreement; it does not verify Git tags, CR lifecycle consistency, dependency references or repository inventory.
7. Governance README, changelog and site content have not kept pace with the register. The governance README still identifies CR-001 to CR-033; the governance changelog's Unreleased section is empty after CR-039 and CR-041 merged; the site homepage still identifies CR-001 to CR-037 and describes a fourteen-repository estate.
8. The site README claims both the validator and guardrail are parity-verified. The published `tools/parity.mjs` gate imports and tests `validateAOP` against fixtures; it does not compare Guardrail decisions with the reference harness. The broader guardrail-parity claim is therefore not evidenced by that gate.
9. The six-level conceptual hierarchy, repository authority structure and programme governance structure are presented close together but are different kinds of structure. The conceptual stack contains a discipline, an operational specification, a capability contract, an execution environment, an actor and an operating regime. The repository map's linear authority-ladder language should not be mistaken for a taxonomy or for the programme's change-control hierarchy.
10. The programme has explicit Intent and Assurance dimensions, evaluation methods and outcome measures, but the reviewed governance surfaces do not yet expose one end-to-end traceability contract linking stakeholder purpose, intended operational outcomes, measures and baselines, decision/action execution, evidence, evaluation and value claims.

These are governance and knowledge-integrity findings. They do not invalidate the AOP concept or imply that the existing runtime and reference examples are unusable. They identify where the programme's public claims, authority boundaries and verification evidence need to be brought back into alignment.

## 2. Problem being addressed

The investigation answers whether the AOP organisation currently provides a reliable and unambiguous structure for:

- identifying the authoritative source for each concept, model, rule, tool and result;
- determining the accepted, implemented and outstanding state of each programme change;
- tracing implementation claims to merged changes, released versions, tags and reproducible verification;
- distinguishing normative artefacts from explanatory, illustrative and interactive representations;
- ensuring that tools used to validate or demonstrate AOP behaviour are tested against the authoritative implementation they claim to represent; and
- tracing purposeful intent through execution evidence to verified operational outcomes without treating conformance or synthetic demonstration results as proof of business value.

## 3. Investigation scope

### In scope

- `aop-governance`: CR register, CR-034 to CR-041, README, changelog, change model, repository map, ADR-0001 and ADR-0006.
- Merged governance PRs #17, #18, #19, #20, #22, #23 and #24.
- Owning-repository evidence for CR-035, CR-036 and CR-037.
- The formal fourteen-repository estate and the additional `site` repository.
- The shared changelog verifier and its CI integration.
- The site publication, interactive tools and parity workflow.
- The conceptual hierarchy, eight-dimension model and the relationship between the knowledge structure and the execution/tooling lifecycle.

### Out of scope

- Implementing CR-041's fault-management fixture remediation.
- Changing normative AOP clauses, schemas or runtime behaviour.
- Reassessing the technical correctness of every historical hardening CR from CR-001 to CR-033.
- Treating synthetic exemplar results as live operational or enterprise performance.
- Making changes to Zero-TAF, OpenDEA or Enterprise-Semantics repositories.

## 4. Working hypothesis

The programme's core architecture is viable, but its governance and knowledge surfaces have accumulated drift because implementation state, release evidence, repository inventory and public presentation are not governed by a single verifiable integrity contract.

The hypothesis would be falsified if the current source records, merged PRs, releases, tags, CI workflows and publication site could be shown to agree on every CR state, repository boundary, authority claim and verification assertion.

## 5. Evidence

### 5.1 CR lifecycle and merged implementation records

The following governance PRs are confirmed merged:

| CR | Governance PR | Merge commit | Evidence and observed disposition |
|---|---|---|---|
| CR-034 | [#17](https://github.com/agentic-operating-procedure/aop-governance/pull/17) | `a974cd3ddf30dbae73667e90dac6b563279f8edf` | Register, programme plan addendum, change-model wiring and README changes landed. CR and register status remain Proposed. |
| CR-035 | [#18](https://github.com/agentic-operating-procedure/aop-governance/pull/18) | `e96e588f1418fce76aa434e3ffee63a38ef1d6bb` | Governance record landed. Current aop-spec mapping explicitly resolves point 4 but leaves point 3 without the disposition required by CR-035. |
| CR-036 | [#19](https://github.com/agentic-operating-procedure/aop-governance/pull/19) | `75b98658a47857f02f4df5352f22eb12ef938256` | Origin tagging and `--agent-fraction` are present in the example corpus generator; changelog records CR-036 under aop-examples v0.4.0, not the CR's stated v0.3.1. |
| CR-037 | [#20](https://github.com/agentic-operating-procedure/aop-governance/pull/20) | `7b1464520e9f7673543623646cb8848d5804fac5` | aop-examples v0.4.0 records canonical metric bindings and the process contribution's accepted-but-not-yet-canonically-assigned state. |
| CR-038 | [#22](https://github.com/agentic-operating-procedure/aop-governance/pull/22) | `4ececd6329f6775c44820736065eaa90f532ace3` | Repository map relationship landed. Reciprocal accepted Zero-TAF ADR-ZTAF-0006 cites CR-038. CR and register status remain Proposed. |
| CR-039 | [#23](https://github.com/agentic-operating-procedure/aop-governance/pull/23) | `e1f594e262dcdad583290abaaad141b8da84c742` | The changelog workflow exists in all thirteen formal repositories other than the shared `.github` repository. The workflow fetches the verifier from the site repository. Full tag and CI-run evidence across the estate has not been established by this investigation. |
| CR-041 | [#24](https://github.com/agentic-operating-procedure/aop-governance/pull/24) | `a863f702ce04520bdb6f6ba5ea47b0d782be0153` | Proposal record and register row landed. Proposed status is correct; merge does not constitute acceptance or implementation. |

The current register labels CR-034 to CR-039 Proposed despite the merged records and implementation evidence above. CR-041 is also Proposed, correctly. CR-040 has a register row describing the missing record, but no corresponding CR file was found.

### 5.2 CR-035 specification inconsistency

The current `aop-spec/docs/aop-metamodel-mapping-specification-scope.md` states that reconciliation point 4 is resolved by CR-035. Point 3 still says the metamodel Stage 01 decision “should be cited” and does not record the completed disposition required by CR-035. The aop-spec 0.6.0 changelog, however, says points 3 and 4 are closed. The CR's implementation claim therefore overstates the current mapping document's state.

### 5.3 CR-036 release inconsistency

The aop-examples generator contains the `origin: human` case attribute and the `--agent-fraction` option for generating agent-origin cases. The changelog records origin tagging under v0.4.0 together with CR-037. CR-036 itself says implementation was in v0.3.1; no v0.3.1 release section appears in the current changelog. The implementation is visible, but the release reference needs correction.

### 5.4 Site repository and CI dependency

The organisation repository search returns the fourteen repositories described by ADR-0001 and the additional public repository `agentic-operating-procedure/site`.

The site README describes documentation, five live tools, browser-side validator/guardrail engines, auto-sync from the estate and the shared changelog verifier. The site therefore has a real publication and interactive-tooling role, but its authority and relationship to the formal fourteen-repository estate have not been recorded in ADR-0001 or the repository map.

The site has a v0.1.0 changelog entry but no Git tag was found in its tag references. This is not automatically a CR-039 breach if the site is formally outside the estate; its versioning and governance treatment must first be stated.

### 5.5 Verification-tool limitations

The shared workflow fetches the verifier from:

`https://raw.githubusercontent.com/agentic-operating-procedure/site/main/tools/changelog.py`

The mutable branch reference means a change to the site tool can alter CI behaviour across repositories without a version-pinned dependency update in those repositories.

The verifier checks:
- the presence and position of the Unreleased section;
- descending release headings;
- release/link-reference consistency;
- duplicate release sections; and
- README version agreement when a version row is present.

It does not check:
- that a README version row exists;
- that the corresponding Git tag exists;
- that CR files and register rows exist and agree on status;
- that CR dependencies resolve;
- that the register's CR range agrees with the README and changelog;
- that the repository inventory agrees with the accepted estate decision; or
- that a published implementation claim has linked merge and verification evidence.

The site parity workflow imports `validateAOP` and checks fixture verdicts. It does not compare the browser Guardrail's decisions with the Python reference harness. The published assertion that both validator and guardrail parity are verified is not supported by this particular gate.

### 5.6 Stale publication records

- `aop-governance/README.md` says the CR register covers CR-001 to CR-033.
- `aop-governance/CHANGELOG.md` has an empty Unreleased section and no entry for the merged CR-039 and CR-041 governance changes.
- The site homepage says the register covers CR-001 to CR-037 and describes a fourteen-repository estate.
- The live CR register covers CR-001 to CR-041 and explicitly identifies the missing CR-040 file.

### 5.7 Concept and knowledge-structure boundary

The foundations repository describes the six-level model as a conceptual hierarchy. Its elements are different kinds of things: a discipline, a procedure specification, a reusable capability, an execution environment, an actor and an operating regime. The programme also has a distinct eight-dimension AOP model and a fourteen-repository authority structure.

These structures are useful, but they must be related through typed relationships rather than collapsed into one ladder. The programme needs explicit distinctions between:
- conceptual classification and operational composition;
- artefact authority and programme change authority;
- authored intent, observed work, compiled procedure and authorised execution;
- AOP specification, skill contract, harness, agent, run and skill invocation; and
- execution outputs, verified operational outcomes and attributable enterprise value.

The reviewed governance surfaces do not yet identify one normative, end-to-end contract for tracing stakeholder purpose and outcome measures through these stages to evidence and evaluation.

## 6. Provenance

Primary evidence:

- [ADR-0001: Fourteen-repository estate](https://github.com/agentic-operating-procedure/aop-governance/blob/main/decisions/ADR-0001-polyrepo-estate-of-fourteen-repositories-across-eleven-tiers.md)
- [ADR-0006: Decision-rights ladder](https://github.com/agentic-operating-procedure/aop-governance/blob/main/decisions/ADR-0006-authority-is-a-decision-rights-ladder-over-five-risk-axes.md)
- [CR register](https://github.com/agentic-operating-procedure/aop-governance/blob/main/docs/cr-register.md)
- [Governance README](https://github.com/agentic-operating-procedure/aop-governance/blob/main/README.md)
- [Governance changelog](https://github.com/agentic-operating-procedure/aop-governance/blob/main/CHANGELOG.md)
- [Repository map](https://github.com/agentic-operating-procedure/aop-governance/blob/main/plans/aop-repository-map-org-scope.md)
- [Change model](https://github.com/agentic-operating-procedure/aop-governance/blob/main/docs/change-model.md)
- [CR-034 through CR-041](https://github.com/agentic-operating-procedure/aop-governance/tree/main/change-requests)
- [aop-spec metamodel mapping](https://github.com/agentic-operating-procedure/aop-spec/blob/main/docs/aop-metamodel-mapping-specification-scope.md)
- [aop-spec changelog](https://github.com/agentic-operating-procedure/aop-spec/blob/main/CHANGELOG.md)
- [aop-examples generator](https://github.com/agentic-operating-procedure/aop-examples/blob/main/corpus/generate_ran_cases.py)
- [aop-examples changelog](https://github.com/agentic-operating-procedure/aop-examples/blob/main/CHANGELOG.md)
- [site README](https://github.com/agentic-operating-procedure/site/blob/main/README.md)
- [site changelog verifier](https://github.com/agentic-operating-procedure/site/blob/main/tools/changelog.py)
- [site parity workflow](https://github.com/agentic-operating-procedure/site/blob/main/.github/workflows/deploy.yml)
- [Zero-TAF ADR-ZTAF-0006](https://github.com/Zero-TAF/ztaf-governance/blob/main/decisions/ADR-ZTAF-0006.md)

The investigation is based on current default-branch file content, GitHub repository inventory, merged PR metadata, changed-file lists and selected tag references as observed on 2026-11-26. The absence of a CR-040 file is based on the current `change-requests/` directory listing and a scoped search for CR-040 commits; it does not prove that no unrecorded local or external draft ever existed.

## 7. Proposed next step

Use this finding as the evidence basis for a governance reconciliation CR (proposed CR-042), with the following ordered work:

1. Reconcile CR-034 to CR-041 against their acceptance criteria, implementation PRs, release entries, tags and verification evidence. Update each CR file and the register only where evidence supports the status. Introduce an explicit Partially implemented state if the current lifecycle cannot represent partial completion accurately.
2. Recover the original CR-040 evidence. If it cannot be recovered, create a clearly labelled retrospective record with provenance and uncertainty; do not fabricate historical approval or renumber subsequent CRs.
3. Decide through an ADR whether `site` is a fifteenth governed repository or an explicitly external publication surface. Record its authority, dependencies, lifecycle, versioning and relationship to the formal estate.
4. Remove the mutable site-main dependency from estate CI. Place the verifier under an appropriate authoritative owner and consume it through an immutable version or digest. Extend governance checks to cover CR/register consistency, dependency references, repository inventory and tag evidence.
5. Reconcile the governance README, changelog and site pages with the authoritative register and estate decision. Make stale status claims fail CI where practical.
6. Correct CR-035's point-3 mapping disposition and CR-036's implementation-version reference in their owning repositories.
7. Add a guardrail parity test that compares browser-side decision outcomes with the reference harness, or narrow the site's claim to the behaviour actually tested.
8. Commission a separate cross-repository knowledge-architecture CR to formalise the relationships between the six-level conceptual stack, eight AOP dimensions, repository authority graph, transformation lifecycle, runtime entities and outcome/evidence model. Keep this distinct from the immediate governance repairs.
9. Keep CR-041 Proposed until accepted through the change model. Do not begin its multi-repository remediation as a consequence of this finding alone.

FND-001 remains Open until the governance reconciliation and the follow-on knowledge/tooling integrity work have explicit owners, accepted records and evidence-backed closure criteria.
