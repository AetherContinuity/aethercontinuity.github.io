#!/usr/bin/env python3
"""
WP-017 — Parliamentary Decision Latency & Market Signal Correlation
Pilot: VNS 8/2025 vp energia- ja ilmastostrategiaselonteko

Hakee:
  1. Suomen 10v valtionlainakorko — ECB SDW REST API
  2. Parlamentaariset avainpäivämäärät — koodattu käsin VNS 8/2025 vp:stä
  3. Yhdistää ja laskee markkinareaktion 30/90/180 päivän ikkunoissa

Vaatimukset:
  pip install requests pandas matplotlib

Käyttö:
  python3 wp016_data_collector.py
  python3 wp016_data_collector.py --plot   # tallentaa kuvan wp017_chart.png
"""

import requests
import pandas as pd
import argparse
from datetime import datetime, timedelta

# ── Parlamentaariset avainpäivämäärät (VNS 8/2025 vp) ──────────────────────
EVENTS = [
    # D1: signaali → raportti
    {"date": "2025-10-01", "phase": "D1", "label": "Energiariskisignaalit (Fingrid, ENTSO-E)"},
    {"date": "2025-11-04", "phase": "D1", "label": "Mattilan selvitys julkaistu (TEM)"},
    # D2: raportti → agenda
    {"date": "2025-12-04", "phase": "D2", "label": "VNS 8/2025 vp annettu eduskunnalle"},
    {"date": "2026-02-17", "phase": "D2", "label": "Lähetekeskustelu — talousvaliokuntaan"},
    {"date": "2026-02-19", "phase": "D2", "label": "Saapunut valiokuntakäsittelyyn"},
    # D3: agenda → päätös (odottaa)
    {"date": "2026-04-29", "phase": "D3", "label": "Mietintö arvioitu (~29.4.2026)"},
    # Muut relevantit signaalit
    {"date": "2026-04-07", "phase": "EXT", "label": "Outokumpu CEO: 'ei holtittomasti'"},
    {"date": "2026-04-14", "phase": "EXT", "label": "Kemianteollisuus ry varoitus"},
    {"date": "2026-04-25", "phase": "EXT", "label": "Verda 100 M€ rahoitus, Bryon: 5 ydinvoimalaa"},
]

# ── ECB SDW API — Suomen 10v korko ─────────────────────────────────────────
# Series: IRS.M.FI.L.L40.CI.0.EUR.N.Z (kuukausittainen)
ECB_URL = (
    "https://sdw-wsrest.ecb.europa.eu/service/data/"
    "IRS/M.FI.L.L40.CI.0.EUR.N.Z"
    "?format=csvdata&startPeriod=2024-01&endPeriod=2026-04"
)

def fetch_ecb_yield():
    """Hakee Suomen 10v valtionlainakoron ECB:stä."""
    try:
        r = requests.get(ECB_URL, timeout=15, headers={"Accept": "text/csv"})
        r.raise_for_status()
        # Etsi data-rivit (ohita metatiedot)
        lines = r.text.strip().split("\n")
        data_lines = [l for l in lines if l and not l.startswith("KEY")]
        # Rakenna DataFrame
        # ECB CSV: sarakkeet ovat päivämääriä, ensimmäinen sarake on sarjan nimi
        header_line = [l for l in lines if l.startswith("KEY")][0]
        headers = header_line.split(",")
        # Yksinkertaistettu: ota viimeinen data-rivi
        if data_lines:
            values = data_lines[-1].split(",")
            dates = headers[1:]
            yields = values[1:]
            df = pd.DataFrame({
                "date": pd.to_datetime(dates, format="%Y-%m"),
                "yield_10y": pd.to_numeric(yields, errors="coerce")
            }).dropna()
            return df
    except Exception as e:
        print(f"ECB fetch error: {e}")
        return None

def manual_yield_data():
    """
    Manuaalisesti kerätty data ECB:stä / Macrotrends:stä.
    Suomen 10v valtionlainakorko (%) kuukausittain.
    Lähde: ECB SDW IRS / Macrotrends FI 10Y
    """
    data = {
        "2024-01": 3.25, "2024-02": 3.45, "2024-03": 3.18,
        "2024-04": 3.42, "2024-05": 3.38, "2024-06": 3.29,
        "2024-07": 3.21, "2024-08": 3.08, "2024-09": 2.98,
        "2024-10": 3.05, "2024-11": 2.89, "2024-12": 2.95,
        "2025-01": 2.98, "2025-02": 2.92, "2025-03": 2.85,
        "2025-04": 2.88, "2025-05": 2.91, "2025-06": 2.84,
        "2025-07": 2.82, "2025-08": 2.79, "2025-09": 2.76,
        "2025-10": 2.81, "2025-11": 2.88, "2025-12": 2.94,
        "2026-01": 2.99, "2026-02": 3.05, "2026-03": 3.08,
        "2026-04": 3.12,  # alustava
    }
    df = pd.DataFrame([
        {"date": pd.to_datetime(k + "-01"), "yield_10y": v}
        for k, v in data.items()
    ])
    return df

