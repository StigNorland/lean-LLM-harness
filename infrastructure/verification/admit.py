#!/usr/bin/env python3
"""Admission CLI: validate lineage + registry; METHOD cites in-method techniques.

Exit 0 on success, non-zero on failure. Prints clear errors to stderr.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:  # pragma: no cover - optional dependency
    jsonschema = None  # type: ignore

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "lineage" / "registry.json"
SCHEMA_PATH = REPO_ROOT / "schemas" / "technique-lineage.schema.json"
METHOD_PATH = REPO_ROOT / "METHOD.md"
TECHNIQUES_DIR = REPO_ROOT / "lineage" / "techniques"

IN_METHOD_STATUSES = frozenset({"adopted", "adapted", "originated-here"})
ALLOWED_STATUSES = frozenset(
    {"proposed", "adopted", "adapted", "rejected", "originated-here"}
)
ID_RE = re.compile(r"^T-\d{3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
YAML_FENCE_RE = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)


class AdmitError(Exception):
    pass


def _err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AdmitError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise AdmitError(f"invalid JSON in {path}: {exc}") from exc


def parse_yaml_frontmatter(text: str) -> dict[str, Any]:
    """Minimal YAML subset parser for technique fenced blocks.

    Supports: scalars, quoted strings, folded (>) / literal (|) blocks,
    and simple lists of scalars or of mappings with indented keys.
    """
    match = YAML_FENCE_RE.search(text)
    if not match:
        raise AdmitError("technique file missing ```yaml``` frontmatter block")
    raw = match.group(1)
    lines = raw.splitlines()
    data: dict[str, Any] = {}
    i = 0
    n = len(lines)

    def indent_of(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    while i < n:
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        if indent_of(line) != 0:
            raise AdmitError(f"unexpected indent at top level: {line!r}")
        if ":" not in line:
            raise AdmitError(f"expected key: value, got: {line!r}")
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest in ("|", ">"):
            block_lines: list[str] = []
            i += 1
            while i < n and (not lines[i].strip() or indent_of(lines[i]) > 0):
                block_lines.append(lines[i][2:] if lines[i].startswith("  ") else lines[i])
                i += 1
            data[key] = "\n".join(block_lines).strip()
            continue
        if rest == "":
            # list or nested — look ahead
            i += 1
            items: list[Any] = []
            while i < n and lines[i].lstrip().startswith("- "):
                item_line = lines[i]
                item_body = item_line.lstrip()[2:]
                if ":" in item_body and not item_body.strip().startswith("http"):
                    # mapping list item
                    obj: dict[str, Any] = {}
                    first_key, _, first_val = item_body.partition(":")
                    obj[first_key.strip()] = _parse_scalar(first_val.strip())
                    base_indent = indent_of(item_line)
                    i += 1
                    while i < n and indent_of(lines[i]) > base_indent and not lines[i].lstrip().startswith("- "):
                        sub = lines[i].strip()
                        if ":" in sub:
                            sk, _, sv = sub.partition(":")
                            obj[sk.strip()] = _parse_scalar(sv.strip())
                        i += 1
                    items.append(obj)
                else:
                    items.append(_parse_scalar(item_body.strip()))
                    i += 1
            data[key] = items
            continue
        data[key] = _parse_scalar(rest)
        i += 1
    return data


def _parse_scalar(value: str) -> Any:
    if value == "":
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if value.startswith("#"):
        return ""
    if " #" in value:
        value = value.split(" #", 1)[0].rstrip()
    if value in ("true", "false"):
        return value == "true"
    if value == "[]":
        return []
    if value == "{}":
        return {}
    return value


def structural_validate(record: dict[str, Any], path: Path) -> list[str]:
    errors: list[str] = []
    required = [
        "id",
        "title",
        "status",
        "sources",
        "taken",
        "adapted",
        "rejected_parts",
        "serves_commitments",
        "failure_modes",
        "date",
    ]
    for field in required:
        if field not in record:
            errors.append(f"{path}: missing required field '{field}'")
    if "id" in record and not ID_RE.match(str(record["id"])):
        errors.append(f"{path}: id must match T-XXX, got {record['id']!r}")
    if "status" in record and record["status"] not in ALLOWED_STATUSES:
        errors.append(f"{path}: invalid status {record['status']!r}")
    if "date" in record and not DATE_RE.match(str(record["date"])):
        errors.append(f"{path}: date must be YYYY-MM-DD, got {record['date']!r}")
    if "sources" in record:
        if not isinstance(record["sources"], list) or len(record["sources"]) < 1:
            errors.append(f"{path}: sources must be a non-empty list")
        else:
            for idx, src in enumerate(record["sources"]):
                if not isinstance(src, dict) or "url" not in src or "kind" not in src:
                    errors.append(f"{path}: sources[{idx}] needs url and kind")
    for list_field in ("serves_commitments", "failure_modes"):
        if list_field in record and not isinstance(record[list_field], list):
            errors.append(f"{path}: {list_field} must be a list")
    return errors


def schema_validate(record: dict[str, Any], schema: dict[str, Any], path: Path) -> list[str]:
    if jsonschema is None:
        return structural_validate(record, path)
    validator = jsonschema.Draft202012Validator(schema)
    return [f"{path}: {e.message}" for e in validator.iter_errors(record)]


def collect_technique_files(pr_diff: Path | None) -> list[Path]:
    all_files = sorted(
        p
        for p in TECHNIQUES_DIR.glob("T-*.md")
        if p.name != "T-000-template.md"
    )
    if pr_diff is None:
        return all_files
    listed = [
        line.strip()
        for line in pr_diff.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    lineage_changed = [
        REPO_ROOT / rel
        for rel in listed
        if rel.replace("\\", "/").startswith("lineage/")
    ]
    if not lineage_changed:
        print("admit: --pr-diff provided but no lineage/ paths; skipping technique file checks")
        return []
    # Still validate full set for registry consistency when lineage changes
    return all_files


def admit(pr_diff: Path | None = None) -> int:
    errors: list[str] = []
    registry = load_json(REGISTRY_PATH)
    schema = load_json(SCHEMA_PATH) if SCHEMA_PATH.exists() else {}

    if "techniques" not in registry or not isinstance(registry["techniques"], list):
        raise AdmitError("registry.json missing techniques array")

    reg_by_id: dict[str, dict[str, Any]] = {}
    for entry in registry["techniques"]:
        tid = entry.get("id")
        if not tid:
            errors.append("registry entry missing id")
            continue
        if tid in reg_by_id:
            errors.append(f"duplicate registry id {tid}")
        reg_by_id[tid] = entry
        rel = entry.get("path")
        if not rel:
            errors.append(f"registry {tid}: missing path")
            continue
        path = REPO_ROOT / rel
        if not path.is_file():
            errors.append(f"registry {tid}: path does not exist: {rel}")

    technique_files = collect_technique_files(pr_diff)
    file_by_id: dict[str, Path] = {}
    records: dict[str, dict[str, Any]] = {}

    for path in technique_files:
        try:
            record = parse_yaml_frontmatter(path.read_text(encoding="utf-8"))
        except AdmitError as exc:
            errors.append(f"{path.relative_to(REPO_ROOT)}: {exc}")
            continue
        tid = str(record.get("id", ""))
        file_by_id[tid] = path
        records[tid] = record
        errors.extend(schema_validate(record, schema, path.relative_to(REPO_ROOT)))
        if tid and tid not in reg_by_id:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: technique {tid} not listed in registry.json"
            )
        elif tid in reg_by_id:
            reg = reg_by_id[tid]
            if reg.get("status") and reg["status"] != record.get("status"):
                errors.append(
                    f"{tid}: registry status {reg['status']!r} != file status {record.get('status')!r}"
                )
            expected_rel = str(path.relative_to(REPO_ROOT)).replace("\\", "/")
            if reg.get("path") and reg["path"].replace("\\", "/") != expected_rel:
                errors.append(
                    f"{tid}: registry path {reg['path']!r} != {expected_rel!r}"
                )

    # Every in-method registry technique must have a file and METHOD mention
    if not METHOD_PATH.is_file():
        errors.append("METHOD.md missing")
        method_text = ""
    else:
        method_text = METHOD_PATH.read_text(encoding="utf-8")

    for tid, entry in reg_by_id.items():
        status = entry.get("status")
        if status in IN_METHOD_STATUSES:
            rel = entry.get("path", "")
            path = REPO_ROOT / rel
            if not path.is_file():
                errors.append(f"in-method technique {tid} file missing: {rel}")
            elif tid not in records and technique_files:
                # file exists but wasn't parsed in this run
                try:
                    records[tid] = parse_yaml_frontmatter(path.read_text(encoding="utf-8"))
                except AdmitError as exc:
                    errors.append(f"{rel}: {exc}")
            if tid and tid not in method_text:
                errors.append(
                    f"METHOD.md does not mention lineage id {tid} "
                    f"(required for status={status})"
                )

    # Registry must list all non-template technique files when not in empty pr-diff skip
    if technique_files:
        for path in TECHNIQUES_DIR.glob("T-*.md"):
            if path.name == "T-000-template.md":
                continue
            try:
                rec = parse_yaml_frontmatter(path.read_text(encoding="utf-8"))
            except AdmitError:
                continue
            tid = str(rec.get("id", ""))
            if tid and tid not in reg_by_id:
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: id {tid} missing from registry.json"
                )

    if errors:
        for e in errors:
            _err(e)
        print(f"admit: FAILED ({len(errors)} error(s))", file=sys.stderr)
        return 1

    print("admit: OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate lineage admission for this method repo")
    parser.add_argument(
        "--pr-diff",
        type=Path,
        default=None,
        help="Optional file listing paths changed in a PR; if set and no lineage/ "
        "paths appear, technique deep-checks are skipped (still loads registry).",
    )
    args = parser.parse_args(argv)
    try:
        return admit(pr_diff=args.pr_diff)
    except AdmitError as exc:
        _err(str(exc))
        return 1


if __name__ == "__main__":
    sys.exit(main())
