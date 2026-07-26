# BEM-E (Aquatic Extension) × HEM — satelliittipohjaisen vedenlaadun seurannan suunnitelma

**Tila:** SUUNNITELTU, EI VIELÄ TOTEUTETTU. Käyttäjän oma ehdotus 2026-07-26:
yhdistää HEM:n hydrologinen HEPP-indeksi Copernicus/Sentinel-2-pohjaisiin
ekologisiin havaintoihin (levät, sameus, rantakasvillisuus, rantaviiva) —
muodollistettu 2026-07-26 nimellä **BEM-E (Aquatic Extension)**, oma
erillinen laajennus BEM:n maaekosysteemin BEPP:stä, ei sulautettuna siihen.

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

## Nimeäminen ja rakenne: BEM-E (Aquatic Extension) — käyttäjän oma ehdotus 2026-07-26

Vahvistettu nimeämisrakenne katsauksesta BEM v0.1:een: uudet vesistöindeksit
muodostavat oman, ERILLISEN laajennuksensa — **BEM-E (Aquatic Extension)**
— ei sulaudu suoraan maaekosysteemin BEPP-kaavaan (D_f/D_s/D_c/R).

**Ydinperiaate, joka on TÄRKEÄMPI kuin mikään yksittäinen kaava:** näitä
indeksejä EI SEKOITETA BEPP-kaavaan ennen kuin niiden yhteys hydrologiseen/
ekologiseen stressiin on validoitu. Ne pysyvät omina, itsenäisinä
mittareinaan siihen asti — sama kurinalaisuus jota on sovellettu läpi
tämän koko työn (esim. ei oletettu ENTSO-E:n dataseteille oikeita
kenttänimiä, ei oletettu DS-ID:iden olevan oikein ilman varmistusta).

### Kypsyysluokitus (A/B/C) — muodollistettu käyttäjän ehdottamasta taulukosta

| Muuttuja | Lähde | Luokka | Peruste |
|---|---|---|---|
| **MNDWI** | Sentinel-2 | **A — vakiintunut** | Xu 2006, useampi riippumaton lähde vahvistaa vakaammaksi kuin perinteinen NDWI |
| **NDCI** | Sentinel-2 | **B — kokeellinen** | Mishra & Mishra 2012, mutta virallinen dokumentaatio (Digital Earth Africa) itse merkitsee sen "kokeelliseksi Sentinel-2:lle" |
| **Sameus** | Sentinel-2 | **C — ei vielä validoitu** | Ei löytynyt vakiintunutta, laajasti hyväksyttyä kaavaa — vain yksi heikko akateeminen lähde |

Tämä kolmiportainen luokitus (A/B/C) tulisi näkyä myös lopullisessa
käyttöliittymässä, ei vain sisäisenä dokumentaationa — käyttäjän ei pidä
joutua arvaamaan kumpaan hän voi luottaa enemmän.

### Ehdotettu §05 "Aquatic Status" -osio (BEM-raportin rakenteeseen)

Käyttäjän oma ehdotus rakenteeksi, kun BEM-E joskus toteutetaan:

```
§05 Aquatic Status
  MNDWI: vesipinta-alan muutos                    [A]
  NDCI:  klorofylli-/leväsignaali                 [B]
  HEPP:  hydrologinen paine (HEM:sta)
  ————————————————————————————————
  Yhdistetty tulkinta (EI yhdistetty KAAVA)
```

"Yhdistetty tulkinta" tarkoittaa RINNAKKAISNÄYTTÖÄ ja sanallista havaintoa
(esim. "pitkä matalan veden jakso + nouseva NDCI-trendi samalla ajanjaksolla"),
EI matemaattista yhdistämistä yhdeksi indeksiksi — se askel vaatisi oman,
myöhemmän validointivaiheensa.

## Instrumenttiperheen kokonaiskehys (käyttäjän oma havainto 2026-07-26)

