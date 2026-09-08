<!-- SPDX-License-Identifier: MIT -->
# Agents

> If you are an AI agent — Claude, Cursor, Codex, Cline, Continue, Aider, Windsurf, Copilot, or any other — this file is the spine. Read it before generating or restyling any UI in this repository or a fork.
>
> Human door: [`START-HERE.md`](START-HERE.md). Full skill: [`skill/white-baggage-tag-aesthetic/SKILL.md`](skill/white-baggage-tag-aesthetic/SKILL.md).

## The object

A white airline baggage tag is a **closed information package under time pressure**. Not minimalism. Every property it has was forced by a failure mode, and the survivors are the design. Why that matters: [`docs/lineage.md`](docs/lineage.md).

## 1. Pick the register first

The tag aesthetic is **not universal**, and applying it to the wrong reader is the main way this system fails. Ask *who is reading this, and in what physical condition* — an operator at a desk, a citizen in sunlight, a minister in a projected room, someone with a long essay.

Console and Index take it natively. Civic takes it with lower density and larger targets. **Editorial and Institutional do not** — a tag-styled deck reads as a receipt. See [`docs/registers.md`](docs/registers.md).

## 2. PO Completeness — the gate, run first

For every element (type, colour, rule, icon, sentence, image):

1. **Name the domain.** Destination, id, context, subject, stub, attachment, material, priority, crew, hazard.
2. **If removed, does a required job fail?** No → delete it.
3. **Does a stronger element already say it?** Yes → merge, keep the higher rank.
4. **Does size match scan order?** No → resize. Do not add copy to explain it.

**Optional is not a category.** If the domain is not in the package, the element is absent.

## 3. Four ranks. Never a fifth

| Rank | Class | Domain |
|---|---|---|
| Primary | `.tag-dest` | Destination noun — the one thing they must not miss |
| Secondary | `.tag-id` + machine form | Stable id, mono, copyable |
| Tertiary | `.tag-status` | Context: owner, env, time, tracking point |
| Fallback | `.tag-fallback` | Human subject — identifies the object when 1–3 fail |
| Stub | `.tag-stub` | Receipt, permalink, export. Rank 4 at smaller size, not a fifth voice |

Never make the id larger than the destination — that is a domain error, not a taste error. Never make everything 16px.

## 4. Ground and ink. Colour is a domain, never a rank

Default package is `--tag-ground` + `--tag-ink`. Do not invent a palette.

`priority` · `crew` · `hazard` exist **only** when that domain is in the record, and are declared with `data-domain`. A coloured rule "for energy" fails the gate.

## 5. Hard bans

- `border-radius` other than `0` or a true circle that carries meaning
- `box-shadow` except `inset` and `:focus-visible` — printed ink casts none
- Gradients between hues, `backdrop-filter`, glassmorphism, dark-glass inversion of the tag
- Inter, Roboto, Poppins, Montserrat, Open Sans, Lato, Geist, Space Grotesk
- Emoji, sparkle pills, "Welcome back", slogans, motivational copy
- A fifth type rank invented as "caption personality"
- Hover or colour alone carrying meaning

## 6. Declare intent in markup

```html
<!-- size: primary · domain: IATA three-letter destination -->
<h1 class="tag-dest">BKK</h1>
```

A block that deliberately fails the gate — a Before panel in a demo — declares it: `data-po="fail"`, or the `.tag-noise` class. Both are exempted by the auditor.

## 7. Every edge resolves to another edge

A printed tag gets alignment for free; a digital one does not. One edge landing eleven pixels short of its neighbour reads as *accident*, the one thing the object never reads as. Line weight carries role — uniform 1px everywhere says nobody decided which line mattered. See [`docs/grid.md`](docs/grid.md).

## 8. Run the gate before you ship

```bash
node tools/tag-audit.mjs .           # or: npx tag-audit .
node tools/tag-audit.mjs . --strict  # CI — exit 1 on errors
```

It decides what a machine can decide: radius, shadow, gradient, banned typeface, inverted hierarchy, colour with no domain, emoji, slogans. **Meaning, non-redundancy, and whether an element earns its place remain human questions** — [`docs/critique-checklist.md`](docs/critique-checklist.md).

## 9. Breaking a rule legitimately

A rule may be broken when **all three** hold — two of three is drift:

1. **Named** — written as an explicit override, not inherited from a template default.
2. **Load-bearing** — it carries information the compliant version cannot.
3. **Written down** — one line in the project's `context.md` stating what broke and what it buys.

**PO Completeness has no exception path.**

## 10. Ethics

Fork the method, not secrets. Example LPN `0217123456` is synthetic. No live passenger data, real bag numbers, or credentials in git. No black-box rankings of cities, carriers, or people. Not an IATA or airline product.
