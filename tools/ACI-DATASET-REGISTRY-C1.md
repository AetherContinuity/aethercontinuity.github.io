# ACI Open Grid Instrument
## Vaihe C — Dataset Registry
### Sidottu Wireframe B-1:n tarpeisiin
**Versio:** C-1.0  
**Status:** Kanoninen sisäinen rekisteri — ei julkinen

---

## Käyttöperiaate

Tämä registry on rakennettu käyttöliittymästä käsin, ei "kaikki mahdollinen data talteen" -logiikalla.  
Jokainen datasarjalinkki on perusteltu sillä, mitä UI-elementtiä se palvelee.

Rakenne:

```
L0  Raw sources       — Fingrid API:n alkuperäiset sarjat
L1  Derived series    — L0:sta lasketut johdetut muuttujat
L2  Metric values     — Mittarikohtaiset laskenta-arvot per ikkuna
L3  Posture output    — Luokituslogiikan tulos + bannerin templating
L4  Display mapping   — UI-elementit ja niiden datalähteet
```

---

## L0 — Raw Sources (Fingrid Open Data)

### Ensisijaiset sarjat

| Sisäinen nimi | Fingrid kuvaus | Dataset ID | Yksikkö | Resoluutio | Päivitys |
|--------------|---------------|-----------|---------|-----------|---------|
| `raw_consumption` | Electricity consumption in Finland | 124 | MW | 1h (myös 3min) | ~15 min viiveellä |
| `raw_production_total` | Electricity production in Finland | 74 | MW | 1h | ~15 min viiveellä |
| `raw_net_import` | Net import of electricity to Finland | 194 | MW | 1h | ~15 min viiveellä |

> **Huom ID-varmennus:** Dataset-numerot 124 / 74 / 194 on tarkistettava Fingrid Open Data API:n
> ajankohtaisesta dokumentaatiosta ennen tuotantokäyttöä. API on muuttunut historiallisesti.
> Tarkistus: `https://data.fingrid.fi/open-data-forms/search/`

### Tarkistusidentiteetti (validointi)

```
validation_check(t) = |raw_consumption(t) − raw_production_total(t) − raw_net_import(t)|

Hyväksyttävä raja: < 50 MW (mittausepätarkkuus + ajastusero)
Jos yli 50 MW → loggaa, älä hylkää dataa automaattisesti
```

### Mitä L0 ei sisällä (tietoiset rajaukset)

| Jätetty pois | Perustelu |
|-------------|-----------|
| Tuotantolajikohtaiset sarjat (vesi, tuuli, ydinvoima…) | Ei tarvita A–E-mittareiden laskentaan; lisättävissä myöhemmin |
| Taajuusdata | Reservi-proxy ei kuulu B-1-wireframeen |
| Pohjoismaiset naapurimaat | L0-sarjoissa ei suoran vertailun tarvetta; tuonti näkyy `raw_net_import`:issa |
| Hintatiedot (ENTSO-E/NordPool) | TN-001/RRTC-konteksti, ei live-instrumentin ydin |

---

## L1 — Derived Series

Kaikki johdetut sarjat lasketaan L0:sta tuntikohtaisesti ennen ikkunalaskentaa.

### L1.1 — `domestic_coverage_instant`

```python
domestic_coverage_instant(t) = raw_production_total(t) / raw_consumption(t)
```

- Yksikkö: suhdeluku [0, ∞]
- Käyttö: DC-mittarin pohja, SP:n stressituntiehto

### L1.2 — `net_import_share_instant`

```python
net_import_share_instant(t) = max(raw_net_import(t), 0) / raw_consumption(t)
```

- Yksikkö: suhdeluku [0, 1]
- Huom: `max(..., 0)` rajaa netto-viennin pois — mittari kuvaa riippuvuutta, ei kapasiteettia
- Käyttö: NIR-mittarin pohja

### L1.3 — `demand_ratio_instant`

```python
demand_ratio_instant(t) = raw_consumption(t) / baseline_consumption(week_of_year(t))
```

- Yksikkö: suhdeluku, normaali ≈ 1.0
- `baseline_consumption(week)`: talvikausien 2018–2024 viikoittainen mediaanikulutus (MW/h)
  - Poikkeusviikot poistettu: COVID-kaudet 2020–2021
  - Tallennusmuoto: staattinen lookup-taulukko (52 viikkoa × mediaanikäyrä)
- Käyttö: DP-mittarin pohja, SP:n stressituntiehto

### L1.4 — `stress_hour_flag`

