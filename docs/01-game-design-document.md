# 📋 POURLE — Final Game Design Document

**Versiyon**: 1.0 (Frozen — Üretim için bağlayıcı)
**Tarih**: 2026-04-28
**Sahibi**: Solo Developer
**Hedef lansman**: 12 hafta sonra (soft launch)

---

## 1. Executive Summary

### Ürün Kimliği

| Parametre | Değer |
|---|---|
| Oyun adı | **POURLE** (working title — Trademarkia kontrol bekliyor) |
| Tag line | "Pour. Spell. Win." |
| Tür | Casual mass-market puzzle (Ball Sort × Wordle hybrid) |
| Platform | iOS + Android |
| Engine | Unity 6 LTS (2D URP) |
| Geliştirme süresi | 12 hafta solo |
| Toplam yatırım | ~$3,000 + 280 saat emek |
| v4 Simulation Score | **4.50** |
| Tahmini D7 retention | 38% |
| Tahmini D30 retention | 22% |
| Tahmini ARPPU | $10–14 |
| Tahmini 1. yıl net kar | **$130K–380K** |
| Başarı ihtimali | %75 (Pivot Gate ile) |

### Hedef Kitle

- **Demografi**: 22–55 yaş, %50 kadın / %50 erkek (mass-market neutral cast)
- **Coğrafya**: ABD, Türkiye, Brezilya, Almanya, Meksika ana hedef
- **Davranış**: İş arası, ulaşımda, evening relax — kısa seanslar (5–15 dakika)
- **Mevcut alışkanlıklar**: Royal Match, Block Blast, Wordle, Ball Sort Puzzle oynayan kullanıcılar

### Niye POURLE Kazanır

1. **İki kanıtlanmış mekanik birleşimi**: Ball Sort Puzzle (500M+ indirme) × Wordle (50M+ kullanıcı) — boş pazar kesişim
2. **Royal Match formülü**: Light Saga meta + warm cozy art + slot-machine peak moments = $3B/yıl kanıtı
3. **Mekanik evrimi**: Her 2–3 episode'da yeni mini-mekanik = oyuncu sıkılmaz (30 episode = 12 farklı yenilik katmanı)
4. **Mass-market neutral**: Cast (mentor erkek + apprentice kadın + kedi) Royal Match'in King + Winston + Duke formülünün birebir uygulaması
5. **Solo yapılabilir**: 12 hafta, ~$3,000, kanıtlanmış pipeline

---

## 2. Vision Statement

> **"Casual mass-market puzzle players around the world need a game they can play during workplace breaks and transit — a game that feels familiar (Ball Sort + Wordle), looks warm and inviting (Royal Match smooth render), and rewards them with a satisfying slot-machine moment every few minutes. POURLE delivers exactly this."**

---

## 3. Core Pillars

### Pillar 1 — Familiar Mechanics, Fresh Combination
Ball Sort Puzzle'ın dokunsal sıvı dökme tatmini + Wordle'ın zihinsel kelime keyfi. İki kanıtlanmış mekanik tek oyunda. Onboarding sıfır — oyuncu 10 saniyede anlıyor.

### Pillar 2 — Royal Match Formula (Mass-Market Polish)
- Smooth 3D toon render (NOT painterly)
- Warm cozy palette (cream + amber + element colors)
- Slot-machine peak moments (jar seal celebration)
- Light Saga meta (chapter, episode, life, star, booster)
- Mass-market neutral characters (50/50 gender appeal)

### Pillar 3 — Never-Boring Mechanic Evolution
30 episode boyunca her 2–3 episode'da yeni mini-mekanik. Color Transform → Locked Caps → Frozen Bottles → Metallic Letters → Lava Bottles → Cosmic Spells. Sürekli tazelik.

### Pillar 4 — Story-Driven Retention
Master Octave (mentor) + Iris (apprentice) + Mochi (cat) cast. 6 chapter boyunca Iris çırak → master arc'ı. Her chapter Octave'in gizemli geçmişinden bir parça açılır. Cliffhanger'lar D7+ retention'ı destekler.

