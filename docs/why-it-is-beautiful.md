<!-- SPDX-License-Identifier: MIT -->
# Why the bag tag is beautiful

This repo existed for a while with a philosophy that argued the tag is *not*
minimalism — and a stylesheet that implemented minimalism anyway. Zero solid
fills, page-scale padding inside the object, colour forbidden on principle, and
a barcode drawn with a CSS gradient. The examples were airy and polite. A real
tag, printed for four cents at a check-in desk, looked better than anything the
system produced.

That gap is the whole lesson, so this document starts from the object rather
than from taste.

---

## The mistake: confusing *restraint* with *emptiness*

Minimalism removes until little is left. A bag tag removes until nothing
*unnecessary* is left — and then packs the remaining space to the edge. Those
are opposite operations that produce superficially similar vocabularies (no
ornament, no colour-for-fun, one typeface) and completely different objects.

The diagnostic is **ink coverage**. A printed bag tag runs somewhere around a
third of its area as solid black: destination bands, barcode blocks, filled
sequence boxes. v2 of this system ran about four percent. Four percent is a
memo. Thirty percent is a tag.

If your output looks calm, you have built a memo.

---

## Six mechanisms that actually do the work

### 1. Density, not whitespace

A tag has no margin to spare because it is 50 mm wide and must carry a
destination, a licence plate, a carrier, a date, a passenger, a routing state
and five redundant stubs. Content runs to roughly 2 mm from a die-cut edge.

This is why the token set now carries **two spacing scales**. Page scale
(`--tag-space-*`) is for the document *around* the object. Tag scale
(`--tag-gutter`, `--tag-gap-zone`) is for *inside* it, and it is roughly an
order of magnitude tighter. v2 used page scale inside the tag; that single
substitution is most of why it floated.

> Compactness is not a style here. It is the consequence of a fixed substrate
> and a non-negotiable payload.

### 2. Reversal — the cheapest hierarchy in print

Knocking type out of a solid band makes it louder without making it bigger.
That matters enormously when width is fixed: you cannot always scale up, but
you can always invert.

*(Stated honestly: no specification I could find requires reversal. This is a
design reading, not a rule — though the engineering rationale is strong, since
direct thermal printing gives you exactly one ink density and no second colour,
which leaves reversal and size as the only hierarchy tools on the object.)*

Reversal also survives failure. A glare-washed, motion-blurred, half-torn strip
still shows *where the black rectangle is*. Shape survives when glyphs do not.

v2 had no reversal at all, so its only hierarchy lever was size — which is why
everything either shouted or whispered with nothing in between.

### 3. Redundancy as structure — where the old doctrine was simply wrong

v2's "PO Completeness" gate said: *every element carries explicit,
non-redundant meaning; if a stronger element already says it, merge.*

A real bag tag violates that rule on purpose. The licence plate is printed
**repeatedly** down the strip — the count varies by carrier and stock, so don't
copy a fixed number. Not as emphasis: as a failure model. The strip gets torn at
an unknown point, soaked, abraded, folded over a handle. Any surviving fragment
must still identify the bag. A 1994 patent (Diemert, Fix GmbH) specifies
identical barcodes at both tag ends *and* on the tear-off control section.

So the rule needed a carve-out, and it is a principled one:

> Redundancy is required when the medium is **lossy** and the read is
> **safety-critical**. Elsewhere it is noise.

Which is exactly the condition of most interfaces worth designing: a log line
that may be truncated, a receipt that may be screenshotted, an error that may be
read aloud over a phone. Repeat the identifier. It is not clutter, it is the
thing that makes the object robust.

And it happens to be where the *rhythm* comes from. The repeated stub rows are
the visual metre of the strip — the reason a tag scans as a composition and not
as a list.

### 4. Colour as routing, not flavour

v2 banned colour as "not a rank." Half right, wholly wrong in effect.

Colour on a tag is not decoration and not a fifth type rank — it is an
**instruction with the longest legibility range on the object**. A rail resolves
across a baggage hall at a distance where the destination code is still a grey
smudge. It is the *first* thing read and the *last* thing to fail.