```python
STRESS_DP_THRESHOLD = 1.08   # kalibrointiparametri
STRESS_DC_THRESHOLD = 0.85   # kalibrointiparametri

stress_hour_flag(t) = 1  jos  demand_ratio_instant(t) > STRESS_DP_THRESHOLD
                              JA domestic_coverage_instant(t) < STRESS_DC_THRESHOLD
                       0  muuten
```

- Yksikkö: binääri {0, 1}
- Käyttö: SP-mittarin laskenta
- **Parametrimuutos vaikuttaa suoraan SP:n ja EPP:n arvoihin — dokumentoitava muutoshistoriassa**

---

## L2 — Metric Values (per ikkuna)

Ikkunat lasketaan kelluvan taaksepäin katsovan ikkunan yli:

```
W24  = viimeiset 24 tuntia  [t-23 : t]
W72  = viimeiset 72 tuntia  [t-71 : t]
W168 = viimeiset 168 tuntia [t-167 : t]
```

### Metric A — Demand Pressure (DP)

| Muuttuja | Kaava | Ikkuna |
|---------|-------|--------|
| `DP_24` | `mean(demand_ratio_instant, W24)` | W24 |
| `DP_72` | `mean(demand_ratio_instant, W72)` | W72 |
| `DP_168` | `mean(demand_ratio_instant, W168)` | W168 |

UI-tarve: `DP_72` pääkortti; `DP_168` EPP-laskentaan; `DP_24` W24-välilehti.

---

### Metric B — Domestic Coverage (DC)

| Muuttuja | Kaava | Ikkuna |
|---------|-------|--------|
| `DC_24` | `mean(domestic_coverage_instant, W24)` | W24 |
| `DC_72` | `mean(domestic_coverage_instant, W72)` | W72 |
| `DC_168` | `mean(domestic_coverage_instant, W168)` | W168 |

UI-tarve: `DC_72` pääkortti; `DC_168` EPP-laskentaan; `DC_24` W24-välilehti.

**Näyttömuoto:** prosentti (`DC_72 × 100` → "74%"), ei suhdeluku.

---

### Metric C — Net Import Reliance (NIR)

| Muuttuja | Kaava | Ikkuna |
|---------|-------|--------|
| `NIR_24` | `mean(net_import_share_instant, W24)` | W24 |
| `NIR_72` | `mean(net_import_share_instant, W72)` | W72 |
| `NIR_168` | `mean(net_import_share_instant, W168)` | W168 |

UI-tarve: `NIR_72` pääkortti; `NIR_168` EPP-laskentaan.

**Näyttömuoto:** prosentti (`NIR_72 × 100` → "24%").

**Rinnakkaisnäyttö:** raakaMW-arvo baselineksi kortissa:  
`NIR_MW_72 = mean(max(raw_net_import, 0), W72)` → "2 940 MW"

---

### Metric D — Stress Persistence (SP)

| Muuttuja | Kaava | Ikkuna |
|---------|-------|--------|
| `SP_24` | `sum(stress_hour_flag, W24) / 24` | W24 |
| `SP_72` | `sum(stress_hour_flag, W72) / 72` | W72 |
| `SP_168` | `sum(stress_hour_flag, W168) / 168` | W168 |

UI-tarve: `SP_168` pääkortti ja SP-baaridiagrammi; kaikki kolme SP-baarien rinnakkaisnäyttöön.

**Näyttömuoto:** prosentti (`SP_168 × 100` → "38%").

**Rinnakkaisnäyttö:** absoluuttinen tuntimäärä:  
`SP_count_168 = sum(stress_hour_flag, W168)` → "64/168 stressituntia"

---

### Metric E — Endurance Pressure Proxy (EPP)

```python
# Normalisaatioparametrit (threshold-rajojen perusteella)
DP_MIN, DP_MAX   = 1.00, 1.30   # norm-asteikko DP:lle
DC_MIN, DC_MAX   = 0.60, 0.95   # norm-asteikko (1-DC):lle käänteisesti
NIR_MIN, NIR_MAX = 0.00, 0.40   # norm-asteikko NIR:lle
SP_MIN, SP_MAX   = 0.00, 0.65   # norm-asteikko SP:lle

def norm(x, x_min, x_max):
    return max(0, min(1, (x - x_min) / (x_max - x_min)))

# Painot
W_DP  = 0.20
W_DC  = 0.30
W_NIR = 0.20
W_SP  = 0.30

# EPP W168
EPP_168 = (W_DP  * norm(DP_168, DP_MIN, DP_MAX)
         + W_DC  * norm(1 - DC_168, 1 - DC_MAX, 1 - DC_MIN)
         + W_NIR * norm(NIR_168, NIR_MIN, NIR_MAX)
         + W_SP  * norm(SP_168, SP_MIN, SP_MAX))

# EPP W72 (suuntamuutoksen havaitsemiseen)
EPP_72 = (W_DP  * norm(DP_72, DP_MIN, DP_MAX)
        + W_DC  * norm(1 - DC_72, 1 - DC_MAX, 1 - DC_MIN)
        + W_NIR * norm(NIR_72, NIR_MIN, NIR_MAX)
        + W_SP  * norm(SP_72, SP_MIN, SP_MAX))
```

