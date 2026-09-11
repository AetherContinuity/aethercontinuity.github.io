# WEM — korjausinventaario 11.9.2026

**TILA: kaikki kahdeksan kohtaa käsitelty. WEM v2.9.3.**

| # | tila | missä |
|---|---|---|
| K1 FS sokea CHP:lle | kirjattu | §01 rajoitelohko, v2.9.2 |
| K2 SP saturoitunut | kirjattu | §01 rajoitelohko + ulottuvuuskortti |
| K3 DP_t vakio | kirjattu | §01 rajoitelohko |
| K4 EPP kapeampi | kirjattu | §01 rajoitelohko |
| K5 nimen kausilupaus | kirjattu | §14, v2.9.3 |
| K6 chpPct-parametri | kirjattu | §10 alaviite, v2.9.3 |
| K7 regressiomenetelmä | ei instrumenttiin | data/wem-mittaukset-2026-09.json |
| K8 jo korjatut | — | v2.8.2–2.9.1 |

**Yhtään kaavaa ei muutettu.** Kaikki kirjattiin näkyviin.

---

Syntyi kun 9.–11.9.2026 mitattu aineisto (säätömarkkina, tarjouskirja,
sähkökattilat, CHP-regressio) osoitti useita instrumentin päätelmiä
epätarkoiksi. Järjestys on vakavuuden mukaan, ei osion.

Jokaisessa kohdassa: **mitä instrumentissa on · mitä mitattiin ·
mitä siitä seuraa · korjauksen koko.**

---

## K1 · FS on sokea CHP:lle [RAKENTEELLINEN]

**Instrumentissa:**

```
FS       = (ydin + vesi × hydro_RF) / kulutus      ← päämittari, EPP-paino 0,30
ECI_semi = (ydin + vesi + CHP)      / tuotanto     ← sivumittari, ei EPP:ssä
```

**Mitattu:** §10 kertoo CHP-eroosiosta ja SM-015 laskee Helsingin
poistuman **−650 MW**. Kumpikaan ei näy `FS`:ssä, koska CHP ei ole
osoittajassa.

Skenaariotaulukon rivit `+3000 MW / −30 %` ja `+3000 MW / −40 %`
antavat **identtisen FS 42,8 %**. Se on taulukossa näkyvissä mutta
selittämättä.

**Seuraus:** instrumentti keskustelee CHP-eroosiosta mutta sen
tärkein komponentti ei mittaa sitä. Lukija olettaa että se mittaa.

