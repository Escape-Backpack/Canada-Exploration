---
id: PZ-009
title: MB: Churchill polar bear jail release map
type: puzzle
# idea | candidate | decided | built | parked
status: idea
# The structure beat this puzzle belongs to (one ID)
beat:
# Props the player needs, e.g. [PP-001]
props: [PP-002, PP-004, PP-005]
# Puzzles that must be solved first, e.g. [PZ-002]
needs: []
# cipher | physical | search | logic | wordplay | other
mechanic: logic
# 1 (easy) to 3 (hard)
difficulty:
# 4-5 characters the cipher can encode (see backpack.json). The envelope it opens is marked
# with the matching symbols; props with envelope: <this ID> go inside.
answer: 7329
# What players call this puzzle on the hint page, e.g. "The luggage tag" (spoiler-free)
hint_title:
# Explicit opt-in for the PUBLIC hint page. Candidates are never published.
publish_hints: no
# Independent of design/build status: untested | passed | changes-needed
test_status: untested
# physical | digital (a digital walkthrough does not verify a physical prop)
test_method:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [Q-004, Q-008]
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: [long-way-home]
---

## How it works
Idea only, nothing decided (2026-10-22). Source: *The Long Way Home* mockup (`the-long-way-home.html`, external, see HANDOFF 2026-10-03). Numbers below are the mockup's values, not envelope answers: envelope answers must be 4-5 characters.
- Logic placement on a Churchill map (5x6 grid: bay, town, old dump, tundra). Three bears go out of the holding facility ("polar bear jail"): mother and cub, young male, old male.
- Six release rules: all on tundra; no two bears in touching squares (diagonals count); mother and cub at least 3 squares from town; old male on the shore; old male east of the mother; young male next to the dump.
- Mockup answer: 29 (old male's square). Checked by brute force on 2026-10-22: the mockup grid has exactly one solution (mother 73, old male 29, young male 32 in its square labels).
- **Designer idea (2026-10-22):** a postcard mentions visiting Churchill and seeing the polar bear jail, and the officials needing to move those 3 bears/pairs to different areas. A map goes with it.
- Q-004 draft lists the Narcisse snake dens for MB instead.
- **Designer choices (2026-10-22):** the postcard (PP-002) tells the story and carries the 6 rules (the separate notice card PP-003 was parked the same day); a Churchill map (PP-004); 3 cardboard bear tokens (PP-005).
- **Open:** answer format (envelope answers are 4-5 characters; the mockup gives 2 digits). Designer: decide later, once the grid is final. Option raised: read two bears' squares as 4 digits, which the postcard or rules would need to point to.
- **Paper test watch (2026-10-22):** do players treat the east riverbank as "shore" for rule 4? See PP-004; the designer keeps the river for now.
- **Answer format (designer, 2026-10-22): zone numbers.** Each square gets a printed 2-digit release-zone number; the answer is two bears' zones read in order (4 digits). The postcard line pointing to them is in PP-002; the numbers are on the map (AS-014).
- **Zone numbers (designer, 2026-10-22): the mockup's set.** Row 1 is the bay (north), column 1 the west:

  | Row | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
  |---|---|---|---|---|---|---|
  | 1 | 71 | 52 | 38 | 90 | 47 | 15 |
  | 2 | 63 | 84 | 26 | 11 | 58 | 29 |
  | 3 | 44 | 17 | 95 | 32 | 76 | 60 |
  | 4 | 23 | 69 | 81 | 54 | 12 | 87 |
  | 5 | 35 | 98 | 41 | 66 | 73 | 20 |

  Solution zones: mother and cub 73, old male 29, young male 32. Answer **7329** = mother's zone, then the old male's (the order Claude proposed with the mockup numbers; designer chose that option). If a player counts the east riverbank as shore, the old male could be read as zone 60, giving 7360 (see PP-004).

## Clue wording

## Hints
1.

## Solution

## Playtest evidence
<!-- Add dated observations only after a test: version/files tested, physical or
digital, what the player tried, where they stalled, hints used, interpretation,
change made and retest result. After a relevant edit, mark untested again. -->