UI-tarve: `EPP_168` posture-banneri ja pääkortti; `EPP_72` trendiviivakaavion toissijainen sarja; 30 päivän historiatrendikaavio käyttää `EPP_168(t)` päivittäin tallennettuna.

**Näyttömuoto:** kaksi desimaalia ("0.54").

---

## L3 — Posture Output

### Posture-luokitus

```python
def classify_posture(EPP_168, SP_168, DC_168, NIR_168):
    # Perustaso EPP:n mukaan
    if   EPP_168 < 0.20: posture = "NORMAL"
    elif EPP_168 < 0.40: posture = "TIGHT"
    elif EPP_168 < 0.65: posture = "ELEVATED"
    else:                posture = "BLACK-PERIOD-LIKE"

    # Override-säännöt (DA-001-henkinen suojaus)
    if SP_168  > 0.55: posture = max_posture(posture, "ELEVATED")
    if DC_168  < 0.65: posture = max_posture(posture, "ELEVATED")
    if NIR_168 > 0.33: posture = max_posture(posture, "ELEVATED")

    return posture

POSTURE_ORDER = ["NORMAL", "TIGHT", "ELEVATED", "BLACK-PERIOD-LIKE"]

def max_posture(a, b):
    return a if POSTURE_ORDER.index(a) >= POSTURE_ORDER.index(b) else b
```

### Komponenttikohtaiset badget (kortit)

```python
def component_badge(value, thresholds):
    # thresholds = [tight_low, elevated_low, bp_low]
    if   value >= thresholds[2]: return "BLACK-PERIOD-LIKE"
    elif value >= thresholds[1]: return "ELEVATED"
    elif value >= thresholds[0]: return "TIGHT"
    else:                        return "NORMAL"

# Esimerkki DP_72:lle (posture nousee threshold ylittyessä)
DP_badge   = component_badge(DP_72,    [1.05, 1.12, 1.22])
DC_badge   = component_badge(1-DC_72,  [0.10, 0.20, 0.30])  # käänteinen
NIR_badge  = component_badge(NIR_72,   [0.10, 0.20, 0.30])
SP_badge   = component_badge(SP_168,   [0.15, 0.30, 0.50])
EPP_badge  = component_badge(EPP_168,  [0.20, 0.40, 0.65])
```

---

### L3 — Posture Banner Template Logic

Bannerin tulkintalause muodostetaan kolmesta fragmentista:

```
Lause = [LEAD] + [DETAIL_1] + [DETAIL_2?] + [CLOSING]
```

#### LEAD — posture-tason mukainen avauslause (1 per taso)

| Posture | LEAD |
|---------|------|
| NORMAL | "Talvinen jatkuvuuspaine normaalirajoissa." |
| TIGHT | "Endurance-marginaalit ohenevat." |
| ELEVATED | "Useampi endurance-signaali koholla samanaikaisesti." |
| BLACK-PERIOD-LIKE | "Monipäiväinen endurance-paine selvästi koholla." |

#### DETAIL — komponenttien perusteella valittavat fragmentit (max 2)

| Ehto | Fragment |
|------|---------|
| `DC_72 < 0.80` ja `DC_persistence_days >= 1` | "Kotimainen peitto on pysynyt alle normaalin {DC_persistence_days} päivän ajan." |
| `DC_72 < 0.70` | "Kotimainen peitto heikko — järjestelmä nojaa merkittävästi tuontiin." |
| `NIR_72 > 0.20` ja `NIR_streak_days >= 2` | "Tuontiriippuvuus on noussut {NIR_streak_days}. peräkkäisenä päivänä." |
| `SP_168 > 0.30` | "Pitkittyvä stressijakso — {SP_count_168} stressituntia viimeiseltä 168 tunnilta." |
| `DP_72 > 1.12` | "Kysyntäpaine selvästi normaalia korkeammalla." |
| `EPP_72 > EPP_168 + 0.10` | "Paine kasvamassa — lyhyen aikavälin EPP noussut nopeasti." |
| `EPP_72 < EPP_168 - 0.10` | "Lyhyen aikavälin paine laskussa, mutta pitkä ikkuna pysyy koholla." |

