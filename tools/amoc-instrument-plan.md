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

## MERKITTAVA KEHITYS 2026-07-31 — kayttaja lataisi oikean RAPID-datan + suora validointi

Kayttaja rekisteroityi itse rapid.ac.uk:hon ja latasi todellisen
`moc_transports.nc`-tiedoston (NetCDF/HDF5, v2024.1a, DOI 10.5285/
48d0bf43-0598-ceb2-e063-7086abc062f1) suoraan aci-repo:on
(`tools/moc_transports.nc`). Tama ratkaisee lopullisesti sen alusta
asti tunnistetun aukon (RAPID:n oma datatiedosto ei ollut viela
loydetty/parsittu).

**Tiedoston sisalto (parsittu netCDF4-kirjastolla):** 14 599 pistetta,
12h resoluutio, 2.4.2004 - 22.3.2024 (viimeinen kelvollinen paiva,
20 puuttuvaa pistetta lopussa). Sisaltaa KAIKKI komponentit: Florida-
salmi (Golfvirta), Ekman, ylakeskiokeaanin kuljetus (UMO - tasmalleen
se suure jota oma SLA-gradienttimme approksimoi), syvat kerrokset,
ja taydellinen MOC. Kokonaistilastot (ka 16.98 Sv MOC) tasmaavat
hyvin aiemmin RAPID:n omalta nettisivulta loydettyihin (17.1 Sv) -
hyva ristiinvalidointi.

### Suora validointitesti — oma approksimaatio vs. oikea data

Tama mahdollisti jotain arvokkainta koko projektissa: VERRATA omaa
karkeaa ita-lansi-SLA-gradienttiamme OIKEAAN RAPID UMO/MOC-arvoon
samoilta paivilta (2020-2021-ajalta, jolta meilla oli jo gradienttidataa).

**Ensimmainen otos (27 pistetta, kasin poimittu):** r=0.056 (UMO),
r=0.014 (MOC) - kaytannossa NOLLA korrelaatio.

**Koko sarja (365 pistetta):** r=0.177 (UMO), r=0.120 (MOC) - heikko
mutta ei enaa olematon. Osoittaa etta pieni otos oli harhaanjohtava.

**Viivekorrelaatio (lag -20...+20 vrk):** loysi selvan parannuksen
positiivisella viiveella:
- lag 0: r=0.177
- lag +5: r=0.277
- lag +10: r=0.339 (paras)
- lag +20: r=0.317

Etumerkki sailyi oikeana koko viivealueella (ei kaantynyt), tukien
etta kyseessa on aito, joskin heikko, signaali - ei pelkkaa kohinaa.

**Fysikaalinen tulkinta:** +10 vrk:n paras viive on linjassa Rossby-
aaltojen etenemisajan kanssa - lansipisteemme (75W) havaitsee saman
signaalin ennen kuin se ehtii vaikuttaa RAPID:n koko altaan kattavaan
UMO-integraaliin.

**Johtopaatos:** oma approksimaatiomme mittaa jotain aidosti, mutta
HEIKOSTI liittyvaa RAPID:n omaan UMO-signaaliin - ei riittava korvike,
mutta ei myoskaan taysin merkityksetov. Tama on rehellinen, kohtalainen
tulos - ei vahva validointi, ei taysi epaonnistuminen.

### Uusi, yleistetty tyokalu: /compare/nao-sla

Kayttajan oma, yksityiskohtainen ehdotus paransi alkuperaista yhden-
Pearson-luvun NAO-vertailua merkittavasti:
1. Lag-skannaus -30...+30 vrk (saadettavissa), palauttaa seka lag=0
   etta parhaan |r|:n loytaneen viiveen
2. Lapinakyvat pistemaarat (sla_points/nao_points/matched_points)
   AINA nakyvissa ennen korrelaatiota
3. P-arvo (normaalijakauma-approksimaatio, tarkka kun n>100)

Kayttajan oma perustelu, kirjattu suoraan: *"ACI:n instrumenttifilosofia
- hypoteesia ei oleteta oikeaksi, vaan sille rakennetaan oma mitattava
testi. Jos korrelaatiota ei loydy, sekin on arvokas tulos."*

Kaikki kolme osaa (lag-logiikka, p-arvo, rakenne) testattu paikallisesti
synteettisella datalla (tunnettu 5 vrk syy-seuraussuhde loytyi
tasmalleen) ennen julkaisua.

### Seuraavat mahdolliset askeleet (ei viela toteutettu)

- Muuntaa koko moc_transports.nc JSON/CSV-muotoon ja tarjota se omana
  reittinaan proxyssa (nyt vain paikallisesti analysoitu, ei viela
  palvelimella)
- Ajaa /compare/nao-sla suoraan RAPID:n omaa UMO-sarjaa vastaan (ei
  vain oman gradienttimme), koska nyt meilla on molemmat oikeasti
  saatavilla samalta ajalta
- Selvittaa saako RAPID:n tuoreempaa versiota (v2024.1a paattyy maalis
  2024 - reilut 2 vuotta vanhaa dataa jo nyt)

## ARKKITEHTUURIREFAKTOROINTI 2026-07-31 — yleinen /compare-moottori

Kayttajan oma arkkitehtuuriehdotus: sen sijaan etta jokainen uusi
sarjavertailu (SLA/NAO, SLA/RAPID, SST/RAPID, SMB/RAPID, NAO/RAPID...)
vaatisi oman, kertakayttoisen reittinsa, rakennettiin yleinen
`/compare?series_a=X&series_b=Y`-moottori jota mika tahansa
rekisteroity sarjapari voi kayttaa ilman uutta koodia.

**SERIES_PROVIDERS-rekisteri:** sla (ita-lansi-gradientti), nao (CPC),
sst (SST-anomalia), smb (Gronlannin SMB) - kaikki toimivia. rapid on
tarkoituksellinen stub joka heittaa selkean virheen (NetCDF-parsinta
ei onnistu suoraan Cloudflare Workerin fetch()+text()-mallilla).

**Kehitysjarjestys (kayttajan oma ehdotus, noudatettu):**
1. Pearson + lag +-30vrk + yhteiset paivamaarat (tehty aiemmin)
2. Spearman + effective N (Neff) - TEHTY TASSA PAIVITYKSESSA
3. Taysi CCF-kayra - jo osittain (lag_spectrum.full_scan)
4. RAPID mukaan kun sen aikasarja on julkaistu proxyssa - EI VIELA

**Vaihe 2 yksityiskohdat:**
- Spearmanin rho: tunnistaa monotonisen (ei valttamatta lineaarisen)
  yhteyden. Testattu: kuutiofunktio antoi rho=1.0 vs Pearson 0.928.
- Effective N (Neff): Bretherton ym. 1999 -tyylinen approksimaatio,
  Neff=N*(1-r1x*r1y)/(1+r1x*r1y). Peruste (kayttajan oma huomio): seka
  NAO etta SLA ovat ajallisesti autokorreloituneita (Rossby-aallot
  etenevat hitaasti) - tavallinen Pearsonin p-arvo raa'alla N:lla olisi
  liian optimistinen. Testattu: vahva autokorrelaatio (r1~0.87) pudotti
  Neff:n 200:sta 28.5:een; valkoinen kohina piti Neff:n lahella N:aa.
- p-arvo lasketaan nyt Neff:lla, ei raa'alla havaintomaaralla.

**Kayttajan oma perustelu kirjattu suoraan:** *"Silloin sama koodi
palvelee myohemmin myos muita ACI-instrumentteja."* ja *"Nain
instrumentti kasvaa hallitusti ilman etta siihen lisataan liian
paljon monimutkaisuutta kerralla."*

