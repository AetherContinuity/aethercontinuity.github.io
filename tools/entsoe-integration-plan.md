# ENTSO-E Transparency Platform -integraatio WEM:iin — suunnitelma

**Tila:** suunniteltu, EI toteutettu. Kayttajan oma ehdotus 2026-07-24,
tarkennettu ENTSO-E:n oman API-dokumentaation ja kayttajan lataaman
referenssikuvan (BZN|SE1 Cross-Border Physical Flows, FI/NO4/SE2,
24.7.2026) perusteella.

## Miksi tama on eri luonteinen kuin aiemmat proxy-lisaykset

Copernicus (NDVI-kuva, BEM) oli itsepalvelu: OAuth-asiakas luodaan
dashboardissa heti, ei odotusaikaa. **ENTSO-E vaatii manuaalisen
sahkopostihyvaksynnan (~3 arkipaivaa)** ennen kuin Security Token
edes voidaan generoida. Tama TARKOITTAA etta rekisteroinnin
ALOITTAMINEN on oma, aikasidonnainen ensimmainen askel joka kannattaa
tehda RIIPPUMATTA siita milloin itse koodia aletaan kirjoittaa.

## Askel 1: Rekisterointi (TEHTY, odotetaan hyväksyntää)

**Tila 2026-07-24, päivitetty:** Transparency Platform -tili olemassa, JA
RESTful API access -pyyntö LÄHETETTY sähköpostilla transparency@entsoe.eu
(otsikko "Restful API access"). ~3 arkipäivän hyväksyntäodotus KÄYNNISSÄ.
Askel 2 (alla) tehdään odotuksen aikana, jotta koodaus voi alkaa heti
tokenin saavuttua ilman lisäviivettä.

1. Rekisteroidy: https://transparency.entsoe.eu — TEHTY
2. Lähetä sähköposti transparency@entsoe.eu, otsikko "Restful API access" — TEHTY
3. Odota ~3 arkipäivää hyväksyntää — KÄYNNISSÄ
4. Kun hyväksytty: kirjaudu, Account Settings -> generoi "Web Api Security Token" — EI VIELÄ

## Askel 2: Tarkat rajapintaparametrit — VARMISTETTU 2026-07-24

Lähteet: ENTSO-E Transparency Platform Restful API Implementation Guide
(transparency.entsoe.eu) + Zendesk-ohjeet (DocumentType-lista,
EIC-aluekoodilista, molemmat päivitetty 2025).

### DocumentType-koodit (varmistettu virallisesta listasta)

| Käyttö | documentType | processType | Huom |
|---|---|---|---|
| Cross-Border Physical Flows (artikla 12.1.G) | **A11** (Aggregated energy data report) | ei vaadita | Mandatory: DocumentType, In_Domain, Out_Domain, TimeInterval. HUOM: API palauttaa VAIN yhden suunnan per pyyntö — molempien suuntien saamiseksi in_Domain/out_Domain on vaihdettava ja tehtävä KAKSI pyyntöä |
| Actual Generation per Type (tuulivoima per tarjousalue) | **A75** (Actual generation per type) | **A16** (Realised) | Vastaa käyttäjän kuvan "tuulivoima per BZN" -tarvetta |
| Wind and Solar Forecast (day-ahead) | **A69** (Wind and solar forecast) | — | 72h-ennusteen Nordic-laajennukseen jos halutaan myöhemmin |

### EIC-aluekoodit — Pohjoismaiden tarjousalueet (varmistettu, ei arvattu)

| Tarjousalue | EIC-koodi |
|---|---|
| BZN\|FI | `10YFI-1--------U` |
| BZN\|SE1 | `10Y1001A1001A44P` |
| BZN\|SE2 | `10Y1001A1001A45N` |
| BZN\|SE3 | `10Y1001A1001A46L` |
| BZN\|SE4 | `10Y1001A1001A47J` |
| BZN\|NO1 | `10YNO-1--------2` |
| BZN\|NO2 | `10YNO-2--------T` |
| BZN\|NO3 | `10YNO-3--------J` |
| BZN\|NO4 | `10YNO-4--------9` |
| BZN\|NO5 | `10Y1001A1001A48H` |
| BZN\|DK1 | `10YDK-1--------W` |
| BZN\|DK2 | `10YDK-2--------M` |

