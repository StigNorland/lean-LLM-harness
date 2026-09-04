# How the methodology itself is updated

The living paper and tooling evolve under a **controlled update loop**. Silent rewrite of commitments or silent assimilation of external techniques is forbidden.

## Loop

```
1. Propose technique (GitHub issue, technique-proposal template)
2. Add lineage stub (status: proposed) + registry entry
3. Implement behind tests (verification, docs, METHOD mentions if in-method)
4. Open PR → admission CI (pytest + admit.py)
5. Decision: adopt | adapt | reject (human / programme owners)
6. Seal method release under releases/vX.Y.Z.json
7. Consuming programmes bump their pin intentionally
```

## Status transitions

| From | To | Requires |
|------|-----|----------|
| (new) | `proposed` | Issue + lineage stub + real sources |
| `proposed` | `adopted` / `adapted` | Validation evidence, tests, METHOD id cite, admission green |
| `proposed` | `rejected` | Short rationale in record; may remain for audit |
| `originated-here` | (stable) | Seed / self lineage; treat like adopted for METHOD cites |

## Sealing a release

1. Ensure `admit.py` and pytest pass on the tip to seal.
2. Write `releases/vX.Y.Z.json` listing in-method technique ids and commitment summary.
3. Tag `vX.Y.Z` and update `CHANGELOG.md`.
4. Announce pin bump guidance in consuming programmes (see `consuming-programmes.md`).

## What not to do

- Edit `METHOD.md` commitments without a changelog entry and, if techniques change, lineage updates.
- Mark external techniques `adopted` without sources and validation evidence.
- Ask programmes to pin `main` for production claims work.
