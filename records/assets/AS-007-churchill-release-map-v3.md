---
id: AS-007
title: Churchill release map v3
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
file: assets/churchill-map/Churchill_Map_v3_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [PZ-009, PP-002, PP-005]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by: AS-008
tags: [long-way-home]
---

Created 2026-10-22. Supersedes AS-006 after the designer rejected the textured illustrated style and requested a fresh start from AS-005: a simple functional map suitable for an officer's office, resembling the visual simplicity of a default street-map background.

Flat colours, simple building footprints and white streets, pale blue water, pale green tundra, and a muted hatched dump area. No generated imagery, satellite imagery or v2 artwork. Original v1 GRID preserved; terrain boundaries follow it closely with small bends, as explicitly permitted by the designer. The geography remains fictional/schematic.

## Files
- `assets/churchill-map/Churchill_Map_v3.pdf`: vector print master; 7 x 5 in trim, 0.125 in bleed per edge, 7.25 x 5.25 in page. Print at actual size.
- `assets/churchill-map/Churchill_Map_v3.svg`: vector companion, including bleed.
- `assets/churchill-map/Churchill_Map_v3_Preview.png`: 200 dpi trimmed preview.
- `assets/churchill-map/Churchill_Map_v3_Bleed_Preview.png`: independent Poppler render.
- `assets/churchill-map/Churchill_Map_v3_Validation.json`: geometry, print and uniqueness checks.
- `source/build_churchill_map_v3.py`: complete editable vector source; imports only v1.

## Checks
- Original v1 uniqueness function run against v3 GRID: exactly one solution, unchanged.
- All 30 cell interiors checked against their assigned terrain on a separate semantic render. Small deviations near cell boundaries are intentional.
- Original 0.82 in squares, no square labels, north arrow and four-entry legend retained. Title/subtitle and Helvetica remain provisional as in v1.
- PDF TrimBox/BleedBox and absence of raster images verified. Poppler render screen-reviewed.
- v1 script and PP-002/PZ-009 records verified unchanged by SHA-256. No rules or answers changed.
- No physical print or player playtest. Built is not tested or designer-approved artwork.

Rebuild from the project folder: `python source/build_churchill_map_v3.py`. No image generation or prompts used for this version.
