<!-- SPDX-License-Identifier: MIT -->
# Anatomy

The white baggage tag is a **closed information package**. Every zone below is a domain. If a zone is on the object, it is required. If it is required, removing it breaks routing, claim, or audit.

![Anatomy of the tag](../assets/diagrams/anatomy.svg)

## Zones

| # | Zone | Domain | Size rank | If absent |
|---|---|---|---|---|
| 1 | Loop / punch | Attachment | Material, not type | Tag detaches or tears at a point |
| 2 | Orthogonal barcode | Machine, second axis | Secondary, rotated | 3D conveyor miss |
| 3 | Destination IATA code | Human destination | **Primary** | Handler cannot sort under time pressure |
| 4 | Carrier / flight / date | Context | Tertiary | Cannot sort without a lookup |
| 5 | Passenger name | Human fallback | Fallback | No backup when LPN and systems fail |
| 6 | 10-digit LPN + Code 128 | Machine key | **Secondary** | No key into BHS / DCS / messages |
| 7 | Stubs / claim | Detachable backup | Stub | No receipt; previous stubs confuse the next scan |
| 8 | Face stock + adhesive | Durability / lifecycle | Material | Unreadable or detached object |

Physical width of the face: **minimum 50.80 mm, maximum tag width 54.00 mm** (IATA Resolution 740 attachments). This repo treats that interval as the *metaphorical* density of a digital package: narrow, complete, no spare chrome.

## LPN (License Plate Number)

Ten digits, as used in Resolution 740 / 751 and baggage messaging:

1. **Lead digit** — 0 interline; 1 fallback; 2 interline expedite/rush; 3–9 interline or online (see IATA LPN issuance notes).
2. **Issuer** — three-digit bag-tag issuer code (Resolution 769).
3. **Serial** — six digits from the departure control system.

Example used throughout this repo: `0217123456` (lead 0, issuer 217, serial 123456). **Example only. Not a live bag.**

The linear barcode is **Code 128** encoding that LPN. The 1D symbol is an identifier, not a routing document: flight and city live in human type and in messages (RP 1745 / BSM), not inside the bars.

## Dual encoding

Vanhoenacker (2012) records the operational reason the barcode appears **twice, offset 90°**: baggage systems are three-dimensional. This repo’s dual-encoding rule is the same idea: human type + machine key; screen + copyable string; object + stub/receipt.

## What is not anatomy

Airline logos as decoration, motivational copy, unused colour fields, “premium” badges, stock photography of suitcases. Those fail the [PO gate](critique-checklist.md).
