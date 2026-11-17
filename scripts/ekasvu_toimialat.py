"""Jalostusarvo, palkat ja yhteisövero per sähkö-GWh toimialaryhmittäin (Tilastokeskuksen tene-ryhmät).
[M] Tilastokeskus 12bu, 15ad; Verohallinto verot_304; [L] tässä."""
import json, itertools

def lue(name):
    d = json.load(open(f"tools/data/ekasvu/raw/{name}.json"))
    ids = d["id"]; dims = d["dimension"]
    axes = []
    for k in ids:
        idx = dims[k]["category"]["index"]
        axes.append(sorted(idx, key=idx.get))
    out = {}
    for combo, v in zip(itertools.product(*axes), d["value"]):
        out[combo] = v
    return ids, out

# tene-ryhmä -> (ntp-koodit, vero-koodit)
RYHMAT = {
    "01": ("Kaivostoiminta (B)", ["B"], ["B"]),
    "02": ("Elintarvike (10-12)", ["C10TC12"], ["10", "11", "12"]),
    "04": ("Metsäteollisuus (16-17)", ["C16_C17"], ["16", "17"]),
    "05": ("Kemia (19-22)", ["C19TC22"], ["19", "20", "21", "22"]),
    "06": ("Metallien jalostus (24)", ["C24"], ["24"]),
    "07": ("Kone- ja metallituote (25,28-30,33)", ["C25", "C28", "C29", "C30", "C33"], ["25", "28", "29", "30", "33"]),
    "08": ("Elektroniikka (26-27)", ["C26_C27"], ["26", "27"]),
    "09": ("Muu (18,23,31,32)", ["C18", "C23", "C31_C32"], ["18", "23", "31", "32"]),
    "SS": ("Teollisuus ja kaivos yhteensä", ["B", "C"], ["B", "C"]),
}
VUODET = ["2022", "2023", "2024"]

_, sahko = lue("sahko")
_, ntp = lue("arvonlisays")
_, vero = lue("yhteisovero")

def s(y, g): return sahko[(y, "SSS", g, "sahko_gwh")]
def n(y, codes, tt): return sum(ntp[("S1", tt, c, y, "ntp-cp")] or 0 for c in codes)
def v(y, codes): return sum((vero[("VEROT_70", y, c, "Sum")] or 0) for c in codes) / 1e6

SAHKOVERO_II, SAHKOVERO_I = 0.5, 22.4  # €/MWh [M]
rivit = []
print(f"{'Ryhmä':38}{'GWh':>8}{'AL M€':>8}{'AL €/MWh':>10}{'Palkat €/MWh':>13}{'Yht.vero €/MWh':>15}{'Sähkövero II €/MWh':>8}")
for g, (nimi, nc, vc) in RYHMAT.items():
    gwh = sum(s(y, g) for y in VUODET) / 3
    al = sum(n(y, nc, "B1GPH") for y in VUODET) / 3
    pk = sum(n(y, nc, "D1K") for y in VUODET) / 3
    yv = sum(v(y, vc) for y in VUODET) / 3
    mwh = gwh * 1e3
    r = dict(g=g, nimi=nimi, gwh=gwh, al=al, pk=pk, yv=yv,
             al_mwh=al * 1e6 / mwh, pk_mwh=pk * 1e6 / mwh, yv_mwh=yv * 1e6 / mwh,
             verotuki_meur=mwh * (SAHKOVERO_I - SAHKOVERO_II) / 1e6)
    rivit.append(r)
    print(f"{nimi:38}{gwh:8.0f}{al:8.0f}{r['al_mwh']:10.0f}{r['pk_mwh']:13.0f}{r['yv_mwh']:15.1f}   verotuki {r['verotuki_meur']:5.0f} M€")
json.dump(rivit, open("tools/data/ekasvu/tulos_toimialat.json", "w"), ensure_ascii=False, indent=1)
print("\nKeskiarvo 2022-2024. AL = bruttoarvonlisäys perushintaan, palkat = palkansaajakorvaukset (D1K).")
