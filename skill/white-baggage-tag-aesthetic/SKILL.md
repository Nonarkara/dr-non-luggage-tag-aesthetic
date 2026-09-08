---
name: white-baggage-tag-aesthetic
description: >-
  Analyze, generate, critique, and apply the functional-minimalist aesthetic of
  the white / plain thermal airline baggage tag (plus RFID, electronic, and
  sustainability extensions) to any closed information package: website, dashboard,
  docs, log line, packaging, or system output. Use when the user wants luggage-tag
  UI, PO Completeness, thermal black-on-white hierarchy, IATA-like destination
  dominance, or to strip decorative noise from an interface.
version: "2.2"
license: MIT
---

# White baggage tag aesthetic v2.0

You are applying **Dr Non’s Luggage Tag Aesthetic**: a closed package in which every element carries explicit, non-redundant meaning. This is not decorative minimalism.

Repo: https://github.com/Nonarkara/dr-non-luggage-tag-aesthetic  
Load tokens from `design-tokens/tokens.css`. Mirror components in `components/`. Run the checklist in `docs/critique-checklist.md`.

## Pick the stock first

**Stock A — thermal** (default). White face, ground and ink, machine-first: a barcode does the sorting and the human type is the fallback. Everything else in this skill assumes Stock A.

**Stock B — printed**. Two or three spot inks on coloured stock. **There is no barcode**, so colour, scale, and composition carry the sorting job a scanner does on Stock A. A full-face carrier colour, a destination at 10× the serial, a striped livery band, a struck serial slightly off-register, type running vertically up the side — all of it is load-bearing, none of it is decoration.

Declare it: `data-stock="printed"` plus a `data-domain`. Tokens in `design-tokens/stock-printed.css`, surfaces in `components/stock-printed.css`, gallery at `components/printed.html`.

Stock B has **harder** limits, not fewer — the constraint is what produces the look:

1. Three inks maximum, and the stock colour is one of them.
2. Flat colour only. A press cannot blend. A two-domain split uses hard stops that meet at one position (`A 0 46%, B 46% 100%`) — that is a press mark, not a gradient.
3. Every ink names a domain: carrier, route family, class, station, priority.
4. The overprint is the only texture. Small misregistration is evidence of process; large is a costume.
5. Rotation is a second reading axis — the job the 90°-offset barcode does. Rotation that only decorates fails.
6. Still four ranks. The ratio widens; no fifth voice appears.
7. Contrast holds on the actual stock: ≥4.5:1 body, ≥3:1 large. Dark ink only on yellow.

Use Stock B for identity, wayfinding, packaging, covers, posters, editorial openers, physical collateral. Use Stock A for dashboards, log lines, admin tables, anything with a machine in the loop. Full doctrine: `docs/stocks.md`.

## PO Completeness (gate — run first)

For every element (type, colour, rule, icon, sentence, image):

1. **Name the domain** (destination, LPN/id, carrier/flight/date, passenger/subject, stub/receipt, attachment, material, RFID, reuse, priority, crew, hazard).
2. **If removed, does a required job fail?** If no → delete.
3. **Does a stronger element already say it?** If yes → merge; keep the stronger rank.
4. **Does size match scan order?** If no → resize, do not explain with extra copy.

Optional is not a category. If the domain is not in the package, the element is absent.

Fail: slogans, filler, motivational copy, emoji, unused badges, “eco” leaves, hero photography, dark-glass inversion of the tag, rainbow accents, decorative manga chrome.

Pass: destination dominant, LPN mono + machine form, context strip, human fallback, stub/receipt, loop/border as attachment.

## Size and domain (declare in markup)

Comment every block:

```html
<!-- size: primary · domain: IATA three-letter destination -->
<h1 class="tag-dest">BKK</h1>
```

