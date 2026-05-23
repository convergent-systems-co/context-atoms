# context-atoms

> Context primitives for AI runtimes — situational frames, environment descriptors, conversation scopes, working-memory shapes, attention budgets.

`context-atoms` is a `*-Atoms` catalog in the [Convergent Systems](https://convergent-systems.co) ecosystem. It defines what exists in its domain — typed, versioned, machine-readable, composable, and open — so runtimes (and humans) can stand on shared infrastructure instead of reinventing it.

This catalog composes with [`agent-atoms`](https://github.com/convergent-systems-co/agent-atoms) and [`prompt-atoms`](https://github.com/convergent-systems-co/prompt-atoms) so an agent's situational context can be expressed as typed, versioned, signed atoms rather than free-text prose dumped into a system prompt.

## Structure

```
context-atoms/
├── ATOMS.yml              # Catalog manifest (atoms-spec/v1.1.0)
├── atoms/                 # Reusable building blocks
├── contexts/              # Compositions assembled from atoms
├── rules/                 # Typed constraint vocabulary
├── schemas/               # Catalog-specific JSON Schemas
├── governance/            # Catalog governance documents
├── keys/                  # Catalog signing key metadata
├── exports/               # CI-generated machine-readable exports
└── docs/                  # Human-readable documentation
```

### Atom types

- `situational-frame`
- `environment-descriptor`
- `conversation-scope`
- `working-memory-shape`
- `attention-budget`

### Runtime consumers

`aish`, `olympus`

## Status

Lifecycle: `bootstrap`. The catalog is scaffolded; atom publication has not begun. See [`ATOMS.yml`](./ATOMS.yml) `lifecycle.current` for the authoritative state.

## How to consume

Machine-readable exports are published in [`exports/`](./exports/) on every release:

- `exports/manifest.json` — lightweight discovery (name, version, counts)
- `exports/catalog.json` — full catalog dump (every atom, composition, rule)

Exports are deterministic, signed, and versioned. See [`ATOMS.yml`](./ATOMS.yml) for the manifest and the conformance spec.

## How to contribute

1. Read [`ATOMS.yml`](./ATOMS.yml) to understand the catalog's atom types, compositions, and rules.
2. Add a new atom under `atoms/<type>/` or a composition under `contexts/<name>/`.
3. Open a PR. CI validates the schema, references, and exports.
4. Larger structural changes go through the [XAIP process](https://github.com/convergent-systems-co/xaips).

## Ecosystem

- **Federation:** [convergent-systems.co](https://convergent-systems.co) · [github.com/convergent-systems-co](https://github.com/convergent-systems-co)
- **Spec:** [github.com/convergent-systems-co/atoms-spec](https://github.com/convergent-systems-co/atoms-spec) (conforms to `atoms-spec/v1.1.0`)
- **Tools:** [github.com/convergent-systems-co/atoms-tools](https://github.com/convergent-systems-co/atoms-tools)
- **Umbrella:** [github.com/convergent-systems-co/atoms](https://github.com/convergent-systems-co/atoms) — all catalogs as submodules
- **Companion catalogs:** [agent-atoms](https://github.com/convergent-systems-co/agent-atoms), [prompt-atoms](https://github.com/convergent-systems-co/prompt-atoms)

## License

Dual-licensed under the v1.1.0 dual-license model:

- **Code** (CI, scripts, schemas, web): [Apache-2.0](./LICENSE)
- **Data** (atoms, compositions, rules): [CC-BY-4.0](./LICENSE-data)
