<!-- SPDX-License-Identifier: MIT -->
# Sources

Primary texts this system is allowed to lean on. Do not invent statistics in PRs.

## Design reading

- Vanhoenacker, Mark. “The Humble Airline Baggage Tag Is a Design Masterpiece.” *Slate*, 4 October 2012. Syndicated e.g. [Tifton Gazette reprint](https://tiftongazette.com/2014/07/20/slate-the-airline-baggage-tag-is-a-masterpiece-of-design/).
- Yau, Nathan. “Masterful design of the everyday baggage tag.” *FlowingData*, 18 October 2012. https://flowingdata.com/2012/10/18/masterful-design-of-the-everyday-baggage-tag/
- Gruber, John. “The Design of Airline Baggage Tags.” *Daring Fireball*, 5 October 2012. https://daringfireball.net/linked/2012/10/05/baggage-tags

Vanhoenacker’s piece is the design argument: loop vs string (force across the width), all-weather adhesive, dual barcodes at 90°, custom print so early-adopter airports can still hand-sort, stubs as backup, RFID as a future layer that cannot delete the printed tag until the network is ready.

## IATA (public)

- Resolution **740** — interline bag tag; LPN; Code 128; optical and manual recording; face width 50.80–54.00 mm (attachments). Printer-facing excerpts: Zebra/industry reproductions of the geometry tables.
- Resolution **751** / LPN issuance white paper — use of all ten digits; lead digit meanings. https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/white-paper_-baggage-lpn-issuance.pdf
- Resolution **753** — four tracking points. Implementation guide (Issue 4.0, 2023): https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/reso753-implementation-guide---2023_issue-4.0.pdf
- IATA baggage tracking (program page, rates change): https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/
- RP **1740c** RFID; RFID fact sheet: https://www.iata.org/contentassets/7d6e4b7e0fbf407eb780e8450102723b/fact-sheet-rfid-bag-tag.pdf
- RP **1754** Electronic Bag Tag; [EBT implementation guide](https://www.iata.org/contentassets/d22bcfe86aa54f22a2919b0e4224f68f/ebt-implementation-guide-edition-1.2.pdf)
- Baggage standards index: https://www.iata.org/en/programs/ops-infra/baggage/standards/

## Materials (industry guides, not IATA)

- Panda Paper Roll. “Airline Baggage Tags Buying Guide.” https://pandapaperroll.com/thermal-baggage-tags-buying-guide/ — thermal / synthetic / PP laminate / freezer-grade / RFID as a **procurement** hierarchy.

## What not to cite as fact

- Vendor “99.9% read rate” marketing.
- Frozen mishandling rates copied from old articles (Vanhoenacker’s 2012 US monthly snapshot is historical).
- This studio’s example LPN `0217123456` as a real bag.
