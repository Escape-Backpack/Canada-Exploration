---
id: Q-007
title: What changes now that this adventure uses envelopes instead of locks?
type: question
# open | answered | parked
status: open
# Records this question is about, e.g. [PZ-003]
about: [PZ-001, PZ-002]
# Leave empty while open
answer:
# Any related record IDs, e.g. [PZ-002, Q-004]
links: []
# Set to an ID when this record is replaced. It then moves to the Parked tab.
superseded_by:
tags: []
---

On 2026-10-12 the designer moved every adventure from locks in a backpack to marked envelopes in a board-game box, with one lookup cipher per adventure. The migration only moved fields: found_in became envelope (same values), and lock/container values went into each record's "Lock-version notes" section. These points still describe the lock version and need a decision:

- **PZ-001 and PZ-002** were designed for 4-digit locks and have no answer yet. Their answers become envelope codes.
- **Premise records** that mention the backpack as the container.
- **Cipher**: backpack.json uses the kit's plain `shapes` preset (digits 0-9) and 2 decoy envelopes as a placeholder. Not chosen by the designer. Each adventure should get its own look (Space uses planets).
