# 🧬 06 — Mechanic Evolution Schedule

**Belge amacı**: Player'ı 30 episode boyunca sıkmamak için her 2–3 episode'da yeni mini-mekanik. Anti-boredom curriculum.

---

## 1. Felsefe

Royal Match'in başarı sırrı: 100+ level boyunca her 5–10 level'da yeni mekanik. POURLE 30 episode = 150 level. Hedef: **her 10–15 level yeni şey.**

**Kural**:
- Yeni mekanik tutorial-free olmalı (visual + Octave 1-cümlelik dialog yeterli).
- Önceki mekanik unutulmamalı — kombine edilebilir olmalı.
- Karmaşıklık eğrisi monoton artmamalı: bazı episode "rest" (önceki mekanik recombine).

---

## 2. Episode-by-Episode Evrim Tablosu

| Episode | Chapter | Mekanik Yenilik | Açıklama |
|---|---|---|---|
| 1 | 1 | Core Ball Sort + Wordle | Tap + pour + seal |
| 2 | 1 | (rest) | 4 element renk çeşitliliği artar |
| 3 | 1 | 4-jar challenge | Standart + Extra Jar booster intro |
| 4 | 1 | **5th element (Aether)** | Mor renk açılır |
| 5 | 1 | Chapter 1 Boss | 4-jar + Aether kompleks |
| 6 | 2 | **Color Transform** | Beyaz harfli berrak sıvı renge boyar |
| 7 | 2 | (rest) | Color transform pratiği |
| 8 | 2 | **Locked Caps (cork)** | 3 hamle sonra mantar açılır |
| 9 | 2 | (rest) | Locked + transform combo |
| 10 | 2 | Chapter 2 Boss | 6-jar combo |
| 11 | 3 | **Frozen Bottle (intro)** | İlk frozen jar, henüz kullanılmaz |
| 12 | 3 | **Heat Booster** | Frozen jar çözer |
| 13 | 3 | (rest) | Heat + locked combo |
| 14 | 3 | **Speed Brew bonus** | İlk bonus level — 60 sn limit |
| 15 | 3 | Chapter 3 Boss | Frozen + heat puzzle |
| 16 | 4 | **Metallic Letters** | Gold/Silver/Bronze element-coded |
| 17 | 4 | **No Hint bonus** | Hint booster kapalı pratik |
| 18 | 4 | (rest) | Metallic + frozen combo |
| 19 | 4 | **Ancient Spell Special** | Tek seviyede 3 mekanik birleşim |
| 20 | 4 | Chapter 4 Boss | Metallic + locked + frozen |
| 21 | 5 | **Lava Bottle (intro)** | Yanlış renk eritir |
| 22 | 5 | (rest) | Lava avoidance practice |
| 23 | 5 | **Master Word bonus** | 5–6 harfli dev şişe |
| 24 | 5 | **Cool Mist Booster** | Lava nötralizasyon |
| 25 | 5 | Chapter 5 Boss | Lava + cool mist + metallic |
| 26 | 6 | **Cosmic Spells** | 5–6 katmanlı dev cosmic jar |
| 27 | 6 | (rest) | Cosmic + frozen combo |
| 28 | 6 | **Cascade bonus** | Mühürlenince diğer şişelerden harf düşer |
| 29 | 6 | **Final Combo** | Tüm 8 mekanik birleşim |
| 30 | 6 | **Cosmic Master Boss** | Final boss — 7 jar, 4 mekanik |

---

## 3. Mekanik Detay Açıklamaları

### 3.1 Core Ball Sort + Wordle (Episode 1)

Temel mekanik. `02-mechanics.md`'de tam spec.

### 3.2 5th Element — Aether (Episode 4)

- Yeni renk: Mor `#9D4EDD`
- Davranış: Standart layer, sadece görsel zenginleşme
- Tutorial: Octave "Bu beşinci element. Diğerlerinden farklı görünür ama aynı kurallarla çalışır."
- Etki: Renk paleti 4 → 5, kelime kombinasyon arttar

### 3.3 Color Transform (Episode 6)

- Mekanik: Beyaz harfli "berrak sıvı" katman, üzerine renkli sıvı dökünce o renge boyar.
- Strategic: Berrak layer'ı doğru renge göre konumlandırma gerekir.
- Visual: Berrak → renge transform 200ms ripple animation.
- Tutorial: "Bu su renksiz. Ama renge dokunduğunda kendine bir renk seçer."

### 3.4 Locked Caps (Episode 8)

- Mekanik: Şişe başında mantar (cork). Mantar varken şişeye dökülemez.
- Açılma: 3 hamle sonra otomatik açılır, VEYA Hint booster ile manuel.
- Strategic: Player diğer şişelerle uğraşırken mantarlı şişe açılma sayacı işler.
- Visual: Mantar üstünde turning circle countdown 3 → 2 → 1 → açık.

### 3.5 Frozen Bottle (Episode 11)

- Mekanik: Şişe donmuş, içerik görünür ama dökülemez/eklenmez.
- Açılma: Heat Booster (Episode 12+).
- Strategic: Frozen şişe genelde "anahtar harf" içerir, doğru zamanda erit.
- Visual: Mavi-buz overlay + ice crystal partikül.

### 3.6 Heat Booster (Episode 12)

- Aktivasyon: Tap & sürükle frozen jar üzerine.
- Etki: Frozen state'i kaldırır, normal jar olur.
- Edinme: Coin (200), bonus level reward, Witch Pass.
- Limit: Seviye başı max 2 (game balance).

### 3.7 Speed Brew Bonus (Episode 14)

