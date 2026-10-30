# ACI — Eduskunta- ja dataseuranta 2026

Päivitetty: 26.4.2026

---

## Eduskunta-asiakirjat

| Tunnus | Nimi | Valiokunta | Status | Seuraava vaihe |
|--------|------|------------|--------|----------------|
| VNS 8/2025 vp | Energia- ja ilmastostrategiaselonteko | TaV + YmV | Käsittelyssä | Mietintö ~29.4.2026 — lue kapasiteettimekanismimaininta |
| HE 24/2026 vp | Ydinenergialaki | TaV + YmV + LaV | Käsittelyssä | Kertoo poliittisesta tahdosta uuteen kapasiteettiin |
| HE 62/2026 vp | Polttoaineiden kestävyyskriteerit | TaV | Lähetekeskustelu käyty | Voimaan 5.8.2026 |

**Seurantalinkki:** eduskunta.fi → hae asiatunnus → "Seuraa asiaa" → sähköposti-ilmoitus

---

## Yhteydenotot

| Päivämäärä | Kohde | Aihe | Status |
|------------|-------|------|--------|
| 18.2.2026 | Atte Harjanne (vihr.) | Energia- ja teollisuusinvestointien koordinaatio | Vastaus saatu 19.2. — "kiinnostava papru" |
| 7.2.2026 | EU-komissio | Open consultation, climate resilience framework | Lähetetty, julkinen kirjaus |
| 25.4.2026 | Heikki Vestola, TaV | VNS 8/2025 vp, sähköjärjestelmän kestävyysvaje | Lähetetty — odottaa vastausta |
| 25.4.2026 | Marjukka Sippola, YmV | VNS 8/2025 vp, CHP-alasajon yhteisvaikutukset | Lähetetty — odottaa vastausta |

---

## Fingrid / ENTSO-E dataseuranta

| Julkaisu | Arvioitu ajankohta | Relevanssi |
|----------|--------------------|------------|
| Fingrid riittävyyskatsaus 2026 | Syksy 2026 | Vahvistaako/kumoaako §2.5 perusskenaarion |
| ENTSO-E ERAA 2026 | Alkuvuosi 2027 | Päivittää kapasiteettivajeen luvut |
| Fingrid talvikatsaus 2025–2026 | Julkaistu | Tuotanto- ja kulutusennätykset tammikuussa |

---

## Seuraavat toimenpiteet

- [ ] Lue VNS 8:n mietintö kun valmistuu (~29.4.) — onko kapasiteettimekanismimaininta?
- [ ] Jos ei mainintaa → kirjaa epilogiin: "Selonteko ei johtanut kapasiteettipäätökseen"
- [ ] Syksy 2026: Fingrid-raportin jälkeen seurantaviesti Vestolalle ja Sippolalle
- [ ] Q4-2026: EU:n ilmastonkestävyysviitekehys julkaistaan — seurantaviesti Annika-Gilstrom.FORGAARD@ec.europa.eu

---

## WP-017 — Parliamentary Decision Latency

**Versio:** v0.7 | **Päivitetty:** 26.4.2026
**Paperi:** https://aethercontinuity.org/papers/wp-017-parliamentary-decision-latency.html

### Referee-kierrokset

| Kierros | Referee | Päätös | Status |
|---------|---------|--------|--------|
| 1 | Referee A | Ehdollisesti hyväksy — major revisions | Korjattu v0.3 |
| 2 | Referee B | Near-publishable — identifikaatio + väitteen mittakaava | Korjattu v0.4 |

### Versiohistoria

| Versio | Muutos |
|--------|--------|
| v0.1 | Pre-print julkaistu |
| v0.2 | Salazar-mekanismi kalibroitu, core thesis lisätty |
| v0.3 | Referee A: spread-hajonta, S&P-aika, falsifiointikriteerit, 2Y-10Y |
| v0.4 | Referee B: overclaim poistettu, FI-DE identifikaatiorajoite, placebo-testi |
| v0.5 | Novo Nordisk confound FI-DK analyysiin |
| v0.6 | §4.5: tuulivoima — capacity installed vs capacity integrated |
| v0.7 | §4.6: kolmen maan investointiputki-typologia (DK/ES-PL/FI) |

