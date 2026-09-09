<!-- SPDX-License-Identifier: MIT -->
# History — where the object came from

Sourced against primary documents where possible. Claims that could not be
verified are marked, and a few widely-repeated stories are marked as myths,
because this repo would rather be dull than wrong.

Full source list: [`sources.md`](sources.md).

---

## The short version

> The modern bag tag has **no single designer**. Its data model was specified by
> an IATA working group chaired by John Vermilye of Eastern Air Lines after the
> 1985 Air India bombing, and ratified by IATA resolution in **1987**. Its
> physical form was developed in parallel by competing label manufacturers
> between **1987 and 1999**. **United Airlines** was the first carrier to deploy
> it system-wide, in **1992**.

If you take one thing from this page: **the bag tag's information architecture is
a counter-terrorism artefact.** Passenger–baggage reconciliation came first.
Automated sorting was the dividend.

---

## 1882 — the separable coupon

John M. Lyons, Moncton, New Brunswick, patented the separable coupon ticket on
**5 June 1882**: issuing station, destination, and a consecutive reference
number, with the lower half given to the passenger and the upper half strapped
to the bag. Railways first, aviation later.

⚠️ A genealogy record gives the same Moncton figure's name as John *Mitchell*
Lyons (1850–1926) while the design literature says John *Michael*. Write
"John M. Lyons."

Everything structural about a modern tag is already there: a shared identifier,
one copy that travels with the object, one copy that travels with the person.

## 1929–1950s — two different objects, often confused

**Warsaw Convention (1929), Article 4** set criteria for issuing baggage checks;
by the 1930s airlines issued standardised paper destination tags on string.

Do not conflate these two artefacts:

1. The **luggage label** — adhesive advertising art, airline logos, route maps,
   light and dark grounds signalling day and night service. This is the
   collectable "golden age" object, and its sophistication was comparable to
   airline travel posters.
2. The **destination tag** — the working paper tag on a string that actually
   routed the bag.

The nostalgia industry sells the first. This repo is about the second.

## Pre-1990 — the immediate ancestor

Paper, string-attached, carrying airline name, flight number, a six-digit tag
number prefixed by the two-letter airline code, and the destination. Originally
hand-written, later pre-printed.

**Colour did the routing.** Elaborate colour schemes let handlers identify a
bag's destination at a glance. Worth noting when people assume the modern
coloured rails are the traditional thing — historically it is the reverse.

It died because it offered little security, was trivial to replicate, and manual
reading could not scale with passenger volumes and connection counts.

## 1985 — Air India Flight 182

A bomb in checked luggage destroyed Air India 182 on **23 June 1985**. IATA, the
ATA and ACI formed the **Baggage Security Working Group**, chaired by **John
Vermilye**, then head of baggage at Eastern Air Lines.

Vermilye's proposal, developed with Allen Davidson of Litton Industries, was the
**licence plate** concept: put a barcoded *number* on the tag that acts as a
pointer into a database, rather than putting the passenger's data on the tag.

Adopted by IATA resolution in **1987**. By **1989** it had grown from a security
reconciliation tool into the basis for automated sortation. Vermilye joined IATA
as Manager Baggage in 1988.

⚠️ **Two myths to avoid.** There is no evidence for any "Vandenbergh"
attribution — it appears in no patent database, encyclopaedia or design source.
And **1984** is not a supportable origin date; use 1985 / 1987 / 1989 / 1992.

## 1987–1999 — the physical artefact, by patent

No single inventor; competing manufacturers solving different failure modes:

| Patent | Assignee | Contribution |
|---|---|---|
| US4817310 (1989) | Rand McNally | Thermally imprintable tag with longitudinal glass-fibre reinforcement |
| US5145211 (1992) | CCL Label | Pattern-coated adhesive with adhesive-free zones |
| US5366249 (1994) | Fix GmbH | Single-web strip, loop + tear-off control section, **identical barcodes at both ends and on the stub** |
| US5670225 (1997) | Yupo | Synthetic paper with **directional** tear resistance |
| US6219947 (2001) | now Taylor Communications | Two-ply loop tag; states the ~22 in × ~2 in dimensions |

## 1992 — first system-wide deployment

**United Airlines**, with tag manufacturer Print-O-Tape.

---

## Why the object looks the way it does

Each of these traces to a named failure mode, not to taste.

**Why thermal, and therefore why black-only.** The tag must be customised at the
point of use — pre-printing every airline × flight × destination × date is
impossible. Direct thermal needs no ink, toner or ribbon (Rand McNally, 1987).
The consequence is the aesthetic: **one ink density, no colour, no halftones, no
gradients, printer-resident fonts.** Hard-edged pure black is not a style
decision; it is the only thing a thermal printhead can do. Any gradient or tint
in a bag-tag pastiche is a tell.

**Why ~51 mm wide, and why the length is looser.** Resolution 740 fixes the face
width at **50.80–54.00 mm** — a printhead constraint binding on every check-in
desk on earth. Length (~53 cm) follows from loop geometry: wrap a handle, overlap
enough to bond adhesive to liner, plus a claim stub, plus a repeated barcode.
**Width is law; length is arithmetic.**

**Why the loop must NOT stick to the bag.** The adhesive closes onto the tag's
own non-stick liner, so the tag rides and rotates freely on the handle. A tag
that cannot rotate presents one fixed face to a 360° scanner array — and if that
face is down, the read fails. Free rotation is a *scanning* requirement wearing
the costume of a convenience feature. The loop also distributes force across the
tag's full width, where a string concentrates it on a small section.

