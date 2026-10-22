---
id: AS-006
title: Churchill release map v2
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: Built-in ImageGen; Python ReportLab composition; PyMuPDF and Poppler verification
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-map/Churchill_Map_v2_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: [long-way-home]
---

Created 2026-10-22 at the designer's request. Supersedes AS-005, whose source and output files remain unchanged.

Hand-drawn illustrated terrain: textured blue bay and inlet, connected gravel streets and detailed buildings, dark gravel dump with rusty scrap and tires, and moss/lichen tundra with rocks and small enclosed ponds. This is a fictional schematic landscape, not a geographically accurate map of Churchill.

## Files
- `assets/churchill-map/Churchill_Map_v2.pdf`: print master, 7 x 5 in trim, 0.125 in bleed on every side; page 7.25 x 5.25 in, with explicit TrimBox and BleedBox. Print at 100% / actual size.
- `assets/churchill-map/Churchill_Map_v2.svg`: full-bleed companion, with embedded raster illustrations and vector grid/text outlines.
- `assets/churchill-map/Churchill_Map_v2_Preview.png`: trimmed 300 dpi preview.
- `assets/churchill-map/Churchill_Map_v2_Bleed_Preview.png`: independent Poppler render including bleed.
- `assets/churchill-map/Churchill_Map_v2_Terrain_Atlas.png` and `Churchill_Map_v2_Tundra_Atlas.png`: saved generated art inputs.
- `source/build_churchill_map_v2.py`: repeatable composition and validation; imports the original v1 drawing furniture and uniqueness checker.
- `assets/churchill-map/Churchill_Map_v2_Validation.json`: grid, per-cell art placements, print measurements, unique-solution result and preserved-file checks.
- `assets/churchill-map/README_v2.md`: rebuild and printing notes.

## Preserved and checked
- Exact v1 5-row by 6-column GRID and 0.82 in square size. Each cell is clipped separately to one terrain; shore and town boundaries follow grid lines.
- No square labels; original north arrow, legend entries, title and subtitle retained. Legend swatches match the new illustrations. The Hudson Bay label is spaced around the centre grid line.
- The original v1 `check_unique()` was run against the v2 GRID: **exactly one solution**, unchanged. No puzzle rules or answers changed; PP-002 and PZ-009 are byte-for-byte unchanged.
- PDF page boxes verified; final page rendered independently with Poppler and screen-reviewed. No physical print or player playtest performed. PZ-009 remains untested.
- Title wording and Helvetica font remain the v1 placeholders; no new choice made about them or the puzzle's answer format.

## Exact generation prompts
Built-in ImageGen used for two illustration atlases. Full prompts, verbatim, are saved in `source/churchill_map_v2_prompts.md`. The first atlas was the style reference for the second. The script controls geometry and all text; generated imagery cannot change the grid or rules.
