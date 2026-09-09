<!-- SPDX-License-Identifier: MIT -->
# Registers — when this aesthetic is right, and when it is wrong

> Imported from [Axiom Design Core](https://github.com/Nonarkara/Axiom-Design-Core) §XV, because that system paid for the lesson first.

A design core that claims to be universal will be applied to surfaces it damages, and the damage looks like coldness, illegibility, or a service that reads as a receipt. Axiom described one register — a dark operator console — while presenting itself as a general law, and every non-console surface fought it until the registers were named.

**This system carries the same risk.** The bag tag is a specific kind of object: high pressure, low dwell time, machine-adjacent, read once by someone who did not choose to read it. Those conditions produce its virtues. Where the conditions do not hold, the virtues become defects.

Pick the register before the first line of CSS. Write it in the project's own `context.md`.

---

## The five

| Register | The reader, and their condition | Tag aesthetic fits? |
|---|---|---|
| **Console** | An operator at a desk, live data, possibly 2am | **Yes — natively.** This is the tag's own register. Dense, machine-adjacent, scan-first. |
| **Index** | Someone reading a ranking or a methodology, deliberately | **Mostly.** Keep the ranks and the id discipline; loosen density so a long table scans without fatigue. |
| **Civic** | A citizen, one thumb, outdoors, in sun, who did not choose to be here | **Partly, and carefully.** Keep destination-dominance and the fallback rank. Drop the density. Raise targets past 44px. The tag is *terse*, and terse reads as *cold* when the reader is anxious rather than busy. |
| **Editorial** | Someone reading start to finish, unhurried | **No.** The tag has no register for prose. Measure caps at 65–75ch, a serif is permitted, density drops. Forcing four ranks onto an essay produces something nobody finishes. |
| **Institutional** | A minister, a board, a projected room, a printed page | **No, and the failure is expensive.** A tag-styled deck reads as a receipt. Restraint here must read as *formality*, not as *operational*. |

## The test that picks the register

Not "what am I building" — **"who is reading this, and in what physical condition?"**

An operator at a desk and a citizen in Phuket sunlight are not the same reader, and giving the second one a 2am ops surface is a failure of empathy dressed as consistency.

Four questions, ninety seconds, before any CSS:

1. **Who is reading, and in what condition?** This picks the register. Nothing else does.
2. **What is the one thing they must not miss?** That element becomes the destination rank.
3. **Is there time pressure?** If not, the four-rank scan hierarchy is solving a problem that does not exist — and a hierarchy that solves nothing reads as shouting.
4. **What am I diverging on, and does it pass all three parts of the Divergence Protocol?** ([`lineage.md`](lineage.md) §5.)

## What never changes, in any register

The tag's own invariants hold everywhere, because they are about honesty rather than intensity:

- **PO Completeness.** If it is present, it is required. No exception path, in any register.
- **`border-radius: 0`**, except a true circle that carries meaning (the punch hole, a status dot).
- **No gradient between two hues**, no `box-shadow` except `inset` and `:focus-visible`, no glassmorphism.
- **Dual encoding.** Human-readable *and* machine form, and the new layer never deletes the old.
- **A fallback rank.** Something identifies the object when every system above it fails.
- **Contrast ≥ 4.5:1** body, ≥ 3:1 large. A tag that cannot be read has failed at the only thing it does.
- **Every number carries its source, tier, and age.** The tag never claims more than it knows.

## What the register is allowed to move

Density · type scale absolute sizes · whether a serif is permitted · motion budget · ground temperature · how many domains may be visible at once · target sizes.

Nothing else.

---

## The honest failure mode

If a surface built from this system feels cold, bureaucratic, or unreadable, the most likely cause is not that the rules were applied badly. It is that they were applied to a reader who was never under time pressure.

The tag is a beautiful answer to eleven seconds. It is the wrong answer to an afternoon.
