# 🎬 Episode Cutscene — Art Prompt

**Amaç**: Episode başlangıç + final cutscene sahneleri. Royal Match'in dialog overlay formülü.

**Boyut**: 1284×2778 portrait.

---

## Sora / ChatGPT / Midjourney Prompt — Sample (Episode 1 Opening)

```
Mobile game cutscene screen for POURLE casual puzzle game, vertical
portrait, smooth 3D toon render Royal Match style.

Composition (top to bottom):
- Background scene (~70% upper screen): Apothecary interior, golden
  hour lighting through lattice window, warm wood tezgah dominant in
  middle ground. Iris standing at door, half-turned, sunlight catching
  her chestnut hair. Master Octave behind tezgah, half-rim glasses
  raised, looking up warmly. Mochi on tezgah surface, head turned
  curiously toward Iris. Background herbs + bottles softly out of focus.

- Dialog box (lower 30% screen):
  - Speaker portrait (left side): Master Octave bust portrait, warm
    encouraging expression, framed in subtle warm gold border.
  - Speaker name tag: "MASTER OCTAVE" in amber rounded font.
  - Dialog text: "Hoşgeldin, çırak. İlk karışımın için temiz bir şişe
    yeterli olur. Renkleri ayır, harfleri konuştur. Basit, ama büyülü."
    in clean readable mid-size sans-serif (Quicksand Medium).
  - Skip button: Small "Skip ▶" upper-right of dialog box.
  - Continue indicator: Small bouncing arrow lower-right of dialog box.

- Bottom edge: Subtle "Episode 1 — Welcome to the Apothecary" chapter
  label.

Color palette:
- Scene: Cream #F5E8D0, warm wood #8B6F47, amber #D4B87A
- Dialog box: Cream #F5E8D0 with deep amber #5C3A21 border + gold #D4B87A
  accent
- Text: Deep amber #5C3A21 for readability

Style: Royal Match smooth 3D toon render. Scene captured like a Pixar
storybook still frame. Dialog overlay clean and minimal, NOT cluttered.
Warm cozy mood, inviting.

Lighting: Top-down warm amber spotlight on Iris (highlight focus on POV
character), secondary fill from window, ambient amber from bottle glow.

NEVER include:
- Painterly or brushstroke style.
- Anime cutscene tropes (no big-eye reactions).
- Belle Époque ornate dialog frame.
- Gothic atmosphere.
- Cluttered HUD overlapping dialog.

Format: 1284×2778 vertical portrait, dialog readable on small phone screen.
```

---

## Cutscene Tip Çeşitleri

### 1. Opening Episode Cutscene (15-30 sn)
- Statik scene background
- 1-3 dialog box turn (Octave + Iris exchange)
- Yeni mekanik teaser visual

### 2. Final Episode Cutscene (15-30 sn)
- Reaksiyon scene (Iris reaction)
- 1-2 dialog box
- Star reward + progress bar fill animasyonu

### 3. Chapter Finale (30-45 sn)
- 3-5 sahne geçişi (cinematic-lite)
- Story beat reveal (Octave's past, Mochi's history, etc.)
- Big chapter unlock animation finale

### 4. New Mechanic Tutorial Cutscene (10-20 sn)
- Mekanik visual demo
- Octave 1-cümlelik açıklama
- Auto-transition to gameplay

---

## Sahne Listesi (30 episode × 2 = 60 cutscene)

| Episode | Opening sahne | Final sahne |
|---|---|---|
| 1 | Iris arriving at apothecary | Iris first 5 successes |
| 2 | Color experimentation | Accidental purple discovery |
| 3 | First customer order | Customer happy departure |
| 4 | Aether discovery | Iris first Aether seal |
| 5 | Recipe book gift | Chapter 1 finale + book |
| ... | ... | ... |
| 30 | Final test setup | Ending — Iris becomes Mistress |

Detay: `docs/05-story-scenarios.md`.

---

## Localization

- Tüm dialog text 10 dile çevrilmiş JSON dosyalarda
- Dialog box layout dynamically expands for longer translations
- RTL support (Phase 2 — Arabic, Hebrew)
- Voice-over Phase 2 (post-launch)

---

## Kullanım

- Episode başlangıç + final
- Chapter finale (genişletilmiş varyant)
- Tutorial mekanik tanıtım
- Story event push notification preview
