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

## Mita tama konkreettisesti toisi WEM:iin (jo dokumentoitu §07:ssa)

1. Nordic-laajuinen Dunkelflaute-tarkistus (WR-komponentin rinnalle,
   ei tilalle) - tuulivoima kaikilta Pohjoismaiden tarjousalueilta
2. SE1:n oma teollinen kuorma (Stegra/HYBRIT) suoraan nakyviin ennen
   TRR:n kiristymista

## Rajaus

Tama dokumentti on SUUNNITELMA, ei toteutus. Tila 2026-07-24:
- Rekisterointi: TEHTY
- API-pääsypyyntö (sähköposti): LÄHETETTY, odotetaan ~3 arkipäivää
- DocumentType/processType-koodit: VARMISTETTU virallisesta lähteestä (A11, A75+A16, A69)
- EIC-aluekoodit: VARMISTETTU virallisesta listasta (kaikki Pohjoismaiden BZN)
- XML-jäsentimen valinta: EI VIELÄ tehty
- Worker-arkkitehtuuri (uusi vs. laajennus): EI VIELÄ päätetty
- Itse koodi: EI VIELÄ kirjoitettu
- Security Token: EI VIELÄ saatu (odottaa hyväksyntää)

Ainoa jäljellä oleva este ennen koodauksen aloittamista on Security
Tokenin saapuminen. Kaikki muu tekninen valmistelu (mitä kutsua, millä
parametreilla, mistä EIC-koodit) on nyt tehty valmiiksi odotusaikana.
