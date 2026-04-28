# 💸 Monetization Funnel

**Belge amacı**: Free → paying user dönüşüm haritası, SKU economy, LTV hesaplama.

---

## 1. Conversion Funnel (1000 install örneği)

```mermaid
flowchart TD
    Install[1000 Installs] -->|85%| Tutorial[850 Complete Tutorial]
    Tutorial -->|D1 retention 42%| D1[357 D1 retained]
    D1 -->|D7 retention 22%| D7[78 D7 retained]
    D7 -->|D30 retention 12%| D30[42 D30 retained]

    Tutorial -->|First paywall view| FirstSee[850 see Starter Pack]
    FirstSee -->|0.5% buy Day 1| Day1Pay[4 buy Day 1 — Starter Pack]

    D7 -->|Witch Pass intro D5-7| WitchPassSee[78 see Witch Pass]
    WitchPassSee -->|2% subscribe| WPSub[2 Witch Pass subscribers]

    D30 -->|Continued buying| RecurringPay[10 recurring buyers]

    Day1Pay --> TotalPaying
    WPSub --> TotalPaying
    RecurringPay --> TotalPaying

    TotalPaying[~16 unique paying users<br/>Conversion: 1.6%]
```

Real-world tahmini: %1.6–%3.5 conversion (Royal Match level %3.5).

---

## 2. SKU-Bazlı Revenue Mix

```mermaid
pie title Revenue Mix by SKU (Year-1 tahmini)
    "Witch Pass Subscription" : 35
    "Coin Packs" : 25
    "Booster Bundles" : 15
    "Life Refills" : 10
    "Theme Bundles" : 8
    "Starter Pack" : 5
    "No Ads" : 2
```

---

## 3. ARPPU Distribution (Paying Users Segment)

```mermaid
xychart-beta
    title "ARPPU Distribution (Paying Users)"
    x-axis [Whale_$50+, Big_$15-50, Mid_$5-15, Small_$1-5]
    y-axis "% of Paying Users" 0 --> 60
    bar [3, 12, 35, 50]
```

- Small spenders (50%): $1-5 (Life Refill, single Booster Bundle)
- Mid spenders (35%): $5-15 (Witch Pass + 1 Theme Bundle)
- Big spenders (12%): $15-50 (Multiple Witch Pass renewals + Coin Packs)
- Whales (3%): $50+ (All themes + premium coins + Witch Pass loyal)

Average ARPPU: ~$12.

---

## 4. Touchpoint Timeline

```mermaid
timeline
    title Monetization Touchpoint per Day
    Day 0 : First Launch
          : NO IAP prompt (pure onboarding)
    Day 1 : Episode 2-3
          : Soft Hint booster offer
    Day 2 : Starter Pack popup ($2.99 limited)
    Day 3 : Continue Free
    Day 5 : Witch Pass intro popup ($7.99)
          : Episode 5-6 unlock
    Day 7 : Coin Pack contextual when out of coins
          : Daily Bloom streak ramp
    Day 14 : First Theme Bundle prompt ($4.99 Frozen)
    Day 21 : 2nd Theme Bundle prompt ($4.99 Volcano)
    Day 30 : Witch Pass renewal reminder
           : Endless Brew unlock teaser
```

---

## 5. Hayat (Lives) Conversion Loop

```mermaid
flowchart LR
    Fail[Player fails level] -->|Lives -1| LivesCheck{Lives > 0?}
    LivesCheck -->|Yes| Retry[Retry button]
    LivesCheck -->|No, Out of lives| BlockerPopup[Lives Out Popup]

    BlockerPopup --> Choice{User Choice}
    Choice -->|Wait 30min| TimerPath[Wait — passive]
    Choice -->|Watch Ad| AdPath[Rewarded Ad +1 life]
    Choice -->|Coin Pay| CoinPath[200 coins = 5 lives]
    Choice -->|IAP $0.99| IAPPath[5 lives instant]
    Choice -->|IAP $4.99| Infinite[Unlimited 24h]

    TimerPath -->|App close & return| Retry
    AdPath -->|Ad complete| Retry
    CoinPath --> Retry
    IAPPath --> Retry
    Infinite --> Retry
```

Tahmini split (out-of-lives moment):
- Wait: 60%
- Watch ad: 25%
- Coin pay: 10%
- IAP: 5% (1.5% IAP $0.99 + 0.5% IAP $4.99)

---

## 6. Witch Pass Lifetime Value

