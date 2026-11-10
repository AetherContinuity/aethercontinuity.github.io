# Löydökset 10.11.2026

**Kotimainen energia- ja polttoainetuotanto voimavarana: mitä haettiin, mitä laskettiin, mikä jäi auki.**

Istunnon muisti. Jokainen laskettu luku on jäljitettävissä tallennettuun aineistoon:

    tools/data/da-fi-2025-11_2026-10.json     4f80f0f3c713   day-ahead FI, 15 min, 35 040 pistettä
    tools/data/wind-fi-2025-11_2026-10.json   9f2a35c630a0   maatuuli FI, 15 min, 35 040 pistettä
    tools/data/da-se1-2025-11_2026-10.json    e4c0a2bd5046   day-ahead SE1, 15 min, 35 040 pistettä
    tools/data/rp-244-talvi-2025-2026.json    527f60ca2a97   ylössäätöhinta (aiempi aineisto)
    tools/laskenta/                           skriptit; ajetaan hakemistosta tools/laskenta, lukevat ../data

Merkinnät: [M] mitattu tai julkaistu, [L] laskettu, [A] arvio tai oletus.

---

## 1 · Hintajakauma 1.11.2025–31.10.2026

    keskihinta        54,8 €/MWh   [L]
    mediaani          32,5
    min / max        −10,9 / 654,9
    ≤ 0 €              1,5 % varteista
    ≤ 5 €             14,8 %
    ≥ 100 €           19,6 %
    ≥ 200 €            2,6 %

    halvimmat 1000 h    1,8      kalleimmat 100 h   341,3
    halvimmat 3000 h    7,4      kalleimmat 500 h   220,7
    halvimmat 5000 h   15,9      kalleimmat 1000 h  181,3

Tarkiste: 17.1.–17.2.2026 keskihinta 158 €/MWh, SM-020:ssa 159.

Jakso sisältää kylmän talven. Vuoden 2025 kalenterivuoden keskihinta oli
40,5 €/MWh [M, Turku Energia]. Tuloksia ei pidä lukea normaalivuotena.

---

## 2 · TN-022 §05 ei kestä

S-2-solmun lisäkate hakelämpölaitokseen verrattuna, toteutuneilla hinnoilla.
Oletukset [A]: PEM 20 MW, hyötysuhde 65 % × 78 %, lämmön talteenotto 30 %,
moottori 45 % sähköä / 40 % lämpöä, siirto ja vero 5 €/MWh, CO2 50 €/t,
vältetty hakelämpö 30 €/MWh, kiinteä käyttökulu 2,7 M€/v, reservitulo
1,5 M€/v (WP-019), lisäinvestointi 90 M€, 6 %, 20 v → 7,8 M€/v.
Varasto rajoittamaton ja ennakointi täydellinen: tulos on yläraja.

    elektrolyysi h   sähkö GWh   SNG GWh   moottori h   lisäkate   pääomakulun jälkeen
        2000             40        20,3        456       +0,9 M€       −6,9 M€
        4000             80        40,6        913       +1,7          −6,2
        5000            100        50,7       1141       +1,7          −6,2
        8760            175        88,8       1999       −4,2         −12,0

TN-022 väittää EBITDA 35–60 M€/v ja takaisinmaksu 2,4–3,1 v. Kaksi virhettä:

- **Fyysinen:** "fossiilisen polttoaineen korvaus" 15–35 M€ @ 70 €/MWh
  edellyttää 214–500 GWh polttoainetta. 20 MW:n PEM tuottaa enintään 89 GWh.
- **Kirjanpidollinen:** elektrolyysin sähkö on rajattu soveltamisalan
  ulkopuolelle. EBITDA on liikevaihto plus vältetty kustannus ilman kuluja.

Vertailukohta on lisäksi maakaasu, vaikka suomalainen kaukolämpö polttaa
haketta. WP-019:n IRR on sidottu TTF:ään samalla virheellä, ja WP-019 §08
toteaa itse solmun olevan perus-TTF:llä "marginally uneconomic".

**Sähköstä sähköksi 23 %. Kesto syntyy varastosta, ei synteesistä.**

---

