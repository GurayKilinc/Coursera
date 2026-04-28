# 🗺️ 03 — Saga Meta System

**Belge amacı**: Royal Match formülünün Saga meta katmanı — hayat, harita, episode, yıldız, booster, Witch Pass.

---

## 1. Meta Loop Hiyerarşisi

```
Game
└── Chapter (6 toplam)
    └── Episode (chapter başı 5 = toplam 30)
        └── Level (episode başı 5 = toplam 150)
            └── Move (oyuncu hamlesi)
```

- **Level**: Tek seviyeli puzzle (3–5 dakika).
- **Episode**: 5 level paketi + cutscene + mekanik mini-yenilik.
- **Chapter**: 5 episode + büyük cutscene + theme değişimi + boss-y final.
- **Game**: 6 chapter = 150 level = ~12–18 saat ana içerik + sonsuz prosedürel.

---

## 2. Hayat (Life) Sistemi

Royal Match birebir uygulaması:

| Parametre | Değer |
|---|---|
| Maksimum hayat | 5 |
| Yenilenme süresi | 30 dakika / hayat |
| Tam yenileme | 2 saat 30 dakika |
| Kullanım | Fail = -1 hayat. Win = hayat etkilenmez. Restart = -0 hayat. |
| Stoklanabilir? | Hayır, max 5 |
| Refill (IAP) | $0.99 = 5 hayat anlık. $4.99 = sınırsız 24 saat. |
| Refill (arkadaş) | Yok (sosyal layer Phase 2) |
| Refill (reklam) | 30 saniye reklam = 1 hayat. Günde max 3 kez. |

### Cliffhanger pattern

Royal Match psikoloji: Cutscene gösterimi sırasında "ama şimdi devam etmek istiyorum, hayatım yok" hissi → bir hayat satın alma intent peak.

---

## 3. Yıldız Sistemi

Her seviye 1–3 yıldız.

| Yıldız | Koşul |
|---|---|
| 1 ⭐ | Seviye tamamlandı (her ne kadar hamle) |
| 2 ⭐ | Optimal hamle sayısının %150 altı |
| 3 ⭐ | Optimal hamle sayısının %120 altı |

