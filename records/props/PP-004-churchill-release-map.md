---
id: PP-004
title: Churchill release map
type: prop
# idea | candidate | decided | built | parked
status: idea
# physical | printed | digital
form: printed
# make | buy | print | 3d-print
source: print
# Where the player finds it: start (loose in the box) or the puzzle whose answer opens its envelope, e.g. PZ-004
envelope:
# On the public reset page: return (back in its envelope) | keep (the team takes it home) | none (not mentioned). Blank = return.
after_game:
# Name on the public reset page, if the title isn't what players call it (optional)
reset_name:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It is then hidden unless the board's "parked" filter is on.
superseded_by:
tags: [long-way-home]
---

Idea (2026-10-22, designer). A map of Churchill for PZ-009, split into a grid of squares: Hudson Bay, town, old dump and open tundra. North up, bay along the top.
**Designer choices (2026-10-22):** the mockup's 5x6 grid as is; 7 x 5 in card; no square labels until PZ-009's answer format is chosen. Current map: AS-010, from the designer's revised JSON drawing, with 0.125 in bleed and unchanged 0.82 in squares. Designer requested restrained Google Maps background styling, with uncovered land as open tundra and sensible blending of overlapping shore/water areas. V6 uses more distinctive green tundra and grey town colours. Terrain boundaries should follow the grid closely, but need not follow it exactly. The earlier textured and decorative visual directions were rejected.
**Map designer tool (2026-10-22, Claude, on the designer's request):** `source/Churchill_Map_Designer.html`, modelled on Norse's Aud Map Designer. The designer draws the map by hand over the fixed puzzle grid: areas (tundra, town, dump, water), lines (road, street, alley, footpath, river, railway), map markers and building footprints sized so about 8 buildings and 2 streets fit in one town square. It checks that every square still reads as its puzzle terrain, and exports SVG, JSON or a 7.25 x 5.25 in print/PDF with bleed. Open it over local HTTP (launch config `canada-static`). No drawing made yet.
Open: square labels; title wording and map font; card stock; which envelope it comes in.

## Player sees
<!-- Shown on the play-test page when the prop has no image file. -->

## Reset
<!-- Optional: how to put it back, e.g. "Fold along the creases". Shown on the public reset page. -->
