# context-atoms — Goals

> Context primitives for AI runtimes — situational frames, environment descriptors, conversation scopes, working-memory shapes, attention budgets.

*This document is derived from the `*-Atoms` ecosystem pattern (see `convergent-systems-co/xdao`). Sections marked **Generated** are pattern-based starting points for revision, not decided plan.*

---

## What this catalog makes civilization-grade

Agent runtimes assemble context the same way every time, but the assembly happens inside opaque code: a system prompt, a few injected facts, a working-memory dictionary, a token budget hardcoded somewhere. There is no shared vocabulary for "this is the situational frame the agent is operating inside" or "this is the conversation scope" or "this is the working-memory shape." Each runtime reinvents context.

By cataloging context primitives, `context-atoms` turns this domain from opaque-and-ephemeral to typed, versioned, composable, machine-readable, and open — the civilization-grade properties the ecosystem requires. An agent's situational context becomes a referenceable artifact instead of a free-text dump.

## What it catalogs

### Atom types

- **`situational-frame`** — The frame the agent is operating inside: task domain, user role, deployment mode (interactive / batch / autonomous), risk posture.
- **`environment-descriptor`** — Surrounding environment: OS / runtime, available tools, network reachability, time zone, locale, organizational tenancy.
- **`conversation-scope`** — Bounds of the current exchange: topic, allowed digressions, prior-turn references, multi-turn continuity rules.
- **`working-memory-shape`** — Typed shape of the working-memory the agent carries between turns: keys, value types, eviction policy, persistence boundary.
- **`attention-budget`** — Token / time / cost budget for context assembly: max tokens, priority ordering for truncation, retention bias.

### Compositions: `contexts`

A `context` composition assembles a situational-frame + environment-descriptor + conversation-scope + working-memory-shape + attention-budget into a complete, runtime-ready context definition. Composes with [`agent-atoms`](https://github.com/convergent-systems-co/agent-atoms) personas and [`prompt-atoms`](https://github.com/convergent-systems-co/prompt-atoms) prompts.

### Rule types

To be defined in v0.1. Likely candidates: `scope-constraint` (which atoms must / must not appear together), `budget-rule` (how attention budgets interact with working-memory persistence), `frame-compatibility` (which situational frames are compatible with which environment descriptors).

## Runtime consumers

- **aish** — Shell-grade AI integration; context-atoms supplies the situational frame and environment descriptor for every shell invocation.
- **olympus** — Pantheon Modules consume context atoms to declare per-module situational context as typed, signed artifacts.

## Status & priority

**Current status:** `bootstrap` (per `ATOMS.yml` `lifecycle.current`)

**Priority tier:** Tier 2 — companion catalog to `agent-atoms` and `prompt-atoms`.

**Trigger / activation condition:** Adopted once the first runtime consumer (aish or olympus) issues a pull request against the catalog for a real composition.

## Roadmap *(Generated — milestone shapes pending real-runtime pull)*

### v0.1 — Bootstrap & schema definition

**Goal:** Type-specific schemas published for all five atom types. First composition published.

**Success criterion:** aish or olympus consumes at least one `context` composition from this catalog in a non-trivial code path.

**Kill criterion:** No runtime consumer pulls in 90 days from bootstrap; downgrade to `historic`.

**Work:**

- [ ] Define type-specific JSON Schema subschemas for the five atom types
- [ ] Publish first reference atom per type (signed, with `lifecycle: published`)
- [ ] Publish first `context` composition
- [ ] Wire export pipeline (`exports/manifest.json`, `exports/catalog.json`)

### v0.2 — Adoption

**Goal:** Second runtime consumer; first multi-atom composition pattern documented.

### v1.0 — Operational

**Goal:** Canonical context vocabulary across the federated `*-atoms` ecosystem.

## Civilization-grade property checklist

Every catalog must satisfy these before v1.0. Failing any blocks a release.

| Property | Mechanism in this catalog |
|---|---|
| Typed | JSON Schema in `schemas/` validates every atom, composition, rule |
| Versioned | Every atom has a semver `version` field; compositions reference atoms by version-pinned ID |
| Signed | v1.1.0 `signing` block enforced in CI; ML-DSA quorum rules per atom path |
| Machine-readable | `exports/catalog.json` published on every release |
| Composable | Compositions reference atoms by ID; CI verifies references resolve |
| Open (code) | Apache-2.0 — see `LICENSE` |
| Open (data) | CC-BY-4.0 — see `LICENSE-data` |
| Durable | No external dependencies for primary content |

## Related

- **Spec:** [atoms-spec](https://github.com/convergent-systems-co/atoms-spec) — conforms to `atoms-spec/v1.1.0`
- **Tools:** [atoms-tools](https://github.com/convergent-systems-co/atoms-tools) — CLI for validate / export / resolve
- **Federation:** [convergent-systems.co](https://convergent-systems.co)
- **Umbrella:** [atoms](https://github.com/convergent-systems-co/atoms) — every catalog as a git submodule
- **Companion catalogs:** [agent-atoms](https://github.com/convergent-systems-co/agent-atoms), [prompt-atoms](https://github.com/convergent-systems-co/prompt-atoms)
- **Manifest:** [`ATOMS.yml`](./ATOMS.yml)