### Data

| Tiedosto | Sisältö |
|----------|---------|
| scripts/wp017_spread_data.json | FI-DE 39 kk (2023–2026) |
| scripts/wp017_fise_data.json | FI-SE 39 kk (2023–2026) |
| scripts/wp017_all_spreads_2020_2026.json | FI-DE + FI-SE + FI-DK 75 kk (2020–2026) |
| scripts/wp017_data_collector.py | Pilottiskripti + parlamentaaritapahtumat |

**Proxy:** https://github.com/AetherContinuity/aci-ecb-proxy v2.3
**Endpointit:** FI10Y · DE10Y · SE10Y · DK10Y · FI-DE · FI-SE · FI-DK · ALL

### Avoimet kysymykset (seuraava referee-kierros)

1. Monetary policy control — tarvitaanko inflaatio-odotusten kontrolli (5y5y swap)?
2. Seuraava instrumentti — 2Y-10Y term spread (Eurostat, ilmainen) vai CDS?
3. Salazar-mekanismi — Referee A ehdotti sisällönanalyysiä rating-lausunnoista
4. Typologia §4.6 — vaatiiko vertaisarviointi lisää maiden dataa?

---

## Luottoluokitustilanne

| Toimija | Luokitus | Näkymät | Viimeisin muutos |
|---------|----------|---------|-----------------|
| Fitch | AA | Vakaa | Laski AA+→AA heinäkuu 2025 |
| Scope | AA+ | Negatiivinen | Elokuu 2025 |
| S&P | AA+ | Negatiivinen | **24.4.2026** — kehysriihen jälkeen, <24h reaktioaika |
| Moody's | Aa1 | Vakaa | Ei muutosta |

S&P seuraava arvio: **lokakuu 2026**

---

## Raportti

Versio: 4.1 | Päivitetty: 26.4.2026
URL: https://aethercontinuity.org/papers/suomen-energiajarjestelman-rakenteellinen-lukkiutuminen.html

---

## Kuopion energiajärjestelmä — hankeseuranta (perustettu 21.10.2026)

Sivu: `tools/kuopio-seuranta.html` · aineisto: `tools/data/kuopio-seuranta.json`

Seurataan, miten etusijalaki, Mustakorven datakeskus (Polarnode), Kuopion Energian LDR-50 ja Volaghyn eSAF etenevät omissa putkissaan ja miten kaupungin päätökset muovaavat lopputuloksen. Ennakkokirjaukset K1–K5 lukittu 21.10.2026; uudet havainnot vain päivättyinä lokimerkintöinä JSON-tiedoston `log`-taulukkoon. Kirjauksen tilaa (`avoin` → `vahvistui` / `kumoutui`) muutetaan vain lokimerkinnän perusteella, ja merkintä viittaa kirjaukseen (`refs`).

Lähteet: ymparisto.fi (YVA), kuopio.oncloudos.com (kaupungin esityslistat), hankeikkuna / eduskunta (TEM043:00/2026), Kuopion Energian tiedotteet ja vastuullisuusraportti.

---

## AMOC — ennakkokirjaus ennen RAPID v2024-2 -dataa (27.10.2026)

RAPID ilmoitti 23.10.2026 päivityksestä v2024-2 (huhtikuu 2004 – marraskuu 2024, doi:10.5285/5c39bf4e-5140-5546-e063-7086abc027bc). Repon nykyinen `tools/moc_transports.nc` on v2024.1a ja päättyy 27.3.2024. Uutta dataa ei ole vielä ladattu eikä nähty.

**Ennuste (A1):** SST↔RAPID_MOC-korrelaatio viiveellä −11 vrk on jaksolla 28.3.–30.11.2024 tilastollisesti merkitsemätön (p > 0,05, efektiivisellä otoskoolla korjattuna), samoin kuin koko sarjassa (AMOC-monitori §01h). Menetelmä sama kuin §01h:ssa: sama SST-piste ja -lähde (`/sst-anomaly`), sama Neff-korjaus, viiveet −30…+30 vrk raportoidaan kaikki.

