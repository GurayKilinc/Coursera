# 📈 Chapter Flow Diagram (Player Progression)

**Belge amacı**: Oyuncunun 30 episode boyunca journey haritası — mekanik açılış, story beat, monetization touchpoint senkronu.

---

## 1. Yüksek-Düzey Player Journey

```mermaid
flowchart TD
    Start([First Launch])
    Start --> Tutorial[Episode 1 Tutorial]
    Tutorial --> Ep1_5[Episodes 1-5: First Brew]
    Ep1_5 -->|D1 retention check| Hook1{Hooked?}
    Hook1 -->|No| Churn1[Churn — Free user lost]
    Hook1 -->|Yes| Ep6_10[Episodes 6-10: Color Magic]

    Ep6_10 -->|D7 retention check| Engaged{Engaged?}
    Engaged -->|No| Churn2[Soft churn — Win-back push]
    Engaged -->|Yes + Starter Pack| Ep11_15[Episodes 11-15: Frozen]

    Ep11_15 --> Ep16_20[Episodes 16-20: Ancient Spells]
    Ep16_20 -->|D30 retention check| Habituated{Daily player?}
    Habituated -->|Yes + Witch Pass| Ep21_25[Episodes 21-25: Volcano]
    Ep21_25 --> Ep26_30[Episodes 26-30: Cosmic Master]
    Ep26_30 --> Endless[Endless Brew Mode]
    Endless --> WhalePath[Whale path: themes + bundles]

    Churn1 --> WinbackPush1[Day 3 push: Free 5 hearts]
    Churn2 --> WinbackPush2[Day 14 push: New chapter unlocked]
    WinbackPush1 --> Ep1_5
    WinbackPush2 --> Ep6_10
```

---

## 2. Episode Detail Flow

```mermaid
flowchart LR
    EpisodeStart([Episode X start]) --> OpeningCutscene[Opening Cutscene]
    OpeningCutscene --> NewMechanicIntro{New mechanic?}
    NewMechanicIntro -->|Yes| MechanicTutorial[Mini-tutorial 5sn]
    NewMechanicIntro -->|No| Level1[Level X-1]
    MechanicTutorial --> Level1
    Level1 -->|Win| Level2[Level X-2]
    Level1 -->|Fail| FailLoop[Fail Loop]
    Level2 -->|Win| Level3[Level X-3]
    Level3 -->|Win| Level4[Level X-4]
    Level4 -->|Win| Level5[Level X-5 Boss]
    Level5 -->|Win| ClosingCutscene[Closing Cutscene]
    ClosingCutscene --> ChapterCheck{Last episode of chapter?}
    ChapterCheck -->|Yes| ChapterFinale[Chapter Finale]
    ChapterCheck -->|No| EpisodeComplete([Episode complete])
    ChapterFinale --> EpisodeComplete

    FailLoop -->|Lives > 0| Restart[Restart level]
    FailLoop -->|Lives = 0| BlockerScreen[Wait or Buy lives]
    BlockerScreen -->|Buy| Restart
    BlockerScreen -->|Wait| RestartLater[Restart 30 min later]
```

---

## 3. Mekanik Açılış Timeline

```mermaid
gantt
    title Mekanik Evrim — 30 Episode
    dateFormat X
    axisFormat %s

    section Chapter 1
    Core Ball Sort + Wordle      :done, ep1, 0, 1
    4-jar challenge              :done, ep3, 2, 1
    5th Element (Aether)         :done, ep4, 3, 1

    section Chapter 2
    Color Transform              :active, ep6, 5, 1
    Locked Caps                  :active, ep8, 7, 1

    section Chapter 3
    Frozen Bottle                :ep11, 10, 1
    Heat Booster                 :ep12, 11, 1
    Speed Brew Bonus             :ep14, 13, 1

    section Chapter 4
    Metallic Letters             :ep16, 15, 1
    No Hint Bonus                :ep17, 16, 1
    Ancient Spell Special        :ep19, 18, 1

    section Chapter 5
    Lava Bottle                  :ep21, 20, 1
    Master Word Bonus            :ep23, 22, 1
    Cool Mist Booster            :ep24, 23, 1

    section Chapter 6
    Cosmic Spells                :ep26, 25, 1
    Cascade Bonus                :ep28, 27, 1
    Final Combo + Boss           :ep30, 29, 1
```

---

## 4. Monetization Touchpoint Mapping

