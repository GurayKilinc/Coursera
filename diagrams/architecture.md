# 🏗️ Unity Scene & System Architecture

**Belge amacı**: POURLE Unity projesinin sahne akışı, manager singleton katmanı, data flow.

---

## 1. Scene Flow (Top Level)

```mermaid
flowchart TD
    Bootstrap[Bootstrap Scene] --> SaveLoad{Save File Exists?}
    SaveLoad -->|No| FirstLaunch[First Launch Tutorial]
    SaveLoad -->|Yes| MainMenu[MainMenu Scene]
    FirstLaunch --> MainMenu
    MainMenu -->|Play| ChapterMap[ChapterMap Scene]
    MainMenu -->|Settings| SettingsOverlay[Settings Overlay]
    MainMenu -->|Store| StoreOverlay[Store Overlay]
    MainMenu -->|Daily Bloom| Gameplay[Gameplay Scene]
    ChapterMap -->|Episode Selected| CutsceneOpening[Cutscene Opening]
    CutsceneOpening --> Gameplay
    Gameplay -->|Win| LevelComplete[LevelComplete Popup]
    Gameplay -->|Fail| LevelFail[LevelFail Popup]
    LevelComplete -->|Episode Last Level| CutsceneClosing[Cutscene Closing]
    LevelComplete -->|Mid Episode| Gameplay
    CutsceneClosing -->|Chapter Last Episode| ChapterFinale[ChapterFinale Cutscene]
    CutsceneClosing -->|Mid Chapter| ChapterMap
    ChapterFinale --> ChapterMap
    LevelFail -->|Retry / Out of Lives| MainMenu
    LevelFail -->|Refill IAP| Gameplay
```

---

## 2. Singleton Manager Layer (DontDestroyOnLoad)

```mermaid
flowchart LR
    GC[GameController] --> SD[SceneDirector]
    GC --> SM[SaveManager]
    GC --> LM[LifeManager]
    GC --> EM[EconomyManager]
    GC --> BM[BoosterManager]
    GC --> AD[AudioDirector]
    GC --> HD[HapticDirector]
    GC --> Loc[LocalizationManager]
    GC --> Anal[AnalyticsManager]
    GC --> IAP[IAPController]
    GC --> Ads[AdsController]
    GC --> Dlg[DialogueDirector]

    SM --> PlayerPrefs[(PlayerPrefs)]
    SM --> LocalJSON[(JSON Local)]
    Anal --> Firebase[(Firebase)]
    IAP --> Apple[(App Store IAP)]
    IAP --> Google[(Google Play IAP)]
    Ads --> AdMob[(AdMob)]
    Ads --> AppLovin[(AppLovin MAX)]
```

---

## 3. Gameplay Scene — System Detail

```mermaid
flowchart TD
    LevelLoader[LevelLoader] -->|Loads LevelSO| LC[LevelController]
    LC --> JarController[JarController]
    LC --> InputController[InputController]
    LC --> WinDetector[WinDetector]
    LC --> ComboTracker[ComboTracker]

    InputController -->|Tap Source| JarController
    InputController -->|Tap Target| JarController
    JarController -->|Pour Request| BSV[BallSortValidator]
    BSV -->|Valid| JarController
    BSV -->|Invalid| InvalidFeedback[Shake + SFX]

    JarController -->|Filled| WV[WordValidator]
    WV -->|Word in Dict| JarSeal[JarSeal Animation]
    WV -->|Not in Dict| WaitState[Wait for More Pours]

    JarSeal --> ComboTracker
    JarSeal --> AD[AudioDirector: SealSFX]
    JarSeal --> HD[HapticDirector: Medium]
    JarSeal --> WinDetector

    WinDetector -->|All Sealed| WinFlow[Trigger Win]
    WinFlow --> StarCalc[Calculate Stars by moves]
    WinFlow --> EM[EconomyManager: Award Coins]
    WinFlow --> SM[SaveManager: Persist Progress]
```

---

## 4. ScriptableObject Data Hierarchy

```mermaid
flowchart TD
    GameMaster[GameMasterSO] --> Chapter1[ChapterSO 1]
    GameMaster --> Chapter2[ChapterSO 2]
    GameMaster --> Chapter3[ChapterSO 3]
    GameMaster --> Chapter4[ChapterSO 4]
    GameMaster --> Chapter5[ChapterSO 5]
    GameMaster --> Chapter6[ChapterSO 6]

    Chapter1 --> Theme1[ThemeSO: Cozy Apothecary]
    Chapter1 --> Ep1[EpisodeSO 1]
    Chapter1 --> Ep2[EpisodeSO 2]
    Chapter1 --> Ep3[EpisodeSO 3]
    Chapter1 --> Ep4[EpisodeSO 4]
    Chapter1 --> Ep5[EpisodeSO 5]

    Ep1 --> CO1[CutsceneSO Opening]
    Ep1 --> L1[LevelSO 1-1]
    Ep1 --> L2[LevelSO 1-2]
    Ep1 --> L3[LevelSO 1-3]
    Ep1 --> L4[LevelSO 1-4]
    Ep1 --> L5[LevelSO 1-5]
    Ep1 --> CC1[CutsceneSO Closing]

    L1 --> Jar1[JarConfigSO]
    L1 --> Jar2[JarConfigSO]
    L1 --> Jar3[JarConfigSO]

    Jar1 --> Liq1[LiquidLayerSO]
    Liq1 --> Color[ColorEnum: Fire]
    Liq1 --> Letter[Char: B]
```

