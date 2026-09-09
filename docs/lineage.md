<!-- SPDX-License-Identifier: MIT -->
# Lineage — why the tag is good design

> Companion cores: [Axiom Design Core](https://github.com/Nonarkara/Axiom-Design-Core) · [Rams × NYCTA Design Core](https://github.com/Nonarkara/Rams-NYCTA-Design-Core). This file is where the three meet.

The luggage tag is usually praised as minimalism. That reading is wrong, and getting it wrong is what produces bad imitations — white space, thin type, a big word, no information.

The tag is not minimal. It is **complete under hostile conditions**. Every property it has was forced by a failure, and the ones that survived are the ones that stopped a bag from being lost.

That is the whole argument for treating it as law, and it is worth stating precisely, because it is the strongest claim this system makes.

---

## 1. It was never styled

Dieter Rams' radios sat on shelves in good light. Vignelli's 1972 diagram was argued over by committees for a decade. Both are magnificent, and both were *decided* — a designer chose, and taste carried the choice.

The bag tag was not decided. It was **selected**, in the biological sense.

Roughly four billion bags a year pass through a system that soaks them, freezes them, drags them face-down across steel, photographs them at angles nobody planned, and hands them to a person with eleven seconds and no context. Anything decorative was removed because it cost money at that volume. Anything ambiguous was removed because it produced a mishandled bag and a claim. Anything merely tasteful never survived a procurement review.

What is left is not a designer's opinion. It is the residue of millions of daily failures.

**This is why it is good design, and it is a different kind of good than Rams or Vignelli.** They achieved restraint through judgment. The tag achieved it through attrition. When you copy Rams you are copying a person's taste, and you may copy it badly. When you copy the tag you are copying an experimental result.

## 2. What it shares with Vignelli

Vignelli's subway diagram and the bag tag solve one problem: **get a stressed stranger to the right place, fast, using a closed set of symbols.**

| Vignelli / NYCTA | The tag |
|---|---|
| Topology over geography — the map lies about distance to tell the truth about decisions | The tag shows no route, no map, no journey. Only the next decision: which pile |
| A closed route palette. No ninth colour, ever | A closed code set. `BKK` is three letters from a finite, governed list |
| The disc encloses identity; bare colour is a signal | Enclosed: the destination block. Bare: a priority or hazard stripe |
| 45° angles only — the constraint makes the system legible | Four type ranks only — the constraint makes the scan order legible |
| The rider never learns the system; the system teaches itself in one glance | The handler never trains on the tag |

The deepest shared move: **both abstract away everything that is true but not decision-relevant.** The subway map omits real geography. The tag omits the flight path, the aircraft, the weather, the passenger's history. Both are accused of being reductive by people who have never had to act in eleven seconds.

## 3. What it shares with Rams

Rams' ten principles read as a description of a bag tag written before anyone thought to look at one:

| Rams | On the tag |
|---|---|
| Useful | Every zone is a routing, claim, or audit job |
| Understandable | A handler with no training sorts correctly in one glance |
| Unobtrusive | It is silent about everything that is not the bag |
| **Honest** | It never claims more than it knows. No confidence it has not earned |
| Long-lasting | Freezer-grade adhesive, synthetic substrate — *durability is information* |
| **Thorough to the last detail** | The barcode prints twice, offset 90°, because belts are three-dimensional |
| As little design as possible | There is none. Not a restrained amount — none |

"Thorough to the last detail" is the one to sit with. The second barcode at 90° is not a flourish. Someone worked out that a conveyor is a 3D environment, that a bag lands in an unplanned orientation, and that a scanner reading one axis will miss. The fix costs nothing at print time and saves bags forever.

**That is the standard.** Not "did I remove enough?" but "did I find the failure mode nobody had looked for, and close it for free?"

## 4. Where the tag goes further than either

Rams and Vignelli both produced objects that could be admired. The tag cannot be admired — it is thrown away in a day, and its whole design budget went into being read once, correctly, by a tired person.

Three properties follow, and none of them are in the Rams or Vignelli canon:

**Dual encoding as a survival rule.** Human type *and* machine key, always both, and the new layer never deletes the old until every reader in the journey can read it. RFID did not remove the printed barcode. That is not conservatism; it is the recognition that a network upgrades unevenly and the weakest reader sets the floor.

**Graceful degradation as a design layer.** The passenger name exists so the object survives total system failure. Most interfaces have no plan for their own database being wrong. The tag's fallback rank is a designed answer to "what if everything else fails."

**Lifecycle as a visible domain.** Substrate, adhesive, reuse, recycle path. Not a sustainability badge — the actual material decision, stated, because it determines whether the object is still readable in Helsinki in February.

## 5. What this system takes from the other two cores

The tag is complete about the object. It is silent about three things the other cores learned the hard way.

### Registers — the tag aesthetic is not universal

Axiom's most expensive lesson: *the Core described one register while claiming to be universal, which is why non-console surfaces kept fighting it.*

This system risks the same error. The tag is a **high-pressure, low-dwell, machine-adjacent** object. Applied to a long essay it produces something unreadable; applied to a citizen service in sunlight it produces something cold; applied to a ministry deck it produces something that looks like a receipt.

Pick a register before applying anything here. See [`registers.md`](registers.md).

### Planar alignment — the law the tag obeys silently

Rams × NYCTA states it: **every edge resolves to another edge.** Nothing floats. The grid is invisible because everything snaps to it.

A real tag obeys this completely — it is printed by a machine on a fixed face, so every zone boundary is shared by construction. A digital imitation does not get that for free, and a tag layout with one edge landing 11px short of its neighbour reads as *accident*, which is the one thing the object never reads as. See [`grid.md`](grid.md).

### The Divergence Protocol — how to break a rule without drifting

A rule here may be broken when **all three** hold. Two out of three is drift:

1. **Named.** The deviation is explicit, written as an override — not inherited from a template default.
2. **Load-bearing.** It carries information the compliant version cannot carry.
3. **Written down.** One line in the project's own `context.md` or `README` stating what was broken and what it buys.

Fails any one → it is not a considered exception, it is a regression. Revert it.

**PO Completeness itself is not subject to this protocol.** It has no exception path.

## 6. The one-line version

> Rams shows what restraint looks like when a designer chooses it.
> Vignelli shows what a closed symbol system does for a stranger in a hurry.
> The tag shows what is left when four billion hostile events a year remove everything that was not load-bearing.

Copy the third one when the surface has a job and a deadline. Copy the first two when it has a reader and a room.
