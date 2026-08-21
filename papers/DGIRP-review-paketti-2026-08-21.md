# DGIRP v0.3 / v0.4 + SM-009 §11 — ulkopuolinen tarkastuspaketti

**Päiväys:** 21.8.2026
**Tarkoitus:** vastakkainen (adversarial) vertaisarvio. Ei validointia.
**Kohde:** DGIRP v0.3 ja v0.4 -muistiot, SM-009 §11 (disclosure gap -variantti), CN-007 (kolmen vajeen malli).

---

## 0. Ohje arvioijalle

Tämä paketti on koottu kritiikkiä varten. Pyydetty tuotos on lista virheitä, ei arvio siitä onko työ hyvää.

Erityisesti pyydetään:

1. Laskennallinen toistettavuus. Tarkista §3:n havainnot itsenäisesti omilla laskuillasi. Älä luota tässä esitettyihin lukuihin.
2. Onko §3:ssa lueteltujen korjausten lisäksi virheitä, joita ei ole huomattu.
3. Onko jokin §3:n korjauksista itsessään väärä.
4. Onko §2:n lähdeluvuissa väärintulkintoja alkuperäislähteisiin nähden.

Merkitse jokainen väitteesi yhdellä kolmesta: **[V]** varmennettu lähteestä, **[A]** ammatillinen havainto, **[P]** varmentamaton päättely. Sama merkintätapa on käytössä alla.

Älä pehmennä. Jos jokin osa työstä pitäisi vetää pois, sano se.

---

## 1. Mitä DGIRP väittää

Kysymys: kuinka paljon järjestelmän resilienssimarginaalia uusi suuri jatkuva sähkökuorma kuluttaa eri sää-, tuotanto-, siirto- ja tuontiskenaarioissa.

Tapaus: 743 MW:n datakeskusklusteri, Kouvola.

Mittari (v0.4 §8.1, grid-only):

    RIILL_G = (F_domestic + F_import) / PeakLoad_stress

Mittari (v0.4 §8.2, hankekorjattu):

    RIILL_P = (F_domestic + F_import + F_system-flex + F_project-flex + F_project-firm) / PeakLoad_stress

Stressikuorma (v0.4 §9):

    PeakLoad_stress(L) = (15 553 + L) × 1,10

Päätösluokat: Green ≥ 1,15 · Amber 1,00–1,15 · Red 0,85–1,00 · Black < 0,85.

v0.3:n tulos: 743 MW on Red 2027–2028 ja Black 2029–2032. Nolla-kuorma on Amber 2027–2028 ja Red 2029–2032.

v0.4 poisti v0.3:n numerotaulukot ja jätti kehyksen.

---

## 2. Lähdeaineisto

### 2.1 Suomen järjestelmä

| Suure | Arvo | Lähde | Tila |
|---|---|---|---|
| Talven 2025–26 kulutushuippu | 15 553 MW, 8.1.2026 klo 17.00–17.15 | Fingrid, talviyhteenveto | [V] |
| Kotimainen tuotanto huipputunnilla | 14 320 MW | sama | [V] |
| Nettotuonti huipputunnilla | 1 233 MW | sama | [V] |
| Painotettu lämpötila huipputunnilla | n. −19 °C | sama | [V] |
| Aluehinta huipputunnilla | 92,39 €/MWh | sama | [V] |
| Kotimainen kapasiteetti erittäin kylmänä ja tyynenä | n. 11 700 MW | Fingrid, riittävyysarvio 2025–26 | [V] |
| Aurora Line käyttöön | 11/2025, SE1→FI 1 900 MW | Fingrid | [V] |
| Tuonti > vanha maksimi (1 200 MW) | 78 % ajasta | Fingrid | [V] |
| Talvi 2025–26 keskimääräistä lämpimämpi | Vantaa +2,2 °C, Kouvola +2,5 °C, Rovaniemi +3,4 °C vs. pitkä keskiarvo | Fingrid / IL | [V] |

### 2.2 Liittymisjono ja kysynnän kasvu

