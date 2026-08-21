# DGIRP v0.3 ja v0.4 — lähdemuistiot

**Liite tiedostoon:** DGIRP-review-paketti-2026-08-21.md
**Status:** työmuistiot, ei julkaistu ACI-korpuksessa, ei versiohistoriaa repossa.
**Huomautus arvioijalle:** näiden dokumenttien alkuperä on keskustelu, ei laskentaskripti. Tämä on olennaista §3.2:n kannalta: v0.3:n taulukon takana ei ole tallennettua laskentaa, jota vasten se voitaisiin tarkistaa. Jos taulukko on generoitu tekstinä eikä laskettu, se selittää poikkeamat suoraan.

---
---

# OSA A — DGIRP v0.3

*Raporttipohjainen analyysi. Muistio 21.8.2026.*

## 1. Johdanto

Tämä muistio kokoaa keskeiset julkisista lähteistä löytyvät luvut ja arviot Suomen sähköjärjestelmän tilasta, ja asettaa ne DGIRP (Dynamic Grid Integration & Resilience Protocol) -viitekehykseen. Tarkoituksena on tuottaa virallisiin raportteihin perustuva pohja sille, millä edellytyksillä uutta suurta, jatkuvaa sähkökuormaa (esim. Kouvolan datakeskusklusteri, 743 MW) voidaan liittää verkkoon eri vuosina.

## 2. Keskeiset lähteet

| Lähde | Raportti | Keskeinen anti |
|---|---|---|
| Fingrid | Yhteenveto sähköjärjestelmän toiminnasta talvella 2025–2026 | Toteutunut kulutushuippu 15 553 MW, tuontitarve 1 233 MW |
| Fingrid | Sähkön riittävyysarvio talvelle 2025–2026 | Kotimainen kapasiteetti stressitilanteessa 11 700 MW |
| Svenska kraftnät | Kortsiktig marknadsanalys 2026–2030 | SE1 muuttuu nettotuojaan vuoteen 2030 mennessä |
| ENTSO-E | Winter Outlook 2025–2026 | Suomi, Viro ja Liettua ainoat mannermaan maat, joissa pieni riski poikkeuksellisissa oloissa |
| Fingrid | Kantaverkon kehittämissuunnitelma | Harjulinja valmistuu 2030–2032 |

## 3. Yhteenveto keskeisistä luvuista

### 3.1 Toteutunut stressitilanne (talvi 2025–2026)

Fingridin raportin mukaan talven 2025–2026 kulutushuippu oli 15 553 MW (8.1.2026 klo 17.00–17.15). Tuolloin:

| Suure | Arvo |
|---|---|
| Kulutus | 15 553 MW |
| Painotettu lämpötila | −19 °C |
| Kotimainen tuotanto | 14 320 MW |
| Nettotuonti | 1 233 MW |
| Aluehinta | 92,39 €/MWh |

Aurora Line otettiin käyttöön marraskuussa 2025 ja nosti SE1→FI-kapasiteetin 1 900 MW:iin. Yhteyttä hyödynnettiin tehokkaasti: tuonti Pohjois-Ruotsista oli 78 % ajasta suurempaa kuin entinen maksimituontikapasiteetti (1 200 MW).

Huomio: Tämä kulutushuippu saavutettiin talvena, joka oli useilla paikkakunnilla (Vantaa +2,2 °C, Kouvola +2,5 °C, Rovaniemi +3,4 °C) selvästi pitkäaikaista keskiarvoa lämpimämpi. Kylmempänä talvena kulutus olisi ollut korkeampi.

### 3.2 Kotimainen kapasiteetti stressitilanteessa

Fingrid arvioi erittäin kylmänä ja tyynenä talvipäivänä kotimaiseksi saatavilla olevaksi kapasiteetiksi 11 700 MW. Tämä tarkoittaa, että 15 553 MW:n kulutushuipussa tuontitarve olisi ollut 3 800 MW — mikä ylittää selvästi Aurora Linen 1 900 MW:n kapasiteetin. Tosiasiassa tuontia tarvittiin 1 233 MW, koska kotimainen tuotanto oli 14 320 MW (eli 2 620 MW enemmän kuin Fingridin stressiarvio).

