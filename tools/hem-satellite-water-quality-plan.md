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

## Toteutetut reitit (alkuperäiset suunnitellut nimet vs. lopulliset)

`aci-corine-proxy`-repossa. Lopulliset nimet lyhyempiä kuin alunperin
kaavailtu (`/lake-ndci` → `/ndci` jne.) — päätetty toteutusvaiheessa,
ei erikseen dokumentoitu tuolloin.

- `/ndci?bbox=...&months=3` — NDCI-tilasto (keskiarvo/hajonta), maskattu
  VAIN vesipikseleihin (SCL==6) — TEHTY JA LIVE-TESTATTU 2026-07-26
- `/mndwi?bbox=...&months=3` — rantaviivan/vesipinta-alan tilasto — TEHTY
  JA LIVE-TESTATTU 2026-07-26
- `/ndci-image?bbox=...` ja `/mndwi-image?bbox=...` — renderöidyt kuvat
  — TEHTY, `/mndwi-image` käytetty myös bbox:in visuaaliseen vahvistukseen
- `/lake-timeseries?bbox=...&startYear=...&endYear=...` — takautuva
  aikasarja — TEHTY, EI SAATU TOIMIMAAN (ks. tilapäivitys alempana)

## Miksi tämä yhdistäisi HEM:n ja BEM:n mielekkäästi

HEM mittaa hydrologista PAINETTA (vedenkorkeus, HEPP). Nämä uudet indeksit
mittaisivat EKOLOGISTA VASTETTA samalla järvellä samaan aikaan — sama
periaate jota BEPP v2:n kertolaskurakenne jo soveltaa muualla (useamman
stressitekijän kohtaaminen samassa paikassa). Pitkän matalan veden jakso
(kuten 2026 kevään SD=0.50-hälytys) voisi ENNAKOIDA rantakasvillisuuden
leviämistä tai leväkukintojen riskiä myöhemmin kesällä — tämä olisi
ensimmäinen konkreettinen tapa TESTATA tätä yhteyttä data vasten, ei vain
olettaa sitä.

## Tila 2026-07-26, päivitetty — MNDWI ja NDCI molemmat live-testattu

- **MNDWI [A]:** live-testattu, mean=-0.284, stDev=0.438, sampleCount=36000,
  noDataCount=291 (~0.8%, hyvä kattavuus). Bbox `26.167,62.567,27.067,63.467`.
- **NDCI [B]:** live-testattu, mean=-0.111, stDev=0.415, sampleCount=36000,
  noDataCount=28043 (~78%, koska maskattu vain vesipikseleihin — kelvollisia
  vesipikseleitä ~22%, täsmää hyvin MNDWI:n omaan vesiosuusarvioon samalla
  bbox:illa). Negatiivinen keskiarvo on SUUNTA-ANTAVASTI linjassa Iisveden
  tunnetun ekologisen profiilin kanssa (SYKE: "kirkasvetinen järvi", hyvä
  ekologinen tila, matala klorofylli odotettavissa) — EI vielä riittävä
  näyttö, vain yksi piste ajassa, ei aikasarja.
- **Sameus [C]:** EI TOTEUTETTU, tarkoituksella jätetty avoimeksi kunnes
  parempi vakiintunut kaava löytyy.

**Molemmat toteutetut indeksit toimivat teknisesti ja tuottavat suunnaltaan
uskottavia arvoja, mutta kumpikin on toistaiseksi vain YKSI mittauspiste —
todellinen arvo BEM-E:lle syntyy vasta pitkästä aikasarjasta (kuten HEPP:n
oma 1959-2026-sarja), ei yksittäisestä luvusta.**

## Seuraavat askeleet (kun palataan tähän)

