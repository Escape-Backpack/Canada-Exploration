---
id: AS-003
title: Canada medallion printable model v2
type: asset
status: built
kind: print
for: PP-001
tool: Python vector CAD and reference tracing
file: assets/medallion/STL/Canada_Medallion_OnePiece_v2.stl
links: [PR-004]
superseded_by:
tags: []
---
## Revision
Requested 2026-10-05. Replaces the first stylised maple leaf with the existing maple-leaf SVG outline, preserving its recognisable pointed lobes and curved notches. CAD verifies zero change outside the leaf region; the train, tracks and rim remain from v1.
Supersedes AS-001; v1 files are retained. This is a built digital asset,
not a confirmed physical print. No ImageGen was used.

The approved shared back is unchanged and byte-identical to the Space back SVG.
50 mm diameter, 3.8 mm body + 0.6 mm relief = 4.4 mm; 0.4 mm back engraving.
Main words: 4.6 mm Arial Bold capitals; brand: 4.0 mm Arial Regular capitals.
Minimum adjacent brand-letter gap: 0.831 mm.

## Files
- Print ZIP: `assets/medallion/Canada_Medallion_Print_Files_v2.zip`.
- Thin back trial: `assets/medallion/STL/Canada_Back_Lettering_Test_1.2mm_v2.stl`.
- Print notes: `assets/medallion/README_v2.md`.
- Exact front/back SVG profiles and JSON geometry/mesh reports are in the same directory.
- Rebuild: `python source/build_medallion_v2.py`.
- Front source: `source/revised_medallion_fronts_v2.py`.
- Leaf reference: `assets/medallion/sources/Maple_Leaf_Reference.svg`.

## Validation
Full STL and thin trial pass closed-edge, winding, one-solid connectivity,
non-degenerate facets and volume checks. Polygon and mesh volumes agree.
Preview visually reviewed; ZIP integrity checked. No actual printer-profile
slice or physical printing was done. Print the thin trial first to inspect
S/B/K, back DOWN, using the actual printer/filament and full scale.
