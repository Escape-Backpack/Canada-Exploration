---
id: AS-015
title: Churchill postcard text side v1
type: asset
# idea | candidate | decided | built | parked
status: built
# image | audio | text | print
kind: print
# The prop this asset is for (one ID)
for: PP-002
# Generator or tool used
tool: Python: source/build_churchill_postcard_back_v1.py (reportlab, Indie Flower)
# Path from the project folder once made, e.g. assets/star-chart.png
file: assets/churchill-postcard/Churchill_Postcard_Back_v1_Preview.png
# Any related record IDs, e.g. [PZ-002, Q-004]
links: [AS-012, PZ-009]
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: [long-way-home]
---

Not generated from a prompt. Built 2026-10-22 by `source/build_churchill_postcard_back_v1.py`. The text side of the postcard; the art side is AS-012.

- 6 x 4 in trim plus 0.125 in bleed; open text side as the designer specified (no address, no Fun Fact box).
- Text is read straight from PP-002's **Text** block at build time, so the card matches the record word for word (rebuild after any text edit).
- Indie Flower in blue-black on the art side's paper colour, 0.3 in margins, 1.3 line spacing, hanging indent on the numbered rules, half-line gap before the signature.
- Fits at **10.75 pt** (17 lines): the blank line before "Mom & Dad" costs a quarter point against the 11 pt measured earlier.

## Files
- `assets/churchill-postcard/Churchill_Postcard_Back_v1.pdf` (print), `Churchill_Postcard_Back_v1_Preview.png` (200 dpi, trimmed).

## Verification
Every paragraph of the record text checked against the PDF's text. Screen-reviewed preview only; not printed or paper-tested.
