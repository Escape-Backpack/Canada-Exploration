---
id: AS-010
title: Churchill release map v6 revised layout and colours
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: Python vector SVG renderer, svglib/ReportLab PDF, PyMuPDF and Poppler verification
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-map/Churchill_Map_v6_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: [long-way-home]
---

Created 2026-10-22 from the designer's revised JSON. Supersedes AS-009. The designer requested more distinctive colours between tundra and town while retaining v5's restrained street-map style.

- Tundra is sage green (`#c8dcb9`); town is neutral grey (`#deddd9`). Legend swatches use the same colours.
- Revised source adds the dump access loop, two parking areas, shed, connecting alley and long footpath. All supplied positions, dimensions and smoothing flags are retained; uncovered land is tundra.
- Shore/water blending and the complete POI legend follow v5. Footpath is a fine brown dashed line and is included in the legend. Parking areas have simple white bay lines; the shed is a small neutral footprint. No new map features invented.
- Exact duplicate port renders once; both entries remain in the source JSON.

## Files
- `assets/churchill-map/Churchill_Map_v6.pdf`: vector print master, 7 x 5 in trim plus 0.125 in bleed on all sides; print at actual size.
- `assets/churchill-map/Churchill_Map_v6.svg`: editable vector companion.
- `assets/churchill-map/Churchill_Map_v6_Preview.png`: 200 dpi trimmed preview.
- `assets/churchill-map/Churchill_Map_v6_Bleed_Preview.png`: independent Poppler render.
- `assets/churchill-map/Churchill_Map_v6_Source.json`: revised designer JSON, preserved verbatim.
- `assets/churchill-map/Churchill_Map_v6_Validation.json`: source hash, features, terrain checks and uniqueness result.
- `source/build_churchill_map_v6.py`: self-contained versioned renderer; imports v1 for the original grid/checker. Rebuild with `python source/build_churchill_map_v6.py`.

## Verification
All 30 dominant base terrain assignments match the original 5 x 6 grid. Original uniqueness checker returns exactly one unchanged solution. No rules or answers edited. Grid squares remain 0.82 in; PDF TrimBox/BleedBox, vector content and legend checked. Final Poppler render screen-reviewed. No physical print or player playtest; zone numbers remain unassigned.

No image generation or prompts used.