---

## 5. Save Data Schema

```json
{
  "playerProfile": {
    "playerId": "uuid",
    "createdAt": "2026-04-28T10:00:00Z",
    "currentChapter": 2,
    "currentEpisode": 6,
    "currentLevel": 3,
    "totalStars": 47,
    "totalCoins": 1240
  },
  "lifeState": {
    "currentLives": 4,
    "lastRefillTimestamp": 1714312345,
    "infiniteLivesUntil": null
  },
  "boosterInventory": {
    "hint": 5,
    "extraJar": 3,
    "undo": 12,
    "autoSort": 2,
    "heat": 1,
    "coolMist": 0
  },
  "purchases": {
    "noAds": false,
    "starterPack": true,
    "witchPassActive": true,
    "witchPassExpires": 1716904345,
    "themesOwned": ["frozen", "volcano"]
  },
  "levelProgress": [
    {"levelId": "1-1", "stars": 3, "completedAt": 1714000000, "bestMoves": 6},
    {"levelId": "1-2", "stars": 2, "completedAt": 1714001000, "bestMoves": 9}
  ],
  "settings": {
    "language": "tr",
    "musicVolume": 0.7,
    "sfxVolume": 1.0,
    "hapticEnabled": true,
    "notificationsEnabled": true
  }
}
```

---

## 6. Pour Algoritma Sequence

```mermaid
sequenceDiagram
    participant User
    participant InputController
    participant JarController
    participant BallSortValidator
    participant WordValidator
    participant AudioDirector
    participant HapticDirector
    participant WinDetector

    User->>InputController: Tap Jar A (source)
    InputController->>JarController: SelectSource(A)
    JarController->>JarController: Highlight A glow
    User->>InputController: Tap Jar B (target)
    InputController->>JarController: AttemptPour(A, B)
    JarController->>BallSortValidator: ValidateMove(A, B)

    alt Move legal
        BallSortValidator-->>JarController: SUCCESS + layerCount
        JarController->>JarController: Animate pour (700ms)
        AudioDirector->>AudioDirector: Play pour SFX
        HapticDirector->>HapticDirector: Light haptic
        JarController->>WordValidator: CheckSeal(B)
        alt Word in dictionary
            WordValidator-->>JarController: SEALED
            JarController->>JarController: Trigger seal animation
            AudioDirector->>AudioDirector: Slot machine SFX
            HapticDirector->>HapticDirector: Medium haptic
            JarController->>WinDetector: NotifySealed(B)
            WinDetector->>WinDetector: Check all jars sealed?
            alt All sealed
                WinDetector-->>JarController: WIN!
            end
        else Not a word yet
            WordValidator-->>JarController: WAIT
        end
    else Move illegal
        BallSortValidator-->>JarController: ILLEGAL
        JarController->>JarController: Shake animation
        AudioDirector->>AudioDirector: Buzz SFX
    end
```

---

## 7. Module Dependency Graph

```mermaid
flowchart TD
    Core[Core Module] --> Logic[Logic Module]
    Core --> Save[Save Module]
    Logic --> Jars[Jars Module]
    Logic --> Dict[Dictionary Module]
    Jars --> Visuals[Visual/Anim Module]
    SagaMeta[SagaMeta Module] --> Core
    SagaMeta --> Save
    SagaMeta --> Economy[Economy Module]
    Boosters[Boosters Module] --> Logic
    Boosters --> Economy
    Mentor[Mentor/Cutscene] --> Core
    Mentor --> Loc[Localization]
    UI[UI Module] --> SagaMeta
    UI --> Economy
    UI --> Boosters
    UI --> Loc
    Audio[Audio Module] --> Core
    Haptic[Haptic Module] --> Core
    Analytics[Analytics] --> Core
    Analytics --> Economy
```

---

## 8. Build Pipeline

```mermaid
flowchart LR
    Source[Git: main branch] --> CI[Unity Cloud Build]
    CI --> AndroidBuild[Android APK]
    CI --> iOSBuild[iOS IPA]
    AndroidBuild --> InternalTest[Play Console Internal Test]
    iOSBuild --> TestFlight[TestFlight Internal]
    InternalTest -->|Pass| ProdAndroid[Play Console Production]
    TestFlight -->|Pass| AppStore[App Store Connect Production]
    ProdAndroid --> Users
    AppStore --> Users
    Users --> Analytics[Firebase Analytics]
    Users --> Crash[Crashlytics]
    Analytics --> Dashboard[Dev Dashboard]
    Crash --> Dashboard
```

---

## 9. Performans Profiling Hedefleri

| Metrik | Hedef | Tool |
|---|---|---|
| FPS (mid-range Android) | 60 | Unity Profiler |
| RAM (peak) | <300 MB | Memory Profiler |
| Build size | <150 MB | Build Report |
| Cold start time | <2 sn | Firebase Performance |
| Scene load (Gameplay) | <1 sn | Unity Profiler |
| Crash-free rate | %99.5+ | Crashlytics |

---

## 10. CI/CD Strategy

- **main branch**: production-ready code
- **dev branch**: active development
- **feature/X branches**: isolated work
- Unity Cloud Build her commit'te otomatik APK + IPA üretir
- TestFlight + Play Console internal track auto-deploy
- Production deploy manuel onay (her hafta)

---

*Sürüm 1.0 — design freeze referansı.*
