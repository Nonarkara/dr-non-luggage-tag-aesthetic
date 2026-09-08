<!-- SPDX-License-Identifier: MIT -->
# Skill examples

## 1. Website status card

**Before (fail):** “Welcome back! Your journey is looking amazing 🚀 Unlock premium tracking.”

**After (pass):** Destination `BKK` primary; `0217123456` secondary; `ARRIVAL · BELT 22 · TG 676` tertiary; `ARKARA/NON` fallback; claim stub with the same LPN.

File: `examples/a-website-status-card/index.html`

## 2. Log line

**Before (fail):** `🎉 Woo! Bag processed OK :) status=awesome dest=bangkok? id=null`

**After (pass):**

```
BKK  lpn=0217123456  point=LOAD  flt=TG676  date=08SEP26  pax=ARKARA/NON
```

File: `examples/b-api-log-line/index.html`

## 3. Doc header

**Before (fail):** “Welcome to the amazing handbook ✨”

**After (pass):** Primary `740`; secondary `docs/standards-740-753`; tertiary `08SEP26 · Nonarkara`; fallback “IATA Resolution 740 + 753 notes”.

File: `examples/c-documentation-header/index.html`

## 4. Agent rewrite prompt

> Rewrite this dashboard widget as a closed baggage-tag package. Declare size and domain on each node. Delete anything that fails PO Completeness. Do not invert to dark glass. Do not add a slogan.

## 5. Domain colour (only when justified)

Expedite row: `data-domain="priority"` and lead-digit-2 analogue in the id. The left rule is the domain, not a hover accent. Without an expedite record, the rule is absent.
