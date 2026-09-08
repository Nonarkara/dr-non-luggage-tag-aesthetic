<!-- SPDX-License-Identifier: MIT -->
# Contributing

PRs must produce a **more complete package**, not a prettier poster.

## Must

- Pass [`docs/critique-checklist.md`](docs/critique-checklist.md).
- Keep ground + ink as the default. Domain colour only with `data-domain` and a reason.
- Cite IATA / FlowingData / buying guides **accurately**. If you cannot source a number, omit the number ([`docs/sources.md`](docs/sources.md)).
- Keep example LPN `0217123456` (or another obviously synthetic id). No live passenger data.
- Add `size` + `domain` comments on new markup.
- SPDX: MIT.

## Must not

- Slogans, emoji chrome, dark-glass “rebrand”, extra type ranks, shadow systems.
- Secrets, tokens, private dashboards, real bag tags.
- Fake statistics or “99.9%” vendor claims presented as IATA fact.

## How

1. Fork. Branch. Small PR.
2. If you change tokens, change `tokens.css` **and** `tokens.json`.
3. Open `examples/gallery/index.html` locally and confirm the object still reads as a tag.
4. Describe the domain you added or the noise you removed — not how you feel about whitespace.

Fixes to citations and hierarchy errors are as welcome as new components.
