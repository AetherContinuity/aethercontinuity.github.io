#!/usr/bin/env python3
"""AMOC-monitorin SST <-> RAPID -toistotesti (5.10.2026).

Kysymys: toistuuko 31.7.2026 raportoitu yhteys (SST-anomalia 60N 30W
edeltaa RAPID:n MOC-kuljetusta 11 vrk, r=0.525) muina vuosina ja
sailyyko se, kun kausisykli poistetaan?

Syotteet (repositoriossa):
  tools/rapid_daily.json              RAPID v2024.1a, paivakeskiarvot
  tools/data/amoc-sst-daily.json      SST-anomalia, CRW, 2004-2024
  tools/data/amoc-nao-2023-2024.json  NAO, ikkuna 2023-2024
Tuloste:
  tools/data/amoc-sst-rapid-results.json  (sivu lukee taman)

Menetelma on sama kuin aci-amoc-proxyn /compare-reitissa: Pearson r
viiveittain, tehollinen otoskoko koko ACF:sta (Pyper & Peterman 1998,
katkaisu min(N/5, 30)), p-arvo t-jakaumasta df=Neff-2, Benjamini-
Hochberg alpha=0.05. Lisaksi vaihesatunnaistettu surrogaattitesti
(suurin |r| kaikkien viiveiden yli, 2000 toistoa, kiintea siemen).
Etumerkki: viive < 0 tarkoittaa, etta sarja A edeltaa sarjaa B.

Aja: python3 scripts/amoc_sst_rapid_analysis.py
"""
import json, datetime as dt, pathlib
import numpy as np
from scipy import stats

ROOT = pathlib.Path(__file__).resolve().parent.parent
rng = np.random.default_rng(20261005)

R = json.load(open(ROOT / 'tools/rapid_daily.json'))
S = json.load(open(ROOT / 'tools/data/amoc-sst-daily.json'))['data']
NAO = json.load(open(ROOT / 'tools/data/amoc-nao-2023-2024.json'))['data']

D0, D1 = dt.date(2004, 4, 7), dt.date(2024, 3, 22)
N = (D1 - D0).days + 1
dates = [D0 + dt.timedelta(days=i) for i in range(N)]
keys = [str(d) for d in dates]
idx = keys.index

def rapid(c):
    return np.array([(R.get(k) or {}).get(c) if (R.get(k) or {}).get(c) is not None else np.nan for k in keys], float)

moc, ek = rapid('moc'), rapid('ek')
sst = np.array([S.get(k, np.nan) for k in keys], float)
nao = np.array([NAO.get(k, np.nan) for k in keys], float)
doy = np.array([d.timetuple().tm_yday for d in dates])

def deseason(x):
    """Poista paivittainen klimatologia (31 vrk:n ikkuna, koko jakso)."""
    clim = np.array([np.nanmean(x[(np.abs(doy - j) <= 15) | (np.abs(doy - j) >= 350)]) for j in range(1, 367)])
    return x - clim[doy - 1]

def pear(x, y):
    ok = ~(np.isnan(x) | np.isnan(y))
    if ok.sum() < 10:
        return np.nan
    return float(np.corrcoef(x[ok], y[ok])[0, 1])

def acf(x, k):
    x = x[~np.isnan(x)]
    return 0.0 if k >= len(x) - 2 else float(np.corrcoef(x[:-k], x[k:])[0, 1])

