<!-- SPDX-License-Identifier: MIT -->
# Sources

Primary texts this system is allowed to lean on. Do not invent statistics in PRs.

## Design reading

- Vanhoenacker, Mark. “The Humble Airline Baggage Tag Is a Design Masterpiece.” *Slate*, 4 October 2012. Syndicated e.g. [Tifton Gazette reprint](https://tiftongazette.com/2014/07/20/slate-the-airline-baggage-tag-is-a-masterpiece-of-design/).
- Yau, Nathan. “Masterful design of the everyday baggage tag.” *FlowingData*, 18 October 2012. https://flowingdata.com/2012/10/18/masterful-design-of-the-everyday-baggage-tag/
- Gruber, John. “The Design of Airline Baggage Tags.” *Daring Fireball*, 5 October 2012. https://daringfireball.net/linked/2012/10/05/baggage-tags

Vanhoenacker’s piece is the design argument: loop vs string (force across the width), all-weather adhesive, dual barcodes at 90°, custom print so early-adopter airports can still hand-sort, stubs as backup, RFID as a future layer that cannot delete the printed tag until the network is ready.

## IATA (public)

- Resolution **740** — interline bag tag; LPN; **Interleaved 2 of 5** (see Corrections above); optical and manual recording; face width 50.80–54.00 mm (attachments). Printer-facing excerpts: Zebra/industry reproductions of the geometry tables.
- Resolution **751** / LPN issuance white paper — use of all ten digits; lead digit meanings. https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/white-paper_-baggage-lpn-issuance.pdf
- Resolution **753** — four tracking points. Implementation guide (Issue 4.0, 2023): https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/reso753-implementation-guide---2023_issue-4.0.pdf
- IATA baggage tracking (program page, rates change): https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/
- RP **1740c** RFID; RFID fact sheet: https://www.iata.org/contentassets/7d6e4b7e0fbf407eb780e8450102723b/fact-sheet-rfid-bag-tag.pdf
- RP **1754** Electronic Bag Tag; [EBT implementation guide](https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/ebt-implementation-guide-edition-1.2.pdf)
- Baggage standards index: https://www.iata.org/en/programs/ops-infra/baggage/standards/

## Materials (industry guides, not IATA)

- Panda Paper Roll. “Airline Baggage Tags Buying Guide.” https://pandapaperroll.com/thermal-baggage-tags-buying-guide/ — thermal / synthetic / PP laminate / freezer-grade / RFID as a **procurement** hierarchy.

## Corrections logged (do not re-introduce)

- **Symbology is Interleaved 2 of 5, not Code 128.** IATA's EBT Implementation Guide §2.5 footnotes R740 directly. Code 128 appears in adjacent aviation uses; it is not the interline LPN symbology.
- **No "Vandenbergh" invented the bag tag.** No supporting source exists in any patent database or encyclopaedia. The licence-plate data model came from the IATA Baggage Security Working Group chaired by John Vermilye after the 1985 Air India bombing; ratified 1987; United deployed system-wide 1992. **1984 is not a supportable date.**
- **Typeface is not Helvetica or Univers.** The only typeface named in an IATA document is Arial Rounded MT Bold "or similar" (RP1754, restating Res 740). Real tags print in printer-resident fonts.
- **Coloured rails are mostly not standardised.** The one standardised colour is a *green* edge marking hold baggage checked in at an EU airport — a customs marking. Priority/class colours are per-carrier. This repo's six-state rail key is an invention and must be labelled as one.
- **Do not state a fixed number of stub repeats.** It varies by carrier and stock.
- **Reversed type is a design reading, not a specification.** No standard requires it.
- **Res 740 fixes width (50.80–54.00 mm); length (~53 cm) is convention**, set by loop geometry.

## Verified additions

- IATA EBT Implementation Guide (symbology, print zones, 4.1 mm / 3 mm type minimums, 95% 360° read benchmark): https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/ebt-implementation-guide-edition-1.2.pdf
- IATA interline baggage guidance (BTIC of originating carrier; barcode references tag number not flight details; Res 753 four points): https://www.iata.org/contentassets/e7a533819be440edbb1e49da96e0f2a8/guidance-document-on-baggage-standards-for-interline.pdf
- Patents: US4817310 (thermal + reinforcement) · US5145211 (pattern-coated adhesive) · US5366249 (loop + control section, identical barcodes) · US5670225 (directional tear) · US6219947 (two-ply loop, ~22in × ~2in)
- SITA Baggage IT Insights 2025 (6.3/1,000 in 2024; 67% better than 2007; 17% tagging/ticketing errors): https://www.sita.aero/about-us/pressroom/news-releases/more-air-passengers-than-ever-with-one-of-the-lowest-rates-of-mishandled-baggage-thanks-to-tech-investments/
- MoMA *Humble Masterpieces* checklist (bar code and airmail envelope included; no bag tag): https://www.moma.org/docs/explore/exhibitions/humble_checklist.pdf
- SFO Museum, *The Passenger Documented* (2014): https://www.sfomuseum.org/exhibitions/passenger-documented-airline-luggage-labels-bag-tags-and-tickets

## 🚨 Fabricated source — never cite

A quote attributed to **"Dr. Lena Cho, Curator of Material Culture at Cooper Hewitt"** about the luggage tag being "the last unmediated artefact of air travel's golden age" is **AI-generated SEO content**. No such person or job title exists at Cooper Hewitt. Its only origin is an e-commerce "product insights" page.

## What not to cite as fact

- Vendor “99.9% read rate” marketing.
- Frozen mishandling rates copied from old articles (Vanhoenacker’s 2012 US monthly snapshot is historical).
- This studio’s example LPN `0217123456` as a real bag.
