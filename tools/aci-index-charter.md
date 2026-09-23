# ACI-indeksicharteri v0.1

Charterin tehtävä: jokainen instrumentti vastaa samoihin kysymyksiin yhdessä paikassa,
ennen kuin live-lukemia luetaan kynnysluokkina. Tähän kirjataan myös tehdyt päätökset ja
kaavamuutokset, koska ne katkaisevat aikasarjan.

Laadittu 23.9.2026 ulkopuolisen tarkastuksen pohjalta. **Jokainen tämän tiedoston väite on
tarkistettu instrumenttien koodista, ei PDF-tulosteista.** Tarkistusmerkintä on kunkin kohdan lopussa.

---

## HEM — Hydrological Endurance Monitor

**§0 Identiteetti.** Mittaa Iisveden vedenkorkeusvajetta ja hydrologista kuormitusta. Dimensioton [0,1].
Aikavakio: kuukausi (komponentit), NVE viikko. Abstraktiotaso: fyysinen (m NN, m³/s) → synteettinen.
Ei ennuste, ei operatiivinen hälytys.

**§1 Aggregointi.** Additiivinen: `HEPP = 0,35·SD + 0,25·EP + 0,25·RF + 0,15·HSP`. Painot summautuvat
1,00, joten asteikko on saavutettavissa. Kynnykset 0,45 ja 0,65 sopivat muotoon.

**§2 Komponentit.**

| Komponentti | Lähde | Kaava | Aikavakio | Paino | Fallback |
|---|---|---|---|---|---|
| SD | SYKE Hydrologiarajapinta, asema 1966 | SD_nyt = (saman vuodenpäivän normaali − havaittu)/0,90 | vrk→kk | 0,35 | SD_kevät, jos SD_nyt puuttuu |
| EP | FMI Kuopio | Thornthwaite-PET, anomalia vs. 1961–2010 | kk | 0,25 | 0,30 jos <12 kk dataa |
| RF | FMI Kuopio (sadanta) tai virtaama | 1 − (sade/mediaani); v. 2026-09 alkaen ensisijaisesti Q/saman vuodenpäivän mediaani (Nokisenkoski 1005) | kk | 0,25 | sadantaversio |
| HSP | NVE Magasinstatistikk | label low 0,70 / normal 0,38 / high 0,15 | viikko | 0,15 | — |

**§3 Kynnykset.** 0,45 (Elevated) ja 0,65 (High). **Alkuperä dokumentoimaton, todennäköisesti a priori.**
Odotettua osuutta luokissa ei ole määritelty.

**§4 Vertailusarja.** SD:n vertailutaso **päätetty 22.9.2026**: ensisijainen on saman vuodenpäivän normaali
(1991–2020), jolloin SD on kausikorjattu; kevään huippuun perustuva SD_kevät näytetään erikseen
(vertailutaso 98,01 m = keskimääräinen vuotuinen maksimi 1910–2025). Aiempi laskenta vertasi syksyn
lukemaa kevään huippuun ja nosti HEPP:iä mekaanisesti läpi syksyn. *(Tarkistettu koodista:
`if(iis?.sdNyt!=null)sd=iis.sdNyt;`)*
**Avoin:** §05:n historiallinen HEPP-sarja 1959–2026 on laskettu ilman SD- ja HSP-komponentteja
(vain FMI + Thornthwaite), joten live-arvoa ei voi verrata sen kynnyksiin. Uudelleenlaskenta SYKE:n
pitkästä sarjasta on tehtävä ennen kuin sarjaa käytetään vertailuun.
**Avoin:** SD:n jakaja 0,90 m on dokumentoimaton. Se on skaalausvakio, ei mitattu hajonta.

**§5 Nollajakauma.** Puuttuu. Tarvitaan HEPP tunnetusti normaalilta, kuivalta ja märältä vuodelta samalla kaavalla.

**§6 Rajoitteet.**
1. §05-sarja ei vertailukelpoinen live-arvon kanssa (pysyvä, kunnes uudelleen laskettu; vaikuttaa tulkintaan).
2. Nimikollisio: RF (sadantakomponentti) ja NVE:n hydro_RF (vesivoimakerroin FS(p):ssä) ovat eri suureita.
   Nimet on erotettava. (vaikuttaa tulkintaan)
3. Muonion §02b: nollakohta puuttuu, osio ei toimi. Asema on tiedossa (Paikka_Id 2532).
4. SD:n jakaja dokumentoimaton.