Katsauksesta nousi esiin kehys joka on syytä kirjata talteen: ACI-
instrumenttiperhe alkaa muistuttaa **ympäristön tilannekuvajärjestelmää**,
ei yksittäisiä irrallisia mittareita:

- **WEM** — energiaresilienssi (Endurance Pressure Proxy)
- **HEM** — hydrologinen tila (Hydrological Endurance Pressure Proxy)
- **BEM** — maaekosysteemin tila (Biodiversity Endurance Pressure Proxy)
- **BEM-E** (suunniteltu) — vesiekosysteemin tila, neljäs näkökulma

Rautalammin reitin pilottialueen rajaus (riittävän hallittava kokonaisuus,
ei liian suuri) mahdollistaa nimenomaan HEM:n ja BEM:n yhteyden näkemisen
samalla alueella — tämä on ollut tarkoituksellinen valinta, ei sattumaa,
ja BEM-E vahvistaisi tätä samaa periaatetta edelleen yhdellä lisäulottuvuudella.

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

**Bbox VISUAALISESTI VAHVISTETTU 2026-07-26:** `26.167,62.567,27.067,63.467`

Prosessi (kolme iteraatiota, /mndwi-image-reittiä käyttäen):
1. Alkuperäinen arvio (`26.667,62.567,27.067,62.967`, symmetrinen keskipisteen
   ympäri) osoittautui leikkaavan järven luoteispäätä — reuna-analyysi
   (ohjelmallinen värilaskenta kuvan reunapikseleista) paljasti vettä
   ylä- (16%) ja vasemmalla reunalla (16%), viitaten etta jarvi jatkuu
   bbox:in ulkopuolelle pohjoiseen/länteen.
2. Ensimmäinen korjaus (+0,15° länteen ja pohjoiseen) EI RIITTÄNYT -
   vasen reuna itse asiassa PAHENI (16%→40%), paljastaen etta jarven
   luodesuuntainen paa ulottuu paljon kauemmas kuin arvattu.
3. Aggressiivisempi korjaus (+0,35° länteen ja pohjoiseen alkuperäisesta)
   tuotti hyvan tuloksen: vasen reuna 40%→4%, ylareuna 16%→11%.
   Kayttajan oma silmamaarainen arvio: "Nyt nakyy kylla jo reilusti
   vesistoja."

Jäljelle jäävä pieni huomio: alareunalla nakyy jonkin verran vetta (16%),
todennakoisesti NAAPURIJARVI (esim. Niinivesi, joka tunnetusti sijaitsee
lahella samalla vedenpinnan tasolla) - EI valttamatta sama jarvi
leikkautuneena, alue on yleisesti jarvirikas. Ei vaadi lisakorjausta
taman kayttotarkoituksen (Iisvesi-Virmasvesi-Rasvanki-kompleksin yleinen
seuranta) kannalta.

**Menetelma jatkoa varten:** ohjelmallinen reuna-analyysi (laske vesivarien
osuus kuvan jokaisella neljalla reunalla erikseen) osoittautui nopeammaksi
ja tarkemmaksi tavaksi arvioida bbox:in riittavyytta kuin pelkka silmamaarainen
tarkastelu - suositellaan samaa menetelmaa jos bbox:eja saadetaan
tulevaisuudessa muille jarville.

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

Tila 2026-07-26: askeleet 1-2 TEHTY osittain (MNDWI-koodi kirjoitettu ja
bbox vahvistettu, MUTTA itse MNDWI-arvoja/tilastoja ei ole viela
live-testattu - vain kuvan VISUAALINEN sijainti on vahvistettu). Seuraavat
askeleet järjestyksessä:

1. ~~Vahvista bbox visuaalisesti~~ — TEHTY, `26.167,62.567,27.067,63.467`
2. ~~Toteuta `/mndwi` ja `/mndwi-image`~~ — KOODI KIRJOITETTU JA PUSHATTU,
   `/mndwi-image` visuaalisesti vahvistettu, MUTTA `/mndwi` (numeerinen
   tilasto) EI VIELA live-testattu tallla bbox:illa
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
