# 🛡️ 11 — Risk Mitigation & Pivot Gates

**Belge amacı**: Bilinen riskler + her risk için backup plan + 3 ana pivot gate.

---

## 1. Risk Matriksi (Heatmap)

| Risk | Olasılık | Etki | Heatmap |
|---|---|---|---|
| Trademark POURLE clash (Trademarkia) | Düşük | Yüksek | 🟡 |
| Solo developer burnout | Orta | Yüksek | 🟠 |
| Mekanik eğlenceli değil (Hafta 4 Gate) | Düşük | Çok yüksek | 🔴 |
| Balance bozuk (Hafta 8 Gate) | Orta | Yüksek | 🟠 |
| Soft launch KPI hedefin altında (Hafta 12 Gate) | Orta | Çok yüksek | 🔴 |
| Crash rate >%2 | Düşük | Yüksek | 🟡 |
| App Store reject | Düşük | Orta | 🟢 |
| Sözlük lokalizasyon hatası | Yüksek | Düşük | 🟢 |
| AI görsel asset Royal Match feel veremiyor | Orta | Orta | 🟡 |
| UA bütçe yetersiz | Yüksek | Orta | 🟡 |
| Pazarda 3rd-party "Ball Sort + Wordle" çıkar | Düşük | Çok yüksek | 🟡 |

---

## 2. Pivot Gate 1 — Hafta 4 (MVP Fun Test)

### Geçme kriteri
- 5 arkadaşın 4'ü "eğlenceli" der
- En az 3 kişi "bir kere daha oynar mıydım?" sorusuna evet der
- Tutorial-free 30 saniye içinde core mechanic anlaşılır

### Geçemezse: Aksiyon planı

**A. Core loop tweak (1 hafta buffer)**:
- Pour kuralı yumuşat (renk strict yerine soft match)
- Word validation hint daha cömert
- Peak moment SFX/visual güçlendir
- Re-test 1 hafta sonra

**B. Core loop temelinden değiştir**:
- Word mekaniğini opsiyonel yap (Ball Sort dominant)
- Wordle layer'ı ekstra puan kaynağına dönüştür
- Risk: Niche kayma → mass market hedef değişir

**C. Pivot to fallback game (LASTPEG)**:
- Eğer Hafta 4'te core fundamentally yanlış → 4 hafta kayıp, LASTPEG (zen peg solitaire) projesine geç
- Zaman maliyeti: 4 hafta + 8 hafta yeniden = 12 hafta
- Bu durumda lansman 6 ay sonraya iter

**Karar matriksi**:
- 4/5 eğlenceli → devam et (PASS)
- 2-3/5 → A planı (1 hafta tweak)
- 0-1/5 → C planı (pivot)

---

## 3. Pivot Gate 2 — Hafta 8 (Balance Check)

