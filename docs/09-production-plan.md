# 🛠️ 09 — Production Plan (12 Hafta Solo Sprint)

**Belge amacı**: Hafta-by-hafta üretim takvimi, pivot gates, Unity architecture, dış maliyet planı.

---

## 1. Üst-Düzey Takvim

| Hafta | Faz | Çıktı | Pivot Gate |
|---|---|---|---|
| 1 | Foundation | Unity proje kurulumu, ScriptableObject şemaları | - |
| 2 | Core Logic | Ball Sort + Wordle çekirdek algoritmasi | - |
| 3 | UX Prototype | Tap-to-pour, peak moment fix | - |
| 4 | MVP | İlk 5 level oynanabilir build | **Gate 1**: Eğlenceli mi? |
| 5 | Saga Meta | Hayat, harita, episode structure | - |
| 6 | Mekanik Evrim 1 | Color transform + Locked caps + Frozen | - |
| 7 | Mekanik Evrim 2 | Heat / Metallic / Lava / Cool Mist | - |
| 8 | Polish & Balance | 30 episode oynanabilir | **Gate 2**: Balance OK mı? |
| 9 | Monetization | IAP integration, Witch Pass, ad SDK | - |
| 10 | Cutscenes & Story | 30+ cutscene, dialog, voice (text-only) | - |
| 11 | Audio & Final Polish | Müzik + SFX + haptic + crash fix | - |
| 12 | Soft Launch | Türkiye + Brezilya + Almanya | **Gate 3**: KPI OK mı? |

**Tahmini günlük çalışma**: 4 saat × 5 gün = 20 saat/hafta × 12 hafta = ~240 saat. Buffer ~40 saat → **280 saat total**.

---

## 2. Hafta-Hafta Detaylı

### Hafta 1 — Foundation

**Hedefler**:
- Unity 6 LTS proje oluştur
- Git repo yapısı (this folder)
- Folder structure: Scripts/, ScriptableData/, Art/, Audio/, Scenes/
- ScriptableObject şemaları yaz: ChapterSO, EpisodeSO, LevelSO, JarConfigSO, MechanicSO, BoosterSO, ThemeSO, CutsceneSO

**Çıktı**: Compile-eden boş proje + 8 SO scripti. Bootstrap scene açılıyor.

---

### Hafta 2 — Core Logic

**Hedefler**:
- `Jar.cs` — şişe state, layer stack, fill/empty
- `LiquidLayer.cs` — color + letter struct
- `BallSortValidator.cs` — pour legal kontrol
- `WordValidator.cs` — sözlük lookup
- `LevelController.cs` — seviye loop
- Unit tests (NUnit) tüm logic için

**Çıktı**: Headless test (visual yok), 10 test seviyesi otomatik solve eder.

---

### Hafta 3 — UX Prototype

**Hedefler**:
- Tap interaction (`InputController.cs`)
- Pour animation (Tween: DOTween free)
- Liquid layer visual (sprite + shader)
- Letter sprite render
- İlk slot-machine peak moment animasyonu

**Çıktı**: Bir seviyeyi gözle görerek oyna.

---

### Hafta 4 — MVP

**Hedefler**:
- 5 hand-designed level (Episode 1)
- Octave + Iris + Mochi placeholder portrait
- Basic UI: HUD, fail/win popup
- Android build → 5 arkadaş test
- **PIVOT GATE 1**: Eğlenceli mi? Tutorial-free 30 saniyede anlıyor mu?

**Karar matriksi**:
- Eğlenceli → devam
- Eğlenceli değil → core loop tweak (1 hafta buffer)
- Tamamen başarısız → pivot to alternative game (LASTPEG fallback)

---

### Hafta 5 — Saga Meta

**Hedefler**:
- LifeManager (5 hayat, 30 dk yenilenme)
- ChapterMap UI (yatay scroll, 30 episode düğümü)
- Yıldız sistemi (1–3 ⭐)
- Coin economy
- Daily Bloom seviye loader
- Save/Load (PlayerPrefs + JSON)

**Çıktı**: Tam meta loop çalışır — fail → bekle → tekrar dene flow.

---

### Hafta 6 — Mekanik Evrim 1

**Hedefler**:
- Color Transform mechanic (beyaz → renkli)
- Locked Cap mechanic (mantar + countdown)
- Frozen Bottle visual + state
- Episode 6, 8, 11 tutorial cutscene placeholder

