# ACI Open Grid Instrument
## Vaihe A — Kanoninen mittarimäärittely
### Metric Names · Formulas · Windows · Thresholds · Posture Logic
**Versio:** A-1.0  
**Status:** Kanoninen runko — ei vielä julkinen

---

## Johdanto

Tämä dokumentti määrittelee täsmällisesti ACI Winter Endurance Monitor -instrumentin seitsemän ydintmittaria. Jokainen mittari on annettu muodossa:

- **Nimi ja rooli**
- **Kaava** (ensin konseptuaalisesti, sitten operationaalisesti)
- **Aika-ikkunat**
- **Threshold-rakenne** neljälle posture-tasolle
- **Tulkinnalliset rajaukset**

Mittarit on numeroitu A–G alkuperäisen instrumenttirungon mukaisesti. Mittarit A–E ovat live-laskettavia. Mittari F on rakenteellinen seurantamittari. Mittari G on tulkinnallinen kehysmuuttuja ilman numeerista live-arvoa.

---

## Yleiset laskentaperiaatteet

### Aika-ikkunat

| Ikkuna | Pituus | Käyttö |
|--------|--------|--------|
| W24 | viimeiset 24 tuntia | lyhyen aikavälin tila |
| W72 | viimeiset 72 tuntia | lähipäivien trendi |
| W168 | viimeiset 168 tuntia (7 vrk) | Black Period -analoginen ikkuna |

Kaikki ikkunat lasketaan kelluvan taaksepäin katsovan ikkunan yli, päätyen viimeisimpään täyteen tuntiin.

### Notaatio

```
t         = viimeisin täysi tunti (UTC)
w         = ikkunan pituus tunneissa (24 / 72 / 168)
X[t-w:t]  = muuttujan X arvot ikkunalla [t-w, t]
avg(X, w) = keskiarvo ikkunalla w
sum(X, w) = summa ikkunalla w
```

### Datalähde (Layer 0)

Kaikki live-mittarit lasketaan Fingrid Open Data -rajapinnan datasta.  
Ydinmuuttujat:

| Muuttuja | Fingrid dataset | Yksikkö |
|----------|----------------|---------|
| `consumption` | kulutus (total) | MW (hourly) |
| `domestic_production` | tuotanto (total) | MW (hourly) |
| `net_import` | netto-tuonti | MW (hourly, positiivinen = tuonti) |

Johdettu tarkistusidentiteetti (validointiin):  
`net_import ≈ consumption − domestic_production`

---

## Core Metric A — Demand Pressure (DP)

### Rooli

Mittaa, kuinka paljon kulutus poikkeaa kauden tilastollisesta normaalitasosta. Pitkittyvä korkea kulutus on Black Period -logiikan peruslähtö.

### Kaava

**Konseptuaalinen:**
> Demand Pressure = Toteutunut kulutus / Kauden normaali kulutus

**Operationaalinen:**

```
DP(t, w) = avg(consumption, t-w:t) / baseline_consumption(week_of_year(t))
```

Missä `baseline_consumption(week)` on kyseisen kalenteriviikon historiallinen mediaanikulutus (MW/h).  
Laskentaikkuna baselinelle: vähintään 3 viime vuoden vastaavat viikot, poislukien poikkeusviikot (COVID 2020–2021).

**Tulos:** dimensioton suhdeluku. Arvo 1.0 = täsmälleen normaali; >1 = yli normaali.

### Aika-ikkunat

| Ikkuna | Muuttuja |
|--------|----------|
| W24 | DP_24 |
| W72 | DP_72 |
| W168 | DP_168 |

Raportoitava pääarvo: **DP_72** (tasapainottaa hetken ja pysyvyyden).

### Threshold-rakenne

| Posture | DP_72 |
|---------|-------|
| Normal | < 1.05 |
| Tight | 1.05 – 1.12 |
| Elevated | 1.12 – 1.22 |
| Black-Period-like | > 1.22 |

*Thresholdit kalibroidaan talvikausien 2018–2024 pohjalta. Tarkistusväli: vuosittain.*

### Rajoitukset

- DP ei erottele kuormatyyppiä (lämpö vs. jatkuva teollinen vs. uusi DC-kuorma).
- Poikkeuksellisen lauha talvi voi pitää DP matalana myös tiukassa järjestelmässä.
- DP yksin ei riitä posture-luokitukseen; vaatii DP_168 persistenssin.