| Suure | Arvo | Lähde | Tila |
|---|---|---|---|
| Datakeskusten liittymissopimukset | ~5 GW | Fingrid, tiedote 18.8.2026 | [V] |
| Sähkökattilat | > 3 GW | sama | [V] |
| Varastot | > 4 GW | sama | [V] |
| Kulutuksen kasvuarvio jos kaikki toteutuu | jopa +40 % | sama | [V] |
| Rakenteilla olevan verkkoinvestoinnin tuoma lisäliityntäkapasiteetti | monin paikoin jo lähes varattu | sama | [V] |
| Liittymissopimus ei takaa toteutumista | Fingridin oma huomautus | sama | [V] |

### 2.3 SE1 ja Pohjola

| Suure | Arvo | Lähde | Tila |
|---|---|---|---|
| SE1-tase 2026 | +14 TWh | SvK, Kortsiktig marknadsanalys 2026–2030 | [V] |
| SE1-tase 2030 | −1 TWh (nettotuoja) | sama | [V] |
| Pohjolan ylijäämä 2026→2030 | 53 → 29 TWh | sama | [V] |
| Välivuodet 2027–2029 (+10,25 / +6,50 / +2,75) | DGIRP:n interpolaatio | v0.3 §4.1 | [P] |
| ENTSO-E Winter Outlook 2025–26 | FI, EE, LT ainoat mannermaan maat, joissa pieni riski poikkeuksellisen epäsuotuisissa oloissa | ENTSO-E | [V] |

### 2.4 Harjulinja

| Suure | Arvo | Lähde | Tila |
|---|---|---|---|
| Jännite | 400 + 110 kV | Fingrid | [V] |
| Päätepisteet | Murtoperä (P-Pohjanmaa) – Koria (Kymenlaakso) | HS 17.8.2026 | [V] |
| Päätepisteet (ristiriita) | Pyhäjärvi – Kouvola | DGIRP v0.3 §3.5 | [A] ristiriita ratkaisematta |
| Uutta johtoaluetta | 4 000–5 000 ha | HS | [V] |
| Rakentaminen | 2030–2032 | Fingrid | [V] |
| Reittipäätös | arviolta kesän 2027 jälkeen | v0.3 | [P] |
| Korialle rakennetaan datakeskus, loppukäyttäjä TikTok | — | HS | [V] |

### 2.5 Datakeskusjousto — pohjoismainen evidenssi

Lähde: Energiforsk 2025:1089, *Datacenter som flexibilitetskapacitet* (Petersson, Stark & Gustafsson, RISE, 2/2025). Kymmenen ruotsalaisen datakeskusomistajan haastattelut.

| Suure | Arvo | Tila |
|---|---|---|
| Ruotsi, asennettu/keskiteho (viitevuosi 2020, Radar/Energimyndigheten) | yrityskohtaiset 319/77 MW (24 %), hyperscale 99/70 MW (71 %), colocation 225/122 MW (54 %), krypto 200/180 MW (90 %) | [V] |
| Joustoskenaario ilman hyperscalereita (~20 % keskikuormasta) | 75 MW | [V] |
| Joustoskenaario hyperscalerit mukaan (~40 % osallistuminen) | 180 MW | [V] |
| Yksi SE1-datakeskus: esikvalifioitu FCR-D Up | 21,7 MW | [V] |
| Sama laitos: aktivoitu energia koko vuonna 2023 | 23 MWh | [V] |
| Tukipalveluita käytössä haastatteluhetkellä | 22 % vastaajista | [V] |
| Onboarding aloitettu | 44 % | [V] |
| FCR-D-korvaus loppuvuonna 2024 | n. 1/10 vuoden 2023 kuukausikeskiarvosta (akkuvarastojen tarjonnan kasvu) | [V] |
| Colocation-sopimusrajoite | ei yhtenäinen: osa noudattaa asiakkaan tahtoa, osa toimii yksipuolisesti | [V] |
| Suurimpien toimijoiden sitova rajoite | korvaustaso, ei sopimus | [V] |

### 2.6 Lämpönielu