Vanha `/compare/nao-sla` sailytetty koodissa taaksepain-yhteensopi-
vuuden vuoksi, merkitty vanhentuneeksi `/status`-vastauksessa.

## TULOS 2026-07-31 — SLA vs NAO, Neff paljasti kriittisen ongelman

Ensimmainen oikea testi uudella `/compare`-moottorilla (sla vs nao,
365 vrk, 367 paallekkaista pistetta):

**Raaka N=367, mutta effective N=17.8** - lag-1-autokorrelaatio oli
0.952/0.953 molemmilla sarjoilla (aarimmaisen korkea). Tama tarkoittaa
etta 367 paivittaisesta havainnosta on tosiasiassa vain ~18 aidosti
itsenaista havaintoa.

**Lopputulos: EI tilastollisesti merkitseva yhteys.** lag=0: r=0.184,
p=0.457. Paras lag=+12: r=0.286, mutta p=0.236 - EI merkitseva
tamakaan, vaikka korrelaatio nayttaisi suuremmalta raa'an N:n kanssa
laskettuna.

### KRIITTINEN JATKOKYSYMYS — aiempi RAPID-UMO-tulos vaatii uudelleenarviointia

Aiemmin (ks. yllaoleva "Suora validointitesti") raportoimme oman SLA-
gradienttimme ja OIKEAN RAPID UMO:n valilla r=0.339 lag+10:lla,
kuvattuna innostuneesti tilastollisesti merkitsevaksi. **Tama laskettiin
RAA'ALLA N=365:lla, ennen kuin Neff-korjaus oli edes olemassa
koodissa.**

Koska SLA-gradientin oma autokorrelaatio on nyt vahvistetusti
aarimmaisen korkea (0.95) ja RAPID:n UMO on fysikaalisesti hidas,
todennakoisesti samankaltaisesti tai voimakkaammin autokorreloitunut
suure, **UMO-tuloksen oma Neff olisi todennakoisesti yhta pieni**
(~15-20 luokkaa) - mika tarkoittaisi etta se aiempi "merkitseva"
loydos oli todennakoisesti LIIAN OPTIMISTINEN.

**MERKITTY SEURAAVAKSI ASKELEEKSI:** kun RAPID-sarja saadaan joskus
kaytettavaksi taman saman `/compare`-moottorin kautta (Vaihe 4), toista
alkuperainen SLA-vs-UMO-testi ja laske sen oma Neff ja Neff-korjattu
p-arvo uudestaan. Todennakoinen lopputulos: aiempi "kohtalainen mutta
lupaava" tulkinta pitaisi todennakoisesti laskea "ei tilastollisesti
merkitseva talla otoskoolla" -tasolle, samaan tapaan kuin NAO-tulos
juuri osoitti.

**Tama on tarkea, itsekriittinen oppimiskokemus koko projektille:**
Neff-korjauksen lisaaminen (kayttajan oma ehdotus) paljasti etta
useampi aiempi, raa'alla N:lla laskettu "loytos" tassa AMOC-
instrumentissa saattaa olla systemaattisesti liian optimistinen
autokorrelaation vuoksi - juuri se ongelma jonka Neff-korjaus oli
tarkoitettu estamaan, mutta joka ehti vaikuttaa tulkintaan ennen
korjauksen lisaamista.

## PARANNUKSET 2026-07-31 — tekniset huomiot /compare-moottoriin

Kayttaja antoi Python/FastAPI-referenssitoteutuksen ja viisi teknista
parannusehdotusta. Koodi itsessaan ei ole suoraan kaytettavissa (oma
pinomme on JS/Cloudflare Workers), mutta menetelmat siirrettiin
suoraan. Kolme toteutettu heti, kaksi merkitty jatkoa varten.

**Toteutettu:**

1. **Taysi ACF-pohjainen Neff** (Pyper & Peterman 1998, alkuperainen
   menetelma) korvasi aiemman lag-1-approksimaation:
   `Neff = N/(1+2*sum_{k=1}^{m} rho_x(k)*rho_y(k))`, katkaisuraja
   m=min(N/5,30). Testattu paikallisesti seka erillisella skriptilla
   etta suoraan tiedostosta poimitulla koodilla (AR(1)-data, N=300,
   antoi Neff=73.1).

2. **Metadata-objekti** (SERIES_METADATA-rekisteri): jokaiselle
   sarjalle lahde+yksikko palautetaan vastauksen `metadata`-kentassa.

3. **Monivertailuhuomautus:** `lag_spectrum.n_lags_tested` + oma
   huomautus etta paras lag on valittu N testatusta viiveesta EIKA
   ole viela korjattu monivertailulle - tama on TUNNISTETTU mutta
   EI VIELA KORJATTU rajoite.

**Ei viela toteutettu (kayttajan omat ehdotukset, jatkoa varten):**

- Luottamusrajat (95%) lag-spektrille - auttaisi arvioimaan onko
  esim. +12 vrk:n huippu aidosti erottuva vai kohinaa
- Taysi Benjamini-Hochberg (FDR) -korjaus 61 samanaikaiselle testille
  (nyt vain huomautus, ei varsinaista korjausta)
- TimeSeries-luokka-abstraktio (Pythonissa hyodyllisempi rakenteellinen
  parannus; JS:n oma provider-funktio + metadata-rekisteri -yhdistelma
  saavuttaa suurelta osin saman hyodyn ilman luokkia)

**Kayttajan oma arviointi arkkitehtuurista, kirjattu suoraan:**
*"Tama alkaa nayttaa jo paljon enemman ACI:n yhteiselta analyysi-
moottorilta kuin yksittaiselta AMOC-apiohjelmalta... uusi instrumentti
tarkoittaa kaytannossa vain uuden fetch_*()-funktion lisaamista, kun
taas kaikki tilastollinen analyysi... voidaan kayttaa sellaisenaan
uudelleen."*

## VAIHE 4 TOTEUTETTU 2026-07-31 — RAPID mukaan /compare-moottoriin

Kayttajan aiemmin lataama `moc_transports.nc` (BODC, v2024.1a) muun-
nettiin Python/netCDF4-kirjastolla kompaktiksi paivittaiseksi JSON:iksi
(7290 paivaa, 2004-04-07...2024-03-22, paivakeskiarvot 12h-resoluutiosta)
ja julkaistiin staattisena tiedostona `aethercontinuity.org/tools/
rapid_daily.json` (460 KB).

**Tekninen ratkaisu:** Cloudflare Worker EI parsi alkuperaista NetCDF/
HDF5-binaarimuotoa - se hakee sen sijaan jo-esikasitellyn JSON:in
tavallisella `fetch()+json()`-kutsulla `aethercontinuity.org`:ista.

**Nelja uutta sarjaa rekisteroity:** `rapid_moc` (kokonaiskuljetus),
`rapid_umo` (ylakeskiokeaanin kuljetus - TASMALLEEN se suure jota oma
SLA-gradienttimme approksimoi), `rapid_gs` (Florida-salmi/Golfvirta),
`rapid_ek` (Ekman). Kaikki merkitty selvasti ei-live-dataksi (paattyy
maalis 2024) metadatassa.

### Seuraava askel — kriittinen jatkotesti odottaa

