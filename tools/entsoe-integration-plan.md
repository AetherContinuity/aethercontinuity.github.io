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

## Askel 1: Rekisterointi (tee ENSIN, odottaessa muu suunnittelu jatkuu)

**Tila 2026-07-24 (vahvistettu kayttajan omalla tarkistuksella):** Transparency
Platform -tili ON JO olemassa, mutta RESTful API -pääsyä EI OLE VIELA pyydetty
(Account Settings ei näytä "Web Api Security Token" -kenttää). Tili ja
API-pääsy OVAT KAKSI ERI ASIAA ENTSO-E:n omassa prosessissa - pelkkä tili
ei riitä.

**SEURAAVA KONKREETTINEN ASKEL (ei viela tehty):** lahetä sähköposti
`transparency@entsoe.eu`, otsikolla "Restful API access", runkoon
rekisteröinnissa käytetty sähköpostiosoite. Tämän jälkeen ~3 arkipäivän
odotus ennen kuin token voidaan generoida.

1. Rekisteroidy: https://transparency.entsoe.eu (tavallinen tili) — TEHTY
2. Lahetä sahkoposti osoitteeseen transparency@entsoe.eu:
   - Otsikko: "Restful API access"
   - Viestiin: sama sahkopostiosoite jolla rekisteroidyit
3. Odota ~3 arkipaivaa hyvaksyntaa
4. Kun hyvaksytty: kirjaudu, Account Settings -> generoi "Web Api
   Security Token"
5. Tallenna token samalla tavalla kuin Copernicus-secretit
   (wrangler secret put ENTSOE_SECURITY_TOKEN uudessa/laajennetussa
   Workerissa)

## Askel 2: Tarkat rajapintaparametrit (selvitettava ENNEN koodausta)

ENTSO-E:n API vaatii TASMALLISET `documentType`/`processType`-koodit
JA EIC-muotoiset aluekoodit (esim. `BZN|SE2` - sama muoto joka nakyy
kayttajan omassa referenssikuvassa). Alla ALUSTAVA lista - VAATII
VARMISTUKSEN Implementation Guidesta ennen koodausta, ei arvattava:

| Kaytto | Todennakoinen documentType/processType | Tila |
|---|---|---|
| Cross-Border Physical Flows (FI<->SE1, SE1<->NO4 jne.) | Todennakoisesti A11 (Aggregated Energy Data Report -tyyppinen) - TARKISTETTAVA | Ei varmistettu |
| Actual Generation per Type (tuulivoima per tarjousalue) | A75 (Actual generation per type) + A16 (Realised) - loydetty ENTSO-E:n omasta esimerkista | Kohtalaisen varma, mutta testattava |
| Day-ahead tuuli/aurinko-ennuste | A69 (Wind and solar forecast) - TARKISTETTAVA | Ei varmistettu |

**EIC-koodit relevanteille alueille** (BZN-muodossa, kuten kayttajan
kuvassa): BZN|FI, BZN|SE1, BZN|SE2, BZN|SE3, BZN|SE4, BZN|NO1,
BZN|NO2, BZN|NO3, BZN|NO4, BZN|NO5, BZN|DK1, BZN|DK2 - TASMALLISET
numeromuotoiset EIC-koodit (esim. `10YFI-1--------U` Suomelle)
LOYDETTAVA ENTSO-E:n omasta aluekoodilistasta ennen ensimmaista
API-kutsua, EI arvattava.

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

Tama dokumentti on SUUNNITELMA, ei toteutus. Yksikaan askel (rekisterointi,
EIC-koodien varmistus, XML-jasentimen valinta, Worker-arkkitehtuuri)
ei ole viela tehty. Kayttajan oma huomio (2026-07-24): "Enso E data
rajapinta vaatinee taas avaimet" - vahvistettu ENTSO-E:n oman
dokumentaation kautta: KYLLA, mutta EI itsepalveluna kuten Copernicus -
manuaalinen sahkopostihyvaksynta ~3 arkipaivan viiveella.