Helenin rakenteilla / valmistuneet (helen.fi, hankesivu):

| Kohde | Sisältö | Tila |
|---|---|---|
| Hanasaari | 200 MW sähkökattilalaitos (4 × 50 MW); lämpövarasto 1 000 MWh, lataus/purku 100 MW; käyttöön lämmityskaudella 2026–27 | [V] |
| Patola | 2 × 50 MW sähkökattila + ilma-vesilämpöpumppu 20–33 MW (vaihtelee ulkoilman mukaan), CO2-kylmäaine; 2026–27 | [V] |
| Salmisaari | 2 × 50 MW sähkökattila + ilma-vesilämpöpumppu 14 MW; tuotanto alkoi lämmityskaudella 2025 | [V] |
| Eiranranta | lämpöpumppulaitos, kaukolämpöteho n. 90 MW; valmis alkuvuodesta 2026 | [V] |
| Yhteensä sähkökattilaa Helsingissä | 400 MW | [V] |
| Mustikkamaan varaston kesto pakkasella | n. 4 h | [V] |

### 2.7 Sääntely — liittyminen ja muutoksenhaku

| Kohde | Sisältö | Tila |
|---|---|---|
| Hankeluvan muutoksenhaku (kotimainen johto) | Energiavirasto → hallinto-oikeus (HOL 808/2019) → valituslupa KHO | [V] |
| Markkinaoikeus | käsittelee Energiaviraston vahvistus-/valvontapäätöksiä, ei hankelupia | [V] |
| Liittymisjohdon hankelupa | **on myönnettävä**, kun sähkönkäyttökohde, voimalaitoskokonaisuus tai energiavarasto liitetään lähimpään ≥110 kV verkkoon — sidottu päätös | [V] |
| Kunnan suostumus reitille | tarvitaan vain jos sijoitusoikeutta ei perusteta lunastuslain menettelyssä | [V] |
| Lunastuslupa | valtioneuvosto → valitus KHO:on, laillisuusvalitus (ei tarkoituksenmukaisuus) | [V] |
| Ennakkohaltuunottolupa | LunL 87 §: ei erikseen valituskelpoinen; KHO: raivaus ja maansiirto eivät peruuttamattomia → ei keskeytystä | [V] |
| Naapuri johtoalueen ulkopuolella | valvontaoikeus toimituksessa ≠ valitusoikeus lunastusluvasta | [A] |
| Suunniteltu priorisointilaki | sähkömarkkinalain muutos, esitys syyskaudella 2026 (Multala, HS 20.8.2026) | [V] |
| EU-rajoite | 2019/944: syrjimätön kolmannen osapuolen pääsy; Ruotsissa markkinaehtoinen hankinta ensin, ehdolliset sopimukset vain jos markkinaehtoinen puuttuu tai on ammennettu, menetelmä Ei:n ennakkohyväksyttävä | [V] |
| SvK liittymisprosessiraportti | 30.4.2026; valmistelee ehdollisia sopimuksia (*villkorade avtal*), vastasuorituksena velvoite rajoittaa ottoa/syöttöä ylikuormitusriskissä | [V] |
| Suomen tehoreservilaki (117/2011) | olemassa oleva strateginen reservi, hyväksyy myös kysyntäjouston — **ei tarkistettu tässä**: voimassa oleva hankintamäärä ja kriteerit | [P] |

### 2.8 Sääntely — datakeskusten raportointi

