# 🎮 02 — Core Mechanics

**Belge amacı**: POURLE çekirdek oynayışının tam kuralları. Programlamaya başlamadan önce kesin referans.

---

## 1. High-Level Loop (10 saniyede)

1. Oyuncu seviyeye girer → ekranda 4–7 cam apothecary şişesi görür.
2. Her şişe içinde renkli sıvı katmanları var. Her katmanın üzerinde tek harf yazılı.
3. **Tap**: Şişeye dokun → en üst katman havaya kalkar.
4. **Tap**: Başka şişeye dokun → katman üstüne dökülür (Ball Sort kuralı).
5. Tek renkten 4 katman dolan şişe → harfler **kelime** ediyorsa **mühürlenir** (Wordle).
6. Tüm şişeler mühürlü = seviye tamam.

---

## 2. Şişe (Jar) Spesifikasyonu

### 2.1 Yapısal kurallar

| Parametre | Değer |
|---|---|
| Maksimum kapasite | 4 katman |
| Minimum kapasite | 0 katman (boş) |
| Şişe tipi | `Standard`, `Locked` (cork), `Frozen`, `Lava` (Episode 8+ varyantlar) |
| Görsel boyut (mobile) | 180×320 px (ortalama 6.5" ekran) |
| Etkileşim alanı | Şişe + 12 px hitbox padding |

### 2.2 Şişe durumları

```
EMPTY        → boş (0 katman)
PARTIAL      → 1–3 katman, karışık veya tek renk
SINGLE_COLOR → 4 katman ama tek renk değil VEYA tek renk ama kelime değil
SEALED       → 4 katman tek renk + harfler geçerli kelime → kilitli
```

`SEALED` durumundaki şişeler oynanış sırasında etkileşime kapalı.

---

## 3. Sıvı Katmanı (Liquid Layer) Spesifikasyonu

### 3.1 Renk paleti (5 element)

| Element | Renk Hex | Tema |
|---|---|---|
| Fire | `#E63946` | kırmızı-turuncu sıcak |
| Water | `#1D7DBF` | gök mavi |
| Earth | `#5C8A3C` | orman yeşili |
| Air | `#F4D35E` | sarı-altın |
| Aether (Episode 4+) | `#9D4EDD` | mor (5. element kilidi açılır) |

### 3.2 Harf yerleşimi

- Her katman bir harf taşır (A–Z İngilizce, ı/ğ/ş Türkçe lokalizasyon eklemesi).
- Harf `katman_renk` ile uyumlu beyaz/koyu kontrast (renk üzerinde okunabilir).
- Harf yönü: alttan üste **doğal okuma yönü** (en alttan başlayan harf kelimenin ilk harfi).
- Ör: Şişede alttan üste `[B][R][E][W]` katmanları → kelime "BREW".

### 3.3 Renk Transform (Episode 6+)

- **Beyaz harfli berrak su** → renkli sıvıyla karışınca harf o renge boyar.
- Kural: Berrak (transparent) layer döküldüğü hedefin rengini alır.

---

## 4. Pour (Dökme) Mekaniği — Ball Sort Kuralı

### 4.1 Yasal hamle

1. Kaynak şişe **boş değil**.
2. Hedef şişe **dolu değil** (≤ 3 katman).
3. Hedef şişe **boş** VEYA en üst katman rengi kaynağın en üst katman rengi ile aynı.
4. Kaynak şişe **mühürlenmiş değil** (`SEALED`).
5. Hedef şişe **mühürlenmiş değil**.

### 4.2 Pour algoritması

```pseudocode
function attemptPour(source: Jar, target: Jar):
    if source.isEmpty() OR source.isSealed(): return ILLEGAL
    if target.isFull() OR target.isSealed(): return ILLEGAL
    sourceTop = source.peek()
    if target.isEmpty() OR target.peek().color == sourceTop.color:
        # Yeşil — dökme legal
        layersToMove = source.countConsecutiveTopColor()
        availableSpace = target.maxCapacity - target.count
        moveCount = min(layersToMove, availableSpace)
        for i in moveCount:
            target.push(source.pop())
        return SUCCESS
    return ILLEGAL_COLOR_MISMATCH
```

**Önemli**: Aynı renkten ardışık üst katmanlar tek hamlede dökülür (klassik Ball Sort).

### 4.3 Animasyon süreleri

| Olay | Süre |
|---|---|
| Şişe seçim glow | 150 ms |
| Şişe eğilme + dökme | 400 ms |
| Sıvı parabolic akış | 300 ms |
| Hedef sıvı ripple | 200 ms |
| Toplam tek dökme | ~700 ms |

Çoklu katman dökme: katman başına +120 ms ek.

---

## 5. Word Validation (Wordle Kuralı)

### 5.1 Mühür koşulları

Şişe `SEALED` olur:
1. Tam 4 katman dolu.
2. Tüm katmanlar **aynı renk**.
3. Alttan üste okuyunca harfler **geçerli kelime** (sözlükte var).
4. Kelime min 3 max 4 harf (4 katman = 4 harf, ancak 3-harfli kelimeler dolgu boş katmanla mühürlenebilir — özel mekanik).

### 5.2 Sözlük (10 dil)

| Dil | Sözlük kaynağı | Min kelime |
|---|---|---|
| EN | SOWPODS subset (3–4 harfli) | 1,200 |
| TR | TDK Türkçe (3–4 harfli) | 800 |
| DE | Duden çekirdek | 900 |
| ES | RAE çekirdek | 950 |
| PT | Aurélio çekirdek | 850 |
| FR | Larousse çekirdek | 900 |
| IT | Zingarelli çekirdek | 800 |
| RU | Ozhegov çekirdek | 1,000 |
| JA | Romanized JIS | 600 (özel kural — hece yapısı) |
| KO | Romanized KS | 600 |

JSON dosyaları `Assets/ScriptableData/Dictionaries/`. Çevrimdışı çalışır.

### 5.3 Kelime geçersizse

- 4 tek-renk dolduğu halde kelime yoksa → **şişe dolu ama mühürsüz**.
- Oyuncu hala içeriği farklı şişeye dökerek kombine edebilir (sözlüğe uygun olana kadar).
- Hint booster önerir (yakın geçerli kelime nasıl dizilebilir).

---

## 6. Slot-Machine Peak Moment (Mühür Kutlaması)

Royal Match formülü: %99 sakin oynanış + %1 patlayıcı kutlama.

### 6.1 SEALED tetikleyince:

| Süre | Olay |
|---|---|
| 0 ms | Tüm şişe içeriği titrer (10 px dampen sin) |
| 100 ms | Altın halka şişe etrafında doğar |
| 200 ms | Halka pulse büyür (1.0 → 1.4 scale) |
| 300 ms | Confetti partikül patlama (15 partikül, 60 frame) |
| 400 ms | Slot-machine SFX `coin_clink_x3.wav` |
| 500 ms | Haptic medium (CoreHaptics intensity 0.7) |
| 700 ms | Yıldız ekranı süslü tarzda büyür → puan sayacına eklenir |
| 1200 ms | Şişe sahneden uzaklaşıp "vault" simgesine uçar |

### 6.2 Combo (zincir mühür)

3 saniye içinde 2. şişe mühürlenirse → "DOUBLE SEAL" toast + 1.5x puan.
4. mühürlenirse → "MASTER BREW" toast + 2x puan + ekstra coin.

---

## 7. Win / Lose Koşulları

### Win

- **Tüm şişeler `SEALED`** = seviye tamam.
- Hamle saymıyor (zen/chill).
- Süre saymıyor (klasik seviyeler).
- Yıldız sistemi: hamle sayısına göre 1–3 yıldız (Saga meta detayı `03-saga-meta.md`).

### Lose

- Yasal hamle kalmadı + boş şişe yok + undo bitti = **fail**.
- Hayat sistemi: 5 hayat, fail → -1 hayat (`03-saga-meta.md`).
- Restart: hayat tüketmeden seviye baştan başlar (oyuncu seçer).

### Bonus level (Episode 14+)

- **Speed Brew**: 60 saniye limit, max kelime mühürle.
- **No Hint**: Hint booster kapalı.
- **Master Word**: Tek dev şişe, 5–6 harfli kelime.
- **Cascade**: Mühürlenince diğer şişelerden harf düşer.

---

## 8. Booster Etkileşimleri

| Booster | Etki | Aktive ediliş |
|---|---|---|
| Hint | Bir sonraki en iyi hamleyi parıltıyla gösterir | Tap & confirm |
| Extra Jar | Bir ek geçici şişe ekler (1 hamle ömür) | Tap & confirm |
| Undo | Son hamleyi geri alır | Tap (ücretsiz 3/seviye) |
| Auto Sort | Tüm tek-renk katmanları otomatik sıralar | Tap & confirm |
| Heat (Ep 14+) | Donmuş şişeyi çözer | Tap & sürükle hedefe |
| Cool Mist (Ep 24+) | Lava şişeyi nötralize eder | Tap & sürükle hedefe |

Booster ekonomi detayı: `03-saga-meta.md` ve `07-monetization.md`.

---

## 9. Special Jar Türleri (Mekanik Evrim)

| Tip | Episode | Davranış |
|---|---|---|
| Standard | 1+ | Normal |
| Locked Cap | 8+ | Mantar tıkalı, 3 hamle sonra açılır |
| Frozen | 11+ | Donmuş, sadece Heat booster çözer |
| Color Transform | 6+ | Beyaz layer girince renk değişir |
| Metallic | 16+ | Gold/Silver/Bronze → element-coded harf |
| Lava | 21+ | Yanlış renk girerse 1 layer erir |
| Cosmic | 26+ | 5–6 katmanlı dev şişe |

Detaylı evrim: `06-mechanic-evolution.md`.

---

## 10. Oyuncu Girdileri (Input)

| Etkileşim | Davranış |
|---|---|
| Single tap (jar) | Seç / dök |
| Double tap (jar) | Yakınlaştır (sadece 5+ jar seviye) |
| Long press (jar) | Detay tooltip (kelime ipucu) |
| Swipe down (HUD) | Pause menu |
| Swipe up | Kelime sözlük history |
| Pinch | Disabled (tasarım kararı) |

Erişilebilirlik: VoiceOver / TalkBack açıkken jar isimlendirme "Jar 3, contains B-R-E gradient red".

---

## 11. Performans Hedefi

| Cihaz | FPS | RAM |
|---|---|---|
| iPhone 11 (2019) | 60 | <250 MB |
| Samsung A52 (2021) | 60 | <300 MB |
| iPhone 8 (2017) | 30 | <200 MB |
| Pixel 4a (2020) | 60 | <280 MB |

Crash rate hedefi: <%0.3.

---

## 12. Edge Case Davranışları

- **Tüm şişeler dolu, mühürlü değil**: Undo otomatik aktive (1 ücretsiz).
- **Aynı renk 5+ katman**: Mantıksal imkansız (4 limit), defansif: error log + jar reset.
- **Geçersiz kelime spam**: Oyuncu 4 katmanı tek renk yapar ama kelime değil → "Try another word" tooltip 3 sn.
- **Çift dil aktif**: Sistem dili birincil, ikincil sözlük fallback kapalı (kafa karıştırıcı).

---

*Sürüm 1.0 — design freeze, üretim için bağlayıcı.*
