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

Reversal also survives failure. A glare-washed, motion-blurred, half-torn strip
still shows *where the black rectangle is*. Shape survives when glyphs do not.

v2 had no reversal at all, so its only hierarchy lever was size — which is why
everything either shouted or whispered with nothing in between.

### 3. Redundancy as structure — where the old doctrine was simply wrong

v2's "PO Completeness" gate said: *every element carries explicit,
non-redundant meaning; if a stronger element already says it, merge.*

A real bag tag violates that rule on purpose. The licence plate is printed
**five or six times** down the strip. Not as emphasis — as a failure model. The
strip gets torn at an unknown point, soaked, abraded, folded over a handle. Any
surviving fragment must still identify the bag.

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

Colour on a tag is not decoration and not a fifth type rank — it is a **routing
instruction with the longest legibility range on the object**. A red rail
resolves across a baggage hall at a distance where the destination code is still
a grey smudge. It is the *first* thing read and the *last* thing to fail.

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
rather than function itself. `components/barcode.js` now emits real Code 128.
The symbols on the example pages scan with a phone.

There is a lovely detail underneath this. Code 128 **Set C** packs two digits
into each symbol, so an all-numeric, even-length payload encodes at double
density. The IATA licence plate is a 10-digit number partly *because* of that —
the data format was chosen to fit the barcode. Form following encoding.

---

## So how playful can this get?

Very — but the play lives in **combination, not decoration**.

A bag tag is a grammar: bands, rails, perforations, repeats, rotations, boxed
sequence numbers, barcodes at three densities. Those parts recombine into a huge
space of legitimate objects, exactly the way a Swiss poster system or a
Dieter Rams product family does. The variation is generative, not applied.

Playful, in this system, means:

- **Rail colour** — six saturated routing states. Loud on purpose.
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
| Colour | forbidden by doctrine | six routing rails, full-bleed, one per package |
| Reversal | none | `.tag-band`, `.tag-seq` |
| Barcode | CSS gradient | real Code 128, Set C for numeric |
| Redundancy | forbidden by the PO gate | required when the medium is lossy |
| Spacing inside the tag | page scale (~1.5 rem) | tag scale (~2 mm equivalent) |
| Format | 40 rem landscape card | vertical strip, 1:7 hero variant |

See `docs/history.md` for where the object came from, and
`examples/d-tag-strip/` for the anatomy assembled.
