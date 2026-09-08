<!-- SPDX-License-Identifier: MIT -->
# Evolution — paper → RFID → reusable

Later layers add a domain. They do not delete earlier layers until the **whole network** can read the new one.

![Evolutionary stack](../assets/diagrams/evolutionary-stack.svg)

## Material stack (industry buying guides)

Procurement guides for thermal bag tags commonly rank substrates by duty, not by fashion. This repo uses that stack as **lifecycle information**:

| Layer | Domain it adds | Typical duty (guides, not IATA law) |
|---|---|---|
| Normal direct thermal | Cheap, indoor, short-haul | Fades; moisture fails it |
| Synthetic thermal | Water / abrasion | Long-haul, humid |
| PP / PE laminate | Tear / scuff film | Default durable loop tag in many catalogues |
| Freezer-grade adhesive | Cold hold | Winter tarmac, cold-chain — **adhesive is the information** |
| RFID inlay | Radio identity | Dual ID with barcode; UHF EPC Gen2 class |

Cite a buying guide as a buying guide. Do not pretend a vendor SKU is Resolution 740.

## RFID (EPC Gen2)

IATA RP **1740c** is the recommended practice for RFID on interline baggage (UHF, ISO 18000-6C / EPC Gen2 family). IATA’s public RFID fact sheet describes a 2019 AGM resolution supporting RFID **in addition to** the existing barcode, plus updated RP 1740c performance tests.

Hong Kong’s airport-wide RFID (from 2008) is the early-adopter story Vanhoenacker already used in 2012: RFID does not replace the printed automated bag tag **until receiving stations can handle it**. Dual encoding is the migration rule.

This repo does not repeat IATA business-case dollar figures. Read IATA’s fact sheet if you need their ROI model.

## Electronic / reusable tags

IATA RP **1754** and the Electronic Bag Tag implementation guide cover reusable hardware with electronic paper, RFID memory, and association to an LPN. Vanhoenacker noted the 2010 Australian domestic permanent-tag experiments and the missing manual backup if the network is not global.

**Sustainability** here is that domain: reuse cycles, a recycle/return plan, residue-free adhesive, battery rules. A leaf icon with the word “eco” is not a domain. It fails PO.

## Design-system rule

When you add RFID, EBT, or a recycle mark to a UI:

1. Name the domain in markup (`data-domain="rfid"` or a stub labelled `REUSE`).
2. Keep destination, LPN, and human fallback until you can prove every reader in the journey uses the new layer.
3. Do not restyle the tag as a gadget advertisement.
