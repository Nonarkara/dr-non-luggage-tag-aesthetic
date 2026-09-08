<!-- SPDX-License-Identifier: MIT -->
# Security

This repository is a **public design system**: tokens, HTML, SVG, and documentation. It does not run a production service and does not hold passenger data.

## What to report

- A **secret** accidentally committed (API key, token, private URL, live LPN/PNR, personal data).
- A change that would instruct agents to scrape private airline/DCS systems or to treat example identifiers as real.

Do not open a public issue that pastes the secret. Email the maintainer via the GitHub profile for [Nonarkara](https://github.com/Nonarkara) or open a private advisory if GitHub Security Advisories are enabled.

## What not to report

- Visual taste, missing rounded corners, absence of dark mode on the tag. Those are design-system law, not vulnerabilities.
- IATA compliance of a fictional example tag.

## Policy

- No credentials in git. Environment *names* only, if a fork adds code.
- Example identifiers stay synthetic.
- Fork the method, not operational systems.
