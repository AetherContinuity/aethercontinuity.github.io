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

### 2. Sentinel-6 geostrofinen virtausindikaattori
- **Lähde:** NOAA Laboratory for Satellite Altimetry (LSA), Sea Level
  Anomaly (SLA) -tuote, 0.25° ruudukko
- **Päivitystahti:** päivittäin, 3-5h viive (lähes reaaliaikainen)
- **Sisältö:** merenpinnan korkeuspoikkeama + siitä johdetut
  geostrofiset virtaukset
- **EI VIELÄ tarkistettu:** tarkka API-osoite/formaatti NOAA CoastWatch
  -palvelusta, vaatiiko rekisteröintiä

### 3. Pohjois-Atlantin meriveden lämpötila-anomalia (SST)
- **Lähde:** ei vielä tarkennettu - useita vaihtoehtoja (NOAA OISST,
  ERSST) ovat laajasti käytettyjä ja hyvin dokumentoituja
- Tunnettu proksi: subpolaarisen "kylmän läiskän" (cold blob)
  jäähtymissignaali toimii yhtenä AMOC:n omana "sormenjälkenä"

### 4. Grönlannin makean veden indikaattori
- **Lähde:** GRACE (2002-2017) + GRACE-FO (2018-nyk.) -satelliitti-
  gravimetria, jäämassan muutos
- **Pääsy:** NASA JPL PODAAC (DOI: 10.5067/GFL20-MJ061) TAI ESA:n
  Climate Change Initiative (DTU Space -tuote)
- **Tuore luku (NOAA Arctic Report Card 2025):** massatase -129±50 Gt
  (2003-2024 keskiarvo -219±16 Gt/v)
- **Mekanismi AMOC:iin (ei vain korrelaatio):** sulamisvesi makeuttaa
  Labradorinmerta → heikentää Labradorinmeren veden (LSW) muodostumista
  → LSW on keskeinen AMOC:n syvän paluuvirtauksen komponentti

## Tunnistettu, vielä ratkaisematon tekninen kysymys

RAPID:n oma sähköpostivaatimus on ainoa neljästä lähteestä joka ei
sovi suoraan WEM-tyyppiseen "live-haku joka lataus" -arkkitehtuuriin.
Kolme vaihtoehtoa selvitettäväksi ennen koodausta:
1. Kokeile AMOCatlas-kirjastoa - ehkä se käyttää jotain muuta,
   avointa peilipalvelinta datalle
2. Rekisteröidy itse, tarkista tuleeko sen jälkeen suora, uudelleen-
   käytettävä latauslinkki (samaan tapaan kuin Copernicus-tunnukset)
3. Jos kumpikaan ei toimi: harkitse harvempaa päivitystahtia (esim.
   kuukausittainen käsin päivitys, kuten Tripwire-kalenterin
   sääntelyosio) sen sijaan että vaadittaisiin live-haku joka lataus

## Seuraavat askeleet järjestyksessä

1. Testaa AMOCatlas-kirjaston `read.rapid()` - toimiiko ilman
   sähköpostirekisteröintiä
2. Selvitä NOAA:n Sentinel-6/SLA-datan tarkka API-osoite
3. Valitse SST-anomalialähde (todennäköisesti NOAA OISST, laajimmin
   käytetty ja hyvin dokumentoitu)
4. Vahvista GRACE/GRACE-FO-datan tarkka hakumuoto (PODAAC vs. ESA CCI)
5. Vasta kaikkien neljän lähteen vahvistuttua: rakenna ensimmäinen
   yksinkertainen näyttö (ei vielä yhdistelmäindeksi) - yksi kortti
   per indikaattori, samaan tapaan kuin WEM:n §11:n kokeelliset kortit