### Esimerkkikutsu (GET, ei vielä ajettu — token puuttuu)

```
https://web-api.tp.entsoe.eu/api?securityToken=TOKEN&documentType=A11&in_Domain=10YFI-1--------U&out_Domain=10Y1001A1001A44P&periodStart=202607230000&periodEnd=202607240000
```
(FI<-SE1-suunta, 24h ikkuna — SE1->FI-suunnan saamiseksi in_Domain/out_Domain vaihdetaan)

### Rajoitteet varmistettu samalla kertaa

- **Vastausmuoto: XML** (GL_MarketDocument / Publication_MarketDocument, IEC-skeemat) — vahvistettu esimerkkivastauksista
- **Rate limit: 400 pyyntöä/min per IP+token**, ylitys -> 10 min esto (HTTP 429)
- **Aikaväli max 1 vuosi** per pyyntö (Standard Data View -tyyppisille kyselyille)
- **Yksi pyyntö = yksi suunta** rajaylityksille (Cross-Border Physical Flows) — Nordic-WR-komponentti tarvitsisi 2 pyyntöä per rajapari (FI<->SE1 molempiin suuntiin) jos molemmat suunnat halutaan

## Askel 3: Tekninen toteutus (uusi asia taman koodikannan sisalla)

**XML-jasennys on GENUINE uusi tekninen kappale** - kaikki nykyiset
proxyt (aci-fingrid-proxy, aci-corine-proxy, aci-nve-proxy) kasittelevat
JSON:ia. ENTSO-E palauttaa XML:aa (IEC 61970 CIM-skeema). Cloudflare
Workers -ymparistossa XML-jasennys vaatii joko:
(a) DOMParser-yhteensopivan kirjaston (esim. `fast-xml-parser`, toimii
Workers-ymparistossa, ei vaadi Node-spesifista DOM:ia), tai
(b) kasin kirjoitetun regex/string-pohjaisen poiminnan yksinkertaisille,
tunnetun rakenteen XML-vastauksille (riskialtis mutta ei ulkoisia
riippuvuuksia).

Suositus: (a) - `fast-xml-parser` on kevyt, ei vaadi natiivimoduuleja,
toimii todennakoisesti Workers-ymparistossa sellaisenaan.

## Askel 4: Arkkitehtuurivalinta

Kaksi vaihtoehtoa, EI viela paatetty:
- **Uusi Worker** (`aci-entsoe-proxy`) - sama malli kuin muut, oma
  repo, oma secret-varasto. Selkeampi erottelu, mutta yksi Worker lisaa.
- **Laajennus olemassa olevaan** (esim. `aci-fingrid-proxy`, koska
  sisaltoalue on lahella - molemmat ovat sahkojarjestelmadataa) -
  vahemman uutta infraa, mutta sekoittaa kaksi eri autentikointi-
  mallia (Fingrid ei vaadi tunnistautumista, ENTSO-E vaatii) samaan
  Workeriin.

Ei suositusta viela - paatettava ennen koodausta.

## Askel 2b: Rakenteilla/suunniteltu tuotantokapasiteetti — käyttäjän oma lisäehdotus 2026-07-24

Kaksi eri ENTSO-E-datalähdettä löytyi tähän tarpeeseen, EI vielä tasa-arvoisen varmasti dokumentoituna:

