# 💰 07 — Monetization Strategy

**Belge amacı**: 7 SKU + ads + Witch Pass abonelik. Royal Match level AMI = 3 (mass-market lite).

---

## 1. Felsefe — Royal Match AMI = 3

**Aggressive Monetization Index (AMI)**:
- 1 = saf premium (Monument Valley)
- 5 = Coin Master raid mechanics + aggressive pop-ups
- 3 = mass-market casual sweet spot

**POURLE = AMI 3**: Reklam izlenebilir-opt-in, hayat sistem yumuşak, 7 SKU dengeli, Witch Pass değerli, NO gambling-lite mekanikler.

**Hedef KPI**:
- Paying conversion: %2.0–3.5
- ARPPU: $10–14
- Ad ARPDAU: $0.04–0.08
- IAP/Ad split: %75 IAP / %25 Ad

---

## 2. SKU Tablosu (7 Total)

| # | SKU | Fiyat | İçerik | Hedef segment |
|---|---|---|---|---|
| 1 | No Ads | $3.99 | Tüm reklamları kaldırır (opt-in 30sn rewarded ad'lar dahil) | Reklam alerjili |
| 2 | Starter Pack | $2.99 | İlk 7 gün içinde sadece — 500 coin + 10 booster + 3 hayat refill | Yeni paying intent |
| 3 | Life Refill (small) | $0.99 | 5 hayat anlık | Anlık çözüm |
| 4 | Life Refill (24h) | $4.99 | Sınırsız hayat 24 saat | Marathon player |
| 5 | Booster Bundle (small) | $1.99 | 6 booster mix | Casual buyer |
| 6 | Booster Bundle (large) | $4.99 | 20 booster mix | Engaged buyer |
| 7 | Coin Pack (3 tier) | $0.99 / $4.99 / $19.99 | 200 / 1500 / 8000 coin | Soft currency buyer |

**Dürüst not**: 7 SKU + Witch Pass + Theme Bundle = toplam 9 IAP slot. Royal Match formülü.

---

## 3. Witch Pass (Subscription)

| Parametre | Değer |
|---|---|
| Fiyat | $7.99 / 30 gün |
| Auto-renew | Opsiyonel (varsayılan açık) |
| İçerik | 30 gün premium track (ödül her gün) + ücretsiz track (sadece az ödül) |
| Tahmini conversion | Paying user %15–20 |
| Tahmini retention | İlk ay %60, ikinci ay %40 |

### Premium track ödül takvimi (30 gün)

| Gün | Ücretsiz track | Premium track |
|---|---|---|
| 1 | 50 coin | 500 coin + 5 booster |
| 5 | 100 coin | Iris jar skin |
| 10 | 1 booster | 1000 coin + 10 booster |
| 15 | 100 coin | Master Octave portrait frame |
| 20 | 50 coin | Mochi UI tema |
| 25 | 1 booster | Cosmic Spells background |
| 30 | 200 coin | 2500 coin + Sınırsız hayat 24 saat |

**Algılanan değer**: ~$15. Fiyat: $7.99. Net "fırsat" hissi → conversion driver.

---

## 4. Theme Bundle (Cosmetic)

Royal Match formülü: Cosmetic skin paketleri.

| Tema | Fiyat | İçerik |
|---|---|---|
| Frozen Theme Bundle | $4.99 | İce jar skin + frosty UI + sound pack |
| Volcano Theme Bundle | $4.99 | Lava jar skin + ember UI + crackle sounds |
| Cosmic Theme Bundle | $4.99 | Galaxy jar skin + cosmic UI + ambient music |

Total theme variants: 3 launch + 3 post-launch (Phase 2).

Cosmetic-only — gameplay etki yok. Sadece collector / fan.

---

## 5. Reklam Stratejisi

### 5.1 Reklam türleri

| Tip | Frekans | Reward |
|---|---|---|
| Rewarded Video | İsteğe bağlı | +1 hayat / +20 coin / +1 booster (oyuncu seçer) |
| Interstitial | Her 3 fail / 1 reklam | Yok (yumuşak interstitial) |
| Banner | Yok | (mass-market casual'da banner kullanmıyoruz) |

### 5.2 Reklam yumuşatma kuralları

- Rewarded ad: Oyuncu HAYIR diyebilir, no penalty.
- Interstitial: 3 fail sonrası max 1 ad / oturum.
- No Ads SKU: Tüm interstitial'leri kaldırır + rewarded'ları kaldırır.
- Ad network: AdMob + AppLovin MAX waterfall.

### 5.3 Tahmini ad gelir

- Daily active users 100K (6. ay):
- Rewarded ad % izleme: %25 DAU → 25K ad/gün
- Rewarded eCPM ortalama $15 (USA $20, TR $5)
- Daily ad gelir: ~$375 → aylık ~$11K
- Interstitial daha düşük (~$3K/ay)
- Toplam ad gelir tahmini: ~$14K/ay (6. ay sonrası)

---

## 6. Konversiyon Funnel

```
1000 indirme
└── 850 retain D1 (%85)
    └── 600 retain D7 (%60)
        └── 250 retain D30 (%25)
            └── 25 paying user (%2.5 conversion)
                └── ~$300 revenue (ARPPU $12)
```

Hedef: 100K indirme/ay (6. ay) = ~$30K/ay IAP + ~$14K/ay ad = ~$44K/ay total.

---

## 7. First-Time Paywall Stratejisi

| Trigger | Prompt | Conversion umudu |
|---|---|---|
| 1. fail | (yok) | - |
| 5. fail (Episode 3) | Starter Pack lifetime offer | %5 |
| 1. hayat tükenmesi | Life refill $0.99 | %3 |
| Episode 5 finish | Witch Pass intro | %2 |
| Day 7 milestone | Coin pack $4.99 | %4 |

**Asla**:
- Hard paywall (devam edemezsin)
- Episode kilit (sadece $$ ile aç)
- Forced ads (skip-imkansız)

---

## 8. ARPDAU + LTV Modeli

| Metrik | Hedef | Top tier ref |
|---|---|---|
| ARPDAU (USA) | $0.18 | Royal Match $0.40 |
| ARPDAU (TR) | $0.06 | TR ortalama $0.12 |
| LTV (USA) | $4.50 | Royal Match $12 |
| LTV (TR) | $1.50 | TR ortalama $3 |
| CPI break-even (USA) | $4.50 | Hedef $2–3 (Apple Search Ads) |
| CPI break-even (TR) | $1.50 | Hedef $0.50 (organic dominant) |

---

## 9. Whale (Yüksek harcama) Segmenti

POURLE casual mass-market — whale sınırlı (top %1 oyuncular).

**Whale offer ladder** (in-game shop):
- $19.99 Coin Pack (8000 coin)
- $49.99 Mega Pack (sadece event'lerde — coin + booster + skin)
- $99.99 Ultimate Pack (Phase 2 — kuvvetli ekonomi data sonrası)

Royal Match'in whale ekonomisi POURLE'de kopyalanmaz — design felsefesi gereği fair-play.

---

## 10. Ekonomi Balance

### Coin akış (input/output)

| Coin source | Günlük tahmini |
|---|---|
| Win rewards | 60–100 coin |
| Daily login | 50 coin |
| Ad rewards | 60 coin (3 max) |
| Episode finish | 50 coin (haftalık) |
| **Toplam günlük** | **~200 coin organic** |

| Coin sink | Maliyet |
|---|---|
| Booster | 50–200 coin |
| Hayat refill | 200 coin |
| Theme cosmetic | 1500 coin (ortalama) |

**Balans**: Free player günlük 200 coin organic kazanır → 1 booster veya 1 hayat refill alır. Pay-to-skip değil pay-for-comfort.

---

## 11. Compliance + Etik

- COPPA / GDPR ad consent prompt (ilk açılış).
- 13 yaş altı kullanıcı: Personalized ads disabled.
- Auto-renew abonelik: Apple App Store + Google Play standart prompt.
- Dark pattern yok: Cancel subscription flow 2 tap.
- Refund: Apple/Google standart pencere içinde otomatik.

---

## 12. Year-1 Revenue Tahmini

| Çeyrek | Aktif kullanıcı | Aylık gelir |
|---|---|---|
| Q1 (soft launch) | 5–20K | $3K–10K |
| Q2 (TR + BR + DE) | 50–100K | $15K–40K |
| Q3 (global launch) | 200–500K | $60K–150K |
| Q4 (mature) | 500K–1M | $100K–250K |

**Yıl 1 toplam tahmini**: $400K–1.2M gross. Net (after platform fee + UA + ops): **$130K–380K**.

---

## 13. Phase 2 Monetization (Post-Launch)

- Co-op (arkadaşa hayat gönder) — sosyal monetization
- Tournament event (haftalık leaderboard + entry coin)
- Limited-time skins (FOMO buyer segmenti)
- Battle Pass V2 (Witch Pass evolution)

Phase 2 = retention + LTV maksimize, Phase 1 = pure foundation.

---

*Sürüm 1.0 — frozen design.*
