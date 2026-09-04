# Verification

| Script | Purpose |
|--------|---------|
| `admit.py` | Validate lineage files + registry; ensure METHOD cites adopted techniques |
| `check_lineage.py` | Registry consistency; METHOD citation keys resolve |
| `tests/` | pytest coverage for admission and lineage checks |

```bash
python infrastructure/verification/admit.py
python infrastructure/verification/admit.py --pr-diff changed_files.txt
python infrastructure/verification/check_lineage.py
python -m pytest infrastructure/verification/tests
```

Optional dependency: `jsonschema` (structural checks used if unavailable).
