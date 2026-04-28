# 🤖 CLAUDE.md — POURLE Project Instructions for Claude

This document provides context, conventions, and operating instructions for any Claude AI agent collaborating on the POURLE project.

---

## 🎯 Project Context

**POURLE** is a casual mass-market mobile puzzle game (Ball Sort × Wordle hybrid) targeting iOS + Android. Solo developer project, 12-week sprint, ~$3,000 budget, $130K–380K year-1 net profit target.

**Core philosophy**: Royal Match formula — warm cozy mass-market polish, slot-machine peak moments, lite Saga meta. NOT premium art piece, NOT niche indie. Workplace-and-transit-friendly casual play.

---

## 📁 Source of Truth

The `docs/` folder contains the **frozen game design**. Do NOT modify design without explicit user approval. The design has been through 8+ iteration cycles to reach this state — additional changes risk scope creep.

Key documents:
- [`docs/00-phase-plan.md`](docs/00-phase-plan.md) — 9-phase master roadmap (start here to know "which phase are we in?")
- [`docs/01-game-design-document.md`](docs/01-game-design-document.md) — master overview
- [`docs/02-mechanics.md`](docs/02-mechanics.md) — core gameplay rules
- [`docs/03-saga-meta.md`](docs/03-saga-meta.md) — life, chapter, episode, star, booster
- [`docs/04-characters.md`](docs/04-characters.md) — Master Octave, Iris, Mochi bibles
- [`docs/05-story-scenarios.md`](docs/05-story-scenarios.md) — 6 chapter scripts
- [`docs/06-mechanic-evolution.md`](docs/06-mechanic-evolution.md) — every-2-3-episode mini-mechanic schedule

---

## 🎨 Visual Style — STRICT Rules

When generating any art prompt or visual asset:

### MUST follow
- ✅ **Royal Match smooth 3D toon render** (90% influence)
- ✅ Pixar's Toy Story / Inside Out smoothness (10% influence)
- ✅ Vector-clean edges, smooth gradient transitions
- ✅ Bold readable shapes
- ✅ Warm cozy palette (cream, amber, gold, balanced element colors)
- ✅ Mass-market neutral (50/50 gender appeal)

### MUST NOT include
- ❌ Painterly texture or visible brushstrokes
- ❌ Oil painting / Clair Obscur painted style
- ❌ Purple/lavender hair on Iris (natural chestnut brown only)
- ❌ K-pop accents (no holographic, pearl, ribbon)
- ❌ Heavy Belle Époque ornate detailing
- ❌ Asian niche markers (paper lanterns, cherry blossoms)
- ❌ Magical girl outfits (bows, hearts, ribbons)
- ❌ Anime / chibi exaggeration
- ❌ Clinical lab feel
- ❌ Hogwarts gothic atmosphere
- ❌ Upcoming-pieces tray in gameplay (removed — bottles already show letters)

See [`docs/08-visual-style.md`](docs/08-visual-style.md) for full guide.

---

## 🧠 Decision-Making Heuristics

When asked to add or modify a feature, apply this 3-question filter (lessons learned from earlier scope creep):

1. **What does this element actually do for the player?** (concrete benefit)
2. **Does this element contribute to retention or monetization?** (otherwise remove)
3. **Does this element narrow the mass-market audience?** (if niche, reconsider)

If the element fails 2 of 3, remove it. The Royal Match formula succeeds because **every UI element earns its place**.

---

## 🚫 Anti-Patterns to Avoid

These patterns caused multiple iteration cycles in design phase:

### Pattern 1: Reflexive feature-adding from other games
- Bad: "Block Blast has an upcoming-pieces tray, let's add one too"
- Good: "Does our mechanic require previewing future pieces? No → don't add"

### Pattern 2: Over-sophistication
- Bad: "Belle Époque painted oil-painting Clair Obscur DNA atmosphere"
- Good: "Royal Match smooth cartoony, simple cozy"

### Pattern 3: Niche aesthetic creep
- Bad: K-pop holographic accents, paper lanterns, witch gothic
- Good: Universal mass-market neutral

### Pattern 4: Feminine-skewing visual decisions
- Bad: Mor/lavender hair, hearts/ribbons, magical girl
- Good: Natural hair, practical outfit, gender-balanced

### Pattern 5: Unverified naming
- Bad: Suggesting names without market check (8 names eliminated due to clashes)
- Good: Always check via web search → trademark → domain → app store BEFORE recommending

---

## 📊 Simulation Methodology

When evaluating any new design choice (name, character, mechanic), use the v4 persona simulation framework:

- 4 markets × 100 personas = 400 personas total (USA, Türkiye, Almanya, Japonya)
- Each persona scored on:
  - Hatırlanırlık (memorability)
  - Söylenebilirlik (pronounceability — global)
  - Tema uyumu (theme fit)
  - Genç kitle çekimi (youth appeal)
  - Mass-market kabul (mass-market acceptance)
- Score 1–5
- Target: **≥ 4.5** for mass-market-grade decisions
- Pivot threshold: **< 4.0** = redesign

