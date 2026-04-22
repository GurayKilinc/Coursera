# Pawsome Blast — MVP Prototype

Mobil block puzzle konseptinin tarayıcıda oynanabilir prototipi. Tek HTML dosyası; sunucu gerektirmez.

## Konsept (özet)

- **Tür**: Casual block puzzle (Block Blast mekaniği)
- **Tema**: Sevimli yavru hayvanları kafeslerden kurtarma
- **Hedef pazar**: Hindistan + Brezilya + ABD + SEA (mobil-öncelikli yüksek hacim)
- **Ayrıştırıcı fark**: Evrensel duygusal çengel (hayvan kurtarma) + Block Blast'ta olmayan kafes-hedef mekaniği + Royal Match tarzı hafif meta için altyapı.

Tam plan dokümanı: `/root/.claude/plans/bir-oyun-fikrine-ihtiyac-m-rippling-wigderson.md`

## Nasıl çalıştırılır

### Masaüstü
`index.html` dosyasına çift tıkla — tarayıcıda açılır.

### Mobilde test (en önemli)
Yerel makine ile aynı Wi-Fi'daki telefondan test için:

```bash
cd pawsome-blast-prototype
python3 -m http.server 8000
# veya: npx serve .
```

Telefondan `http://<bilgisayarın-yerel-IP>:8000` adresini aç.

### Nasıl oynanır
1. Alttaki 3 parçadan birini **bas-sürükle** ile tahtaya taşı.
2. Pembe ışıklı alan yerleşebilir; kırmızı alan yerleşemez.
3. Bir **satırı veya sütunu tamamen doldur** → blok patlar, puan kazanırsın.
4. Kilit ikonlu **kafesli hücreyi** temizlersen bir yavru hayvan kurtarılır.
5. Aynı hamlede birden fazla hat → **çifte combo** + skor çarpanı.
6. 🐱 Reroll (3 kullanım): parça seti kötüyse yeniler.
7. Hiçbir parça sığmazsa oyun biter.

## Test Protokolü (go/no-go için kritik)

Planın MVP fazındaki 15 kişilik testte bakılacak sorular:

- [ ] **Sıfır tutorial**: Kullanıcı 30 saniye içinde tutorial olmadan oynamaya başlıyor mu?
- [ ] **"Bir el daha" hissi**: 10 dakika oynadıktan sonra kapatmak istemiyor mu?
- [ ] **Combo dopamin**: Çifte/zincir yapınca yüz ifadesi değişiyor mu?
- [ ] **Evrensel**: 7 yaş çocuk + 65 yaş büyükanne ikisi de anlıyor mu?
- [ ] **Mobilde akıcılık**: Düşük bütçeli Android'de 60 FPS ve gecikmesiz sürükleme var mı?
- [ ] **Duygusal çekim**: "Kurtarılan" sayacı arttığında tatmin var mı?

## Şu anki kapsamda olan / olmayan

**Var** ✅
- 8×8 ızgara + drag-drop
- 17 farklı tetromino şekli
- Satır + sütun temizleme
- Çifte / zincir combo + çarpan
- Kafes hedefi (rastgele 2 + random yeni kafes)
- Kurtarılan hayvan sayacı
- Game over tespiti
- Yardımcı: 🐱 reroll (3 kullanım)
- Mobil dokunmatik desteği (PointerEvent)
- Sevimli pastel tema

**Yok — bilerek (MVP kapsamı dışı)** ❌
- Meta progression / barınak yenileme
- Seviye sistemi (sonsuz mod)
- Ses/müzik
- Profesyonel hayvan asset'leri (şimdilik emoji)
- Monetizasyon
- Analitik
- Battle Pass

Bu eksikler plan dosyasındaki **Yol B — Tam Ürün** fazında eklenecek; MVP başarılı olursa.

## Sonraki Adımlar (önerilen sıra)

1. **Hissiyat testi** — arkadaş/aile grubu ile prototipi dene.
2. **Metrik topla** — ortalama session süresi, gönüllü 2. oyun oranı.
3. **Go sinyali** → Unity'ye port + 3D hayvan asset'leri + barınak meta.
4. **No-go sinyali** → core loop ayarı (parça dağılımı, kafes sıklığı, combo çarpanı) + yeniden test.

## Teknoloji

- Vanilla HTML + CSS + JS (sıfır bağımlılık)
- PointerEvent API (iOS + Android + masaüstü tek kod)
- ~500 satır JS; okuması/değiştirmesi kolay

Unity/Godot'a geçerken mantık doğrudan taşınır; `findFullLines`, `canPlace`, `getPieceCells`, `resolveClearsAndCascade` fonksiyonları language-agnostic referans.