### 3.3 SE1:n muuttuva rooli

| Vuosi | SE1:n keskimääräinen ylijäämä |
|---|---|
| 2026 | +14 TWh |
| 2030 | −1 TWh (nettotuoja) |

Pohjois-Ruotsi muuttuu nettoviejästä nettotuojaan viidessä vuodessa. Koko Pohjolan ylijäämä pienenee 53 TWh:sta 29 TWh:iin vuosina 2026–2030.

### 3.4 ENTSO-E:n riskiarvio

Winter Outlook 2025–2026: Euroopan tilanne kokonaisuutena suotuisa. Mannermaan maista vain Suomi, Viro ja Liettua kohtaavat pieniä riskejä poikkeuksellisen epäsuotuisissa olosuhteissa: kylmä sää yhdistettynä korkeaan suunnittelemattomien katkosten määrään. Suomen sähköjärjestelmä on yhä enemmän tuulivoimavaltainen, ja paikallisen tuotannon ja siirtoyhteyksien luotettavuus on kriittistä kylminä ja tyyninä päivinä.

### 3.5 Harjulinja

Fingrid suunnittelee Harjulinjaa — uutta 400+110 kV voimajohtoyhteyttä **Pyhäjärveltä Kouvolaan**. Rakentaminen arviolta 2030–2032. Hanke on YVA-menettelyssä, päätös reitistä arviolta kesän 2027 jälkeen.

## 4. Analyysi: DGIRP-mittarit

### 4.1 α(t) — SE1:n vientimarginaali

SE1-energiataseen perusteella johdettu vientimarginaali (NTC 2 300 MW × α):

| Vuosi | SE1-tase (TWh) | α(t) | Vientikapasiteetti (MW) |
|---|---|---|---|
| 2026 | +14 | 0,70 | 1 610 |
| 2027 | +10,25 | 0,575 | 1 323 |
| 2028 | +6,50 | 0,45 | 1 035 |
| 2029 | +2,75 | 0,325 | 748 |
| 2030 | −1,00 | 0,20 | 460 |
| 2032 | −2,5 (arvio) | 0,15 | 345 |

### 4.2 RIILL (Resilience Index for Load and Infrastructure)

    RIILL_t = (Firm_domestic + Import_firm(t) + Flexibility_credible) / PeakLoad_stress

Lähtöarvot:

- Firm_domestic = 11 700 MW (Fingridin stressiarvio)
- Import_firm(t) = edellä laskettu vientikapasiteetti
- Flexibility_credible = 15 % kulutuksesta
- PeakLoad_stress = kulutus × 1,1

### 4.3 RIILL_P05 (pahin 5 %)

Koska RIILL vaihtelee sään, huoltojen ja tuonnin mukaan, P05-arvo on tyypillisesti 10–15 % keskiarvoa pienempi. Oletetaan konservatiivisesti **12 % pudotus**.

RIILL_P05 eri vuosina ja kuormilla:

| Lisäkuorma | 2027 | 2028 | 2029 | 2032 |
|---|---|---|---|---|
| 0 MW | 0,866 | 0,829 | 0,792 | 0,768 |
| 250 MW | 0,847 | 0,811 | 0,776 | 0,752 |
| 500 MW | 0,830 | 0,795 | 0,760 | 0,738 |
| 743 MW | 0,811 | 0,777 | 0,745 | 0,722 |
| 1 000 MW | 0,795 | 0,762 | 0,730 | 0,708 |
| 1 500 MW | 0,763 | 0,731 | 0,701 | 0,681 |
| 2 000 MW | 0,733 | 0,703 | 0,675 | 0,656 |

### 4.4 Päätösmatriisi

Kriteerit: Green ≥ 1,15 · Amber 1,00–1,15 · Red 0,85–1,00 · Black < 0,85

