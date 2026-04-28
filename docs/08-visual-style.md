# 🎨 08 — Visual Style Guide

**Belge amacı**: Royal Match smooth render formülünün uygulama kuralları. Tüm art prompt + asset üretimi bu rehbere bağlanır.

---

## 1. Stil Pillar — "Royal Match Smooth"

| Etki | % Pay |
|---|---|
| Royal Match | %90 |
| Pixar (Toy Story / Inside Out) | %10 |

**Net definition**:
- Smooth 3D toon render
- Vector-clean edges
- Soft gradient transitions
- Bold readable shapes
- Warm cozy palette
- Mass-market neutral (50/50 gender)

---

## 2. Renk Paletleri

### 2.1 Birincil palet (UI + ortam)

| Renk adı | Hex | Kullanım |
|---|---|---|
| Cream | `#F5E8D0` | Background, UI panel |
| Amber | `#D4B87A` | Accent, gold trim |
| Warm Wood | `#8B6F47` | Apothecary tezgah |
| Deep Amber | `#5C3A21` | Dark accent, font |
| Off-White | `#FFFAF0` | Bright pop, highlight |

### 2.2 Element renkleri (gameplay sıvı)

| Element | Hex | Light variant | Dark variant |
|---|---|---|---|
| Fire | `#E63946` | `#FF6B7A` | `#A82838` |
| Water | `#1D7DBF` | `#4DA8E0` | `#0E5A8C` |
| Earth | `#5C8A3C` | `#7DB05E` | `#3D5E26` |
| Air | `#F4D35E` | `#FFE383` | `#C7A938` |
| Aether | `#9D4EDD` | `#B879F0` | `#6E2DA0` |

### 2.3 Yasak renk-uygulamaları

- ❌ Mor saç (Iris)
- ❌ Pembe saç (Iris)
- ❌ Holographic / pearl tones (K-pop)
- ❌ Aşırı doygun "neon" renk
- ❌ Sade siyah-beyaz palette (mass-market değil)

---

## 3. Tipografi

| Kullanım | Font | Ağırlık |
|---|---|---|
| UI başlık | Fredoka Bold (Google Fonts free) | 700 |
| UI gövde | Nunito SemiBold | 600 |
| Şişe harfi | Fredoka Bold (oversized) | 700 |
| Cutscene dialog | Quicksand Medium | 500 |

**Yedek yasaklar**:
- ❌ Comic Sans
- ❌ Times / Serif (premium feel istemiyoruz)
- ❌ Handwritten / cursive (okunaksız)
- ❌ Gothic blackletter (Belle Époque)

---

## 4. Render Stil Reçetesi

Sora / ChatGPT / Midjourney prompt'larına dahil edilecek anahtar kelimeler:

```
✅ MUST include:
- "smooth 3D toon render"
- "Royal Match style"
- "vector-clean edges"
- "soft gradient transitions"
- "warm cozy palette"
- "mass-market mobile game art"
- "Pixar smoothness, Toy Story polish"
- "bold readable shapes"

❌ MUST NOT include (negative prompt):
- "painterly"
- "oil painting"
- "brush strokes" / "brushstrokes"
- "Clair Obscur" / "DNA atmosphere"
- "Belle Époque"
- "K-pop"
- "anime / chibi"
- "magical girl"
- "purple hair" / "lavender"
- "ribbon" / "bow" / "heart accessory"
- "gothic" / "witch hat"
- "paper lanterns" / "cherry blossoms"
- "pearl" / "holographic" / "iridescent"
- "clinical lab"
```

---

## 5. Asset Listesi (12 hafta plan)

### 5.1 UI Asset (~30 element)

- Main menu background
- Chapter map background (6 farklı tema)
- HUD elementler (life, coin, star, booster icons)
- Popup pencereleri (level complete, fail, store)
- Settings UI

### 5.2 Karakter Asset (~20 element)

- Master Octave: 5 portrait (neutral, happy, surprised, proud, wave)
- Iris: 5 portrait (neutral, focused, excited, determined, wave)
- Mochi: 4 sprite (sleeping, meowing, alert, playing)
- Background NPC: 3 (yaşlı kadın müşteri, genç müşteri, yerli kadın)
- Iris evolution (chapter 6 mistress): 1 portrait revision

### 5.3 Gameplay Asset (~40 element)

- Şişe varyantları (standard, locked, frozen, lava, cosmic, metallic)
- Renk katman shader / sprite
- Harf tile (A–Z + dil özel chars)
- Mantar (cork) sprite + countdown ring
- Buzul partikül + ısı dalga shader
- Lava bubble + ember partikül
- Cosmic starfield background
- Slot machine peak moment efekt (halo, confetti, ring)

