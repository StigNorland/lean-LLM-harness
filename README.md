# lean-LLM-harness

A **living, controlled, traceable** research-honesty methodology — portable tooling that research programmes can clone or pin.

This repository is the **method**, not a science programme. It does not contain domain ontology, programme-specific gates, or experimental claims. Programmes such as [screen-medium-foundations](https://github.com/StigNorland/screen-medium-foundations) pin a sealed release and apply the commitments locally.

## Quick start

```bash
# Pin a sealed release (preferred for consuming programmes)
git clone --branch v0.1.0 --depth 1 \
  https://github.com/StigNorland/lean-LLM-harness.git

# Or work on the living tip (maintainers / contributors)
git clone https://github.com/StigNorland/lean-LLM-harness.git
cd lean-LLM-harness
python -m venv .venv && source .venv/bin/activate
pip install pytest jsonschema
python infrastructure/verification/admit.py
python -m pytest infrastructure/verification/tests
```

## What to read

| Document | Role |
|----------|------|
| [`METHOD.md`](METHOD.md) | Canonical living paper — commitments, limits, application |
| [`lineage/`](lineage/) | Citation ledger for every borrowed or originated technique |
| [`releases/`](releases/) | Sealed method versions for programme pins |
| [`docs/consuming-programmes.md`](docs/consuming-programmes.md) | How programmes pin and stay compatible |
| [`docs/update-strategy.md`](docs/update-strategy.md) | How the methodology itself evolves |
| [`AGENTS.md`](AGENTS.md) | Hard rules for human and agent contributors |

## Design in one paragraph

Good-faith authors still degrade: status inflation, post-hoc prereg edits, deleted negatives, analogy sold as derivation, fit sold as prediction. This method makes **epistemic status explicit**, keeps **negatives and underdetermination permanent**, orders **gates so downstream work cannot rescue upstream failure**, requires **preregistration before decisive steps**, and insists that **automation verifies but never decides**. Techniques borrowed from elsewhere must land as **lineage records** before adoption; silent assimilation is forbidden. Pull requests that change the method must pass **admission validation**.

## Do not

- Copy programme-specific science into this repo.
- Adopt a technique without a lineage record and citation.
- Treat CI green as a scientific decision.
- Invent citations or backfill lineage after the fact.

## License and citation

MIT — see [`LICENSE`](LICENSE). Cite via [`CITATION.cff`](CITATION.cff).

## Status

Scaffold `v0.1.0`. First sealed release points at the SMF-originated core commitments (`T-001`). Proposed external techniques (`T-002`–`T-004`) illustrate intake format only and are **not adopted**.
