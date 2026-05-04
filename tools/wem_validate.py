#!/usr/bin/env python3
"""
WEM Validation Script — vertaa WEM-parametrit Fingrid API-arvoihin
Käyttö: python3 wem_validate.py
Tarvitsee: requests, python-dotenv (pip install requests)
API-avain: aseta FINGRID_API_KEY ympäristömuuttujaan
"""

import requests
import json
from datetime import datetime, timedelta, timezone

# Tarkistettavat datasetit
DATASETS = {
    124: ("Kulutus", 5000, 15000),
    192: ("Kokonaistuotanto", 4000, 14000),
    188: ("Ydinvoima", 1500, 4500),
    191: ("Vesivoima", 100, 5000),
    181: ("Tuulivoima", 0, 7000),
    201: ("CHP kaukolämpö", 500, 5000),
    202: ("CHP teollisuus", 200, 3000),
}

def fetch_latest(ds_id, api_key):
    """Hakee viimeisimmän arvon Fingrid API:sta"""
    now = datetime.now(timezone.utc)
    start = (now - timedelta(hours=2)).strftime('%Y-%m-%dT%H:%M:%SZ')
    end = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    url = f"https://data.fingrid.fi/api/datasets/{ds_id}/data"
    headers = {"x-api-key": api_key}
    params = {"startTime": start, "endTime": end, "format": "json", "pageSize": 10}
    
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        data = r.json().get("data", [])
        if data:
            vals = [d["value"] for d in data if d.get("value") is not None]
            return sum(vals) / len(vals) if vals else None
    except Exception as e:
        return f"VIRHE: {e}"
    return None

def run_validation(api_key):
    print(f"\n{'='*60}")
    print(f"WEM Validation — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")
    
    all_ok = True
    for ds_id, (name, min_val, max_val) in DATASETS.items():
        val = fetch_latest(ds_id, api_key)
        
        if isinstance(val, str):  # virhe
            print(f"❌ DS {ds_id} ({name}): {val}")
            all_ok = False
        elif val is None:
            print(f"⚠️  DS {ds_id} ({name}): ei dataa")
            all_ok = False
        elif val < min_val or val > max_val:
            print(f"⚠️  DS {ds_id} ({name}): {val:.0f} MW — EPÄREALISTINEN (odotus {min_val}–{max_val} MW)")
            all_ok = False
        else:
            print(f"✅ DS {ds_id} ({name}): {val:.0f} MW — OK")
    
    print(f"\n{'='*60}")
    if all_ok:
        print("✅ Kaikki parametrit kunnossa")
    else:
        print("⚠️  Tarkista yllä merkityt parametrit")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    import os
    api_key = os.environ.get("FINGRID_API_KEY", "")
    if not api_key:
        print("Aseta FINGRID_API_KEY ympäristömuuttuja")
        print("Rekisteröi: https://data.fingrid.fi/en/instructions")
        print()
        print("Ilman API-avainta: avaa WEM selaimessa ja tarkista")
        print("sanity check -varoitukset status-barissa.")
    else:
        run_validation(api_key)