**Kumoutuu, jos:** viiveellä −11 vrk p < 0,05 Neff-korjattuna uudella jaksolla.

**Lisäksi kirjataan ennen analyysiä:** versioiden v2024.1a ja v2024-2 erot päällekkäisellä jaksolla 2004–3/2024 raportoidaan ennen kuin uutta jaksoa analysoidaan. Jos aiemmat arvot ovat muuttuneet, §01h lasketaan uudelleen koko sarjalle v2024-2:lla.

Huom.: ennuste esitettiin keskustelussa 23.10.2026, mutta se kirjattiin repoon vasta tällä commitilla 27.10.2026. Data ei ollut kumpanakaan päivänä saatavilla.

**Tulos 27.10.2026 (lisätty, kirjausta ei muutettu):** A1 vahvistui. Jaksolla 28.3.–25.11.2024 r = 0,08 viiveellä −11 vrk, Neff 40, p = 0,64; 0/61 viivettä merkitsevä (BH); surrogaatti-p 0,63. Kausisykli poistettuna r = −0,22, p = 0,53. Versioerot v2024.1a ↔ v2024-2 raportoitiin ensin: harha +0,16 Sv, r = 0,985 (5 vrk), joten aiemmat tulokset pysyvät. Poikkeamat: v2024-2:ssa ei päiväsarjaa (5 vrk interpoloitu), jakso päättyy 25.11., komponentit puuttuvat. AMOC-monitori §01i; `tools/data/amoc-a1-results.json`.

---

## AMOC — ennakkokirjaus B1 ennen OSNAP-analyysiä (30.10.2026)

Aineisto: `OSNAP_MOC_MHT_MFT_TimeSeries_201408_202006_2023.nc` (Fu ym., luotu 24.4.2023), kuukausiarvot 8/2014–6/2020 (71 kk), MOC tiheyskoordinaateissa (σθ). Tiedosto saatiin 30.10.2026; tämä kirjaus tehtiin ennen kuin arvoja luettiin tai laskettiin. Uudempi versio (8/2014–7/2022, 2025) on olemassa mutta ei käytössä.

Kaikki parit kuukausianomalioina (kausisykli poistettu), Pearson viiveittäin, Neff ACF:stä, p t-jakaumasta, Benjamini–Hochberg α = 0,05, kuten §01h. RAPID-vertailussa käytetään v2024-2:n sarjaa `amoc_sigma0_1m` (sama koordinaatti kuin OSNAP).

**B1a.** SST 60°N 30°W ↔ OSNAP East MOC, viiveet −6…+6 kk. *Ennuste:* ei BH-merkitsevää viivettä. *Kumoutuu, jos:* vähintään yksi viive BH-merkitsevä.

**B1b.** OSNAP koko MOC ↔ RAPID AMOCσ0, viiveet −12…+12 kk. *Ennuste:* ei BH-merkitsevää viivettä, ja |r| < 0,3 kaikilla viiveillä. *Kumoutuu, jos:* jokin viive BH-merkitsevä tai |r| ≥ 0,3.

**B1c (toistotarkistus, ei hypoteesi).** OSNAP koko MOC:n vaihtelu seuraa East-osaa enemmän kuin West-osaa (Lozier ym. 2019): r(ALL, EAST) > r(ALL, WEST) samanaikaisesti.

**Voimarajoitus kirjattu etukäteen:** N = 71, kuukausisarjoissa Neff todennäköisesti 15–35; vain |r| ≳ 0,4 voi tulla merkitseväksi. Nollatulos B1a/B1b:ssä ei siis osoita, ettei yhteyttä ole, vaan ettei tällä aineistolla havaittavaa yhteyttä ole.

