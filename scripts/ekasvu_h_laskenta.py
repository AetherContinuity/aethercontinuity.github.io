"""Ennakkokirjaus H: osittainen fiskaalinen vaikutus julkisyhteisöihin 2030,
rinnakkaislaskenta (datakeskustaso D × hankevaihe P × ajoitus × oletukset).
Säännöt: SEURANTA.md, H ja lisäys 1 (jäädytys 17.11.2026). Vain vakiokirjasto.
[M] lähde, [L] laskettu, [A] oletus."""
import itertools, json

H = 8760
H2 = 55.0                                   # MWh/t H2 [A] (G lisäys 2)
D0 = 3.8                                    # TWh, perusura
DC_TASOT = {"D0 TEM": 3.8, "D0b Statnett": 4.0, "D1a tiekartta": 5.0, "D1b tiekartta": 6.0,
            "D2a ET": 11.0, "D2b ET": 18.0, "D3 SM-022": 17.5}

# Hankeliite (lisäys 1). cod2030 = käyttöönotto 2030 -> ajoituskerroin t
def hankkeet(cf):
    return [  # nimi, taso, TWh, hyvitys M€ (kohdistettu), työpaikat, cod2030
        ("Freija",      "P1", 160 * H * cf / 1e6,            110.6,       100, False),
        ("Arctic Sisu", "P1", 56.1e3 * H2 / 1e6 / 3,         150.0 / 3,   100, True),
        ("VolagHy",     "P1", 50e3 * 0.5 * H2 / 1e6,         150.0,       100, True),
        ("ETFuels",     "P2", 300 * H * cf / 1e6,            118.6,        60, True),
        ("Plug site 1", "P2", 87 * H * cf / 1e6,              44.2,        40, True),
        ("Plug site 2", "P2", 207 * H * cf / 1e6,            105.8,        94, True),
    ]
TASOT = {"P0": [], "P1": ["P1"], "P2": ["P1", "P2"]}

# Verot ja maksut [M]
SV_I, SV_II, HVM = 22.4, 0.5, 0.85          # €/MWh
YV_DC = 11.6e3 / (8760 * 0.8)               # €/MWh (SM-022 kululisämalli)
YV_P2X_YLA = 18.9                           # €/MWh (verot_304 ryhmä 24)
YV_VALTIO = 0.7715                          # jako 2026
PALKKA = 60e3                               # € [A]
PER_TP = {"valtio": 0.12 * PALKKA, "kunnat": 0.07 * PALKKA,
          "tyoelake": 0.244 * PALKKA,
          "muut_sosrahastot": (0.0123 + 0.0089 + 0.0191 + 0.0088) * PALKKA}

def solu(dc_taso, p, t=0.5, nettouusi=0.5, yv_p2x=0.0, cf=0.6, dc_tp_per_twh=120):
    dDC = dc_taso - D0
    sek = {"valtio": 0.0, "kunnat": 0.0, "tyoelake": 0.0, "muut_sosrahastot": 0.0}
    # datakeskukset
    sek["valtio"] += dDC * (SV_I + HVM)
    yv = dDC * YV_DC
    sek["valtio"] += yv * YV_VALTIO; sek["kunnat"] += yv * (1 - YV_VALTIO)
    tp = dDC * dc_tp_per_twh
    # P2X
    p2x_twh = 0.0; hyv_vah = 0.0
    for nimi, taso, twh, hyv, tpp, cod30 in hankkeet(cf):
        if taso not in TASOT[p]: continue
        k = t if cod30 else 1.0
        if k == 0: continue
        e = twh * k
        p2x_twh += e
        sek["valtio"] += e * (SV_II + HVM)
        brutto = e * yv_p2x
        vah = min(brutto, 0.10 * hyv * k)       # hankekohtainen raja
        hyv_vah += vah
        netto = brutto - vah
        sek["valtio"] += netto * YV_VALTIO; sek["kunnat"] += netto * (1 - YV_VALTIO)
        tp += tpp * k
    for s in sek:
        if s in PER_TP: sek[s] += tp * nettouusi * PER_TP[s] / 1e6
    return {"sek": sek, "summa": sum(sek.values()), "p2x_twh": p2x_twh, "dDC": dDC,
            "tyopaikat": tp, "hyvitys_vahennys": hyv_vah,
            "menetetty_II": p2x_twh * (SV_I - SV_II)}

def bkt_2030():
    b = 281.783e3
    for g in (0.008, 0.017, 0.017, 0.015, 0.015): b *= (1 + g) * 1.02
    return b

if __name__ == '__main__':
    ERO = 0.014 * bkt_2030()
    print(f"Vertailuero ≈ {ERO:.0f} M€\n")
    print("PÄÄARVO (t 50 %, nettouusi 50 %, P2X-yhteisövero 0, käyttöaste 60 %, DC 120 tp/TWh), M€ / % vertailuerosta")
    print(f"{'':16}" + "".join(f"{p:>16}" for p in TASOT))
    rivit = []
    for dn, dv in DC_TASOT.items():
        cells = [solu(dv, p) for p in TASOT]
        print(f"{dn:16}" + "".join(f"{c['summa']:8.0f} {c['summa']/ERO:6.1%} " for c in cells))
    print("\nVÄLIT (kaikki yhdistelmät: t 0/50/100, nettouusi 0/50/100, yv 0/yläraja, cf 40/60/80, DC tp 120/400)")
    tulos = {}
    for dn, dv in DC_TASOT.items():
        rivi = []
        for p in TASOT:
            vals = [solu(dv, p, t, n, y, c, j)['summa'] for t, n, y, c, j in itertools.product(
                (0, 0.5, 1), (0, 0.5, 1), (0, YV_P2X_YLA), (0.4, 0.6, 0.8), (120, 400))]
            pa = solu(dv, p)
            tulos[f"{dn}|{p}"] = {"paa": pa['summa'], "min": min(vals), "max": max(vals), "sek": pa['sek'],
                                  "p2x_twh": pa['p2x_twh'], "tyopaikat": pa['tyopaikat']}
            rivi.append(f"{min(vals):5.0f}–{max(vals):<5.0f}")
        print(f"{dn:16}" + "".join(f"{r:>16}" for r in rivi))
    print("\nALASEKTORIT, pääarvo (M€): valtio / kunnat / työeläkelaitokset / muut sosiaaliturvarahastot")
    for key in ("D0 TEM|P1", "D0 TEM|P2", "D1b tiekartta|P1", "D2b ET|P2", "D3 SM-022|P2"):
        s = tulos[key]['sek']
        print(f"  {key:20} {s['valtio']:6.1f} / {s['kunnat']:5.1f} / {s['tyoelake']:5.1f} / {s['muut_sosrahastot']:4.1f}")
    for p in TASOT:
        c = solu(3.8, p)
        print(f"\n{p}: P2X {c['p2x_twh']:.2f} TWh, työpaikat {c['tyopaikat']:.0f}, hyvitysvähennys {c['hyvitys_vahennys']:.1f} M€, menetetty luokan II vero {c['menetetty_II']:.0f} M€", end="")
    print()
    json.dump({"vertailuero": ERO, "solut": tulos}, open("tools/data/ekasvu/h_tulos_2026-11-17.json", "w"), ensure_ascii=False, indent=1)