```mermaid
flowchart TD
    Day1[Day 1: $7.99 first month] --> Daily[Daily reward claim]
    Daily -->|Engagement loop| Day29[Day 29: Almost expired]
    Day29 -->|Auto-renew or cancel?| Decision

    Decision -->|60% renew| Month2[$7.99 month 2]
    Decision -->|40% cancel| Lapsed
    Month2 -->|40% renew| Month3[$7.99 month 3]
    Month3 -->|30% renew| Month4[$7.99 month 4+]

    Lapsed -->|D14 win-back push| WinBack
    WinBack -->|10% return| Month1Reset[Re-subscribe $7.99]

    Day1 --> LTVCalc{LTV calculation}
    Month2 --> LTVCalc
    Month3 --> LTVCalc
    Month4 --> LTVCalc

    LTVCalc --> AvgLTV[Witch Pass user LTV: ~$22]
```

Witch Pass LTV: $7.99 × 1 + (60% × $7.99) + (40% × 60% × $7.99) + ... = ~$22.

---

## 7. Cohort Revenue Curve

```mermaid
xychart-beta
    title "Cumulative Revenue per User Cohort ($)"
    x-axis [D1, D7, D14, D30, D60, D90, D180, D365]
    y-axis "Revenue per User ($)" 0 --> 5
    line [0.05, 0.30, 0.70, 1.50, 2.50, 3.20, 4.10, 4.80]
```

LTV target: $4.50–5.00 per install (USA market). Türkiye/Brezilya proxy: ~$1.50.

---

## 8. Ad Revenue Funnel

```mermaid
flowchart TD
    DAU[100K DAU at 6-month mark]
    DAU -->|25% watch rewarded| RewardedView[25K rewarded views/day]
    DAU -->|3 fail/day per user avg → 1 interstitial| Interstitial[10K interstitial/day]
    DAU -->|No banner shown| NoBanner[0]

    RewardedView -->|eCPM $15 USA, $5 TR| RewardedRev[Rewarded daily: $375]
    Interstitial -->|eCPM $8 USA, $3 TR| InterstitialRev[Interstitial daily: $80]

    RewardedRev --> TotalAd[Total Ad Revenue: ~$455/day]
    InterstitialRev --> TotalAd

    TotalAd --> Monthly[Monthly Ad Revenue: ~$13.5K]
```

---

## 9. Total Year-1 Revenue Tahmini

```mermaid
flowchart LR
    Q1[Q1 Soft Launch<br/>$5K-15K] --> Q2[Q2 TR+BR+DE Expansion<br/>$30K-80K]
    Q2 --> Q3[Q3 Global Launch<br/>$120K-300K]
    Q3 --> Q4[Q4 Mature<br/>$200K-500K]
    Q4 --> YearTotal[Year-1 Total Gross<br/>$355K-895K]
    YearTotal -->|30% Apple/Google fee| AfterFee[After fee: $250K-625K]
    AfterFee -->|UA + ops| Net[Net Profit: $130K-380K]
```

---

## 10. Whale Identification Pipeline

```mermaid
flowchart TD
    AllPaying[Paying Users] -->|Total spend tracking| Segment{Segment}
    Segment -->|Spent >$50| WhaleSegment[Whale Segment 3%]
    Segment -->|Spent $15-50| BigSegment[Big Spender 12%]
    Segment -->|Spent <$15| StandardSegment[Standard 85%]

    WhaleSegment -->|Special offers| WhaleOffers[Mega Pack $19.99<br/>Ultimate Pack $49.99]
    BigSegment -->|Theme bundles| BigOffers[Theme Bundle $4.99]
    StandardSegment -->|Standard funnel| StdOffers[Coin Pack + Booster]
```

POURLE'de aggressive whale targeting yok — fair-play ethos. Whale segment doğal organic.

---

## 11. Monetization Health Metrics

| Metrik | Hedef | Kötü sınır | Aksiyon eğer kötü |
|---|---|---|---|
| Conversion rate | %2+ | %1- | Starter Pack ara timing |
| ARPDAU | $0.10+ | $0.05- | Reklam frequency arttır |
| ARPPU | $10+ | $5- | Witch Pass değer arttır |
| LTV | $4.50+ | $2- | UA budget cut, organic dominant |
| CPI break-even | <$3 | >$5 | Targeting daralt |
| Witch Pass renewal | 60%+ | 40%- | Premium track ödül arttır |

---

## 12. Pricing Sensitivity Test (A/B)

Soft launch sırasında test:

| Test | Variant A | Variant B | Winner ölçütü |
|---|---|---|---|
| Starter Pack | $2.99 | $1.99 | Daha yüksek revenue |
| Witch Pass | $7.99/mo | $4.99/mo | Subscriber rate × ARPPU |
| Coin Pack small | $0.99 = 200 | $0.99 = 300 | Conversion rate |
| Theme Bundle | $4.99 each | 3 themes for $9.99 | Bundle uplift |

A/B test framework: Firebase Remote Config + Analytics cohort split.

---

*Sürüm 1.0 — design freeze.*
