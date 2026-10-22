---
id: AS-008
title: Churchill release map v4
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-004
# Generator or tool used
tool: Python ReportLab vector drawing; PyMuPDF and Poppler verification
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-map/Churchill_Map_v4_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-009
tags: [long-way-home]
---

Created 2026-10-22. Supersedes AS-007 after the designer requested a little more detail while retaining the clean office/street-map style.

Adds restrained vector detail: pale shoreline bands and sparse water lines; muted roof colours, ridges, small annexes and forecourts; moss patches, sparse stones/grass and three small enclosed tundra ponds; gravel marks, metal stacks, timbers and tires at the dump. Flat colours and open space remain dominant. No photographic textures or generated imagery.

## Files
- `assets/churchill-map/Churchill_Map_v4.pdf`: vector print master, 7 x 5 in trim plus 0.125 in bleed on each side; print at actual size.
- `assets/churchill-map/Churchill_Map_v4.svg`: vector companion including bleed.
- `assets/churchill-map/Churchill_Map_v4_Preview.png`: 200 dpi trimmed preview.
- `assets/churchill-map/Churchill_Map_v4_Bleed_Preview.png`: independent Poppler render.
- `assets/churchill-map/Churchill_Map_v4_Validation.json`: print, terrain and uniqueness checks.
- `source/build_churchill_map_v4.py`: editable vector detail/composition, importing the v3 base and original v1 checker.

## Preserved and checked
- Exact v1 GRID, unchanged v3 terrain boundaries and street layout. Terrain edges still follow grid lines closely with small bends.
- 0.82 in squares, no square labels, north arrow, legend and provisional title/font preserved.
- Original v1 uniqueness checker run on v4 GRID: exactly one solution, unchanged. PP-002 and v1 source hashes unchanged. This map task did not edit PZ-009; a concurrent designer update added only its zone-number-format note, verified and preserved. Numbers and bear order remain open, so v4 is still unnumbered.
- All 30 cell interiors verified on the unchanged semantic terrain render; small enclosed ponds are decorative tundra features, not additional Hudson Bay cells.
- TrimBox/BleedBox and absence of raster images verified. Final Poppler render screen-reviewed.
- No physical print or player playtest; this does not mark the artwork designer-approved.

Rebuild from the project folder: `python source/build_churchill_map_v4.py`. No image-generation prompts used.
