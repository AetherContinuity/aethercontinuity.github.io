# AMOC Endurance/Continuity -instrumentti — suunnitelma

**Tila:** Suunnitteluvaihe, 2026-07-30. Ei vielä koodia. Sama kuri kuin
BEM-E:n omassa suunnitteluvaiheessa (ks. hem-satellite-water-quality-plan.md):
data ensin, koodi vasta kun lähteet on vahvistettu.

**Alkuperä:** Käyttäjän oma ehdotus + toisen harrastelijan tarkennettu
kommentti 2026-07-30: WEM:n analyysityyli (useita riippumattomia
datalähteitä, ristiinvalidointi, yksi synteettinen tilannekuva) sopisi
hyvin AMOC-tutkimukseen. Tärkeä ero WEM:iin: AMOC:n havaintoverkko on
kansainvälinen alusta alkaen, ei yhden maan järjestelmä.

## Metodologinen ero WEM:iin — tärkeä, käyttäjän oma huomio

AMOC-epävarmuudet ovat rakenteellisesti suurempia kuin sähköjärjestelmässä:
- Havaintoaikasarjat lyhyempiä (RAPID 2004-, OSNAP vielä lyhyempi)
- Monet suureet epäsuoria proksia, ei suoria mittauksia
- Tutkijaryhmät erimielisiä kynnyksen läheisyydestä
- Subpolaarinen mittaussarja "vielä liian lyhyt" luotettavaan
  vuosikymmentason trendianalyysiin (vahvistettu haulla 2026-07-30)

**Tästä seuraa:** rinnakkaisten, riippumattomien indikaattoreiden
periaate on tässä *tarpeellisempi* kuin sähköjärjestelmässä, ei vain
kiva-to-have. Yksikään yksittäinen mittari ei riitä.

## Toinen harrastelijan oma metodologinen suositus — poikkeaa WEM:stä

WEM rakensi EPP-kaavan suhteellisen varhain ja on sen jälkeen joutunut
korjaamaan sitä useaan otteeseen (v2→v3→v4). AMOC-instrumentissa
ehdotettu järjestys on toisin päin:

1. Rakenna neljä yksinkertaista, itsenäistä indikaattoria ensin
2. Ymmärrä niiden keskinäinen käyttäytyminen
3. Rakenna mahdollinen yhdistelmäindeksi vasta tämän jälkeen

Tämä vältetään sen että instrumentti monimutkaistuu ennen kuin
perusrakenne on osoittautunut hyödylliseksi.

## Neljä aloitusindikaattoria ja niiden vahvistetut datalähteet (2026-07-30)

### 1. RAPID-indeksi (26.5°N, subtrooppinen AMOC)
- **Lähde:** rapid.ac.uk, data ylläpitäjänä BODC (British Oceanographic Data Centre)
- **DOI:** 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1
- **Aikasarja:** huhtikuu 2004 - maaliskuu 2024+ (v2024.1a, 19.9 vuotta)
- **Sisältö:** moc_transports-tiedosto, MOC-kuljetus + osakomponentit
  (Florida Straits, Ekman, mid-ocean), Sverdrupeina (10^6 m3/s)
- **KITKAKOHTA (havaittu 2026-07-30):** suora lataus rapid.ac.uk:sta
  vaatii sähköpostirekisteröinnin lomakkeella - EI suoraa API-tokenia
  kuten ENTSO-E/Fingrid/Copernicus. Eri tilanne kuin muut ACI-instrumentit.
- **Mahdollinen helpotus:** AMOCatlas-Python-kirjasto (github.com/
  AMOCcommunity/amocatlas) tarjoaa standardoidun `read.rapid()`-
  funktion joka hoitaa haun/välimuistituksen - EI VIELÄ testattu
  toimiiko se ohittaa sähköpostivaatimuksen vai käyttääkö se jotain
  muuta, jo avointa peilipalvelinta.
