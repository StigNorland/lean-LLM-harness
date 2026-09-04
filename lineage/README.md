# Lineage ledger

Borrowed techniques **must** be cited. This directory is the citation ledger for the living research method.

## Rules

1. Every technique has a file `techniques/T-XXX-slug.md` and an entry in `registry.json`.
2. Status values: `proposed` | `adopted` | `adapted` | `rejected` | `originated-here`.
3. Only `adopted`, `adapted`, and `originated-here` count as part of the sealed method surface. They must be mentioned by id in `METHOD.md`.
4. `proposed` stubs illustrate intake and support discussion; they must **not** be treated as adopted.
5. Sources need real URLs (or bibliographic keys in `bibliography.bib`). Do not invent citations.
6. When adapting, record what was taken, what was changed (`adapted`), and what was deliberately left out (`rejected_parts`).

## Workflow

```
issue (technique-proposal) → lineage stub (proposed)
  → implement behind tests → PR + admit CI
  → decision (adopt / adapt / reject) → seal method release
  → consuming programmes bump pin
```

See [`docs/update-strategy.md`](../docs/update-strategy.md).

## Machine index

[`registry.json`](registry.json) is the machine-readable index. Schema: [`schemas/technique-lineage.schema.json`](../schemas/technique-lineage.schema.json).

## Verification

```bash
python infrastructure/verification/check_lineage.py
python infrastructure/verification/admit.py
```
