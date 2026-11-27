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

**Tulos 30.10.2026 (lisätty, kirjausta ei muutettu):** Kolvosen NDCI (touko–syyskuun P10D-mediaani, −40 m polygoni 1,19 km²): 2018 0,016 · 2019 −0,003 · 2020 0,028 · 2021 −0,011 · 2022 0,013 · 2023 0,041 · 2024 0,040 · 2025 0,029 · 2026 0,061.
- C0 piti: 2026 on jakson suurin.
- C1 piti: 2023 (0,041) ja 2024 (0,040) ylittävät perusjakson maksimin (0,028); 2025 vain niukasti (0,029).
- C2: ρ = 0,60 (2018–2025), kuvaileva.

Verrokit (lisätty jälkikäteen, ei ennakkokirjattu): Iisvesi ei näytä nousua 2022 jälkeen (2023–2026: 0,008, −0,004, −0,015, −0,031), joten Sentinel-2:n käsittelyversion vaihto 2022 ei selitä Kolvosen nousua. Lähijärvi 3 km lännessä (0,23 km²): 2023–2025 ei ylitä omaa perusjaksoaan, mutta 2026 on myös sen suurin (0,082) — vuoden 2026 kukinta oli osin alueellinen, varoitusmerkki 2023–2024 ei. Metsänkäyttöilmoitukset (järvi + 2 km): noin 150–310 ha/v 2010–2026 ilman nousevaa trendiä; LVV:n väite lisääntyneistä metsätaloustoimista ei näy ilmoituksissa tällä rajauksella. Vedenkorkeus: SYKE:n Kolvosen asemalla ei havaintoja 2015 jälkeen. `tools/data/bem-e-kolvonen.json`.
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

---

## BEM-E — ennakkokirjaus E: ennustaako NDCI vesienhoidon 4. kauden luokituksen heikkenemisen? (30.10.2026)

**Kysymys.** Erottaako Sentinel-2:n NDCI-muutos 2018–2023 ne järvet, joiden ekologisen tilan luokka heikkenee vesienhoidon 4. kaudella (2028–2033), niistä joiden ei? 4. kauden luokitus on keskeneräinen; tarkemmat tiedot julkaistaan Pohjois-Karjalan YTR:n muistion (25.5.2026) mukaan joulukuussa 2026 kuulemisen yhteydessä. Kukaan ei siis tiedä tulosta tätä kirjattaessa, eikä NDCI-arvoja ole laskettu.

**Järvijoukko (kiinnitetty, `tools/data/bem-e/vh4/vh4_jarvet.json`, sha256 bd95e32a3605503d; polygonit `vh4_polygonit.json`, 386d3589f4aeb0a8).** Lähde Syken WFS `jarvet_ekologinen_tila_2022` (3. kausi). Kelpoisuus: ELY POS, ESA, POK, KAS tai KES; pinta-ala 1–50 km²; ei voimakkaasti muutettu eikä keinotekoinen; luokitustaso vedenlaatuluokitus, suppea tai laaja ekologinen luokitus (ei pelkkä asiantuntija-arvio); luokka erinomainen–huono. Kelpoisia 760. Otos: kaikki 16 järveä, joiden luokka heikkeni 3. kaudella todellisen tilan muutoksen vuoksi, ja 240 muuta yksinkertaisella satunnaisotannalla (Python `random.Random(20261030).sample`, järjestys vpdtunnuksen mukaan) — yhteensä 256. Polygoni: Syken vesimuodostuma −40 m, URL-pituuden vuoksi lisäkutistus ja yksinkertaistus samalla toleranssilla (pysyy rajauksen sisällä; 216 järvellä 10 m, enintään 100+ m).

**Altiste.** `/lake-timeseries`, NDCI, touko–syyskuun P10D-mediaani vuosille 2018–2023. Δ = ka(2021–2023) − ka(2018–2020); vähintään kaksi kelvollista vuotta kummassakin puoliskossa, muuten järvi pois (kirjataan).

**Vaste (kun 4. kausi julkaistaan).** Y = 1, jos 4. kauden ekologinen tila on huonompi kuin 3. kauden (`ekoltila`) samalle vesimuodostumalle; yhdistys vpdtunnuksella, toissijaisesti nimi + kunta. Ensisijainen: mikä tahansa luokan heikkeneminen. Toissijainen: vain heikkenemiset, jotka Syke merkitsee todelliseksi tilan muutokseksi (jos 4. kauden aineisto erottelee sen).

**E1 (ensisijainen).** Δ:n AUC vasteelle Y on > 0,5, yksisuuntainen Mann–Whitney p < 0,05. *Ennuste:* toteutuu, AUC noin 0,6. *Kumoutuu, jos:* p ≥ 0,05.
**E2.** Δ:n ylimpään neljännekseen kuuluvissa järvissä heikkenemisosuus on suurempi kuin muissa, yksisuuntainen Fisher p < 0,05.
**Ennustelista.** Ylimmän neljänneksen järvet julkaistaan erillisenä committina NDCI-laskennan jälkeen ja ennen 4. kauden luokituksen julkaisua.

**Rajoitukset kirjattu etukäteen.** (1) 4. kaudella arviointiperusteet muuttuivat (Luke/Syke-raportti), joten osa luokkamuutoksista johtuu menetelmästä eikä järvestä — tämä heikentää kaikkia yhteyksiä nollaa kohti; toissijainen vaste rajaa tätä. (2) 4. kauden aineistojakso ei ole tiedossa; oletus 2018–2023. (3) Heikkenemisiä odotetaan vähän (3. kaudella todellisia 16/760 ≈ 2 %; kaikki heikkenemiset 32/760 ≈ 4 %), joten testin voima voi jäädä pieneksi — jos Y = 1 alle 8 järvellä, tulos raportoidaan kuvailevana. (4) Määräaika: jos 4. kauden luokitusta ei ole saatavilla 30.6.2027 mennessä, tila raportoidaan tuolloin.

### E — ennustelista julkaistu (30.10.2026, kirjausta ei muutettu)

NDCI laskettu kaikille 256 järvelle (`tools/data/bem-e/vh4/vh4_ndci_raw.json`; ensimmäisen ajon CDSE 429 -virheet ajettiin uudelleen, lopullisessa aineistossa ei puuttuvia vuosia). Pois jääneitä 0. Δ-mediaani +0,0065 (p25 −0,0023, max +0,0474). Ylimmän neljänneksen raja Δ ≥ 0,0149; listalla 64 järveä: `tools/data/bem-e/vh4/vh4_ennustelista.json`. Laskenta `scripts/bem_e_vh4_delta.py`, kaikki Δ:t `vh4_delta.json`. Kuvaileva huomio, ei testi: 3. kaudella heikentyneistä 16 järvestä 5 osuu ylimpään neljännekseen (odotus 4). Testi E1/E2 ajetaan, kun 4. kauden luokitus julkaistaan.

---

## Energiaintensiivinen kasvu ja julkinen talous — ennakkokirjaus G ennen inkrementaalista laskentaa (17.11.2026)

**Kysymys.** Kuinka paljon energiaintensiivinen kasvu (datakeskukset, vety ja e-polttoaineet, akkuteollisuus, teollisuuden sähköistyminen) parantaa julkisyhteisöjen rahoitusasemaa vuonna 2030 suhteessa VM:n perusuraan? SM-022 (datakeskusten rahavirrat) siirtyy tämän muistion datakeskusosioksi.

**Ei kyllä/ei-kynnystä.** Tulos raportoidaan osuutena vertailuerosta. Lukitaan mittatikku, ei johtopäätöstä.

**Lukitut säännöt.**
1. *Kohde:* inkrementaalinen nettovaikutus julkisyhteisöjen (S13: valtio, kunnat, hyvinvointialueet, sosiaaliturvarahastot) rahoitusasemaan vuonna 2030. Lasketaan skenaarion ja VM:n perusuran erotus. VM:n perusuraan jo sisältyvää toimintaa ei lasketa uudelleen.
2. *Tulot:* sähkövero, yhteisövero, palkkojen tuloverot sekä työnantaja- ja työntekijämaksut siltä osin kuin ne ovat S13:n tuloja. Työeläkemaksut raportoidaan omana rivinään, koska ne kasvattavat myös tulevia eläkevastuita.
3. *Palkkojen inkrementaalisuus:* palkkojen verot ja maksut lasketaan vain nettouudelle työllisyydelle. Osuus on oletus, joka esitetään herkkyytenä 0 / 50 / 100 %. Muilta toimialoilta siirtyvä työvoima ei tuo lisätuloa.
4. *Vähennykset:* suorat tuet, sähköveron verotuki (luokka II vs. luokka I) ja puhtaan siirtymän verohyvitykset. Ei kaksinkertaista vähentämistä: jos tulo lasketaan jo toteutuvalla verokohtelulla, samaa tukea ei vähennetä uudelleen.
5. *Vertailuero:* VM:n syksyn 2026 ennusteen vuoden 2030 alijäämän ja EU:n 3 %:n viitearvon erotus (ennusteessa 4,4 % → 1,4 %-yks.). Euroina lasketaan saman ennusteen vuoden 2030 nimellisestä BKT:sta. Erotus on laskennallinen vertailukohta, ei EDP:n korjausvelvoite (sitova ohjaus on nettomenopolku).
6. *Suorat ja välilliset erikseen:* toimipaikan suora vaikutus, hankintaketju erillisenä arviona ja rakennusvaihe erillisenä, ei summata vakiintuneeseen vuoteen.
7. *Raportointi:* M€/v, osuus vertailuerosta ja epävarmuusväli.
8. *Rajaus:* sähkön hintavaikutusta ei mallinneta; se mainitaan ehtona (kasvaako tuotanto kulutuksen tahdissa).

**Avoin ennen laskentaa (kirjataan tähän lisäyksenä ennen tuloksia):** skenaarioiden tarkka määrittely sektoreittain. Datakeskuksille vähintään VM/TEM 3,8 TWh (lähde ja vuosi tarkistettava, onko päivitetty syksyn 2026 ennusteeseen) ja SM-022:n 17,5 TWh. Muille sektoreille nimetyt hankkeet (puhtaan siirtymän verohyvityslista 12/2025, Fingridin liittymissopimukset).

**Jo nähty ennen kirjausta.** Toimialojen tasot 2022–2024 (Tilastokeskus 12bu, 15ad; Verohallinto verot_304; yrtt 13zn): arvonlisäys, palkat ja yhteisövero per sähkö-MWh, luokan II verotuki noin 756 M€/v [L], maksetut suorat tuet teollisuudelle 220–400 M€/v. Lisäksi Tuike Finland Oy:n tilinpäätösluvut. Nämä ovat tasotietoja, eivät inkrementaalisia tuloksia. Laskenta: `scripts/ekasvu_hae.py`, `scripts/ekasvu_toimialat.py`.

### G — lisäys 1: skenaariot (17.11.2026, ennen laskentaa)

**Kehys.** Fingridin teollisuuden ja datakeskusten sähkönkulutus (ennuste 9/2025): noin 38 TWh (2025) → 45 TWh (2030 kohtalainen kilpailukyky) / 63 TWh (2030 erinomainen). Lisäys +7 / +25 TWh. Arvojen kohdistus luettu kaavion tekstistä; tarkistetaan alkuperäisestä ennen laskentaa, ja mahdollinen korjaus kirjataan tähän.