Tama mahdollistaa sen aiemmin tunnistetun, tarkeimman jatkotestin:
toistaa alkuperainen SLA-vs-UMO-validointitesti (r=0.339 lag+10:lla,
laskettu RAA'ALLA N=365:lla ENNEN Neff-korjauksen olemassaoloa) nyt
taydella Neff-korjauksella saman yleisen `/compare`-moottorin kautta:

```
GET /compare?series_a=sla&series_b=rapid_umo&date=2024-03-22&days=365
```

Odotettu lopputulos (kirjattu jo aiemmin epailyksena): koska SLA:n oma
autokorrelaatio on vahvistetusti aarimmaisen korkea (~0.95), ja RAPID:n
UMO on fysikaalisesti hidas suure jolla on todennakoisesti samankaltainen
tai voimakkaampi autokorrelaatio, taman testin oma effective N olisi
todennakoisesti samaa pientä luokkaa (~20-30) kuin SLA-vs-NAO-testissa
- mika tekisi aiemmasta "merkitsevasta" r=0.339-loydoksesta todennakoisesti
EI-merkitsevan Neff-korjatulla p-arvolla. Tama testi on viela ajamatta -
seuraava luonnollinen askel.

## TESTI AJETTU 2026-07-31 — SLA vs RAPID_UMO, lopullinen tulos

Testi ajettiin: `series_a=sla&series_b=rapid_umo&date=2024-03-22&days=365`.

**Tulos:** lag=0: r=-0.013 (kaytannossa nolla). "Paras" lag=-30 (HUOM:
osui haun AARIREUNAAN, ei aitoon sisaiseen huippuun - metodologinen
varoitus, ei aito loydos): r=0.359, p=0.070 - EI merkitseva talla-
kaan. Effective N=24.2, sama pieni luokka kuin SLA-vs-NAO-testissa.

### Taysi Benjamini-Hochberg FDR-korjaus toteutettu ja ajettu

Kayttajan oma ehdotus: koska 61 viivetta testataan samanaikaisesti,
"paras loydetty r" on altis satunnaiselle ylikorostumiselle. BH-menetelma
(1995) toteutettiin taydellisesti.

**VAKAVA BUGI LOYTYI JA KORJATTU ENNEN JULKAISUA:** alkuperainen
toteutus kaytti `array.slice(0, maxSignificantRank)` jossa arvo saattoi
olla -1 - mutta JS:ssa `slice(0,-1)` tarkoittaa "kaikki paitsi viimeinen",
EI tyhjaa taulukkoa. Tama olisi tuottanut vaaria positiivisia lahes
kaikissa "ei mitaan merkitseva" -tapauksissa. Loytyi ja korjattiin
paikallisella testauksella (BH:n oma 1995-paperin klassinen esimerkki +
kaksi synteettista aariitapausta) ennen kuin virhe paatyi tuotantoon.

**BH-korjauksen lopputulos SLA-vs-RAPID_UMO-datalla: 0/61 viivetta
merkitseva.** Pienin yksittainen p-arvo koko spektrissa oli 0.070 -
jo yli tavallisen 0.05-kynnyksen ilman mitaan korjaustakaan, joten BH
(joka on vielapa tiukempi) ei tietenkaan loytanyt mitaan.

### LOPULLINEN JOHTOPAATOS koko validointiketjulle

Oma karkea kahden pisteen SLA-gradienttiapproksimaatio EI ole
tilastollisesti perusteltu korvike RAPID:n omalle UMO-mittaukselle,
millaan testatulla viiveella, taydella FDR-korjauksella tarkistettuna.
Alkuperainen, innostunut r=0.339-loydos (raaka N, ennen Neff:ia)
osoittautui lopulta paikkansapitamattomaksi kun samaa kysymysta
testattiin oikealla menetelmalla ja toisen vuoden datalla.

**Tama on hyva, rehellinen paatepiste taman spesifin validointi-
kysymyksen kohdalla.** AMOC-instrumentin muut kolme korttia (SST,
Gronlanti-SMB, RAPID-viitetilastot) pysyvat validina, itsenaisina
indikaattoreina - vain SLA-gradientin rooli "karkeana RAPID-
approksimaationa" on nyt kumottu tilastollisesti perustellusti, ei
vain epailty.

## MERKITTAVA POSITIIVINEN LOYDOS 2026-07-31 — SST korreloi RAPID:n kanssa

Systemaattinen kierros muita sarjapareja /compare-moottorilla paljasti
ensimmaisen aidosti positiivisen, FDR-korjauksen kestavan tuloksen
koko projektissa.

**SST ↔ RAPID_MOC** (date=2024-03-22, days=365):
- lag=0: r=0.392, p=0.019 (jo merkitseva ilman korjaustakin)
- lag=-11 (paras): r=0.525, p=0.0007
- **BH-korjaus: 21/61 viivetta pysyy merkitsevana (lagit -21...-1)**

Tama on laadullisesti eri tulos kuin SLA- ja NAO-testit: 21 PERAKKAISTA
viivetta muodostavat yhtenaisen klusterin, ei yksittaista eristettya
piikkia - tama on juuri se rakenteellinen ero jota pidetaan aidon
signaalin merkkina kohinan sijaan. Suunta on fysikaalisesti mielekas:
SST-anomalia edeltaa MOC-arvoa ~11 vrk:lla - pintalampotilan poikkeama
toimisi varhaisena merkkina tulevasta AMOC-muutoksesta.

**NAO ↔ RAPID_MOC:** BH 0/61 merkitseva, vahvistaen etta NAO ei nayta
suoraa yhteytta RAPID:n oikeaan MOC-arvoon (samansuuntainen tulos kuin
SLA-NAO-testissa).

## KORJAUS 2026-07-31 — SMB-RAPID-aikaikkunaongelma ratkaistu, uusi gmb-sarja

Alkuperainen SMB↔RAPID-vertailu palautti "0 paallekkaista paivamaaraa" -
virheen. Tama EI ollut vaara kyselyparametri: DMI:n GSMB.txt kattaa
vain nykyisen sulamiskauden (~2025-09 alkaen), ei ulotu RAPID:n
historialliselle ajalle (2004-2024) lainkaan - aito rakenteellinen
aikaikkunoiden paallekkaisyyden puute.

**Loydetty parempi, pidempi lahde:** GEUS/PROMICE-massatase (Mankoff
ym. 2021), thredds.geus.dk/MassBalance/MB_cumulative.csv. Paivittainen,
1986-nykyhetki - ulottuu RAPID:n koko ajalle. Lisaksi tama on
KOKONAISMASSATASE (sisaltaa jaatikoiden kalvamisen/discharge), ei
vain DMI:n pintamassatase - tasmalleen se suure jota alunperin
tavoiteltiin (ks. HEM/BEM-E:n oma GRACE-keskustelu paljon aiemmin).

Rekisteroity uutena 'gmb'-sarjana (paivittainen ero kumulatiivisesta
tasosta, testattu paikallisesti). Vanha 'smb' (DMI, nykyinen kausi)
sailytetty ennallaan omana kayttotarkoituksenaan.

**Seuraava askel:** ajaa gmb↔rapid_moc samalla menetelmalla - nyt
kun aikaikkunat aidosti paallekkain, tama on viela testaamaton pari.

## TULOS 2026-07-31 — GMB vs RAPID_MOC, toinen huolellisesti hylatty hypoteesi

Nyt kun aikaikkunat aidosti paallekkain (GEUS/PROMICE ulottuu
RAPID:n koko ajalle), testi ajettiin: N=396, lag-1-autokorrelaatiot
0.846/0.982 (molemmat korkeita), Neff≈40 (taydella ACF:lla).

**Lag=0: r=-0.138.** Paras loydetty: **lag=-27, r=-0.254, p≈0.106,
BH q≈0.615** - EI merkitseva edes ilman korjausta (p>0.05), saati
BH-korjauksen jalkeen. Sama kuri kuin aiemmin: paras-lag-tulos ei
ylitulkittu vaikka se olisi voinut nayttaa "kiinnostavalta" ilman
tilastollista tarkistusta.

**Fysikaalinen tulkinta (kayttajan oma, hyvin perusteltu huomio):**
Gronlannin kokonaismassatase on vain YKSI monista samanaikaisista
AMOC:iin vaikuttavista tekijoista (Labradorinmeren konvektio,
Irmingerinmeren prosessit, NAO, tuulikentta, pintalampotila,
suolaisuus, arktinen makean veden vienti, monivuotiset merivarastot).
Ei ollut odotettavaa etta yhden muuttujan GMB selittaisi merkittavan
osan RAPID:n vaihtelusta yksinaan - negatiivinen tulos on siis
fysikaalisesti johdonmukainen, ei yllattava.

## METODOLOGINEN KEHYS 2026-07-31 — kaksi validointityyppia

Kayttajan oma, tarkea kasitteellinen erottelu joka muuttaa /compare-
moottorin luonnetta pelkasta korrelaatiolaskurista systemaattiseksi
hypoteesien falsifiointityokaluksi:

**Suora validointi** - kysyy: *"nakyyko yhteys datassa?"*
Esimerkkeja: SLA↔RAPID (hylatty), GMB↔RAPID (hylatty), SST↔RAPID
(HYVAKSYTTY, r=0.525 lag-11:lla, BH 21/61 merkitseva)

**Mekanistinen validointi** - kysyy: *"onko olemassa uskottava
fysikaalinen valiketju?"*
Esimerkkeja kayttajan omin sanoin:
- NAO → tuulikentta → Ekman → RAPID_EK
- GMB → makea vesi → suolaisuus → syvaveden muodostus → RAPID_MOC

**Nailla kahdella ei pida sekoittaa toisiaan.** Suora validointi voi
epaonnistua (kuten GMB↔RAPID_MOC juuri teki) vaikka mekanistinen
ketju olisi periaatteessa uskottava - koska valiaskeleet (esim.
suolaisuuden muutos, syvaveden muodostuksen viive) eivat nay suoraan
kahden paateen valisessa korrelaatiossa jos matkalla on useita
muita, kilpailevia vaikuttavia tekijoita.

### Vakiintunut prosessi uusille prokseille (kayttajan oma, kirjattu suoraan)

1. Lisataan uusi fetch_*-moduuli
2. Verrataan RAPIDiin
3. Lasketaan Pearson, Spearman, Neff ja lag-spektri
4. Korjataan monivertailu (BH)
5. Hyvaksytaan tai hylataan proksi datan perusteella

Kayttajan oma yhteenveto: *"Vertailumoottori nayttaa nyt saavuttaneen
pisteen, jossa sita voi kayttaa yleisena hypoteesien
falsifiointityokaluna, ei vain korrelaatiolaskurina... paljon
vahvempi tutkimusasetelma kuin instrumentti, joka etsii vain
vahvistusta ennakko-oletuksille."*

### Tilannekatsaus kaikista suoran validoinnin tuloksista tahan mennessa

| Pari | Tulos | BH-merkitsevia |
|---|---|---|
| SLA ↔ RAPID_UMO | Hylatty | 0/61 |
| SLA ↔ NAO | Hylatty | 0/61 |
| NAO ↔ RAPID_MOC | Hylatty | 0/61 |
| GMB ↔ RAPID_MOC | Hylatty | 0/61 |
| **SST ↔ RAPID_MOC** | **Hyvaksytty** | **21/61** |

Nelja hylattya, yksi hyvaksytty - tama suhde itsessaan on terveellinen
muistutus siita etta useimmat intuitiiviset proksihypoteesit eivat
kestä huolellista tilastollista testausta, ja se on juuri niin kuin
pitaakin olla jarjestelmassa joka aidosti falsifioi, ei vain vahvista.

## TULOS 2026-07-31 — NAO vs RAPID_EK: lupaava mutta vahvistamaton yhteys

Mekanistisen validoinnin ensimmainen testi (kayttajan oma prioriteetti:
NAO -> tuulikentta -> Ekman -> RAPID_EK, suorin odotettu mekanismi).

**Validointitulos:** NAO-RAPID_EK-vertailu tuotti tahan mennessa
vahvimman havaitun yhteyden (paras r≈0.41, lag +1 vrk), ja huipun
sijainti vastaa odotettua fysikaalista mekanismia. Yhteys ei kuitenkaan
sailynyt tilastollisesti merkitsevana 61 viiveen Benjamini-Hochberg-
korjauksen jalkeen (q≈0.078). Tulos luokitellaan lupaavaksi mutta
viela vahvistamattomaksi, ja se ansaitsee jatkotutkimuksia pidemmilla
aikasarjoilla tai ennalta maaritellyilla viivehypoteeseilla.

**Perustelut (kayttajan omat, kirjattu tarkasti):**
- Kohtalainen korrelaatio (r≈0.41) on selvasti suurempi kuin aiemmissa
  hylatyissa vertailuissa (SLA-UMO, SLA-NAO, NAO-MOC, GMB-MOC)
- Huippu sijaitsee lagilla +1 vrk, EI hakualueen reunalla (toisin kuin
  SLA-testeissa) - paremmin linjassa odotetun mekanismin kanssa
- Yksittainen testi (lag=0, p=0.004) on merkitseva, mutta 61 viiveen
  monivertailukorjauksen jalkeen tulos ei ylita ennalta asetettua
  kynnysta
- BH q≈0.078 on lahella, mutta EI ALLE, 0.05:ta

**Tarkea metodologinen huomio kayttajalta, kirjattu suoraan:** jos
tulevissa analyyseissa paatetaan ENNALTA (ennen datan katsomista) etta
testataan vain esim. viiveet -3...+3 vrk (koska fysiikka antaa siihen
perusteen), kyse ei enaa ole 61 vaihtoehdon jalkikateisesta seulonnasta.
Talloin tilastollinen asetelma muuttuu ja naytto voitaisiin arvioida
eri tavalla (vahemman ankaralla monivertailukorjauksella, koska
hypoteesi olisi ennalta rajattu, ei jalkikateen valittu parhaan
tuloksen perusteella).

## KOLMILUOKKAINEN VALIDOINTIKEHYS (kayttajan oma ehdotus, korvaa binaarisen hyvaksytty/hylatty)

Kayttajan oma, tarkeampi jaottelu: pelkka "hylatty/hyvaksytty" ei
riita kuvaamaan tuloksia tarkasti. Kolme luokkaa:

1. **Validoitu tassa aineistossa** - nayttö on vahva ja lapaisee
   ennalta maaritellyt kriteerit TASSA nimenomaisessa datassa; EI
   sama asia kuin lopullisesti vahvistettu luonnonilmio (nyt: vain
   SST-RAPID_MOC)
2. **Lupaava mutta vahvistamaton yhteys** - fysikaalisesti uskottava
   ja datassa nakyva signaali, mutta naytto ei viela tayta asetettua
   tilastollista kynnysta (nyt: NAO-RAPID_EK)
3. **Ei nayttoa yhteydesta** - aineisto ei tue hypoteesia talla
   analyysilla (nyt: SLA-UMO, SLA-NAO, NAO-MOC, GMB-MOC)

**Tarkea kielenkaytollinen huomio kayttajalta:** valtetaan ilmaisua
"melkein merkitseva" - tilastollisesti tulos on joko asetetun
kriteerin mukaan merkitseva tai ei ole. Sen sijaan kuvataan naytto
asteittain (kolme luokkaa ylla).

**PAIVITYS 2026-07-31:** "Validoitu"-luokan nimi tarkennettu muotoon
"Validoitu tassa aineistossa" kayttajan huomiosta - pelkka "Validoitu"
voisi tulkita liian yleispateva vaitteeksi, vaikka rinnalla oleva teksti
jo mainitsee etta 11 vrk:n viive poikkeaa kirjallisuudesta, RAPID
paattyy maalis 2024:aan, ja lisavalidointia tarvitaan. Nama kolme
seikkaa yhdessa viittaavat vahvaan mutta ei viela lopullisesti
vahvistettuun loydokseen.

### Paivitetty tilannekatsaus kaikista tuloksista

| Pari | Paras r | Lag | BH q (huipulla) | Luokka |
|---|---|---|---|---|
| SLA ↔ RAPID_UMO | 0.359 | -30 (reunalla) | ~1.0 | Ei nayttoa |
| SLA ↔ NAO | 0.286 | +12 | ~1.0 | Ei nayttoa |
| NAO ↔ RAPID_MOC | -0.252 | -16 | ~0.94 | Ei nayttoa |
| GMB ↔ RAPID_MOC | -0.254 | -27 | ~0.61 | Ei nayttoa |
| **NAO ↔ RAPID_EK** | **0.415** | **+1** | **~0.078** | **Lupaava, vahvistamaton** |
| **SST ↔ RAPID_MOC** | **0.525** | **-11** | **<0.05 (21/61)** | **Validoitu tassa aineistossa** |

**Jatkoaskel merkitty:** ennalta rajattu viivehypoteesi (esim. vain
-3...+3 vrk NAO-EK:lle, perustuen tunnettuun tuulipakotteen nopeuteen)
voisi antaa tilastollisesti vahvemman testin kuin nykyinen 61 viiveen
jalkikateinen seulonta - ei viela toteutettu.

## TULOS 2026-07-31 — NAO-RAPID_EK kapealla ikkunalla (±3 vrk), tarkka metodologinen kirjaus

Testattiin suppealla, fysiikkaan perustuvalla ikkunalla (maxLag=3):
6/7 viivetta pysyi merkitsevana BH-korjauksen jalkeen (kaikki paitsi
-3, q=0.060). Itse korrelaatioarvot eivat muuttuneet (r~0.40-0.42) -
vain tilastollinen viitekehys (7 testia 61:n sijaan) muuttui.

**Kayttajan oma, tarkka metodologinen kirjaus (sanatarkasti):**

*"NAO ↔ RAPID_EK: Alkuperainen laaja viiveskannaus (-30...+30 vrk)
tunnisti korrelaatiohuipun noin +1 vrk:n kohdalla, mutta tulos ei
sailynyt merkitsevana koko 61 viiveen monivertailukorjauksen jalkeen.
Taman jalkeen tehtiin fysiikkaan perustuva tarkastelu suppeassa ±3
vrk:n ikkunassa, joka vastaa odotettua Ekman-vasteen aikaskaalaa.
Tassa rajatussa analyysissa useat viiveet olivat merkitsevia. Koska
suppea ikkuna maariteltiin vasta alkuperaisen laajan analyysin
jalkeen, tulosta pidetaan hypoteesia tukevana mutta riippumattomassa
aineistossa vahvistettavana, ei lopullisena validointina."*

**Tarkea kielenkaytollinen huomio:** ei kayteta ilmaisua "osittain
tuettu" - se voisi antaa vaikutelman etta naytto on vahvempi kuin se
tilastollisesti on. Sen sijaan kuvataan tarkasti mita tehtiin: kaksi
erillista, peratysta vaihetta jotka EI PIDA sekoittaa:

1. **Eksploratiivinen analyysi** (61 viivetta) - hypoteesin muodostaminen
2. **Hypoteesia tukeva kohdennettu analyysi** (±3 vrk) - lisanaytto,
   mutta ei viela riippumaton vahvistus

**Seuraava askel eksplisiittisesti kirjattu:** testata sama ±3 vrk:n
hypoteesi UUDELLA aineistolla tai myohemmin kertyvalla datalla,
jolloin analyysi olisi aidosti ennalta maaritelty (ei jalkikateen
kapennettu nyt kaytetysta samasta datasta).

**Kayttajan oma kokoava huomio:** *"Sen sijaan etta 'pelastettaisiin'
tulos muuttamalla analyysia huomaamatta, dokumentoidaan avoimesti,
miksi suppea analyysi tehtiin ja miten se vaikuttaa tulkintaan. Se
tekee johtopaatoksesta uskottavamman, vaikka se onkin varovaisempi."*

### Paivitetty luokitus NAO-RAPID_EK:lle

Ei enaa pelkkaa "lupaava, vahvistamaton" vaan tarkempi kuvaus: hypoteesia
tukeva tulos KAHDESSA PERAKKAISESSA analyysivaiheessa (eksploratiivinen
+ kohdennettu), mutta viela ilman riippumatonta, aidosti ennalta
maariteltya vahvistusta uudella datalla. Ei nostettu "Validoitu"-
luokkaan SST:n rinnalle, koska metodologinen ero (jalkikateen
kapennettu ikkuna vs. aidosti ennalta maaritelty) on aito ja tarkea.

## KOLMIVAIHEINEN VALIDOINTIKEHYS (kayttajan oma kokoava kirjaus, 2026-07-31)

Taman kierroksen tarkein saavutus ei ollut yksittainen korrelaatiotulos
vaan se, etta dokumentaatio erottaa nyt selvasti kolme vaihetta:

1. **Eksploratiivinen analyysi** - etsitaan, loytyyko datasta
   ylipaataan kiinnostavia ilmioita (esim. 61 viiveen laaja skannaus)
2. **Kohdennettu analyysi** - testataan fysiikkaan perustuvaa,
   rajattua hypoteesia (esim. ±3 vrk NAO-RAPID_EK:lle)
3. **Riippumaton vahvistus** - sama ENNALTA MAARITELTY testi tehdaan
   UUDELLA aineistolla - TAMA VAIHE PUUTTUU VIELA yhdellakaan
   tahan mennessa testatulla parilla, mukaan lukien SST-RAPID_MOC

### Tarkea rajoite kirjattu etukateen - "maalitolppien siirtelyn" estamiseksi

Koska RAPID-aineisto paattyy maaliskuuhun 2024, todellinen riippumaton
vahvistus EI VALTTAMATTA TULE MAHDOLLISEKSI VIELA PITKAAN AIKAAN.
Nykyinen luokitus (myos SST:n "Validoitu") pitaa sailyttaa varovaisena
kunnes jompikumpi toteutuu:

- RAPID:n seuraava virallinen data-paivitys (uusi versio pidemmalla
  aikasarjalla), TAI
- vaihtoehtoinen, riippumaton havaintosarja joka mittaa samaa prosessia

Tama on kirjattu tarkoituksella nakyvasti ETUKATEEN, jotta
tulevaisuudessa ei voida hiljaa "siirtaa maalitolppia" ja julistaa
jotain validoiduksi ilman etta vaihe 3 on aidosti tapahtunut.

## VERSIOHISTORIA - AMOC-monitorin kehityskaari

- **v0.1** (30.7.2026): rakennettiin instrumentti ja datavirrat (nelja
  korttia: RAPID-viite, SLA-gradientti, SST-anomalia, Gronlanti-SMB)
- **v0.2** (31.7.2026): validoitiin prokseja systemaattisesti /compare-
  moottorilla, mukaan lukien negatiivisten tulosten hyvaksyminen
  (SLA-UMO, SLA-NAO, NAO-MOC, GMB-MOC hylatty; SST-MOC validoitu
  vaiheen 1-2 osalta; NAO-EK lupaava mutta ei viela vahvistettu)
- **Seuraava vaihe** (ei viela alkanut): riippumattomat vahvistukset
  (vaihe 3) niille hypoteeseille jotka jaivat lupaaviksi mutta ei viela
  lopullisesti osoitetuiksi - odottaa RAPID-paivitysta tai
  vaihtoehtoista datalahdetta

**Kayttajan oma loppuarvio, kirjattu suoraan:** *"Tallainen etenemistapa
on metodologisesti vahva, koska dokumentaatio kertoo avoimesti myos
siita, mita instrumentti ei viela tieda. Juuri se lisaa sen
uskottavuutta."*

## VERTAILU AIEMPAAN KIRJALLISUUTEEN (2026-07-31)

Kayttajan oma ehdotus: verrataan omia tuloksia julkaistuun tutkimukseen
samoista yhteyksista. Tama on kirjattu tarkoituksella varovaisesti -
ei "vahvistettu" vaan asteittain, samaan tapaan kuin kolmiluokkainen
validointikehys yleisemminkin.

**NAO ↔ RAPID Ekman (EK).** Oma analyysi loysi voimakkaimman yhteyden
noin +1 vuorokauden viiveella. Tama on linjassa julkaistun kirjallisuuden
kanssa, jossa NAO:n tuulipakotteen on osoitettu vaikuttavan Ekman-
kuljetukseen nopeasti, paivien aikaskaalassa. Moat ym. (2016) kuvaavat
26.5°N RAPID-havaintojen perusteella juuri tallaisen nopean tuulivasteen
(5 vrk aikaskaala), ja Khatri ym. (2022) erottavat nopean Ekman-
valitteisen vasteen hitaasta, useiden vuosien mittaisesta AMOC-
vasteesta. Tama tukee sita, etta lyhyen aikavalin analyysissa juuri
EK-komponentista voidaan odottaa loytyvan yhteys, kun taas koko MOC:n
muutokset eivat viela nay. **Luokitus: yhteensopiva julkaistun
kirjallisuuden kanssa.**

**SST ↔ RAPID MOC.** Oma analyysi tuotti voimakkaimman yhteyden noin
11 vuorokauden viiveella. Julkaistussa kirjallisuudessa vastaavia
yhteyksia on raportoitu tyypillisesti noin kuukauden tai useiden
kuukausien aikaskaaloilla (esim. Yan ym. 2015: 1 kk johtava SST,
SST-SLP-vaihekovarianssi 4-11 kk:n aikaskaaloilla). Taman vuoksi oma
tulos on toistaiseksi kirjallisuuden kanssa vain OSITTAIN yhtenevä:
yhteyden olemassaolo on johdonmukainen, mutta havaittu viive on
selvasti lyhyempi kuin useimmissa aiemmissa tutkimuksissa. Syy voi
liittya aineistojen eroihin, aluevalintaan, suodatukseen, tai siihen
etta lyhytaikainen ja pidempiaikainen SST-vaihtelu kuvaavat osittain
eri fysikaalisia prosesseja. Yksi tukeva yksityiskohta: sama
kirjallisuus (Yan ym. 2015) toteaa korrelaation olevan vahvin
nimenomaan UMO-komponentin kanssa - tasmalleen se suure jota oma
SLA-gradienttimme yritti (epaonnistuneesti) approksimoida aiemmin.
**Luokitus: osittain yhteensopiva kirjallisuuden kanssa; havaittu
viive poikkeaa aiemmista tutkimuksista ja vaatii lisavalidointia.**
Taman vuoksi tulosta ei pideta viela lopullisesti validoituna, vaan
se edellyttaa riippumatonta vahvistusta uudemmalla RAPID-aineistolla
tai toisella havaintosarjalla.

## § 01f — Suodatustestin rajoite (31.7.2026)

SST ↔ RAPID_MOC -parin validointia syvennettiin liukuvan keskiarvon
suodatuksella (30, 60 ja 90 vrk) - kayttajan oma ehdotus mekanistisen
validoinnin Vaihe 1:na.

**Suodatuksen vaikutus.** Kun liukuvan keskiarvon pituutta kasvatettiin
(30 -> 60 -> 90 vrk), korrelaatio SST-anomalioiden ja RAPID MOC:n
valilla voimistui (r≈0.76 -> 0.87 -> 0.92) ja optimaalinen viive
sailyi johdonmukaisesti noin -11 vuorokaudessa. Viiveen pysyvyys
viittaa siihen, ettei havaittu yhteys ole pelkastaan korkeataajuisen
kohinan seurausta.

| Suodatus | Pearson r | Neff | Huomio |
|---|---|---|---|
| Ei suod. | 0.525 | 24.2 | Vertailukohta |
| 30 vrk | 0.762 | 10.4 | Neff puolittuu |
| 60 vrk | 0.872 | 7.8 | Vain ~8 itsenaista jaksoa |
| 90 vrk | 0.921 | 6.6 | Vain ~6-7 itsenaista jaksoa |

**Metodologinen rajoite.** Samalla suodatus kasvatti sarjojen
autokorrelaatiota erittain voimakkaasti (lag-1 ≈ 1), jolloin
havaintojen tehollinen maara (Neff) pieneni noin 10:sta alle 7:aan.
Tama on odotettu seuraus pitkista paallekkaisista liukuvista
keskiarvoista eika analyysivirhe - 90 vrk:n ikkuna limittyy 89/90-
osaltaan vierekaisen paivan kanssa. Se kuitenkin tarkoittaa, etta
suodatetut korrelaatiot perustuvat hyvin pieneen maaraan riippumattomia
havaintoja.

**Johtopaatos.** Tulosta ei tule tulkita siten, etta 90 vuorokauden
suodatus "todistaisi" vahvemman fysikaalisen yhteyden. Luotettavampi
tulkinta on, etta analyysi osoittaa stabiilin noin 11 vuorokauden
viiverakenteen, mutta kaytettavissa oleva yhden vuoden aineisto on
liian lyhyt vahvistamaan kuukausimittakaavan yhteytta tilastollisesti
riippumattomien havaintojen perusteella. Hypoteesi vaatii vahvistuksen
usean vuoden aineistolla tai vaihtoehtoisesti menetelmilla, jotka
mallintavat autokorrelaation suoraan (esim. ARIMA- tai Monte Carlo
-surrogaattitestit).

**Kayttajan oma, erityisen kiinnostava huomio:** paras viive pysyy
tasmalleen -11 vuorokaudessa kaikilla kolmella suodatustasolla. Tama
on metodologisesti vahvempi havainto kuin pelkka korrelaatiokertoimen
kasvu, koska juuri korrelaation suuruus on herkempi suodatuksen
aiheuttamille vaikutuksille, kun taas viiveen pysyvyys voi heijastaa
aidompaa dynamiikkaa. Tamakin kannattaa kuitenkin nahda toistaiseksi
hypoteesia tukevana havaintona, ei viela naytto syy-seuraussuhteesta.

### Seuraava askel: koko 2004-2024 RAPID-datan kaytto

Kayttajan oma suositus: koska RAPID-dataa on 20 vuotta (josta vain
yksi vuosi oli tarkastelussa), laajenna suodatustesti kattamaan koko
aikasarjan. Jos signaali on aito, korrelaatio sailyy ja Neff on
riittava (esim. >30) paljon suuremmalla raa'alla N:lla. Vaihtoehtoinen
menetelma: kuukausikeskiarvot ilman liukuvia ikkunoita (ei limittymista,
Neff vastaisi todellisia vapausasteita paremmin).

## TEKNINEN LAPIMURTO 2026-08-01 — Cloudflare Cache API osoittautui alipyyntoongelman syyksi

Kayttajan pitka, systemaattinen vianetsinta (502->503->502, palojen
pienennys 21->3->1, kuukausittainen naytteenotto, monthStep-saato
6->12) paljasti lopulta etta itse **Cache API -kaare** (`cachedFetch`,
lisatty aiemmin valimuistia varten) oli subrequest-rajan ylityksen
todellinen syy - vaikka Cloudflaren oma dokumentaatio nimenomaisesti
sanoo etta `cache.match()` "never sends a subrequest to the origin."

**Diagnoosi:** dryRun-tila vahvisti laskennan taysin oikeaksi (20
ankkuripistetta, ~21 arvioitu alipyyntomaara - selvasti alle ilmaisen
tason 50:n rajan) mutta oikea haku epaonnistui silti. Vaihdettaessa
`cachedFetch` takaisin plain `fetch()`:iin (poistaen Cache API -kaare
kokonaan) ongelma katosi valittomasti.

**Johtopaatos:** joko Cache API:n kaytannon toiminta poikkeaa dokumen-
toidusta tassa nimenomaisessa tilanteessa (esim. `cache.put()` yhdessa
streamatun Response bodyn klonauksen kanssa saattaa aiheuttaa jotain
ylimaaraista), tai kyseessa on jokin muu, hienovarainen vuorovaikutus.
Valimuisti poistettu toistaiseksi taman /compare-polun ERDDAP-hausta -
merkitty jatkokehitykseksi rakentaa se takaisin turvallisemmalla
tavalla (esim. KV-storage Cache API:n sijaan).

## TULOS 2026-08-01 — SST vs RAPID_MOC, kiintea -11 vrk viive, 20 vuotta (yksi piste/vuosi)

Ensimmainen onnistunut pitkan aikavalin testi: **r=0.069, p=0.77,
Neff=20** - kaytannossa ei mitaan yhteytta.

### KORJAUS 2026-08-01: alkuperainen "kausivaihtelun yhteensattuma" -selitys oli liian kevyt

Kayttajan oma, tarkempi kritiikki: *"Luonnonilmio ei kayttaydy
kalenteripaivien mukaan."* Tama on oikea, terävampi huomio kuin
alkuperainen selityksemme.

### KORJAUS 2026-08-01 (toinen kierros): oma aiempi korjauskin oli liian vahva

Kayttajan tarkennys omaan aiempaan korjaukseeni: yllaoleva vaite
("jos -11 vrk on todellinen, JATKUVA fysikaalinen prosessi... sen
pitaisi nakya mista tahansa vuoden kohdasta") on ITSESSAAN liian vahva
vaite. Luonnossa monet prosessit ovat kausiriippuvaisia - SST:n ja
RAPID:n valinen kytkenta voi hyvinkin vaihdella vuodenaikojen mukaan,
eika oletus "pitaisi nakya ymparivuotisesti" ole perusteltu ilman
lisanaytto.

**Korjattu, tarkempi muotoilu (kayttajan oma, kirjattu sanatarkasti):**

*"Miksi tulos ei kumoa alkuperaista loytoa: Sama kalenteripaiva eri
vuosilta ei ole riippumaton testi alkuperaiselle hypoteesille. Jos
SST-RAPID-yhteys on vuodenaikaan sidottu tai vaihtelee vuosittain,
yksittaisen kalenteripaivan vertaaminen 20 vuoden yli voi havittaa
signaalin kokonaan. Tulos (r≈0) osoittaa vain, ettei juuri tama
kalenterileikkaus sisaltanyt havaittavaa yhteytta. Se ei yksin
vahvista eika kumoa alkuperaista -11 vuorokauden viivehavaintoa.
Luontevampi jatkotesti on toistaa koko 61 viiveen analyysi useille
toisistaan riippumattomille vuosille tai pidemmille ajanjaksoille ja
arvioida, toistuuko sama viive johdonmukaisesti."*

**Ero aiempaan:** ei enaa vaiteta etta ilmion "pitaisi nakya mista
tahansa vuoden kohdasta" - sen sijaan selitetaan miksi KAYTETTY TESTI
ei valttamatta ole herkka havaitsemaan kyseista ilmiota, jattaen
auki mahdollisuuden etta yhteys on aidosti kausiriippuvainen.
KOKO 61 VIIVEEN PAIVATASON SKANNAUS TOISTETTUNA USEALLE ERI,
RIIPPUMATTOMALLE VUODELLE ERIKSEEN (esim. 2010, 2015, 2020, kukin oma
taysi 365 paivan ikkunansa). Jos -11 vrk:n huippu loytyy johdonmukai-
sesti jokaisesta naista riippumatta mihin vuodenaikaan tai vuoteen
data osuu, se olisi aito, kalenterista riippumaton signaali. Tama
testaisi ilmiota sen OMILLA ehdoilla, ei meidan kalenterimme ehdoilla.
Ei viela toteutettu.
on merkitty seuraavaksi askeleeksi, ei viela toteutettu.

## KONTEKSTI 2026-08-01 — ilmakehan CO2/metaani, ei toteutettu datasarjana

Kayttajan kysymys: miten ilmakehan CO2/CH4-pitoisuudet liittyvat
AMOC:iin. Kayttajan oma paatos: ei rakenneta datapipelinea talle,
vain mainitaan kontekstina.

**CO2 -> AMOC on paaasiallinen, kausaalisesti todennettu suunta.**
Kim ym. (2021, npj Climate) kaytti Convergent Cross Mapping -menetelmaa
(kausaalisuuden tunnistus dynaamisten jarjestelmien teoriasta) OIKEALLE
havaintodatalle, ei vain malleille: nouseva CO2 vaikuttaa Pohjois-
Atlantin lampovoihin ja sadantaan, heikentaen AMOC:ia - arvioitu
3.7±1.0 Sv 1854-2016, suurempi kuin mallien oma arvio (1.4±1.4 Sv).
Mekanismi kulkee juuri LAMPOVOIDEN (SST - ainoa validoitu loytomme)
ja SADANNAN (makea vesi - GMB-testimme) kautta - sama kaksi valikatta
jotka olemme jo testanneet erikseen, vain ei suoraan CO2:ta itseaan.

**Aikaskaalaongelma tekee suorasta testauksesta epakaytannollista:**
mallitutkimukset osoittavat AMOC:n tasapainottuvan CO2-pakotteeseen
VUOSISATOJEN-VUOSITUHANSIEN aikaskaalalla (2xCO2: ~2000v, 8xCO2:
>10000v). Tama on sama rakenteellinen ongelma kuin SST-suodatustestissa
- meidan 1-20 vuoden ikkunamme ei voisi koskaan tavoittaa tata
nimenomaista, hidasta pakotereittia suoraan, vaikka se olisi todellinen.

**Metaani:** heikommin suoraan testattu nykydatalla - vahvin naytto
paleoklimatologiasta (jaaydinnaytteet, CH4-piikit Dansgaard-Oeschger
-tapahtumissa, jaakausiaikaskaalaa, ei nykyhetken vuosikymmenia).

**Takaisinkytkenta (AMOC -> CO2):** olemassa, mutta suunta/voimakkuus
epavarma (meren/maan hiilikierron kautta). Kiinnostava sivuhavainto:
heikentynyt AMOC voi pitkittaa alueellista kuivuutta (Valimeri) VAIKKA
CO2-paastoja vahennettaisiin - osoittaen etta valtameren oma hitaus
voi tehda ilmastovaikutuksista osittain palautumattomia lahivuosi-
kymmenina.

**Paatos:** ei lisata CO2/CH4-sarjaa /compare-tyokaluun (esim. NOAA
Mauna Loa) - aikaskaalaongelma tekisi testista todennakoisesti
tuloksettoman samalla tavalla kuin muut lyhyen aikavalin testimme,
eika lisaarvoa katsottu riittavaksi oikeuttamaan uutta datapipelinea.
Mainittu vain kontekstina taman dokumentin sivuhuomautuksena.

## RAJOITE 2026-08-01 — dekadien valinen vertailu ei ole mahdollinen tallla instrumentilla

Kayttajan oma huomio: ilmio etenee hitaasti, tarkastelua pitaisi tehda
vertaamalla vuosikymmenten tilastoja paivätason viivekorrelaation
sijaan.

**Tarkistettu suoraan RAPID:n omasta datasta:** koko aikasarja kattaa
tasmalleen 20,0 vuotta (2004-04-02 - 2024-03-27) - TASMALLEEN kaksi
dekadia. Tama ei riita minkaanlaiseen tilastollisesti mielekkaaseen
dekadien valiseen korrelaatioon tai trendianalyysiin - tarvittaisiin
vahintaan 5-10 riippumatonta dekadia (50-100+ vuotta).

**Kuvaileva vertailu (ei tilastollinen testi, vain kaksi lukua):**
- 2004-2014: MOC ka=17.18 Sv, stdev=4.66
- 2014-2024: MOC ka=16.77 Sv, stdev=4.12
- Muutos: -0.4 Sv - pieni murto-osa luonnollisesta vaihtelusta

**Vaihtoehto - Kim ym. (2021) / Caesar ym. (2018) SST-pohjainen
rekonstruktio 1854/1870-nykyhetki:** menetelma laskee SST-indeksin
(subpolaarisen pyorteen keskilampotila miinus globaali keskiarvo,
"lampenemisreika"/"kylma laiska" -kuvio), kalibroi taman CMIP-
ilmastomalleja vasten, ja soveltaa kalibroitua suhdetta pitkaan
SST-havaintosarjaan (HadISST) rekonstruoidakseen AMOC:n voimakkuuden
ajalta ennen RAPID:ia. Tulos: ~3±1 Sv heikkeneminen 1900-luvun
puolivalista.

**Mutta tamakin menetelma on itsessaan kiistanalainen:** tuore
CMIP6-mallivertailu (2025) osoitti etta SPG-sormenjalki "ei seuraa
AMOC-vaihtelua johdonmukaisesti" luonnollisen vaihtelun simulaatioissa -
oletettu tiukka kytkenta ei pida johdonmukaisesti paikkaansa. Toinen
tutkimus (2024) lisaa etta sormenjalki muuttuu vahemman luotettavaksi
voimakkaamman lampenemisen oloissa.

### LOPULLINEN JOHTOPAATOS

**Dataa ei ole saatavilla tarpeeksi pitkalta aikavalilta ilmion
arviointiin nailla valineilla.** RAPID:n oma suora mittaus (20v) on
liian lyhyt dekadien valiseen vertailuun. Vaihtoehtoiset, pidemmat
SST-pohjaiset rekonstruktiot ovat olemassa, mutta ne ovat itsessaan
mallikalibroituja prokseja joilla on tuoreesti dokumentoituja, avoimia
luotettavuusongelmia - ei suoria, riidattomia ikkunoita menneisyyteen.
Tama instrumentti ei siis pysty tallla hetkella vastaamaan
kysymykseen AMOC:n vuosikymmenten aikaskaalan kayttaytymisesta millaan
tallla hetkella kaytettavissa olevalla tyokalulla tai datalahteella.

## KONTEKSTI 2026-08-01 — albedo-takaisinkytkenta Gronlannin jaamassaan, ei toteutettu datasarjana

Kayttajan huomio: jos peruskallio paljastuu, albedo muuttuu
huomattavasti, kiihdyttaen tasapainon muutosta. Ei kirjattu
datapipelinena, vain kontekstina.

**Nykytila (2026):** hallitseva mekanismi ei viela ole laajamittainen
peruskallion paljastuminen, vaan LUMIRAJAN SIIRTYMINEN paljastaen
tumman PALJAAN JAAN (ei kalliota) lumen alta. Van As ym. (Science
Advances): 2001-2017 tama selitti 53% nettoauringonsateilyn
vaihtelusta sulamisvyohykkeella, vahvisti sulamista 5x verrattuna
muihin tummentaviin prosesseihin (levat, hydrologinen lika).
Vahvistuu edelleen koska jaatikko litistyy korkeammilla korkeuksilla
lampenevassa ilmastossa. Varsinainen kallio (albedo ~0.1-0.2) olisi
viela tummempi kuin paljas jaa (~0.3-0.4) - tapahtuu jo reunoilla,
ei viela laajamittaisesti keskiosissa.

**Vastakkainen, hidastava mekanismi:** peruskallion ISOSTAATTINEN
KOHOAMINEN jaamassan vahentyessa - negatiivinen takaisinkytkenta,
noin 1/3 jaan paksuuden muutoksesta ~3000 vuoden aikaskaalalla.

Ei lisatty uutta datasarjaa - mainittu vain kontekstina taman
dokumentin sivuhuomautuksena, samaan tapaan kuin CO2/CH4-konteksti
edella.

## PAATTAVA METODOLOGINEN KEHYS 2026-08-01 — mylly, vilja, resepti

Keskustelun paatteeksi syntyi vertaus joka tiivistaa taman koko
projektin keskeisen opetuksen. Kayttajan oma, kolmiosainen jaottelu
(oma alkuperainen kaksiosainen vertaukseni + kayttajan lisaama
kolmas kategoria):

1. **Myllyongelma** - laskenta-, ohjelmisto- tai infrastruktuurirajoite.
   Ratkeaa paremmalla tyokalulla, optimoinnilla tai enemman lasken-
   tateholla. Esimerkki tasta projektista: Cache API -bugi
   (subrequest-raja), ERDDAP:n pitka-aikavali-502-ongelma - molemmat
   ratkesivat koodilla/arkkitehtuurilla.

2. **Viljaongelma** - dataa ei yksinkertaisesti ole olemassa. Ratkeaa
   vain ajan myota tai korvaamalla puuttuva tieto epasuoralla
   aineistolla. Esimerkki: RAPID:n 20 vuoden raja dekadien valiseen
   vertailuun - mikaan mylly ei loihdi lisaa vuosia tyhjasta, vain
   aika tai epasuorat rekonstruktiot (joilla oma epavarmuutensa) auttavat.

3. **Reseptiongelma** - data on olemassa, mutta alkuperainen hypoteesi
   ei kuvaa todellisuutta. Talloin parempi mylly eika enempaa viljaa
   auta. Esimerkki: SLA↔RAPID_UMO - oikea RAPID-aikasarja, kunnollinen
   analyysimenetelma (Pearson/Spearman/Neff/BH-korjaus), asianmukaisesti
   tehdyt tilastolliset testit - ja tulos silti negatiivinen. Ongelma
   ei ollut laskennassa eika datan maarassa, vaan siina ettei kahden
   pisteen SLA-gradientti toiminut haluttuna RAPID-proksina tassa
   aineistossa.

**Yleistettava periaate (kayttajan oma muotoilu):** *"Ensin kysy: onko
kyse myllyongelmasta, viljaongelmasta vai reseptiongelmasta? Vasta
sitten kannattaa paattaa, rakennetaanko isompi mylly, odotetaanko
lisaa viljaa vai kirjoitetaanko resepti uusiksi."*

Tama on yleistettavissa paljon taman yhden AMOC-projektin ulkopuolellekin:
moni tutkimushanke hukkaa aikaa kasvattamalla "myllya" vaikka ongelma
onkin datan rajallisuudessa tai itse hypoteesissa. Taman projektin oma
vahvuus oli valmius hyvaksya myos kolmas vaihtoehto (SLA:n hylkaaminen,
GMB:n hylkaaminen, NAO-MOC:n hylkaaminen) kun validointi ei tukenut
alkuperaista oletusta - tama on tutkimusmetodologisesti arvokas
lopputulos, ei epaonnistuminen.
