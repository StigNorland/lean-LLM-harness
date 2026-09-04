# Consuming programmes

How programmes such as [screen-medium-foundations](https://github.com/StigNorland/screen-medium-foundations) pin and use this method.

## Pin a sealed release

Prefer a **tag** or vendored release JSON over tracking the living tip:

```bash
git clone --branch v0.1.0 --depth 1 \
  https://github.com/StigNorland/lean-LLM-harness.git method
```

Or record in your programme:

```json
{
  "method": "lean-LLM-harness",
  "pin": "v0.1.0",
  "url": "https://github.com/StigNorland/lean-LLM-harness"
}
```

Read `releases/v0.1.0.json` for the sealed technique set and commitment summary.

## Do

- Map METHOD §2 commitments onto local artefacts (status labels, gates, prereg, negatives).
- Cite lineage ids (`T-001`, …) when you rely on a technique from this method.
- Bump the pin deliberately when adopting a new sealed release.
- Keep programme science in the programme repo.

## Do not

- Copy domain ontology or experimental claims into this method repo.
- Silently paste techniques from elsewhere into the programme without lineage (propose upstream or maintain a local ledger that still cites sources).
- Treat method CI green as acceptance of a scientific claim.

## Compatibility

Breaking commitment changes should bump the major version of the sealed release. Programmes should read `CHANGELOG.md` before bumping.