**Skenaariot vuodelle 2030** (lisävaikutus lasketaan suhteessa S0:aan):
- S0 perusura: VM:n syksyn 2026 ennuste; datakeskukset 3,8 TWh (TEM:n energiatase).
- S1 kohtalainen: teollisuus + datakeskukset +7 TWh; datakeskukset 3,8 TWh; loput vety, e-polttoaineet ja materiaalit.
- S2 erinomainen: +25 TWh; datakeskukset 17,5 TWh (SM-022, 2,5 GW, 80 %); loput 7,5 TWh muut sektorit.

**Sektorijako** datakeskusten ulkopuolella: puhtaan siirtymän verohyvityksen saaneet 40 hanketta (Business Finland, päivitys 25.2.2026; 2 264 M€: P2X/uusiutuva 17 kpl 1 544 M€, varastot 18 kpl 311 M€, materiaalit 5 kpl 410 M€). Hankkeiden sähköteho (MW) haetaan YVA-asiakirjoista ja hankkeiden omista tiedoista; lähde kirjataan hankekohtaisesti. Hankkeet järjestetään toteutumisjärjestykseen (lopullinen investointipäätös > rakenteilla > lupavaihe), ja kunkin skenaarion TWh täytetään tässä järjestyksessä.

**Verohyvityksen vähennys 2030:** 10 % myönnetystä hyvityksestä niille hankkeille, jotka on täytetty skenaarioon (yläraja; edellyttää verotettavaa voittoa). Energiavarastot lasketaan kustannuseränä, mutta ei kulutuslisäyksenä.

**Kirjattu ristiriita:** omaan datakeskustaulukkoon "rakenteilla" kirjattu 4,1 GW vastaisi noin 29 TWh:ta, enemmän kuin S2:n koko lisäys. Raportoidaan tuloksena, ei soviteta.

### G — lisäys 2: muuntokertoimet ja täyttöjärjestys (17.11.2026, ennen laskentaa)

- Elektrolyysin käyttöaste 60 % [A], herkkyys 40 / 80 %. Vedyn sähkönkulutus 55 MWh/t H₂ [A].
- Hankkeen, jonka teho ei ole julkinen, kulutus johdetaan tuotemäärästä ja ilmoitetaan [L]-merkittynä.
- Täyttöjärjestys tilan mukaan (FID > rakenteilla > lupa/FEED > esiselvitys); saman tilan sisällä tavoitevuoden mukaan. Lopetettuja hankkeita (NordFuel) ei täytetä, eikä niiden hyvitystä vähennetä.
- Kuluttuaan kehykseen (S1 +7, S2 +25 TWh) täyttö loppuu; ylimenevä osa raportoidaan hankeputken ja kehyksen erona.
- Hanketaulukko: `tools/data/ekasvu/hankkeet-2026-11-17.md`.

### G — lisäys 3: tarkistukset ja lukitsematta jääneet laskentavalinnat (17.11.2026, ennen laskentaa)

**Tarkistukset (lisäys 1 edellytti):**
- Fingridin kaavion 2030-kohdistusta ei voitu tarkistaa alkuperäisestä: fingrid.fi on estetty työtilan verkosta, eikä tekstimuunnos erottele kaavion sarjoja. Ristiintarkistus: Fingridin kokonaiskulutusarvio 2030 on 106–123 TWh nykyisestä noin 88 TWh:sta (Taloustaito/Leskelä 2026), eli kokonaislisäys +18…+35 TWh, johon sisältyvät myös lämmitys ja liikenne. Kehys +7 / +25 TWh teollisuudelle ja datakeskuksille pidetään; epävarmuus raportoidaan.
- 3,8 TWh: lähde on TEM:n energiatase VM:n vuoden 2025 lausuntoaineistossa (tuki 83 M€ vuonna 2030 ↔ 3,8 TWh × 21,9 €/MWh). Päivitystä syksyn 2026 ennusteeseen ei löytynyt. Vertailuna: Energiateollisuuden Leskelä arvioi datakeskusten osuudeksi 10–15 % kulutuksesta 2030 (noin 11–18 TWh); Daily Finland 5–6 TWh. Raportoidaan rinnakkain, S0 pysyy 3,8:ssa.

**Laskentavalinnat, joita G ei vielä lukinnut:**
1. *S1:n muu kulutus* lasketaan samalla tavalla kuin lisäys 1 laski S2:n: kehys − datakeskusten taso = 7 − 3,8 = 3,2 TWh. (Tulkinta käyttää datakeskusten tasoa eikä lisäystä 2025→2030; vaihtoehtoinen tulkinta raportoidaan herkkyytenä.) Lisäys suhteessa S0:aan: S1 = datakeskukset 0 + muu 3,2 TWh; S2 = datakeskukset +13,7 + muu 7,5 TWh.
2. *Täyttöjärjestys lupa/FEED-luokassa tavoitevuoden mukaan:* Arctic Sisu (2028–) → Freija (2029, YVA VE1 160 MW ensimmäisenä vaiheena) → VolagHy (2030) → Koppö → Vetyalfa (VE1 500 MW) → Arctial. Esiselvitysvaiheen hankkeita ei tarvita, jos kehys täyttyy.
3. *Tuotemäärästä johdettu kulutus:* Arctic Sisu 56,1 kt H₂ × 55 MWh/t; VolagHy 50 kt eSAF × 0,5 t H₂/t eSAF [A] × 55 MWh/t.
4. *Sähkövero:* datakeskukset luokka I 22,4 €/MWh, P2X/teollisuus luokka II 0,5 €/MWh. Huoltovarmuusmaksu 0,85 €/MWh omana rivinä (Huoltovarmuusrahasto kuuluu valtionhallintoon). Luokan II verotukea ei vähennetä uudelleen (sääntö 4), mutta se raportoidaan menetettynä tulona.
5. *Yhteisövero:* datakeskukset SM-022:n kululisämalli (5 %, 1,16 M€/MW, 20 %). Uudet P2X-laitokset: väli 0 (ei verotettavaa voittoa käynnistysvuosina) … metallien jalostuksen taso 19 €/MWh (verot_304, 2022–2024), josta vähennetään verohyvitys 10 %/v enintään verosta.
6. *Työpaikat ja palkkojen verot:* datakeskukset 120 työpaikkaa/TWh (Tuike 2025, kulutus 1 TWh [A]); P2X 100 työpaikkaa/laitos [A] (VolagHy 100+, ETFuels 60 ilmoitettu). Työvoimakustannus 70 k€/v, josta S13:lle 40 % [A]. Nettouusi osuus 0/50/100 % (sääntö 3).
7. *Vertailuero:* BKT 2025 281,8 mrd € (Tilastokeskus 15a9) kasvatettuna VM:n reaalikasvuilla (2026 0,8 %, 2027–28 1,7 %, 2029–30 1,5 %) ja deflaattorilla 2 % [A]; erotus 1,4 %-yks. (alijäämä 4,4 % 2030).
8. *Lukitun ulkopuolella:* kiinteistövero (kuntien tulo) ei kuulunut sääntöön 2; raportoidaan erillisenä huomiona, ei summaan.

### G — tulos (17.11.2026, laskettu lisäysten 1–3 jälkeen, kirjausta ei muutettu)

Laskenta `scripts/ekasvu_g_laskenta.py`, tuloste `tools/data/ekasvu/g_tulos_2026-11-17.txt`. Vertailuero 2030: noin 4,7 mrd € (BKT noin 334 mrd € [L]).

| | Lisäys S0:aan | Nettovaikutus S13 | Osuus vertailuerosta | Väli (käyttöaste, nettouusi työ, P2X-yhteisövero) |
|---|---|---|---|---|
| S1 kohtalainen | muu +3,2 TWh (Arctic Sisu, osa Freijaa) | 52 M€ | 1,1 % | 4–52 M€ (0,1–1,1 %) |
| S2 erinomainen | DC +13,7, muu +7,5 TWh | 492 M€ | 10,5 % | 351–496 M€ (7,5–10,6 %) |

S2:sta 307 M€ (62 %) on datakeskusten sähköveroa luokassa I. P2X:n yhteisövero on yläraja (metallien jalostuksen taso miinus verohyvitys 10 %/v); alaraja 0. Luokan II menetetty sähkövero P2X-kulutukselta: S1 70 M€, S2 164 M€ (ei vähennetty, sääntö 4).

Herkkyydet: S1 vaihtoehtoisella tulkinnalla (muu 5,2 TWh) 74 M€ (1,6 %). Pelkät datakeskukset ET:n 11–18 TWh:lla: 204–401 M€ (4,4–8,6 %).

Lukitun ulkopuolella, ei summassa: kiinteistövero (kunnat).

---

## Seurattava muistioaihe: kotimaiset polttoaineet, vaihtotase ja verokohtelu (kirjattu 17.11.2026)

Kysymys: voiko kotimaisten polttoaineiden tuotanto ja käyttö kotimaan liikenteessä ja varavoimassa korvata fossiilisten tuontia niin, että vaihtotase ja kansantalous paranevat pitkällä aikavälillä, ja millä verokohtelulla tämä ei heikennä julkista taloutta?

Lähtötiedot: energiatuotteiden tuonti 10,0 mrd € ja vienti 5,6 mrd € (2025, Tilastokeskus); fossiilisten osuus sähköntuotannosta alle 2 %; energiaverot 3,8 mrd € (2025), uusiutuvien CO₂-vero puolitettu; ETS2 noin +20 snt/l 2027.

Mittarit: energian nettotuonti tuotteittain (ehk-taulukot proxyn kautta); polttoaineveron menetys korvattua litraa kohden; kustannusero €/MWh ETS2:n kanssa ja ilman; Suomeen jäävä osuus omistusmalleittain (ulkomainen, eläkeyhtiö, kunnallinen, osuuskunta); huoltovarmuusarvo omana eränä. Liittyy: TN-017, TN-018, ennakkokirjaus G.

Tehdään energiaintensiivisen kasvun muistion jälkeen; ennakkokirjaus ennen laskentaa.

### G — toteutusseloste (17.11.2026, laskennan ja katselmoinnin jälkeen; lukittuja lukuja ei muuteta)

