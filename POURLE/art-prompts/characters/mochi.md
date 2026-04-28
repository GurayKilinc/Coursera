# 🐱 Mochi — Character Art Prompt

**Karakter spec**: Bkz. `docs/04-characters.md` Mochi bible.

**Çıktı**: 4 sprite varyasyon (sleeping, meowing, alert, playing) + idle animation reference.

---

## Mochi Full Reference Sheet Prompt

```
Character reference sheet for "Mochi", adult gray tabby cat companion in
casual mobile puzzle game POURLE. Smooth 3D toon render in Royal Match
style with Pixar Toy Story polish.

Physical:
- Species: Adult domestic shorthair cat, gray tabby pattern.
- Size: Normal adult cat size, well-fed but NOT exaggerated obese
  cartoonish, NOT skinny stray.
- Fur: Silver-gray base #8B8C82 with darker charcoal #3A3D38 stripe
  pattern (mackerel tabby) running along back and tail. Soft fluffy
  texture but groomed.
- Eyes: Bright warm green #5C8A3C, friendly curious expression default,
  NOT predator slit-pupil scary, NOT anime exaggerated huge eyes.
- Nose: Small pink #E8A8B0.
- Ears: Standard upright cat ears, slightly tufted at tips, alert default.
- Tail: Medium length, often held up curling at tip (happy cat default).
- Whiskers: Standard length, soft.
- Paws: Pink toe beans visible from below, small black paw pads.

Accessories:
- Small thin gold collar with tiny brass bell (apothecary mascot symbol,
  the bell rings softly in cutscenes). NOT bow tie, NOT ribbons.
- NO costume, NO outfit, NO witch hat, NO accessories beyond collar.

NEVER include:
- Black cat (avoids witch trope).
- Sphinx / hairless breed (niche).
- Anime kawaii double tail (Japanese yokai trope).
- Magical creature appearance (NOT a familiar, just a normal cat).
- Witch hat or wizard accessories.
- Anime "uwu" exaggerated kawaii face.
- Bow tie or ribbon collar.
- Magical floating presence.
- Multiple tails or supernatural features.

Color palette:
- Primary: Silver gray #8B8C82
- Stripe: Charcoal #3A3D38
- Eyes: Warm green #5C8A3C
- Nose: Soft pink #E8A8B0
- Collar accent: Gold #D4B87A

Style: Royal Match smooth 3D toon render (90%), Pixar polish (10%).
Universally appealing animal mascot — relatable, warm, NOT idealized
exaggerated cute.

Mood reference: Disney's "Marie" from Aristocats (warm classic cartoon
cat, NOT modern kawaii), Pixar's "Sox" from Lightyear smoothness,
Studio Ghibli's "Jiji" warmth (color: gray instead of black).

Negative prompt: NO painterly, NO oil painting, NO brushstrokes, NO
black cat, NO witch familiar, NO anime kawaii uwu, NO magical girl
mascot, NO costume, NO ribbon, NO bow tie, NO hat, NO supernatural
features, NO chibi exaggeration, NO Lisa Frank style, NO neon colors.

Output format: Multi-pose reference sheet (front, side, top-down,
sleeping curl, alert standing) plus 4 expression variants (sleeping,
meowing, alert, playing). Crisp 4K.
```

---

## Varyasyon Promptları

### 1. Sleeping (Idle UI)
```
Mochi curled up sleeping in a tight ball, tail wrapped around body, eyes
gently closed, breathing soft visual rise-fall, ears relaxed but slightly
twitchy. Looped idle animation reference.
```

### 2. Meowing (Hint Booster Activation)
```
Mochi sitting upright, looking up at camera, mouth slightly open in
"miyav" position, paw extended forward as if pointing/asking. Cute but
NOT exaggerated kawaii.
```

### 3. Alert (Cutscene Reaction)
```
Mochi standing tall, ears perked fully forward, eyes wide and curious,
tail upright with slight curl at tip, looking off-camera as if reacting
to story event. Tense alert posture.
```

### 4. Playing (Win Celebration)
```
Mochi mid-jump or rolled belly-up, paws batting at falling confetti
particles, eyes bright with joy, tail fluffed playfully. Action pose.
```

---

## Animasyon Sprite Listesi

| Animasyon | Frame count | Süre |
|---|---|---|
| Idle breathing | 24 | 3 sn loop |
| Tail twitch | 16 | 1.5 sn loop |
| Alert (head turn) | 8 | trigger |
| Meow (mouth open + sound) | 12 | trigger |
| Paw point (hint booster) | 12 | trigger |
| Curl up (sleep) | 18 | trigger |
| Stretch (waking) | 24 | trigger |
| Win jump | 20 | trigger |
| Sit blink | 8 | 4 sn random loop |

---

## Kullanım

- Cutscene background ambient (most scenes)
- Hint booster activation (Mochi paw points)
- Idle main menu mascot
- Loading screen tip animation
- Mochi-themed UI tema (Witch Pass premium track ödül)
- App icon variant (mascot focus)
