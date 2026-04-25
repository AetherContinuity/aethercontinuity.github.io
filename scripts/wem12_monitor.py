#!/usr/bin/env python3
"""
WEM §12 — Energiaindeksin seurantaskripti
Proxy: https://aci-fingrid-proxy.ruotsalainen-marko.workers.dev/api

Käyttö:
  python3 wem12_v2.py              # 72h tase
  python3 wem12_v2.py --hours 24  # 24h ikkuna
  python3 wem12_v2.py --csv       # lisää CSV-lokiin

Raspberry Pi crontab:
  0 * * * * python3 /home/pi/wem12_v2.py --csv >> /home/pi/wem12.log 2>&1
"""
import requests, argparse, csv, os, sys
from datetime import datetime, timedelta, timezone

PROXY = "https://aci-fingrid-proxy.ruotsalainen-marko.workers.dev/api"

# Fingrid dataset IDs
DS = {
    "production":    192,
    "consumption":   193,
    "net_import":    198,   # pos=vienti, neg=tuonti
    "wind":          181,
    "frequency":     177,
    "shortage":      336,   # 0=normaali, 1-3=hälytys
    "spot":          105,   # €/MWh
    "se1_transfer":   24,   # SE1→FI MW
    "bat_charge":    398,
    "bat_discharge": 399,
}

def fetch(ds_id, hours=2):
    end   = datetime.now(timezone.utc)
    start = end - timedelta(hours=hours)
    try:
        r = requests.get(PROXY, params={
            "datasets":  ds_id,
            "startTime": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "endTime":   end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "format": "json", "sortBy": "startTime",
            "sortOrder": "asc", "pageSize": 20000,
        }, timeout=15)
        r.raise_for_status()
        return r.json().get("data", [])
    except Exception as e:
        print(f"  [virhe] DS {ds_id}: {e}", file=sys.stderr)
        return []

def latest(ds_id):
    data = fetch(ds_id, hours=2)
    return data[-1]["value"] if data else None

def mwh(ds_id, hours):
    """Kumulatiivinen MWh — 3min pisteet → 0.05h/piste"""
    data = fetch(ds_id, hours=hours)
    return round(sum(d.get("value",0) for d in data) * (3/60), 1) if data else 0.0

def run(hours=72, csv_log=False):
    now = datetime.now()
    print(f"\n{'='*58}")
    print(f"  WEM §12 Energiaindeksi  |  {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*58}")

    # Reaaliaikaiset
    print("\n[1] REAALIAIKAISET MITTAUKSET")
    rt = {k: latest(v) for k, v in DS.items()}

    def row(label, val, unit="MW", lo=None, hi=None):
        if val is None: print(f"  {label:<30} [ei dataa]"); return
        flag = " ⚠️" if (lo and val<lo) or (hi and val>hi) else ""
        print(f"  {label:<30} {val:>9.1f} {unit}{flag}")

    row("Tuotanto:",         rt["production"])
    row("Kulutus:",          rt["consumption"])
    row("Nettosiirto:",      rt["net_import"],  warn_below=-2000)
    row("  SE1→FI (DS24):", rt["se1_transfer"])
    row("Tuulivoima:",       rt["wind"])
    row("Taajuus:",          rt["frequency"], "Hz", lo=49.9, hi=50.1)
    row("Spot:",             rt["spot"], "€/MWh")
    if rt["shortage"] is not None:
        s = {0:"normaali",1:"varoitus",2:"hälytys",3:"kriisi"}.get(int(rt["shortage"]),"?")
        print(f"  {'Pula-asema:':<30} {int(rt['shortage']):>9}    ({s})")

    # 72h kumulatiivinen
    print(f"\n[2] {hours}H KUMULATIIVINEN ENERGIATASE")
    p  = mwh("production",  hours)
    c  = mwh("consumption", hours)
    n  = mwh("net_import",  hours)
    s1 = mwh("se1_transfer",hours)
    balance = p - c - n

    print(f"  {'Tuotanto:':<32} {p:>10.0f} MWh")
    print(f"  {'SE1-tuonti (DS24):':<32} {s1:>10.0f} MWh")
    print(f"  {'Nettosiirto (DS198):':<32} {n:>+10.0f} MWh")
    print(f"  {'Kulutus:':<32} {c:>10.0f} MWh")
    print(f"  {'─'*44}")
    print(f"  {'NETTOTASE:':<32} {balance:>+10.0f} MWh")
    if c > 0 and s1:
        print(f"  {'SE1-riippuvuus kulutuksesta:':<32} {abs(s1)/c*100:>9.1f} %")

    # Indeksiarvio
    print(f"\n[3] WEM §12 INDEKSIARVIO ({hours}h)")
    st = rt["shortage"]
    fr = rt["frequency"]
    if st is not None and int(st) >= 2:
        arvio = "🔴  KRIITTINEN — pula-asema aktiivinen"
    elif fr is not None and fr < 49.9:
        arvio = "🔴  KRIITTINEN — taajuus alhaalla"
    elif balance < -10000:
        arvio = "🔴  VAKAVA VAJE"
    elif balance < -3000:
        arvio = "⚠️   ALIJÄÄMÄINEN — merkittävä tuontitarve"
    elif balance < 0:
        arvio = "🟡  LIEVÄ VAJE — normaali tuontitilanne"
    else:
        arvio = "✅  POSITIIVINEN — omavaraisuus ikkunassa"
    print(f"  {arvio}")
    print(f"\n{'='*58}\n")

    if csv_log:
        fname = "wem12_log.csv"
        row_d = {"timestamp": now.isoformat(),
                 "prod_rt": rt["production"], "cons_rt": rt["consumption"],
                 "net_rt": rt["net_import"],  "se1_rt": rt["se1_transfer"],
                 "freq": rt["frequency"],     "shortage": rt["shortage"],
                 "spot": rt["spot"],
                 f"prod_{hours}h": p, f"cons_{hours}h": c,
                 f"net_{hours}h": n, f"se1_{hours}h": s1,
                 f"balance_{hours}h": balance}
        hdr = not os.path.exists(fname)
        with open(fname, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=row_d.keys())
            if hdr: w.writeheader()
            w.writerow(row_d)
        print(f"  Tallennettu: {fname}")

    return balance

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--hours", type=int, default=72)
    p.add_argument("--csv",   action="store_true")
    a = p.parse_args()
    run(a.hours, a.csv)