## 3 · Moottorivoimala ei kannata hintapiikeillä

Hyötysuhde 45 %, muuttuva käyttökulu 8 €/MWh [A]. Pääoma 1000 €/kW, 6 %,
20 v → 87 €/kW/v, kiinteä käyttökulu noin 20 → **107 €/kW/v** [A].

    polttoaine €/MWh         rajakust.   h/v     day-ahead-kate
    LNG 45                     108       1441      77 €/kW/v
    LNG 45 + päästöoikeus      141        761      42
    biometaani 90              208        190      15
    biometaani 120             275         73       7

Talvi 1.11.2025–31.3.2026, yläraja max(day-ahead, ylössäätö DS 244):

    LNG 45 + päästöoikeus      787 h     64 €/kW

Kate ei kata pääomaa edes kalliina talvena. Rakentamista ajaa jokin muu:

- **omistajan suojaus** (EPV on Mankala-yhtiö; osakkaat suojaavat omaa
  vähittäismyyntiään), tai
- **sääntö:** Polarnoden 200 MW:n LNG-voimala on mitoitettu etusijalain
  80 %:n joustorajaan (kuopio-seuranta.json, K1).

Biometaani säätövoimalassa ei synny markkinaehtoisesti. Se vaatisi
velvoitteen.

---

## 4 · Tuuli syö oman hintansa: mitattu

    tuulituotanto           21,9 TWh, keskiteho 2 497 MW   [M]
    keskihinta              54,8 €/MWh
    tuulen saama hinta      33,9 €/MWh                     [L]
    suhde                   0,62
    korrelaatio hinta–tuuli r = −0,479

    tyynin neljännes        447 MW     97,2 €
    toinen                1 502 MW     65,0 €
    kolmas                2 998 MW     38,1 €
    tuulisin neljännes    5 039 MW     19,1 €

Hinta on tyynimmässä neljänneksessä viisinkertainen tuulisimpaan nähden.
Uusi tuuli tuottaa halpaa sähköä kuluttajalle, ei ylituottoa omistajalle.
Vuokra on säätökyvyssä.

---

## 5 · Kuopion hiili

Yhdistetty co2-lahteet-fi-2024.json ja kuopio-seuranta.json:

    Volaghy eSAF, CO2-tarve                 250 kt/a   [M, YVA-ohjelma]
    Mondi Sorsasalo, biogeeninen 2024       153 kt     [L, E-PRTR]
    vaje                                    ~100 kt
    Haapaniemi, biogeeninen                 350–400 kt [A]
    Haapaniemi 2 poistuu                    ~2035      [M]

Kaupunki omistaa alueen suurimman biogeenisen hiilen lähteen ja korvaa sen
reaktorilla, joka ei tuota hiiltä, samaan aikaan kun sen kaavoittamalle
alueelle suunnitellaan 750 M€:n laitosta, jolta hiili loppuu kesken.
K1–K5 eivät kata tätä. Ehdokas K6:ksi.

---

## 6 · Korpuksen sisäiset ristiriidat

- **CHP ja reservit.** SM-008 ja WP-019 laskevat CHP:lle reservituloa.
  loydokset-2026-09.md §2: CHP on lämpöohjattu eikä ole tarjouskirjassa
  (r = −0,671).
- **LDR-50:n hinta.** SM-008: 300–500 M€/yksikkö. TN-022: 150–300 M€.
  Kuopion Energia: noin 200 M€ kahdelle.
- **Suomen Lantakaasu.** TN-017 §06.5: 21 viljelijän osuuskunta.
  Todellisuudessa Valion ja St1 Biokraftin 50/50-yhteisyritys [M, St1].
  St1 Biokraftin omistavat St1 (50 %), HitecVision ja Aneo. Investoinnista
  noin 100 M€:sta 19,2 M€ on RRF-tukea.
- **SM-003:n Kuopio-solmu.** Kuopion Energia ei aio jatkaa sähköntuotantoa.
  Viitesolmu on kontrafaktuaali.

---

## 7 · Ulkoiset luvut

