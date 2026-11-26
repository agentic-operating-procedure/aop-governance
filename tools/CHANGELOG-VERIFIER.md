# Canonical changelog verifier

## Authority

The canonical estate changelog utility is maintained at
`aop-governance/tools/changelog.py`. The source was relocated from
`agentic-operating-procedure/site/tools/changelog.py` under CR-042.

The site copy is a legacy compatibility copy during the migration. It is not
an independent source of authority and must not be modified to introduce
different verification behaviour.

## Consumer contract

A repository consuming this utility must:

1. Fetch it from an immutable commit in `aop-governance`, never from a branch
   name such as `main`.
2. Verify the downloaded file against a SHA-256 digest recorded in the
   consumer workflow or another reviewed, immutable integrity manifest.
3. Stop the workflow if fetching, digest verification, Python setup or tool
   execution fails. A skipped verifier is not a pass.
4. Run the verifier against the checked-out repository contents.
5. Report the verifier result separately from dependency acquisition and
   setup results.

The immutable commit and digest are deliberately not populated in this
initial relocation change. They must be taken from the merged canonical
revision and then applied consistently in the estate migration tranche.

## Commands

- `python3 tools/changelog.py verify <repository-path>`
- `python3 tools/changelog.py add <repository-path> <version> <date> <entry-file>`

The utility validates changelog section structure, release ordering, link
references, duplicate release sections and the README Version row. It does
not establish semantic correctness of a release, AOP conformance, execution
validity, outcome achievement or attributable organisational value.

## Verification

The standard-library test suite is run with:

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
python3 tools/changelog.py verify .
```