| Kohde | Sisältö | Tila |
|---|---|---|
| EU | Delegoitu asetus 2024/1364 (EED 2023/1791 art. 12): ≥500 kW IT-teho, 24 indikaattoria, EU-tietokanta, määräpäivä 15.5. vuosittain | [V] |
| Ruotsi | Lag 2025:570; tiedot salassa pidettäviä OSL 30:23 §:n nojalla, julkisia vain aggregoituna | [V] |
| Suomi | energiatehokkuuslaki, valvoja Energiavirasto, sääntelyn piirissä alustavasti n. 50 datakeskusta | [V] |
| Suomi — julkisuuden taso | HE: ≥500 kW datakeskusten on asetettava yleisesti saataville tieto **sijaintimaakunnastaan**; lisäksi säännökset Energiaviraston tiedonsaantioikeudesta | [V] |
| Energiateollisuus ry, lausunto 3/2026 | hukkalämmön hyötykäytön vaatimus on "liian vähäinen ja muodollisuus, josta vapautuu erittäin helposti"; kaukolämpöverkot Suomen uniikki kilpailuetu, johon laki ei vastaa | [V] |
| Vapautusperuste, jonka ET sanoo aukeavan liian helposti | **ei tarkistettu** — pykälä luettava | [P] |

---

## 3. Istunnossa tehdyt havainnot

Numerointi kritiikin vakavuuden mukaan.

### 3.1 α:n "korjaus" v0.3 → v0.4 on skaalaus, ei korjaus [A, laskettavissa]

v0.3 §4.1 johti α:n suoraan SE1:n vuosienergiataseesta: α = 0,70 kun tase +14 TWh, α = 0,20 kun tase −1 TWh. Suhde on lineaarinen, n. 0,0333 α-yksikköä per TWh, ja se kerrotaan NTC:llä 2 300 MW firm-tuontikapasiteetiksi.

v0.4 §6 väittää poistaneensa muunnoksen TWh → MW-firm.

Jaa v0.3:n α-arvot luvulla 0,70:

| Vuosi | v0.3 α | v0.3 α / 0,70 | v0.4 α |
|---|---|---|---|
| 2026 | 0,70 | 1,000 | 1,00 |
| 2027 | 0,575 | 0,821 | 0,82 |
| 2028 | 0,45 | 0,643 | 0,64 |
| 2029 | 0,325 | 0,464 | 0,45 |
| 2030 | 0,20 | 0,286 | 0,30 |
| 2032 | 0,15 | 0,214 | 0,20 |

Sama sarja normalisoituna vuoden 2026 arvolla. Muunnosta ei poistettu, se nimettiin uudelleen skenaarioindeksiksi. Metodologiakappale väittää korjanneensa asian, jota ei korjattu.

**Pyydetty tarkastus:** onko yllä oleva laskelma oikein. Jos on, v0.4 §2 ja §6 on kirjoitettava uudelleen.

### 3.2 v0.3:n RIILL-taulukko ei ole toistettavissa omista määritelmistään [A]

v0.3 §4.2 kaava ja lähtöarvot: F_domestic = 11 700, Import = α × 2 300, Flex = 0,15 × kulutus, PeakLoad_stress = kulutus × 1,1, P05 = keskiarvo × 0,88.

Havaitut poikkeamat:

- 2027, 0 MW: kaavasta P05 ≈ 0,790. Taulukossa 0,866. Ilman 1,1-kerrointa saadaan 0,869 — lähellä 2027:ää, muttei 2028:aa (kaava 0,853, taulukko 0,829).
- Kuormaherkkyys: taulukko putoaa n. 0,019 per 250 MW, kaava antaa n. 0,012.
- Monotonisuus väärin: 2029→2032 tuonti putoaa enemmän (−403 MW) kuin 2028→2029 (−287 MW), mutta RIILL putoaa vähemmän (−0,024 vs −0,037).

Viimeinen kohta on riippumaton siitä, mitä kaavaa käytettiin: suunta on väärä.

**Pyydetty tarkastus:** toista taulukko. Jos et pysty, se on vedettävä pois tai laskenta julkaistava.

### 3.3 Koko Red/Black-tulos riippuu yhdestä lukuvalinnasta [A]

11 700 MW (stressiarvio) vs. 14 320 MW (toteutunut kotimainen tuotanto huipputunnilla, −19 °C). Ero 2 620 MW = 22 %.

−19 °C painotettu lämpötila on aito pakkashuippu, ei leuto tunti. v0.3 §3.1 perustelee konservatiivisuutta sillä, että talvi oli keskimäärin lämmin — mutta se vertaa kausikeskiarvoa yksittäiseen tuntiin.