**Biokaasu** [M, Suomen Biokierto ja Biokaasu ry]

    tuotanto 2023            920 GWh (biometaani 243, biokaasu 676)
    kulutus 2024           1 300 GWh
    kulutus 2025 (arvio)   2 300 GWh
    biometaanin tuonti       240 (2023) → 400 (2024) → 1 300 GWh (2025)
    vireillä                 39 hanketta, 1 769 GWh, josta LBG 1 368

**Velvoite loi kysynnän, ja tuonti täytti sen.** Vuonna 2025 tuotu
biometaani ylitti kotimaisen tuotannon. Tuojamaat Tanska, Ranska ja
Alankomaat.

**Energian ulkomaankauppa 2025** [M, Tilastokeskus ennakko]

    tuonti 10,0 mrd €, vienti 5,6 mrd € → netto noin 4,4 mrd €

**Jakeluvelvoite** [M]: 19,5 % (2026), 22,5 % (2027), 31 % (2028), 34 % (2030).
RFNBO-velvoite 1,5 %-yks. 2028–2029, 4 %-yks. 2030. Tasoja on muutettu
2022 ja 2024; lisävelvoite laskettiin 6 → 4 %-yks.

**Kuntakaupat** [M]

    Pori Energia 49 % → Polhem Infra (2025)     366 M€; yritysarvo 905 M€
        liikevoitto 20,8 M€ (2024), 18,7 M€ (2025)
        → yritysarvo / liikevoitto noin 44
    Etelä-Savon Energia 49 % → abrdn (2024)     130 M€ + lisäosinko 31 M€
        + konsernilainojen takaisinmaksu 28 M€
    Parainen, kaukolämpö 75 % → Adven (2023)    osakassopimus rajasi
        vuoden 2025 korotuksen 7 %:iin; Adven esitti 13 %

**Porin kauppa ei tue väitettä, että kunta häviää rahassa.** 366 M€
kuuden prosentin tuotolla on 22 M€/v. 49 % noin 20 M€:n liikevoitosta on
noin 10 M€/v ennen korkoja ja veroja. Ostaja maksoi 44-kertaisen
liikevoiton, mikä on perusteltavissa vain odotuksella hintojen ja
säännellyn tuoton kasvusta. Maksaja on silloin asiakas, ei kaupunki.
Menetys on määräysvalta hinnoitteluun, ei kassavirta. CN-028:n pääväite
(operatiivinen veto-oikeus) pitää; rahallinen tappio-oletus ei.

---

## 8 · Mitä jäi auki

- **CN-028:n kauppalista.** Paperissa ei ole kauppakohtaista taulukkoa.
  Väite "Tampere, Kajaani, Lappeenranta, Hämeenlinna → Elenia" on
  tarkistamatta, ja Tampereen osalta epäilyttävä.
- **Mikkelin velkajärjestely.** Väite konsernivelan sadan miljoonan
  kasvusta on yhden blogikirjoituksen varassa. Tarkistettava tilinpäätöksestä.
- **Biokaasun tuotanto 2024 ja 2025.** Kulutus ja tuonti löytyivät,
  tuotantoa ei.
- **Normaalivuosi.** Kohdat 2–4 pitää ajaa myös kalenterivuodelle 2025.
- **Varaston koko.** TN-022-laskelma olettaa rajattoman varaston.
- **Kuopion kesäminimi MW.** Ei julkaistu (kuopio-seuranta.json).
- **Teknologiavienti.** Mittaria ei ole määritelty.

---

## 9 · Menetelmähavainto

Neljä istunnon väitettä kaatui, kun ne laskettiin: moottorien
kannattavuus piikeillä, biokaasu säätövoimaloissa, kunnan rahallinen
tappio myynnissä ja "PtX:stä ei löydy tietoa". Kaksi vahvistui: TN-022:n
kate ja tuulen kannibalisaatio. **Arvio ja laskelma erosivat suunnaltaan
vain siellä, missä arvio perustui periaatteeseen eikä lukuun.**

---

## 10 · Lisäys: tilannekuva 10.11.2026 klo 15.45

