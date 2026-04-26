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
