<!-- SPDX-License-Identifier: MIT -->
# START HERE

You cloned **Dr Non’s Luggage Tag Aesthetic Design System**. This file is the door. The [README](README.md) is the wall you show the street.

## What this is

A forkable method: treat the **white thermal airline baggage tag** as the law of a closed information package. Every element must carry explicit, non-redundant meaning. Size and domain are information. Human scan under time pressure comes first.

It is **not** an IATA manual, not an airline product, not a passenger database, not a ranking.

## 15-minute human path

1. Look at the hero: [`assets/hero-tag.svg`](assets/hero-tag.svg) — destination dominant, LPN/barcode second, stubs as backup.
2. Open [`examples/gallery/index.html`](examples/gallery/index.html) in a browser. No build.
3. Pick a register — this aesthetic is not universal: [`docs/registers.md`](docs/registers.md).
4. Read the gate: [`docs/critique-checklist.md`](docs/critique-checklist.md), and run its machine half: `node tools/tag-audit.mjs .`
5. Copy [`design-tokens/tokens.css`](design-tokens/tokens.css) + [`components/tag-system.css`](components/tag-system.css) into your surface.
6. Rebuild one object (a card, a row, a header, a log line) until it is a tag.

## Agent path

1. Read [`skill/white-baggage-tag-aesthetic/SKILL.md`](skill/white-baggage-tag-aesthetic/SKILL.md).
2. Do not invent a palette. Ground + ink. Four ranks.
3. Declare `size` and `domain` in markup comments.
4. Fail the PO gate → remove, merge, or resize. Do not write a slogan to cover a hole.

## Map

| Path | Job |
|---|---|
| [`docs/philosophy.md`](docs/philosophy.md) | Why the tag is the law |
| [`docs/lineage.md`](docs/lineage.md) | Why this is good design — Rams, Vignelli, and what the tag adds |
| [`docs/registers.md`](docs/registers.md) | **When this aesthetic is wrong.** Read before any CSS |
| [`docs/grid.md`](docs/grid.md) | Every edge resolves to another edge |
| [`tools/tag-audit.mjs`](tools/tag-audit.mjs) | The gate, runnable. `--strict` in CI |
| [`docs/anatomy.md`](docs/anatomy.md) | Eight zones |
| [`docs/hierarchy.md`](docs/hierarchy.md) | Scan order + UI mapping |
| [`docs/standards-740-753.md`](docs/standards-740-753.md) | What we actually cite |
| [`docs/evolution.md`](docs/evolution.md) | Thermal → RFID → reusable |
| [`docs/sources.md`](docs/sources.md) | Sources; no invented stats |
| [`docs/how-to.md`](docs/how-to.md) | Apply |
| [`components/`](components/) | TagCard, StatusStrip, IdBlock, DestinationHero, StubBackup, DashboardRow |
| [`examples/`](examples/) | Three before/after applications |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | PRs must pass PO |
| [`SECURITY.md`](SECURITY.md) | No secrets in this repo |

## Ethics (Nonarkara)

- **Fork the method, not the secrets.** Example LPN `0217123456` is synthetic. Do not commit live passenger names, real bag numbers, API keys, or airline credentials.
- **No black-box rankings.** This is a hierarchy of *scan jobs*, not a score of cities, airlines, or people.
- **Not official.** Independent studio work by [Dr Non Arkaraprasertkul](https://github.com/Nonarkara). Not IATA, not a carrier, not depa.
- **Bilingual welcome.** TH–EN on city lines and claim stubs when it adds a reader. Do not duplicate `BKK` as ornament.

## Recommended GitHub topics

`design-system` `design-tokens` `iata` `baggage-tag` `functional-minimalism` `css` `html` `documentation` `accessibility`

(Topics on github.com may already be set; this list is for forks.)
