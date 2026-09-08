<!-- SPDX-License-Identifier: MIT -->
# Standards notes — IATA 740 / 753 (and neighbours)

This repository is **not an IATA publication**. It is a design-system reading of public standards and implementation guides. For operational compliance, use the current IATA manuals.

## Resolution 740 — bag tag as a readable object

Resolution 740 specifies the **interline baggage tag** that must support optical scanning **and** manual recording.

Facts this system depends on (do not invent beyond these):

- **License Plate Number (LPN)** — ten digits; also called the 10-digit bag tag / 10-digit barcode. It is the key into automated baggage systems, departure control, and baggage information messages (RP 1745 / RP 1755).
- **Symbology** — linear **Code 128** encoding the LPN on the tag. The 1D symbol identifies the bag; it does not carry the itinerary.
- **Human type on the same object** — destination, flight data, and name remain printed so a handler or a broken system can still read the tag. IATA’s 753 implementation material states that Resolution 740 defines support for optical scanning, OCR, RFID (with RP 1740c), **and** manual recording.
- **Face geometry** — tag maximum width **54.00 mm**; face material width **minimum 50.80 mm** (Resolution 740 attachments S1/T, as reproduced in industry printer documentation).
- **Lead digit** (with Resolution 751 / 740 §5.1.2) — 0 interline; 1 fallback; 2 interline expedite/rush; 3–9 interline or online. Issuer is the 3-digit code (Resolution 769); serial is six digits.

## Resolution 753 — tracking as a mandatory domain

Resolution 753 requires member airlines to track baggage at **four core points** (wording from IATA’s implementation guide):

1. **Acceptance** — acquisition from the passenger (airport or off-airport).
2. **Load** — delivery of the bag onto the aircraft.
3. **Transfer** — delivery and acquisition when custody changes between members or their agents.
4. **Arrival** — delivery of the bag to the passenger.

The ten-digit bag tag number is **mandatory** whenever a tracking point is recorded. Date/time is recommended, especially for offline scans.

This is why a dashboard row in this design system has a **point** cell, not a mood cell.

## Neighbour practices (evolutionary, not decoration)

| Practice | Job |
|---|---|
| RP 1740a | Tag media quality |
| RP 1740c | UHF RFID for interline baggage (EPC Gen2 / ISO 18000-6C family) |
| RP 1754 | Form and function of the **Electronic Bag Tag** |
| RP 1745 | Baggage information messages (the LPN’s job as a key) |

RFID and EBT **add** a radio domain. They do not license you to drop the printed LPN while any station still reads bars or type.

## Mishandling statistics

IATA publishes mishandling rates that **change by year**. This repo does not freeze a number in the design tokens. For current figures, use [IATA baggage tracking](https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/). Resolution 753 exists because tracking points are the functional response to mishandling — not because a landing page needs a large statistic.

## Sources

Listed in [`sources.md`](sources.md).
