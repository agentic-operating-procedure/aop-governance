# ADR-0008: Per-Repository Agent Doctrine Files Are Local-Only

_Status: Accepted_

## Context

Working repositories in this estate carry a local doctrine file that points
at the board, the skill and the snapshot for the channel that owns them.

## Decision

Those doctrine files are local working configuration. They are excluded from
published repository content and are listed in each repository's ignore
file.

## Rationale

The doctrine encodes how an assistant operates against a repository. It is
operational configuration for a specific collaborator, not part of the
authority a reader consumes. Publishing it would put process scaffolding
into the artefact that is meant to be the authority.

## Consequences

A clone of any repository is immediately usable for its published purpose.
A collaborator who wants the local doctrine copies it from the workspace.
