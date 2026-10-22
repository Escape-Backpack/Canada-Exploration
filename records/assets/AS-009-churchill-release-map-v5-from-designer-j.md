---
id: AS-009
title: Churchill release map v5 from designer JSON
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
file: assets/churchill-map/Churchill_Map_v5_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: [long-way-home]
---

Created 2026-10-22 from the designer's supplied JSON drawing. Supersedes AS-008, whose visual direction the designer found too childish. This version applies restrained street-map styling directly to the designer's geometry.

## Direction and method
- User's JSON is the layout source, preserved verbatim as `assets/churchill-map/Churchill_Map_v5_Source.json`.
- Uncovered land is open tundra. Muted solid terrain fills, white local streets, pale yellow main road, blue rivers and understated POI symbols; no added scenery, building layout, playful decoration or invented place names.
- Polygon positions and smoothing flags are preserved. Beaches and rocky shore are drawn below water, so submerged overlap is hidden and land-side strips remain. Rivers join the water underneath its fill; road/river crossing receives small bridge parapets.
- The exact duplicate port entry remains in the source JSON but renders once. All 11 unique place-marker types have a legend entry, including the JSON's `beariail` kind shown as Bear jail.

## Files
- `assets/churchill-map/Churchill_Map_v5.pdf`: vector print master, 7 x 5 in trim, 0.125 in bleed per edge. Print at actual size.
- `assets/churchill-map/Churchill_Map_v5.svg`: editable vector companion.
- `assets/churchill-map/Churchill_Map_v5_Preview.png`: 200 dpi trim preview.
- `assets/churchill-map/Churchill_Map_v5_Bleed_Preview.png`: independent Poppler render.
- `assets/churchill-map/Churchill_Map_v5_Source.json`: unmodified designer drawing; compatible with the existing map designer.
- `assets/churchill-map/Churchill_Map_v5_Validation.json`: source hash, feature counts, terrain sampling and original uniqueness result.
- `source/build_churchill_map_v5.py`: renderer and checks. Rebuild with `python source/build_churchill_map_v5.py`.

## Checks and limitations
- Original 5 x 6 logical grid, 0.82 in square size, north arrow, title/subtitle and no zone numbers retained.
- The dominant base terrain in each square matches v1 (20 x 20 samples per cell on the rendered smoothed polygons). Shore strips, roads, rivers and markers are map details, not additional whole-cell terrain assignments.
- Original v1 uniqueness checker: exactly one unchanged solution. No rules or answers edited.
- PDF print boxes, vector content and complete place legend checked; final Poppler render screen-reviewed.
- No physical print or player playtest; visual approval remains with the designer. Zone values and bear order remain open.

No image generation used; no generation prompt.