### Geçme kriteri
- 100 procedural seviye %70+ tester completion rate
- Ortalama seviye süresi 2–4 dakika (target)
- Difficulty curve monoton-NOT (yani bazı kolay break'ler var)
- Hint booster usage %30 altında (over-reliance değil)

### Geçemezse: Aksiyon planı

**A. Difficulty rebalance (3 gün)**:
- BFS solver re-run, optimal hamle threshold ayarla
- Hand-designed levels gözden geçir
- Procedural generator parametre tweak

**B. Tutorial expansion (2 gün)**:
- Episode 1–3 daha yumuşak başlangıç
- Hint cümlecik daha açıklayıcı
- Mochi UI assistant aktif rolü artır

**C. Mechanic complexity reduce**:
- Cosmic Spells'i basitleştir (5–6 letter yerine 4–5)
- Lava bottle hatasında 1 layer yerine 0 layer eritme (forgiveness)
- Locked cap countdown 3 yerine 5 hamle

---

## 4. Pivot Gate 3 — Hafta 16 (KPI Soft Launch Review)

### Geçme kriteri (5 KPI hedef)

| KPI | Hedef |
|---|---|
| D1 retention | %42+ |
| D7 retention | %22+ |
| Store rating | 4.5+ |
| Paying conversion | %2.0+ |
| Crash-free | %99.5+ |

### Geçme matriksi

| KPI durumu | Aksiyon |
|---|---|
| 5/5 ✅ | Global launch + UA $5K/ay |
| 4/5 ✅ | 2 hafta zoom on weakest KPI, retest |
| 3/5 ✅ | 4 hafta polish + retest |
| 2/5 ✅ | 6 hafta refactor (core loop OR monetization) |
| 0–1/5 ✅ | Pivot or shut down (acı karar) |

---

## 5. Spesifik Risk Çözümleri

### 5.1 Trademark POURLE clash

**Mitigation**:
- Hafta 1'de Trademarkia $99 search yap
- Clash bulunursa: POPLET veya MIXLE fallback ($99 ek search)
- Hafta 4'e kadar isim final
- Asset rebrand 2 günde mümkün (icon + store listing)

### 5.2 Solo developer burnout

**Mitigation**:
- Pazar günleri zorunlu tatil
- Hafta 6'da 2 günlük buffer
- Her milestone sonrası ödül (kendine)
- Sosyal yalıtım kontrol — haftada 1 gün arkadaşla
- Egzersiz minimum 30 dk/gün

**Sıkıntı sinyalleri** (kendine soru):
- Sabah motivation %50 altı 3 gün üst üste mi?
- Code'a girince anksiyete mi?
- "Bu proje işe yaramayacak" düşüncesi sürekli mi?

3 evet → 3 günlük tatil, sonra rotasyon.

### 5.3 AI görsel asset Royal Match feel veremiyor

**Mitigation**:
- Hafta 3'te art direction lock — 5 test prompt deneme
- Royal Match smooth render fail ederse → 2D illustrative fallback (Procreate basit toon)
- Asset Store'dan hazır character pack — $30–50
- Backup: Profesyonel illustrator $500 (Fiverr) — 5 character + UI set

### 5.4 Pazar rakip çıkar

**Mitigation**:
- Devlog public — first-mover psychology
- Pre-launch waitlist (TikTok / Twitter)
- POURLE name register IP olarak (Trademarkia post-pilot)
- Differentiator: 30 episode mekanik evrim — kopya zor

### 5.5 UA bütçe yetersiz

**Mitigation**:
- Pilot bütçe $500, eğer KPI iyiyse Apple/Google feature submission ücretsiz
- Press outreach (Touch Arcade, Pocket Gamer) 0 cost
- TikTok organic — ASMR peak moment slot machine clip viral potansiyel
- Reddit organic — r/puzzlevideogames, r/gamedev devlog

### 5.6 Crash rate >%2

**Mitigation**:
- Hafta 11'de Unity Cloud Diagnostics + manual stress test
- Crashlytics enable
- Hotfix protocol: 24 saat reaction time
- Backup: Önceki build'e revert (Unity Cloud Build version control)

### 5.7 Sözlük lokalizasyon hatası

**Mitigation**:
- Native speaker review her dil ($300 budget pro check)
- Community feedback channel (Discord)
- Hotfix-able dictionary (JSON external file, app update gerek değil)

---

## 6. Schedule Buffer Stratejisi

| Buffer kaynağı | Süre |
|---|---|
| Sprint sonları (12 hafta × 1 gün) | 12 gün |
| Hafta 6 buffer (sürpriz) | 2 gün |
| Hafta 8 polish | 2 gün |
| Hafta 11 final polish | 3 gün |
| **Total buffer** | **19 gün** |

19 gün = ~%16 buffer of 280 saat plan. Çoğu risk içinde absorbe edilir.

---

## 7. Kategorik Backup Plans

### 7.1 Konsept başarısız olursa: LASTPEG (Zen Peg Solitaire)

Backup oyun: 33-hole peg solitaire + premium zen art.
- Üretim süresi: 8 hafta (mekanik basit)
- Bütçe: $1,500
- Hedef ARPPU: $14 (premium one-time IAP)
- Hedef pazar: USA + Almanya (premium casual)

Risk: Daha küçük pazar (zen niche), ama doğrulanmış (Monument Valley benchmark).

### 7.2 Soft launch başarısız ama core eğlenceli: POURLE V2

- Mekanik core korunur
- Monetization light-touch yumuşat (paywall'ları kaldır)
- Reposition: Premium one-time IAP $4.99 (Block Blast Pro modeli)
- Yeniden lansman 4 hafta sonra

### 7.3 Hiç bir şey çalışmazsa

- Coursera + freelance ile borç ödeme
- Project archive olarak kaydet (öğrenilen şeyler kıymetli)
- 6 ay sonra portföy değerlendirme

---

## 8. Yatırım vs Geri Dönüş Yağmuru

| Senaryo | Olasılık | Year-1 net |
|---|---|---|
| Best case (KPI hedefin %150+) | %15 | $400K–800K |
| Hedef case (KPI hedefte) | %50 | $130K–380K |
| Underperform (50–80% hedef) | %20 | $30K–80K |
| Failure (LASTPEG pivot) | %10 | -$2K (sunk) ama LASTPEG potential $50K |
| Total shutdown | %5 | -$3K |

**Beklenen değer (EV)**: ~$140K (probability-weighted).

---

## 9. Yerleşik Discipline (Pivot Yapma Kuralları)

Pivot kararı vermeden önce:

1. **Veri kanıtı**: Algı değil, KPI data.
2. **3 günlük "sleep on it"**: Acil panik kararı kaçır.
3. **Ölçülmüş alternatif**: Pivot hedefi de KPI matriksi var mı?
4. **Sunk cost reddi**: "Zaten 8 hafta yatırdım" → bu argüman geçersiz.

---

## 10. Project Health Dashboard

Her hafta cuma günü 30 dakika review:

- [ ] Bu hafta planlanan görevlerin %80'i tamamlandı mı?
- [ ] Bloker var mı? (3 günden fazla stuck)
- [ ] Burnout sinyali var mı?
- [ ] Sprint hedefi gerçekçi mi?
- [ ] Buffer kullanım oranı?
- [ ] Cumartesi-Pazar tatili planlandı mı?

---

*Sürüm 1.0 — frozen design.*
