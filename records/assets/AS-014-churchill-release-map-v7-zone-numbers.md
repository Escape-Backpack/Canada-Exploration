---
id: AS-014
title: Churchill release map v7 (zone numbers)
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: Python: source/build_churchill_map_v7.py on top of the v6 renderer
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-map/Churchill_Map_v7_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, AS-010]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: [long-way-home]
---

Not generated from a prompt. Built 2026-10-22 by `source/build_churchill_map_v7.py`, which reuses the v6 renderer and checks unchanged. Supersedes AS-010.

Changes from v6, both requested by the designer:
- **Zone numbers:** every square has its 2-digit zone number (PZ-009's table) in a small white chip in the top-right corner: 9.6 x 7.2 pt, 1.4 pt inset, bold Helvetica 5.6 pt.
- **Fire station badge** moved 5.2 pt west (x 139.5 to 134.3) in row 3, column 2, just enough to clear that square's chip. `Churchill_Map_v7_Source.json` is the v6 drawing with only this change.

## Files
- `assets/churchill-map/Churchill_Map_v7.pdf`: vector print master, 7 x 5 in trim plus 0.125 in bleed.
- `assets/churchill-map/Churchill_Map_v7.svg`, `Churchill_Map_v7_Preview.png` (200 dpi, trimmed).
- `assets/churchill-map/Churchill_Map_v7_Source.json`, `Churchill_Map_v7_Validation.json`.

## Verification
- All 30 dominant terrains match the puzzle grid; the original checker gives exactly one solution.
- The zones on the solution squares are 73 (mother and cub), 29 (old male) and 32 (young male), so the map gives PZ-009's answer 7329.
- Every chip stays outside a 0.75 in token centred in its square, and no place badge touches a chip. All 30 numbers are present as text in the PDF.
- Known overlap: chip 12 (row 4, column 5) sits on the corner of the dump's parking lot; the number stays readable.
- Screen-reviewed preview only. Not printed or paper-tested.