**Çıktı**: Episode 1–11 (33 level) oynanabilir.

---

### Hafta 7 — Mekanik Evrim 2

**Hedefler**:
- Heat Booster (Frozen unlock)
- Metallic Letters (Episode 16)
- Lava Bottle + Cool Mist Booster (Episode 21, 24)
- Cosmic Spells jar (Episode 26)

**Çıktı**: Episode 12–26 (45 level) oynanabilir.

---

### Hafta 8 — Polish & Balance

**Hedefler**:
- 30 hand-designed boss level (1/episode) + 120 procedural (auto-validated solver)
- BFS solver — her seviye için optimal hamle hesaplama
- Star threshold ayarı
- Difficulty curve check
- Bonus level formats (Speed Brew, No Hint, Master Word, Cascade)
- **PIVOT GATE 2**: Balance OK mı? Tester completion rate %70+?

**Çıktı**: 150 level oynanabilir, başarı eğrisi makul.

---

### Hafta 9 — Monetization

**Hedefler**:
- Unity IAP integration (Apple + Google)
- AdMob SDK (banner disabled, rewarded + interstitial)
- AppLovin MAX waterfall
- 7 SKU + Witch Pass + Theme Bundle slot
- Receipt validation (Apple StoreKit / Google Play Billing)
- Test purchases (sandbox)

**Çıktı**: Tüm SKU sandbox'da satın alınabilir.

---

### Hafta 10 — Cutscenes & Story

**Hedefler**:
- 30 episode cutscene (giriş + final)
- 6 chapter cutscene
- Dialog text (10 dil için extraction-ready format)
- Cutscene player (slide-in + fade-out + skip)
- Localization framework (i18n JSON-based)

**Çıktı**: Tüm hikaye akışı oynar.

---

### Hafta 11 — Audio & Final Polish

**Hedefler**:
- Müzik: 6 chapter theme + ambient (asset store / royalty-free)
- SFX: 30+ unique sound (pour, seal, fail, button, peak)
- Haptic: CoreHaptics + Niceft Vibrations
- Crash fix sweep (Unity Cloud Diagnostics)
- Performance profiling (60 fps mid-range target)
- App icon final design (3 variant test)
- Store listing draft (8 screenshots + 30s promo video)

**Çıktı**: Build production-ready.

---

### Hafta 12 — Soft Launch

**Hedefler**:
- Türkiye + Brezilya + Almanya store launch
- Apple Search Ads $200 budget
- Meta UA $300 budget
- Firebase Analytics monitoring
- Crashlytics on
- Daily KPI check

**Çıktı**: 5–20K indirme. KPI matriksi:

| Metrik | Hedef | Alt limit |
|---|---|---|
| D1 retention | %42+ | %30 |
| D7 retention | %22+ | %12 |
| D30 retention | %12+ | %6 |
| Store rating | 4.5+ | 4.0 |
| Paying conversion | %2.0+ | %1.0 |
| Crash-free rate | %99.5+ | %99.0 |

**PIVOT GATE 3**: Tüm metrik hedefte → global launch + UA artır. Yarısı altsa → 1 ay polish + tekrar test.

---

## 3. Unity Architecture

### 3.1 Scene yapısı

| Scene | İçerik |
|---|---|
| `Bootstrap.unity` | İlk yüklenen, save load + scene route |
| `MainMenu.unity` | Ana menü, settings, store |
| `ChapterMap.unity` | 30 episode harita |
| `Gameplay.unity` | Aktif puzzle |
| `Cutscene.unity` | Dialog overlay |
| `LoadingTransition.unity` | Geçiş ekranı |

### 3.2 Manager Singleton katmanı

```
GameController (DontDestroyOnLoad)
├── SceneDirector
├── SaveManager
├── LifeManager
├── EconomyManager (coin)
├── BoosterManager
├── AudioDirector
├── HapticDirector
├── LocalizationManager
├── AnalyticsManager (Firebase)
├── IAPController
├── AdsController
└── DialogueDirector (cutscene)
```

### 3.3 Folder structure

