# Löydökset 9.–14.9.2026

**Mitä mitattiin, mitä siitä seurasi, ja mikä jäi auki.**

Istunnon muisti. Korjausinventaario kertoo mikä WEM:ssä oli hämärää;
proxy-ohje kertoo miten rajapintoja käytetään. Tämä kertoo **mitä
opittiin järjestelmästä itsestään.**

Jokainen luku on jäljitettävissä tallennettuun aineistoon:

    tools/data/rp-244-talvi-2025-2026.json      527f60ca2a97
    tools/data/rp-margin-talvi-2025-2026.json   69a25d6a94ad
    tools/data/wem-mittaukset-2026-09.json      d90ed9140b7e

---

## 1 · Riittävyys ja korjauskyky ovat eri asioita

**Tämä on istunnon keskeisin löydös.**

9.9.2026 klo 14:45–20:15 ylössäätöhinta oli 500–4 000 €/MWh yksitoista
kertaa. Samana päivänä:

    EPP              0,566   "Elevated"
    Shortage Status  0       "normaali"
    SP (W168)        54,8 %

**Kumpikaan ei näyttänyt mitään.** Kuusi tuntia 166:sta keskiarvoistuu
näkymättömiin.

Ketju mitattiin loppuun asti:

| suure | lähde | 9.9. klo 17:15 |
|---|---|---|
| ACE — tasevirhe | DS 397 | −819 MW |
| tarjottu ylös | DS 373 | 592 MW |
| aktivoitu | DS 342 | 593 MW |
| **jäljellä** | erotus | **−1 MW** |
| hinta | DS 244 | 2 640 → 4 000 € |

**Tarjouskirja tyhjeni kokonaan.** Ja tarjousmäärä *laski* kriisin
aikana 850 → 592 MW — tarve kasvoi, tarjonta väheni.

Talven kalibroinnissa (17 470 pistettä) marginaali **ei mennyt
miinukselle kertaakaan**. Yksi syyskuun päivä ylitti koko edellisen
talven.

### RP_margin — uusi päämittari

    RP_margin = (tarjottu ylös − aktivoitu) / tarjottu ylös

Talven vyöhykejakauma, ja **hinnan mediaani nousee monotonisesti**:

    runsas       >60 %    98,38 %      44 €
    normaali   40–60 %     1,30 %     300 €
    kireä      20–40 %     0,23 %     542 €
    niukka      5–20 %     0,06 %   1 990 €
    tyhjenemässä <5 %      0,03 %   4 000 €

**Rajoja ei valittu hinnan mukaan — hinta seuraa niistä.** Se on vahvin
yksittäinen todiste siitä että mittari mittaa oikeaa asiaa.

`DS 373` on *available* eikä *installed*: Fingridin oma kuvaus sanoo
että se **ei sisällä epäkäytettäviä tarjouksia.**

---

## 2 · CHP:n rooli osoittautui vääräksi kolmesti

Oletin ensin että CHP on ylössäätötarjonnan lähde. Se kumottiin kolme
kertaa peräkkäin:

**Korrelaatio on negatiivinen molempiin suuntiin.** Talven otoksesta
(26 vrk, 2 087 paria): CHP ↔ tarjottu ylös **r = −0,671**, CHP ↔
tarjottu alas **r = −0,527**.

    CHP  180 MW  →  tarjottu 1 398 MW  ·  hinta med   8 €
    CHP 2156 MW  →  tarjottu   769 MW  ·  hinta med 154 €

**Kesä vahvisti.** Kesän tarjouskirja mediaani 1 010 MW vs. talven
1 059 — suhde **0,95** — vaikka CHP oli kesällä 6–78 MW. Jos CHP olisi
tarjonnan lähde, kesällä pitäisi olla romahdus. Ei ole.

**Ja kulutuskontrolli kumosi kolmannen version.** Väitin että "kylmällä
järjestelmä on yksipuolisemmin niukka". Kulutus vakioituna CHP:n
vaikutus alas/ylös-suhteeseen **katoaa** ja korkean kulutuksen
kolmanneksessa **kääntyy**. Alkuperäinen taulukko näytti **kulutuksen**
vaikutuksen, ei CHP:n.

