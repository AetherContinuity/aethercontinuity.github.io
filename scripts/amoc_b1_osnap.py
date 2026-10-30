#!/usr/bin/env python3
"""Ennakkokirjaus B1 (SEURANTA.md, 30.10.2026): OSNAP v2023 (8/2014-6/2020).

B1a  SST 60N 30W   <-> OSNAP East MOC, viiveet -6..+6 kk
B1b  OSNAP koko MOC <-> RAPID AMOC sigma0 (v2024-2), viiveet -12..+12 kk
B1c  toistotarkistus: r(ALL, EAST) > r(ALL, WEST)

Kaikki kuukausianomalioina. Menetelma kuten scripts/amoc_sst_rapid_analysis.py:
Pearson viiveittain, Neff koko ACF:sta, p t-jakaumasta df=Neff-2, BH alpha=0.05.
Viive < 0: ensimmainen sarja edeltaa toista.

Aja repon juuresta:
  python3 scripts/amoc_b1_osnap.py OSNAP_MOC_MHT_MFT_TimeSeries_201408_202006_2023.nc \
      RAPID_transports_v2024-2.nc tools/data/amoc-b1-results.json
Datatiedostot ladataan OSNAP:n (Georgia Tech) ja RAPID:n sivuilta; eivat ole repossa.
"""
import json, sys, datetime as dt, pathlib
import numpy as np, netCDF4 as nc
from scipy import stats

ROOT = pathlib.Path(__file__).resolve().parent.parent
OSN, RAP, OUT = sys.argv[1:4]
B = dt.date(1950, 1, 1)

o = nc.Dataset(OSN)
om = [(B + dt.timedelta(days=float(t))) for t in o.variables['TIME'][:]]
okeys = [(d.year, d.month) for d in om]
osn = {v: np.array(o.variables[v][:], float) for v in ('MOC_ALL', 'MOC_EAST', 'MOC_WEST')}

r = nc.Dataset(RAP)
rm = [(B + dt.timedelta(days=float(t))) for t in r.variables['time_1m'][:]]
rap = dict(zip([(d.year, d.month) for d in rm], np.array(r.variables['amoc_sigma0_1m'][:], float)))

S = dict(json.load(open(ROOT / 'tools/data/amoc-sst-daily.json'))['data'])
for k, v in json.load(open(ROOT / 'tools/data/amoc-sst-2024-ext.json'))['data']:
    S.setdefault(k, v)
sst_m = {}
for k, v in S.items():
    y, m = int(k[:4]), int(k[5:7])
    if v is not None:
        sst_m.setdefault((y, m), []).append(v)
sst_m = {k: np.mean(v) for k, v in sst_m.items() if len(v) >= 15}

def anom(keys, vals, clim_keys=None, clim_vals=None):
    """Poista kuukausiklimatologia. Klimatologia annetusta (pidemmasta) sarjasta jos annettu."""
    ck, cv = (clim_keys, clim_vals) if clim_keys is not None else (keys, vals)
    clim = {m: np.nanmean([v for (y, mm), v in zip(ck, cv) if mm == m]) for m in range(1, 13)}
    return np.array([v - clim[m] for (y, m), v in zip(keys, vals)])

def pear(x, y):
    ok = ~(np.isnan(x) | np.isnan(y))
    return np.nan if ok.sum() < 10 else float(np.corrcoef(x[ok], y[ok])[0, 1])

def acf(x, k):
    x = x[~np.isnan(x)]
    return 0.0 if k >= len(x) - 2 else float(np.corrcoef(x[:-k], x[k:])[0, 1])

