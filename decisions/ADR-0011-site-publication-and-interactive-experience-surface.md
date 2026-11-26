# ADR-0011: The AOP Site Is a Publication and Interactive Experience Surface

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-26 |
| Owner | Emmanuel A. Otchere |
| Layer | Governance |
| Depends on | ADR-0001; CR-042 |
| Supersedes | — |

## 1. Context

ADR-0001 defines a fourteen-repository core estate in which each repository holds authority for one class of programme artefact. The organisation also contains `agentic-operating-procedure/site`, which publishes programme information, hosts interactive tools and mirrors selected artefacts from the core estate.

The site is operationally significant, but it is not currently represented in the fourteen-repository estate. Its current responsibilities include documentation and publication, interactive demonstrations, browser-side representations of AOP validation and guardrail behaviour, synchronisation and parity tooling, and the shared changelog verifier currently consumed by core-repository CI.

Without an explicit boundary, the site can be mistaken for a fifteenth core authority repository. Browser-side implementations and published descriptions may also be mistaken for normative or conformance authorities.

## 2. Decision

Classify `agentic-operating-procedure/site` as the **AOP programme publication and interactive experience surface**, outside the fourteen-repository core authority estate defined by ADR-0001.

The site may:
- publish and explain authoritative AOP artefacts;
- present documentation, diagrams, learning material and worked examples;
- host interactive demonstrations and browser-side implementations;
- synchronise and display versioned material from authoritative repositories;
- expose links to the source artefacts, versions and verification evidence.

The site does not:
- define or amend the AOP concept or normative vocabulary;
- own the normative AOP model, identifiers, schemas or conformance clauses;
- define architecture or runtime trust boundaries;
- authorise actions or establish runtime decision authority;
- certify conformance or independently upgrade evaluation claims;
- replace the reference harness, specification validator or authoritative conformance process.

For each mirrored or executable representation, the site must identify its authoritative upstream source and version. Where the site contains an implementation of normative behaviour, its parity with the authoritative implementation must be demonstrated by reproducible tests; otherwise it must be labelled as illustrative or experimental.

The programme-wide changelog verifier is governance tooling, not a site publication responsibility. Its authoritative source belongs in `aop-governance`; the site may consume it as a pinned dependency.

## 3. Rationale

This classification preserves the fourteen-repository authority model while acknowledging the site's distinct publication and interaction role. It avoids both extremes: silently treating the site as a core normative repository, or treating it as an ungoverned static website despite its executable tools and CI dependencies.

The site can evolve at a publication cadence without changing the authority or lifecycle of the artefacts it presents.

## 4. Consequences

- ADR-0001 continues to describe the fourteen-repository core estate; the site is recorded separately as a programme surface.
- The repository map and governance README identify the site and its upstream dependencies without counting it as a core authority repository.
- Site content must expose source provenance and version information for normative and executable representations.
- Changelog verification policy and implementation are owned by `aop-governance`, consumed by immutable references.
- Site parity claims must be scoped to tests actually executed.
- Promotion of the site into the core estate, or transfer of an authoritative responsibility to it, requires a separate CR and ADR.

## 5. What this decision is not

This ADR does not create a new repository, alter the AOP specification, transfer normative authority to the site, or assert that the current site tooling is already conformant or fully parity-verified.