**1. Installed Capacity per Production Type [artikla 14.1.A] — VARMISTETTU, käyttökelpoinen jo nyt**
- `documentType=A68`, `in_Domain=<BZN EIC>`, PsrType valinnainen (B19=Wind Onshore, B18=Wind Offshore)
- Palauttaa VUOSITTAISEN asennetun kapasiteetin tuotantotyypeittäin per tarjousalue
- Käyttökelpoisuus: perättäisten vuosien vertailu näyttää KASVUN (esim. jos SE1:n tuulivoiman asennettu kapasiteetti kasvaa vuodesta toiseen, se näkyy suoraan tässä sarjassa) — EPÄSUORA mutta luotettava tapa nähdä äskettäin valmistunut kapasiteetti
- EI kerro yksittäisistä RAKENTEILLA olevista hankkeista, vain vuositason koontisumman

**2. "Production and Generation Units" -master data (yksittäiset laitokset, tila "existing"/"planned") — EI VIELÄ VARMISTETTU**
- Löytyi viite (Zendesk-artikkeli, bot-suojauksen takana, ei saatu haettua suoraan): "Information about production units & generation units (existing and planned) with an installed generation capacity equaling to or exceeding..."
- Tämä VAIKUTTAISI olevan täsmälleen se mitä alunperin kysyit — yksittäiset laitokset MERKITTYNÄ tilalla joka erottelee olemassa olevat suunnitelluista
- MUTTA: tämä näyttää olevan eri datamuoto (`Configuration_MarketDocument`, "ProductionAndGenerationUnits" massaeristys File Libraryn kautta) kuin yksinkertainen RESTful GET-kysely muiden datalähteiden tapaan — TARKKAA parametrilistaa (documentType/businessType tälle nimenomaiselle näkymälle) EI SAATU VARMISTETTUA bot-suojauksen takia
- **Rehellinen rajaus:** tätä EI pidä merkitä käyttökelpoiseksi ennen kuin joko (a) Zendesk-sivu saadaan auki kirjautuneena käyttäjänä, tai (b) token saapuu ja tätä voidaan kokeilla suoraan API:sta, tai (c) File Library -osion oma dokumentaatio käydään läpi tarkemmin

**Suositus:** aloita Nordic-WR-toteutus artiklalla 14.1.A (varmistettu, riittää näyttämään kapasiteetin KASVUN vuositasolla) — palataan yksittäisten "planned"-laitosten tarkempaan dataan tarvittaessa myöhemmin, kun token on saatu ja voidaan kokeilla suoraan.



1. Nordic-laajuinen Dunkelflaute-tarkistus (WR-komponentin rinnalle,
   ei tilalle) - tuulivoima kaikilta Pohjoismaiden tarjousalueilta
2. SE1:n oma teollinen kuorma (Stegra/HYBRIT) suoraan nakyviin ennen
   TRR:n kiristymista

## Askel 3: Koodi kirjoitettu (2026-07-24) — validoitu esimerkki-XML:ää vastaan, ei live-APIa