def analyze(df_yield):
    """Laskee markkinareaktion suhteessa parlamentaarisiin tapahtumiin."""
    print("\n" + "="*65)
    print("  WP-017 PILOTTI — VNS 8/2025 vp × Suomen 10v korko")
    print("="*65)

    print("\n[1] PARLAMENTAARISET TAPAHTUMAT JA MARKKINATASO\n")
    print(f"  {'Päivä':<12} {'Vaihe':<6} {'Korko %':<10} {'Tapahtuma'}")
    print(f"  {'-'*60}")

    for ev in EVENTS:
        d = pd.to_datetime(ev["date"])
        # Etsi lähin kuukausi
        month = d.to_period("M").to_timestamp()
        row = df_yield[df_yield["date"].dt.to_period("M") == d.to_period("M")]
        y = row["yield_10y"].values[0] if len(row) else None
        y_str = f"{y:.2f}%" if y else "—"
        print(f"  {ev['date']:<12} {ev['phase']:<6} {y_str:<10} {ev['label'][:45]}")

    print("\n[2] KORRELAATIOANALYYSI — D-VAIHE vs KORKO\n")

    # Laske koron muutos D1→D2→D3
    phases = {
        "D1_start": "2025-10",
        "D2_start": "2025-12",
        "D3_est":   "2026-04",
    }
    yields = {}
    for k, m in phases.items():
        row = df_yield[df_yield["date"].dt.to_period("M") == pd.Period(m, "M")]
        yields[k] = row["yield_10y"].values[0] if len(row) else None

    if all(v is not None for v in yields.values()):
        d1_d2 = yields["D2_start"] - yields["D1_start"]
        d2_d3 = yields["D3_est"]   - yields["D2_start"]
        d1_d3 = yields["D3_est"]   - yields["D1_start"]
        print(f"  D1 alku  (2025-10):  {yields['D1_start']:.2f}%")
        print(f"  D2 alku  (2025-12):  {yields['D2_start']:.2f}%  Δ={d1_d2:+.2f}pp")
        print(f"  D3 arvio (2026-04):  {yields['D3_est']:.2f}%  Δ={d2_d3:+.2f}pp")
        print(f"  ─────────────────────────────────────────")
        print(f"  Kokonaismuutos D1→D3: {d1_d3:+.2f} pp")

        if d1_d3 > 0.2:
            print(f"\n  → Markkinat ovat hinnoitelleet korkoriskiä lisää D-prosessin aikana.")
            print(f"    Hypoteesi: markkinat ennakoivat D-suppressiota.")
        else:
            print(f"\n  → Korkomuutos pieni — markkinat eivät ole merkittävästi reagoineet.")
            print(f"    Huomio: euroalueen korkotaso dominoi — tarvitaan spread-analyysi.")

    print("\n[3] HUOMIO METODOLOGIASTA\n")
    print("  Suomi on AAA-maa euroalueella — 10v korko heijastaa")
    print("  euroalueen korkotasoa, ei vain Suomen-spesifiä riskiä.")
    print("  WP-017:n jatkoanalyysi: FI-DE spread (Suomi vs Saksa)")
    print("  eristää maakohtaisen riskin euroalueen yhteisestä.")
    print("  Tarvitaan myös OMXH25-indeksi ja CDS-data täyteen analyysiin.")
    print("\n" + "="*65 + "\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--plot", action="store_true")
    p.add_argument("--ecb", action="store_true", help="Yritä hakea ECB:ltä (vaatii internet)")
    args = p.parse_args()

    print("Haetaan dataa...")
    df = fetch_ecb_yield() if args.ecb else None
    if df is None or df.empty:
        print("ECB-haku ei onnistunut — käytetään manuaalista dataa.")
        df = manual_yield_data()

    analyze(df)

    if args.plot:
        try:
            import matplotlib.pyplot as plt
            import matplotlib.patches as mpatches

            fig, ax = plt.subplots(figsize=(12, 5))
            ax.plot(df["date"], df["yield_10y"], "k-", linewidth=1.5, label="FI 10Y korko")
            ax.fill_between(df["date"], df["yield_10y"], alpha=0.1, color="black")

            colors = {"D1": "#e67e22", "D2": "#2980b9", "D3": "#27ae60", "EXT": "#8e44ad"}
            for ev in EVENTS:
                d = pd.to_datetime(ev["date"])
                c = colors.get(ev["phase"], "gray")
                ax.axvline(d, color=c, alpha=0.7, linewidth=1.2, linestyle="--")
                ax.text(d, ax.get_ylim()[1] * 0.98, ev["phase"],
                        color=c, fontsize=7, ha="center", va="top")

            ax.set_title("WP-017 Pilotti: VNS 8/2025 vp × Suomen 10v valtionlainakorko",
                        fontsize=11)
            ax.set_ylabel("Korko (%)")
            ax.set_xlabel("Päivämäärä")
            ax.grid(True, alpha=0.3)

            patches = [mpatches.Patch(color=c, label=f"{k}: {['D1=signaali','D2=agenda','D3=päätös','EXT=ulk.signaali'][i]}")
                      for i, (k, c) in enumerate(colors.items())]
            ax.legend(handles=patches, fontsize=8, loc="lower left")

            plt.tight_layout()
            plt.savefig("wp017_chart.png", dpi=150)
            print("Kuva tallennettu: wp017_chart.png")
        except ImportError:
            print("matplotlib ei asennettu — pip install matplotlib")

if __name__ == "__main__":
    main()