| Lisäkuorma | 2027 | 2028 | 2029 | 2032 |
|---|---|---|---|---|
| 0 MW | Amber | Amber | Red | Red |
| 250 MW | Red | Red | Red | Red |
| 500 MW | Red | Red | Red | Red |
| 743 MW | Red | Red | Black | Black |
| 1 000 MW | Red | Red | Black | Black |
| 1 500 MW | Black | Black | Black | Black |
| 2 000 MW | Black | Black | Black | Black |

## 5. Keskeiset johtopäätökset

1. Jo nykytilanne (0 MW lisäkuorma) on vuonna 2029 Red-luokassa — järjestelmän pahin 5 % jaksoista on jo kireällä ilman uutta kuormaa. ENTSO-E tunnistaa saman riskin.
2. 250 MW:n lisäkuorma riittää pudottamaan järjestelmän Red-luokkaan jo 2027.
3. 743 MW:n Kouvola-kuorma on 2027–2028 Red (vaatii joustovelvoitteet, Cap & Trim) ja 2029–2032 Black (ei voida hyväksyä ilman merkittäviä lisätoimia).
4. **Mikään kuorma ei yllä Green- tai Amber-luokkaan** — koko tarkasteluväli on Red tai Black.
5. SE1-dynamiikka on ratkaiseva tekijä.

## 6. Suositukset

1. 743 MW:n liittäminen edellyttää merkittävää uutta firm-kapasiteettia (ei näköpiirissä), merkittävää siirtokapasiteetin lisäystä, ja sitovaa joustovelvoitetta (esim. 50 % kuormasta leikattavissa Black Periodissa).
2. Harjulinjan aikataulua tulisi tarkastella kriittisesti.
3. Black Period -priorisointi on määriteltävä etukäteen.
4. SE1-riippuvuutta ei voi pitää itsestäänselvyytenä.

## 7. Liite: lähdeviitteet

| Lähde | Keskeinen sisältö |
|---|---|
| Fingrid, talviraportti 2025–2026 | Kulutus korkeimmillaan 15 553 MW; kotimainen tuotanto 14 320 MW; nettotuonti 1 233 MW |
| Fingrid, talviraportti | Aurora Line nosti rajasiirtokapasiteetin 1 900 MW:iin; tuonti 78 % ajasta suurempaa kuin entinen maksimi 1 200 MW |
| ENTSO-E, Winter Outlook 2025–2026 | Mannermaalla vain Suomi, Viro ja Liettua kohtaavat pieniä riskejä poikkeuksellisen epäsuotuisissa oloissa |
| ENTSO-E, Winter Outlook | Suomen järjestelmä yhä tuulivoimavaltaisempi; paikallisen tuotannon ja siirtoyhteyksien luotettavuus kriittistä kylminä ja tyyninä päivinä |
| Svenska kraftnät, Kortsiktig marknadsanalys | Ylijäämä pienenee 14 TWh:sta (2026) −1 TWh:iin (2030) |
| Fingrid, Harjulinja | Voimajohdot Pyhäjärveltä Kouvolaan vuosina 2030–2032 |

---
---

# OSA B — DGIRP v0.4

*Raporttipohjainen analyysi. Muistio 21.8.2026. Status: analytical working paper.*

## 1. Johdanto

Tämä muistio arvioi Suomen sähköjärjestelmän kykyä vastaanottaa uutta suurta ja jatkuvaa sähkökuormaa tilanteessa, jossa samanaikaisesti: (1) talven kulutushuiput ovat korkeita, (2) kotimainen firm-kapasiteetti on rajallinen, (3) tuulivoiman osuus kasvaa, (4) sähköntuonnin merkitys säilyy suurena stressitilanteissa, (5) Pohjois-Ruotsin ylijäämä pienenee, (6) pohjois-eteläsuuntaiset siirtotarpeet kasvavat, (7) uutta kantaverkkokapasiteettia rakennetaan vaiheittain.

Tarkastelun kohteena on 743 MW:n jatkuva lisäkuorma suuren datakeskusklusterin esimerkkitapauksena.

Kysymys: *Kuinka paljon järjestelmän resilienssimarginaalia uusi suuri jatkuva kuorma kuluttaa eri sää-, tuotanto-, siirto- ja tuontiskenaarioissa?*