Jos F_domestic = 14 320, osoittaja kasvaa n. 0,15 ja lähes jokainen solu nousee luokan.

Ratkaisematta: mikä osuus 14 320 MW:sta oli tuulta, mikä oli huoltotilanne, ja mitä Fingridin 11 700 MW olettaa tuulesta ja käytettävyydestä. Ilman tätä erottelua kumpaakaan lukua ei voi käyttää.

**Pyydetty tarkastus:** onko 11 700 ja 14 320 saatettavissa samalle perustalle julkisesta aineistosta.

### 3.4 Stressikerroin on väärässä paikassa [A]

v0.4 §9: (15 553 + 743) × 1,10.

Kerroin 1,10 kuvaa sään aiheuttamaa kulutuksen nousua eli lämmityskuormaa. Datakeskuksen kuorma on lämpötilariippumaton; pakkasella jäähdytystehontarve päinvastoin laskee.

Oikea muoto: 15 553 × 1,10 + 743.

Vaikutus: 817 MW → 743 MW, otsikkoluku paisuu 74 MW. Käsitteellisesti pahempi: kuorman jäykkyys on juuri se ominaisuus, jota DGIRP mittaa, ja tässä se on mallinnettu joustavaksi.

### 3.5 Kysyntäjousto on väärällä puolella murtoviivaa [A]

v0.4 §8.2 lisää F_project-flex osoittajaan. Kysyntäjousto on kuorman vähennys, ei kapasiteetin lisäys:

    (F + 372) / 17 926  ≠  F / (17 926 − 372)

Oma tuotanto (F_project-firm) kuuluu osoittajaan, leikkaus nimittäjään. Nykyisellään RIILL_P sekoittaa kaksi fysikaalisesti eri asiaa samaan termiin, ja luokkarajat kalibroituvat väärin.

### 3.6 Nolla-kuorma on Red 2029 — mittarin reductio [A]

v0.3 §5 johtopäätös 1: nykytilanne ilman uutta kuormaa on Red 2029. Johtopäätös 4: mikään kuorma ei yllä Green- tai Amber-luokkaan koko tarkasteluvälillä.

ENTSO-E sanoo samasta järjestelmästä: pieni riski poikkeuksellisen epäsuotuisissa olosuhteissa.

Indeksi, jonka nollatapaus jo hylkää, ei erottele hankkeita — se mittaa raja-arvojen valintaa. Rajat on kalibroitava nollatapausta vastaan tai indeksillä ei ole päätösarvoa.

### 3.7 Kuorma ja siirtoyhteys ovat sama hanke [A]

Harjulinja päättyy Korialle, jonne rakennetaan datakeskusta; 743 MW on Kouvolan klusteri. DGIRP käsittelee linjaa eksogeenisena verkkomuuttujana ja kuormaa eksogeenisena kuormamuuttujana, vaikka linja on todennäköisesti mitoitettu tämä kuorma mukana. Sama asia lasketaan kahdesti: ensin riskinä, sitten ratkaisuna.

### 3.8 BPH edellyttää tuntitason RIILL:iä, jota ei ole määritelty [A]

v0.4 §16 ja §19 laskevat tunteja, joina RIILL_P < 0,85. §8 rakentaa suhdeluvun yhdestä stressihuipusta. Yhden skenaarion tunnusluvusta ei voi laskea tuntijakaumaa. Tarvitaan RIILL(t) tuntikohtaisella kuormalla ja tuntikohtaisella käytettävissä olevalla kapasiteetilla.

### 3.9 Joustoskenaariot ovat ristiriidassa oman lähdepohjan kanssa [A]

v0.4 §12 tarjoaa joustotasot 25 / 50 / 75 %. SM-009 §11:n oma lähde (Energiforsk 2025:1089) antaa ~20 % keskikuormasta vaatimattomilla teknisillä toimilla, kansallisesti 75–180 MW, ja esikvalifioitu 21,7 MW tuotti 23 MWh koko vuonna 2023.

