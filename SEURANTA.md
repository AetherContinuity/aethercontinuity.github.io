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

## BEM-E — ennakkokirjaus C ennen Kolvosen aikasarjaa (30.10.2026)

Tausta: Yle 29.10.2026 — Kolvonen (Enonkoski/Savonlinna, järvinumero 04.297.1.001) peittyi heinäkuun lopulla 2026 sinileväkukintaan. LVV:n mukaan ravinnekuormitusta on ollut 5–6 vuotta; asukkaan mukaan muutos alkoi yli kymmenen vuotta sitten ja "toissa talvena vesi ei kirkastunut". Kysymys: näkyikö kehitys satelliitissa ennen romahdusta? NDCI-arvoja ei ole laskettu ennen tätä kirjausta.

**Menetelmä (kiinnitetty etukäteen).** Polygoni: Sentinel-2 SCL-vesiluokka (6) yhdeltä pilvettömältä touko–kesäkuun kuvalta ennen vuotta 2026, rannasta −40 m puskuroituna (sama käytäntö kuin Iisvesi). Mittari: aci-corine-proxy `/lake-timeseries?polygon=<GeoJSON>&indices=ndci,mndwi&startYear=2018&endYear=2026` — touko–syyskuun P10D-osavälien mediaani vuodelle, 20 m, harmonizeValues. Perusjakso 2018–2021.

**C0 (menetelmän toimivuus).** Vuoden 2026 NDCI on jakson 2018–2026 suurin. *Jos ei:* menetelmä ei havaitse tunnettua kukintaa, ja C1 jää tulkitsematta.

**C1 (varoitusmerkki).** Ainakin yhden vuoden 2023–2025 NDCI ylittää perusjakson 2018–2021 suurimman arvon. *Ennuste:* toteutuu. *Kumoutuu, jos:* kaikki vuodet 2023–2025 ≤ max(2018–2021).

**C2 (kuvaileva).** NDCI:n Spearmanin ρ vuoden kanssa 2018–2025 > 0. Ei merkitsevyysrajaa (n = 8).

**Rajoitukset kirjattu etukäteen:** touko–syyskuun mediaani laimentaa lyhyen loppukesän kukinnan; pienessä järvessä rantasekoittuminen 20 m:n pikseleillä; pintakukinta nostaa myös lähi-infrapunaa, joten NDCI voi käyttäytyä kukinnassa epälineaarisesti (C0 testaa tämän). Metsänkäyttöilmoitukset ja vedenkorkeus (SYKE-asema Paikka 2925) raportoidaan kuvailevina, ilman ennustetta.