## 2. Metodologinen muutos v0.3:sta v0.4:ään

v0.3:n keskeinen ongelma oli, että kolme eri asiaa sekoittuivat: vuositasoinen energiatasapaino, hetkellinen siirtokapasiteetti, ja firm-kapasiteetti.

v0.4 erottaa ne.

**2.1 Kolme kapasiteettitasoa**

- **A. Energy balance** — vuositasolla tuotannon ja kulutuksen suhde.
- **B. Transfer capability** — tekninen ja kaupallinen siirtokapasiteetti tiettynä ajankohtana.
- **C. Firm contribution** — se osuus kapasiteetista, jonka voidaan konservatiivisesti olettaa olevan käytettävissä juuri stressitilanteessa.

Näin: TWh ≠ MW_firm, eikä vuosittaista SE1-ylijäämää muunneta suoraan firm-tuonniksi.

## 3. Lähdepohja

| Lähde | Keskeinen aineisto |
|---|---|
| Fingrid, talvi 2025–2026 | Kulutushuippu 15 553 MW, kotimainen tuotanto 14 320 MW, nettotuonti 1 233 MW |
| Fingrid, riittävyysarvio | Erittäin kylmän ja tyynen tilanteen kotimainen kapasiteetti n. 11 700 MW |
| Svenska kraftnät, Kortsiktig marknadsanalys | SE1:n ja Pohjolan tasapainon muutos 2026–2030 |
| ENTSO-E, Winter Outlook 2025–2026 | Suomen riittävyysriski epäedullisissa olosuhteissa |
| Fingrid, kantaverkon kehittämissuunnitelma | Harjulinjan aikataulu ja vaikutus |

## 4. Toteutunut stressitilanne 2025–2026

Peak(2025/26) = 15 553 MW, 8.1.2026 klo 17.00–17.15.

| Muuttuja | Arvo |
|---|---|
| Kulutus | 15 553 MW |
| Kotimainen tuotanto | 14 320 MW |
| Nettotuonti | 1 233 MW |
| Lämpötila | n. −19 °C |
| Aluehinta | 92,39 €/MWh |

Järjestelmä ei ollut lähellä nollariskiä edes toteutuneessa huipputilanteessa: n. 7,9 % kulutuksesta katettiin nettotuonnilla. Kyseinen talvi oli keskimääräistä lämpimämpi.

*Toteutunut huippu ei ole sama asia kuin fysikaalinen stressihuippu.*

## 5. Fingridin stressikapasiteetti

Firm_domestic = 11 700 MW.

    Gap = 15 553 − 11 700 = 3 853 MW

*3 853 MW ei tarkoita automaattisesti 3 853 MW:n tuontitarvetta.* Se on stressiskenaarion kapasiteettivaje ennen muiden resurssien huomioimista.

## 6. SE1:n muuttuva rooli

| Vuosi | SE1-tase, TWh | Tulkinta |
|---|---|---|
| 2026 | +14 | vahva ylijäämä |
| 2027 | n. +10,25 | ylijäämä pienenee |
| 2028 | n. +6,50 | ylijäämä pienenee nopeasti |
| 2029 | n. +2,75 | lähellä tasapainoa |
| 2030 | −1 | nettotuontitilanne |

Näitä lukuja **ei muunneta suoraan MW-firm-tuonniksi**, vaan niitä käytetään tuontimarginaalin skenaarioiden ohjaajana.

## 7. α(t) v0.4 — vientimarginaali-indeksi

v0.3:ssa α(t) tulkittiin käytännössä MW-kapasiteettina. v0.4:ssa:

    α(t) = ExportMarginScenario(t)

α ei ole NTC. Se on skenaarioindeksi, joka kuvaa SE1:n vientimarginaalin suhteellista heikkenemistä.

