<!-- SPDX-License-Identifier: MIT -->
# Stocks — the same law, two printing technologies

> [`registers.md`](registers.md) asks *who is reading, and in what condition.* This file asks a different question: **what press made this object, and what could that press do?**
>
> A register picks the reader. A stock picks the vocabulary.

The repo began from one tag — the white thermal automated bag tag. That object is correct, and it is not the whole tradition. The printed tags people actually collect and pin are loud: a full-bleed orange ground, `LON` at the height of a fist, a serial struck in red across the corner, a striped carrier band, a city name set vertically up the side.

The easy reading is that those are decorative and the thermal tag is disciplined. **That reading is wrong**, and getting it right is what makes this a system rather than a preference.

---

## Why the printed tag is colourful

A thermal tag has a barcode. The barcode does the sorting; the human type is the backup layer for when the machine fails.

**A printed tag has no barcode.** There is no machine in the loop at all. And the sorting job does not go away because the technology is absent — a handler in 1968 still had to move a bag to the right cart in a few seconds, in a shed, at night.

So the job moved into the only channels available:

| Job | Thermal stock | Printed stock |
|---|---|---|
| Identify the carrier | Text field | **The colour of the whole face** |
| Sort into a pile fast | Barcode → machine | **Colour + a city name at extreme scale** |
| Encode route family | Message data | **A striped band, or a two-tone split** |
| Encode class or priority | `data-domain` stripe | **A second ink, or an overprint** |
| Prove the object was processed | Scan record | **The overprinted serial, misregistered** |

Every colour on a vintage tag is doing the work a barcode does now. **It is the same PO Completeness, solved with pigment because there was no scanner.**

That is why those tags look good, and why imitations of them look bad. The imitation copies the palette. The original was carrying routing information in that palette.

---

## The two stocks

### Stock A — Thermal *(the default)*

Direct thermal on white or near-white synthetic face. One head, one ink, no colour. Machine-first: the barcode is the key and the human layer is the fallback.

Ground and ink. Four ranks. Colour only when `priority`, `crew`, or `hazard` is genuinely in the record. Everything in [`philosophy.md`](philosophy.md) and [`hierarchy.md`](hierarchy.md) describes this stock.

Use it when there is a machine in the loop, a dense operational surface, or live data.

### Stock B — Printed

Letterpress or flexo, two or three spot inks on coloured or kraft stock. Human-first: no machine reads this, so the face itself must sort.

Colour is a **domain field**, scale range is wider, and composition carries information the thermal stock puts in text.

Use it for identity, wayfinding, packaging, covers, posters, editorial openers, event and physical collateral — anywhere a human sorts by eye and no scanner is involved.

---

## Stock B has harder limits, not fewer

This is the part that keeps "playful" from becoming slop.

A vintage tag looks good **because of what the press could not do.** Two or three inks, flat, on a fixed stock. That constraint produced every quality worth copying. Remove the constraint and you get a gradient mess that references the aesthetic without earning it.

So Stock B carries its own hard limits, and they are stricter in some ways than Stock A:

1. **Three inks maximum, and the stock colour is one of them.** A cream stock plus black plus one red is a complete tag. A fourth ink is a press change nobody paid for.
2. **Flat colour only. No gradients, ever.** A press lays down solid ink. This is not a style rule; it is what the technology does. Gradient is the single fastest way to make this look like a filter instead of a print.
3. **Every ink names a domain.** Carrier, route family, class, station, priority. Write it in `data-domain`. An ink chosen "because orange feels warm" fails the gate exactly as it does in Stock A.
4. **The overprint is the only permitted texture.** A serial or a station mark struck in a second ink, allowed to sit slightly off-register. That misregistration is *evidence of process* — the record of a real machine hitting a real object. It is wabi-sabi, not a distress filter. **Never fake more wear than the process would produce.**
5. **Rotation is a second reading axis, not a flourish.** Vertical type is permitted where it does the job the second barcode does on a thermal tag: give a reader approaching from another angle a way in. Rotated type that only decorates fails.
6. **Still four ranks.** The *ratio* between them widens — a destination may run 10× the serial instead of 4× — but no fifth voice appears. Extreme scale is not a new rank; it is the same rank, louder, because there is no machine to fall back on.
7. **Contrast still holds.** ≥ 4.5:1 body, ≥ 3:1 large, on the actual stock colour. A yellow stock takes a dark ink; white type on yellow is the one combination the NYCTA system also bans outright.

---

## What carries over unchanged

PO Completeness · the four ranks · `border-radius: 0` except a true circle · no shadow, no blur, no glassmorphism · dual encoding · a fallback rank · every number carrying source, tier and age · every edge resolving to another edge.

**Stock B changes the palette and the scale range. It does not change the law.**

---

## Choosing

| Situation | Stock |
|---|---|
| A machine reads it; live data; dense operations | **A — Thermal** |
| A person sorts it by eye; no scanner in the loop | **B — Printed** |
| Identity, packaging, cover, poster, physical collateral | **B — Printed** |
| A dashboard, a log line, an admin table | **A — Thermal** |
| An editorial opener or section divider inside a thermal surface | **B**, scoped to that block, declared |

The two mix, but never inside one object. A page may open with a printed-stock hero and continue in thermal — a physical tag with a printed face and a thermal-printed strip is exactly that object. What fails is a single card with half a colour field and half a white ground and no reason for either.

Declare the stock in markup: `data-stock="printed"`. The auditor reads it, and enforces the ink limit rather than relaxing the rules.

---

## The one-line version

> The white tag is what the job looks like when a machine does the sorting.
> The printed tag is what the same job looks like when a person does.
>
> Neither is decoration. One has a scanner and the other has ink.
