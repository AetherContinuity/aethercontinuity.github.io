#!/usr/bin/env python3
"""Ennakkokirjaus E (SEURANTA.md, commit 7231759): altiste Δ ja ennustelista.
Δ = ka(NDCI 2021–2023) − ka(NDCI 2018–2020); ≥2 kelvollista vuotta kummassakin puoliskossa.
Kelvollinen vuosi = /lake-timeseries palautti NDCI-arvon (ei null).
Ennustelista = Δ:n ylin neljännes (kvartiiliraja numpy.percentile 75, Δ ≥ raja).
Aja: python3 scripts/bem_e_vh4_delta.py <vh4_ndci.json> tools/data/bem-e/vh4/
"""
import json, sys, pathlib, numpy as np
RAW, OUTD = sys.argv[1], pathlib.Path(sys.argv[2])
J = {x['vpdtunnus']: x for x in json.load(open(OUTD / 'vh4_jarvet.json')) if x.get('mukana')}
R = json.load(open(RAW))
rows, pois = [], []
for k in sorted(J):
    y = {r['y']: r['ndci'] for r in R[k]['rows'] if r['ndci'] is not None}
    a = [y[v] for v in (2018, 2019, 2020) if v in y]; b = [y[v] for v in (2021, 2022, 2023) if v in y]
    if len(a) < 2 or len(b) < 2:
        pois.append({'vpdtunnus': k, 'nimi': J[k]['nimi'], 'syy': f'kelvollisia vuosia {len(a)}+{len(b)}'}); continue
    rows.append({'vpdtunnus': k, 'nimi': J[k]['nimi'], 'kunta': J[k]['kunta'], 'ely': J[k]['ely'],
                 'tila_3kausi': J[k]['tila_3kausi'], 'ryhma': J[k]['ryhma'],
                 'ndci': {str(v): round(y[v], 4) for v in sorted(y)},
                 'ka_2018_20': round(float(np.mean(a)), 4), 'ka_2021_23': round(float(np.mean(b)), 4),
                 'delta': round(float(np.mean(b) - np.mean(a)), 4)})
d = np.array([r['delta'] for r in rows]); q = float(np.percentile(d, 75))
for r in rows: r['ylin_neljannes'] = bool(r['delta'] >= q)
rows.sort(key=lambda r: -r['delta'])
out = {'ennakkokirjaus': 'SEURANTA.md E (commit 7231759, 30.10.2026)', 'laskettu': '2026-10-30',
       'menetelma': 'aci-corine-proxy /lake-timeseries, NDCI touko–syys P10D-mediaani; Δ = ka(2021–23) − ka(2018–20)',
       'n_otos': len(J), 'n_mukana': len(rows), 'n_pois': len(pois), 'pois': pois,
       'kvartiiliraja_75': round(q, 4), 'n_ylin_neljannes': sum(r['ylin_neljannes'] for r in rows),
       'delta_jakauma': {'mediaani': round(float(np.median(d)), 4), 'p25': round(float(np.percentile(d, 25)), 4),
                         'min': round(float(d.min()), 4), 'max': round(float(d.max()), 4)},
       'jarvet': rows}
json.dump(out, open(OUTD / 'vh4_delta.json', 'w'), ensure_ascii=False, indent=1)
lista = [{k: r[k] for k in ('vpdtunnus', 'nimi', 'kunta', 'ely', 'tila_3kausi', 'delta')} for r in rows if r['ylin_neljannes']]
json.dump({'ennakkokirjaus': out['ennakkokirjaus'], 'julkaistu': '2026-10-30', 'kvartiiliraja_75': out['kvartiiliraja_75'],
           'ennuste': 'Näissä järvissä 4. kauden ekologisen tilan heikkenemisosuus on suurempi kuin muissa (E2).',
           'jarvet': lista}, open(OUTD / 'vh4_ennustelista.json', 'w'), ensure_ascii=False, indent=1)
print({k: out[k] for k in ('n_otos', 'n_mukana', 'n_pois', 'kvartiiliraja_75', 'n_ylin_neljannes', 'delta_jakauma')})