---

## Core Metric B — Domestic Coverage (DC)

### Rooli

Mittaa, kuinka suuri osa kokonaiskysynnästä katetaan kotimaisella tuotannolla. Matala kotimainen peitto pitkittyvässä talvijaksossa kasvattaa ulkoista tai varantoriippuvuutta.

### Kaava

**Konseptuaalinen:**
> Domestic Coverage = Kotimainen tuotanto / Kokonaiskulutus

**Operationaalinen:**

```
DC(t, w) = avg(domestic_production, t-w:t) / avg(consumption, t-w:t)
```

**Tulos:** prosenttiosuus tai suhdeluku [0, 1+].  
Arvo yli 1.0 tarkoittaa netto-vientiä (kotimainen tuotanto ylittää kulutuksen).

### Aika-ikkunat

| Ikkuna | Muuttuja |
|--------|----------|
| W24 | DC_24 |
| W72 | DC_72 |
| W168 | DC_168 |

Raportoitava pääarvo: **DC_72** ja **DC_168** rinnakkain.

### Threshold-rakenne

| Posture | DC_72 | DC_168 |
|---------|-------|--------|
| Normal | > 0.90 | > 0.88 |
| Tight | 0.80 – 0.90 | 0.78 – 0.88 |
| Elevated | 0.70 – 0.80 | 0.68 – 0.78 |
| Black-Period-like | < 0.70 | < 0.68 |

*DC_168-threshold on lievästi matalampi kuin DC_72, koska 7 vrk kattavuus sallii enemmän lyhytaikaista varianssia.*

### Rajoitukset

- DC ei erota, onko kotimainen tuotanto dispatchable vai säästä riippuvaa.
- Korkea DC voi nojata vesivoimaan, jonka energia ei välttämättä ole vapaasti käytettävissä.

---

## Core Metric C — Net Import Reliance (NIR)

### Rooli

Mittaa, kuinka suuren osan taseesta järjestelmä kattaa netto-tuonnilla. Hetkellinen tuonti ei yksin ole ongelma — monipäiväinen systemaattinen tuontiriippuvuus on kiinnostava signaali.

### Kaava

**Konseptuaalinen:**
> Net Import Reliance = Netto-tuonti / Kokonaiskulutus

**Operationaalinen:**

```
NIR(t, w) = avg(max(net_import, 0), t-w:t) / avg(consumption, t-w:t)
```

*Huom: max(net_import, 0) rajaa netto-viennin nollaan — mittari kuvaa riippuvuutta, ei vientikapasiteettia.*

**Tulos:** suhdeluku [0, 1]. Arvo 0.20 tarkoittaa, että 20 % kulutuksesta katetaan tuonnilla.

### Aika-ikkunat

| Ikkuna | Muuttuja |
|--------|----------|
| W24 | NIR_24 |
| W72 | NIR_72 |
| W168 | NIR_168 |

Raportoitava pääarvo: **NIR_72** ja **NIR_168**.

### Threshold-rakenne

| Posture | NIR_72 | NIR_168 |
|---------|--------|---------|
| Normal | < 0.10 | < 0.10 |
| Tight | 0.10 – 0.20 | 0.10 – 0.18 |
| Elevated | 0.20 – 0.30 | 0.18 – 0.27 |
| Black-Period-like | > 0.30 | > 0.27 |

### Rajoitukset

- NIR kuvaa historiallista toteumaa, ei rajasiirtokapasiteetin käytettävissä olevaa reserviä.
- Korkea NIR samanaikaisesti korkean DP:n ja alhaisen DC:n kanssa on vahvempi signaali kuin NIR yksinään.

---

## Core Metric D — Stress Persistence (SP)

### Rooli

Mittaa, kuinka pitkään järjestelmä on samanaikaisesti sekä korkeakuormaisessa että heikosti katetun tilassa. DA-003:n ja WP-001:n kannalta kesto on olennaisempi kuin yksittäinen tunti.

### Kaava

**Konseptuaalinen:**
> Stress Persistence = Osuus ikkunan tunneista, joilla sekä kysyntäpaine että kotimainen peitto ovat stressivyöhykkeessä

