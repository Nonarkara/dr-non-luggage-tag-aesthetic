<!-- SPDX-License-Identifier: MIT -->
# MoMA rules, and where they stop

**The frame obeys. The face and the skin do not.**

[MoMA Rules](https://github.com/Nonarkara/moma-rules) is Dr Non's layout canon in
a form that executes — ten laws, each with a check that fails a build rather than
a principle that asks to be agreed with. This document says which parts of the
luggage-tag system sit inside that envelope, which sit outside it on purpose, and
why the boundary falls where it does.

The split is not a compromise. It is MoMA's own: their production stylesheet
carries 876KB of CSS and exactly three chromatic values, because **the colour is
supposed to be in the art, not the chrome.** The wall is modular. The painting on
it is not. That is the same line drawn here.

---

## The three layers

| Layer | What it is | Governed by | Checked by |
|---|---|---|---|
| **Envelope** | The page the tag is shown on — sections, columns, gutters, rules, rows, lists | MoMA Laws I–IX in full | `checkMomaScale` in `tools/tag-audit.mjs` |
| **Face** | The depicted object — the 50.8mm printed tag and its interior | Its own closed sub-scale, stated below | Exempt from the page scale; Law VII still applies |
| **Skin** | Ephemera — stamps, biro, rotation, misregistration, torn perforation, fade | The accumulation rule: a mark may appear only where the event it records happened | `checkEphemeraEvents`; exempt from MoMA entirely |

Accents, flavours, and follies live in the skin. They are outside the laws by
design, and the exemption is deliberately narrow — the audit grants it only to a
line carrying an `eph` marker or a face token, never to a comment claiming one.

---

## Law by law

**I. One origin** — applies to the envelope. Inside a face the origin is the
die-cut edge, not the page datum, and the hairline corollary holds everywhere: a
1px rule is drawn with `outline` or `box-shadow: inset`, never with a `border`
that displaces its children.

**II. The scale** — the envelope uses the closed fifteen. See the face sub-scale
below. The skin is exempt.

**III. Size and leading are one token** — applies, and this system goes further.
Size here is not a style but a **rank**: destination, stable id, context, human
fallback, stub. Five tokens, and the id may never outrank the destination. See
[`hierarchy.md`](hierarchy.md).

**IV. The grid fills · V. One rhythm · VI. Same skeleton** — apply to the
envelope unchanged. VI is weaker than what already holds here: PO Completeness
requires every face to carry the same *slots*, not merely the same height.

**VII. No near miss** — applies at every scale, with no exemption anywhere,
including inside the face and the skin. A 1–6px delta reads as a failed attempt
at alignment rather than an intentional offset, and that is true of a rotated
stamp as much as of a column. Rotate a mark 6 degrees or leave it square; a mark
1 degree off is not weathered, it is wrong.

**VIII. One hairline** — reconciled rather than adopted. A border here is one of
two things and never something between:

```
0 / 1 / 2px      a LINE.  1 is the hairline.
                          2 is the object's own edge — Law VIII's
                          "deliberate emphasis", and the only second weight.
>= 4px on scale  a BAND.  A colour block that happens to be declared as a
                          border, like the domain rail. It is ink, not chrome.
```

1.5, 2.5, 3, 5 and 6 are neither — too thick to read as a rule, too thin to read
as a field. That is exactly where "a second design language arguing with the
first" lives, and the audit fails on it. The skin is exempt: a 2.5px stamp rule
is an impression, not a border.

**IX. Zero radius** — already law here. The loop punch is a true circle and
exempt, as it is in MoMA Rules.

**X. Never say a number twice** — **this system inverts it, and the inversion is
the point.**

A real tag prints the licence plate five or six times down the strip. Not because
the build was lazy in public, but because the strip tears, and the read is
safety-critical. Law X is right about a screen, where the medium is lossless and
a repeated value is the build showing its working. It is wrong about a tag.

The rule that replaces it: **redundancy is required when the medium is lossy and
the read is safety-critical; elsewhere it is noise.** A dashboard is lossless —
Law X applies to it in full. See [`philosophy.md`](philosophy.md).

Law X's second half — hierarchy follows semantic weight, the thing you look up by
is the largest thing in the cell — is adopted without change. It is the same
statement as this system's own first law.

---

## The face sub-scale

A 50.8mm printed face is not a 1280px page. Forcing the page's 4px base into it
would collapse three distinct interior roles into one and destroy the density
that does the sorting work on a printed tag with no barcode.

So the face declares its own set, and it is closed:

```
2px   --tag-gap-tight    between rows of a stub block
3px   --tag-gutter       the die-cut margin, ~2mm at face scale
6px   --tag-gap-zone     between anatomical zones
6px   --tag-pad-zone     inside a zone
```

Three values, each with a named role. Law II's requirement is that the set be
closed, not that it be that particular set — two elements align when their values
come from the same small set and cannot when the set is open. A fourth face value
needs a fourth role, written down here first.

---

## Running the check

```bash
node tools/tag-audit.mjs . --strict
```

Off-scale envelope spacing and in-between border weights are errors. The face and
skin exemptions are granted by token name, not by intention — an ordinary
component cannot claim them by adding a comment.

The four MoMA laws that need a laid-out page rather than source text (orphan grid
cells, ragged rows, near-miss edges, rhythm count) are not implemented here.
Until they are, run them from MoMA Rules itself:

```bash
npx --yes github:Nonarkara/moma-rules moma-lint .
```
