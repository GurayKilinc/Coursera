# 🧪 POURLE

> *"Pour. Spell. Win."* — Casual mass-market mobile puzzle game.

**POURLE** is a hybrid casual mobile puzzle game combining the satisfying liquid-pouring mechanic of **Ball Sort Puzzle** with the wordplay tension of **Wordle**. Players sort colorful liquid layers between magical apothecary jars while spelling out words — each layer carries a letter that must align into valid words when the jar is sealed.

Designed for **everyday mass-market play** (workplace breaks, transit, evening relax), built on the proven **Royal Match formula** (warm cozy art, slot-machine peak moments, lite Saga meta with chapters/lives/stars/boosters).

---

## 🎯 Core Identity

| | |
|---|---|
| **Working title** | POURLE |
| **Genre** | Casual puzzle (Ball Sort × Wordle hybrid) |
| **Engine** | Unity 6 LTS (2D URP) |
| **Platforms** | iOS + Android |
| **Target audience** | 22–55, balanced 50%/50% gender, global mass-market |
| **Pilot markets** | Türkiye, Brezilya, Almanya |
| **Production timeline** | 12 weeks solo |
| **Total investment** | ~$3,000 + ~280 dev hours |
| **Estimated v4 score** | 4.50 |
| **D7 retention target** | 38% |
| **D30 retention target** | 22% |
| **ARPPU target** | $10–14 |
| **Year-1 net profit estimate** | $130K–380K |

---

## 🎮 Core Loop

1. **Tap** a jar → top liquid layer (with its letter) lifts.
2. **Tap** another jar → liquid + letter pours over (Ball Sort rule: same color or empty).
3. **Fill** a jar with 4 single-color layers.
4. If the letters spell a **valid word** → jar **seals** with golden halo (slot-machine peak moment).
5. Clear all jars to win the level.

---

## 🧬 Mechanic Evolution Schedule

A new mini-mechanic appears every **2–3 episodes** (every 10–15 levels). Player NEVER gets bored across 30 episodes / 150 levels. See [`docs/06-mechanic-evolution.md`](docs/06-mechanic-evolution.md).

| Episode | New Mechanic |
|---|---|
| 1–3 | Core Ball Sort + Wordle |
| 4–5 | 5th element (purple GLOW) |
| 6–7 | Color transformation (white letters dye in liquid) |
| 8–10 | Locked Caps (cork-locked jars) |
| 11–13 | Frozen Bottles (need warm liquid) |
| 14–15 | Heat Booster + speed challenge |
| 16–18 | Metallic letters (element-coded gold/silver/bronze) |
| 19–20 | Ancient Spell special levels |
| 21–23 | Lava Bottles (wrong color melts) |
| 24–25 | Cool Mist Booster |
| 26–28 | Cosmic Spells (5–6 letter boss words) |
| 29–30 | Final combo + Cosmic Master boss |

---

## 🎭 Cast — Trio