**Operationaalinen:**

```
stress_hour(h) = 1  jos  DP_instant(h) > 1.08  JA  DC_instant(h) < 0.85
                 0  muuten

SP(t, w) = sum(stress_hour, t-w:t) / w
```

Missä `DP_instant(h)` ja `DC_instant(h)` ovat yksittäisen tunnin hetkelliset arvot (ei ikkunakeskiarvoja).

**Tulos:** osuus [0, 1]. Arvo 0.40 tarkoittaa, että 40 % ikkunan tunneista on stressituntiehdon täyttäviä.

### Aika-ikkunat

| Ikkuna | Muuttuja |
|--------|----------|
| W72 | SP_72 |
| W168 | SP_168 |

*SP_24 lasketaan mutta sen merkitys on vähäinen; yksittäinen stressipäivä ei ole instrumentin ydinkysymys.*

Raportoitava pääarvo: **SP_168** (Black Period -analoginen ikkuna).

### Threshold-rakenne

| Posture | SP_168 |
|---------|--------|
| Normal | < 0.15 |
| Tight | 0.15 – 0.30 |
| Elevated | 0.30 – 0.50 |
| Black-Period-like | > 0.50 |

### Rajoitukset

- SP on binääriehtoihin perustuva mittari — threshold-valinta vaikuttaa tulokseen.
- Stressitunnin ehtoparametrit (1.08 / 0.85) ovat instrumentin kalibrointiparametreja, joita voidaan säätää.

---

## Core Metric E — Endurance Pressure Proxy (EPP)

### Rooli

Instrumentin tärkein synteettinen mittari. Yhdistää A–D:n tulokset yhdeksi diagnostiseksi arvoksi, joka kuvaa kokonaispaineena: järjestelmä voi olla hetkellisesti tasapainossa mutta samalla ajallisesti kiristyvä.

### Kaava

**Konseptuaalinen:**
> EPP yhdistää pitkittyvän kysynnän, heikon kotimaisen peiton ja jatkuvan tuontiriippuvuuden paineeksi

**Operationaalinen:**

```
EPP(t) = w_DP  * norm(DP_168)
        + w_DC  * norm(1 − DC_168)
        + w_NIR * norm(NIR_168)
        + w_SP  * norm(SP_168)
```

Missä:
- `norm(x)` = lineaarinen normalisaatio välille [0, 1] threshold-taulukon ääriarvojen mukaan
- Painot (oletusarvot): `w_DP = 0.20`, `w_DC = 0.30`, `w_NIR = 0.20`, `w_SP = 0.30`

**Tulos:** arvo välillä [0, 1]. Korkeampi arvo = suurempi endurance-paine.

### Painotusperustelu

| Komponentti | Paino | Perustelu |
|-------------|-------|-----------|
| DP_168 | 0.20 | Kysyntäpaine on välttämätön konteksti, ei yksin ratkaiseva |
| 1 − DC_168 | 0.30 | Kotimaisen peiton heikkous on suorin endurance-signaali |
| NIR_168 | 0.20 | Tuontiriippuvuus on rakenteellinen riski, ei itsenäinen kriisimerkki |
| SP_168 | 0.30 | Pysyvyys on mittarin ydinkysymys; kesto vie eniten painoa |

*Painot ovat instrumentin parametreja — ne voidaan kalibroida talvikausien validointiajolla.*

### Aika-ikkuna

EPP lasketaan aina **W168-pohjaisista komponenteista**. Lisäksi raportoitaan EPP_72 (W72-pohjaisista komponenteista) nopeamman suuntamuutoksen havaitsemiseksi.

### Threshold-rakenne

| Posture | EPP |
|---------|-----|
| Normal | < 0.20 |
| Tight | 0.20 – 0.40 |
| Elevated | 0.40 – 0.65 |
| Black-Period-like | > 0.65 |

### Rajoitukset

- EPP on synteettinen — se tiivistää, ei selitä. Yksittäisten komponenttien arvojen tulee aina olla saatavilla.
- Painotukset ovat normatiivisia valintoja; eri painotus tuottaa eri EPP-arvon.
- EPP ei ole viranomaismittari eikä korvaa operatiivista tilannekuvaa.

---

## Core Metric F — Allocation Pressure (AP)

