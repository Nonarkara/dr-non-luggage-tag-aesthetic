<!-- SPDX-License-Identifier: MIT -->
# Agents

> If you are an AI agent — Claude, Cursor, Codex, Cline, Continue, Aider, Windsurf, Copilot, or any other — this file is the spine. Read it before generating or restyling any UI in this repository or a fork.
>
> Human door: [`START-HERE.md`](START-HERE.md). Full skill: [`skill/white-baggage-tag-aesthetic/SKILL.md`](skill/white-baggage-tag-aesthetic/SKILL.md).

> **Read [`BUILDER.md`](BUILDER.md) first.** That file is the method — how the work gets
> made. This file is the law — what a correct surface looks like. Obeying the law without
> the method produces compliant work that is still the wrong thing.

## The object

A white airline baggage tag is a **closed information package under time pressure**. Every property it has was forced by a failure mode, and the survivors are the design. Why that matters: [`docs/lineage.md`](docs/lineage.md).

**It is not minimalism, and it is not austerity.** A 1968 tag is maximally disciplined and maximally characterful at once, because the character carries information. The roof:

1. It works for both machines and humans.
2. Information hierarchy and condensation — the important thing first.
3. MoMA rules — strict, therefore communicative and structurally beautiful.
4. **Under that roof there is room for colour, composition, and character.**

Rule 4 is the one most often dropped, which produces acres of white space, one enormous thin word, and no information.

## 1. Pick the register first

The tag aesthetic is **not universal**, and applying it to the wrong reader is the main way this system fails. Ask *who is reading this, and in what physical condition* — an operator at a desk, a citizen in sunlight, a minister in a projected room, someone with a long essay.

Console and Index take it natively. Civic takes it with lower density and larger targets. **Editorial and Institutional do not** — a tag-styled deck reads as a receipt. See [`docs/registers.md`](docs/registers.md).

## 1b. Then pick a stock

**Stock A — thermal** (default): white face, ground and ink, machine-first. A barcode does the sorting; the human layer is the fallback. Everything below assumes this stock.

**Stock B — printed**: two or three spot inks on coloured stock. **There is no barcode**, so colour, scale, and composition carry the sorting job a scanner does on Stock A. Declare `data-stock="printed"` and a `data-domain`.

Stock B has *harder* limits, not fewer: three inks maximum counting the stock · flat colour only, a press cannot blend · every ink names a domain · the overprint is the only texture · rotation is a second reading axis, not a flourish · still four ranks, only a wider ratio. See [`docs/stocks.md`](docs/stocks.md).

## 1c. Then decide how much skin

Roughly **65% system, 35% ephemera** — stamps, handwriting, rotation, colour fields, irregular silhouettes.

**A mark may appear only when the event it records actually happened.** A stamp means a station handled it. Handwriting means a human overrode the machine. A tear means a stub was claimed. Declare it: `data-event="stamped"`, `"annotated"`, `"claimed"`, `"handled"`.

A mark with no event is manufactured wear, which is the opposite of what wear is for. The auditor rejects it. **Never rotate a primary block** — rotation is for stubs and secondary fragments; the thing you must read first is the thing that sits straight. See [`docs/ephemera.md`](docs/ephemera.md).

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
- Gradients that *blend*. A two-domain split uses hard stops that meet at one position (`A 0 46%, B 46% 100%`) — that is a press mark, not a gradient. `backdrop-filter`, glassmorphism, and dark-glass inversion stay banned outright
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

The page around the tag obeys the [MoMA layout laws](https://github.com/Nonarkara/moma-rules) in full: one origin, a closed spacing scale of `0 4 8 12 16 20 24 32 40 48 64 80 96 120 160`, no orphan grid cells, and **no border between 2px and 4px** — 1 and 2 are lines, 4 and up are colour bands, and in between is a second design language.

The face and the ephemera skin sit **outside** those laws on purpose. A 50.8mm face has its own closed sub-scale; a stamp rotated six degrees is not on any grid and should not be. The exemption is granted by token name, not by claim — [`docs/moma.md`](docs/moma.md) says exactly where the boundary falls and why.

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