### Selitys

CHP on **lämpöohjattua**. Se ajaa koska lämpöä tarvitaan, ei koska
sähkömarkkina kutsui. Siksi se ei tarjoa kumpaakaan suuntaa: ylös ei
mahdu (jo täydellä), alas ei voi (lämpö katoaisi).

**CHP:n teho on kylmyyden mittari, ei tarjonnan lähde.** Se näkyy
DS 192:ssa ja FS:ssä, ei tarjouskirjassa.

---

## 3 · Sähkökattilat ovat hintajoustava kuorma

`DS 371`, saatavilla 3.12.2024 alkaen. **Maksimi 1 069 MW** — enemmän
kuin Loviisan kapasiteetti.

    hinta   3 €  →  kattilat 720 MW  ·  CHP  261 MW
    hinta 159 €  →  kattilat 183 MW  ·  CHP 1714 MW

Korrelaatio hintaan **r = −0,643**, CHP:hen **r = −0,668**.

**Takaisinkytkentä mitattuna, ei päätelty kannattavuudesta:** kattila
korvaa CHP:n lämpöä juuri halvimpina tunteina eli vie siltä
käyttötunteja. Kylmällä kattila on pois ja CHP:n pitäisi ajaa — mutta
jos se on ajettu alas kannattamattomana, sitä ei silloin ole.

Ne ovat käytännössä **alassäätöresurssi joka ei ole tarjouskirjassa**,
ja se selittää osan epäsymmetriasta: alassäätöä on 1,63-kertaisesti.

---

## 4 · Inertia — kolmas ulottuvuus

`DS 260`, 130–164 GWs, 15 min. Pohjoismaisen järjestelmän liike-energia.

Korrelaatio tuuleen **r = −0,603**: tuulen kasvaessa inertia laskee,
koska turbiinit ovat taajuusmuuttajan takana eivätkä tuota
pyörimisenergiaa.

```
FS           paljonko peruskuormaa on
RP_margin    paljonko korjauskykyä on jäljellä
inertia      kuinka nopeasti taajuus putoaa ENNEN korjausta
```

**`WR` on ollut koko ajan inertian epäsuora mittari**, mutta sitä ei
ole sanottu ääneen eikä mitattu. Ei vielä WEM:ssä.

---

## 5 · Kaksi mekanismia jotka näyttävät samalta

Lauantai-ilta 12.9.2026, tyyni iltapäivä:

    klo 12   tuuli    69 MW   tarjottu 1 011 MW   hinta 159 €
    klo 19   tuuli 1 630 MW   tarjottu   922 MW   hinta   0 €
    klo 02   tuuli 3 499 MW   tarjottu 1 438 MW   hinta   4 €

**Tuuli viisikymmenkertaistui neljässätoista tunnissa.** Hinta oli
koholla (27,6 % tunneista 100–500 €, talvi 25,3 %) mutta `RP_margin`
pysyi 75 %:ssa.

| | hinta | tarjouskirja | marginaali |
|---|---|---|---|
| tuuleton hetki | ↑ | ohuempi | säilyy |
| huoltoseisokki 9.9. | ↑ | tyhjenee | → 0 |

**Kallis ei ole sama kuin niukka.** Hinta mittaa tarjousten tasoa,
marginaali niiden riittävyyttä. Siksi `RP_margin` on päämittari eikä
hinta.

---

## 6 · Huoltopäällekkäisyys empiirisenä ankkurina

Syyskuussa 2026 OL3 ja molemmat Loviisan yksiköt olivat osin
samanaikaisesti huollossa. W168-ydinvoima **3 243 MW** täyden
**4 394 MW** sijaan.

    mitattu FS (huollot päällä)              57,9 %
    FS samalla kulutuksella ilman huoltoja   71,4 %
    kulutus joka antaisi 57,9 % täydellä     +1 988 MW