### Rooli

Rakenteellinen seurantamittari, joka tekee näkyväksi ajallisen synkronointiongelman: kuorma sitoutuu nopeasti, L3-vastauskapasiteetti kasvaa hitaasti. Ei live-laskettava tunneittain, vaan kausikohtainen tai vuosineljänneskohtainen analyysi.

### Kaava

**Konseptuaalinen:**
> Allocation Pressure = BP-energiaintegraali / Arvioitu pitkäkestoinen kotimainen endurance-kapasiteetti

**DA-003:n esimerkkilogiikka:**
Yksi 300 MW jatkuva uusi kuorma kasvattaa 168 tunnin Black Period -energiaintegraalia:

```
ΔBP_energy = 300 MW × 168 h = 50 400 MWh
```

**Operationaalinen AP-mittari (kausikohtainen):**

```
AP_season = sum(consumption, BP_window) / estimated_L3_endurance_capacity
```

Missä `estimated_L3_endurance_capacity` on tekninen arvio pitkäkestoisen dispatchable kapasiteetin kumulatiivisesta energiasta 168 tunnin ikkunassa.

**Trendimittari:**

```
AP_trend = ΔBP_energy_integral(year) / ΔL3_capacity(year)
```

Jos AP_trend > 1, kuorma kasvaa nopeammin kuin sitä kantava kapasiteetti.

### Aika-ikkuna

Ei tuntipohjainen. Lasketaan:
- **kausikohtaisesti** (joulukuu–helmikuu)
- vertaillen talveen edeltäneeseen talveen

### Threshold-rakenne

AP:lle ei anneta numeraalisia posture-kynnyksiä samoin kuin A–E:lle, koska L3-kapasiteetin arvio sisältää merkittävää epävarmuutta. Sen sijaan:

| Tulkinta | Ehto |
|----------|------|
| Tasapainossa | AP_trend ≈ 1.0 (±0.10) |
| Divergoiva | AP_trend > 1.15 (kuorma kasvaa nopeammin) |
| Konvergoiva | AP_trend < 0.85 (kapasiteetti kasvaa nopeammin) |

### Rajoitukset

- AP vaatii L3-kapasiteettiestimaatin, joka ei ole suoraan saatavissa Fingrid Open Datasta.
- Ensimmäisessä vaiheessa AP toimii tulkinnallisena kehysmittarina, ei automaattisena laskennallisena arvona.
- Manuaalinen päivitys talvikausien välillä on hyväksyttävä toteutustapa.

---

## Core Metric G — Residual Risk Transfer Context (RRTC)

### Rooli

Rakenteellinen tulkintakehys, ei numeerinen live-mittari. Kuvaa, kuinka systeeminen allokointirakenne jakaa stressin seurauksia — ja erityisesti, jääkö residual riski suojaamattomille kuluttajille.

### Sisältö

RRTC ei laske arvoa vaan ylläpitää kolmea rakennetulkintaa:

**RRTC-1: Suojarakenne**  
Kuinka suuri osa kokonaiskulutuksesta on PPA:n tai kiinteän sopimuksen kautta hintasuojattu?  
*(Ei suoraan laskettavissa Fingrid-datasta; viittaus julkisiin PPA-ilmoituksiin ja markkina-analyysiin.)*

**RRTC-2: Spot-altistunut kuorma**  
Arvio spot-hinnalle altistuvan kulutuksen osuudesta — erityisesti kotitaloudet ilman kiinteää sopimusta.

**RRTC-3: Stressitapahtuman hintaseuraus**  
Kuinka paljon spot-hinta on noussut aiemmissa korkean kysynnän jaksoissa? Viittaus historiallisiin talvi-spike-tapahtumiin.

### Threshold-rakenne

RRTC:lle ei aseteta posture-kynnyksiä. Sen sijaan instrumentti sisällyttää RRTC:n:
- **tulkinnallisena kehyskontekstina** korkean EPP:n tai Elevated/Black-Period-like -luokituksen yhteydessä
- **viittauksena TN-001:n rakenteelliseen epäsymmetria-analyysiin**

### Rajoitukset