The naming process used this framework to evaluate 8 candidates before settling on POURLE (4.50).

---

## 🔧 Production Conventions

### Unity project structure
```
Assets/
├── Scripts/
│   ├── Core/              # GameController, SceneDirector
│   ├── Jars/              # Apothecary jar, liquid layer, letter
│   ├── Logic/             # BallSortValidator, WordValidator, etc
│   ├── SagaMeta/          # ChapterMap, EpisodeManager, LifeManager
│   ├── Mentor/            # Master Octave + Iris + Mochi cutscene system
│   ├── PeakMoment/        # JarSeal celebration, ComboTracker
│   ├── Boosters/          # Hint, ExtraJar, Undo, AutoSort, Heat, CoolMist
│   ├── BonusLevels/       # SpeedBrew, NoHint, MasterWord, Cascade
│   ├── UI/                # Menus, HUD, popups
│   ├── Audio/             # AudioDirector, slot machine SFX
│   ├── Haptics/
│   ├── Localization/
│   └── Economy/           # IAPController, AdsController, CoinBank
├── ScriptableData/
│   ├── Chapters/          # 6 ChapterSO
│   ├── Episodes/          # 30 EpisodeSO
│   ├── Levels/            # 150 LevelSO
│   └── Dictionaries/      # 10 language word lists JSON
├── Art/                   # Sprites, animations, themes
├── Audio/                 # Music, SFX, voice
└── Scenes/                # Bootstrap, MainMenu, ChapterMap, Gameplay, Cutscene
```

### Naming conventions
- **C# classes**: PascalCase (`ChapterMap`, `LifeManager`)
- **Variables**: camelCase (`currentLevel`, `playerLives`)
- **ScriptableObjects**: Suffix `SO` (`ChapterSO`, `LevelSO`)
- **Folders**: PascalCase
- **Scenes**: PascalCase (`MainMenu.unity`)

### Commit conventions
- `feat: add chapter map UI`
- `fix: liquid pour animation timing`
- `docs: update mechanic evolution table`
- `art: add Iris portrait V2`

---

## 🏁 When User Asks for Help

### If user asks for new design
1. Check `docs/` first — is this already decided?
2. If yes, refer them to the doc and confirm before changing
3. If no, apply 3-question filter before suggesting

### If user asks for art prompt
1. Reference [`docs/08-visual-style.md`](docs/08-visual-style.md) — Royal Match smooth render rules
2. Use existing prompts in `art-prompts/` as base
3. Apply STRICT NO-GO list

### If user asks for Unity code
1. Follow conventions in [`docs/09-production-plan.md`](docs/09-production-plan.md)
2. Reference Unity scene/system architecture in [`diagrams/architecture.md`](diagrams/architecture.md)
3. Always create ScriptableObject schemas BEFORE writing logic

### If user asks for naming/branding decisions
1. POURLE is current working title
2. Final name confirmed via Trademarkia $99 search (pending)
3. Fallback names if POURLE clashes: POPLET, MIXLE (both have known risks — see [`docs/01-game-design-document.md`](docs/01-game-design-document.md))

---

## 🧭 Project Phases

| Phase | Status | Notes |
|---|---|---|
| 1. Concept ideation | ✅ Complete | 8+ name iterations, mascot revisions, mechanic evolution |
| 2. Design freeze | ✅ Complete | This documentation |
| 3. Trademark verification | ⏳ Pending | Trademarkia $99 search |
| 4. Unity prototype | ⏳ Next | Weeks 1–4 |
| 5. MVP build | ⏳ | Weeks 5–8 (Gate 2: balance check) |
| 6. Polish + integration | ⏳ | Weeks 9–11 |
| 7. Soft launch | ⏳ | Week 12 (Türkiye + Brezilya + Almanya) |
| 8. Tune + global launch | ⏳ | Weeks 12–26 |

---

## 🆘 Common Issues + Solutions

### "Should I add feature X?"
Apply 3-question filter. If failing → don't add.

### "Visual feels too feminine / too gothic / too painterly"
Re-read [`docs/08-visual-style.md`](docs/08-visual-style.md). Royal Match smooth render is the only target.

### "Player will get bored at level X"
Cross-reference [`docs/06-mechanic-evolution.md`](docs/06-mechanic-evolution.md) — every 2–3 episode brings new mechanic. If gap, propose a new mini-mechanic.

### "Monetization too aggressive / too soft"
Target AMI = 3 (Royal Match level). See [`docs/07-monetization.md`](docs/07-monetization.md).

---

## 📞 Final Reminder

**Trust the docs**. The user spent significant time reaching this design — DON'T make autonomous changes. When in doubt, ask the user before suggesting modifications.

When uncertain about a name, mechanic, or visual choice, **always run the v4 simulation framework** (see Simulation Methodology above) to test the assumption before committing.

The goal: **Ship POURLE in 12 weeks. Reach $130K–380K net profit in year 1.** Every decision should serve this goal.

---

*Last updated: design freeze, soft launch preparation phase.*