50 % ja 75 % eivät ole skenaarioita vaan vastoin omaa aineistoa. Rajaus 0–25 %, ylitykset perusteltava erikseen omalla tuotannolla.

### 3.10 743 MW:n alkuperä on ilmoittamatta [A]

Liittymissopimus, YVA vai koottu arvio. Ilman lähdettä koko muistio näyttää siltä kuin luku olisi vahvistettu.

### 3.11 Monte Carlo riippumattomista marginaaleista hävittää riskin [A]

v0.4 §22.4 esittää 10 000 skenaariota, joissa vaihtelevat lämpötila, tuuli, vesitilanne jne. Jos nämä otetaan riippumattomista marginaalijakaumista, tuhoutuu juuri se korrelaatiorakenne joka **on** riski: kylmä ja tyyni esiintyvät yhdessä, ja Suomen, Ruotsin ja Norjan kylmä esiintyy yhdessä — siksi tuonti pettää täsmälleen silloin kun sitä tarvitaan.

Vaihtoehto: fysikaalisesti yhtenäinen uusintaotanta ERA5:stä (Copernicus Climate Data Store; tunneittainen 2 m lämpötila ja 100 m tuuli vuodesta 1940, n. 31 km hila, maksuton). Polku:

1. Regressoi Fingridin tuntikulutus lämpötilaa vastaan.
2. Aja regressio kaikkien ERA5-talvien yli → empiirinen jakauma huippukuormasta. Tämä korvaa kertoimen 1,10 mitatulla luvulla.
3. Samat kentät antavat SE1:n ja Norjan kuorman sekä koko Pohjolan tuulen samanaikaisesti → korreloitu tuontimarginaali ilman α-skenaariota.
4. Tarkista C3S Energy -indikaattorit ennen omaa toteutusta (valmiit ERA5-johdetut maakohtaiset kysyntä- ja kapasiteettikerroinaikasarjat).

Rajoite: n. 46 talvea antaa ehkä 2–3 aitoa ääripakkasjaksoa. P05 on sillä otoksella puolustettavissa, P01 ei.

### 3.12 SM-009 §11: salassapidon kohde on väärin nimetty Ruotsin osalta, oikein Suomen osalta [A]

Ruotsi: OSL 30:23 § on yleinen liikesalaisuussäännös, joka koskee kaikkea yritystason energiadataa. Aggregointi on tilastosalaisuuden vakiokäytäntö. Viranomainen (Energimyndigheten) **näkee** datan. Väite "suljettu niiltä instituutioilta, jotka sitä käyttäisivät" ei pidä paikkaansa; sulkeminen kohdistuu yleisöön ja tutkimukseen. "Aktiivinen oikeudellinen konstruktio" väittää motiivia, jota ei voi näyttää toteen.

Suomi: julkisuuden alaraja on kirjoitettu erityislakiin ja asetettu **maakuntatasolle**. Se on lainsäätäjän valinta, ei tilastosalaisuuden sivutuote. §11:n väite pätee Suomessa, vaikka ei päde Ruotsissa.

**Korjaus:** rajaa väite Suomeen ja kohdista se julkisuuteen ja tutkimukseen, ei päätöksentekoon.

### 3.13 SM-009 §11: väite tarvittavasta granulariteetista on liikaa [A]

§11 väittää, että laitostason data on "juuri sitä granulariteettia, jota kapasiteettimekanismi tarvitsisi". Kapasiteettimekanismi ei tarvitse laitostason tietokantaa vaan esikvalifiointia, jonka toimija toimittaa itse silloin kun haluaa korvauksen. Oma aineisto todistaa tämän: Radar/Energimyndigheten 2023:n MW-luvut olivat julkisia ja riittivät Energiforskille skenaarioiden laskemiseen.

### 3.14 SM-009 §11: keskeisin numero on haudattu [A]

21,7 MW esikvalifioitua → 23 MWh aktivoitua koko vuonna 2023 on noin tunti yhdellä megawatilla. Se on empiirinen kumoaminen väitteelle "datakeskukset ovat jo joustavia". Nyt se on kappaleen keskellä tukiaineistona.

