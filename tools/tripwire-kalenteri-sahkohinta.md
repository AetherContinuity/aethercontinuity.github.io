# Tripwire-kalenteri — kuuden elementin sähkönhintaskenaariomalli

**Tila:** Käyttäjän oma rakenne 2026-07-29, täydennetty kahdella puuttuvalla
kohdalla samana päivänä. Tämä muuttaa aiemman kertaluonteisen kuuden
elementin analyysin (ks. keskustelu 2026-07-29) jatkuvasti päivittyväksi
seurantatyökaluksi.

## Kuusi elementtiä ja niiden tripwire-tahti

| # | Elementti | Tripwire-tahti | Mitä seurataan | Lähde/tapa |
|---|---|---|---|---|
| 1 | Kysyntä (datakeskukset) | Neljännesvuosittain | Uudet investointipäätökset, kokonais-MW-putki | HS/Nordea-tyyppiset koosteartikkelit, Fingridin liittymäjono |
| 2 | Firm-kapasiteetti (ydin+hydro) | Puolivuosittain | OL-huoltoseisokit, uudet SMR-päätökset | TVO, WEM §07 (jo seurattu) |
| 3 | Säätyvä kapasiteetti | Neljännesvuosittain | Wärtsilän ja muiden tilauskirja, uudet FI-tilaukset | Wärtsilän omat lehdistötiedotteet (huom: julkaisevat Q-tahtiin) |
| 4 | Tuontiventtiili (SE1) | Kuukausittain (TRR) + puolivuosittain (hankkeet) | TRR-lukema; Stegra/HYBRIT-ramppi, uudet SE1-hankkeet | **WEM §12 suoraan** (TRR jo reaaliaikainen) + uutisseuranta |
| 5 | Laitetoimitusrajoite | Neljännesvuosittain | Wärtsilän oma tilauskirja/toimitusaikojen piteneminen | Sama lähde kuin #3 |
| 6 | Geopolitiikka/kaasu/päästöoikeus | **Kuukausittain** | TTF-kaasu, EUA-päästöoikeus, Suomen spot ja volatiliteetti | TTF-futuurit, EU ETS -hintaseuranta |

## Täydennys A — puuttunut oma sarake: sääntelykalenteri (siirto + vero)

Ei seurata markkinatahtiin, koska **ei liiku markkinan mukana vaan omalla,
päätöksentekosidonnaisella syklillään** (ks. 2026-07-29 korjattu keskustelu
siitä miksi "siirto vakiona" -oletus oli virheellinen):

| Mitä | Tahti | Miksi |
|---|---|---|
| Energiaviraston valvontajakson päätökset | Kerran/nelivuotiskausi (nykyinen 2024–2031) | Tuottokattomallin oma sykli |
| Sähköveron/huoltovarmuusmaksun muutosilmoitukset | Aina kun hallitus/eduskunta ilmoittaa (ei ennakoitavissa tahtina) | Ks. huhtikuun 2026 korotus — ei säännöllinen, vaan tapahtumapohjainen |
| Verkkoyhtiöiden tehomaksu-käyttöönotot | Puolivuosittain | Uusi, tammikuun 2026 määräys — käyttöönotto vaihtelee yhtiöittäin |

## Täydennys B — talvikauden jälkeinen validointi (käyttäjän oma neljäs kohta)

Tämä on rakenteellisesti sama periaate kuin WEM:n oma backtest (§09) —
**ex-post-tarkistus, ei ennuste**:

1. Kuinka monta todellista niukkuustuntia (SP-määritelmä, WEM §06) toteutui?
2. Osuiko niukkuus samoihin viikkoihin kuin malli ennakoi (esim. kylmä+tyyni-yhdistelmä)?
3. Mikä kuudesta elementistä selitti eniten toteutunutta poikkeamaa ennusteesta?
4. Päivitä seuraavan talven mallin painotukset tämän perusteella.

## Miksi tämä toimii — sama periaate kuin ACI:n muissa instrumenteissa

Tämä rakenne vastaa täsmälleen sitä mitä HEM/BEM-E ja WEM jo tekevät kukin
omalla tavallaan: **erottele nopeasti liikkuvat markkinasignaalit
(kuukausittain), hitaammat rakenteelliset päätökset (neljännes/puolivuosi),
ja hitaimmat regulaatio-/investointisyklit (vuosi+) — älä sekoita niitä
samaan tarkistustahtiin.** Sama virhe jonka teimme siirron kanssa (pidimme
sitä vakiona vaikka se liikkuu, mutta eri tahtiin kuin energiahinta) olisi
toistunut koko mallissa ilman tätä eksplisiittistä tahdistusta.

## Ei vielä tehty

Tämä on rakenne, ei vielä toimiva työkalu. Ei sisällä automaatiota,
hälytysrajoja (esim. "TTF > X € = päivitä Korkea-skenaario") eikä
integraatiota mihinkään ACI-instrumenttiin. Nämä ovat luonnollisia
seuraavia askeleita jos rakennetta halutaan viedä pidemmälle.