| Vuosi | α-skenaario | Tulkinta |
|---|---|---|
| 2026 | 1,00 | korkea vientimarginaali |
| 2027 | 0,82 | lievästi heikentynyt |
| 2028 | 0,64 | selvästi heikentynyt |
| 2029 | 0,45 | matala |
| 2030 | 0,30 | erittäin matala |
| 2032 | 0,20 | stressiskenaario |

Nämä eivät ole Svenska kraftnätin ennusteita vaan DGIRP:n skenaarioarvoja.

## 8. RIILL v0.4

### 8.1 RIILL-G — Grid-only

    RIILL_G = (F_domestic + F_import) / PeakLoad_stress

- F_domestic = stressitilanteessa saatavilla oleva kotimainen firm-kapasiteetti
- F_import = konservatiivisesti arvioitu firm-tuonti
- PeakLoad_stress = stressikuorma

### 8.2 RIILL-P — Project-adjusted

    RIILL_P = (F_domestic + F_import + F_system-flex + F_project-flex + F_project-firm) / PeakLoad_stress

## 9. Stressikuorma

    PeakLoad_stress = PeakLoad_base × 1,10
    15 553 × 1,10 = 17 108 MW

Lisäkuorman L tapauksessa:

    PeakLoad_stress(L) = (15 553 + L) × 1,10
    (15 553 + 743) × 1,10 = 17 926 MW

## 10. 743 MW:n vaikutus

    743 / 15 553 = 4,78 %
    743 × 1,10 = 817 MW

743 MW:n jatkuva kuorma lisää stressitilanteen kapasiteettivaatimusta n. 817 MW ennen kuin hankkeen oma jousto otetaan huomioon.

## 11. Joustavuus

v0.4 ei enää oleta automaattisesti 15 %:n joustoa.

    F_credible = F_DSR + F_storage + F_backup + F_industrial
    F_credible,i = F_installed,i × A_i × R_i × D_i

- A = käytettävyys stressitilanteessa
- R = toteutuvan aktivoinnin luotettavuus
- D = ajallinen kesto-/samanaikaisuuskerroin

## 12. Kouvolan 743 MW — joustoskenaariot

| Joustotaso | Leikattava kuorma |
|---|---|
| 0 % | 0 MW |
| 25 % | 186 MW |
| 50 % | 372 MW |
| 75 % | 557 MW |

## 13. RIILL-päätösluokat

| Luokka | RIILL-P05 | Tulkinta |
|---|---|---|
| Green | ≥ 1,15 | vahva marginaali |
| Amber | 1,00–1,15 | hallittava |
| Red | 0,85–1,00 | merkittävä resilienssiriski |
| Black | < 0,85 | kriittinen marginaali |

Luokat eivät ole viranomaisen hälytysrajoja.

## 14. P05 — uusi määritelmä

v0.3:ssa P05 muodostettiin vähentämällä keskiarvosta kiinteä 12 %. v0.4:ssa tätä ei enää pidetä lopullisena menetelmänä.

    RIILL_P05 = Q_0,05(RIILL)

Jakauma muodostetaan epävarmuustekijöistä: lämpötila, tuulivoima, vesivoima, ydinvoiman käytettävyys, lämpövoiman käytettävyys, siirtoyhteyksien käytettävyys, SE1:n vientimarginaali, muiden Pohjoismaiden kysyntä, Suomen kulutus, uuden kuorman käyttäytyminen.

## 15. Harjulinja

Valmistuminen 2030-luvun alkuun. DGIRP ei käsittele sitä binäärisenä muuttujana vaan asteittaisena kapasiteetin muutoksena: GridCapacity(t).

Oleellinen kysymys: kuinka paljon lisäsiirtokapasiteettia on käytettävissä minäkin vuonna ja missä järjestelmän osassa?

## 16. Päätösmatriisi

Kolme ulottuvuutta:

- **A.** RIILL_G — grid-only resilience
- **B.** RIILL_P — project-adjusted resilience
- **C.** BPH = Hours(RIILL_P < 0,85) — Black Period exposure

Erottelu: (1) järjestelmä on kriittinen ilman hankkeen toimia, (2) hanke pystyy pienentämään altistusta, (3) hanke ei pysty pienentämään altistusta riittävästi.

