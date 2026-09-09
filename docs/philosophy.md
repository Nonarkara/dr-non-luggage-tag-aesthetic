<!-- SPDX-License-Identifier: MIT -->
# Philosophy

A white airline baggage tag is not "minimalism." It is a **complete package under time pressure**.

That distinction is the whole system. Minimalism removes until a surface feels calm. The tag removes until nothing is left that does not stop a bag from being lost. One is an aesthetic goal; the other is a survival constraint that happens to produce an aesthetic. They look similar in a screenshot and behave nothing alike under load.

Pilot Mark Vanhoenacker called the automated bag tag a masterpiece of design and engineering (*Slate*, 2012). Nathan Yau amplified that reading on FlowingData: the everyday sticky loop is an information system — synthetic substrate, custom-printed destination and name, bar-coded license plate, still manually readable when the black box of the belt fails.

Why the object earns that status, and how it differs from Rams and Vignelli: [`lineage.md`](lineage.md).

Where the old doctrine was wrong, and the mechanisms behind it: [`why-it-is-beautiful.md`](why-it-is-beautiful.md). Where the object came from: [`history.md`](history.md).

---

## The six laws

### 1. PO Completeness

Every element carries explicit meaning. **If it is present, it is required. If it is required, absence breaks the system.**

**The redundancy carve-out.** An earlier version of this document said *non-redundant*, and that was wrong about the object it claims to describe. A real tag prints the licence plate five or six times down the strip, because the strip gets torn, soaked and abraded, and any surviving fragment must still identify the bag. Repetition there is the failure model, not waste — and it supplies the visual rhythm that makes the strip read as a composition.

The rule is therefore: **redundancy is required when the medium is lossy and the read is safety-critical; elsewhere it is noise.** Duplicating a label because the layout felt bare still fails. A city name printed beside `BKK` on a screen — where nothing tears — is noise, because the code already carried that job at a higher rank.

**Optional is not a category.** The instinct to mark something optional is the instinct to avoid deciding. Either the domain is in the package or the element is gone.

### 2. Size is information

Type scale is human scan order, not decoration.

This inverts the usual relationship. Normally a designer chooses a hierarchy that *expresses* importance. Here the hierarchy *is* the routing instruction: the largest element is the one a handler must act on first, and making anything else largest is a factual error about the job.

Making the LPN larger than the destination says the machine key outranks where the bag goes. That is not a taste disagreement — it is wrong in the way a mislabelled axis is wrong. Making everything 16px says there is no time pressure, which is also a claim, and usually a false one.

### 3. Domain is information

IATA three-letter codes, the 10-digit LPN, carrier, material durability, sustainability lifecycle — each is a named domain. **Colour exists only when a domain (priority, crew, hazard) is actually in the package.**

Colour is never a rank. A rank is a position in the scan order; a domain is a fact about the record. A coloured rule on a row means *this record has that property*. A coloured rule "for energy" is a lie about the data, told in paint.

**But where a domain is genuinely present, the colour is loud.** A full-bleed routing rail, not a tint and not a 1-px accent. Colour has the longest legibility range on the object — it resolves across a baggage hall while the destination code is still a smudge. An earlier version of this document treated colour as a risk to be avoided and shipped a system with no ink in it. The discipline is *which* domains earn colour, never *how quietly* they get it.

### 4. Hierarchy

Human stress-scan first, then machine-readability, then durability, then lifecycle. **Never invert that without renaming the object.**

The order is not a preference ranking — it is a dependency chain. Durability protects readability; readability serves the scan; the scan is the point. Optimising a lower layer at the cost of a higher one produces an object that is beautifully manufactured and functionally dead.

### 5. Closed package

The tag, the card, the row, the log line, the doc header, the shipping label — one object. No leftover chrome.

"Closed" means the object answers its own questions without a second surface. A row that requires opening a detail pane to know what it is has not closed. A card with a status you must hover to read has not closed — hover is not available to a thumb, a screen reader, or a printout.

### 6. Density

The object is packed to its edge. A printed tag runs roughly a third of its area as solid ink and holds content to about 2 mm of a die-cut edge.

**Restraint means *nothing unnecessary*, not *nothing there*.** If the result looks calm, it is a memo, not a tag. This is the law most often lost when the other five are read as an argument for austerity.

---

## What the tag is honest about

The property most worth stealing, and the least copied:

**A tag never claims more than it knows.** There is no confidence indicator, no projected arrival, no reassuring green tick over a bag whose scan failed. When the system loses track, the tag says nothing — and the printed name and destination are still there, doing the job at a lower tier.

Most interfaces do the opposite under uncertainty: they show a comforting summary, a cached number with no age, a checkmark over a failure. The tag's design answer is a **fallback rank** — a layer that still identifies the object when everything above it is wrong.

Build the fallback rank. It is where the honesty lives.

---

## Dual encoding, and why the old layer stays

Human-readable *and* machine-readable, always both. RFID did not remove the printed barcode; the barcode did not remove the printed name.

This is not conservatism. A network upgrades unevenly, and **the weakest reader in the journey sets the floor.** A bag routed through one airport that cannot read the new layer is lost by the new layer. So the new layer *adds* a domain and deletes nothing until every reader can read it.

The same rule governs an interface. A copy button does not replace the visible id. A JSON export does not replace the readable row. A QR code does not replace the URL.

---

## The invitation

**Fork the method, not the secrets.** Recreate the same functional aesthetic for websites, systems, docs, packaging, dashboards, and closed information packages. Do not paste private LPNs, passenger data, or airline credentials into a public fork.

Bilingual labels (EN / TH) are welcome when they **add a reader**, not when they repeat the destination as ornament. `BKK` stays primary. `จุดหมาย` may sit in the city line. `ใบรับ` may sit on the claim stub.

---

## Where this stops being right

The tag answers eleven seconds. It is the wrong answer to an afternoon.

A long read, a citizen service in sunlight, a ministry deck — each has a different reader in a different condition, and applying tag discipline unchanged produces something cold, terse, or bureaucratic. Pick the register first: [`registers.md`](registers.md).
