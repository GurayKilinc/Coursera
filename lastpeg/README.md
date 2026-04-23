# LastPeg — Zen Peg Solitaire (Prototype)

Browser-based MVP of the **LastPeg** concept from the approved plan: a premium
zen reinterpretation of the 340-year-old French court puzzle *Peg Solitaire*,
styled with moonlight + glass orb aesthetics, aimed at US / Japan / Germany-UK
/ South Korea premium casual audiences.

This is a **Week 1-2 MVP** prototype — plain HTML/CSS/JS, single file, runs in
any mobile browser. No Unity dependency yet; the purpose is to validate the
**core game feel** before committing to full Unity production.

## How to Run

Just open `index.html` in any modern browser:

```
open index.html
```

Or serve locally:

```
cd lastpeg
python3 -m http.server 8000
# visit http://localhost:8000
```

Works on mobile: open the file via any static host (GitHub Pages, Netlify,
`python -m http.server`) and visit on a phone.

## How to Play

- **Tap a glass orb** — it highlights, and valid jump targets glow gold.
- **Tap a glowing target** — the orb arcs over its neighbor, vanishing it.
- **Goal**: reduce the board to a single remaining orb.
- **Perfect Clear**: finish with the last orb on the center hole for a rare
  crystal.
- **Undo** is unlimited. No time, no move counter, no pressure.

## What This Prototype Covers

- [x] Core peg solitaire logic (jump rules, undo stack, win detection)
- [x] 5 starter levels with increasing complexity
- [x] Moonlight theme visuals (midnight marble board + glass orbs + moonbeam)
- [x] Win states: standard *Complete* + rare *Perfect Clear*
- [x] Dead-end detection (no-moves-left warning)
- [x] Mobile-first portrait layout

## What's Not Here (Next Sprints)

Per the approved 12-week plan:
- Week 3-4: Procedural level generator (seed-guaranteed solvable)
- Week 5: 3D Garden meta (crystal collection)
- Week 6: Theme store + 5 additional themes
- Week 7: Audio + haptic layer
- Week 9: IAP integration
- Week 12: Soft launch (Canada + Germany)

## Validation Goals (this prototype)

Hand this to 5 friends/family. Watch for:
1. Do they start playing within **30 seconds** without a tutorial?
2. Do they say "just one more" after 15 minutes?
3. Do they discover Undo on their own?
4. Which level felt *too* easy or *too* hard?

If all four answers are positive → go to Unity port (Week 3+).
If not → tune feel, not features.

## Next Steps

See `/root/.claude/plans/bir-oyun-fikrine-ihtiyac-m-rippling-wigderson.md` for
the full 12-week implementation plan, monetization strategy, soft-launch KPI
matrix, and portfolio roadmap (BOXDREAM → STICKS → TANGRAMO → UR).
