#!/usr/bin/env python3
"""Check that METHOD citation keys resolve and the registry is consistent."""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Reuse admit helpers
sys.path.insert(0, str(Path(__file__).resolve().parent))
from admit import (  # noqa: E402
    IN_METHOD_STATUSES,
    METHOD_PATH,
    REGISTRY_PATH,
    REPO_ROOT,
    TECHNIQUES_DIR,
    AdmitError,
    load_json,
    parse_yaml_frontmatter,
)

T_ID_RE = re.compile(r"\bT-\d{3}\b")


def main() -> int:
    errors: list[str] = []
    registry = load_json(REGISTRY_PATH)
    known = {e["id"]: e for e in registry.get("techniques", []) if "id" in e}

    method = METHOD_PATH.read_text(encoding="utf-8")
    cited = sorted(set(T_ID_RE.findall(method)))
    for tid in cited:
        if tid == "T-000":
            continue
        if tid not in known:
            errors.append(f"METHOD.md cites {tid} but registry has no such id")

    for tid, entry in known.items():
        path = REPO_ROOT / entry["path"]
        if not path.is_file():
            errors.append(f"registry {tid}: missing file {entry['path']}")
            continue
        try:
            record = parse_yaml_frontmatter(path.read_text(encoding="utf-8"))
        except AdmitError as exc:
            errors.append(f"{entry['path']}: {exc}")
            continue
        if record.get("id") != tid:
            errors.append(f"{entry['path']}: frontmatter id {record.get('id')!r} != {tid}")
        if entry.get("status") != record.get("status"):
            errors.append(
                f"{tid}: registry/file status mismatch "
                f"({entry.get('status')!r} vs {record.get('status')!r})"
            )
        if entry.get("status") in IN_METHOD_STATUSES and tid not in method:
            errors.append(f"in-method {tid} not mentioned in METHOD.md")

    # Orphan technique files
    for path in TECHNIQUES_DIR.glob("T-*.md"):
        if path.name == "T-000-template.md":
            continue
        try:
            record = parse_yaml_frontmatter(path.read_text(encoding="utf-8"))
        except AdmitError as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        tid = record.get("id")
        if tid not in known:
            errors.append(f"{path.name}: not listed in registry.json")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"check_lineage: FAILED ({len(errors)} error(s))", file=sys.stderr)
        return 1

    print("check_lineage: OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AdmitError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