**What is actually standardised, and what is ours.** Exactly one coloured rail on
a real tag is a standard, and it is not about priority: a **green edge marks hold
baggage checked in at an EU airport**, so destination customs can separate
intra-EU bags from third-country ones. IATA treats it as a compliance
requirement. Priority and class-of-service colours are *per-carrier conventions*,
and for short connections IATA's guidance recommends a remark, a **separate**
sticker, or a system attribute — explicitly not a standardised rail on the main
tag. Historically, it was the pre-1990 string tags that used elaborate colour
schemes so handlers could read a destination at a glance.

So the six-state key in `tokens.css` is **a designed vocabulary for information
packages, not an aviation standard.** Ship it labelled as an invention. The
principle it borrows is real; the specific colour-to-meaning mapping is not.

The correct rule is not "no colour." It is:

- Colour must encode a **state that exists in the record** (priority, class,
  short connection, hazard, oversize).
- It appears as a **full-bleed rail or band**, never a 1-px accent or a tint.
- **One rail per package.** Two competing rails is two competing instructions.

That constraint is what makes it playful rather than chaotic — see below.

### 5. Rotation is free hierarchy

Turning the routing serial 90° along the edge of the destination costs no space
and creates an unmistakable second channel. Same size, same weight, different
axis, therefore different domain. The eye separates them instantly without any
label doing the work.

### 6. Machine marks as texture

Barcodes are the only element on a tag with fine, regular, high-frequency
detail. Set against a 4 cm destination code, they create the contrast that makes
the composition feel dense rather than merely crowded — the same
coarse-versus-fine tension that makes Swiss typographic posters work.

This is why the fake barcode was such an expensive shortcut. A gradient gets the
texture but concedes the argument: it says the marks are a picture of function
rather than function itself. `components/barcode.js` now emits real symbols that
scan with a phone.

There is a lovely detail underneath this, and getting it right required a
correction. The interline licence plate is encoded in **Interleaved 2 of 5**,
not Code 128 — IATA's Electronic Bag Tag guide says baggage infrastructure is
built on optically scanned interleaved 2 of 5, footnoting Resolution 740.

I2of5 *interleaves digit pairs*: the first digit of each pair is carried in the
bars, the second in the spaces between them. That is why it needs an even
number of digits, and why it fits ten of them in roughly half the width of a
non-interleaved symbol. Half the width buys a wider X dimension, and a wider X
dimension reads more reliably off a lurching conveyor.

So the licence plate is a **10-digit** number partly because the encoding wants
an even count of numerals. Form following encoding — and note this is the
opposite of the usual assumption that the barcode is a dumb rendering of a
number chosen for human reasons.

---

## So how playful can this get?

Very — but the play lives in **combination, not decoration**.

A bag tag is a grammar: bands, rails, perforations, repeats, rotations, boxed
sequence numbers, barcodes at three densities. Those parts recombine into a huge
space of legitimate objects, exactly the way a Swiss poster system or a
Dieter Rams product family does. The variation is generative, not applied.

Playful, in this system, means:

- **Rail colour** — six saturated states. Loud on purpose. (Ours, not IATA's.)
- **Reversal density** — how much of the strip runs as solid band.
- **Repeat count and rhythm** — four stubs or eight; even or syncopated.
- **Rotation** — what runs vertically, and on which edge.
- **Barcode module width** — fine texture versus coarse.
- **Format** — shelf strip, full 1:7 hero, dashboard row, log line.

Not playful, in this system:

- Illustration dropped onto the face.
- Gradients, glows, rounded corners, drop shadows.
- A rail colour chosen because it looked nice next to the last one.
- A slogan above the destination.

The test is one question: **if I removed this, would a real job fail?** Rail
colour passes when the package is genuinely a priority bag. It fails the moment
it is "warmer than the green one."

That is the difference between a system that is fun and a system that is
decorated. The tag is proof you can have the first without the second.

---

## What changed in v3

| | v2 | v3 |
|---|---|---|
| Ink coverage | ~4% | bands, rails, filled boxes |
| Colour | forbidden by doctrine | six full-bleed rails, one per package (our key, labelled as such) |
| Reversal | none | `.tag-band`, `.tag-seq` |
| Barcode | CSS gradient | real Interleaved 2 of 5 (the actual Res 740 symbology) |
| Redundancy | forbidden by the PO gate | required when the medium is lossy |
| Spacing inside the tag | page scale (~1.5 rem) | tag scale (~2 mm equivalent) |
| Format | 40 rem landscape card | vertical strip, 1:7 hero variant |

See `docs/history.md` for where the object came from, and
`examples/d-tag-strip/` for the anatomy assembled.