Fragmenttien valintajärjestys: valitaan 1–2 eniten poikkeavaa komponenttia (suurin etäisyys normaaliin).

Lisäapumuuttujat fragmentteja varten:

```python
DC_persistence_days  = consecutive_days_below(DC_daily_avg, 0.80)
NIR_streak_days      = consecutive_days_above(NIR_daily_avg, 0.20)
```

#### CLOSING — kiinteä päätöslause (aina sama)

```
"Tämä on diagnostinen luokitus, ei operatiivinen hälytys."
```

---

## L4 — Display Mapping

Mitä data-arvoa kukin UI-elementti tarvitsee:

### Posture Banner

| UI-elementti | Tarvittu arvo |
|-------------|--------------|
| Posture-taso (teksti + väri) | `posture` (NORMAL / TIGHT / ELEVATED / BLACK-PERIOD-LIKE) |
| Tulkintalause | `banner_text` (L3 template output) |
| EPP-numero | `EPP_168` |
| EPP-sublabel | kiinteä: "W168 · synteettinen" |
| Posture scale (4 palkkia) | `posture` → korostetaan oikea palkki |

### Core Metric Cards (W72 oletusnäkymä)

| Kortti | Pääarvo | Subtext-arvo 1 | Subtext-arvo 2 | Badge |
|--------|---------|---------------|---------------|-------|
| A — DP | `DP_72` (×) | `baseline_consumption(viikko)` MW | `mean(raw_consumption, W72)` MW | `DP_badge` |
| B — DC | `DC_72` (%) | `mean(raw_production_total, W72)` MW | `mean(raw_consumption, W72)` MW | `DC_badge` |
| C — NIR | `NIR_72` (%) | `NIR_MW_72` MW | "{streak} peräkkäinen vrk" | `NIR_badge` |
| D — SP | `SP_168` (%) | `SP_count_168` / 168 tuntia | ikkunalabel "W168" | `SP_badge` |
| E — EPP | `EPP_168` | komponenttipainot (kiinteä teksti) | — | `EPP_badge` |

### Bar chart — DP fill

```
bar_fill_pct = norm(DP_72, 1.00, 1.30) × 100
```

### W24 välilehti (eri laskentaikkuna, ei zoom)

| Kortti | Arvo |
|--------|------|
| A — DP | `DP_24` |
| B — DC | `DC_24` |
| C — NIR | `NIR_24` |
| D — SP | `SP_24` (huom: W24:n SP on usein merkityksetön yksinään) |
| E — EPP | `EPP_72` (W72-pohjainen, koska W24-EPP on liian lyhyt) |

> **W24-välilehtihuomio:** SP_24 on niin lyhyt ikkuna, että siihen kannattaa lisätä UI-huomautus:  
> "Lyhyt ikkuna — katso W72 tai W168 pysyvyyden arviointiin."

### W168 välilehti

| Kortti | Arvo |
|--------|------|
| A — DP | `DP_168` |
| B — DC | `DC_168` |
| C — NIR | `NIR_168` |
| D — SP | `SP_168` |
| E — EPP | `EPP_168` |

### Aikasarjakaavio (pääkaavio, W72 oletusnäkymä)

| Sarja | Arvo | Väri |
|-------|------|------|
| Kulutus | `raw_consumption` tuntisarjana W72:lla | #c8a820 |
| Kotimainen tuotanto | `raw_production_total` tuntisarjana W72:lla | #3aaa6a |
| Import-gap (täyttö) | välialue tuotannon ja kulutuksen välillä kun `net_import > 0` | #d06020 (täyttö) |

### SP-baarit (oikea paneeli)

| Baari | Arvo |
|-------|------|
| W24 | `SP_24 × 100` % + `sum(stress_hour_flag, W24)` / 24 |
| W72 | `SP_72 × 100` % + `sum(stress_hour_flag, W72)` / 72 |
| W168 | `SP_168 × 100` % + `SP_count_168` / 168 |

### EPP 30 päivän trendikaavio