**Korjauksen koko:** `FS`:n määritelmän muuttaminen **katkaisisi
aikasarjan** — ja WEM:n oma koodi varoittaa juuri siitä (kommentti
1.8.2026: FS-muutos "muutti hiljaa julkaistuja historia-arvoja ilman
versiointia", peruttiin samana päivänä).

**Ei siis korjata kaavaa. Kirjataan rajoite näkyviin `FS`-kortin
viereen.** Ja harkitaan `ECI_semi`:n nostamista näkyvämmäksi, koska
se on ainoa joka näkee CHP:n.

---

## K2 · SP on saturoitunut [VAKAVA]

**Instrumentissa:** `SP` = stressituntien osuus, kynnys
`gap > kulutus × 5 %`. EPP-paino **0,30**.

**Mitattu 9.9.2026:** 21 tuntia, **21 stressituntia (100 %)**, gap
**29–35 %** eli kuusinkertaisesti kynnyksen yli koko ajan.

Talven W168-arvo oli 54,8 % ja se luokitellaan "BP-like".

**Seuraus:** mittari joka on päällä sadassa prosentissa tunneista ei
erottele. WEM:n oma §07 varoittaa tästä — *"SP toimii
varhaisvaroituksena eikä kriisi-indikaattorina"* — mutta se ei toimi
varhaisvaroituksenakaan jos se on aina päällä.

**Korjauksen koko:** kynnyksen muuttaminen katkaisee aikasarjan kuten
K1:ssä. `SP_depth` on jo olemassa (v4, kokeellinen) ja se erottelee —
se on oikea korjaus, mutta se vaatii v4:n vakiinnuttamisen.

**Väliaikainen:** §01:n ulottuvuuskortti näyttää jo `SP`:n ja
`SP_depth`:n rinnakkain. Se riittää kunnes v4 ratkaistaan.

---

## K3 · DP_t on vakio [VAKAVA]

**Instrumentissa:** `DP_t` = lämpötilakorjattu kysyntäpaine,
EPP-paino **0,20**.

**Mitattu:** `1,000` **kaikissa ikkunoissa**, W24/W72/W168.
`dp_t_raw` on 2,41 — se on leikattu ykköseen.

**Seuraus:** viidennes EPP:stä on vakio. EPP:n vaihtelu tulee siis
käytännössä `WR`:stä ja `FS`:n kulutusnimittäjästä.

**Korjauksen koko:** normalisointirajan (`TEMP_SIGMA 900`) muuttaminen
katkaisee aikasarjan. Saturaatio on jo merkitty `saturated`-kentässä ja
näkyy §01:ssä.

**Ei korjata. Kirjataan mitä siitä seuraa EPP:n tulkinnalle.**

---

## K4 · EPP:n liikkuva osa on kapeampi kuin miltä näyttää [SEURAUS]

K1–K3 yhdessä:

```
FS       liikkuu, mutta sokea CHP:lle
SP       liikkuu vähän, saturoitunut yläpäässä
DP_t     ei liiku lainkaan
WR       liikkuu
```

**Seuraus:** neljästä komponentista yksi on vakio ja yksi lähes
kyllästynyt. **EPP liikkuu käytännössä `WR`:n ja kulutuksen mukaan.**

Se ei tee EPP:stä väärää, mutta se tekee siitä kapeamman kuin
neljän komponentin summa antaa ymmärtää.

**Korjauksen koko:** ei koodia. Yksi kappale §01:een.

---

## K5 · Nimi lupaa kausiluonteisuutta jota ei ole [KOHTALAINEN]

**Instrumentissa:** *Winter Endurance Monitor*. §07 sanoo että
kesäkuukaudet ovat referenssitasoa, ja §01:ssä on kesäkauden
huomautus.

**Mitattu 11.9.2026:** tarjouskirja kesällä vs. talvella

```
kesä (viikkootos, kesä–elo 2025 ja 2026)   med 1 010 MW
talvi 2025–26 (koko)                       med 1 059 MW
suhde                                            0,95
```

**Ja `RP_margin` kesällä:** mediaani **100 %**, ei kertaakaan alle
40 %.

**Seuraus:** korjauskyky ei ole kausiluonteinen. Riittävyys on
(kulutus on talvella suurempi), mutta korjausmarginaali ei.

**Korjauksen koko:** ei nimenmuutosta — nimi on historiallinen ja
kertoo mistä instrumentti syntyi. Kirjataan §14:ään että
mittauskausi ei rajoita RP:tä.

---

## K6 · chpPct-parametri skenaarioissa [KOHTALAINEN]

**Instrumentissa:** `calcWindowScenario(slice, dcMW, chpPct)`, ja
skenaariotaulukossa viisi riviä joissa `chpPct` vaihtelee.

**Mitattu 10.9.2026:** `chpPct` ei muuta `FS`:ää lainkaan (K1), ja
sen vaikutus `WR`:ään on 0,001 EPP:ssä. Ainoa kanava on `SP`, jota ei
voi laskea keskiarvoista.

**Seuraus:** kaksi taulukon riviä on identtisiä ja lukija ei tiedä
miksi. Parametri antaa ymmärtää enemmän vaikutusvaltaa kuin sillä on.

**Korjauksen koko:** alaviite taulukkoon. **Ei** parametrin poistoa —
`SP`-kanava on todellinen, sitä ei vain voi laskea aggregaateista.

---

## K7 · CHP-regressio ei erota kahta mekanismia [MENETELMÄ]

**Yritetty 11.9.2026:** regressio `CHP ~ lämpötila` talvittain,
tavoitteena mitata lämpösidonnaisuuden löystyminen.

**Tulos:** kulmakerroin −58,5 · −79,2 · −75,4 · −36,6 · −140,4.
**Trendiä ei ole.**

**Syy:** 18 päivää, ja otospäivien lämpötilakeskiarvo vaihtelee
−6,8:sta −0,3:een talvien välillä. Regressio ekstrapoloi eri
etäisyyksiltä.

**Ja syvempi syy:** kaksi mekanismia tuottaa saman signaalin —
**leuto talvi** (palautuva) ja **kapasiteetin purku** (pysyvä).
Regressio ei erota niitä ilman lämpötilakontrollia.

**Seuraus:** ei päätelmää suuntaan eikä toiseen. Testi on oikea,
aineisto väärä.

**Korjauksen koko:** ei instrumenttiin mitään. Kirjataan menetelmä
ja se mitä tarvittaisiin: satoja päiviä per talvi, **sovitetut
lämpötilavälit**. Ja vertailukohta on SM-015 — jos regressio näyttää
suuremman pudotuksen kuin ilmoitetut sulkemiset, erotus on
**ajamatta jättämistä**.

---

## K8 · Jo korjatut — ei toimenpiteitä

| # | mikä | korjattu |
|---|---|---|
| a | CHP "vapauttaa korjausmarginaalia talvella" | v2.9.1, mitattu r = −0,67 |
| b | `RP_curve` päämittarina | v2.9.0, korvattu `RP_margin`:lla |
| c | Compound-banneri renderöityi vaikka ehto ei täyttynyt | `display:none` |
| d | `{series, ...d}` ylikirjoitti aliaksen (aci-ecb-proxy) | 6aa6762 |
| e | SE1:n oletettu halpuus | v2.8.2, mitattu 107,1 €/MWh |

---

## Yhteenveto

**Kolme kohtaa (K1–K3) ovat rakenteellisia eikä niitä korjata
kaavaa muuttamalla** — se katkaisisi aikasarjan, ja WEM:n oma koodi
dokumentoi mitä siitä seurasi kun niin kerran tehtiin.

**Ne kirjataan näkyviin.** Se on sama ratkaisu kuin
`role_confidence 0.5` ja `calibrated: false` muualla tässä
projektissa: rakenne näkyy, arvoa ei keksitä, rajoite on luettavissa
siellä missä se vaikuttaa.

**K4 on niiden seuraus** ja se on tärkein yksittäinen kirjaus:
EPP:n liikkuva osa on kapeampi kuin neljän komponentin summa antaa
ymmärtää.

**K5–K7 ovat pienempiä** ja niistä kaksi ei vaadi koodia lainkaan.

Yksikään näistä ei tee EPP:stä väärää. Ne tekevät siitä
**kapeamman ja tarkemmin rajatun** kuin mitä esitys antaa ymmärtää —
ja se on korjattavissa esitystä muuttamalla.
