# Contracts

Lightweight interface notes for programmes that pin this method.

## Expected from this repo

- Sealed release JSON under `releases/vX.Y.Z.json`
- Stable technique ids (`T-XXX`) and registry
- Verification CLIs that exit non-zero on structural failure

## Expected from consuming programmes

- A pin (git tag / submodule / vendored release JSON)
- Local mapping of commitments to programme artefacts
- No silent copy of techniques without citing lineage ids back to this method (or a fork's ledger)

## Non-goals

Contracts here do not encode domain science, ethics approval, or claim acceptance.