```
Assets/
├── Scripts/
│   ├── Core/              # GameController, SceneDirector
│   ├── Jars/              # Jar, LiquidLayer, Letter
│   ├── Logic/             # BallSortValidator, WordValidator, BFSSolver
│   ├── SagaMeta/          # ChapterMap, EpisodeManager, LifeManager
│   ├── Mentor/            # Octave + Iris + Mochi cutscene system
│   ├── PeakMoment/        # JarSeal celebration, ComboTracker
│   ├── Boosters/          # Hint, ExtraJar, Undo, AutoSort, Heat, CoolMist
│   ├── BonusLevels/       # SpeedBrew, NoHint, MasterWord, Cascade
│   ├── UI/                # Menus, HUD, popups
│   ├── Audio/
│   ├── Haptics/
│   ├── Localization/
│   └── Economy/           # IAPController, AdsController, CoinBank
├── ScriptableData/
│   ├── Chapters/          # 6 ChapterSO
│   ├── Episodes/          # 30 EpisodeSO
│   ├── Levels/            # 150 LevelSO
│   ├── Mechanics/         # 12 MechanicSO
│   ├── Boosters/          # 6 BoosterSO
│   ├── Themes/            # 6 ThemeSO
│   └── Dictionaries/      # 10 dil JSON sözlük
├── Art/
│   ├── Sprites/
│   ├── Animations/
│   ├── Themes/
│   └── Shaders/
├── Audio/
│   ├── Music/
│   ├── SFX/
│   └── Voice/
└── Scenes/
```

---

## 4. Dış Bağımlılıklar (Asset Store + AI)

| Item | Kaynak | Maliyet |
|---|---|---|
| DOTween | Asset Store | $15 |
| TextMeshPro | Unity built-in | $0 |
| Niceft Vibrations | Asset Store | $20 |
| AdMob SDK | Google free | $0 |
| AppLovin MAX | Free | $0 |
| Firebase | Google free tier | $0 |
| 6 müzik track | Asset Store / Epidemic Sound | $30 |
| 30 SFX | Freesound + Asset Store | $20 |
| AI görsel (Sora/Midjourney) | $10/ay × 3 ay | $30 |
| Trademarkia search | $99 | $99 |
| Domain (pourle.com) | $12/yıl | $12 |
| Apple Developer | $99/yıl | $99 |
| Google Play Developer | $25 one-time | $25 |
| **Toplam** | | **~$350** |

UA bütçe (12 hafta soft launch): $500.

**Total external cost**: ~$850. Buffer: $2,150 → toplam $3,000 budget.

---

## 5. Solo Developer Pratikleri

### 5.1 Daily ritmi
- Sabah: 2 saat code
- Akşam: 2 saat playtest / asset / planning
- 5 gün/hafta

### 5.2 Sanity preservation
- Pazartesi sabah daily standup (kendine):
  - Geçen hafta ne yaptım?
  - Bu hafta ne yapacağım?
  - Bloker var mı?
- Cuma sonu: Build deploy + 1 saat playtest

### 5.3 Burnout önleme
- Pazar tatil zorunlu
- Hafta 6'da 2 günlük buffer (sürpriz problem için)
- Her milestone sonrası küçük ödül (kendine)

---

## 6. Risk Mitigation Buffer

Her sprint sonunda 1 günlük buffer dahil. Total 12 günlük buffer = 12 hafta planı içinde.

Aşılırsa: Hafta 8 ve Hafta 11 de 2 günlük "polish only" buffer var.

Detay: `11-risk-mitigation.md`.

---

## 7. Quality Gates

| Gate | Geçme kriteri |
|---|---|
| Hafta 4 (MVP) | 5 arkadaş 15 dakikadan çok oyna, 4/5 "eğlenceli" der |
| Hafta 8 (Balance) | 100 procedural level %70+ tester completion |
| Hafta 11 (Final polish) | Crash rate <%0.5, performance 60 fps mid-range |
| Hafta 12 (Soft launch) | KPI matriksinin %50+ hedefte |

---

## 8. Tools

- **IDE**: Visual Studio Code + Unity extension
- **Source control**: Git + GitHub
- **Asset bundling**: Unity Addressables
- **CI/CD**: Unity Cloud Build (free tier)
- **Crash reporting**: Firebase Crashlytics
- **Analytics**: Firebase + Unity Analytics
- **Communication**: (yok — solo)

---

*Sürüm 1.0 — frozen design.*
