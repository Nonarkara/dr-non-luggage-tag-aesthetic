<!-- SPDX-License-Identifier: MIT -->
# Grid — every edge resolves to another edge

> Imported from [Rams × NYCTA Design Core](https://github.com/Nonarkara/Rams-NYCTA-Design-Core) — the Planar Alignment Law. A physical tag obeys it for free; a digital one does not.

A printed tag is struck by a machine onto a fixed face. Every zone boundary is shared by construction: the destination block ends exactly where the barcode field begins, because one die and one print head decided both.

A digital imitation gets none of that for free. This is the most common way a tag-styled interface fails — not by adding decoration, but by letting one edge land eleven pixels short of the one beside it.

**Misalignment reads as accident.** Accident is the single thing a bag tag never reads as.

---

## The law

> Trace any edge across the surface. Before it terminates, it must meet another edge — a sibling's boundary, a shared margin, a module rule, or the page edge. Never arbitrary whitespace.
>
> Everything snaps to the invisible grid. The grid is invisible *because* everything snaps.

## What it means in practice

- **One grid, declared once.** Columns, gutters, and the container width are tokens, never per-component numbers. Sibling zones share a `gap`; stacked sections share their left and right insets.
- **Edges align across zones, not only within them.** The left edge of the destination, the left edge of the LPN, the left edge of the context strip, and the left edge of the stub sit on one line.
- **Vertical rhythm follows the same discipline.** Baselines and zone tops land on shared steps, not eyeballed offsets.
- **A caption aligns to the edge of the thing it captions**, not to its own margin.

## Line weight carries role

The tag uses rules, never shadows, to build structure — so the rules must do more work than a single hairline can.

| Weight | Role |
|---|---|
| `--tag-rule-width` (1.5px) | Structural division — a zone boundary, the tear line above a stub |
| `--tag-rule-hair` (1px) | Separation inside a zone — rows in a context strip |
| Domain colour rule | A domain is in the record. Never for emphasis |

**Uniform 1px everywhere is itself a tell.** It says nobody decided which line mattered. On a real tag the perforation, the fold, and the field divider are visibly different operations.

## The check, before shipping any surface

Overlay a grid — mentally or literally — and look for a single edge that does not meet another. If one floats, the layout is unfinished. Snapping it is a one-line mandatory fix, not scope creep.

Two faster versions:

- Squint until the type is unreadable. What remains should be a small number of clean rectangles, not a scatter.
- Screenshot it, and draw four lines: the leftmost edge, the rightmost, the topmost, the bottom. Every element should touch at least one, or another element's edge.

## Why this is the difference between authored and generated

Aligned edges are how an eye registers *someone decided*. It is the same signal as a die-cut corner or a correctly-set condensed grotesque: evidence of a decision, at a scale below conscious notice.

Generated layouts are usually *nearly* aligned — close enough to look intentional in a screenshot, wrong enough to feel off in the hand. The canon objects contain no accidental edges. Neither does a bag tag; it cannot afford one.