- RRTC on poliittisesti sensitiivinen muuttuja — instrumentti pyrkii rakenteelliseen kuvaukseen, ei normatiiviseen arvioon yksittäisistä toimijoista.
- TN-001:n sanamuoto: "rakenteellinen epäsymmetria, ei yksittäisten toimijoiden väärä käytös."

---

## Posture Logic — Kokonaisluokitus

### Luokituslogiikka

Kokonaisposture määräytyy **EPP:n ensisijaisesti**, mutta sitä korjataan komponenttien ääriarvoilla seuraavasti:

```
IF EPP < 0.20                         → Normal
IF EPP 0.20–0.40                      → Tight
IF EPP 0.40–0.65                      → Elevated
IF EPP > 0.65                         → Black-Period-like

OVERRIDE-säännöt (yksittäinen komponentti voi nostaa posturea):
  IF SP_168 > 0.55 → vähintään Elevated (vaikka EPP < 0.40)
  IF DC_168 < 0.65 → vähintään Elevated
  IF NIR_168 > 0.33 → vähintään Elevated
```

### Posture-kuvaukset (julkinen tulkintateksti)

| Posture | Kuvaus |
|---------|--------|
| **Normal** | Talvinen jatkuvuuspaine normaalirajoissa. Kotimainen tuotanto kattaa suurimman osan kysynnästä. Ei merkittävää endurance-signaalia. |
| **Tight** | Kysyntäpaine koholla tai kotimainen peitto heikentynyt. Järjestelmä toimii, mutta marginaalit ohenevat. Endurance-kerroksen tilanne seurannassa. |
| **Elevated** | Useampi endurance-signaali samanaikaisesti koholla. Pitkittyvä riippuvuus tuonnista tai dispatchable-kerroksesta. Merkittävä kumulatiivinen paine, vaikka hetkellinen tasapaino säilyisi. |
| **Black-Period-like** | Useamman päivän korkea kuorma, heikko kotimainen peitto ja korkea endurance-paine yhtä aikaa. Järjestelmä toimii, mutta on diagnostisesti samankaltainen kuin Black Period -skenaariot. Tämä ei ole viranomaishälytys. |

---

## Kalibrointiparametrit — yhteenveto

| Parametri | Oletusarvo | Kalibroinnin lähde |
|-----------|-----------|---------------------|
| DP_72 Tight-kynnys | 1.05 | Talvikaudet 2018–2024 |
| DC_72 Tight-kynnys | 0.80 | Talvikaudet 2018–2024 |
| NIR_72 Tight-kynnys | 0.10 | Talvikaudet 2018–2024 |
| SP stress_hour DP-ehto | 1.08 | Instrumenttiparametri |
| SP stress_hour DC-ehto | 0.85 | Instrumenttiparametri |
| EPP paino w_DC | 0.30 | Normatiivinen valinta |
| EPP paino w_SP | 0.30 | Normatiivinen valinta |

---

## Metodinen lukituslista

Nämä rajaukset ovat kanonisia ja pysyvät muuttumattomina versionumeroon asti:

1. **Mittarit ovat diagnostisia, eivät optimointimittareita.**
2. **Posture-luokitus ei ole viranomaishälytys.**
3. **Risk transfer on rakenteellinen havainto, ei moraalinen syytös.**
4. **Stability ≠ endurance.** Hetkellinen tasapaino ei tarkoita monipäiväistä kestävyyttä.
5. **MW ≠ MWh.** Hetkellinen teho ei yksin ratkaise Black Period -ongelmaa.
6. **EPP on synteettinen indeksi** — komponenttiarvot ovat aina ensisijainen tulkintalähde.

---

## Viittaukset

| Dokumentti | Rooli tässä mittaristossa |
|------------|--------------------------|
| WP-001 | Capacity vs. Duration -erottelu; Black Period 168h-ikkuna |
| DA-001 | Early warning -logiikka; "Concern trending toward Danger" |
| DA-003 | Layer divergence; allokointia kiihtyvä kuorma vs. hidas L3-kasvu |
| WP-008 | Uuden jatkuvan kuorman endurance-vaikutukset |
| TN-001 | PPA-rakenne ja residual risk transfer -logiikka |

---

*ACI Open Grid Instrument — Metric Definition v A-1.0*  
*Tämä dokumentti on kanoninen mittarirunko. Seuraavat vaiheet: B (Observatory wireframe) ja C (Dataset registry).*
