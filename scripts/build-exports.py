#!/usr/bin/env python3
"""Build exports/catalog.json from validated atoms, compositions, and rules.

Walks atoms/, contexts/, rules/; validates each against its schema; assembles
a single machine-readable catalog manifest. Exits 1 on validation failure.
TOML atoms and compositions are loaded natively alongside JSON.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("error: jsonschema not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # fallback: pip install tomli
    except ImportError:
        tomllib = None  # TOML loading disabled; only JSON atoms will be collected

REPO = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO / "schemas"
ATOMS_DIR = REPO / "atoms"
COMPOSITIONS_DIR = REPO / "contexts"
RULES_DIR = REPO / "rules"
EXPORT_PATH = REPO / "exports" / "catalog.json"
CATALOG_NAME = "context-atoms"
CATALOG_VERSION = "0.1.0"


def load_validator(name: str) -> jsonschema.Draft202012Validator:
    schema = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
    return jsonschema.Draft202012Validator(schema)


def _load_file(path: Path):
    """Load a JSON or TOML file into a dict. Returns None on skip."""
    if path.suffix == ".toml":
        if tomllib is None:
            print(
                f"warning: skipping {path.name} — tomllib/tomli not available; "
                "install Python 3.11+ or run: pip install tomli",
                file=sys.stderr,
            )
            return None
        with path.open("rb") as fh:
            return tomllib.load(fh)
    return json.loads(path.read_text(encoding="utf-8"))


def collect(dir_path: Path, validator, label: str, validate_toml: bool = False) -> list[dict]:
    """Collect atoms/compositions from dir_path.

    JSON files are always validated against validator.
    TOML files are collected as-is unless validate_toml is True (TOML follows
    its own grammar defined in schema-atoms, not the JSON schema here).
    """
    if not dir_path.exists():
        return []
    out: list[dict] = []
    seen: set[Path] = set()
    for pattern in ["*.json", "*.toml"]:
        for path in sorted(dir_path.rglob(pattern)):
            if path in seen or path.name.startswith("."):
                continue
            seen.add(path)
            data = _load_file(path)
            if data is None:
                continue
            if path.suffix == ".json" or validate_toml:
                errors = list(validator.iter_errors(data))
                if errors:
                    print(f"✗ {path.relative_to(REPO)} ({label}):", file=sys.stderr)
                    for err in errors:
                        loc = "/".join(str(x) for x in err.absolute_path) or "<root>"
                        print(f"    {err.message} at {loc}", file=sys.stderr)
                    sys.exit(1)
            out.append(data)
    return out


def main() -> int:
    atoms = collect(ATOMS_DIR, load_validator("atom-v1.json"), "atom")
    compositions = collect(COMPOSITIONS_DIR, load_validator("composition-v1.json"), "composition")
    rules = collect(RULES_DIR, load_validator("rule-v1.json"), "rule")

    catalog = {
        "catalog": CATALOG_NAME,
        "version": CATALOG_VERSION,
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "atoms": atoms,
        "compositions": compositions,
        "rules": rules,
    }

    EXPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {EXPORT_PATH.relative_to(REPO)} — {len(atoms)} atoms, {len(compositions)} compositions, {len(rules)} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