### 5.4 Cutscene Asset (~30 element)

- 6 chapter background art
- Apothecary interior (3 view: tezgah, mağaza, bodrum library)
- Volcano scene
- Frozen mountain scene
- Hidden library scene

**Toplam tahmini ~120 unique asset.** AI üretimi (Sora/Midjourney) + asset store + manuel polish.

---

## 6. Animasyon Spec

### 6.1 Idle döngüleri

| Element | Frame | Süre |
|---|---|---|
| Şişe içi sıvı bobble | 30 frames | 2 sn loop |
| Mochi nefes | 24 frames | 3 sn loop |
| Mantar countdown ring | 60 frames | 3 hamle |
| Cosmic starfield | particle | sürekli |

### 6.2 Pour animation

- Şişe eğilme: 0–400 ms
- Sıvı parabolic akış: 100–400 ms
- Hedef ripple: 400–600 ms
- Toplam: ~700 ms

### 6.3 Seal celebration (peak moment)

- Halka doğuş: 0–200 ms
- Halka pulse: 200–500 ms
- Confetti: 300–700 ms
- Yıldız büyütme: 700–1200 ms
- Toplam: 1.2 sn

---

## 7. Sahne Aydınlatma

### 7.1 Apothecary interior

- Ana ışık: Üstten amber warm spotlight (`#F5C87A`)
- Sekonder: Pencereden yumuşak gündüz ışığı (`#E8DCC0`)
- Accent: Şişelerden iç parıltı (each color element kendi hafif glow'u)

### 7.2 Frozen scene

- Ana ışık: Üstten cool moonlight (`#D8E8F4`)
- Sekonder: Buzdan refraction shimmer
- Accent: Iris fener + Mochi göz parıltı

### 7.3 Volcano scene

- Ana ışık: Lava'dan alttan kırmızı glow (`#FF4530`)
- Sekonder: Üstten karanlık (`#2A1810`)
- Accent: Iris cool mist booster mavi parıltı (kontrast)

---

## 8. Mobil Optimizasyon

| Constraint | Değer |
|---|---|
| Texture max | 2048×2048 (atlas) |
| Sprite resolusyonu | 1080p hedef (iPhone 11+ optimal) |
| Tek seferde sahne sprite | <250 |
| Particle simultaneous | <50 |
| Animation fps | 30 fps target (60 fps mid-range) |
| Build size | <150 MB (download) |

---

## 9. Bilinmeyen / Riskli Render Patterns

| Pattern | Karar |
|---|---|
| Parallax depth shifting | Sadece chapter map'te kullan |
| Lottie animasyon | Hayır — Spine veya 2D Sprite atlas yeterli |
| Volumetric fog | Hayır — performans risk |
| Real-time lighting | Hayır — baked lights only |
| Procedural shader (lava/ice) | Evet — tek-shot test sonra approve |

---

## 10. Tutorial Görselleri

- Octave point gestures (parmak işareti)
- Tap target highlights (yumuşak amber halka)
- Drag arrow (akıcı vector)
- "Try it!" callout (Iris konuşma balonu)

Tutorial asset = 8 unique elemen.

---

## 11. App Store / Play Store Asset

| Asset | Boyut | Adet |
|---|---|---|
| App icon (iOS) | 1024×1024 | 3 varyant test |
| Feature graphic (Play Store) | 1024×500 | 1 |
| Screenshots (iOS 6.5") | 1284×2778 | 8 |
| Screenshots (iOS 5.5") | 1242×2208 | 8 |
| Screenshots (Android) | 1080×1920 | 8 |
| Promo video | 30 sn portrait | 1 |

Detay: `art-prompts/marketing-key-art.md` ve `art-prompts/icons/`.

---

## 12. Brand Identity Checklist

Her asset üretiminden önce kontrol:

- [ ] Royal Match smooth render mı?
- [ ] Painterly / brushstrokes YOK mu?
- [ ] Renk paleti onaylı mı?
- [ ] Mass-market neutral (50/50 gender) mi?
- [ ] Niche cultural marker yok mu?
- [ ] Magical girl / chibi / anime exaggeration yok mu?
- [ ] Iris saç doğal kestane mi?
- [ ] Octave sıcak grandfather mı (NOT scary wizard)?
- [ ] Mochi gri tabby mi (NOT kara kedi)?

---

*Sürüm 1.0 — frozen design.*