```mermaid
flowchart TD
    Day0[Day 0: First Launch] --> NoIAP[No IAP prompt — pure onboarding]
    NoIAP --> Day1[Day 1: Episode 2-3]
    Day1 --> StarterPack[Starter Pack offer popup<br/>$2.99 — 7-day limited]
    StarterPack -->|5% buy| ConvertedPaying[Paying user]
    StarterPack -->|95% skip| Day2[Day 2: Continue Free]

    Day2 --> Day5[Day 5: Episode 5-6]
    Day5 --> WitchPassFirstSee[Witch Pass intro<br/>$7.99/month]
    WitchPassFirstSee -->|2% subscribe| WitchPassSubscriber

    Day5 --> Day7[Day 7: Episode 7-8]
    Day7 --> CoinPackOffer[Coin Pack contextual<br/>$0.99 / $4.99]

    Day7 --> Day14[Day 14: Episode 14-15]
    Day14 --> ThemeBundle[Theme Bundle Frozen<br/>$4.99 cosmetic]

    Day14 --> Day30[Day 30: Episode 25+]
    Day30 --> WhaleOffer[Mega Pack offer<br/>$19.99]

    ConvertedPaying --> AdditionalPurchases[Recurring: Coin packs, Boosters, Lives]
    WitchPassSubscriber --> WitchPassRenewal[Auto-renew month 2]
```

---

## 5. Retention Curve Tahmini

```mermaid
xychart-beta
    title "Retention Curve (% of Day 0 cohort)"
    x-axis [D0, D1, D3, D7, D14, D30, D60, D90]
    y-axis "% retained" 0 --> 100
    line [100, 42, 30, 22, 15, 12, 9, 7]
```

**Hedef değerler**:
- D1: %42+ (Royal Match benchmark %48)
- D7: %22+ (Royal Match %26)
- D30: %12+ (Royal Match %15)
- D90: %7+ (long-term sticky)

---

## 6. Cliffhanger Pattern

Her chapter sonunda bir story beat reveal → ertesi gün açma sebebi:

| Chapter | Cliffhanger Reveal |
|---|---|
| 1 | "Niye beni seçtin Master?" — sorulmuş ama cevapsız |
| 2 | Mysterious frozen bottle from Octave's old friend |
| 3 | Mochi'nin gerçek sahibi Octave'in eski yoldaşı |
| 4 | Octave'in adventurer geçmişi açığa çıkar |
| 5 | Iris solo expedition — Octave's friend's keepsake |
| 6 | Iris becomes Mistress, Octave returns to mountains |

Her cliffhanger oyuncuyu ertesi gün geri çağırır → D7 retention'ın %75+ kısmı bu pattern'e bağlı.

---

## 7. Star Earnings Curve

```mermaid
xychart-beta
    title "Cumulative Stars by Episode"
    x-axis [Ep5, Ep10, Ep15, Ep20, Ep25, Ep30]
    y-axis "Stars" 0 --> 90
    line [10, 25, 40, 55, 70, 85]
```

3⭐ × 5 level × 6 chapter = 90 max. Tahmini ortalama 75 (oyuncu çoğu seviyede 2-3⭐).

---

## 8. Funnel Drop-off Tahmini

```mermaid
flowchart TD
    Install[1000 Installs] -->|85%| Tutorial[850 Complete Tutorial]
    Tutorial -->|85%| D1[722 D1 retain]
    D1 -->|65%| D7[469 D7 retain]
    D7 -->|55%| D30[258 D30 retain]
    D30 -->|9.7% of D30| Pay[25 paying users]
    Pay -->|ARPPU $12| Revenue[$300 lifetime revenue]
```

Hedef: 1000 install → $300 LTV gross → ~$200 net (after 30% platform fee).

CPI break-even: ~$0.20 (very cheap markets like TR organic).

---

## 9. Soft Launch Geographic Funnel

```mermaid
flowchart LR
    GlobalImpression[Global Impressions] --> TR[Türkiye 40%]
    GlobalImpression --> BR[Brezilya 35%]
    GlobalImpression --> DE[Almanya 25%]

    TR --> TR_Install[5K install]
    BR --> BR_Install[5K install]
    DE --> DE_Install[2K install]

    TR_Install -->|D1 45%| TR_D1[2.25K D1]
    BR_Install -->|D1 40%| BR_D1[2.0K D1]
    DE_Install -->|D1 50%| DE_D1[1.0K D1]

    TR_D1 -->|Pay 1.8%| TR_Pay[40 paying]
    BR_D1 -->|Pay 1.5%| BR_Pay[30 paying]
    DE_D1 -->|Pay 3.5%| DE_Pay[35 paying]

    TR_Pay -->|ARPPU $7| TR_Rev[$280]
    BR_Pay -->|ARPPU $6| BR_Rev[$180]
    DE_Pay -->|ARPPU $14| DE_Rev[$490]
```

DE en yüksek ARPPU, TR + BR hacim — strateji doğrulanır.

---

## 10. Witch Pass Subscription Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Free: New User
    Free --> WitchPassPreview: D5 prompt
    WitchPassPreview --> Free: Skip
    WitchPassPreview --> WitchPassActive: Subscribe ($7.99)
    WitchPassActive --> WitchPassActive: Daily reward claim
    WitchPassActive --> ChurnRisk: 25 days elapsed
    ChurnRisk --> WitchPassActive: Auto-renew
    ChurnRisk --> Cancelled: User cancels
    WitchPassActive --> WinBack: Day 30 expired
    WinBack --> WitchPassActive: Re-subscribe
    WinBack --> Cancelled: Lapse
    Cancelled --> [*]
```

---

*Sürüm 1.0 — design freeze.*