- Format: Tek seviye, 60 sn timer.
- Hedef: Max kelime mühürle.
- Reward: Coin × kelime sayısı + 1 booster.
- Frekans: Her chapter'da 1 (Chapter 3+).

### 3.8 Metallic Letters (Episode 16)

- Mekanik: Bazı katmanlar altın/gümüş/bronz harf (sıradan beyaz/koyu yerine).
- Davranış: Gold = aether match, Silver = earth, Bronze = fire (element kodlu).
- Kelime mühürleme: Metallic harfli kelime mühürleyince +20 coin bonus.
- Visual: Metallic shader ile parıltı.

### 3.9 No Hint Bonus (Episode 17)

- Format: Tek seviye, Hint booster kapalı.
- Hedef: Skill-only çözüm.
- Reward: 50 coin + ego boost.
- Frekans: Her chapter'da 1 (Chapter 4+).

### 3.10 Ancient Spell Special (Episode 19)

- Format: 1 büyük seviye, locked + frozen + metallic combo.
- Hedef: Master oyuncu testi.
- Reward: Exclusive jar skin + 200 coin.
- Frekans: Tekil event level, story-locked.

### 3.11 Lava Bottle (Episode 21)

- Mekanik: Lava şişe içinde sürekli akan kırmızı sıvı.
- Hatalı işlem: Yanlış renk dökerseniz, lava o katmanı eritir (kayıp).
- Strategic: Sadece doğru renkle yaklaş.
- Visual: Lava bubble partikül + ısı dalga shader.

### 3.12 Master Word Bonus (Episode 23)

- Format: Tek devasa şişe, 5–6 katman.
- Hedef: 5 veya 6 harfli kelime kur (örn. "BREWS", "SPELLS", "POURS").
- Reward: 100 coin + 2 booster.
- Frekans: Her chapter'da 1 (Chapter 5+).

### 3.13 Cool Mist Booster (Episode 24)

- Aktivasyon: Tap & sürükle lava jar üzerine.
- Etki: Lava state'i nötralize, geçici güvenli jar (3 hamle).
- Edinme: Coin (250), bonus reward, Witch Pass.
- Limit: Seviye başı max 1.

### 3.14 Cosmic Spells (Episode 26)

- Mekanik: Cosmic jar — 5 veya 6 katman kapasiteli.
- Kelime: 5–6 harfli kelime gerekli mühür için.
- Strategic: Daha uzun planlama, kelime sözlüğü daha kısıtlı.
- Visual: Yıldız partikülleri + galaksi background içinde.

### 3.15 Cascade Bonus (Episode 28)

- Format: Tek seviye, 4–5 jar.
- Mekanik: Bir jar mühürlenince, diğer jar'lardan rastgele 1 layer düşer.
- Strategic: Mühür sırası planlama.
- Frekans: Her chapter'da 1 (Chapter 6).

### 3.16 Final Combo (Episode 29) + Cosmic Master Boss (Episode 30)

- Format: Tüm mekanik birleşim.
- Episode 29-5: Locked + Frozen + Metallic + Lava aynı seviyede.
- Episode 30-5: Cosmic jar + Lava + Cascade dynamic + Time pressure.
- Reward: Game ending unlock + "Endless Brew" mode.

---

## 4. Anti-Boredom Mantığı

| Pattern | Kullanım |
|---|---|
| 2 episode yeni → 1 episode rest | Yeni mekanik + pratik |
| Combine, don't replace | Yeni mekanik eskisi unutmadan eklenir |
| Boss'un tüm mekanikleri zorlasın | Chapter sonları skill checkpoint |
| Bonus levels her chapter farklı tip | Format çeşitliliği |
| Sürpriz event (Episode 19) | Story-locked unique level |

---

## 5. Player Skill Eğrisi Tahmini

| Episode | Tahmini başarı oranı (oyuncu) |
|---|---|
| 1–5 | %95 (tutorial) |
| 6–10 | %85 (öğrenme) |
| 11–15 | %75 (zorluk eğrisi) |
| 16–20 | %70 (mid-game) |
| 21–25 | %65 (challenge) |
| 26–30 | %55 (mastery) |

Fail oranı = yeni hayat satın alma fırsatı = monetization.

---

## 6. Endless Brew (Post-Episode 30)

Chapter 6 sonrası açılır. Sonsuz prosedürel jeneratör. Mekanikler random kombinasyonu. Leaderboard global ve arkadaş arası.

- Difficulty rating sistemi (1–10).
- Daily challenge entegrasyonu.
- Witch Pass ekstra XP kaynağı.

---

## 7. Mekanik Üretim Maliyeti (Solo)

| Mekanik | Tahmini geliştirme süresi | Risk |
|---|---|---|
| Core Ball Sort + Wordle | 2 hafta (Hafta 1–2) | Düşük |
| Aether 5. element | 0.5 gün (renk + asset) | Düşük |
| Color Transform | 2 gün (shader + logic) | Orta |
| Locked Caps | 1 gün (timer logic) | Düşük |
| Frozen Bottle + Heat | 2 gün (state machine) | Orta |
| Metallic Letters | 1 gün (shader + score logic) | Düşük |
| Lava Bottle + Cool Mist | 2 gün (interaction logic) | Orta |
| Cosmic Spells | 1 gün (jar variant) | Düşük |
| Cascade dynamic | 2 gün (chain reaction) | Orta |
| Bonus level formats (4 tip) | 4 gün toplam | Düşük |

**Toplam mekanik dev süre**: ~17 gün → 12 hafta planında Hafta 4–10 arası dağıtılır.

---

*Sürüm 1.0 — frozen design.*