Day-ahead-hinnat vartilla 15.45–16.00 (ENTSO-E A44; samat luvut kuin SvK:n
kontrollihuoneen kartassa):

    SE1    91,06 €/MWh
    FI     99,08
    SE3   347,19
    EE    530,74
    PL    858,40

    vuorokauden keskihinnat: FI 107,8 · SE1 54,1 · SE3 275,3 · EE 305,1 · PL 459,5
    FI–EE-hintaero yli 1 €: 82/96 varttia, suurin ero 475 €

Suomi oli halpa lenkki kalliiden alueiden välissä ja toimi siirtoreittinä.
Fingridin mittaus klo 15.45 (+ vienti, − tuonti): EstLink +1 016 MW (DS 140),
FI–SE3 −433 MW (DS 61), FI–SE1 noin −1 750…−1 900 MW (DS 87). Sähkö virtasi
siis SE3:sta Suomeen, vaikka SE3:n hinta oli 248 € Suomea korkeampi: hintaeroa
vastaan kulkeva virta, joka on mahdollinen flow-based-laskennassa. Syytä ei
ole selvitetty. Hintaero FI–EE 432 € × 1 016 MW on noin
440 000 € pullonkaulatuloa tunnissa, joka jaetaan Fingridin ja Eleringin
kesken. Niukka tekijä on siirtoyhteys, ja sen vuokra kertyy verkonhaltijalle.
Illalla FI nousi EE:n tasolle (klo 19: 322,5 vs. 322,9), eli sama yhteys
toi Manner-Euroopan hinnan Suomeen heti kun pullonkaula lakkasi sitomasta.

Ennakkokirjaukset F1–F3 (SEURANTA.md) tehtiin samana päivänä.

**Euroopan aikataulu** [M, asetus (EU) 2026/261]: venäläisen LNG:n
pitkäaikaiset sopimukset kielletään 1.1.2027, putkikaasun 30.9.2027
(viimeistään 1.11.2027). 1.1.2027 on sama päivä, jona Meri-Pori siirtyy
markkinalle (F1).

---

## 11 · Energian paino kotitalouksien taloudessa

Aineisto: `kotitalouksien-energiamenot-2012-2026.json` (7a975363926e). [M] Tilastokeskus.

**Osuus kulutusmenoista 2022** (Kulutustutkimus; sähkö, kaasu ja muut
polttoaineet 04.5 + ajoneuvopolttoaineet 07.2.2):

    kaikki            7,5 %   (2 993 €/v)
    I pienituloisin   6,2 %   (1 212 €)
    II                8,2 %
    III               7,4 %
    IV                8,3 %
    V suurituloisin   7,1 %   (4 606 €)

    2012: 7,6 %  ·  2016: 6,4 %  ·  2022: 7,5 %

Osuus on pienin pienituloisimmalla viidenneksellä, ei suurin. Syy on
mittaustapa: kerrostalon lämpö sisältyy vuokraan ja vastikkeeseen eikä
kirjaudu energiaksi, ja autottomia on enemmän. Asumisen koko pääryhmä (04)
näyttää eron: I 38,6 %, V 30,0 %. Energian hinta osuu pienituloiseen
asumiskulun kautta ja viiveellä, ei energialaskuna.

**Hintamuutos, vuoden 2021 keskiarvo → 10/2025–9/2026** (KHI):

    kokonaisindeksi                +17,4 %
    sähkö                          +20,5 %   (huippu 2023: +46 %)
    muu lämpö (kaukolämpö)         +29,3 %   (noussut joka vuosi)
    ajoneuvopolttoaineet           +17,0 %   (viim. 12 kk +13 % vuodesta 2025)

Sähkö ja polttoaineet ovat palanneet yleisen hintatason tuntumaan.
Kaukolämpö on ainoa, joka on kallistunut reaalisesti (noin +10 %) ja ilman
laskuvaihetta. Se on myös ainoa, jossa asiakas ei voi vaihtaa toimittajaa.

KHI:n painot 2026: 04.5 on 50,2 ‰ ja 07.2.2 on 30,1 ‰, yhteensä noin 8 %.

Rajoitukset: Kulutustutkimus on tehty viimeksi 2022, joten tuloluokittaista
tietoa hintahuipun jälkeen ei ole. Keskiarvo peittää pörssisähköasiakkaan
ja sähkölämmittäjän talvikuukaudet.