Kimi K3.1 Pro katselmoi kirjauksen ja laskennan vastaavuuden (ogas3 `katselmoinnit/g-energiaintensiivinen-vastaus-2026-11-17.md`, PR #33). Löydökset tarkistettiin koodia vasten; kaikki pitivät. Tämä seloste tarkentaa tulkintaa, ei muuta tulosta.

**1. Pääluvut ovat ylärajoja.** Tulostaulukon 52 M€ (S1) ja 492 M€ (S2) on laskettu nettouusilla työpaikoilla 100 % ja P2X-yhteisöverolla metallien jalostuksen tasolla. G ei lukinnut raportoitavaa pistearvoa. Keskiarvio (nettouusi 50 %, P2X-yhteisövero 0) samalla koodilla: S1 6 M€ (0,1 %), S2 381 M€ (8,1 %). Väli 4–52 / 351–496 M€ on ehdollinen herkkyysväli kolmelle oletukselle, ei epävarmuusväli.

**2. Toteuttamatta jääneet kohdat:**
- *Energiavarastot kustannuksena (lisäys 1):* ei laskettu. Yläraja 10 % × 311,4 M€ = 31 M€/v, jos kaikki 18 varastoa ovat käytössä ja voitollisia 2030. Varastot eivät kuulu S1/S2-kulutuslisäykseen, joten erä raportoidaan erillisenä.
- *Työeläkemaksut omana rivinä (sääntö 2):* ei eritelty; 40 %:n S13-osuus sisältää ne erottelematta.
- *Suorat tuet:* ei vähennetty, koska hankekohtaisia S13-rahoitteisia tukia ei ole koottu. EU:n Innovaatiorahaston tuet (Koppö, Vetyalfa) eivät ole S13:n kustannus.
- *Hankintaketju ja rakennusvaihe (sääntö 6):* ei arvioitu.
- *Hankeputken ylitys (lisäys 2):* koodin "kehyksestä jäi" on täyttämättä jäänyt kehys, ei ylitys. Ylitys [L]: täyttöjärjestyksen nimetyt hankkeet yhteensä 16,0 TWh vs. S1 3,2 / S2 7,5 TWh → 12,8 / 8,5 TWh jää kehyksen ulkopuolelle; lisäksi esiselvitysvaiheen Plug Power (2,2 GW ≈ 11,6 TWh) ja ETFuels (≈ 1,6 TWh).
- *S0:n päällekkäisyys:* ei varmistettu, sisältääkö VM:n perusura jo osan hankkeista.
- *Ehto (sääntö 8):* tulos edellyttää, että kulutuksen lisäys toteutuu ja että tuotanto kasvaa sen tahdissa; hintavaikutusta ei mallinneta.

**3. Muut tarkennukset:**
- Osittain täytetyn hankkeen hyvitys ja työpaikat skaalattiin lineaarisesti kulutusosuudella (koodi rivi 28); valinta ei ollut lukittu.
- Verohyvityksen raja "enintään verosta" tehtiin yhteenlasketulle P2X-verolle; hankekohtaisesti tulos on sama tässä ajossa, koska jokaisen täytetyn hankkeen brutto ylittää 10 % sen hyvityksestä.
- Arctialin 1 000 työpaikkaa (rivi 20) on ilman lähdettä; ei vaikuta tuloksiin, koska Arctial ei täyty kumpaankaan skenaarioon.
- Vuoden 2030 BKT on johdettu reaalikasvuista ja 2 %:n deflaattorista, ei VM:n julkaistusta nimellisarvosta; vaikuttaa vain prosenttiosuuksiin.
- Vaihtoehtoisen S1-tulkinnan datakeskustaso 2,0 TWh (2025) on oletus [A] (vrt. 1,3 TWh 2024 TEM; 1,6 TWh 2024 Daily Finland).

**4. Seuraava laskenta tehdään uudella ennakkokirjauksella (H),** joka lukitsee ennen laskentaa: raportoitavan pistearvon oletukset; hankkeiden toteutumis- ja viivästymisskenaariot (ei automaattista korvaamista seuraavalla hankkeella); S0:n sisällön; hankekohtaiset tuet ja hyvitykset; jaon valtioon, kuntiin, hyvinvointialueisiin ja työeläkelaitoksiin; TyEL-rivin; kiinteistöveron, rakennusvaiheen ja hankintaketjun erilliset arviot.

---

## Energiaintensiivinen kasvu ja julkinen talous — ennakkokirjaus H, rinnakkaislaskenta hankkeen vaiheen mukaan (17.11.2026)

G pysyy muuttumattomana historiallisena kirjauksena. H on uusi laskentakierros G:n toteutusselosteen kohdan 4 pohjalta. Luonnosta kommentoivat ChatGPT ja Marko; Markon ratkaisu: **rinnakkaislaskenta, vaihtoehdot mukaan**.

**1. Kysymys ja nimitys.** Kuinka paljon energiaintensiivinen kasvu kasvattaa julkisyhteisöjen (S13) tuloja 2030 suhteessa VM:n perusuraan, kun hankkeet otetaan mukaan vain dokumentoidun vaiheensa mukaan? Tulos on **osittainen fiskaalinen vaikutus**, ei nettovaikutus: siitä puuttuvat sähkön hintavaikutus, syrjäytyminen ja verkkokustannukset. Matriisin solu yhdistää datakeskus- ja P2X-kulutuksen laskennallisesti; se ei väitä, että molemmat toteutuisivat ilman sähköjärjestelmän muita muutoksia.

**2. Datakeskusten taso 2030 (rinnakkaiset vaihtoehdot, ei todennäköisyysjakauma).** Lähteet luokitellaan alkuperän mukaan; samaa lukua toistavat lähteet ovat yksi taso.
- D0 3,8 TWh — TEM:n energiatase (VM:n verotuloarvion perusta), perusura.
- D1 5–6 TWh — Datakeskusten kansallinen tiekartta (VN:n selvityshenkilö); toistettu HE 282/2026:ssa ja FDCA:n tiedotteessa 4/2026. Daily Finland ei ole itsenäinen lähde.
- D2 11–18 TWh — Energiateollisuus (Leskelä, Taloustaito 2026: 10–15 % kulutuksesta). Attribuutio tarkistetaan lisäyksessä 1 (onko alkuperä Fingrid).
- D3 17,5 TWh — SM-022:n ACI-skenaario (2,5 GW × 80 %).
- D4 VTT/FDCA (julkistettu 28.10.2026): **otetaan mukaan vain, jos 2030-kulutusluku varmistetaan raportista lisäyksessä 1**. ChatGPT:n ilmoittamaa 13–23 TWh:ta (ja siinä Fingridille attribuoitua 9–18 TWh:ta) ei ole varmistettu. Lähteen luonne merkitään: toimialajärjestön tilaama.
Rekisterin 4,1 GW rakenteilla ei muunneta kulutukseksi; se raportoidaan hankeputken mittarina.

**3. Muut hankkeet vaiheen mukaan (kumulatiivisesti).**
- P0: lopullinen investointipäätös tai rakenteilla. 17.11.2026 ei yhtään P2X-hanketta — nolla tarkoittaa rajauksen tulosta, ei hankkeiden puuttumista.
- P1: + lupa/FEED, ilmoitettu käyttöönotto ≤ 2030 (nyt Arctic Sisu, Freija, VolagHy).
- P2: + esiselvitys, ilmoitettu käyttöönotto ≤ 2030 (nyt ETFuels, Plug Power site 1+2).
Ilman ilmoitettua käyttöönottovuotta tai käyttöönotto > 2030 (Koppö, Vetyalfa, Northern Green Fuels, Arctial, Sakatti): hankeputken seuranta, ei laskentaa. Ei automaattista korvaamista. Fingridin kehys (teollisuus + DC 2030 45–63 TWh; Fingrid Q3/2025: kokonaiskulutus 103–123 TWh) vain tarkistuksena.

**4. Käyttöönottovuoden ajoitus (rinnakkain).** Tarkka käyttöönottokuukausi käytetään, jos tiedossa. Muutoin käyttöönotto 2030 lasketaan rinnakkain 0 %, 50 % ja 100 % vuosikulutuksesta; ≤ 2029 täydellä vuosikulutuksella.

**5. Rinnakkaiset oletukset.** Kaikki yhdistelmät lasketaan ja raportoidaan:
- nettouusi työ 0 / 50 / 100 %;
- P2X-yhteisövero 0 / metallien jalostuksen taso 18,9 €/MWh, hyvitys vähennetään hankekohtaisesti enintään hankkeen verosta;
- elektrolyysin käyttöaste 40 / 60 / 80 %.
Muistion tiivistelmälauseessa käytetään keskiarviota (työ 50 %, P2X-yhteisövero 0, käyttöaste 60 %, ajoitus 50 %); kaikki muut yhdistelmät julkaistaan liitteenä.

**6. Hankekohtainen liite (lukitaan lisäyksessä 1 ennen laskentaa).** Vaihe, ilmoitettu käyttöönottovuosi/-kuukausi, sähkönkulutus 2030, liityntä- ja tuotantoriippuvuudet, verohyvitys, ilmoitetut pysyvät työpaikat, lähde ja lähteen päivämäärä. **Jäädytyspäivä**: lisäyksen 1 päivämäärä; sen jälkeiset hanketiedot eivät muuta H:ta.

**7. Alasektorit.** Valtio, kunnat, työeläkelaitokset (S13141, omana rivinä; kasvattavat myös eläkevastuuta, kuuluvat silti S13:n rahoitusasemaan ja siten vertailueroon), muut sosiaaliturvarahastot. Hyvinvointialueille ei jyvitetä tuloja (ei verotusoikeutta). Sähkövero ja huoltovarmuusmaksu valtiolle; yhteisövero verontilityslain 2026 jako-osuuksin; palkkojen verot ja maksut lisäyksessä 1 kirjattavin parametrein (Veronmaksajat/VM 2026).

**8. Erillisarviot, ei summaan.** Energiavarastot kolmena eränä (loppukäyttö ei kasva; verkkosähkön häviöt, jos läpivirtaus saatavilla; verohyvitys ≤ 31 M€/v). Datakeskusten kiinteistövero (rakennusosan arvo/MW ja kunnan veroprosentti; jos lähdettä ei löydy, ei arviota). Rakennusvaihe kertaluonteisena (kotimainen osuus Tilastokeskuksen panos-tuotostaulukoista tai kirjattu oletusväli). Hankintaketju tyypin I kertoimilla lähimmälle toimialalle.

**9. Vertailuero.** VM:n syksyn 2026 ennusteen 2030 nimellinen BKT, jos löytyy; muuten G:n johto merkittynä.

**10. Järjestys.** (1) tämä kirjaus; (2) lisäys 1: hankeliite, parametrit, D2:n attribuutio ja D4:n varmistus, jäädytyspäivä; (3) laskenta ja tulos erikseen; (4) Kimin katselmointi ennen muistiota.

### H — lisäys 1: lähteet, hankeliite ja parametrit (17.11.2026, ennen laskentaa). Jäädytyspäivä 17.11.2026.

**Datakeskusten tasot (harmonisoitu):**
- D0 3,8 TWh — TEM:n energiatase (VM:n perusura).
- D0b ~4 TWh — Statnett, pohjoismainen datakeskusennuste (Argus 26.3.2026). Siirtoverkkoyhtiön oma malli; Fingrid-riippuvuutta ei tiedetä. Lisätty, koska se on ainoa löydetty TSO-tason datakeskuskohtainen luku.
- D1 5 / 6 TWh — datakeskusten kansallinen tiekartta (HE 282/2026 toistaa; FDCA 4/2026 toistaa; Daily Finland ja Nordea eivät ole itsenäisiä tasoja). Molemmat päät lasketaan.
- D2 11 / 18 TWh — Energiateollisuus (Leskelä, Taloustaito 2026, 10–15 % kulutuksesta). Alkuperä (ET:n oma vai Fingridin) ei selvinnyt; attribuutio ET. Molemmat päät lasketaan.
- D3 17,5 TWh — SM-022 (ACI).
- D4 VTT/FDCA — **ei mukana**: 2030-kulutuslukua ei varmistettu raportista jäädytyspäivään mennessä. Saatavilla oleva kapasiteettiluku (FDCA, Poikola: jopa 2 800 MW 2030) raportoidaan hankeputken mittarina.
- ERAA 2025 / TYNDP: ei käytetä tasona; kansalliset kysyntäsyötteet ovat siirtoverkkoyhtiöiden (Suomessa Fingrid), eikä datakeskuserittelyä löytynyt. SvK KMA2025 käytetään vain Pohjoismaiden tasekontekstina, ei Suomen datakeskustasona.

**Hankeliite (P-tasot):**

| Hanke | Taso | Käyttöönotto (uusin lähde) | Kulutus 2030 (60 %) | Hyvitys M€ | Työpaikat | Lähde |
|---|---|---|---|---|---|---|
| Arctic Sisu, Kotka | P1 | 1. vaihe: 2028 (Cursor 6/2025) → mahdollisesti 2030 (Argus 8/2026); uusin lähde → 2030 | 1. vaihe = 1/3 × 56,1 kt H₂ × 55 MWh/t = 1,03 TWh [L/A: kolme samankokoista vaihetta] | 150,0 (1/3 kohdistuu 1. vaiheeseen [A]) | 100 [A] | Argus, Cursor |
| Freija, Nokia | P1 | ensituotanto 2029 (FID-tavoite 2026) | VE1 160 MW → 0,84 TWh | 110,6 | 100 [A] | LVV 2.4.2026, h2-view |
| VolagHy, Kuopio | P1 | käyttöönotto 2030 | 50 kt eSAF × 0,5 t H₂/t × 55 = 1,38 TWh [A] | 150,0 | 100 (ilmoitettu 100+) | Business Kuopio, chemXplore |
| ETFuels, Ranua | P2 | COD 2030 | 300 MW → 1,58 TWh | 118,6 | 60 (ilmoitettu) | carbonstorage.io, Kaleva |
| Plug Power site 1 + 2 | P2 | vuosikymmenen loppu (2023), FID-tavoite 2025/26 ei vahvistettu; → 2030 | sivustokohdistus tuntematon: teho johdetaan hyvityksestä: 2,55 M€/MW (5,6 mrd € / 2,2 GW), hyvitys = 20 % → site 1 87 MW, site 2 207 MW [L] → 1,55 TWh | 44,2 + 105,8 | 1 000 / 2,2 GW × 294 MW = 134 [L] | Plug Power 2023, Business Finland |

Kaikilla P1–P2-hankkeilla käyttöönotto 2030 paitsi Freija (2029) → ajoitus 0/50/100 % koskee Arctic Sisua, VolagHya, ETFuelsia ja Plugia. Hankeputki ilman laskentaa: Koppö (200 MW), Vetyalfa (500–1 000 MW), Northern Green Fuels, Arctial (~7 TWh), Sakatti, Norsk e-Fuel (80 kt), Arctic Sisu vaiheet 2–3.

**Datakeskusten työpaikat (rinnakkain):** 120 / TWh (Tuike Finland Oy, oma henkilöstö) ja 400 / TWh (Haminan kampus ml. urakoitsijat, Google/Yle) [kulutus 1 TWh A].

**Palkkaparametrit 2026:** vuosipalkka 60 000 € [A]. Työeläkelaitokset: TyEL 24,4 % (työnantaja keskim. 17,10 %, työntekijä 7,30 %; ETK 2026). Muut sosiaaliturvarahastot: työttömyysvakuutus 1,23 % + 0,89 %; sairausvakuutus työnantaja 1,91 % + palkansaajan päivärahamaksu 0,88 % (Varma 2026). Valtio: valtion tulovero ja yle-vero 12 % palkasta [A]; kunnat: kunnallisvero 7,0 % palkasta [A] (keskimääräinen kunnallisvero-% 7,57, efektiivinen alempi vähennysten vuoksi). Kirkollisvero ja sairaanhoitomaksu jätetään pois [A].

**Yhteisöveron jako 2026:** valtio 77,15 %, kunnat 22,85 % (laki 706/2024 muutettuna HE 59/2026 mukaisesti; 1.6.2026 voimaan tullut laki 394/2026).

**Erillisarviot:** rakennusvaiheen kotimainen osuus ja hankintaketju Tilastokeskuksen panos-tuotostaulukoista (StatFin/pt: 14yp tuonnin käyttötaulukko, 14yt Leontiefin käänteismatriisi, 14yr työpanoskertoimet; 2021–2023). Datakeskusten kiinteistöverolle ei löytynyt lähdettä rakennusosan arvosta per MW → ei arviota (H kohta 8). Varastojen läpivirtausta ei löytynyt → häviöt kuvataan sanallisesti.

**Vertailuero:** VM:n syksyn 2026 nimellistä 2030 BKT:ta ei löytynyt; käytetään G:n johtoa (≈ 334 mrd €, erotus 1,4 %-yks. ≈ 4,68 mrd €).

### H — tulos (17.11.2026, laskettu lisäyksen 1 jälkeen, kirjausta ei muutettu)

Laskenta `scripts/ekasvu_h_laskenta.py`, tuloste `tools/data/ekasvu/h_tulos_2026-11-17.txt`, solut JSON:na. Vertailuero ≈ 4 678 M€. **Osittainen fiskaalinen vaikutus**, ei nettovaikutus.

Pääarvo (ajoitus 50 %, nettouusi työ 50 %, P2X-yhteisövero 0, käyttöaste 60 %, DC 120 tp/TWh), M€ ja osuus vertailuerosta:

| | P0 (FID) | P1 (+lupa/FEED) | P2 (+esiselvitys) |
|---|---|---|---|
| D0 TEM 3,8 | 0 (0,0 %) | 6 (0,1 %) | 9 (0,2 %) |
| D0b Statnett 4 | 5 (0,1 %) | 11 (0,2 %) | 14 (0,3 %) |
| D1 tiekartta 5–6 | 32–59 (0,7–1,3 %) | 38–64 | 41–68 (0,9–1,4 %) |
| D2 ET 11–18 | 192–378 (4,1–8,1 %) | 197–384 | 201–388 (4,3–8,3 %) |
| D3 SM-022 17,5 | 365 (7,8 %) | 371 | 374 (8,0 %) |

Kaikkien yhdistelmien välit (ajoitus 0/50/100, nettouusi 0/50/100, P2X-yhteisövero 0/yläraja, käyttöaste 40/60/80, DC-työpaikat 120/400 per TWh): esim. D0 × P2 1–112 M€; D3 × P2 342–612 M€; täysi matriisi tulosteessa.

Havainnot:
- Hankevaihe (P0→P2) muuttaa pääarvoa enintään 9 M€; datakeskustaso (D0→D2b) 378 M€. Tulos määräytyy lähes kokonaan datakeskusten kulutuksesta ja niiden luokan I sähköverosta.
- P0 = 0: yhdelläkään P2X-hankkeella ei ole lopullista investointipäätöstä jäädytyspäivänä.
- P2X 3,6 TWh (P2) tuottaa pääarvolla alle 10 M€; luokan II menetetty sähkövero samalta kulutukselta 79 M€ (ei vähennetty, raportoitu).
- Alasektorit: lähes kaikki valtiolle (sähkövero). Esim. D2b × P2: valtio 360, kunnat 10, työeläkelaitokset 15, muut sosiaaliturvarahastot 3 M€.

Erillisarviot (ei summaan):
- Energiavarastot: verohyvitys ≤ 31 M€/v; häviöitä ei laskettu (läpivirtausta ei saatavilla).
- Rakennusvaihe, investointikysynnän tuontiosuudet 2023 (Tilastokeskus 14yp/14ym): tietokoneet ja elektroniikka (26) 92 %, koneet (28) 79 %, sähkölaitteet (27) 66 %, tekniset palvelut (71) 26 %, metallituotteet (25) 9 %, rakentaminen (41–43) ≈ 0 %. Kotimainen osuus investoinnista hankintarakenteen mukaan [A, laskentahetkellä]: datakeskus ilman palvelimia ~65 %, palvelimet mukana ~35 %; P2X ~52 %.
- Hankintaketju: Leontiefin käänteismatriisin sarakesummat 2022 (14yt): kemia (20) 1,37, metallien jalostus (24) 1,64, tietojenkäsittely (62–63) 1,46, rakentaminen 1,88. Euromääräistä arviota ei tehty, koska hankkeiden tuotosta ei tunneta.
- Kiinteistövero: ei arviota (lähdettä ei löytynyt).

### H — toteutusseloste (17.11.2026, laskennan ja katselmoinnin jälkeen; lukittuja lukuja ei muuteta)

Kimi K3.1 Pro katselmoi H:n (ogas3 `katselmoinnit/h-energiaintensiivinen-vastaus-2026-11-17.md`). Löydökset tarkistettiin koodia vasten; kaikki pitivät.

1. **Kaikki yhdistelmät julkaistu** (H §5 edellytti): `tools/data/ekasvu/h_yhdistelmat_2026-11-17.csv`, 2 268 riviä, alasektoreittain; `scripts/ekasvu_h_yhdistelmat.py` käyttää samaa laskentaa.
2. **Lukitsematta jääneet laskentasäännöt, jotka koodi toteuttaa:**
   - Verohyvityksen vuosikäyttö enintään 10 % myönnetystä (Business Finlandin ehto, G:n kartoitus) — ei kirjattu H:hon; vaikuttaa vain P2X-yhteisöveron ylärajaan, ei pääarvoon (yhteisövero 0).
   - Ajoituskerroin skaalaa kulutuksen lisäksi työpaikat ja hyvityksen; H §4 määräsi vain kulutuksen. Työpaikkojen skaalaus pienentää palkkatuloja.
   - Käyttöaste koskee vain MW-pohjaisia hankkeita (Freija, ETFuels, Plug); tuotemäärästä johdetut (Arctic Sisu, VolagHy) ovat kiinteitä.
   - Pääarvon DC-työpaikkaintensiteetti 120/TWh on funktion oletus; lisäys 1 esitti 120 ja 400 rinnakkain nimeämättä pääarvoa. 400 nostaisi pääarvoa kaikilla tasoilla D0:n yläpuolella.
3. **Lähdetasot:** D0b (~4 TWh) käsitellään 4,0:na; 0,2 TWh:n lisäys ja siitä seuraava ~5 M€ ovat pyöristysherkkiä eikä niitä tulkita itsenäiseksi vahvistukseksi. D2 11/18 TWh on johdettu 10–15 %:sta Fingridin kokonaiskulutuksella 106–123 TWh [L]; D2:n alkuperä on julkaisuattribuutio, ei osoitettu itsenäisyys.
4. **Tulkintarajat:** "tulos määräytyy datakeskusten kulutuksesta" pätee pääarvoon tasoilla D1–D3; D0–D0b:llä tulos tulee pääosin P2X:stä, ja D0 × P2 -välin (1–112 M€) määräävät P2X-oletukset. "Menetetty luokan II vero" (P2: 79 M€) on laskennallinen ero luokan I veroon, ei menetys VM:n perusuraan nähden.
5. **Erillisarviot:** rakennusvaiheen hankintapainot [A, laskentahetkellä]: datakeskus ilman palvelimia 41–43 45 %, 27 20 %, 28 25 %, 71 10 % → kotimainen ~65 %; palvelimet mukana 26 50 %, 41–43 20 %, 27 10 %, 28 15 %, 71 5 % → ~35 %; P2X 28 45 %, 27 15 %, 41–43 30 %, 71 10 % → ~52 %. Ei oletusväliä eikä euromäärää. Varastojen kolmijakoa ei eritelty tuloksessa.
6. **Seuraavaan kierrokseen (ennakkokirjaus ennen laskentaa):** DC-työintensiteetin pääarvo, veroparametrien lähteet numeroina, hyvityksen vuosikäyttö, työpaikkojen käynnistysprofiili, käyttöasteen kohdehankkeet, D0b:n kattavuus ja tarkka luku, D2:n alkuperä, Plugin sivustotehot suorista lähteistä, P2X:n perusura ja sähköveron vastafaktuaali.
7. **Muistion SM-023 v0.2 katselmointi (Kimi, 17.11.2026, `ogas3/katselmoinnit/sm023-vastaus-2026-11-17.md`).** Muistion päätaulukko ja alasektorit vastaavat H:n tulostetta. Tarkistettu löydös: hanketaulukon (`tools/data/ekasvu/hankkeet-2026-11-17.md`) rivi "Muut 6 uusiutuva + 3 materiaalia" on 274,4 M€, oikea summa Business Finlandin listasta on 321,7 M€ (uusiutuvat 212,0 + materiaalit 109,7); taulukon rivit summautuvat siksi 2 217,3 M€:oon, ei 2 264 M€:oon. Rivi on yhteenvetorivi, eikä H:n laskenta käytä sitä; jäädytettyä taulukkoa ei muuteta. Muistiossa korjattiin väitteiden rajaus (laskennan kattavuus, ei todennäköisyyksiä, kaikkien yhdistelmien yläraja 630 M€ = 13,5 %), Fingrid-kehyksen vertailukohta (muu kulutus 3,2–7,5 TWh), 1,5 GW / 5–6 TWh -tulkinta (yhteensopivat 38–46 %:n käyttöasteella) ja oletusmerkinnät. Avoimeksi jäi laskentajälki 71 M€:n verkkojyvitykselle, Tuike-palkoille ja rakennusvaiheen kotimaisuusosuuksille sekä P1-hankkeiden vaihenäyttö.

## DCA:n epäsymmetria ja Yhdysvaltain sitoutuminen Suomeen — ennakkokirjaus I (17.11.2026)

Kirjattu ennen indikaattoridatan hakua. Lähtökohta on Stubbin FT-haastattelu (17.11.2026: Euroopan Venäjä-yhteyksien ulkoistaminen Yhdysvalloille on "vastuutonta") ja Bildin raportti (13.11.2026) Venäjän vaatimuksesta Suomen Nato-erosta rauhanneuvotteluissa.

**1. Sopimusperusta (tarkistettu sanatarkasti 17.11.2026).** SopS 70/2024, Finlex avoin data `akn/fi/act/treaty/2024/70/fin@/media/8114.pdf` (aci-policy-proxy, PR #10); PDF ja sarake-erotellut tekstit `tools/data/dca/`, sha256 `78647198…a427e8e3`. Kirjauksen kannalta olennaiset määräykset:
- 3.1 ja 4.1–4.2: Yhdysvalloilla on oikeuksia ("authorized unimpeded access", "may … preposition", "unencumbered right to remove … at any time"). Yksikään "U.S. forces shall" / "United States shall" -lause ei velvoita läsnäoloon tai alueiden käyttöön.
- 3.4 ja 3.6: Suomi antaa sovitut alueet käyttöön ilman vuokraa ja pyrkii pyydettäessä helpottamaan pääsyä muihin satamiin, lentokenttiin ja teihin ilman kustannuksia Yhdysvalloille.
- 29.1: "All obligations under this Agreement shall be subject to the availability of appropriated funds." 29.5–6: riidat ratkaistaan neuvotellen, ei tuomioistuimessa eikä kolmannella osapuolella.
- 30.3: alkuvaihe 10 vuotta, sen jälkeen irtisanominen vuoden ilmoitusajalla. 30.4: liitettä A (15 aluetta) voivat muuttaa osapuolet tai toimeenpanijat kirjallisesti.
- Rakenne on Yhdysvaltain mallisopimus (PuVL 7/2024, UaVM 5/2024): sama Norjan, Ruotsin ja Tanskan sopimuksissa.

**2. Hypoteesi.** Sopimus sallii Yhdysvaltain sitoutumisen ohentamisen irtisanomatta, Suomi on sidottu vähintään 31.8.2034 asti. Jos Yhdysvallat käyttää tätä liikkumavaraa rauhanneuvottelujen aikana, sen pitäisi näkyä ensin Yhdysvaltain rahavirroissa (29.1) ja vasta sitten läsnäolossa. Hypoteesi ei väitä painostusta; se väittää, että ohentaminen olisi havaittavissa julkisesta datasta.

**3. Vertailuasetelma.** Lähtötaso Suomessa on matala, joten absoluuttinen väheneminen ei ole testattavissa. Vertailu tehdään samalla mallisopimuksella toimiviin maihin: Norja, Ruotsi, Tanska. Kuvaileva, ei kausaalinen: vertailumaiden kehitystä ei voi kohdistaa neuvotteluihin.

**4. Indikaattorit (vain vuositason kokonaissummat ja lukumäärät).**
- I1 Rakennushankkeet: C-1 (Construction Programs), maakohtainen summa, pyyntö ja hyväksytty, $K, FY2024→. Suomi, NO, SE, DK.
- I2 EDI: onko EDI budjetissa omana kokonaisuutenaan; maakohtainen summa, jos eritelty. Muuten vain Euroopan kokonaissumma.
- I3 Puolustusministeriön sopimusvelvoitteet, suorituspaikka maa (USAspending/FPDS), FY-summa, samat neljä maata.
- I4 Harjoitukset Suomessa Yhdysvaltain osallistumisella: kappalemäärä kalenterivuodessa Puolustusvoimien tiedotteista.
- I5 (konteksti, ei läsnäolo) DSCA:n asekauppailmoitukset Suomelle: lukumäärä ja $ — mittaa riippuvuutta, ei sitoutumista.

**5. Rajaus: kokoamisen vaikutus.** Ei kerätä eikä julkaista aluekohtaisia tietoja: ei hankkeiden sijainteja, ennakkovarastoinnin paikkoja, harjoitusten paikkoja tai ajoituksia, ei yksittäisiä joukkojen liikkeitä. Jos lähde antaa tiedon vain aluekohtaisesti, se summataan maatasolle ennen tallennusta eikä alkuperäistä riviä tallenneta. Testattava kysymys ("kasvaako Yhdysvaltain sitoutuminen Suomeen suhteessa vertailumaihin") ei vaadi sijaintitietoa.

**6. Lähtötaso ja mittausajat.** Lähtötaso FY2024–FY2026 (I1–I3, I5) ja 2024–2026 (I4). Mittaus vuosittain: seuraava, kun FY2028:n budjettipyyntö julkaistaan (kevät 2027) ja FY2027:n määrärahat on hyväksytty.

**7. Tulkinta lukitaan etukäteen (mittapuu, ei kynnys).**
- Ohentamisen kanssa yhteensopiva: Suomen I1+I3 laskee tai pysyy, kun vertailumaiden keskiarvo kasvaa, kahtena peräkkäisenä FY:nä; tai I4 laskee lähtötason alle.
- Ohentamisen kanssa ristiriitainen: Suomen I1+I3 kasvaa vähintään vertailumaiden tahtia, ja I4 pysyy lähtötasolla tai kasvaa.
- Muut yhdistelmät raportoidaan sellaisinaan ilman tulkintaa.
- EDI:n poistuminen (I2) koskee koko Eurooppaa; se raportoidaan erikseen, ei Suomen ohentamisena.

**8. Ei tehdä.** Ei väitetä painostusta eikä syy-yhteyttä neuvotteluihin. Ei mallinneta sotilaallista kykyä. Ei käytetä luokiteltua tai vuotanutta aineistoa.

**9. Jo nähty ennen kirjausta (ilmoitetaan).** C-1 FY2027:n maayhteenvedot luettu osittain hakutyökalulla: Suomea ei mainittu FY2025–FY2027-yhteenvedoissa, Norjalla ilmavoimien rakennushankkeita (FY2025 8 000 $K, FY2026 72 000 $K, lukema epävarma). Bloomberg (2023): Suomeen kohdistuneen sopimustyön arvo kymmenkertaistui FY2021→FY2022. FY2027 alkoi väliaikaisella rahoituspäätöksellä (CRS). Nämä tarkistetaan kokonaan lähtötasomittauksessa.

**10. Tekninen edellytys.** comptroller.war.gov ja api.usaspending.gov eivät ole työtilan sallittujen joukossa; haku proxyn kautta (uusi worker tai reitti), sama kertaluonteinen tallennus kuin muissa ACI-lähteissä.

### I — poikkeama 1 (17.11.2026, lähtötasohaun jälkeen, ennen I3:n osittelua ja ennen mitään tulkintaa)

**Mitä on jo nähty.** Lähtötasohaku (ogas3 `us-lahteet`, ajo 44151879753, `data/us/i_lahtotaso_2026-11-17.json`): I1:n maayhteenvetorivit ja I3:n kokonaissummat FY2019–FY2026 neljälle maalle. Haku tehtiin GitHub Actionsilla, koska Cloudflare-proxy sai DoD:lta 403 ja USAspendingilta 525 (kohta 10 toteutui eri reittiä).

**1. I3 ei mittaa läsnäoloa.** Suorituspaikka kertoo, missä maassa sopimus toteutetaan, ei Yhdysvaltain läsnäoloa. Kokonaissummaan sisältyvät Yhdysvaltain hankinnat maan puolustusteollisuudelta. I3 jaetaan USAspendingin tuote- ja palvelukoodin (PSC) ensimmäisen merkin mukaan:
- **I3a läsnäolo:** Y (rakentaminen), Z (kiinteistöjen huolto ja korjaus), X (tilojen vuokra), S (yhdyskuntapalvelut ja kiinteistönhoito), M (valtion tilojen käyttö).
- **I3b tavarat:** numeeriset PSC-koodit.
- **I3c muut palvelut:** muut kirjaimet (mm. J, R, V, A). Raportoidaan, ei tulkita.
Kohdan 7 tulkintasäännössä "I1+I3" korvataan "I1+I3a". I3b raportoidaan kontekstina kuten I5.

**2. Viive.** DoD:n sopimustiedot julkaistaan USAspendingissa noin 90 päivän viiveellä. Tilivuosi luetaan valmiiksi vasta seuraavan kalenterivuoden tammikuun jälkeen; FY2026 merkitään lähtötasossa keskeneräiseksi ja haetaan uudelleen 2/2027.

**3. I1:n sarakkeet ja kaksoislaskenta.** Sama maarivi toistuu C-1:ssä usean taulukon (määrärahatili, yhteenveto) alla. Sääntö: käytetään sitä saraketta, jonka taulukon otsikko on budjettipyyntö kyseiselle FY:lle (C-1:n otsikkorivi luetaan, kohderivejä ei); identtiset rivit samasta FY:stä lasketaan kerran. Jos otsikkoa ei voida yksiselitteisesti liittää riviin, raportoidaan rivit sellaisinaan ilman summaa.

**4. Kokoamisrajaus ennallaan.** PSC-osittelu tehdään maatasolla; PSC-kohtaisia rivejä ei tallenneta, vain kolme summaa (I3a, I3b, I3c) maata ja FY:tä kohden.

### I — lähtötaso, osa 1: I1 ja I3 (17.11.2026)

Aineisto: ogas3 `data/us/i_lahtotaso_2026-11-17.json` (ajot 44153127569 ja 44155030338). Vain maatason summat.

**I1 (C-1, $K).** Jokainen C-1 sisältää "Summary for FY" -taulukot edelliselle, kuluvalle ja pyyntövuodelle sarakkeilla Auth Amount / Amount (pyyntö) / Appn Amount / TOA Amount. Sama maarivi esiintyy kokonaistaulukossa ja määrärahatilin taulukossa (Air Force tai Navy); lasketaan kerran (poikkeama 1, kohta 3). Arvo = Appn Amount uusimmasta C-1:stä, jossa kyseinen FY esiintyy.

| FY | Suomi | Ruotsi | Norja | Tanska |
|---|---|---|---|---|
| 2023 | – | – | 8 200 | – |
| 2024 | – | – | 119 000 | – |
| 2025 | – | – | 8 000 | 106 200 |
| 2026 | – | – | 72 000 | – |
| 2027 (pyyntö) | – | – | – | – |

Rajoite: "Unspecified Locations" -rivi (FY2025: 1,53 mrd $) ei kohdistu maahan; sitä ei jyvitetä.

**I3 (USAspending, DoD-velvoitteet suorituspaikan mukaan, M$; I3a läsnäolo / I3b tavarat / I3c muut palvelut).** FY2026 keskeneräinen (poikkeama 1, kohta 2).

| Maa | FY2022 | FY2023 | FY2024 | FY2025 | FY2026* |
|---|---|---|---|---|---|
| Suomi | 1,0 / 14,0 / 7,8 | 0,2 / 3,0 / 8,1 | 0,1 / 0,9 / 6,9 | 0,4 / 1,5 / 2,2 | 0,0 / 0,0 / 5,3 |
| Ruotsi | 1,8 / 319,8 / 4,6 | 1,1 / 268,9 / 11,0 | 0,1 / 195,6 / 31,6 | 0,5 / 591,6 / 50,3 | 0,0 / 58,0 / 149,8 |
| Norja | 5,4 / 3,8 / 27,8 | 9,5 / 22,9 / 19,5 | 3,9 / 108,6 / 23,2 | 13,5 / 589,0 / 22,7 | 8,2 / 1 006,1 / 21,3 |
| Tanska | 1,9 / 9,2 / 2,5 | 1,3 / 3,2 / 2,5 | 0,8 / 12,3 / 3,2 | 0,6 / 3,6 / 54,3 | 0,0 / 0,7 / 0,1 |

Havainto ilman tulkintaa (kohta 7 vaatii kaksi peräkkäistä FY:tä mittausjakson ajalta): Suomella ja Ruotsilla ei ole Yhdysvaltain rakennushankkeita FY2023–FY2027; Norjalla ja Tanskalla on. I3a on kaikissa maissa pieni (≤ 13,5 M$/v), joten sen erottelukyky on heikko; läsnäolon kustannukset kulkevat pääosin henkilöstö- ja toimintamenoina, jotka eivät näy maakohtaisina sopimuksina.

### I — poikkeama 2 (17.11.2026, ennen I4:n laskentaa)

Kohta 4 määritteli I4:n lähteeksi "Puolustusvoimien tiedotteet" ilman aineiston rajausta tai koodaussääntöä. Kiinnitetään ennen laskentaa:
- **Aineisto:** Puolustusvoimien ja puolustusministeriön tiedotteet puolustusvoimat.fi:ssä ja valtioneuvosto.fi:ssä, julkaistu 1.1.2024–31.12.2026, haettu koneellisesti (GitHub Actions). Uutismedia ei kuulu aineistoon.
- **Yksikkö:** harjoitus nimellä (esim. "Cold Response 26"); sama harjoitus useassa tiedotteessa lasketaan kerran, vuosi = harjoituksen alkamisvuosi.
- **Ehto:** tiedotteen tekstin mukaan (1) harjoitus tai sen osa toteutetaan Suomen alueella ja (2) Yhdysvaltain asevoimat osallistuu. Pelkkä Naton tai "liittolaisten" maininta ei riitä. Kansalliskaarti (esim. Virginian kansalliskaarti) lasketaan.
- **Lisäksi** raportoidaan erikseen tiedotteet, jotka koskevat Yhdysvaltain läsnäoloa ilman nimettyä harjoitusta; ne eivät kuulu I4:n lukuun.
- **Validiteettirajoite:** I4 mittaa tiedotettua harjoitustoimintaa, ei läsnäolon kestoa tai vahvuutta. Tiedotuskäytännön muutos näkyy I4:ssä kuin toiminnan muutos.
- **Kokoamisrajaus:** paikkoja ja päivämääriä ei tallenneta; vain harjoituksen nimi ja vuosi.

### I — poikkeama 3 (17.11.2026, ennen I4:n laskentaa)

Poikkeama 2:n koneellinen haku ei onnistu: puolustusvoimat.fi, valtioneuvosto.fi ja defmin.fi torjuvat automaattisen haun (GitHub Actions 403; Cloudflare-bottitarkistus proxylle). Tarkistusta ei kierretä. I4 kootaan käsin verkkohaulla löytyvistä Puolustusvoimien ja puolustushallinnon tiedotteista sekä niitä sanatarkasti referoivista uutisista ("Puolustusvoimat kertoo tiedotteessa"). Koodaussääntö ja kokoamisrajaus ennallaan. Aineisto on epätäydellinen ja haun tuloksista riippuvainen: I4 on alaraja, ja vuosien välinen vertailu on suuntaa antava. Jo nähty ennen kirjausta: haun tulokset Cold Response 26, Karelian Sword 26, Rock Sisu / Sword 26 ja Protective Fence 26.

### I — lähtötaso, osa 2: I4 (17.11.2026, poikkeama 3:n mukaan, alaraja)

Harjoitukset Suomen alueella, joihin Yhdysvaltain asevoimat osallistuu tiedotteen tai sitä referoivan uutisen mukaan (vain nimi ja vuosi):
- 2024: Northern Forest 24; ALTAH Pohjoinen 24 → **2**
- 2025: Lively Sabre 25 → **1**
- 2026: Cold Response 26; Rock Sisu (Sword 26); Karelian Sword 26 (Virginian kansalliskaarti); Saber Strike 26, Suomen osuus → **4**

Ei laskettu (ehto ei täyty löydetyssä tekstissä): Nordic Response 24, Freezing Winds 25, Southern Griffin 25 ja Protective Fence 26 (Yhdysvaltain osallistumista ei mainittu); kolmenvälinen ilmavoimaharjoitus 2025 ja hävittäjien Lapin-harjoitus 5/2026 (nimi puuttuu löydetystä tekstistä). Läsnäolo ilman nimettyä harjoitusta, raportoidaan erikseen: Baltic Sentry -merijalkaväkiosasto (2/2025); merijalkaväen joukkueet ja kalustokoulutus (7/2025→).

Aineisto on haun tuloksista riippuvainen alaraja; vuosien välinen ero on suuntaa antava. Seuraava mittaus kaikille indikaattoreille: FY2028:n budjettipyyntö (kevät 2027) ja I3:n FY2026 uudelleenhaku 2/2027.

### I — poikkeama 4 (17.11.2026, lähtötason jälkeen, ennen ensimmäistä seurantamittausta)

Ulkoisen luennan (DeepSeek) jälkeen; ei muuta lähtötason lukuja.

1. **Tulkintarajaus.** I1 ja I3a mittaavat Yhdysvaltain upotettuja investointeja Suomeen, eivät sitoutumisen uskottavuutta kokonaisuutena. Kohdan 7 tulkinnat koskevat vain upotettuja investointeja; niistä ei päätellä puolustustahtoa eikä 5 artiklan uskottavuutta.
2. **Ennakkovarastointi on mittaamaton.** EDI:n "Enhanced Prepositioning" -rahoitusta ei kohdisteta maille, kalusto ei näy I1:ssä eikä luotettavasti I3:ssa, ja DCA 4.1:n ennakkoilmoitukset menevät Puolustusvoimille, eivät julkisuuteen. Vain Yhdysvaltain rahoittama varastoinfrastruktuuri näkyy I1:ssä. Julkisesti tiedotettu ennakkovarastointi Suomeen kirjataan erikseen laadullisena havaintona (vain tieto tapahtumasta ja vuosi, ei paikkaa eikä määrää, kohta 5).
3. **Joukkojen pysyvyys on mittaamaton.** I4 laskee harjoituksia, ei läsnäolon kestoa tai pysyvää sijoittamista. Tiedotettu pysyvä tai jatkuva Yhdysvaltain joukko-osasto Suomessa kirjataan samoin erikseen laadullisena havaintona.

## Idea: korpuksen väiterekisteri (kirjattu 27.11.2026, ei toteutettu)

Lähtökohta: SM-024:n kierros 26.–27.11.2026 osoitti, että yhden paperin korjaus (WP-020 Finding 3, CN-008:n "taloudellisesti kannattava") koskee väitteitä muissakin papereissa, ja ne löytyivät muistista eivätkä hausta.

Ehdotus: jokaisen paperin väitteet koneluettavaan rekisteriin (esim. `data/vaitteet.json`), yksi rivi väitettä kohden:

- paperi ja kohta (§), väitteen teksti
- merkintä `[M]` / `[L]` / `[A]` / `[—]`
- lähde ja hakupäivä
- tila: voimassa / rajattu / korjattu / kumottu, ja viittaus korjaukseen
- riippuvuudet: mitkä muiden papereiden väitteet nojaavat tähän

Käyttö:

- korjauksen jälkeen haku kertoo, mitkä muut väitteet on tarkistettava
- `[—]`-kohdat ajetaan määräajoin uudelleen (ogas3:n vahdin tapaan)
- ennakkokirjaukset (SM-024 T1, CN-030 M1/M2, AMOC A/B, BEM-E C–E, G) samaan rekisteriin tarkistuspäivineen. (Korjaus 27.11.2026: alkuperäisessä listassa oli "WEM F", jota ei ole olemassa; WEM:n ensimmäinen rekisteröinti on WEM-L1 alla.)

Valinnainen kenttä `countertest` (vasta-analyysi):

```yaml
countertest:
  condition: "Mikä havainto heikentäisi tai kumoaisi väitteen?"
  evidence_required: "Mistä ja millä menetelmällä havainto saataisiin?"
  status: not_specified | not_tested | tested
  note: "Mitä testi näytti, lähde ja päivä (vain kun status = tested)"
```

- Ei pakollinen. `[A]`-väitteille lähtökohtaisesti tarpeellinen; jos kunnollista ehtoa ei pystytä määrittelemään, kirjataan `not_specified` eikä keksitä falsifioijaa.
- `tested` tarkoittaa, että määritelty testi on suoritettu, ei että väite olisi vahvistettu. Tulos luetaan `note`-kentästä.
- Vastanäyttö ei ole kumoaminen: havainto voi heikentää väitettä kumoamatta sitä. Väitteen tilaa ei muuteta automaattisesti; muutoksen tekee ihminen ja kirjaa sen.
- Ei automaattista arviointilogiikkaa tässä vaiheessa.

Järjestys (27.11.2026): ensin tarkistuksen muisti (rekisteri), sitten määräaikainen seuranta (`[—]`-kohdat vahdilla), generatiivinen toiminta vasta niiden päälle. Muuten tuotantokyky kasvaa nopeammin kuin virheiden havaitsemiskyky.

Rajaus: rekisteri on työkalu, ei uusi paperisarja. Aloitus pienenä: SM-024, WP-020, CN-008, CN-030.

### SM-024 — ennakkokirjaus T1 (26.11.2026)

Suomenlahden talvimerenkulku, tarkistus 30.6.2027. Teksti ja kynnykset: `papers/sm-024-pohjoinen-solmu.html` § 06; mittauskoodi ja koosteet `AetherContinuity/ogas3`: `tools/talvimeri.py`, `data/talvimeri/`.

## Väiterekisteri — hyväksymistesti H1: WP-020 Finding 3 (ennakkokirjaus 27.11.2026)

Odotettu tulosjoukko kirjattu ennen rekisterin toteutusta. Joukkoa ei muuteta rekisterin löydösten perusteella; puutteet kirjataan uutena lisäyksenä päivämäärineen.

**Testattava väite (F3).** WP-020 § 06, Finding 3: "Neither pathway has stalled for technical or financial reasons. Both have stalled because no actor owns the integrated outcome."

**Korpuksen rajaus.** `AetherContinuity/aethercontinuity.github.io`, main @ `8ed6eb0` (27.11.2026). Hakemistot `papers/`, `supplements/`, `tools/`, `decisions/`, tiedostot `*.html` ja `*.md`. Pois: hakemistosivut (`index.html`, `papers-index.html`, `Oldindex.html`) ja `tools/ACI-INSTRUMENT-*`.

**Hakumenetelmä.**
1. Termihaku A (kirjainkoko ei ratkaise): `WP-020|CN-008|Perämer|Gulf of Bothnia|Laanila` → 9 tiedostoa.
2. Termihaku B (kirjainkoko ratkaisee): `Transfennica|RoRo|[Rr]o-ro|Haaparan|Haparanda|Oulun satam|Port of Oulu|maasilta|land bridge|länsikäytäv|länsireit` → 4 tiedostoa (WP-020, CN-008, CN-030, SM-024).
3. Jokaisen osuman konteksti luettu (±200 merkkiä); WP-019, SM-007 ja CN-030 § 8 luettu erikseen ylävirran ja rinnakkaisuuden tarkistamiseksi.
4. Hylätty termi: `Kemi` ilman rajausta (osuu sanoihin kemikaali, kemia).

Rajoite: haku löytää vain sanastoltaan samankaltaiset kohdat. Väite, joka nojaa F3:een eri sanoin ja ilman viittausta, voi puuttua joukosta.

**Suhdelajit.** H1 luokittelee suhteet neljään lajiin (H1:n vaatimus, ei vielä tietomallin täydellinen määrittely):

- `depends_on` — väite nojaa F3:een argumentissaan
- `same_claim` — sama väite toisessa paikassa tai toisin sanoin
- `qualifies` — väite rajaa tai tarkentaa F3:a
- `related` — sama aihe tai argumenttikokonaisuus, riippuvuutta ei ole osoitettu; ei saa nousta riippuvuudeksi

**Odotettu tulosjoukko.**

| # | Kohta | Väite | Suhde | Peruste |
|---|---|---|---|---|
| D1 | WP-020 § 06, Recommendations for state actors | "Assign coordination responsibility for the integrated Laanila–logistics hub development to a named entity" | `depends_on` F3 | Suositus johdetaan suoraan F3:sta |
| S1 | CN-008, tiivistelmä, 2. virke | "Pullonkaula on koordinaatio." | `same_claim` F3 | Sama väite tiivistettynä |
| S2 | CN-008, "Miksi tämä ei etene" | Transfennica-reitti "lakkautettiin kun koordinoiva tahto hävisi, ei teknisten tai taloudellisten syiden takia" | `same_claim` U2 | Sama historiallinen väite kuin WP-020:n historiaosiossa; F3:n premissi, ei siitä johdettu |
| X1 | CN-008, tiivistelmä, 1. virke | "Suljettu kiertotalousmalli on teknisesti valmis ja taloudellisesti kannattava." | `related` | Kannattavuusväite; lähempänä WP-020:n Finding 1:tä kuin F3:a |
| X2 | CN-008, "Mitä tarvitaan" | "Volyymi on olemassa jos toimijat koordinoivat." | `related` | Kysyntää koskeva ehtolause; samansuuntainen mekanismi, mutta ei osoitettu nojaavan F3:een |
| Q1 | SM-024 v0.2 § 02, "Mitä tämä tarkoittaa korpukselle" | F3:n taloudellinen peruste rautatie- ja maasiltalogistiikassa ei osoitettu | `qualifies` F3 | Rajaa F3:n soveltamisalaa |
| Q2 | WP-020 rajaushuomio ja CN-008 rajaushuomio (27.11.2026) | Sama rajaus | `qualifies` F3 (ja S1) | Rajaavat F3:a ja sen esiintymää CN-008:ssa |
| I1 | CN-030 § 8, "Kuka omistaa kokonaisuuden" | Länsireitin läpäisykyvylle ei ole mittaria, tavoitetta eikä omistajaa | `related` | Itsenäinen samansuuntainen havainto; peruste huoltovarmuuden tavoitepäätös (568/2024), ei F3 |
| I2 | WP-020 § 06, Finding 5 | Reittikohtainen peruste vahvistuu energiapolusta riippumatta | `related` | Eri väite samasta polusta; ei kumoudu, vaikka F3 kumoutuisi logistiikan osalta |

Huomio S2: `same_claim` koskee vain Transfennican lakkautuksen selitystä, ei koko CN-008:n koordinaatiodiagnoosia. Suhdeketju on `CN-008 S2 → same_claim → WP-020 U2 → premissi → WP-020 F3`. Rekisteri ei saa päätellä S2:n riippuvan suoraan F3:sta: S2 jakaa F3:n premissin, ei välttämättä samaa argumentointihistoriaa.

Huomio S1–S2: CN-008 (1.5.2026) ja WP-020 v0.1 (2.5.2026) ovat rinnakkaisia. Julkaisuaika ja keskinäiset viittaukset eivät ratkaise, kumpi on alkuperä; `same_claim` ei ota kantaa suuntaan.

**Ylävirta (F3:n premissit; testin pitää näyttää nämä ylävirtana).**

| # | Kohta | Väite |
|---|---|---|
| U1 | WP-020 § 01.1 | Laanila "technically ready, economically viable, institutionally stalled" (viittaa WP-019 § 3) |
| U2 | WP-020 § 01, Historical Context | Transfennican vetäytyminen "reflects the same coordination failure" |
| U3 | WP-020 § 03 | Kolmen vajeen diagnoosi (SM-009) logistiikka–energia-integraatiolle |
| U4 | WP-019, Oulu-polku; SM-009; CN-007 | Koordinaatiovaje elektrolyysi-investoinnin ja reservimarkkinasopimuksen välillä; kolmen vajeen malli |

**Poissuljetut osumat.** SM-021 (Perämeren LNG voimalan polttoaineena), WP-019:n Laanila-taulukot ja investointiluvut (energiapolun tila, ei F3:n väitettä; WP-019:n koordinaatiokohta on U4), TN-001 (CN-008 mainittu ruokobiomassan lähteenä), `ACI-STRUCTURE.md` (numerointi).

**Hyväksymiskriteerit rekisterin toteutukselle.**
1. Löytää D1 suhteella `depends_on`.
2. Tunnistaa S1 ja S2 suhteella `same_claim` (S2 suhteessa U2:een) eikä esitä niitä kahtena erillisenä väitteenä.
3. Näyttää U1–U4 ylävirtana eikä alavirtana.
4. Luokittelee Q1–Q2 suhteella `qualifies`.
5. Pitää X1–X2 ja I1–I2 suhteessa `related` eikä nosta niitä riippuvuuksiksi. Tämä on testin tiukin kohta: se mittaa, osaako rekisteri jättää yhdistämättä väitteet, joiden samankaltaisuus houkuttelee yhdistämään.
6. Ei esitä poissuljettuja osumia minkäänlaisina suhteina F3:een.
7. Näyttää jokaiselle löydökselle perusteen ja alkuperän (tiedosto, kohta, lainaus).

Kirjauksen teki Claude (Opus 5.5) haulla ja kontekstiluennalla; luokittelu on päätelmä, ei mittaus. Katselmoinnin (ChatGPT, 27.11.2026) jälkeen D2–D4 jaettiin suhdelajeihin S1, S2, X1 ja X2, ja R1 ja R3 merkittiin itsenäisiksi (`related`, I1–I2). Marko hyväksyi S1/X1-jaon ja S2:n ylävirtaluokituksen 27.11.2026.

## Väiterekisteri — hyväksymistesti H2: CN-030 "Miksi tätä ei ole laskettu" (ennakkokirjaus 27.11.2026)

Odotettu tulosjoukko kirjattu ennen täyttöä v2. Joukkoa ei muuteta täytön löydösten perusteella; puutteet kirjataan uutena lisäyksenä päivämäärineen. H1:tä ei muuteta.

**Mitä H2 mittaa.** H1 mittasi papereiden välisiä suhteita, ja täyttö 1 poimi lähinnä ristiviittauksia. H2 mittaa paperin sisäistä argumenttiketjua (aineistohavainto → välipäätelmä → johtopäätös) ja suhteen `perusta`-kentän käyttöä (ogas3 PR #48).

**Testattava väite (T).** CN-030 luku 10, kohta "Miksi tätä ei ole laskettu", 3. virke: "Poolausarvo ja kapasiteettiketjun pienin lenkki eivät kuulu yhdenkään tehtävään, koska ne syntyvät vasta, kun osat lasketaan yhdessä."

Huomio: kohdeväite valittiin Markon kollegalta saadun kuvauksen perusteella. Kuvaus oli parafraasi ("kumpikaan", "VR Transpoint"); sanatarkkaa muotoa ei ole korpuksessa. Lainaus yllä on korpuksesta, ja sen premissi nimeää kolme toimijaa.

**Korpuksen rajaus.** `AetherContinuity/aethercontinuity.github.io`, main @ `adb800b` (27.11.2026), sama kuin täytössä 1. Hakemistot ja poisrajaukset kuten H1:ssä. SM-024 on mukana (tiedosto korpuksessa, piilotettu hakemistosta).

**Hakumenetelmä.**
1. Termihaku A (kirjainkoko ratkaisee): `[Pp]oolausarvo|[Pp]oolattu|vaunupool|kapasiteettiketju|pienin lenkki|yhdenkään tehtävään|kenenkään tehtävä|pooling value` → 1 tiedosto (CN-030).
2. Termihaku B (kirjainkoko ei ratkaise): `kenenkään tehtäv|ei kuulu kenell|yhdenkään tehtäv|integrated outcome|owns the|kukaan ei laske|ei laske kukaan|kokonaiskapasiteet|ei omistajaa|syntyvät vasta|lasketaan yhdessä|poolau|pooli` → 23 tiedostoa. CN-030:n ulkopuolella osumat ovat muotoa "no actor/institution owns the …", sanaa `pooli` eri merkityksessä tai SM-015:n "ei kuulu kenellekään" / "ei omistajaa".
3. CN-030:n sisällä lisäksi `kapasiteettiketj|lenkki|laskematta|ei ole arvioitu|mittaamatta|kokonaisuu|työnjak`. Luvut 4, 8.2, 8 "Kuka omistaa kokonaisuuden", 9, 10 ja 12 luettu kokonaan; SM-024:n CN-030-viittaukset luettu.
4. Hylätty: `pooli` CN-030:n ulkopuolella (CN-003:n poolimenetelmä on koordinaatioryhmä, SM-005:n riskien poolaus eri käsite).

Rajoite kuten H1:ssä: haku löytää vain sanastoltaan samankaltaiset kohdat.

**Suhdelajit ja perusta.** H1:n neljä suhdelajia. Lisäksi `perusta` (ogas3 PR #48): `eksplisiittinen` = argumentti ilmaisee yhteyden yksiselitteisesti, suhdetta nimeävää sanaa ei vaadita; `rekonstruoitu` = yhteys on pääteltävä erillisistä kohdista tai välivaiheista.

**Ylävirta (T:n premissit).**

| # | Kohta | Väite | Suhde | Perusta | Peruste |
|---|---|---|---|---|---|
| U1 | CN-030 luku 10, sama kohta, 1.–2. virke | "Väylävirasto arvioi rajanylitystä, VR kotimaan yhdistettyä kuljetusta, Huoltovarmuuskeskus varastoja ja tonnistoa. Kukin tekee oman osansa." | T `depends_on` U1 | eksplisiittinen | Työnjakopremissi samassa kappaleessa |
| U2 | CN-030 luku 4.2 | "useampi virta tuottaa yhdessä kalustolle paremman käyttöprofiilin kuin erilliset järjestelmät"; ΔN = Σᵢ maxₜ Dᵢ(t) − maxₜ Σᵢ Dᵢ(t) | T `depends_on` U2 | rekonstruoitu | Määritelmä tekee poolausarvosta yhteislaskennan tuloksen; luku 10 ei viittaa lukuun 4.2 |
| U3 | CN-030 luku 8.2, "Kapasiteettiketjun lenkki" | "Käytävän arvo häiriössä on sen heikoimman lenkin välityskyky." | T `depends_on` U3 | rekonstruoitu | Pienin lenkki selviää vasta viiden lenkin vertailusta |

**Muut odotetut suhteet.**

| # | Kohta | Väite | Suhde | Peruste |
|---|---|---|---|---|
| Q1 | CN-030 luku 10, sama kohta, 4.–5. virke | "Tämä ei ole hankesuositus. Lopputulos voi olla 'ei kannata' yhtä hyvin kuin 'tässä on jotain'." | `qualifies` T | Rajaa T:n: laskematon arvo ei ole osoitettu arvo |
| P1 | CN-030 luku 12 (kaksi kohtaa) | "…mikä kasvattaa luvun 4 poolausarvoa [A]"; "Nootin oma lisä on poolausarvo: … [A]" | `depends_on` U2 (eksplisiittinen); ei suhdetta T:hen | Käyttää poolausarvon käsitettä, ei T:n selitystä |
| O1 | SM-024 v0.2 § 01 | "CN-030: länsikäytävän läpäisykyvylle ei ole mittaria, tavoitetta eikä omistajaa (§ 8)." | `same_claim` I1 | Nimetty viittaus |

**Rajatapaukset (useampi hyväksytty luokitus).**

| # | Kohta | Väite | Hyväksytty | Peruste |
|---|---|---|---|---|
| R1 | CN-030 luku 9 | "Kapasiteettiketjun viisi lukua (8.2). Ne ovat viranomaisten ja satamien julkista tai pyydettävissä olevaa tietoa." ja poolauskysymys | `related` tai rekonstruoitu `depends_on` T | Asetelma laskee juuri sen, mikä T:n mukaan jää laskematta, mutta kumpikaan ei perustele itseään toisella |
| U4 | CN-030 luku 4.1 | "Se ei vastaa kysymykseen, mitä uutta kysyntää monikäyttöinen kalusto voisi mahdollistaa. Jälkimmäistä ei ole arvioitu missään löydetyssä lähteessä." | T `depends_on` U4 (rekonstruoitu), `related` tai ei suhdetta | U4 koskee arvioimatonta lisäkysyntää, T poolausarvon ja pienimmän lenkin syntymistä yhteislaskennassa. T voi selittää U4:n havainnon tai olla siitä riippumaton johtopäätös; teksti ei ratkaise |
| S1 | CN-030 tiivistelmä | "Poolattu, monikäyttöinen kalusto on laskematta, ei kielteisesti testattu (luvut 4–6)." | `same_claim` U4, `related`, T `depends_on` S1 (rekonstruoitu) tai ei suhdetta; ei `same_claim` T:n kanssa | Laskemattomuus (S1) ja arvioimaton lisäkysyntä (U4) eivät ole automaattisesti sama väite. T:hen varmaa on vain se, etteivät S1 ja T ole sama väite: S1 toteaa laskemattomuuden, T selittää sen |
| I1 | CN-030 luku 8, "Kuka omistaa kokonaisuuden" | "Kun jokainen varautuu omaan tarpeeseensa, reitin kokonaiskapasiteettiin ei varaudu kukaan. … Länsireitin läpäisykyvylle ei ole mittaria, tavoitetta eikä omistajaa." | `related` tai rekonstruoitu `depends_on` T | Samansuuntainen kapasiteettipuolesta, mutta eri toimijat (yritykset ja valtio vs kolme viranomaista) ja eri kohde (varautuminen vs laskenta). Ei `same_claim`: T:ssä on poolauspuoli ja syyselitys |

**Houkutusjoukko.** Samankaltaisuus houkuttelee yhdistämään. `related` tai puuttuminen hyväksytään; `depends_on` tai `same_claim` T:hen ei.

| # | Kohta | Väite | Miksi ei riippuvuus |
|---|---|---|---|
| N1 | WP-020 § 06, Finding 3 | "Both have stalled because no actor owns the integrated outcome." | CN-030 viittaa WP-020:een, mutta T ei nojaa F3:een eikä toista sitä: F3 selittää hankkeen pysähtymisen, T laskennan puuttumisen |
| N2 | SM-007; CN-004 § 01 | "No one owns the complete picture." / "no actor owns the whole" | Korpuksen yleinen rakennehavainto; CN-030 ei viittaa |
| N3 | SM-009; SM-010 | "No actor owns the aggregate." / "no actor owns the aggregate exposure" | Sama |
| N4 | SM-015 | "Silmukka kulkee kaikkien näiden rajojen läpi — se ei kuulu kenellekään." | Lähin suomenkielinen sanamuoto; eri ilmiö (poliittinen takaisinkytkentä) |
| N5 | WP-013 | "They have not happened because no institution owns the compound problem." | Sama kuin N2 |

**Poissuljetut osumat.** CN-003 (poolimenetelmä), SM-005 (riskien poolaus), hakemistosivujen `pooli`-osumat, muut "owns the" -osumat (CN-025, SM-014, SM-003, SP-007, synthesis-memo-finland-2030, DA-007, TN-009, TN-012, TN-013).

**Hyväksymiskriteerit.** Kattavuus 1–5, tarkkuus 6–8, alkuperä 9; raportoidaan erikseen.
1. Löytää U1 suhteella T `depends_on`, perusta `eksplisiittinen`.
2. Löytää U2 ja U3 suhteella T `depends_on` ja näyttää ne T:n ylävirtana.
3. Perusta: U2 ja U3 eivät ole `eksplisiittinen` eikä U1 ole `rekonstruoitu`. Puuttuva perusta ei täytä kriteeriä.
4. Tunnistaa O1:n `same_claim`-suhteeksi I1:een.
5. Luokittelee Q1:n `qualifies` T ja liittää P1:n U2:een eikä T:hen.
6. Rajatapaukset R1, I1, U4 ja S1 taulukon hyväksyttyjen luokitusten mukaan. Eksplisiittinen `depends_on` ei täytä kriteeriä missään niistä; S1:n `same_claim` T:n kanssa ei täytä kriteeriä.
7. N1–N5 eivät ole `depends_on`- eikä `same_claim`-suhteessa T:hen. Testin tiukin kohta, kuten H1:n kriteeri 5.
8. Ei esitä poissuljettuja osumia minkäänlaisina suhteina T:hen.
9. Näyttää jokaiselle löydökselle perusteen ja alkuperän (tiedosto, kohta, lainaus).

**Vertailun ehdot.**
- CN-030 oli mukana täytössä 1. Vertailuraportti toteaa tämän ja ajaa H2:n myös täytön 1 raakatulosta vastaan lähtötasona; ero täyttöön v2 näyttää pyynnön muutoksen vaikutuksen.
- Täytön v2 pyynnön laatija ei näe H1:tä eikä H2:ta. Ensisijainen vertailu tehdään raakatulosta vastaan, kuten H1:ssä.
- Kirjauksen teki Claude (Opus 5.5) haulla ja kontekstiluennalla; luokittelu on päätelmä, ei mittaus. Kirjoittaja on nähnyt H1:n ja täytön 1 raakatuloksen, joten odotetun tuloksen muodostaminen on kontaminoitunut: H2 ei ole sokkona laadittu testi. Sokkous koskee vain täyttöä v2 (eri istunto). H2:n arvo on siinä, yleistyykö uusi poiminta toiseen kohteeseen.
- Katselmoinnin (ChatGPT, 27.11.2026) jälkeen U4 ja S1 siirrettiin pakollisista suhteista rajatapauksiksi ennen täyttöä v2. Tämän jälkeen H2:ta ei muuteta.

### H2 — lisäys 1: raportointi (27.11.2026, täytön v2 pyynnön lukemisen jälkeen, ennen raakatuloksen avaamista)

Täytön v2 pyyntö (ogas3 #49) ohjeistaa: "related ei ole riippuvuus. Älä käytä sitä riippuvuuden heikompana muotona … älä kirjaa depends_on-suhdetta äläkä korvaa sitä related-suhteella." Ohje juontuu luovutusviestistä, jonka tämän kirjauksen tekijä kirjoitti ("related ei ole riippuvuus"). Ohje todennäköisesti vähentää related-suhteita. Lisäksi pyyntö käskee kirjaamaan epävarman perustan rekonstruoiduksi.

Kirjaaja on nähnyt raakatuloksen yhteenvetotilastot (related 0, depends_on 18, joista rekonstruoituja 5) mutta ei esiintymiä eikä suhteita. Lisäys ei siis ole sokko related-suhteiden määrän osalta.

Kriteereitä ei muuteta. Raportointi tarkentuu kahdella tavalla:
- Kriteerissä 6 R1:n ja I1:n tulos jaetaan luokkiin "hyväksytty", "väärä luokitus" ja "puuttuu". Puuttuminen ei edelleenkään täytä kriteeriä, mutta se raportoidaan erikseen, koska pyyntö ohjasi pois related-suhteista.
- Kriteerissä 3 raportoidaan erikseen, johtuuko U1:n mahdollinen `rekonstruoitu` epävarmuussäännöstä (perustelu toteaa epävarmuuden) vai luokituksesta.

H1:n toteutus (`tools/vaiterekisteri_h1.py`) raportoi related-suhteen jo valmiiksi tietona eikä läpäisyehtona; sitä ei muuteta.

## WEM-L1 — fyysisten lopputulosten ennakkorekisteröinti (27.11.2026, ei ennuste)

WEM:n EPP-jäädytys (30.9.2026) edellyttää, että uusi yhdistelmäindeksi tehdään vain ennakkorekisteröitynä fyysistä lopputulosta vastaan. Tämä kirjaus lukitsee lopputulosmuuttujat. Se ei ole väite eikä ennuste, eikä sillä testata WEM:n ennustekykyä.

- Ikkuna: 1.10.2026–31.3.2027.
- Muuttujat ovat sisäkkäisiä, eikä niitä lasketa yhteen. Kaava ja kelpoisuussäännöt ovat samat kuin vertailutasossa.
  - RP_margin < 20 % (varttia)
  - RP_margin < 5 % (varttia)
  - RP_margin < 0 (varttia)
  - ylössäätöhinta ≥ 500 €/MWh (varttia)
- Vertailutaso: `tools/data/rp-margin-talvi-2025-2026.json` (lukittu 16.9.2026). Arvot 16 / 6 / 0 / 77, kelpaavia vartteja 17 470. Arvoja ei muuteta.
- Puuttuva vartti ei ole nollahavainto. Puuttuvat raportoidaan muuttujittain. Lähteiden määritelmämuutokset kirjataan poikkeamina.
- Pois rajattu: DS 336 ja tehoreservin aktivointi. Ne lisätään vain uutena rekisteröintinä ennen kuin niiden data on nähty.
- Ajoitus: ikkuna alkoi ennen kirjausta. Kirjaaja ei ole hakenut ikkunan dataa.
- Määrittely, koodi ja keruu: `AetherContinuity/ogas3` `data/wem-lopputulos/rekisterointi.json`, `tools/wem_lopputulos.py`, workflow `wem-lopputulos`. Tilat ovat MITATTU ja HAVAINTO_PUUTTUU.
