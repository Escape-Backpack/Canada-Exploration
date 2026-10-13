# Handoff

## 2026-10-05: documentation closeout (Codex)
- **Status:** Requested document synchronization completed; chat ready to archive. Current AS-003/004 and PP-001 remain the design source of truth. The sibling EscapeBackpack/index.html now links Canada v2 and its corrected-leaf comparison. Superseded AS-001 points to preserved README_v1.md.
- **Checks:** Document links and active records checked; root index and both Aurora guide sections reviewed over local HTTP; all 29 new section links/images return 200; images load, identity appears in print content, and no browser console warnings/errors. Earlier digital geometry checks still apply; no physical print or actual printer-profile slice.
- **Next:** Print the thin back trial with the intended printer/material and inspect S/B/K, then test the full medallion. No commit, push or publication.


## 2026-10-05: maple leaf corrected in medallion v2 (Codex)
- **Requested:** Designer said the first maple leaf looked wrong.
- **Changed:** Replaced it with the existing maple-leaf SVG outline; train, tracks and rim retained exactly. New AS-003 model and AS-004 preview supersede AS-001/002. PP-001 references current model.
- **Files:** v2 one-piece STL, thin trial, SVGs/preview, measured reports, sources, notes and ZIP under assets/medallion. v1 outputs and README preserved.
- **Checks:** Both v2 meshes pass closure, winding, connectivity, non-degenerate facets and volume; back matches approved Space SVG. CAD reports zero profile change outside the leaf region. Preview reviewed; ZIP integrity and record validation pass. No actual printer-profile slice or physical print.
- **Next:** Print thin back trial with intended printer/material, then the full two-colour medallion. No commit, push or publication.


## 2026-10-05: themed medallion built (Codex)
- **Worked on:** PP-001, AS-001 and AS-002, after the designer requested medallions for Aurora, Hockey and Canada and selected the proposed motifs.
- **Selected:** maple leaf and train, navy/yellow, with the improved shared back. The physical prop is not marked built/tested; final release/container remain unassigned.
- **Created:** Full one-piece STL, matching 1.2 mm back trial, exact SVG profiles/PNG preview, reports, self-contained sources, README and ZIP under `assets/medallion/`.
- **Method:** Vector CAD for maple leaf and train; no ImageGen used.
- **Checks:** Both meshes pass closure, winding, one-solid connectivity, non-degenerate facets and volume checks; preview screen-reviewed; shared back SVG matches Space exactly; ZIP integrity and record validation pass. No printer-profile slice or physical test.
- **Next step:** Print the full-size thin back trial using the actual printer/material and inspect S/B/K, then test the full two-colour medallion.


Update at the end of every session. Newest entry on top. Refer to records by ID.

## 2026-10-03: NT and NU reveal puzzles
- **Worked on:** the two territory puzzles that use a reveal prop.
- **Ideas recorded (status idea, nothing decided):** PZ-001 (NT: red acetate reveals a puzzle, rebus/icons, needs a second prop to decode; aurora clue), PZ-002 (NU: UV pen reveals the code jumbled, a second prop reorders it; long winter + "special lights" clue). Both set to a 4-digit lock.
- **Open, not yet recorded as questions:** the second prop for each; where the UV pen and light are found; the exact clue wording so players try the tool; test the paper under UV.
- **Not committed.**
- **Next step:** pick the second prop for PZ-001 or PZ-002.

## 2026-10-03: external mockup added
- **Worked on:** added `the-long-way-home.html`, a playable browser mockup made with another AI model.
- **Not decisions:** it differs from the records (single 19-year-old traveller in 1967, not the parents;
  2-digit passport cells and one 3-digit final lock instead of the Q-001 split; its own set of facts).
  Treat it as a source of puzzle ideas only. Nothing in it has been written into records.
- **Next step:** unchanged (Q-004 or Q-003); optionally mine the mockup for candidate puzzles.

## 2026-09-30: lock types
- **Worked on:** brainstorm of the Canada backpack; lock weights.
- **Answered:** Q-001 (keep the four defaults: 6x 3-digit, 4x colour, 3x 4-digit, 2x 4-letter; locks numbered 1-15).
- **Idea, not yet recorded:** meta-puzzle for the final locks (Q-003). Postcards were rejected to stay different from Norse.
- **Answered also:** Q-005 (retired parents are the sender; PR-001 still a candidate).
- **Decided:** PR-005 (parents' travel backpack), PR-006 (travel-book pages + souvenirs/facts), PR-007 (playful tone), PR-008 (chronological, congratulation notes).
- **Answered:** Q-006.
- **Idea, not yet recorded:** map + ruler distance puzzle (3-digit lock).
- **Drafted:** Q-004 now has a 13-row candidate list (unverified), still open.
- **Next step:** verify the facts and confirm the route order (Q-004), or Q-003 (final locks).

## 2026-09-30: project set up from the seed
- **Worked on:** repo created; seed notes from backpack-kit/seeds/canada.md turned into records.
- **Decided:** PR-003 (15 locks: one per province/territory plus two final; a different puzzle type per stop).
- **Candidates:** PR-001 (a relative who travelled everywhere), PR-002 (learn obscure facts), PR-004 (medallion + train invitation).
- **New open questions:** Q-001 to Q-006.
- **Next step:** Q-001 (lock types), or Q-004 (a fact per province/territory).

## YYYY-MM-DD: <piece worked on>
- **Worked on:**
- **Decided:** (IDs whose status changed to decided or built)
- **New open questions:** (Q- IDs)
- **Next step:**