**Optimal hamle**: BFS solver tarafından hesaplanan minimum (level design test sırasında lock'lanır).

Yıldız kullanımı:
- Chapter ilerleme (her chapter 80+ ⭐ gerekir kilit açma)
- Cosmetic unlock (jar skin, theme)
- Witch Pass premium track ekstra ⭐ kazanır

---

## 4. Chapter Map

### 4.1 Görsel düzen

Royal Match-vari ilerleme yolu:
- 30 episode düğümü (5 chapter × 5 episode + 6. chapter 5 episode)
- Yatay scroll harita
- Mevcut episode parıltıyla işaretli
- Tamamlanmış episode altın checkmark
- Kilitli episode kilit ikonu + "Ulaş 3⭐ Episode X-Y"

### 4.2 Theme değişimleri

| Chapter | Tema | Renk paleti |
|---|---|---|
| 1 — First Brew | Cozy apothecary | Cream + amber + warm wood |
| 2 — Color Magic | Renk patlaması | Tüm 4 element + beyaz transform |
| 3 — Frozen Element | Buzulmuş kütüphane | Soft icy blue + silver |
| 4 — Ancient Spells | Hidden library | Burgundy + gold + leather |
| 5 — Volcano Brew | Volkan keşfi | Lava red + obsidian + ember orange |
| 6 — Cosmic Master | Yıldız çatısı | Cosmic purple + starfield + aether |

---

## 5. Episode Yapısı

Her episode 5 level + 1 başlangıç cutscene + 1 final cutscene.

```
Episode X başlangıç
└── Cutscene (15–30 sn) "Master Octave introduces new mini-mechanic"
    └── Level X-1 (kolay - tutorial)
    └── Level X-2 (orta)
    └── Level X-3 (orta)
    └── Level X-4 (zor)
    └── Level X-5 (boss-style, ultra zor)
        └── Final cutscene (15–30 sn) "Iris reaction + story beat"
```

Cutscene rejimi: skip butonu var (3 saniye long-press).

---

## 6. Booster Sistemi

### 6.1 Booster türleri (6 toplam)

| Booster | Çekirdek mekanik | Episode ilk açılış |
|---|---|---|
| Hint | Sonraki en iyi hamleyi gösterir | Episode 1 |
| Extra Jar | 1 hamlelik ek şişe | Episode 3 |
| Undo | Son hamleyi geri al | Episode 1 (3 ücretsiz/seviye) |
| Auto Sort | Tek-renk katmanları otomatik sıralar | Episode 5 |
| Heat | Frozen jar çözer | Episode 14 |
| Cool Mist | Lava jar nötralize | Episode 24 |

### 6.2 Booster ekonomi

| Edinme yolu | Maliyet |
|---|---|
| Coin satın alma | 50–200 coin/booster |
| Bonus seviye ödülü | 1–3 booster random |
| Daily login | 1 booster (rotating) |
| Witch Pass | Haftalık 2 booster bundle |
| IAP bundle | $1.99 = 6 booster, $4.99 = 20 booster |

---

## 7. Coin (Soft Currency)

| Edinme yolu | Miktar |
|---|---|
| Level win | 5–15 coin (zorluğa göre) |
| 3⭐ bonus | +10 coin |
| Episode finish | +50 coin |
| Chapter finish | +200 coin |
| Daily login (gün 7) | +100 coin |
| Reklam izleme | +20 coin (günlük max 3) |
| IAP | $0.99 = 200, $4.99 = 1500, $19.99 = 8000 |

Coin harcama:
- Booster satın alma
- Hayat refill (200 coin = 5 hayat)
- Theme cosmetic unlock

---

## 8. Witch Pass (Subscription)

Royal Match Royal Pass formülü.

| Parametre | Değer |
|---|---|
| Süre | 30 gün |
| Fiyat | $7.99/ay |
| Ücretsiz track | 30 gün boyunca, çoğu küçük ödül |
| Premium track | Witch Pass alanlar — premium ödül her gün |

### 8.1 Premium track ödülleri (örnek 30 gün)

| Gün | Premium ödül |
|---|---|
| 1 | 500 coin + 5 booster |
| 5 | Exclusive Iris jar skin |
| 10 | 1000 coin + 10 booster |
| 15 | Master Octave portrait frame |
| 20 | Mochi mascot UI tema |
| 25 | Cosmic Spells background |
| 30 | 2500 coin + Sınırsız hayat 24 saat |

Pass holders: total ~$15 değer / $7.99 — algılanan fırsat.

---

## 9. Daily Bloom (Günlük puzzle)

Royal Match'in "Daily Royale" formülü.

- Her gün UTC 00:00 yenilenir.
- Tek seviye, özel zorluk eğrisi (ortalama 2⭐ hedef).
- Tamamlamak: +30 coin + 1 booster + Daily Streak +1.
- Streak ödülleri: 7 gün → 200 coin, 14 gün → exclusive jar, 30 gün → premium jar set.

---

## 10. Bonus Levels (Episode 14+)

Mekanik tazeleme:

| Bonus tip | Frekans | Episode başlangıç |
|---|---|---|
| Speed Brew | 1 / chapter | Episode 14 (Chapter 3) |
| No Hint | 1 / chapter | Episode 17 (Chapter 4) |
| Master Word | 1 / chapter | Episode 22 (Chapter 5) |
| Cascade | 1 / chapter | Episode 27 (Chapter 6) |

Bonus level tamamlama: +100 coin + Witch Pass XP +50.

---

## 11. Progresyon Eğrisi

| Episode | Hedef oyuncu seviyesi | Tahmini süre |
|---|---|---|
| 1–5 | Newbie tutorial | 1–2 gün |
| 6–10 | Casual day-2 | 3–5 gün |
| 11–15 | Engaged day-7 | 7–10 gün |
| 16–20 | Habituated day-14 | 14–20 gün |
| 21–25 | Devoted day-21 | 21–28 gün |
| 26–30 | Expert day-30+ | 30–45 gün |

Sonsuz prosedürel: Episode 30 sonrası "Endless Brew" — auto-generate level + leaderboard.

---

## 12. Saga Meta Architecture (Code)

ScriptableObject yapısı:

```csharp
ChapterSO
├── chapterId: int
├── title: string
├── theme: ThemeSO
├── unlockEpisode: int (önceki chapter son episode)
├── episodes: EpisodeSO[]
└── finalCutscene: CutsceneSO

EpisodeSO
├── episodeId: int
├── title: string
├── startCutscene: CutsceneSO
├── levels: LevelSO[5]
├── newMechanic: MechanicSO (varsa)
└── endCutscene: CutsceneSO

LevelSO
├── levelId: int
├── jars: JarConfigSO[]
├── difficulty: enum (Easy, Medium, Hard, Boss)
├── optimalMoves: int (BFS solver)
├── starThresholds: int[3]
└── boosterRestrictions: BoosterFlags
```

Detay: `09-production-plan.md` Unity architecture.

---

*Sürüm 1.0 — frozen design.*
