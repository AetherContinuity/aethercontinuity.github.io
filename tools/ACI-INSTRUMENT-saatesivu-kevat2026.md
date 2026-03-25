# ACI Winter Endurance Monitor
## Saatesivu — Kevät 2026

---

Tämä instrumentti valmistui talvella 2024–2025. Kevään 2025 saatesivussa kirjoitettiin, että varsinainen koetinkivi on tammi–helmikuu 2026 — ja että silloin nähdään, toimiiko diagnostiikka.

Nyt on maaliskuu 2026. Koetinkivi on takana.

---

### Mitä talvi 2025–2026 näytti

Instrumentilla oli tällä talvella taustallaan se, mitä kevään 2025 kalibrointijakso tuotti: toimiva laskentaketju, EPP-trendiin kertynyt historiakerros, ja baseline joka ei enää ollut pelkkä teoreettinen approksimatio.

Diagnostiikka toimi rakenteellisesti tarkoitetulla tavalla. Stress Persistence -laskuri reagoi kiristymisjaksoihin tunnistettavasti. EPP-posture liikkui kalibroitua taustatasoa vasten eikä hukkumassa kohinaan.

Kalibrointiparametrien osalta — DP-kynnys 1.08 ja DC-kynnys 0.85 — talvi antoi ensimmäisen oikean vertailupohjan. Ennen seuraavaa talvea on perusteet tarkistaa, ovatko kynnykset kalibroituneita vai vaativatko hienosäätöä todellisen talviaineiston valossa.

---

### Mitä keväällä 2026 kannattaa tehdä

**Tarkista dataset-IDs ennen kuin kevätdata alkaa kertyä.** Fingrid Open Data -datasetit 124, 74 ja 194 — kulutus, tuotanto ja netto-tuonti — kannattaa varmistaa `data.fingrid.fi`:stä. Fingrid on muuttanut ID-numeroita aiemmin. Yksi tarkistus nyt säästää yhden debuggauskerran ensi lokakuussa.

**Anna kevään tasoittaa EPP-historia.** Talvikiristykset jäävät trendikaavioon. Kevät rakentaa sen normaalin tason, jota vasten ensi syystalven kiristyminen piirtyy. Kolme rauhallista kuukautta on enemmän kuin riittävä kalibrointijakso.

**Tarkista SP-kynnykset nyt kun vertailuaineisto on olemassa.** Viime talven data on ensimmäinen kerta, jolloin kalibrointiparametreja voidaan arvioida todellista talvijaksoa vasten — ei pelkästään teoreettisesti. Muutos on edelleen yksi rivi `CONFIG`-lohkossa, mutta nyt tiedetään mihin suuntaan.

**Valmistele instrumentti v2-kysymykseen.** Ensimmäinen kokonainen talvi on osoittanut, mitkä mittarit toimivat ja missä on liikkumavaraa. Ennen ensi talvea on syytä katsoa, tarvitseeko instrumentti rakenteellisia muutoksia vai riittääkö parametritason säätö.

---

### Miksi seuraava koetinkivi on talvi 2026–2027

Tammi–helmikuu 2026 oli ensimmäinen kerta, jolloin instrumentilla oli täysi valmiustila. Talvi 2026–2027 on ensimmäinen kerta, jolloin instrumentilla on myös edellinen talvi vertailuaineistona.

Yksittäinen talvi kertoo, toimiiko diagnostiikka. Kaksi talvea kertoo, onko se kalibroitu.

---

### Yksi lause tiivistettynä

> Ensimmäinen koetinkivi on takana. Nyt alkaa kalibrointi.

---

*ACI Open Grid Instrument — Winter Endurance Monitor*
*Aether Continuity Institute · aethercontinuity.org*
*Kevät 2026*
