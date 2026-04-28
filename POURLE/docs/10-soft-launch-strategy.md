# 🚀 10 — Soft Launch Strategy

**Belge amacı**: Hafta 12'de pilot ülkelere lansman, KPI izleme, global launch karar matriksi.

---

## 1. Pilot Ülkeler

| Ülke | Neden | Beklenen DAU | Beklenen ARPDAU |
|---|---|---|---|
| **Türkiye** | Düşük UA maliyeti, iyi TR sözlük testi, hızlı feedback | 5–10K | $0.06 |
| **Brezilya** | Kazanç ucuz UA, Portugese sözlük testi, mass-market davranış | 5–10K | $0.05 |
| **Almanya** | Premium European market proxy, German sözlük, $$$ test | 1–3K | $0.20 |

**Total pilot DAU**: ~15K DAU hedefi.

**Pilot süresi**: 4 hafta (Hafta 12–16).

---

## 2. Pilot Yapılmayan Ülkeler

| Ülke | Neden ertelendi |
|---|---|
| ABD | Yüksek UA maliyeti ($4–6 CPI), Phase 2'de organic + paid combine |
| Japonya | Sözlük + cultural tweak Phase 2 |
| Güney Kore | Localization Phase 2 |
| Çin | Apple Pay yok, Tencent gerekli |
| Hindistan | Düşük ARPPU, hacim ama gelir az |

---

## 3. Lansman Checklist (Hafta 11–12)

### 3.1 Apple App Store

- [ ] App Store Connect listing
- [ ] App Privacy Detail (data collection beyan)
- [ ] App Tracking Transparency prompt
- [ ] Screenshots (8 adet, 6.5" + 5.5")
- [ ] Promo video (30 sn portrait)
- [ ] Keywords (100 char limit, ASO research)
- [ ] Description (TR + EN + DE + PT)
- [ ] Age rating: 4+
- [ ] Pricing: Free with IAP

### 3.2 Google Play

- [ ] Play Console listing
- [ ] Data Safety Form
- [ ] Feature graphic (1024×500)
- [ ] Screenshots (8 adet, portrait)
- [ ] Promo video YouTube link
- [ ] Description (TR + EN + DE + PT)
- [ ] Content rating: PEGI 3
- [ ] Pricing: Free with IAP

### 3.3 ASO (App Store Optimization)

**Keywords (Apple, comma-separated, 100 char)**:
```
puzzle, word, brew, alchemy, ball sort, wordle, casual, sort, letter, jar, mix, magic, witch
```

**Title (30 char)**:
```
POURLE: Pour & Spell Puzzle
```

**Subtitle (30 char)**:
```
Brew Letters into Magic Words
```

**Description açılışı (ilk 3 satır kritik)**:
```
🧪 Sort liquid letters. Spell magical words. Master the art of POURLE.

Pour colorful potions between bottles, line up letters into real words,
and seal each jar with a satisfying golden glow.
```

---

## 4. UA (User Acquisition) Stratejisi

### 4.1 Bütçe (12 hafta pilot)

| Kanal | Bütçe | Hedef |
|---|---|---|
| Apple Search Ads (TR + DE) | $200 | 200–400 install |
| Meta Ads (FB + IG) (TR + BR + DE) | $250 | 500–1000 install |
| TikTok organic content | $0 | 100–500 organic install |
| Reddit ads (r/puzzlevideogames, r/casualgames) | $50 | 50 install |
| **Toplam UA** | **$500** | **~1000–2000 paid + 1000 organic** |

### 4.2 Reklam asset

- 30 sn gameplay video (vertical 9:16) × 3 varyant
- Static asset 5 (jar peak moment, character cast, mechanic showcase, CTA, testimonial)
- A/B test framework: 2 video + 2 static = 4 creative

### 4.3 Organik kanallar

- TikTok: Günlük gameplay clip (slot machine peak moment ASMR)
- Reddit: Devlog post weekly (r/IndieGaming, r/gamedev)
- Twitter / X: Behind-the-scenes thread
- Press release: Touch Arcade, Pocket Gamer

---

## 5. KPI İzleme Matriksi

### 5.1 Günlük metrikler

| Metrik | Tool | Hedef |
|---|---|---|
| Install rate | Firebase | 50–500/gün |
| D1 retention | Firebase | %42+ |
| D7 retention | Firebase | %22+ |
| Session length | Firebase | 8+ dakika |
| Crash-free rate | Crashlytics | %99.5+ |
| Store rating | App Store / Play | 4.5+ |
| Paying conversion | Firebase + IAP receipt | %2+ |
| ARPPU | IAP receipt sum | $10+ |
| ARPDAU | revenue/DAU | $0.10+ |

### 5.2 Haftalık review

- Cohort retention curve (D1, D3, D7, D14)
- Funnel drop-off (install → tutorial → first IAP)
- Top 3 fail level (zorluk eğrisi sorunu)
- En çok satın alınan SKU
- Ad fill rate (network performance)