**§7 Muutosloki.** 22.9.2026 SD_nyt ensisijaiseksi, havaittu vedenkorkeus ennusteen tilalle, NN-nollakohta
96,88 m luettuna VedenkTasoTieto-taulusta. 22.9.2026 §00: mitattu taso, saman vuodenpäivän normaali,
tulo- ja lähtövirtaama, kausitrendit (data/hem-iisvesi-normals-trends.json).

---

## BEM — Biodiversity Endurance Monitor

**§0 Identiteetti.** Mittaa valuma-alueen ekologista kuormitusta. Dimensioton [0,1]. Aikavakio: vuosi.
Abstraktiotaso: synteettinen.

**§1 Aggregointi.** **Kertova:** `BEPP = D_f^1,2 · D_s^1,0 · D_c^0,8 · (1−R)^1,5`.
*(Tarkistettu koodista, rivi 448.)*
**⚠ Asteikko ei ole saavutettavissa.** Koska D_s, D_c ≤ 1 ja R ≥ 0, pätee BEPP ≤ D_f^1,2.
D_f = 0,6·(1−metsäosuus) + 0,4·min(1, NDVI-hajonta/0,30). Metsäosuudella 65 % ja hajonnalla 0,234
D_f = 0,522 ja **katto 0,458**. Luokat Critical (≥0,50) ja BP-like (≥0,75) ovat siis aritmeettisesti
ulottumattomissa. D_f:ää rajaa lisäksi CORINE, joka päivittyy muutaman vuoden välein.
Katto näytetään 23.9.2026 alkaen BEPP-luvun vieressä.
**Eksponentit 1,2 / 1,0 / 0,8 ja (1−R)^1,5 ovat dokumentoimattomia.** Ne ovat perheen ainoat
perustelemattomat painot.

**§2 Komponentit.** D_f (CORINE + Sentinel-2 NDVI-hajonta, live), D_s (FinBIF, live), R (FinBIF, live),
D_c (tallennettu aineisto data/bem-dc-2004-2025.json). D_c:n fallback on kiinteä arvo 0,318, jos tiedosto ei lataudu.

**§3 Kynnykset.** 0,25 / 0,50 / 0,75. Alkuperä dokumentoimaton; asetettu olettaen vapaasti varioivat komponentit (ks. §1).

**§4 Vertailusarja.** SERIES 2010 → 2018 → 2026. D_c on laskettu samalla kaavalla kaikille, mutta
**vuosien 2010 ja 2018 arvot ovat aliarvioita**, koska palautuvan komponentin 20 vuoden ikkuna täyttyy
vasta 2023 (ilmoitusaineisto alkaa 2004). Siksi dS/dt (2018→2026) yliarvioi D_c:n kasvua. Merkitty sivulle.

**§5 Nollajakauma.** Puuttuu. Ei tiedetä, mikä BEPP olisi ollut esimerkiksi 1990-luvulla.

**§6 Rajoitteet.**
1. Kynnykset ulottumattomissa (pysyvä, kunnes muoto tai kynnykset muutetaan; vaikuttaa tulkintaan).
2. dS/dt osittain artefakti (väliaikainen, korjautuu 2043 tai ikkunaa lyhentämällä).
3. D_f on approksimaatio, ei validoitu fragmentaatiomittausta vasten.
4. R:n otos pieni.
5. D_c:n pysyvä komponentti perustuu 6 ruudun otantaan, 95 %:n LV 0,15–0,67 % maa-alasta.

**§7 Muutosloki.** 21.9.2026 D_c kahtena komponenttina, normalisointi
`D_c = 0,5·min(1, palautuva%/20) + 0,5·min(1, pysyvä%/2)` [A]; D_c 0,61 → 0,318, BEPP 0,066 → 0,039.
22.9.2026 §03b säteily ja §03c ilmakehän kaasut taustatietona (ei BEPP-vaikutusta).
23.9.2026 saavutettava maksimi näkyviin.

---

## WEM — Winter Endurance Monitor

**§0 Identiteetti.** Mittaa Suomen talvijärjestelmän monipäiväistä kestävyyttä. Synteettinen [0,1].
Aikavakio: 24 h / 72 h / 168 h. Abstraktiotaso: 1–2 tasoa yli operatiivisen simuloinnin.
Ei ennuste, ei hälytysjärjestelmä.

**§1 Aggregointi.** Additiivinen + preemio:
`EPP = (1−FS)·0,30 + SP·0,30 + DP_t·0,20 + WR·0,20 + P(T168)`, P ∈ {0; 0,05; 0,12}.
Painot summautuvat 1,00 ja **lopputulos on rajattu `Math.min(1, …)`**, joten maksimi on 1,0 eikä 1,12.
*(Tarkistettu koodista, rivit 2031 ja 2052. Ulkopuolisen tarkastuksen väite [0, 1.12] ei pidä paikkaansa.)*
Huom: preemio voi työntää arvon kattoon, jolloin mittari lakkaa erottelemasta.