**Järjestelmä ajoi siis tilaa jota skenaario "2027: +1500 MW DC"
kuvaa** — mitattuna, ei laskettuna.

**Rajoitus:** huolto on väliaikainen ja ennakoitu. Pysyvä kulutuslisäys
ei pääty lokakuun lopussa. **Koe aliarvioi pysyvän kasvun vaikutusta.**

---

## 7 · Rakenteelliset ennusteet (SvK, Fingrid)

Svenska kraftnätin *Kortsiktig marknadsanalys 2024*, Fingridin omat
luvut Suomelle:

**Suomi 2025 → 2029, MW:**

    vesivoima      2 570 →  2 570      vakio
    ydinvoima      4 394 →  4 394      vakio
    CHP            6 473 →  5 668      −805
    kaasuturbiinit   116 →     71      −45
    maatuulivoima  8 741 → 17 196   +8 455
    aurinko        2 581 → 10 430   +7 849
    yhteensä      24 938 → 41 136  +16 198

**FS:n osoittaja on täsmälleen vakio 6 964 MW koko jakson.** Kaikki
kasvu menee nimittäjään. Se on rakenteellinen syy sille miksi `FS`
heikkenee ilman että mitään poistuu.

Ja −805 MW CHP-poistuma on **riippumaton vahvistus** SM-015:n
monitorille, joka on koottu käsin laitostason ilmoituksista.

**SE1:**

    vesivoima   8 128 → 8 128   ei kasva
    tuulivoima  6 579 → 8 932   +2 353

> *"Exporten på AC-förbindelserna från SE1 till Finland består under
> analysperioden men **försvagas kraftigt från och med 2028**."*

Pohjoismainen ylijäämä supistuu **52 → 16 TWh** 2025–2029. Ja nettovirta
Suomen ja SE3:n välillä **kääntyy 2029**.

Se on linjassa `HLBY-27 ≈ −0,55 €/MWh` -termiinihinnan kanssa: Suomi ei
enää ole halpa pää.

---

## 8 · Mitä jäi auki

**Trendimittaus ei ole mahdollinen.** `DS 373` alkaa 3/2025 — yksi
talvi, ei sarjaa. Talvi 2026–27 on ensimmäinen vertailukohta ja se
kannattaa kaapata järjestelmällisesti.

**CHP ~ lämpötila -regressio ei erottele.** Kulmakerroin −58,5 / −79,2
/ −75,4 / −36,6 / −140,4 MW/°C viideltä talvelta. Trendiä ei ole; otos
on 18 päivää ja otospäivien lämpötila vaihtelee −6,8…−0,3. Kaksi
mekanismia tuottaa saman signaalin: **leuto talvi** (palautuva) ja
**kapasiteetin purku** (pysyvä). Erottaminen vaatii lämpötilakontrollin
ja satoja päiviä per talvi.

**Vertailukohta olisi SM-015.** Jos regressio näyttää suuremman
pudotuksen kuin ilmoitetut sulkemiset, erotus on **ajamatta
jättämistä** — se on kannattavuusvaikutus jota sähkökattilat
aiheuttavat.

**Inertia ei ole WEM:ssä.** `DS 260` on todennettu muttei liitetty.

**EPAD-validointi puuttuu.** Kauppapaikka on Euronext (Nasdaq luopui
3/2026), `HLBQ-27` ja `LLBQ-27` ovat maksumuurin takana. Tripwire-
kalenterin täydennys C kuvaa rakenteen.

---

## 9 · Menetelmähavainto

Lähes jokainen tämän istunnon löydös — ja jokainen virhe — tuli siitä
että **kaksi lukua verrattiin toisiinsa.**

DS 105:n vakionolla löytyi kun spot ja S_ENERGY eivät täsmänneet.
CHP:n väärä rooli löytyi kun kesä ja talvi vertailtiin. Ulottuvuuskortin
väärä mittari löytyi tulosteesta, ei testeistä. Ja `RP_margin`
löydettiin kun hinta ja määrä yhdistettiin.

**Yksi luku ei paljasta mitään. Kaksi lukua paljastaa ristiriidan.**