**Why it survives a nick.** The substrate is anisotropic synthetic paper:
Elmendorf tear of **15–80 g** along one axis versus **100–600 g** across it, so a
transverse tear does not propagate (Yupo, US5670225). Matching the design-press
account that tags must not tear further once nicked.

**Why the stub tear exposes adhesive.** Base ply and liner are cut at different
offsets, so removing the passenger's receipt exposes a fresh strip of adhesive
and arms the loop closure. One gesture, two functions.

---

## The data model

**LPN = 1 + 3 + 6.**

| Position | Field | Meaning |
|---|---|---|
| 1 | Tag type | `0` interline/online · `1` fallback · `2` RUSH · `3`–`9` carrier-specific |
| 2–4 | BTIC | Baggage Tag Issuer Code, assigned under Res 769 (e.g. `001` American) |
| 5–10 | Serial | Six-digit sequential bag number |

**The tag is a pointer, not a record.** IATA states the barcode references the
ten-digit tag number, *not* the flight details printed beside it; those resolve
through Baggage Information Messages. Everything human-readable on the face is
**redundant backup for when the database link fails** — which is exactly why the
layout reads like a fallback document.

⚠️ A common error: that the last three digits count bags in a series. This
conflicts with the 1+3+6 structure.

**Symbology: Interleaved 2 of 5**, per IATA's EBT guide footnoting R740 — *not*
Code 128, which several secondary sources get wrong. I2of5 interleaves digit
pairs (first digit in the bars, second in the spaces), needs an even digit
count, and fits ten digits in roughly half the width of a non-interleaved
symbol. Narrower symbol → wider X dimension → more reliable reads off a moving
belt. **The 10-digit length is partly an encoding constraint.**

**Specified layout.** Final destination at the **top** of the routing area, vias
beneath it ordered first-transfer-lowest — so the list reads bottom-to-top in
journey order. Minimum type: **4.1 mm** routing area, **3 mm** information area.
The only typeface named in an IATA document is **Arial Rounded MT Bold "or
similar"** — so "Helvetica" and "Univers" are folklore; in practice tags print in
whatever font the thermal printer has resident.

**The barcode appears twice, offset 90°**, because a baggage system is a far more
three-dimensional environment than a supermarket checkout.

**The green edge is customs, not priority.** It identifies hold baggage checked
in at an EU airport so destination customs can separate intra-EU from
third-country bags. Priority and class colours are per-carrier; IATA suggests
short connections be flagged by a remark or a *separate* sticker rather than a
rail. **The rail key in this repo is our invention.**

---

## Res 753 — what changed conceptually

Requires scanning at four custody points: check-in/loading, the agreed transfer
point, handover to a downline carrier, and arrival.

753 is a **process** standard, not a format standard — it says nothing about how
the tag looks. What it changed is what the tag is *for*: from an identifier read
at sortation to a custody-transfer token generating an auditable event trail.

⚠️ Adoption/effective dates (commonly given as 2013 / June 2018) are unverified
here.

---

## Recognition — a smaller literature than you would expect

The serious design criticism of the airline bag tag is essentially **two posts,
two weeks apart, in October 2012**: Mark Vanhoenacker's *Slate* piece ("It's a
masterpiece of design," 4 Oct 2012) and FlowingData's response (18 Oct 2012).

**MoMA's *Humble Masterpieces* (2004, 122 objects, curated by Paola Antonelli)
did not include a bag tag** — but it did include the **Bar Code** and an
**Airmail Envelope**. The canon reached into exactly this register — disposable,
machine-readable, logistical — and picked the barcode rather than the object
that carries it.

⚠️ No evidence was found of a bag tag in MoMA's *collection*; the collection
database blocks automated queries, so this is "no evidence," not "confirmed
absent." Luggage tags on moma.org are **Design Store merchandise**, not
accessions. Same trap at the Delta Flight Museum.

The real institutional home is **SFO Museum** — AAM-accredited, in an airport,
with a catalogue classification literally named *"Baggage Destination/Handling
Tag,"* and two relevant exhibitions (2009, 2014). The **National Air and Space
Museum** holds an Airline Baggage Label Collection (NASM.XXXX.0146).

🚨 **A fabricated quote is circulating.** A line attributed to "Dr. Lena Cho,
Curator of Material Culture at Cooper Hewitt," about the luggage tag being the
last unmediated artefact of air travel's golden age, is **AI-generated SEO
content**. No such person or job title exists at Cooper Hewitt. It is
rhetorically perfect, which is precisely why it is tempting. Do not use it.

---

## Reliability

SITA *Baggage IT Insights 2025*: **6.3 mishandled bags per 1,000 passengers** in
2024 (6.9 in 2023), a **67% improvement since 2007**. Of those, 74% delayed, 18%
damaged or pilfered, 8% lost or stolen. Root causes: transfer 41%, **tagging and
ticketing errors 17%** — which *rose* three points — loading 16%.

Read rates: IATA's benchmark for the printed tag is **95% on an automatic 360°
array**; RFID programmes claim 99%+. Only **3%** of lost bags involve a detached
tag.

The relevant fact for a designer: **the tag is not a solved problem.** A sixth of
all mishandling is still a tagging or ticketing error.