def neff(x, y, mmax):
    ok = ~(np.isnan(x) | np.isnan(y)); x, y = x[ok], y[ok]
    n = len(x); m = min(n // 5, mmax)
    den = 1 + 2 * sum(acf(x, k) * acf(y, k) for k in range(1, m + 1))
    return float(max(2, min(n, n / den if den > 0 else n)))

def p_t(rr, n):
    if n < 3 or abs(rr) >= 1: return float('nan')
    t = rr * np.sqrt((n - 2) / (1 - rr * rr)); return float(2 * stats.t.sf(abs(t), n - 2))

def bh(ps, alpha=0.05):
    ps = np.array(ps); m = len(ps); o_ = np.argsort(ps)
    pa = np.where(ps[o_] <= (np.arange(1, m + 1) / m) * alpha)[0]
    k = 0 if len(pa) == 0 else pa.max() + 1
    return sorted(int(i) for i in o_[:k])

def lagged(a, b, l):
    if l < 0: return a[:l], b[-l:]
    if l > 0: return a[l:], b[:-l]
    return a, b

def scan(a, b, L):
    ne = neff(a, b, mmax=24)
    lags = list(range(-L, L + 1)); rs = [pear(*lagged(a, b, l)) for l in lags]
    ps = [p_t(x, ne) for x in rs]; sig = bh(ps); best = int(np.nanargmax(np.abs(rs)))
    return {'n': int(np.sum(~np.isnan(a) & ~np.isnan(b))), 'neff': round(ne, 1),
            'r0': round(rs[lags.index(0)], 3), 'paras_viive': lags[best], 'paras_r': round(rs[best], 3),
            'paras_p': round(ps[best], 4), 'max_abs_r': round(float(np.nanmax(np.abs(rs))), 3),
            'bh_merkitsevia': len(sig), 'viiveita': len(lags), 'bh_viiveet': [lags[i] for i in sig],
            'spektri': [{'viive': l, 'r': round(x, 3), 'p': round(p, 4)} for l, x, p in zip(lags, rs, ps)]}

# Anomaliat. OSNAP: oma klimatologia (vain 6 v). RAPID ja SST: koko sarjan klimatologia (kuten §01h).
A = {v: anom(okeys, osn[v]) for v in osn}
rk = sorted(rap); rap_an = dict(zip(rk, anom(rk, [rap[k] for k in rk])))
sk = sorted(sst_m); sst_an = dict(zip(sk, anom(sk, [sst_m[k] for k in sk])))
R = np.array([rap_an.get(k, np.nan) for k in okeys]); SST = np.array([sst_an.get(k, np.nan) for k in okeys])

out = {'ajettu': '2026-10-30', 'ennakkokirjaus': 'SEURANTA.md B1 (commit 60f9b85, 30.10.2026)',
       'aineisto': {'osnap': 'OSNAP v2023, 8/2014-6/2020, %d kk' % len(okeys), 'rapid': 'RAPID v2024-2 amoc_sigma0_1m',
                    'sst': 'CRW 60N 30W, kuukausikeskiarvot'},
       'anomaliat': 'OSNAP oma kuukausiklimatologia (2014-2020); RAPID ja SST koko sarjan klimatologia'}
b1a = scan(SST, A['MOC_EAST'], 6)
b1b = scan(A['MOC_ALL'], R, 12)
out['B1a_sst_vs_osnap_east'] = {**b1a, 'ennuste_piti': b1a['bh_merkitsevia'] == 0}
out['B1b_osnap_all_vs_rapid_sigma0'] = {**b1b, 'ennuste_piti': b1b['bh_merkitsevia'] == 0 and b1b['max_abs_r'] < 0.3}
re_, rw = pear(A['MOC_ALL'], A['MOC_EAST']), pear(A['MOC_ALL'], A['MOC_WEST'])
out['B1c_toisto'] = {'r_all_east': round(re_, 3), 'r_all_west': round(rw, 3), 'toistui': re_ > rw}
# Kuvailevat (ei kirjattu ennusteeksi): raa'at keskiarvot ja samanaikainen raaka korrelaatio
out['kuvailevat'] = {'osnap_all_ka': round(float(np.mean(osn['MOC_ALL'])), 2), 'osnap_east_ka': round(float(np.mean(osn['MOC_EAST'])), 2),
                     'osnap_west_ka': round(float(np.mean(osn['MOC_WEST'])), 2),
                     'rapid_sigma0_ka_samalla_jaksolla': round(float(np.nanmean([rap.get(k, np.nan) for k in okeys])), 2)}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
for k in ('B1a_sst_vs_osnap_east', 'B1b_osnap_all_vs_rapid_sigma0'):
    v = out[k]; print(k, {x: v[x] for x in ('n', 'neff', 'r0', 'paras_viive', 'paras_r', 'paras_p', 'max_abs_r', 'bh_merkitsevia', 'ennuste_piti')})
print('B1c', out['B1c_toisto']); print('kuvailevat', out['kuvailevat'])
