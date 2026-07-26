# HEM × Satelliittipohjainen vedenlaadun seuranta — suunnitelma

**Tila:** SUUNNITELTU, EI VIELÄ TOTEUTETTU. Käyttäjän oma ehdotus 2026-07-26:
yhdistää HEM:n hydrologinen HEPP-indeksi Copernicus/Sentinel-2-pohjaisiin
ekologisiin havaintoihin (levät, sameus, rantakasvillisuus, rantaviiva).

## Tausta ja rajaus

Satelliitti näkee OPTISET oireet, ei ravinnepitoisuutta suoraan:
- ✅ Klorofylli/sinileväkukinnat (heijastuksen muutos)
- ✅ Sameus (kiintoaine, levät — epäsuora proxy)
- ✅ Rantakasvillisuuden leviäminen
- ✅ Rantaviivan muutos (pitkäaikainen, jos vedenkorkeus poikkeaa normaalista pitkään)
- ❌ Fosfori/typpi EI mitattavissa suoraan — vain epäsuorasti korreloivien
  optisten oireiden kautta, vaatisi vesinäytteitä todelliseen pitoisuuteen

Pintaveden lämpötila (jonka käyttäjä myös mainitsi) VAATISI lämpöinfrapuna-
anturin — Sentinel-2:lla EI OLE termistä kanavaa. Tarvittaisiin Landsat
8/9 (TIRS) tai Sentinel-3 (SLSTR), eri satelliitti kuin alla käytetty.
EI kuulu tämän suunnitelman piiriin, merkitty mahdolliseksi jatkotyöksi.

## Indeksit ja niiden VARMISTETUT kaavat (2026-07-26)

Kaikki kolme varmistettu Sentinel Hubin omasta virallisesta
custom-scripts-arkistosta (github.com/sentinel-hub/custom-scripts) ja/tai
useasta riippumattomasta akateemisesta lähteestä — EI arvattu.

| Indeksi | Kaava (Sentinel-2) | Lähde | Luotettavuus |
|---|---|---|---|
| **NDCI** (klorofylli/sinilevä) | `(B05-B04)/(B05+B04)` | Mishra & Mishra 2012, Sentinel Hub virallinen | Kohtalainen — **merkitty "kokeelliseksi Sentinel-2:lle" viralisessa Digital Earth Africa -dokumentaatiossa**, ei vielä täysin validoitu/kalibroitu sisävesille |
| **MNDWI** (rantaviiva/vesipinta-ala) | `(B03-B11)/(B03+B11)` | Xu 2006, Sentinel Hub virallinen | Vahva — **useampi riippumaton lähde vahvistaa MNDWI:n vakaammaksi kuin perinteinen NDWI** rantaviivan seurantaan, koska SWIR-kaista (B11) vaimentaa kasvillisuuden/rakennetun ympäristön kohinaa paremmin kuin NIR (B08) |
| **Sameus** | `(B04+B03)/B02` | YKSI akateeminen lähde (arxiv 2605.24515) | **HEIKKO — EI yhtä vakiintunutta, laajasti validoitua kaavaa kuin NDCI/MNDWI:lla.** Ei virallista Sentinel Hub -custom-scriptia löytynyt. Käytettävä varoen, merkittävä selvästi kokeelliseksi jos toteutetaan. |

**Rehellinen yhteenveto:** MNDWI on tukevin lähtökohta (vakaa, hyvin
dokumentoitu). NDCI on käyttökelpoinen mutta vaatii oman "kokeellinen"
-merkintänsä. Sameus on selvästi heikoin — voisi jättää pois ensimmäisestä
versiosta tai toteuttaa vasta kun parempi, vakiintuneempi kaava löytyy.

## Kohdealue — Iisvesi/Virmasvesi/Rasvanki

Varmistettu (en.wikipedia.org/wiki/Iisvesi):
- Keskikoordinaatti: **62.767°N, 26.867°E**
- Mitat: 42,2 km pitkä (luode-kaakko), 15,0 km leveä, pinta-ala 164,5 km²
- Kolme allasta: Iisvesi, Virmasvesi, Rasvanki

**Alustava bbox (EI VIELÄ visuaalisesti tarkistettu):**
`26.667,62.567,27.067,62.967` (n. ±22km keskipisteestä joka suuntaan,
kattaa koko kolmen altaan kompleksin marginaalilla)