- **Tunnetut aukot datassa:** esim. 3.9.-21.11.2018 osa WB2-poijusta
  menetetty kalastusvaurion vuoksi - dokumentoitu läpinäkyvästi
  README:ssä, sama avoimuus kuin WEM:n omat datarajoitukset.

### 2. Sentinel-6 geostrofinen virtausindikaattori — VAHVISTETTU 2026-07-30
- **Lähde:** NOAA CoastWatch ERDDAP, dataset ID `noaacwBLENDEDsshDaily`
  ("Sea Surface Height Anomalies, Altimetry (S-3A/B,CryoSat2,Jason-2/3,
  SARAL), Near Real-Time, Global 0.25°, 2017-present, Daily")
- **Päivitystahti:** päivittäin, 3-5h viive (lähes reaaliaikainen)
- **Sisältö:** merenpinnan korkeuspoikkeama (sla, metreinä) 0,25°
  ruudukossa (720x1440 pistettä globaalisti)
- **API-tyyppi: ERDDAP/griddap** - standardoitu, hyvin dokumentoitu
  OPeNDAP-pohjainen rajapinta. **EI KIRJAUTUMISTA** - `web_fetch`
  haki koko dataset-infosivun (.html) taydellisena, mukaan lukien
  koko metadata-attribuuttirakenteen, ilman minkaanlaista estetta.
- **Kyselymuoto** (dokumentoitu esimerkki):
  `https://coastwatch.noaa.gov/erddap/griddap/noaacwBLENDEDsshDaily.
  csv?sla[(AIKA)][(LEVEYSASTE)][(PITUUSASTE)]`
- **EI VIELA testattu:** itse arvokysely (vain info-sivu/metadata
  vahvistettu) - oma web_fetch-tyokaluni vaatii etta tarkka URL
  (mukaan lukien omat kyselyparametrit) on jo esiintynyt haussa, joten
  en voinut testata juuri tata kyselya suoraan. Tama EI ole NOAA:n
  palvelun rajoitus, vain oman tyokaluni oma rajoite - todennakoisesti
  toimisi suoraan selaimessa tai tulevassa Cloudflare Worker -proxyssa
  (sama arkkitehtuuri kuin muut ACI-proxyt).
- **Selvä parannus RAPID:iin verrattuna:** talla on TAYDELLINEN,
  standardoitu, itse-dokumentoiva API-rakenne alusta asti - ei
  tarvetta arvata tiedostopolkuja tai etsia vaihtoehtoisia reitteja.

### 3. Pohjois-Atlantin meriveden lämpötila-anomalia (SST) — LÄHDE LÖYDETTY 2026-07-30
- **Perustuote:** NOAA OISST v2.1 - vakiintunut, laajasti käytetty
  standardi. 0,25° ruudukko, päivittäinen, saatavilla 1981-nykyhetki.
  Referenssi-ilmasto: 1991-2020 (nykyinen WMO:n 30v normaalijakso).
- **API-lähde (sama ERDDAP-kuvio kuin Sentinel-6/SLA):**
  `oceanwatch.pifsc.noaa.gov/erddap/griddap/CRW_sst_anom_v1_0.html`
  (Coral Reef Watch -tuote, mutta **globaali kattavuus** -89,975°...
  89,975° - soveltuu siis myos Pohjois-Atlantin subpolaariseen
  alueeseen vaikka ensisijainen kayttotarkoitus on koralliriuttojen
  seuranta)
- **Vaihtoehtoinen, alueellisesti rajattu ERDDAP-lahde** (EI sovellu
  suoraan, vain merkitty vertailuksi): `cwcgom.aoml.noaa.gov/erddap/
  griddap/miamiSSTAnomaly.html` - rajattu Karibian/Meksikonlahden
  alueelle (7-38°N, -110...-56°W), ei kata Pohjois-Atlantin
  subpolaarista aluetta.
- **Ei-API-vaihtoehto, hyva visuaalinen ristiintarkistus:**
  climatereanalyzer.org tarjoaa jo valmiin, interaktiivisen OISST-
  anomaliakayran tietyille alueille (esim. Pohjois-Atlantti) - ei
  raaka-API mutta hyva silmamaarainen vahvistus jos tarkkaa
  API-arvoa on vaikea tulkita.
