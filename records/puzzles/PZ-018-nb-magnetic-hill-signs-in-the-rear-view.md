---
id: PZ-018
title: NB: Magnetic Hill signs in the rear-view mirror
type: puzzle
# idea | candidate | decided | built | parked
status: idea
# The structure beat this puzzle belongs to (one ID)
beat:
# Props the player needs, e.g. [PP-001]
props: [PP-006]
# Puzzles that must be solved first, e.g. [PZ-002]
needs: []
# cipher | physical | search | logic | wordplay | other
mechanic: logic
# 1 (easy) to 3 (hard)
difficulty:
# 4-5 characters the cipher can encode (see backpack.json). The envelope it opens is marked
# with the matching symbols; props with envelope: <this ID> go inside.
answer:
# What players call this puzzle on the hint page, e.g. "The luggage tag" (spoiler-free)
hint_title:
# Explicit opt-in for the PUBLIC hint page. Candidates are never published.
publish_hints: no
# Independent of design/build status: untested | passed | changes-needed
test_status: untested
# physical | digital (a digital walkthrough does not verify a physical prop)
test_method:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [Q-003, Q-008]
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: [long-way-home]
---

## How it works
Idea, designer's direction (2026-10-22). Replaces PZ-005 (mockup's reversed-bearings version).

**Real fact:** Magnetic Hill (Moncton) is an optical illusion. You drive to the bottom, shift into neutral, and the car rolls backwards, apparently uphill; the road actually slopes gently downhill. Checked against Wikipedia, Atlas Obscura and CTV (2026-10-22). The mockup's "white post" was not confirmed; sources disagree on paved vs gravel.

**Designer's direction (2026-10-22, second version):**
- **Postcard:** talks about Magnetic Hill and what the parents did, and gives "right before / right after" clues about landmarks. The quirky roadside attraction goes on the postcard's back (art side), see Q-003; keep the roadside theme out of the puzzle itself.
- **Map:** the hill road with landmarks only (farm, intersection, pond, lookout), drawn in driving order (arrows down to the bottom). No signs: players place them.
- **Hand-drawn mirrored sketches:** the 4 road signs seen in the rear-view mirror while rolling backwards, in shuffled order. Some sketches show a landmark too.
- **Magnetic Hill matters:** going the wrong direction gives a different order, not just the reverse. (First version had the signs on the map, so only two orders were possible; designer rejected it.)

**Signs (designer chose 4, one without a number, generic donut shop, MAXIMUM wording):** Steep hill 9%, Next donut shop 3 km, Moose crossing (no number), MAXIMUM 20 km/h.

**Clue logic (agreed 2026-10-22; clue wording still to write):** "before/after" depend on travel direction. Rolling backwards up the hill, the rear-view mirror shows where the car is going, so a landmark seen behind a sign in the mirror comes right after that sign.
| Sign | Clue | Rolling up (correct) | Driving down (trap) |
|---|---|---|---|
| Steep hill 9% | right before the farm | below the farm | above the farm |
| Next donut shop 3 km | right after the farm | farm-intersection | below the farm |
| Moose crossing | mirror sketch: pond just beyond the sign | intersection-pond | pond-lookout |
| MAXIMUM 20 km/h | right after the pond | pond-lookout | intersection-pond |

- Correct, bottom to top: 9 · 3 · moose · 20 = 9320.
- Wrong direction, read in driving order: 2093. Half-right mixes: 2039 and 3920.
- The intersection separates the farm pair from the pond pair; the lookout is a decoy at the top.
- Optional confirmation or hint: "the second sign we passed gave us cravings for donuts".

**Paper mockups:** v1 (signs on the map, rejected) and v2 (landmarks only, moose sketch shows the pond) in `assets/magnetic-hill/`, built by `source/build_magnetic_hill_v1.py` / `_v2.py`. Not paper-tested. No postcard text and no sketch-card header yet (designer's wording).

**Open:**
- Answer (4-5 digits; the shapes cipher encodes digits only). 9320 is the example, not chosen.
- Postcard wording with the 3 clues (designer writes it).
- "Steep hill 9%" is fiction on a gentle real slope (fine as a joke, or soften). The landmarks are generic, not the real site's.

## Clue wording

## Hints
1.

## Solution

## Playtest evidence
<!-- Add dated observations only after a test: version/files tested, physical or
digital, what the player tried, where they stalled, hints used, interpretation,
change made and retest result. After a relevant edit, mark untested again. -->