Tarkkuus tulisi varmistaa samalla tavalla kuin BEM:n NDVI-kuvan kanssa —
renderöimällä ensin visuaalinen Process API -kuva ja tarkistamalla
peittääkö bbox koko järven ilman liikaa ympäröivää maata.

## Arkkitehtuuriehdotus

**Uudelleenkäytä `aci-corine-proxy`:n olemassa olevaa Copernicus/Sentinel
Hub -tunnistautumista** (sama `getCopernicusToken()`, sama secret-varasto)
— EI tarvita uutta rekisteröintiä tai uutta proxya. Kolme mahdollista
toteutustapaa:

1. **Statistical API** (kuten BEM:n oma D_f/NDVI-tilastohaku) — palauttaa
   keskiarvon/hajonnan koko bbox:in yli per ajanjakso. Sopii aikasarjan
   rakentamiseen (esim. NDCI-keskiarvo per kuukausi 2019-2026).
2. **Process API** (kuten BEM:n oma renderöity NDVI-kuva) — palauttaisi
   visuaalisen kartan järven pinnasta väritettynä NDCI/MNDWI-arvon mukaan.
3. **Molemmat** — Statistical API HEPP-integraatioon (numeerinen aikasarja),
   Process API visuaaliseksi kuvaksi HEM:n käyttöliittymään (kuten BEM:n
   NDVI-kuva).

## Ehdotetut uudet reitit (EI VIELÄ TOTEUTETTU)

Samaan `aci-corine-proxy`-repoon:

- `/lake-ndci?bbox=...&months=3` — NDCI-tilasto (keskiarvo/hajonta) järven
  vesipikseleille. VAATISI vesimaskin (esim. MNDWI>0-suodatin evalscriptin
  sisällä) jotta rantametsä/pellot eivät vääristä lukemaa.
- `/lake-mndwi?bbox=...&months=3` — rantaviivan/vesipinta-alan tilasto,
  vertailukelpoinen vuodesta toiseen.
- `/lake-ndci-image?bbox=...` — renderöity kuva (kuten BEM:n NDVI-kuva),
  väriliukuma vihreä→keltainen→punainen (matala→korkea klorofylli).

## Miksi tämä yhdistäisi HEM:n ja BEM:n mielekkäästi

HEM mittaa hydrologista PAINETTA (vedenkorkeus, HEPP). Nämä uudet indeksit
mittaisivat EKOLOGISTA VASTETTA samalla järvellä samaan aikaan — sama
periaate jota BEPP v2:n kertolaskurakenne jo soveltaa muualla (useamman
stressitekijän kohtaaminen samassa paikassa). Pitkän matalan veden jakso
(kuten 2026 kevään SD=0.50-hälytys) voisi ENNAKOIDA rantakasvillisuuden
leviämistä tai leväkukintojen riskiä myöhemmin kesällä — tämä olisi
ensimmäinen konkreettinen tapa TESTATA tätä yhteyttä data vasten, ei vain
olettaa sitä.

## Rajaus ja seuraavat askeleet

Tämä on SUUNNITELMA, ei toteutus. Mitään reittiä ei ole vielä kirjoitettu
eikä testattu. Seuraavat askeleet järjestyksessä:

1. Vahvista bbox visuaalisesti (Process API -testikuva, sama menetelmä
   kuin BEM:n NDVI-kuvan kanssa)
2. Toteuta `/lake-mndwi` ENSIN (vahvin kaava, selkein tulkinta)
3. Toteuta `/lake-ndci` toisena, merkiten selvästi "kokeellinen Sentinel-2:lle"
4. Sameus jätetään avoimeksi — ei toteuteta ennen kuin parempi kaava löytyy
5. Vasta kaikkien läpi käytyä testausta (sama kuri kuin ENTSO-E-integraatiossa:
   validoi ensin paikallisesti tunnettua rakennetta vastaan, sitten live-data)
   integroidaan HEM:n omaan käyttöliittymään

## Viitteet

- NDCI: Mishra, S., & Mishra, D. R. (2012). Remote Sensing of Environment, 117, 394-406.
- MNDWI: Xu, H. (2006). International Journal of Remote Sensing, 27, 3025-3033.
- Sentinel Hub custom-scripts: github.com/sentinel-hub/custom-scripts (NDCI, NDWI/MNDWI)
- Iisvesi-Virmasvesi-Rasvanki: en.wikipedia.org/wiki/Iisvesi, fi.wikipedia.org/wiki/Iisvesi–Virmasvesi–Rasvanki
