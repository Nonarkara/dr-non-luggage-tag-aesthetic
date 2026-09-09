<!-- SPDX-License-Identifier: MIT -->
# Components

HTML + CSS. Optional one-file JS for copy-to-clipboard. Open any file in a browser.

| File | Tag zone |
|---|---|
| [`TagCard.html`](TagCard.html) | Closed package |
| [`DestinationHero.html`](DestinationHero.html) | Primary destination |
| [`IdBlock.html`](IdBlock.html) | LPN + barcode |
| [`StatusStrip.html`](StatusStrip.html) | Carrier / flight / date |
| [`StubBackup.html`](StubBackup.html) | Claim / stubs |
| [`DashboardRow.html`](DashboardRow.html) | Same package at list density |
| [`tag-system.css`](tag-system.css) | Shared |
| [`tag-system.js`](tag-system.js) | Optional copy |

Markup comments declare **size** and **domain**. That is load-bearing, not a style note.


## Stock B — printed

`stock-printed.css` adds the printed-tag surfaces: `.pt-face`, `.pt-face--field`, `.pt-face--split`, `.pt-band`, `.pt-dest`, `.pt-serial`, `.pt-vertical`, `.pt-arrow`, `.pt-perf`, `.pt-punch`.

Load it after `tag-system.css`, set `data-stock="printed"` and a `data-domain` on the face. Gallery: [`printed.html`](printed.html). Doctrine: [`../docs/stocks.md`](../docs/stocks.md).

Type scales to the **face**, not the viewport — `.pt-face` is a container, and the destination is sized in `cqi`. A tag's type is set to the tag.
