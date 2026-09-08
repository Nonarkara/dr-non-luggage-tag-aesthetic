<!-- SPDX-License-Identifier: MIT -->
# Design tokens

Fork these files. Do not restyle the ranks.

| File | Use |
|---|---|
| [`tokens.css`](tokens.css) | Drop into any page. CSS custom properties. |
| [`tokens.json`](tokens.json) | Same values for Style Dictionary or codegen. |

## What is a token here

A token is a **named information carrier**, not a theme swatch.

- **Ground / ink** — thermal face stock and thermal print. The default package is two colours.
- **Rank** — primary destination, secondary LPN, tertiary context, fallback name. Size *is* the rank.
- **Space** — 4 px module, analogous to a barcode module family.
- **Mono** — LPN, flight, timestamps, request ids. If it is a key, it is tabular and copyable.
- **Domain colours** — `priority`, `crew`, `hazard` only. Documented in the markup as a domain, never as “accent”.

## What is not a token

Gradients, radius scales, shadow elevations, brand rainbows, dark-mode inversion of the tag itself. A tag does not become a night-mode sticker.

## Mapping

See [`../docs/hierarchy.md`](../docs/hierarchy.md) and [`../assets/diagrams/website-dashboard-mapping.svg`](../assets/diagrams/website-dashboard-mapping.svg).