**§2 Komponentit.** FS (DS 188+191+124, 0,30), SP (DS 124+192, 0,30), DP_t (Open-Meteo + C_exp(T), 0,20,
fallback DP_s), WR (DS 181, 0,20), P (T168-preemio). FS(p):n kaava (hydro_RF-skaalaus) on dokumentoimaton.

**§3 Kynnykset.** 0,25 / 0,50 / 0,75. Backtest (§09) ei kelpaa kalibroinniksi: sen stressikriteeri oli
NordPool-hinta, ja instrumentti toteaa itse mittaavansa osittain väärää asiaa.

**§4 Vertailusarja.** Backtest-periodit 2022–2024 käyttävät rekonstruoituja kuukausikeskiarvoja ja
synteettistä tuntiprofiilia; nykyinen periodi on live-dataa. DP_t:n uudelleenkalibrointi 8/2026 katkaisi
sarjan: sitä ennen ja sen jälkeen lasketut arvot eivät ole vertailukelpoisia.

**§5 Nollajakauma.** Puuttuu. Tarvitaan EPP tunnetusti normaalilta talvelta ja tunnetusti kireältä,
samalla kaavalla laskettuna.

**§6 Rajoitteet.**
1. Kynnysten alkuperä dokumentoimaton.
2. FS(p):n kaava dokumentoimaton.
3. Backtest mittaa hintakriisiä, ei fyysistä riittävyyttä.
4. DP_t:n kalibrointi katkaisi sarjan.
5. Komponenttien saturaatio (DP_t, SP) poistaa erottelukyvyn; varoitus näkyy §01:ssä.

**§7 Muutosloki.** 1.8.2026 §02/§10/§11 uudelleenrenderöinti hydro_RF:n saapuessa.
**23.9.2026: sama vika löytyi §01:stä** — posture näytti pysyvästi hydroRF = 1,0 -pohjaista EPP:tä
(0,573 vs. §02/§06/§09/§11 0,587, molemmat W168). Ero ei ollut aikaleimaero vaan renderöintijärjestys.
Korjattu v2.12.4: §01, §03, §05 ja §06 renderöidään uudelleen samasta objektista.
21.9.2026 v2.12.2 aikaviipalehaku (proxy ei välitä page-parametria), §16 tuntileikkaus, §17 sähkövarastot.
22.9.2026 v2.12.3 P1-malliarvio ja §10 CFE.

---

## Päätöslista

| # | Instrumentti | Päätös | Vaikutus | Tila |
|---|---|---|---|---|
| 1 | HEM | SD:n vertailutaso | koko verdict | **tehty 22.9.2026**: saman vuodenpäivän normaali |
| 2 | BEM | Kertova muoto: kalibroi kynnykset vai vaihda additiiviseksi | Critical/BP-like saavutettavuus | avoin; katto näkyvissä 23.9.2026 alkaen |
| 3 | WEM | Preemion suhde kattoon | — | **ei toimenpiteitä**: jo rajattu koodissa |
| 4 | Kaikki | Nollajakauma tunnetuilta vuosilta | kynnysten oikeutus | avoin, vaatii dataa |
| 5 | HEM | §05-sarjan uudelleenlaskenta SYKE:n pitkästä sarjasta | live vs. historia | avoin |
| 6 | WEM | FS(p):n kaavan dokumentointi | toistettavuus | avoin |
| 7 | BEM | dS/dt 20 v ikkunan täytyttyä | trendin validiteetti | odottaa |
| 8 | HEM | RF / hydro_RF -nimikollisio | tulkinta | avoin |

**Järjestys:** kohta 2 on päätös, ei laskenta, ja se kannattaa tehdä ennen muita. Kohdat 4 ja 5 vaativat
dataa. Kohdat 6 ja 8 ovat dokumentointia.

**Yhteinen havainto.** Kaikki kolme instrumenttia kärsivät samasta ongelmasta eri muodossa: live-arvoa
verrataan sarjaan, joka on laskettu eri kaavalla (HEM: SD ja §05; BEM: D_c:n ikkuna; WEM: DP_t:n kalibrointi).
Tämä on yksi ongelma, ei kolme. Charterin §4 on olemassa juuri sen takia.

Jokainen instrumentti viittaa tähän tiedostoon §04:ssä (metodologia) yhdellä rivillä.