- **Ei viela testattu itse arvokysely** - sama rajoitus kuin
  Sentinel-6/SLA:n kanssa (web_fetch vaatii tarkan URL:in jo
  hakutuloksissa).
- **Miksi tämä on relevantti AMOC:lle:** subpolaarisen "kylmän läiskän"
  (cold blob) jäähtymissignaali Pohjois-Atlantissa toimii yhtenä
  AMOC:n omana "sormenjälkenä" - juuri se alue johon tämä indikaattori
  kohdistettaisiin.

### 4. Grönlannin makean veden indikaattori — REITTI VAHVISTETTU 2026-07-30
- **Perusta:** GRACE (2002-2017) + GRACE-FO (2018-nyk.) -satelliitti-
  gravimetria, jäämassan muutos
- **TÄRKEÄ HAVAINTO:** NASA JPL PODAAC:n omat GRACE-datasetit
  VAATIVAT AIDOSTI NASA Earthdata Login -kirjautumisen ("Protected
  buckets... users must log in to Earthdata Login") - tämä on ERI
  tilanne kuin RAPID:n pelkkä käyttöliittymäkohteliaisuus. PODAAC-
  reitti EI siis sovellu suoraan.
- **VAHVISTETTU, EI-KIRJAUTUMISTA-VAATIVA VAIHTOEHTO:** ESA:n Climate
  Change Initiative -sivu (climate.esa.int/en/projects/ice-sheets-
  greenland/data) latautui `web_fetch`:illa täysin onnistuneesti, ei
  kirjautumista. Sivu osoittaa SUORAAN kahteen avoimeen latauspisteeseen
  juuri oikealle Gravimetric Mass Balance (GMB) -tuotteelle:
  - `data1.geo.tu-dresden.de/gis_gmb/` (TU Dresden, suora portaali)
  - `products.esa-icesheets-cci.org/products/downloadlist/GMB/` (ESA:n
    oma latauslista)
- **Tuore luku (NOAA Arctic Report Card 2025):** massatase -129±50 Gt
  (2003-2024 keskiarvo -219±16 Gt/v)
- **Mekanismi AMOC:iin (ei vain korrelaatio):** sulamisvesi makeuttaa
  Labradorinmerta → heikentää Labradorinmeren veden (LSW) muodostumista
  → LSW on keskeinen AMOC:n syvän paluuvirtauksen komponentti
- **Ei viela testattu:** itse TU Dresden- tai ESA-portaalin oma
  tiedostorakenne/formaatti - vain paasy vahvistettu, ei tarkkaa
  kyselymuotoa.

**PÄIVITYS 2026-07-30 (myöhemmin samana päivänä) — TOTEUTETTU, VAIHTOEHTOISELLA SUUREELLA:**

Foorumilta löytyi kiistaton vahvistus etta PODAAC:n GRACE-data vaatii
AIDON kirjautumisen — jopa kayttaja jolla oli oma, toimiva Earthdata-
tunnus (.netrc-tiedosto, selainkaytto toimi) epaonnistui ohjelmallisessa
lataamisessa (HTTP 200 mutta sisalto oli "ei paasyoikeutta" -HTML).
TU Dresdenin oma NetCDF-ruudukko (~36 Mt) taas vaatisi erillisen
NetCDF-jasentajan, ei sovi suoraan Cloudflare Workerin fetch()+text()
-malliin.

**LÖYDETTY JA TOTEUTETTU AVOIN VAIHTOEHTO:** DMI:n Polar Portal
(`download.dmi.dk/Research_Projects/polarportal/PP_GSMB/GSMB.txt`) —
täysin avoin, ei kirjautumista, PÄIVITTÄIN päivittyvä tekstitiedosto.
Vahvistettu web_fetch:illä 2026-07-30: sisälsi dataa 2025-09-01 asti
2026-05-17 saakka (julkaisuhetkellä), muoto YYYYMMDD SMB(Gt/d) SMBacc(Gt).

**TÄRKEÄ ERO:** tämä on PINTAmassatase (SMB, HARMONIE-AROME-malli:
sadanta miinus sulaminen) — EI GRACE:n oma KOKONAISmassatase (joka
sisältäisi myös jäätiköiden kalvamisen/discharge-komponentin). Eri,
mutta läheisesti liittyvä suure — SMB on nopeampi/herkempi signaali
lyhyen aikavälin sulamistapahtumille, kun taas GRACE:n kokonaistase
kuvaa koko jäätikön massataseen hitaammin mutta kattavammin.

**TOTEUTETTU:** `/greenland-smb`-reitti aci-amoc-proxyssa, jäsentää
koko sarjan regex-suodatuksella, palauttaa sekä koko historian että
viimeisimmän arvon erikseen. Testattu paikallisella yksikkötestillä
(synteettinen näyte, 3/3 riviä jäsentyi oikein) ennen julkaisua.

## Tunnistettu tekninen kysymys — RATKENNUT 2026-07-30

**PÄIVITYS 2026-07-30 (myöhemmin samana päivänä):** Testattiin
`web_fetch`-työkalulla (eri tyokalu kuin bash, ei domain-rajoitusta)
suora haku osoitteesta `https://rapid.ac.uk/sites/default/files/
rapid_data/README.pdf` — **ONNISTUI TÄYSIN, ei sähköpostilomaketta,
ei kirjautumista, koko sisältö tuli läpi puhtaasti.**

**Johtopäätös:** aiempi `403 Forbidden` (AMOCatlas + bash_tool) oli
todennäköisesti OMAN ymparistoni domain-rajoitus, EI RAPID:n aito
vaatimus. RAPID:n oma "sähköpostilomake" data-download-sivulla
vaikuttaa olevan vain nettisivun käyttöliittymän kohteliaisuuskäytäntö
selaimen kautta klikkaaville käyttäjille (käytetään käyttötilastointiin
rahoituksen perustelemiseksi) — EI tekninen este suoralle tiedostohaulle
tunnetulla, suoralla URL-osoitteella.

**Ei vielä varmistettu:** itse data-tiedosto (moc_transports.nc tai
vastaava) samalla polulla - vain README.pdf testattu onnistuneesti
tällä menetelmällä. Seuraava askel: hae tarkka, ajantasainen data-
tiedoston URL (versionumero saattaa muuttua julkaisujen valilla, ks.
README:n oma versiohistoria) ja testaa sama menetelma sille.

**Mahdollinen vaihtoehtoinen polku löytyi ja testattu (2026-07-30):**
`rapid.ac.uk/rapidmoc/rapid_data/transports.php` ohjautui uudelleen
`about-us/history`-sivulle (vanha URL, ei enää voimassa Drupal-
paivityksen jalkeen) — EI itsessaan johtanut dataan, mutta paljasti
sivuston nykyisen navigaatiorakenteen.

**Löytyi ja testattu onnistuneesti: `rapid.ac.uk/data/integrated-
transports`** — sivu vahvistaa datan olemassaolon ja antaa TUOREET,
VIRALLISET tilastot suoraan HTML:sta (ei vain PDF:sta):

| Komponentti | Keskiarvo ± keskihajonta (Sv) |
|---|---|
| Gulf Stream (Florida Straits) | 31,8 ± 3,4 |
| Ekman | 3,8 ± 3,4 |
| Yläkeskiokeaani | −18,4 ± 3,4 |
| **MOC (kokonaiskiertokuljetus)** | **17,1 ± 4,4** |
| UNADW (ylempi syvä paluuvirtaus) | −12,1 ± 2,5 |
| LNADW (alempi syvä paluuvirtaus) | −5,8 ± 2,8 |

Syvän paluuvirtauksen (UNADW+LNADW) korrelaatio MOC:n kanssa: **R=-0,9902**
(lahes taydellinen kaanteinen yhteys, fysikaalisesti odotettu).

Sivu mainitsee datan olevan saatavilla NetCDF/Matlab/ASCII-muodossa,
mutta **itse latauslinkkia ei loytynyt tekstimuotoisesta hausta** -
saattaa olla JavaScript-renderoity nappi jota web_fetch ei tavoita
suoraan. Tama on nyt ainoa jaljella oleva aukko: tarkka data-tiedoston
URL.

## Scoping-päätös 2026-07-30 — live-automaatio ei ole kriittinen tälle projektille

Käyttäjän oma huomio: "voimme oikeastaan elää osittain ilman live
dataakin." Tämä on käytännössä oikea linjaus, ei vain kompromissi:

**AMOC eroaa rakenteellisesti WEM:stä juuri tässä.** Sähkön hinta
muuttuu tunneittain — live-haku oli WEM:lle aidosti arvokas. RAPID:n
oma data itsessään päivittyy VAIN KERRAN VUODESSA (uusi julkaisu,
esim. v2023.1 → v2024.1a). Live-automaatio ei siis koskaan olisi ollut
yhtä kriittinen tälle projektille — vuosittainen, käsin tehty päivitys
(sama periaate kuin Tripwire-kalenterin sääntelyosio) on täysin
riittävä, ei kompromissi.

**Tästä seuraa:** sen tarkan latauslinkin metsästämistä ei tarvitse
jatkaa kiireellisenä - "Integrated transports" -sivun omat, jo
löydetyt tilastot (17.1±4.4 Sv jne.) riittävät sellaisenaan
ensimmäiseksi, käsin päivitettäväksi referenssipisteeksi. Tarkka
data-tiedosto olisi tarpeen vasta jos/kun halutaan laskea oma,
tarkempi indeksi raakadatasta - ei valttamaton ensimmaiselle,
yksinkertaiselle versiolle.

Alkuperäinen 2026-07-30 aamun tulos (403, epäluotettava) säilytetty
alla historiallisena kirjauksena:

**Testattu 2026-07-30 (aamu):** `pip install amocatlas` + `read.rapid()`
palautti `403 Forbidden` osoitteesta rapid.ac.uk/sites/default/files/
rapid_data/moc_transports.nc. **TULOS ON EPÄLUOTETTAVA** - Claude-
assistentin oma bash-tyokaluymparisto sallii verkkoyhteydet vain
ennalta maaratylle domain-listalle (GitHub, PyPI/npm-rekisterit jne.),
eika rapid.ac.uk ole talla listalla. 403 saattaa siis tulla OMASTA
egress-proxysta, ei RAPID:n palvelimelta itseltaan.

Kolme vaihtoehtoa selvitettäväksi ennen koodausta:
1. Testaa AMOCatlas rajoittamattomasta ymparistosta (kayttajan oma
   kone) - ratkeaako 403 silloin
2. Rekisteröidy itse rapid.ac.uk:hon, tarkista tuleeko sen jälkeen
   suora, uudelleenkäytettävä latauslinkki (samaan tapaan kuin
   Copernicus-tunnukset)
3. Jos kumpikaan ei toimi: harkitse harvempaa päivitystahtia (esim.
   kuukausittainen käsin päivitys, kuten Tripwire-kalenterin
   sääntelyosio) sen sijaan että vaadittaisiin live-haku joka lataus

## Seuraavat askeleet järjestyksessä

1. ~~Testaa AMOCatlas-kirjaston `read.rapid()`~~ — TEHTY 2026-07-30:
   `web_fetch` (eri työkalu kuin bash) haki README:n täysin onnistuneesti
   ilman kirjautumista. RAPID:n oma "email-lomake" on käyttöliittymä-
   käytäntö, ei tekninen este.
2. ~~Selvitä NOAA:n Sentinel-6/SLA-datan tarkka API-osoite~~ — TEHTY:
   NOAA CoastWatch ERDDAP (`noaacwBLENDEDsshDaily`), ei kirjautumista,
   koko metadata vahvistettu.
3. ~~Valitse SST-anomalialähde~~ — TEHTY: NOAA OISST v2.1, saatavilla
   samasta ERDDAP-kuviosta (`CRW_sst_anom_v1_0`, globaali kattavuus).
4. ~~Vahvista GRACE/GRACE-FO-datan tarkka hakumuoto~~ — TEHTY: PODAAC
   vaatii aidosti Earthdata-kirjautumisen, mutta ESA CCI → TU Dresden
   -reitti (`data1.geo.tu-dresden.de/gis_gmb/`) ei vaadi kirjautumista.

**Kaikki neljä lähdettä nyt tunnistettu, pääsy vahvistettu vähintään
info-/portaalitasolla.** Yksikään ei vaadi kirjautumista lopullisessa,
valitussa reitissä (RAPID suoraan, kaksi ERDDAP-lähdettä, ESA/TU Dresden
Grönlannille PODAAC:n sijaan).

5. Testaa jokaisen lähteen oma TARKKA arvokysely (ei vain info-sivu) -
   vaatii joko käyttäjän oman selaimen testin, tai tulevan Cloudflare
   Worker -proxyn (samat rakenne kuin muut ACI-proxyt), koska
   web_fetch-tyokaluni oma rajoitus (vaatii URL:in jo hakutuloksissa)
   estää omien, tarkkojen kyselyparametrien testaamisen suoraan
6. Vasta tämän jälkeen: ensimmäinen yksinkertainen näyttö, yksi kortti
   per indikaattori (ei vielä yhdistelmäindeksi), samaan tapaan kuin
   WEM:n §11:n kokeelliset kortit

## v0.1 rakennettu ja testattu — havainnot 2026-07-30

Ensimmäinen visuaalinen näyttö (`AMOC-monitor.html`) rakennettu ja
kaikki neljä korttia toimivat elävällä datalla. Kaksi merkittävää
löydöstä matkalla:

### 1. Itä-länsi-gradientin suunnitteluvirhe ja korjaus

Käyttäjän (ja hänen harrastelijaystävänsä) fysikaalinen kritiikki:
yhden pisteen SLA EI VOI tuottaa geostrofista gradienttia (gradientti
on määritelmällisesti kahden pisteen erotus). Korjattu lisäämällä
`/sla-gradient` (länsi ~75°W, itä ~15°W, 26.5°N, approksimoi RAPID:n
omaa länsi+sisäosa+itä-menetelmää karkeasti) ja `/sla-gradient-mean`
(30/365 vrk liukuva keskiarvo).

**Kvantitatiivinen tarkistus:** yhden päivän gradientti (-0,048 m)
vastaisi ~0,8 m/s nopeutta jos koko vesipatsas liikkuisi - epärealistisen
korkea RAPID:n omaan ~0,1-0,3 m/s tasoon verrattuna, vahvistaen että
yksittäinen päivä on mesoskaalakohinan dominoima.

**Kausivaihtelu löytyi, ei kohinaa:** kahden vuoden data (2024-2025,
2025-2026) paljasti johdonmukaisen, toistuvan vuosisyklin - syvä
negatiivinen pohja kesällä (-0,17...-0,28 m, heinä-elokuu), voimakas
positiivinen huippu talvella/keväällä (+0,20...+0,26 m, tammi-huhtikuu).
Amplitudi lähes identtinen molempina vuosina. Mekanismi: steerinen
(lämpölaajenemis-) merenpinnan kausivaihtelu, hyvin dokumentoitu
ilmiö (Hochet ym. 2024, Scientific Reports: jopa 20 cm amplitudi
paikoin Pohjois-Atlantilla). Käänteinen vaihe verrattuna yksinkertaiseen
"lämpenee kesällä" -odotukseen selittyy advektio-pintavuo-tasapainolla
(sama tutkimus: advektio, ei paikallinen lämmitys, hallitsee vaihetta
jopa 50 %:ssa valtamerta).

### 2. Golfvirta vs. AMOC - aktiivinen tieteellinen kiista, ei yksiselitteinen

Käyttäjän oma kysymys ("Golfvirta heikkenee") johti tärkeään
täsmennykseen: Golfvirta (tuulen ajama, subtrooppisen pyörteen
läntinen reunavirtaus) EI ole sama asia kuin AMOC (termohaliininen,
koko altaan syvyyssuuntainen kierto) - RAPID:n omat luvut osoittavat
tämän suoraan (Golfvirta/Florida-salmi 31,8 Sv vs. AMOC:n nettokuljetus
17,1 Sv, erotus kiertää takaisin pyörteen sisällä).

**Neljä historiallisesti ristiriitaista arviota (Wikipedia, koottu
2026-07-30):**
- NASA 2010: Golfvirta voimistunut vuodesta 1993
- 2015-tutkimus: heikentynyt 15-20% viimeisten 200 vuoden aikana
- Potsdam 2018: AMOC hidastunut 15% 1900-luvun puolivalin jalkeen,
  synnyttäen "lämpökuplan" New Yorkin/Mainen edustalle
- 2023 (Piecuch/WHOI): "vedenpitävä" 4% heikkeneminen 40 vuodessa,
  99% varmuus

**Tuorein korjaus (2024-2025, Volkov ym., NOAA AOML/Nature
Communications):** löysi että Florida-salmen kaapelimittauksissa oli
korjaamaton systemaattinen virhe (Maan geomagneettisen kentän hidas
muutos vääristi jännitemittauksesta johdettua kuljetusarvoa). Korjauksen
jälkeen Florida-virta osoittautui VAKAAKSI koko 40 vuoden ajalta, ei
heikkeneväksi - ja tämä vähensi myös AMOC:n oman heikkenemistrendin
26.5°N:ssä noin 40%, tehden siitä "vain marginaalisesti merkitsevän."

**Wikipedia huomauttaa suoraan:** media on toistuvasti sekoittanut
AMOC:n ja Golfvirran ja uutisoinut virheellisesti Golfvirran
pysähtymisestä. AMOC:n pysähtymistä pidetään epätodennäköisenä tällä
vuosisadalla (vaatisi 3-5°C lämpenemisen, nykytoimilla ennustettu 2,4°C).

**Opetus omalle projektillemme:** tämä on täsmälleen se ilmiö jota
olemme itse kohdanneet (väärä muuttujanimi, väärä pisteen valinta,
oletettu mekanismi joka osoittautui vääräksi) - ammattilaistutkijatkin
voivat erehtyä instrumentin omasta systemaattisesta virheestä, ja
"vedenpitäväksi" kuvattu tulos voi silti osoittautua vääräksi
myöhemmin. Vahvistaa entisestään harrastelijaystävän alkuperäistä
periaatetta: yksinkertaista ensin, ymmärrä käyttäytyminen huolellisesti,
älä luota yhteen "lopulliseen" tulokseen ilman ristiinvalidointia.

## KORJAUS 2026-07-30 (myöhemmin samana päivänä) — kausikorjaus oli väärä lähtöoletus

**Alkuperäinen ykkösprioriteetti (kausikorjattu anomalia, `/sla-gradient-
anomaly`) rakennettiin väärälle oletukselle.** Oletimme että itä-länsi-
gradientti noudattaa kiinteää, kalenteriin sidottua vuosisykliä (kahden
vuoden datan perusteella: helmi-huhtikuu huippu, elo-syyskuu pohja).

**Kolme lisävuosiparia (2019-2020, 2020-2021, ja yritys 2015-2016 joka
epäonnistui puuttuvan datan vuoksi) paljasti että jokainen vuosipari
näyttää TÄYSIN ERI vaiheen:**

| Vuosipari | Pohja | Huippu |
|---|---|---|
| 2024-2026 | heinä-elokuu | tammi-huhtikuu |
| 2020-2021 | helmi-maalis + heinä | huhti-touko |
| 2019-2020 | syyskuu + kesäkuu | marraskuu |

Ei kahta samanlaista. Käyttäjän oma varovaisuus ("ei tehdä johtopäätöksiä
vielä, mitä muut ovat havainneet") johti kirjallisuushakuun joka
selitti tämän täydellisesti.

### Tieteellinen selitys löytyi - tämä on tunnettu ilmiö, ei virhe meidän datassamme

**Frajka-Williams (2015), alkuperäinen SLA→UMO-proksimenetelmä jota
approksimoimme:** koko menetelmä perustuu **läntisen reunan SLA:n
VUOSIENVÄLISEEN (interannual) vaihteluun**, ei kausivaihteluun -
selittää yli 90% MOC:n vuosienvälisestä vaihtelusta.

**RAPID:n oma virallinen 20 vuoden yhteenveto:** "MOC vaihtelee paivien
ja vuosikymmenen valisilla aikaskaaloilla" - "odottamattomia vaihteluita
joka ikisella mitatulla aikaskaalalla", mukaan lukien suuri notkahdus
2010-2011. Jopa ammattilaiset yllattyivat 20 vuoden datalla.

**Mekanismi tasmaa suoraan omaan pituusastevalintaamme:** "Vuosienvaliset
vaihtelut havaitaan lantisessa altaassa (70-80W)... yhdenmukaisia
lanteen etenevien Rossby-aaltojen kanssa" (Elipot ym., Kanzow ym. 2009) -
sama alue (75W) jota kaytimme lansipisteena.

**Kausivaihtelu on olemassa mutta ALISTEINEN, ei hallitseva:** tuore
katsaus (2025) listaa kolme paallekkaista, eri aikaskaalan ilmiota:
kausivaihtelu (Chidichimo ym. 2010, Kanzow ym. 2010), vuosienvalinen
vaihtelu (McCarthy ym. 2012, Roberts ym. 2013), ja mesoskaala (Evans
ym. 2022). Kun vuosienvalinen (Rossby-aalto-) signaali on voimakkaampi,
kausisykli hukkuu sen alle eika nay puhtaana vuodesta toiseen.

### Johtopäätös ja korjaus

**Kolme keskenaan erilaista vuosiparia EI ole virhe menetelmassamme -
se on tasmalleen se ilmio jonka ammattioseanografit ovat dokumentoineet
samasta muuttujasta samalla leveysasteella.** Alkuperainen kausikorjaus-
oletus (kiintea kuukausittainen klimatologia) on siis todennakoisesti
HARHAANJOHTAVA, ei vain karkea - se voi luoda keinotekoisen "anomalian"
pelkastaan siksi etta kunkin vuoden oma, kalenterista riippumaton vaihe
sattuu eroamaan kahden aiemman vuoden keskiarvosta.

**Kaytannon seuraus `/sla-gradient-anomaly`-reitille:** tama reitti
sailytetaan koodissa (arvokas oppimiskokemus + validi lahtokohta
jatkotyolle), mutta sen tulkintaa pitaa korjata - anomalia kuvaa eroa
KAHDEN VUODEN otokseen, ei mitaan vakiintunutta normaalia. Oikeampi
lahestymistapa vaatisi todennakoisesti joko (a) paljon pidemman
aikasarjan (vuosikymmenia) jotta kausi- ja vuosienvalinen komponentti
voitaisiin erottaa tilastollisesti, tai (b) suoraan RAPID:n oman UMO-
aikasarjan kayttoa (kun sen tarkka datatiedosto joskus loytyy) sen
sijaan etta yritettaisiin approksimoida sita karkealla kahden pisteen
SLA-erolla.

**Tama on hyva, konkreettinen esimerkki koko AMOC-projektin omasta
opista:** yksinkertaisen instrumentin rakentaminen paljasti nopeasti
ettei "yksinkertaista ensin" tarkoita "oletukset ovat aina oikeita
ensin" - se tarkoittaa etta virheelliset oletukset paljastuvat
nopeammin ja halvemmalla kun rakennetaan pienesta alkaen, ei
paallikoita monimutkaisen yhdistelmaindeksin taakse.