**Tulos 30.10.2026 (lisätty, kirjausta ei muutettu):** B1 piti, kaksi osaa niukasti. B1a: paras r = −0,41 viiveellä −1 kk (nimellinen p = 0,04), Neff 26, 0/13 BH-merkitsevä. B1b: suurin |r| = 0,295 viiveellä −6 kk (nimellinen p = 0,02), Neff 64, 0/25 BH-merkitsevä; raja |r| < 0,3 täyttyi 0,005:n marginaalilla. B1c toistui: r(ALL, EAST) = 0,91, r(ALL, WEST) = 0,42. B1a:n negatiivinen yhteys on hypoteesi OSNAP 2020–2022 -aineistolle, ei tulos. AMOC-monitori §01j; `tools/data/amoc-b1-results.json`.

---

## BEM-E — ennakkokirjaus D ennen Karttulanlahden aikasarjaa (30.10.2026)

Tausta: käyttäjän havainto 30.10.2026, että Virmasveden Karttulanlahdella (62°53'22"N 26°58'24"E, Kuopio) on koettu samantyyppinen kehitys kuin Kolvosessa. NDCI-arvoja ei ole laskettu ennen tätä kirjausta. Kesäkuvia ei ole katsottu; polygonin rajaamiseen käytettiin vain toukokuun kuvaa.

**Polygoni (kiinnitetty):** `tools/data/bem-e/karttulanlahti_m40.geojson` (sha256 alkaa 08f8309dff733598). Sentinel-2 SCL = 6, 11.5.2025 (35VMK), leikattu UTM35-ikkunaan 498141–499441 E, 6972130–6973980 N (lahden suu eteläreunassa), suurin yhtenäinen vesialue, −40 m puskuri: 0,175 km² (raaka 0,341 km²). **Mittari** kuten C: `/lake-timeseries`, NDCI, touko–syyskuun P10D-mediaani, 2018–2026. **Vertailu:** Iisvesi-polygoni (`iisvesi`, −40 m, 137 km², sisältää Virmasveden; lahden osuus < 0,2 %).

**D1.** Ainakin yhden vuoden 2023–2025 NDCI ylittää perusjakson 2018–2021 suurimman arvon. *Ennuste:* toteutuu. *Kumoutuu, jos:* kaikki 2023–2025 ≤ max(2018–2021).

**D2.** Ero lahti − Iisvesi: vuosien 2023–2025 keskiarvo ylittää perusjakson 2018–2021 suurimman eron. *Ennuste:* toteutuu. *Kumoutuu, jos:* ei ylitä. D2 erottaa lahden oman kehityksen koko järven ja sään vaihtelusta, joten se on D1:tä vahvempi testi.

**D0 (kuvaileva).** Vuoden 2026 sijoitus jaksolla 2018–2026; Karttulanlahdelta ei ole kirjattua tietoa kesän 2026 kukinnasta, joten ennustetta ei anneta.

**Rajoitukset kirjattu etukäteen:** lahti on kapea (puskuroituna noin 150 m leveä), joten 20 m:n pikseleissä rannan vaikutus on suurempi kuin Kolvosessa; ennuste nojaa osin käyttäjän havaintoon, ei riippumattomaan lähteeseen.

**Tulos 30.10.2026 (lisätty, kirjausta ei muutettu):** D1 ja D2 kumoutuivat. Karttulanlahden NDCI: 2018 0,035 · 2019 0,023 · 2020 0,028 · 2021 0,024 · 2022 0,018 · 2023 0,011 · 2024 0,029 · 2025 0,014 · 2026 0,024.
- D1: perusjakson maksimi 0,035 (2018); yksikään vuosi 2023–2025 ei ylitä sitä.
- D2: ero Iisveteen 2023–2025 keskimäärin 0,022, perusjakson suurin ero 0,071 (2018).
- D0: 2026 sijalla 4/9.

Lahti on koko jakson ajan Iisvettä tuottavampi (ero 0,003–0,071), mutta nousua ei näy. Mahdollisia syitä, joita tämä mittari ei erota: kapean lahden rantasekoittuminen, touko–syyskuun mediaanin laimennus, tai havaittu muutos koskee muuta kuin kasviplanktonia (vesikasvillisuus, näkösyvyys, liettyminen). `tools/data/bem-e/karttulanlahti-tulos.json`.