def neff(x, y, mmax=30):
    ok = ~(np.isnan(x) | np.isnan(y)); x, y = x[ok], y[ok]
    n = len(x); m = min(n // 5, mmax)
    den = 1 + 2 * sum(acf(x, k) * acf(y, k) for k in range(1, m + 1))
    return float(max(2, min(n, n / den if den > 0 else n)))

def p_t(r, n):
    if n < 3 or abs(r) >= 1:
        return float('nan')
    t = r * np.sqrt((n - 2) / (1 - r * r))
    return float(2 * stats.t.sf(abs(t), n - 2))

def bh_significant(ps, alpha=0.05):
    ps = np.array(ps); m = len(ps); order = np.argsort(ps)
    passed = np.where(ps[order] <= (np.arange(1, m + 1) / m) * alpha)[0]
    k = 0 if len(passed) == 0 else passed.max() + 1
    return sorted(int(i) for i in order[:k])

def lagged(a, b, lag):
    if lag < 0: return a[:lag], b[-lag:]
    if lag > 0: return a[lag:], b[:-lag]
    return a, b

def scan(a, b, i0, i1, L=30, mmax=30):
    wa, wb = a[i0:i1 + 1], b[i0:i1 + 1]
    ne = neff(wa, wb, mmax)
    lags = list(range(-L, L + 1))
    rs = [pear(*lagged(wa, wb, l)) for l in lags]
    ps = [p_t(r, ne) for r in rs]
    sig = bh_significant(ps)
    best = int(np.nanargmax(np.abs(rs)))
    return {
        'neff': round(ne, 1), 'r0': round(rs[lags.index(0)], 3),
        'paras_viive': lags[best], 'paras_r': round(rs[best], 3), 'paras_p': round(ps[best], 4),
        'bh_merkitsevia': len(sig), 'viiveita': len(lags),
        'bh_viiveet': [lags[i] for i in sig],
        'spektri': [{'viive': l, 'r': round(r, 4), 'p': round(p, 5)} for l, r, p in zip(lags, rs, ps)],
    }

def surrogate(x):
    z = x.copy(); z[np.isnan(z)] = np.nanmean(x)
    f = np.fft.rfft(z - z.mean()); ph = rng.uniform(0, 2 * np.pi, len(f)); ph[0] = 0
    return np.fft.irfft(np.abs(f) * np.exp(1j * ph), n=len(z))

def surrogate_p(a, b, L, n=2000):
    def max_abs_r(x, y):
        return np.nanmax(np.abs([pear(*lagged(x, y, l)) for l in range(-L, L + 1)]))
    obs = max_abs_r(a, b)
    # Yksi surrogaatti per toisto, sama sarja kaikille viiveille.
    mx = np.array([max_abs_r(a, surrogate(b)) for _ in range(n)])
    return round(float(np.mean(mx >= obs)), 3), round(float(np.quantile(mx, 0.95)), 3)

def slim(s):
    return {k: v for k, v in s.items() if k != 'spektri'}

mocA, ekA, sstA, restA = deseason(moc), deseason(ek), deseason(sst), deseason(moc - ek)
out = {
    'ajettu': '2026-10-05',
    'skripti': 'scripts/amoc_sst_rapid_analysis.py',
    'menetelma': 'Pearson viiveittain; Neff koko ACF:sta (katkaisu min(N/5,30)); p t-jakaumasta df=Neff-2; Benjamini-Hochberg alpha=0.05; viive<0 = SST edeltaa',
    'aineisto': {'paivia': N, 'alku': keys[0], 'loppu': keys[-1], 'sst': 'CRW noaacrwsstanomalyDaily 60N 30W', 'rapid': 'RAPID v2024.1a'},
}

# A. Alkuperainen ikkuna
i0, i1 = idx('2023-02-21'), idx('2024-03-22')
out['alkuperainen_ikkuna'] = {'alku': keys[i0], 'loppu': keys[i1], **scan(sst, moc, i0, i1)}
sp, q95 = surrogate_p(sst[i0:i1 + 1], moc[i0:i1 + 1], 30)
out['alkuperainen_ikkuna']['surrogaatti_p'] = sp
out['alkuperainen_ikkuna']['surrogaatti_95'] = q95
out['alkuperainen_ikkuna_kausisykli_poistettu'] = slim(scan(sstA, mocA, i0, i1))

# B. Ekman-erottelu samassa ikkunassa
out['ekman_erottelu'] = {
    'sst_vs_ekman': slim(scan(sst, ek, i0, i1)),
    'sst_vs_moc_miinus_ekman': slim(scan(sst, moc - ek, i0, i1)),
}

# C. Vuosittainen toisto: 396 vrk:n ikkuna, loppu 22.3. kunakin vuonna
years = []
for y in range(2006, 2025):
    e = idx(f'{y}-03-22'); s = e - 395
    raw, an = scan(sst, moc, s, e), scan(sstA, mocA, s, e)
    r11 = lambda sc: next(p['r'] for p in sc['spektri'] if p['viive'] == -11)
    years.append({
        'vuosi': y, 'alku': keys[s], 'loppu': keys[e],
        'raaka': {**slim(raw), 'r_viive_m11': round(r11(raw), 3)},
        'kausisykli_poistettu': {**slim(an), 'r_viive_m11': round(r11(an), 3)},
    })
out['vuosittain'] = years
def summ(key):
    rs = [y[key]['r_viive_m11'] for y in years]
    pos = sum(1 for r in rs if r > 0)
    return {
        'vuosia': len(years),
        'bh_merkitsevia_vuosia': sum(1 for y in years if y[key]['bh_merkitsevia'] > 0),
        'r_m11_positiivisia': pos, 'r_m11_mediaani': round(float(np.median(rs)), 3),
        'merkkitesti_p': round(float(stats.binomtest(pos, len(rs)).pvalue), 3),
    }
out['vuosittain_yhteenveto'] = {'raaka': summ('raaka'), 'kausisykli_poistettu': summ('kausisykli_poistettu')}

# D. Koko jakso, paivaanomaliat
out['koko_jakso_paiva'] = {
    'sst_vs_moc': slim(scan(sstA, mocA, 0, N - 1, L=60, mmax=365)),
    'sst_vs_ekman': slim(scan(sstA, ekA, 0, N - 1, L=60, mmax=365)),
    'sst_vs_moc_miinus_ekman': slim(scan(sstA, restA, 0, N - 1, L=60, mmax=365)),
}

# E. Koko jakso, kuukausianomaliat + surrogaattitesti
ym = np.array([d.year * 12 + d.month for d in dates]); months = np.unique(ym)
def monthly(x):
    return np.array([np.nanmean(x[ym == m]) if np.sum(~np.isnan(x[ym == m])) >= 15 else np.nan for m in months])
mS = monthly(sstA)
out['koko_jakso_kuukausi'] = {}
for name, series in (('sst_vs_moc', mocA), ('sst_vs_ekman', ekA), ('sst_vs_moc_miinus_ekman', restA)):
    mB = monthly(series)
    lags = list(range(-12, 13)); rs = [pear(*lagged(mS, mB, l)) for l in lags]
    best = int(np.nanargmax(np.abs(rs))); ne = neff(mS, mB, mmax=48)
    sp, q95 = surrogate_p(mS, mB, 12)
    out['koko_jakso_kuukausi'][name] = {
        'kuukausia': int(len(months)), 'neff': round(ne), 'r0': round(rs[lags.index(0)], 3),
        'paras_viive_kk': lags[best], 'paras_r': round(rs[best], 3), 'paras_p': round(p_t(rs[best], ne), 4),
        'surrogaatti_p': sp, 'surrogaatti_95': q95,
    }

# F. NAO <-> Ekman samassa ikkunassa, t-jakaumalla (aiemmin normaaliapproksimaatio)
out['nao_vs_ekman'] = {
    'laaja_61_viivetta': slim(scan(nao, ek, i0, i1)),
    'kapea_7_viivetta': slim(scan(nao, ek, i0, i1, L=3)),
    'huom': 'Kapea ikkuna rajattiin 31.7.2026 vasta laajan skannauksen jalkeen; ei riippumaton vahvistus.',
}

json.dump(out, open(ROOT / 'tools/data/amoc-sst-rapid-results.json', 'w'), ensure_ascii=False, indent=1)
a = out['alkuperainen_ikkuna']
print('Alkuperainen ikkuna: r=%.3f viive=%d Neff=%.1f p=%.4f BH %d/%d surrogaatti-p=%.3f' % (
    a['paras_r'], a['paras_viive'], a['neff'], a['paras_p'], a['bh_merkitsevia'], a['viiveita'], a['surrogaatti_p']))
print('Sama, kausisykli poistettu:', out['alkuperainen_ikkuna_kausisykli_poistettu'])
print('Vuosittain:', json.dumps(out['vuosittain_yhteenveto'], ensure_ascii=False))
print('Koko jakso paiva:', {k: (v['paras_r'], v['paras_viive'], v['bh_merkitsevia']) for k, v in out['koko_jakso_paiva'].items()})
print('Koko jakso kk:', json.dumps(out['koko_jakso_kuukausi'], ensure_ascii=False))
print('Ekman-erottelu:', {k: (v['paras_r'], v['paras_viive'], v['bh_merkitsevia']) for k, v in out['ekman_erottelu'].items()})
print('NAO-Ekman:', {k: (v['paras_r'], v['paras_viive'], v['neff'], v['paras_p'], v['bh_merkitsevia'], v['viiveita']) for k, v in out['nao_vs_ekman'].items() if k != 'huom'})
