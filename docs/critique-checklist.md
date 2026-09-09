<!-- SPDX-License-Identifier: MIT -->
# Critique checklist

Run this on any closed package: physical tag, page, dashboard row, log line, PDF, slide, box.

![PO completeness gate](../assets/diagrams/po-completeness-gate.svg)

## (a) PO completeness

- [ ] Every visible element has a **named domain**.
- [ ] If the element were removed, a required job would fail (route, identify, claim, audit, attach, survive).
- [ ] There is no “optional” chrome. Optional is not a category. Either the domain is in the package or the element is gone.

## (b) No noise

- [ ] No filler, motivational, or marketing sentences.
- [ ] No decorative illustration that does not encode a domain.
- [ ] No duplicate of a stronger element **for decorative reasons** (pretty city name repeating BKK without a second job).
- [ ] Repetition that *is* present serves tear-tolerance or an orthogonal read path — see (d). Note that (b) and (d) pulled against each other in v2: one forbade duplication while the other demanded backup. Decorative duplication fails; failure-model duplication is required.
- [ ] No emoji, sparkle, or “welcome back”.

## (c) Human hierarchy

- [ ] Destination-equivalent is the largest type.
- [ ] LPN / object id is second, mono, copyable.
- [ ] Context is third (who / when / what flight or env).
- [ ] Human name is fallback, not the hero.
- [ ] A stressed person gets the primary fact in under a second.

## (d) Dual encoding

- [ ] Machine key exists in human-readable form **and** in a machine form (barcode, field, copy button, JSON key).
- [ ] A stub/receipt/permalink exists if the object will leave this screen.
- [ ] Orthogonal backup exists where the reading angle can fail (second barcode, second column, export).

## (e) Size–domain coherence

- [ ] Visual weight matches scan order. No inverted hierarchy.
- [ ] Domain colour, if any, matches a real domain (priority / crew / hazard) and is documented in markup.

## (e2) Density and presence

The gate v2 was missing, and the reason its output read as minimalism.

- [ ] The package carries **solid ink**, not only hairlines and type. Bands, filled sequence boxes, barcode blocks.
- [ ] Type that needs to outrank its neighbours is **reversed out of a band** before it is made bigger. Reversal is free hierarchy; size is expensive.
- [ ] Spacing inside the object uses the **tag scale** (`--tag-gutter`, `--tag-gap-zone`), not the page scale (`--tag-space-5`+). Content runs to the edge.
- [ ] Squint at it. If it reads as a pale panel rather than a printed object, it fails, however correct the hierarchy is.
- [ ] Barcodes are **real encodings** of the id (`components/barcode.js`), not gradients that look like barcodes. A decorative barcode concedes that the marks are ornamental, which is the opposite of this system's claim.

## (f) Material / lifecycle

- [ ] Contrast holds (ink on ground; do not invert the tag into a dark glassmorphism card).
- [ ] The substrate is declared if it matters (thermal vs synthetic vs RFID vs reusable).
- [ ] Nothing relies on a hover, animation, or colour-only cue to carry meaning.

## (g) Evolutionary readiness

- [ ] A later layer (RFID, EBT, reuse mark) **adds** a domain; it does not delete barcode or human type until the whole network can read the new layer.
- [ ] Sustainability, if present, is a lifecycle fact (reuse, recycle path, residue-free adhesive) — not a leaf icon.

**Fail any box → do not ship.** Resize, merge, or remove. Do not add copy to explain the decoration.