## 17. 743 MW:n tulkinta

Testattava hypoteesi: *Ilman merkittävää hankekohtaista joustoa tai muuta firm-kapasiteettia 743 MW:n jatkuva lisäkuorma kasvattaa Suomen sähköjärjestelmän stressialtistusta olennaisesti erityisesti tilanteissa, joissa kotimainen tuotanto on lähellä Fingridin stressiarviota ja SE1:n tuontimarginaali on heikentynyt.*

## 18. Aikajänne 2027–2032

- **Vaihe I: 2027–2028.** SE1:n vientimarginaali edelleen merkittävä, mutta järjestelmä herkkä samanaikaiselle kylmälle, tyynelle, korkealle kulutukselle, vikaantumiselle ja siirtorajoitteille. Posture: Red ilman vahvaa hankekohtaista joustoa.
- **Vaihe II: 2029–2030.** SE1:n ylijäämä huomattavasti pienempi, uuden kuorman vaikutus kumuloitunut. Posture: Elevated / Red-to-Black.
- **Vaihe III: 2031–2032.** Harjulinjan vaikutus alkaa muuttaa rakennetta. Kysymys ei ole "onko Suomessa sähköä" vaan "pystyykö järjestelmä siirtämään tehon oikeaan paikkaan oikeaan aikaan".

## 19. Black Period

    BlackPeriod = RIILL_P < 0,85

Ei tarkoita automaattisesti sähköpulaa vaan sitä, että jäljelle jäävä resilienssimarginaali on liian pieni hyväksyttäväksi ilman erityisiä vastatoimia.

## 20. Cap & Trim

**Cap** — kuorman yläraja stressitilanteessa:

    Load_max,Black = 743 MW × (1 − J)

**Trim** — asteittainen leikkaus:

| DGIRP-tila | Kuorma |
|---|---|
| Normal | 743 MW |
| Tight | 650 MW |
| Elevated | 550 MW |
| Black | 370 MW tai vähemmän |

Arvot ovat esimerkkejä, eivät viranomaisrajoja.

## 21. Keskeiset johtopäätökset

1. Toteutunut huippukuorma 15 553 MW, mutta stressiarvion 11 700 MW osoittaa järjestelmän olevan erittäin kylmässä ja tyynessä tilanteessa huomattavasti riippuvaisempi ulkoisesta kapasiteetista.
2. 743 MW vastaa n. 4,8 % toteutuneesta huipusta ja n. 817 MW:n lisäystä 10 % stressikertoimella laskettuun kapasiteettitarpeeseen.
3. Pohjois-Ruotsin ylijäämän pienentyminen on merkittävä rakenteellinen muutos.
4. SE1:n vuositasoinen energiatasapaino ei ole sama asia kuin firm-tuontikapasiteetti. Suora muunnos poistetaan v0.4:ssä.
5. Suurten kuormien järjestelmäriskiä ei voi arvioida pelkän MW-luvun perusteella.
6. Kuorma ilman sitovaa joustoa on huomattavasti riskialttiimpi kuin nimellisesti saman kokoinen kuorma, jolla on 25–50 % todellisesti aktivoitavaa joustoa.
7. Harjulinja parantaa pitkän aikavälin siirtokykyä, mutta ei ole automaattinen ratkaisu vuosien 2027–2031 riskiin.
8. Oikea kysymys: *millä firm-, jousto-, siirto- ja kuormanhallintaehtojen yhdistelmällä 743 MW voidaan liittää niin, ettei P05-resilienssi putoa kriittisen rajan alapuolelle?*

## 22. Suositukset

**22.1 Liittymisehtoihin:** hankekohtainen firm-kapasiteetti, sitova kysyntäjousto, Black Period -leikkauskyky, akun/varavoiman todellinen käytettävyys, jouston aktivointiaika, jouston kesto, kuorman vaiheistus.

**22.2 Verkkosuunnitteluun:** liittymispisteen paikallinen siirtokyky, pohjois-eteläsuuntaiset virtaukset, N-1/N-2-tilanteet, samanaikaiset uudet suurkuormat.