| Rank | CSS | Domain |
|---|---|---|
| Primary | `.tag-dest` | IATA code or destination-equivalent noun |
| Secondary | `.tag-id` + barcode | 10-digit LPN / stable object id |
| Tertiary | `.tag-status` | Carrier, flight, date, env, tracking point |
| Fallback | `.tag-fallback` | Passenger name / human subject |
| Stub | `.tag-stub` | Claim, permalink, export, audit copy |

Default colours: `--tag-ground` `#f7f6f2`, `--tag-ink` `#111111`.  
Domain colours (`priority`, `crew`, `hazard`) **only** when that domain is in the record. Document with `data-domain`.

## Human hierarchy

Time pressure first, then machine, then durability, then lifecycle:

1. Destination (arm’s length)
2. LPN / id (copyable, dual-encoded)
3. Context (act without another pane)
4. Name (when 1–3 fail)
5. Stub (object leaves this screen)

Never make the id larger than the destination. Never make everything 16 px.

## Dual encoding

Human-readable **and** machine form: Code 128 (or JSON key / copy button), plus a stub. Physical tags print the barcode twice at 90° because conveyors are 3D (Vanhoenacker 2012). Digital analogue: a second column, an export, a permalink.

## Material / lifecycle

Name the substrate if it matters: thermal, synthetic, PP/PE laminate, freezer-grade adhesive, RFID inlay, EBT/reusable. Durability is information. Sustainability is reuse/recycle/residue — not ornament.

Evolutionary rule: RFID (IATA RP1740c, EPC Gen2 / ISO 18000-6C) and EBT (RP1754) **add** a domain. Do not delete printed LPN or human type until every reader in the journey uses the new layer.

## Anatomy (physical reference)

- Face stock width ~50.8–54 mm (Resolution 740).
- Destination IATA code primary.
- 10-digit LPN: lead + 3-digit issuer + 6-digit serial; Code 128; human digits under bars.
- Airline + flight + date tertiary.
- Passenger name fallback.
- Stubs / claim backup.
- RFID / sustainability only when domain-justified.

Standards notes: `docs/standards-740-753.md`. Do not invent mishandling percentages.

## Application patterns

| Package | Primary | Secondary | Tertiary | Fallback | Stub |
|---|---|---|---|---|---|
| Website card | Status noun / IATA | Object id | Env, time | Subject | Receipt link |
| Dashboard row | Dest column | Mono id | Point + flight | Name | Row export |
| Log / API | First token | `lpn=` / `id=` | `point=` `flt=` `date=` | `pax=` | Repeatable line |
| Doc header | Spec / dest number | Permalink slug | Date, owner | Human title | Download/cite |
| Packaging | SKU dest | Barcode + GTIN | Batch, date | Contents name | Tear-off receipt |

Before/after: `examples/`. Live preview: `examples/gallery/index.html`.

## Run the gate

```bash
node tools/tag-audit.mjs .           # or npx tag-audit .
node tools/tag-audit.mjs . --strict  # CI
```

It decides what a machine can: radius, shadow, blended gradients, banned typefaces, inverted hierarchy (an id larger than its destination), colour with no domain, ink count per printed face, field/ink contrast below 3:1, emoji, slogans. A block that deliberately fails — a Before panel — declares `data-po="fail"` or uses `.tag-noise`.

Meaning and non-redundancy stay human questions.

## Critique checklist (all must pass)

(a) PO completeness  
(b) no noise  
(c) human hierarchy  
(d) dual encoding  
(e) size–domain coherence  
(f) material/lifecycle  
(g) evolutionary readiness  

Fail any → remove, merge, or resize. Do not add copy to justify decoration.

## Ethics

Fork the **method**, not secrets or live passenger data. Example LPN `0217123456` is synthetic. This is not an IATA or airline product. No black-box rankings. Bilingual TH–EN labels are for extra readers, not extra chrome.

## Output contract

When generating UI or copy:

1. Use ground/ink and the four ranks.
2. Include markup comments for size + domain.
3. Show a closed package (card, row, or log line), not a mood board.
4. If asked for both a noisy version and a tag version, label Before (fails PO) and After (PO complete).