`aci-entsoe-proxy` — repo luotu (https://github.com/AetherContinuity/aci-entsoe-proxy),
koodi pushattu, Cloudflaren natiivi Git-integraatio deployasi Workerin
automaattisesti pushin yhteydessä (ei erillistä `wrangler deploy` -tarvetta).
Kolme reittiä: `/wind-generation` (A75+A16), `/cross-border-flow` (A11,
molemmat suunnat automaattisesti), `/installed-capacity` (A68).

**Validoitu paikallisesti ENNEN live-testiä:** kaksi ydinjäsennysrakennetta
(GL_MarketDocument ja Publication_MarketDocument, molemmat fast-xml-parser:lla)
testattu ENTSO-E:n OMAA dokumentaation esimerkki-XML:ää vastaan — molemmat läpäisivät.

**LIVE-TESTI ONNISTUI 2026-07-24:** `/wind-generation?bzn=SE1&periodStart=2026-07-23T00:00:00Z&periodEnd=2026-07-24T00:00:00Z`
palautti oikean datan ENSIMMÄISELLÄ yrityksellä — `MktPSRType.psrType`
("B19", Wind Onshore) tunnistui oikein, 96 pistettä 15 min resoluutiolla
(= tasan 24h), arvot realistisia (n. 25–1660 MW SE1:n tuulelle,
vuorokausivaihtelu näkyy selvästi). Aiempi epävarmuus tästä rakenteesta
(ks. alla, historiallinen) osoittautui turhaksi varovaisuudeksi — koodi
toimi sellaisenaan.

**Sivuhavainto testauksesta (paikallinen, ennen live-testiä):** attribuutilliset kentät (esim.
`in_Domain.mRID codingScheme="A01"`) jäsentyvät fast-xml-parser:lla
muotoon `{"#text": "...", "@_codingScheme": "A01"}`, ei pelkäksi
merkkijonoksi — huomioitava jos näitä kenttiä joskus luetaan suoraan.

## Tila 2026-07-24 — /wind-generation LIVE JA TOIMII

- Rekisteröinti: TEHTY
- API-pääsypyyntö (sähköposti): HYVÄKSYTTY
- DocumentType/processType-koodit: VARMISTETTU virallisesta lähteestä (A11, A75+A16, A69, A68)
- EIC-aluekoodit: VARMISTETTU virallisesta listasta (kaikki Pohjoismaiden BZN)
- XML-jäsentimen valinta: TEHTY (fast-xml-parser)
- Worker-arkkitehtuuri: TEHTY (uusi repo, aci-entsoe-proxy)
- Itse koodi: KIRJOITETTU JA DEPLOYATTU (Cloudflare-GitHub-integraatio)
- Security Token: SAATU JA ASETETTU (Cloudflare Dashboard → Variables and Secrets)
- **`/wind-generation`: LIVE-TESTATTU, TOIMII TÄYSIN** — SE1 tuulivoima, 96 pistettä/24h, MktPSRType.psrType tunnistui oikein ensimmäisellä yrityksellä

## Kriittinen korjaus 2026-07-24 — ENTSO-E:n harva pistekoodaus

`/cross-border-flow?from=FI&to=SE1` -live-testi paljasti todellisen bugin:
ENTSO-E jättää KOKONAAN POIS Point-elementtejä XML:stä kun arvo ei muutu
edellisestä (ei vain jätä quantity-kenttää tyhjäksi olemassa olevasta
Point-elementistä — koko elementti puuttuu). FI→SE1-virtaus pysyi 0:ssa
suurimman osan 24h-ikkunasta, ja vastaus sisälsi vain positiot 1, 39–42 —
loput 91 puuttuivat kokonaan. Alkuperäinen `flattenPeriod` iteroi vain
XML:ssa olevien pisteiden yli, joten väliin jäävät positiot katosivat
tulosjoukosta kokonaan (5 pistettä 96:n sijaan) sen sijaan että ne
täyttyisivät viimeisimmällä tunnetulla arvolla.

**Korjattu ja validoitu** paikallisella testillä (simuloitu tarkalleen
todellinen harva vastaus + täysi 96 pisteen sarja regressiotestinä,
molemmat läpäisivät). Sama korjaus vaikuttaa myös `/wind-generation` ja
`/installed-capacity` -reitteihin — `/wind-generation`:n aiempi onnistunut
testi sattui saamaan täyden 96 pisteen sarjan SE1:n tuulelle eikä siksi
paljastanut bugia, mutta sama koodipolku olisi voinut epäonnistua toisella
tarjousalueella tai ajanjaksolla jossa tuulituotanto pysyisi vakiona.

## Jäljellä (ei vielä testattu)

- `/cross-border-flow` (A11, kaksoiskutsu-logiikka) — LIVE-TESTATTU 2026-07-24, paljasti ja korjasi kriittisen harvan-pistekoodauksen bugin (ks. yllä). Ei vielä uudelleentestattu korjauksen jälkeen.
- `/installed-capacity` (A68, vuositason kapasiteetti) — ei vielä live-testattu
- WEM:n oma frontend-integraatio (Nordic-WR-komponentti) — ei vielä aloitettu, odottaa että kaikki kolme reittiä on ensin vahvistettu toimiviksi