**22.3 Tuontiriippuvuuteen:** SE1:n vientimarginaalia ei tule käsitellä vuoden 2030 jälkeen vakaana hätävarana.

**22.4 Seuraava simulaatiovaihe:** tuntitason Monte Carlo, vähintään 10 000 vuosi-/stressiskenaariota, joissa vaihtelevat lämpötila, tuuli, vesitilanne, tuotantolaitosten käytettävyys, SE1-tuonti, siirtorajoitteet, kulutushuippu, 743 MW:n jousto ja Harjulinjan vaiheittainen käyttöönotto. Raportoidaan RIILL_P05, RIILL_P01, BlackPeriodHours, ExpectedLoadShedding, ImportDependency.

## 23. Diagnostinen hypoteesi

*Suomen sähköjärjestelmän suuren uuden jatkuvan kuorman integraatioriski ei määräydy yksin kotimaisen tuotantokapasiteetin tai kantaverkon nimellisen siirtokapasiteetin perusteella. Riski syntyy kolmen muuttuvan tekijän yhteisvaikutuksesta: stressitilanteen kotimaisen firm-kapasiteetin rajallisuudesta, ulkoisen kapasiteetin — erityisesti SE1:n — heikkenevästä saatavuusmarginaalista sekä uuden kuorman jäykkyydestä.*

    IntegrationRisk = f(FirmCapacity, ImportMargin, GridCapacity, LoadFlexibility, StressDuration)

eikä

    IntegrationRisk = f(MW_new)

## 24. Lopullinen tulkinta

DGIRP v0.4 ei esitä, että 743 MW:n klusteria ei voitaisi teknisesti liittää. Suuren jatkuvan kuorman liittäminen muuttaa järjestelmän resilienssiprofiilia juuri siinä ajassa, jossa yksi Suomen perinteisistä ulkoisista puskurimekanismeista — Pohjois-Ruotsin rakenteellinen sähköylijäämä — on heikkenemässä. Vuoden 2027 liittymispäätös ei ole sama asia kuin vuoden 2030 liittymispäätös.

## 25. Rajaus

Perustuu julkisesti saatavilla olevaan aineistoon ja DGIRP v0.4 -kehykseen. Ei viranomaisen ennuste, riittävyysarvio eikä operatiivinen hälytys. RIILL-, α- ja Black Period -muuttujat ovat DGIRP:n omia diagnostisia suureita. Seuraava validointitaso on tuntitason Monte Carlo -simulaatio.

---
---

# OSA C — Mitä v0.4 poisti v0.3:sta

Tämä erotus on §3.2:n ja §4:n kannalta olennainen, ja se on koottu tähän erikseen, jotta arvioijan ei tarvitse tehdä sitä käsin.

| v0.3:ssa | v0.4:ssä |
|---|---|
| α numeerisena vientikapasiteettina (MW) | α dimensiottomana skenaarioindeksinä, ei esiinny yhdessäkään kaavassa |
| NTC 2 300 MW × α | poistettu |
| Flexibility_credible = 15 % kulutuksesta | F_credible = Σ F_installed,i × A_i × R_i × D_i (kertoimia ei ole numeroitu) |
| P05 = keskiarvo × 0,88 | P05 = Q_0,05(RIILL), jakaumaa ei ole muodostettu |
| Täysi RIILL_P05-taulukko: 7 kuormatasoa × 4 vuotta | poistettu kokonaan |
| Täysi Green/Amber/Red/Black-matriisi | poistettu kokonaan |
| Johtopäätös "743 MW on Black 2029–2032" | korvattu testattavalla hypoteesilla ilman lukuja |

**Seuraus:** v0.4 ei sisällä yhtään laskettua RIILL-arvoa. Ainoa versio, jossa lukuja on, on v0.3, ja sen taulukon toistettavuus on tarkastuspaketin §3.2:n kohde. Jos v0.3:n taulukko ei ole toistettavissa eikä v0.4 sisällä lukuja, kehyksellä ei tällä hetkellä ole yhtään validoitua numeerista tulosta.