### Pillar 5 — Solo-Buildable Scope
- 12 hafta üretim
- ~120 unique sanat asset (AI + asset store ile yönetilebilir)
- 150 level (30 hand-designed boss + 120 procedural, BFS solver validated)
- Asset Store ~$95 + AI görsel ~$50 = düşük dış maliyet

---

## 4. What POURLE Is NOT

Açıklığa kavuşturulmalı — design freeze noktasında **NOT** kabul edilen tasarımlar:

- ❌ NOT a hardcore puzzle game (Picross/Sudoku premium niche kitle değil)
- ❌ NOT a children's edutainment game (Letter Lab değil — eğitim app değil)
- ❌ NOT a magical girl / anime-styled game (Iris natural look, NOT princess)
- ❌ NOT a Belle Époque sophisticated art piece (Royal Match cozy mass-market)
- ❌ NOT a witch-gothic atmosphere (Master Octave warm grandfather, NOT scary wizard)
- ❌ NOT a niche Asian-market specific (no paper lanterns / cherry blossoms / K-pop accents)
- ❌ NOT a clinical lab simulator (cozy apothecary, NOT chemistry class)
- ❌ NOT a gambling-lite (no Coin Master raid mechanics, no aggressive monetization)
- ❌ NOT a beer / coffee themed game (BREWBOX rejected for this reason)
- ❌ NOT a complex 3-mechanic hybrid (Ball Sort + Wordle = 2, no third layer like K-pop or Belle Époque)

---

## 5. Reference Documents

Bu doküman master overview. Detaylı bilgi için:

- **Faz planı (kod öncesi master roadmap)**: [`00-phase-plan.md`](00-phase-plan.md)
- **Mekanik kuralları**: [`02-mechanics.md`](02-mechanics.md)
- **Saga meta sistem**: [`03-saga-meta.md`](03-saga-meta.md)
- **Karakter detay**: [`04-characters.md`](04-characters.md)
- **6 chapter senaryoları**: [`05-story-scenarios.md`](05-story-scenarios.md)
- **Mekanik evrimi (her 2–3 episode)**: [`06-mechanic-evolution.md`](06-mechanic-evolution.md)
- **Monetizasyon**: [`07-monetization.md`](07-monetization.md)
- **Görsel stil**: [`08-visual-style.md`](08-visual-style.md)
- **12 haftalık üretim planı**: [`09-production-plan.md`](09-production-plan.md)
- **Soft launch stratejisi**: [`10-soft-launch-strategy.md`](10-soft-launch-strategy.md)
- **Risk + pivot gates**: [`11-risk-mitigation.md`](11-risk-mitigation.md)

---

## 6. Frozen Design Status

Bu doküman **donmuş tasarım**. Sonraki revizyonlar için:

- **Yeni karar gerekliyse**: Bu dokümana **revizyon tarihi + değişiklik notu** eklenir
- **Deviasyon önerisi**: 3-soru filtresinden geçmeli (CLAUDE.md'de detay)
- **Onay**: Tasarım sahibi (kullanıcı) onaylamadan değişmez

---

## 7. Success Definition

### Soft launch (Hafta 12–16)
- D1 retention ≥ 42%
- D7 retention ≥ 22%
- D30 retention ≥ 12%
- Store rating ≥ 4.5
- Paying conversion ≥ 2.0%

### 6 ay
- 100K–500K aktif kullanıcı
- $50K–200K aylık gelir
- En az 1 ülkede top 100 puzzle category

### 1 yıl
- 500K–2M aktif kullanıcı
- **$130K–380K net kar** (komisyon + UA + ops sonrası)
- Witch Pass 5K+ aktif aboneliği

### 2 yıl
- 2. oyun lansmanı (Saga meta kod reuse → 8 hafta)
- Portföy gelir $300K–700K/yıl