- **Master Octave** — 65-year-old male alchemist mentor (Royal Match's "King Robert" archetype)
- **Iris** — 22-year-old female apprentice (capable practical, natural chestnut hair, NOT princess)
- **Mochi** — gray tabby cat companion (universal animal mascot)

See [`docs/04-characters.md`](docs/04-characters.md) for full character bibles.

---

## 📖 Story — 6 Chapters

| Chapter | Title | Theme | Episodes |
|---|---|---|---|
| 1 | First Brew | Iris's first day, basic alchemy | 5 |
| 2 | Color Magic | Color transformation discovery | 5 |
| 3 | Frozen Element | Mysterious frozen gift from Octave's past | 5 |
| 4 | Ancient Spells | Hidden library, Octave's adventurer past | 5 |
| 5 | Volcano Brew | Iris's solo dangerous expedition | 5 |
| 6 | Cosmic Master | Iris becomes Mistress, final boss | 5 |

Full scenario writing in [`docs/05-story-scenarios.md`](docs/05-story-scenarios.md).

---

## 💰 Monetization

| SKU | Price |
|---|---|
| No Ads | $3.99 |
| Starter Pack (first 7 days) | $2.99 |
| Life Refill | $0.99 / $4.99 |
| Booster Bundle | $1.99 / $4.99 |
| Coin Pack | $0.99 / $4.99 / $19.99 |
| Witch Pass (subscription) | $7.99 / 30 days |
| Theme Bundle | $4.99 each |

Light AMI (Aggressive Monetization Index = 3, Royal Match level). Full strategy in [`docs/07-monetization.md`](docs/07-monetization.md).

---

## 📁 Repository Structure

```
POURLE/
├── README.md                          (this file)
├── CLAUDE.md                          (instructions for Claude)
├── docs/
│   ├── 01-game-design-document.md     (master design doc)
│   ├── 02-mechanics.md                (core gameplay mechanics)
│   ├── 03-saga-meta.md                (life, chapter, episode, star, booster)
│   ├── 04-characters.md               (Master Octave + Iris + Mochi bibles)
│   ├── 05-story-scenarios.md          (6 chapter detailed scenarios)
│   ├── 06-mechanic-evolution.md       (every 2-3 episode mini-mechanic)
│   ├── 07-monetization.md             (7 SKU + ads + Witch Pass)
│   ├── 08-visual-style.md             (Royal Match smooth render guide)
│   ├── 09-production-plan.md          (12-week solo sprint)
│   ├── 10-soft-launch-strategy.md     (pilot countries, KPI targets)
│   └── 11-risk-mitigation.md          (pivot gates, backup plans)
├── art-prompts/
│   ├── marketing-key-art.md           (hero banner)
│   ├── banner.md                      (social media banner)
│   ├── characters/
│   │   ├── master-octave.md
│   │   ├── iris.md
│   │   └── mochi.md
│   ├── gameplay-screens/
│   │   ├── normal-gameplay.md
│   │   ├── peak-moment.md
│   │   ├── chapter-map.md
│   │   ├── episode-cutscene.md
│   │   ├── chapter-frozen.md
│   │   └── chapter-volcano.md
│   └── icons/
│       ├── icon-v1-bottle-hero.md
│       ├── icon-v2-character-focused.md
│       └── icon-v3-letter-focused.md
└── diagrams/
    ├── architecture.md                (Unity scene & system architecture)
    ├── chapter-flow.md                (player progression flow)
    └── monetization-funnel.md         (free → paying conversion funnel)
```

---

## 🚀 Production Status

- ✅ Final Game Design Document complete
- ✅ All Sora/ChatGPT art prompts written (Royal Match smooth render style)
- ✅ Character cast finalized (Master Octave + Iris + Mochi)
- ✅ 6-chapter story scenarios written
- ⏳ Trademark professional search (Trademarkia $99) — pending
- ⏳ Domain registration (pourle.com / pourle.app) — pending
- ⏳ Unity project skeleton — week 1 sprint
- ⏳ MVP playable build — week 4 (Pivot Gate 1)
- ⏳ Soft launch — week 12 (Türkiye + Brezilya + Almanya)

---

## 🛡️ Trademark / Domain Status

⚠️ **Working title**. Manual web search clean as of design freeze, but professional trademark search via Trademarkia.com ($99) or trademark attorney ($300–500) is required before final commitment. If POURLE clashes, fallback names: POPLET, MIXLE (both pre-vetted).

---

## 📊 Success Metrics (12-Month)

- **Soft launch (week 12–16)**: D1 ≥ 42%, D7 ≥ 22%, D30 ≥ 12%
- **Month 6**: 100K–500K MAU, $50K–200K monthly revenue
- **Year 1**: 500K–2M MAU, **$130K–380K net profit** (after platform fee + UA + ops)
- **Year 2**: 2nd game launched (Saga meta code reuse), portfolio revenue $300K–700K/year

---

## 🤝 Contributing

This is a solo developer project. The repository serves as the single source of truth for all design, art prompts, and production decisions.

For Claude AI agents collaborating on this project, see [`CLAUDE.md`](CLAUDE.md).

---

*Document version 1.0 — frozen design as of soft launch preparation phase.*