| Sarja | Arvo |
|-------|------|
| EPP_168 historiatrendinä | tallennettava päivittäin: `EPP_168(t_midnight)` |
| Historiaikkuna | 30 päivää (= 30 datapistettä) |
| Taustabändit | kiinteät threshold-rajat: 0.20 / 0.40 / 0.65 |

---

## Tallennussuositus

### Live-laskentatiheys

```
Haku Fingridistä:  1x / tunti (tai kun uusi tuntidata saatavilla)
L1-laskenta:       jokaisen haun jälkeen
L2-laskenta:       jokaisen haun jälkeen
L3-posture:        jokaisen haun jälkeen
```

### Historiakerros (minimivaatimus)

| Taso | Mitä tallennetaan | Rakeisuus | Säilytysaika |
|------|------------------|-----------|-------------|
| Raw | `raw_consumption`, `raw_production_total`, `raw_net_import` | 1h | 90 päivää |
| Derived | `stress_hour_flag`, `domestic_coverage_instant`, `demand_ratio_instant` | 1h | 90 päivää |
| Metrics | `DP_*`, `DC_*`, `NIR_*`, `SP_*`, `EPP_*` kaikissa ikkunoissa | 1h | 90 päivää |
| Posture | `posture`, `EPP_168` | 1 / vrk (midnightarvo) | 3 vuotta |
| Baseline | `baseline_consumption(week)` | 1 / viikko | staattinen |

> **Winter replay -mahdollisuus:** 90 päivän raw-historia riittää yhden täyden talvikauden jälkianalyysiin.

---

## Metric F — Allocation Pressure (rekisterissä, ei live-pinnassa)

AP ei kuulu live-laskentaan. Rekisteröidään kontekstuaalisena rakennemittarina:

| Tietotarve | Lähde | Päivitystiheys |
|-----------|-------|----------------|
| Talvinen kokonaiskulutus (BP-energiaintegraali) | L2: `sum(raw_consumption, W168)` talven huippuviikolla | 1 / talvikausi |
| Uuden jatkuvan kuorman arvio (MW) | Fingridin julkiset liityntäilmoitukset, julkiset DC-hankkeet | Manuaalinen, 1–2 x vuosi |
| L3-kapasiteetin endurance-arvio (MWh/168h) | Tekninen arvio (ei Fingrid-suoraan) | Manuaalinen, 1 x vuosi |
| AP_trend-laskelma | Kausikohtainen vertailulaskelma | 1 / talvikausi |

AP tallennetaan erilliseen `structure_context`-tauluun, ei live-metriikkaan.

---

## Julkinen vs. sisäinen kerros

| Data | Julkinen sivu | Sisäinen työkalu |
|------|--------------|-----------------|
| Fingrid dataset-numerot | **ei** | kyllä |
| Proxy-asetukset / API-avain | **ei** | kyllä |
| L1-raakasarjat (tuntitaso) | **ei** | kyllä (debug) |
| L2-metriikka-arvot | kyllä (näytetään kortissa) | kyllä |
| L3-posture + banneri | kyllä | kyllä |
| SP stressituntiehtoparametrit (1.08 / 0.85) | **ei** | kyllä |
| EPP-painotukset (0.20 / 0.30 / 0.20 / 0.30) | kyllä (method note) | kyllä |
| AP rakennemittari | kontekstuaalisesti myöhemmin | kyllä |

---

## Avoimet kohdat ennen toteutusta

| # | Kohta | Prioriteetti |
|---|-------|-------------|
| 1 | Fingrid dataset-ID:iden varmennus (124 / 74 / 194) | Korkea — tee ensin |
| 2 | Baseline-taulukon rakentaminen (talvikaudet 2018–2024) | Korkea — vaatii kertaluonteisen datalatauksen |
| 3 | `DC_persistence_days` ja `NIR_streak_days` -apumuuttujien laskentalogiikka | Keski — tarvitaan bannerin fragmentteihin |
| 4 | W24-välilehden SP-disclaimer UI-tasolla | Matala — muotoilukysymys |
| 5 | EPP 30 vrk historiatrendin tallennuksen aloitusajankohta | Matala — tallennus voidaan aloittaa heti |

---

## Versiohistoria

| Versio | Muutos |
|--------|--------|
| C-1.0 | Ensimmäinen rekisteri — sidottu Wireframe B-1:een |

---

*ACI Open Grid Instrument — Dataset Registry v C-1.0*  
*Tämä dokumentti on sisäinen tekninen rekisteri. Edeltävät vaiheet: A-1.0 (Metric Definition), B-1 (Observatory Wireframe).*
