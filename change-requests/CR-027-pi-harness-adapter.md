# CR-027: Optional Pi-Based Harness Adapter

| Field | Value |
|---|---|
| Estate ID | CR-027 (Review 2, item 18) |
| Class | Implementation + Adoption |
| Priority | P2 |
| Depends on | CR-011, CR-015, CR-019 |
| State | In progress (the experimental adapter + self-test 5/5 landed under CR-032; a live Pi integration and the promotion gates remain) |

## Problem

Pi (earendil-works/pi) is an extensible agent harness with an SDK, skills and extensions, and explicitly provides no built-in filesystem, process, network or credential permission system, running with the launching process's permissions. A Pi extension alone therefore cannot serve as the AOP enforcement boundary. As an optional reference integration it would demonstrate the estate's implementation-neutrality principle on a real third-party harness.

## Change

Prototype an optional adapter: Pi reasons and proposes; the external guardrail and sandbox mediate all effects; immutable AOP versions load with bounded context; Pi tool proposals translate to canonical actions through the enforcement point; direct shell, filesystem, process, network and credential routes are sandboxed or denied unless explicitly mediated; SOP intake through publication remains separate auditable stages; the domain package composes approved AOPs and versioned skills with explicit precedence rules.

## Acceptance

- The adapter passes the relevant document and harness profiles, including bypass attempts through extensions or subprocesses.
- Labelled experimental until an independent implementation and a live pilot pass the relevant gates. Never a normative dependency.

## Landing note (2026-11-05)

Landed under CR-032. See the landing CR for the full audit.
