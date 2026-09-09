<!-- SPDX-License-Identifier: MIT -->
# Philosophy

A white airline baggage tag is not “minimalism.” It is a **complete package under time pressure**.

Pilot Mark Vanhoenacker called the automated bag tag a masterpiece of design and engineering (Slate, 2012). Nathan Yau amplified that reading on FlowingData: the everyday sticky loop is an information system — synthetic substrate, custom-printed destination and name, bar-coded license plate, still manually readable when the black box of the belt fails.

This design system takes that object as law:

1. **PO Completeness.** Every element carries explicit meaning. If it is present, it is required. If it is required, absence breaks the system.

   **The redundancy carve-out.** v2 of this document said *non-redundant*, and that was wrong about the object it claims to describe. A real tag prints the licence plate five or six times down the strip, because the strip gets torn, soaked and abraded and any surviving fragment must still identify the bag. Repetition there is the failure model, not waste — and it supplies the visual rhythm that makes the strip read as a composition. The rule is therefore: **redundancy is required when the medium is lossy and the read is safety-critical; elsewhere it is noise.** Duplicating a label because the layout felt bare still fails.
2. **Size is information.** Type scale is human scan order, not decoration.
3. **Domain is information.** IATA three-letter codes, 10-digit LPN, carrier, material durability, sustainability lifecycle — each is a domain. Colour exists only when a domain (priority, crew, hazard, class, short connection) is actually in the package — but where it does exist it is **loud**: a full-bleed routing rail, not a tint or a 1-px accent. Colour has the longest legibility range on the object; it resolves across a baggage hall when the destination code is still a smudge. v2 treated colour as a risk to be avoided and shipped a system with no ink in it. See [why-it-is-beautiful.md](why-it-is-beautiful.md).
4. **Hierarchy.** Human stress-scan first, then machine-readability, then durability, then lifecycle. Never invert that without renaming the object.
5. **Closed package.** The tag, the card, the row, the log line, the doc header, the shipping label — one object. No leftover chrome.
6. **Density.** The object is packed to its edge. A printed tag runs roughly a third of its area as solid ink and holds content to ~2 mm of a die-cut edge. Restraint means *nothing unnecessary*, not *nothing there*. If the result looks calm, it is a memo, not a tag.

The invitation: **fork the method, not the secrets.** Recreate the same functional aesthetic for websites, systems, docs, packaging, dashboards, and closed information packages. Do not paste private LPNs, passenger data, or airline credentials into a public fork.

Bilingual labels (EN / TH) are welcome when they **add a reader**, not when they repeat the destination as ornament. `BKK` stays the primary. `จุดหมาย` may sit in the city line. `ใบรับ` may sit on the claim stub.
