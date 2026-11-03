# CR-001: Seed the Wave 1 Governance Surface

| Field | Value |
|---|---|
| Status | Implemented |
| Date | 2026-11-03 |
| Owner | Emmanuel A. Otchere |
| Layer | Governance |
| Depends on | None |

## 1. Problem statement

The organisation exists, and four Wave 1 repositories exist, but none of them carries content. A repository without a README, a licence, and a stated authority is a placeholder, and a placeholder does not hold authority.

## 2. Objective

Land the governance surface: the change model, the lifecycle model, the release policy, the contributor rules, the artefact templates, and the published programme plan.

## 3. Scope

`aop-governance` only. The other three Wave 1 repositories are seeded separately.

## 4. Acceptance criteria

- `aop-governance` carries a README stating its authority in one sentence.
- The change model, the lifecycle model, the release policy, and the contributor rules are published under `docs/`.
- ADR-0001 through ADR-0010 are published under `decisions/`.
- The programme plan, the repository map, the cascade checklist, and the concept model are published under `plans/`.
- A licence commit and CODEOWNERS are present.
- A changelog entry records the landing.

## 5. Cascade audit

This change establishes the governance tier. It does not alter the meaning of any term, the shape of the model, or the boundaries of any repository. The cascade reaches no tier below governance, because no tier below governance yet exists.

## 6. What this CR is not

It is not the creation of the other Wave 1 repositories. It is not a specification, an architecture, or an implementation. It does not ratify the concept itself, which is the work of ADR-0001 through ADR-0010 and the concept model.

## 7. Implementation

Implemented in the `v0.1.0` landing of `aop-governance`.