1. ~~Vahvista bbox visuaalisesti~~ — TEHTY, `26.167,62.567,27.067,63.467`
2. ~~Toteuta ja live-testaa `/mndwi` + `/mndwi-image`~~ — TEHTY
3. ~~Toteuta ja live-testaa `/ndci` + `/ndci-image`~~ — TEHTY
4. Sameus jätetään yhä avoimeksi — ei toteuteta ennen kuin parempi kaava löytyy
5. **Takautuva aikasarja (`/lake-timeseries`) — RAKENNETTU, MUTTA EI SAATU
   TOIMIMAAN 2026-07-27. Syy jäi lopulta TUNNISTAMATTA.**
   - Käyttäjän oma metodologisesti tarkennettu suunnitelma (kesäkauden
     touko–syyskuu-keskiarvo per vuosi yksittäisen kuvan sijaan,
     kehys 1959–2017 pitkä HEPP-vertailu vs. 2018–2025 "luonnollinen
     validointijakso" satelliitin kanssa rinnakkain) — idea itsessään
     pysyy hyvänä ja metodologisesti perusteltuna, vain TOTEUTUS
     epäonnistui.
   - **Systemaattinen vianetsintä, kolme hypoteesia testattu, kaikki
     kumottu:**
     1. L2A-tuotannon systemaattinen alku (toukokuu 2017) — testattiin
        vuotta 2016, sai "data":[]. Siirrettiin ikkuna 2018-2025:een.
     2. Vuosi 2018 EI TOIMINUT MYÖSKÄÄN — sama "data":[] tulos, kumosi
        hypoteesin #1 kokonaan.
     3. Aikavälin pituus (153pv vs. toimivan /mndwi:n ~90pv) — testattiin
        lyhyempää 61pv ikkunaa (debugEndDay-parametrilla) samalle
        vuodelle 2018 — EDELLEEN "data":[]. Kumosi myös tämän hypoteesin.
     4. Arkiston "syvyys"/ikä — testattiin vuotta 2024 (lähellä
        nykyhetkeä, mutta yhä historiallinen) — EDELLEEN sama tulos.
        Kumosi myös tämän.
   - **Yhteinen tekijä joka EI vielä ole täysin tutkittu:** kaikki
     epäonnistuneet kutsut käyttivät KIINTEITÄ, ETUKÄTEEN LASKETTUJA
     päivämääriä (esim. `"2018-05-01T00:00:00Z"`), kun taas KAIKKI
     toimivat kutsut (`/mndwi`, `/ndci`) käyttivät `now.toISOString()`-
     suhteellista väliä ("nyt - X kuukautta"). Tätä EI ehditty testata
     erikseen ennen kuin päätettiin siirtyä pois tästä ongelmasta.
   - **PÄÄTÖS 2026-07-27 (käyttäjän oma, käytännöllinen linjaus):**
     ei jatketa tämän debuggaamista juuri nyt. `/mndwi` ja `/ndci`
     (ajankohtainen "nyt"-tilanne) toimivat molemmat täydellisesti ja
     riittävät BEM-E:n ensimmäiselle, käyttökelpoiselle versiolle.
     Takautuva aikasarja jää AVOIMEKSI jatkokehitykseksi paremmalla
     ajalla — koodi (`runStatsForRange`, `handleLakeTimeseries`) on
     valmiina repossa jos joku myöhemmin haluaa jatkaa vianetsintää,
     esim. kokeilemalla `now.toISOString()`-tyylistä suhteellista
     aikaväliä kiinteiden päivämäärien sijaan seuraavaksi hypoteesiksi.
   - **SYKE:n oma vaihtoehto tutkittu osittain:** `tarkka.syke.fi` /
     `geoserver2.ymparisto.fi` WMS-palvelu tarjoaa kansallisesti
     kalibroidun (C2RCC-malli) näkösyvyys-/vedenlaatudataa Suomen
     järville vuodesta 2016. Löydettiin ETTÄ palvelun oma
     `COPERNICUS_CMEMS_EO_HIROC_CHL` (klorofylli) -kerros KATTAA VAIN
     Itämeren rannikkoalueen (59,1–60,8°N) — EI Iisveden aluetta
     (62,77°N). Alkuperäistä näkösyvyyskerrosta (`EO_HR_WQ_S2_SDT`,
     joka nimenomaan mainitsee "Suomen järvet") EI ehditty testata
     Iisveden koordinaateilla GetFeatureInfo-kyselyllä — jää avoimeksi
     vaihtoehtoiseksi poluksi jos oma Sentinel Hub -integraatio ei
     etene.
6. ~~Integrointi HEM:n käyttöliittymään omana Aquatic Status -osiona~~ —
   TEHTY 2026-07-27, §09 (ei §05, koska §05 oli jo varattu HEPP-
   aikasarjalle HEM:ssä). Live-testattu ja vahvistettu toimivaksi:
   MNDWI/NDCI/HEPP näkyvät rinnakkain, A/B-kypsyysmerkinnät näkyvissä
   käyttäjälle asti, "yhdistetty tulkinta" pelkkänä sanallisena
   varovaisuushuomautuksena (ei matemaattista yhdistämistä).

## Viitteet

- NDCI: Mishra, S., & Mishra, D. R. (2012). Remote Sensing of Environment, 117, 394-406.
- MNDWI: Xu, H. (2006). International Journal of Remote Sensing, 27, 3025-3033.
- Sentinel Hub custom-scripts: github.com/sentinel-hub/custom-scripts (NDCI, NDWI/MNDWI)
- Iisvesi-Virmasvesi-Rasvanki: en.wikipedia.org/wiki/Iisvesi, fi.wikipedia.org/wiki/Iisvesi–Virmasvesi–Rasvanki
