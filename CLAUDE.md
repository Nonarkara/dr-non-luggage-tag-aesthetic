<!-- SPDX-License-Identifier: MIT -->
# CLAUDE.md — Claude Code quick-start

> Loaded automatically when you `cd` into this repository, or when this file is symlinked into a project's root or `.claude/`.

> **Read [`BUILDER.md`](BUILDER.md) first.** That file is the method — how the work gets
> made. This file is the law — what a correct surface looks like. Obeying the law without
> the method produces compliant work that is still the wrong thing.

## Read in this order

1. **[`AGENTS.md`](AGENTS.md)** — the spine. Most work is correct after this one file.
2. **[`docs/registers.md`](docs/registers.md)** — before any CSS. The tag aesthetic is not universal; the wrong register is the main failure mode.
3. **[`docs/ephemera.md`](docs/ephemera.md)** — the 65/35 mix, and the rule that keeps the skin out of kitsch.
4. **[`skill/white-baggage-tag-aesthetic/SKILL.md`](skill/white-baggage-tag-aesthetic/SKILL.md)** — the full invocable skill.
5. **[`docs/moma.md`](docs/moma.md)** — the envelope. What obeys the MoMA layout laws, and what is outside them on purpose.
6. **[`docs/lineage.md`](docs/lineage.md)** — why this object is worth copying, and where it goes further than Rams or Vignelli.
7. **[`components/index.html`](components/index.html)** — the live gallery. Reference it; do not invent variants.

## How to apply

- **Before designing anything**, answer: who is reading this, in what physical condition? That picks the register. Nothing else does.
- **Import [`design-tokens/tokens.css`](design-tokens/tokens.css)** and do not redefine the colour, type, or spacing variables.
- **For a dashboard row**: destination column first and largest, mono id second, context third, human fallback last, an action that leaves a copy.
- **For a log line**: first token is the destination, then `lpn=`, then `point=` `flt=` `date=`, then `pax=`.
- **For a doc header**: spec number as destination, permalink slug as id, date and owner as context.

## Non-negotiable

- **Never invent a palette.** Ground and ink. Colour is a domain, never a rank.
- **Never make the id larger than the destination.** That is a domain error.
- **Never round a corner** other than a true circle carrying meaning.
- **Never use** a gradient between hues, a non-inset shadow, blur, or glassmorphism.
- **Never invent a fifth rank.**
- **Never put a border between 2px and 4px.** A line is 1 or 2; a band is 4 or more. In between is a second design language — [`docs/moma.md`](docs/moma.md).
- **Never ship without** `node tools/tag-audit.mjs . --strict` exiting 0.

## The thing most often got wrong

This is not minimalism, and treating it as minimalism produces the characteristic bad imitation: acres of white space, one thin enormous word, and no information.

It is also not austerity. Roughly a third of a good surface here is ephemera — colour fields, stamps, handwriting, rotation — and every bit of it records something that happened.

The tag is *dense*. It is complete. It carries a destination, a machine key, a context strip, a human fallback, a receipt, and a material decision — on a face 50mm wide. Removing information to make it feel calm is the opposite of the method.

When in doubt, ask whether a required job would fail without the element. If yes, it stays, however busy the result looks.
