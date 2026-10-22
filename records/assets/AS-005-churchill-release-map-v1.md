---
id: AS-005
title: Churchill release map v1
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: Python (reportlab vector drawing, PyMuPDF for SVG/PNG)
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-map/Churchill_Map_v1_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-006
tags: [long-way-home]
---

Not generated from a prompt: drawn as vector art by `source/build_churchill_map_v1.py` (2026-10-22).

Files in `assets/churchill-map/`: `Churchill_Map_v1.pdf` (print), `Churchill_Map_v1.svg`, `Churchill_Map_v1_Preview.png` (150 dpi).

- 7 x 5 in landscape, trim size, **no bleed** yet. Squares 0.82 in (for 0.75 in tokens, PP-005).
- Grid: the mockup's 5 rows x 6 columns, as chosen by the designer. Row 1 bay; town on the west (5 squares); bay inlet in row 2, columns 3-4; old dump at row 4, column 5.
- No square labels (designer: wait for PZ-009's answer format).
- North arrow and a legend (Hudson Bay, Town, Old dump, Open tundra) for rules 1, 4 and 5.
- The build script checks the 6 rules from PP-002 and stops unless there is exactly one solution. v1 result (row, column, counted from the north-west): mother and cub 5,5; old male 2,6; young male 3,4.
- Placeholder wording and font, not chosen by the designer: title "Churchill, Manitoba", subtitle "Polar bear release map", Helvetica labels.
- Screen-reviewed preview only. Not printed or paper-tested.
