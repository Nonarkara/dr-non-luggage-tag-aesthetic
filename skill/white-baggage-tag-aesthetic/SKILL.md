---
name: white-baggage-tag-aesthetic
description: >-
  Analyze, generate, critique, and apply the functional-minimalist aesthetic of
  the white / plain thermal airline baggage tag (plus RFID, electronic, and
  sustainability extensions) to any closed information package: website, dashboard,
  docs, log line, packaging, or system output. Use when the user wants luggage-tag
  UI, PO Completeness, thermal black-on-white hierarchy, IATA-like destination
  dominance, or to strip decorative noise from an interface.
version: "3.0"
license: MIT
---

# White baggage tag aesthetic v2.0

You are applying **Dr Non’s Luggage Tag Aesthetic**: a closed package in which every element carries explicit, non-redundant meaning. This is not decorative minimalism.

Repo: https://github.com/Nonarkara/dr-non-luggage-tag-aesthetic  
Load tokens from `design-tokens/tokens.css`. Mirror components in `components/`. Run the checklist in `docs/critique-checklist.md`.

## PO Completeness (gate — run first)

For every element (type, colour, rule, icon, sentence, image):

1. **Name the domain** (destination, LPN/id, carrier/flight/date, passenger/subject, stub/receipt, attachment, material, RFID, reuse, priority, crew, hazard).
2. **If removed, does a required job fail?** If no → delete.
3. **Does a stronger element already say it?** If yes → merge; keep the stronger rank.
4. **Does size match scan order?** If no → resize, do not explain with extra copy.

Optional is not a category. If the domain is not in the package, the element is absent.

Fail: slogans, filler, motivational copy, emoji, unused badges, “eco” leaves, hero photography, dark-glass inversion of the tag, rainbow accents, decorative manga chrome.

Pass: destination dominant, LPN mono + machine form, context strip, human fallback, stub/receipt, loop/border as attachment.

## Density gate (run immediately after PO)

PO tells you what may stay. Density tells you how it must be set.

1. **Ink.** Does the package carry solid fill — a band, a filled box, a barcode block? Hairlines and type alone fail.
2. **Reversal before size.** Anything that must outrank its neighbours gets knocked out of a solid band *before* it is scaled up. Reversal is free; size costs measure.
3. **Tag scale inside, page scale outside.** Inside the object use `--tag-gutter` / `--tag-gap-zone` (~2 mm equivalent). `--tag-space-5`+ is for the document *around* it. Using page scale inside is what makes tags float.
4. **Rail.** If a routing state exists in the record, it is a full-bleed colour band — never a tint, never a 1-px accent. One rail per package.
5. **Real barcodes.** Use `components/barcode.js`. The interline licence plate symbology is **Interleaved 2 of 5** (IATA R740, via the EBT guide) — *not* Code 128, a common error. I2of5 interleaves digit pairs into bars and spaces, which is why it needs an even digit count and why the LPN is 10 digits. Code 128 is the fallback for alphanumeric payloads only. Never a CSS gradient — a decorative barcode concedes the marks are ornamental, which is the opposite of the claim.

## Redundancy rule (supersedes "non-redundant" in v2)

Repeat the identifier when the medium is **lossy** and the read is **safety-critical** — a torn strip, a truncated log line, a screenshotted receipt, a number read aloud over a phone. A real tag prints the licence plate five or six times for exactly this reason, and the repetition supplies the strip's rhythm.

Duplicating something because the layout felt bare still fails.

## Colour (supersedes "colour is not a rank")

Colour is not a *type rank* and never replaces size in the scan order. It is a **domain channel with the longest range on the object** — a rail resolves across a hall when the destination code is still a smudge.

Rails in `design-tokens/tokens.css`: `standard` (green), `priority` (red-orange), `business` (blue), `transfer` (amber), `hazard` (dark red), `heavy` (violet). Set with `data-rail="…"`.

⚠️ **Say that this key is ours.** On real tags only one coloured rail is standardised — a **green edge for hold baggage checked in at an EU airport**, a customs marking, not a priority one. Priority/class colours are per-carrier; IATA recommends short connections be flagged by a remark or a *separate* sticker rather than a rail. Use the vocabulary, label it as a design invention, never as an aviation standard.

Play lives in **combination, not decoration**: rail colour, reversal density, repeat count and rhythm, rotation axis, barcode module width, format. Not in illustration, gradients, glows, or rounded corners.

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

Human-readable **and** machine form: Interleaved 2 of 5 for a numeric licence plate (or JSON key / copy button), plus a stub. Physical tags print the barcode twice at 90° because conveyors are 3D (Vanhoenacker 2012). Digital analogue: a second column, an export, a permalink.

## Material / lifecycle

Name the substrate if it matters: thermal, synthetic, PP/PE laminate, freezer-grade adhesive, RFID inlay, EBT/reusable. Durability is information. Sustainability is reuse/recycle/residue — not ornament.

Evolutionary rule: RFID (IATA RP1740c, EPC Gen2 / ISO 18000-6C) and EBT (RP1754) **add** a domain. Do not delete printed LPN or human type until every reader in the journey uses the new layer.

## Anatomy (physical reference)

- Face width 50.80–54.00 mm (Res 740). **Width is law; length (~53 cm) is convention** — set by loop geometry, not by spec.
- Destination IATA code primary.
- 10-digit LPN: lead digit (0 interline · 1 fallback · 2 RUSH) + 3-digit issuer code (BTIC, Res 769) + 6-digit serial; **Interleaved 2 of 5**; human digits under the bars.
- Routing area lists final destination at the TOP, vias beneath it ordered first-transfer lowest — the list reads bottom-to-top in journey order.
- Minimum type: routing area 4.1 mm, information area 3 mm (Res 740 via RP1754).
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

## Critique checklist (all must pass)

(a) PO completeness  
(b) no noise (decorative duplication fails; failure-model duplication is required)  
(c) human hierarchy  
(d) dual encoding  
(e) size–domain coherence  
(e2) **density and presence** — solid ink, reversal, tag-scale spacing, real barcodes  
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
5. **Ship it dense.** Load `components/tag-strip.css` for band / rail / perf / repeat, and `components/barcode.js` for real symbols. A correct-but-pale result is a failed result — see `docs/why-it-is-beautiful.md` and `examples/d-tag-strip/`.