Sama koskee lukuja 75–180 MW: keskustelun lähtökohta oli 1,2–2 GW muunnettavaa kapasiteettia. Ero on kertaluokka. Kirjoita se tulokseksi.

### 3.15 CN-007: malli ennustaa väärin sähkökattilat [A]

Kolmen vajeen malli selittää kapasiteettimekanismin viivästymisen, mutta ennustaa väärin sen, että Helsinkiin rakennettiin 400 MW sähkökattilaa ja kansallisesti > 3 GW ilman yhtään politiikkainstrumenttia — pelkällä tuntihintavolatiliteetilla ja polttoaineen välttämisellä.

Ehdotettu kaventaminen: mittaus- ja sanktiovaje sitovat vain siellä, missä korjaavalla toimella ei ole omistajaa, joka hyötyy siitä yksin. Sähkökattilalla on yksityinen kassavirta, tehoreservillä ei.

Falsifiointitesti: etsi tapaus, jossa toimenpiteellä oli selvä yksityinen tuotto ja se silti jäi tekemättä vuosikausiksi. Jos löytyy, kaventaminen ei riitä.

### 3.16 Pienet [A]

- v0.3 §3.5 Pyhäjärvi–Kouvola vs. HS Murtoperä–Koria. Ratkaistava.
- NTC 2 300 MW (v0.3 §4.1) vs. Aurora Line 1 900 MW SE1→FI. Mistä 400 MW:n ero, ja onko se firm.
- SM-009 §11 runko: "Svensk Näringsliv", oikein "Svenskt Näringsliv".
- v0.4 §7 määrittelee α:n mutta yksikään kaava ei käytä sitä. Joko F_import(t) = F_import,base × α(t) tai poista.

---

## 4. Rakenteellinen huomio

v0.3 → v0.4 -siirtymässä poistettiin numerot ja jätettiin kehys. Se tekee muistiosta vaikeammin falsifioitavan, ei paremman: v0.4 esittää hypoteesin, jota ei voi testata, koska ainoa versio jossa oli lukuja, ei ollut toistettavissa (3.2).

Vaihtoehdot: palauta luvut korjattuina, tai vedä v0.3:n taulukko julkisesti pois.

---

## 5. Avoimet kysymykset, joita ei tässä istunnossa ratkaistu

1. Mikä osuus Fingridin 14 320 MW:sta oli tuulta huipputunnilla, ja mitä 11 700 MW olettaa.
2. Onko Fingridin riittävyysarvion kapasiteetti jo verrattu Fingridin omaan stressihuippuun — jos on, 1,10-kerroin kertoo stressin kahdesti.
3. Mistä 743 MW on peräisin.
4. Tehoreservilain (117/2011) voimassa oleva hankintamäärä ja hyväksymiskriteerit.
5. Energiatehokkuuslain hukkalämpövelvoitteen vapautusperuste, jonka Energiateollisuus sanoo aukeavan liian helposti.
6. Onko maaliskuun 2026 energiatehokkuuslain muutosesitys annettu ja mitä hukkalämpöpykälästä tuli.
7. Liittymissopimusten raukeamisehdot ja vakuudet — ilman use-it-or-lose-it -ehtoa verkon hitaus ei rajoita datakeskuksia, vain muita.
8. Irlanti (CRU, Dublin): mikä osuus hakijoista täytti dispatchable-vaatimuksen, mikä vetäytyi, rakennettiinko yhtään yksikköä. Ainoa olemassa oleva koe dispatchable-velvoitteesta.
9. Suomen priorisointilakiesityksen soveltamisala: jos se rajautuu tietyn päivän jälkeen jätettyihin hakemuksiin, laki koskee vain jäännöstä jo jaetusta jonosta.

---

## 6. Mitä ei pyydetä

Ei arviota siitä, onko DGIRP kiinnostava kehys. Ei ehdotuksia laajentaa kehystä. Ei uusia mittareita.

Pyydetään: mitkä §3:n väitteistä ovat vääriä, ja mitä §3:sta puuttuu.