---

## 6. Go / No-Go Karar Matriksi (Hafta 16)

| Senaryo | Aksiyon |
|---|---|
| Tüm KPI hedefte | **Global launch** + UA $5K ay |
| 5/8 KPI hedefte | 2 hafta polish (zorluk, monetization tweak) → tekrar test |
| 3/8 KPI hedefte | 4 hafta refactor (core loop, balance, art) |
| 1/8 KPI hedefte | **Pivot**: LASTPEG fallback veya konsept kapat |

### 6.1 KPI öncelik sırası (kritik)

1. D1 retention (en kritik — ilk izlenim)
2. D7 retention (engagement health)
3. Store rating (organic discoverability)
4. Crash-free rate (technical kalite)
5. Paying conversion (monetization viability)
6. ARPPU (revenue efficiency)
7. Session length (engagement depth)
8. D30 retention (long-term sticky)

---

## 7. Phase 2 Genişleme (Hafta 16+)

Pilot başarılı varsayımı:

### 7.1 Hafta 17–20 (Genişleme 1)
- ABD lansman
- Apple Search Ads $1K/hafta
- ASO optimization (keywords iterate)
- Bug fix sweep

### 7.2 Hafta 21–24 (Genişleme 2)
- Japonya + Güney Kore localization
- UA $2K/hafta
- Yeni event: "Spring Brew Festival" (limited skin + bonus level)

### 7.3 Hafta 25+ (Mature)
- Aylık event cadence
- Co-op feature beta
- Witch Pass V2 iterate
- Phase 3 prep: 2. oyun konsept

---

## 8. Sosyal Medya Planı

| Platform | Frekans | İçerik |
|---|---|---|
| TikTok | Günlük | Gameplay clip 15–60 sn |
| Twitter / X | 2x/hafta | Devlog + tease + community Q&A |
| Reddit | Haftalık | Devlog post (gamedev/indiegaming) |
| Instagram | 3x/hafta | Concept art + character spotlight |
| YouTube Shorts | Haftalık | Gameplay clip + dev commentary |
| Discord | Real-time | Community channel pre-launch |

---

## 9. Press Outreach

### 9.1 Hedef yayınlar

- Touch Arcade (mobile gaming)
- Pocket Gamer (mobile reviews)
- The Verge (tech)
- Polygon (mainstream gaming)
- Kotaku (gaming culture)
- Indie Game Lover (indie spotlight)

### 9.2 Pitch template

```
Subject: POURLE — Ball Sort meets Wordle (Solo dev project, soft launch [DATE])

Hi [Editor],

I'm a solo developer launching POURLE, a hybrid puzzle game combining the
satisfying liquid-pouring of Ball Sort Puzzle with Wordle's word-building
tension. After 12 weeks of solo development, the game soft launches in
Türkiye/Brazil/Germany on [DATE].

Key angles:
- 2 proven mechanics, 1 novel combination
- Royal Match-style production polish on solo budget (~$3K)
- Gentle monetization (no gambling-lite, no aggressive paywalls)
- 6 chapters, 30 episodes, 150 levels of mechanic evolution

Press kit: [URL]
Demo build (TestFlight): [URL]
Devlog: [URL]

Happy to answer questions or set up a quick demo call.

Thanks,
[Solo Dev Name]
```

---

## 10. Crisis Yönetimi

### 10.1 Olası sorunlar

| Sorun | Olasılık | Çözüm |
|---|---|---|
| Crash rate >%2 | Orta | Hotfix 24 saat içinde, store update |
| Negative review wave | Düşük | Reply individual, hotfix edilebilir bug fix |
| IAP receipt validation fail | Düşük | Server-side validation backup |
| Localization typo | Yüksek | Community feedback channel + hotfix |
| Trademarkia POURLE clash | Düşük | Fallback name plan (POPLET / MIXLE) |

### 10.2 Trademark sorunu olursa

- Hafta 12 öncesi: $99 Trademarkia search yapılmış olmalı.
- Clash bulunursa: 2 hafta name swap (POPLET veya MIXLE).
- Tüm asset rebrand: store listing + app icon + key art.

---

## 11. Soft Launch Bütçe Özeti

| Kalem | Maliyet |
|---|---|
| UA (4 hafta) | $500 |
| Press release service (PR Newswire / Indie kit) | $200 |
| Localization (10 dil pro check) | $300 |
| Soft launch buffer (sürpriz) | $200 |
| **Total** | **$1,200** |

---

## 12. Success Definition (Pilot Phase)

**Pilot success = Phase 2'ye yeşil ışık**:
- D1 retention ≥ %42
- D7 retention ≥ %22
- Store rating ≥ 4.5
- Paying conversion ≥ %2.0
- Crash-free ≥ %99.5

5/5 ✅ → Global launch.
3–4/5 → 1 ay polish.
0–2/5 → Pivot.

---

*Sürüm 1.0 — frozen design.*
