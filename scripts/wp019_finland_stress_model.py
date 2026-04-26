"""
WP-019 — Finland Sovereign Stress Model 2026-2032
Anchored to official Valtiokonttori data

Key fix: interest cost uses portfolio repricing mechanics from VK-SENSITIVITY
  averageFixing = 5.43 years → 18.4% reprices annually
  Effective cost = (1 - repricing_share) * i_legacy + repricing_share * i_market
"""
import json, random
random.seed(42)

# ── OFFICIAL ANCHORS (Valtiokonttori) ──────────────────────────────
D0           = 187.7   # mrd €, central gov debt end-2025 (VK-DEBT-GDP)
GDP0         = 187.7 / 0.667   # = 281.4 mrd €
INTEREST_25  = 3.013   # mrd € actual 2025 (VK-INTEREST)
INTEREST_26B = 3.246   # mrd € budget 2026 (TAE 2026)
AVG_FIXING   = 5.43    # years (VK-SENSITIVITY March 2026)
REPRICING    = 1/AVG_FIXING  # = 18.4%/year

# Implied effective rate from actuals
I_EFF_25 = INTEREST_25 / D0   # = 1.6% (legacy portfolio, still mostly cheap bonds)

print("="*70)
print("  SUOMI STRESSIMALLI 2026–2032 — v1.0")
print("  Ankkuri: Valtiokonttori viralliset luvut (VK-DEBT-GDP, VK-INTEREST,")
print("           VK-SENSITIVITY). CC BY 4.0")
print("="*70)
print(f"\n  D₀  = €{D0:.1f}mrd (66.7% BKT, end-2025)")
print(f"  GDP₀= €{GDP0:.1f}mrd")
print(f"  i_eff_2025 = {I_EFF_25*100:.2f}% (legacy portfolio average)")
print(f"  averageFixing = {AVG_FIXING}v → {REPRICING*100:.1f}% reprices/year")
print(f"  Budget 2026 korkomenot = €{INTEREST_26B}mrd (TAE 2026 validation)")

# ── INTEREST COST MODEL ──────────────────────────────────────────────
def interest_cost(D, i_eff_prev, i_market):
    """
    Effective interest cost using VK-SENSITIVITY repricing mechanics:
    - (1-18.4%) of portfolio continues at previous effective rate
    - 18.4% reprices to current market rate
    Returns: (interest_mrd, new_i_eff)
    """
    i_eff_new = (1 - REPRICING) * i_eff_prev + REPRICING * i_market
    cost = i_eff_new * D
    return cost, i_eff_new

# Validate 2026: i_market ~3.2%, i_eff_25=1.6%
cost_26, i_eff_26 = interest_cost(D0, I_EFF_25, 0.032)
print(f"\n  Validation 2026: model={cost_26:.3f}mrd€ | budget={INTEREST_26B}mrd€ "
      f"→ {'✓ match' if abs(cost_26-INTEREST_26B)<0.3 else f'diff={cost_26-INTEREST_26B:+.2f}'}")

# ── SCENARIOS ────────────────────────────────────────────────────────
scenarios = {
    "Optimistinen": {
        "g_nom": 0.035,
        "i_market": [0.028, 0.026, 0.025, 0.025, 0.025, 0.025, 0.025],
        "pd_pct": 0.015,
    },
    "Baseline stress": {
        "g_nom": 0.025,
        "i_market": [0.032, 0.034, 0.036, 0.037, 0.038, 0.038, 0.038],
        "pd_pct": 0.025,
    },
    "Kriisi R2→R3": {
        "g_nom": 0.015,
        "i_market": [0.038, 0.045, 0.052, 0.055, 0.055, 0.052, 0.050],
        "pd_pct": 0.035,
    }
}

YEARS = list(range(2025, 2033))
results = {}

for name, p in scenarios.items():
    D = D0; GDP = GDP0; i_eff = I_EFF_25
    path = [{"year": 2025, "debt": D, "gdp": GDP, "ratio": round(D/GDP*100,1),
             "interest": INTEREST_25, "pd": None, "i_eff_pct": round(i_eff*100,2)}]
    for t in range(7):
        interest, i_eff = interest_cost(D, i_eff, p["i_market"][t])
        pd = p["pd_pct"] * GDP
        D = D + pd + interest
        GDP = GDP * (1 + p["g_nom"])
        path.append({"year": YEARS[t+1], "debt": round(D,1), "gdp": round(GDP,1),
                     "ratio": round(D/GDP*100,1), "interest": round(interest,2),
                     "pd": round(pd,2), "i_eff_pct": round(i_eff*100,2)})
    results[name] = path

# ── PRINT TABLE ───────────────────────────────────────────────────────
for name, path in results.items():
    print(f"\n  {'─'*68}")
    print(f"  {name.upper()}")
    print(f"  {'Vuosi':>6} {'BKT':>8} {'Velka':>8} {'V/BKT':>8} {'Korko':>8} "
          f"{'i_eff':>7} {'PD':>6}")
    print(f"  {'':>6} {'mrd€':>8} {'mrd€':>8} {'%':>8} {'mrd€':>8} {'%':>7} {'mrd€':>6}")
    print(f"  {'─'*68}")
    for r in path:
        pd_s = f"{r['pd']:.1f}" if r['pd'] else "—"
        print(f"  {r['year']:>6} {r['gdp']:>8.1f} {r['debt']:>8.1f} "
              f"{r['ratio']:>7.1f}% {r['interest']:>8.2f} "
              f"{r['i_eff_pct']:>6.2f}% {pd_s:>6}")

# ── STABILITY ─────────────────────────────────────────────────────────
print(f"\n{'='*70}")
print("  STABIILISUUSANALYYSI — Domar-ehto")
print(f"  Debt stabilizes when: PD ≤ (g - i_eff) × D")
print(f"{'='*70}")
print(f"\n  {'Skenaario':<18} {'g':>6} {'i_eff_32':>9} {'g−i':>6} {'Velka_32':>10} {'Stable?':>10}")
for name, path in results.items():
    r32 = path[-1]
    g = scenarios[name]["g_nom"]
    i32 = r32['i_eff_pct']/100
    gi = g - i32
    stable = "✗ KASVAA" if gi < 0 else "✓"
    print(f"  {name:<18} {g*100:>5.1f}% {i32*100:>8.2f}% {gi*100:>5.1f}% "
          f"{r32['debt']:>8.1f}mrd {stable:>10}")

# ── KEY PHASE THRESHOLDS ──────────────────────────────────────────────
print(f"\n  FAASIT (baseline stress):")
bs = results["Baseline stress"]
for r in bs:
    ratio = r['ratio']
    if ratio < 70: phase = "R1 — hallittavissa"
    elif ratio < 80: phase = "R1/R2 — paineet kasvavat"
    elif ratio < 90: phase = "R2 — fiskaalinen kitka"
    elif ratio < 100: phase = "R2/R3 — markkinapaine nousee"
    else: phase = "R3 — kriisialue"
    if r['year'] in [2025,2027,2029,2031]:
        print(f"    {r['year']}: {ratio:.1f}% → {phase}")

with open('/home/claude/repo/scripts/wp019_stress_results.json', 'w') as f:
    json.dump({
        'model': 'Finland Sovereign Stress Model 2026-2032 v1.0',
        'anchors': {'D0': D0, 'GDP0': round(GDP0,1), 'i_eff_2025_pct': round(I_EFF_25*100,2),
                    'avg_fixing_years': AVG_FIXING, 'repricing_annual_pct': round(REPRICING*100,1)},
        'validation_2026': {'model_mrd': round(cost_26,3), 'budget_mrd': INTEREST_26B},
        'scenarios': results
    }, f, indent=2)
print(f"\n  Saved: wp019_stress_results.json")

# ── MONTE CARLO ───────────────────────────────────────────────────────
print(f"\n{'='*70}")
print("  MONTE CARLO — 5000 simulaatiota (baseline stress ±shokit)")
print(f"{'='*70}")

N = 5000
target_year = 2032
results_mc = {"debt_ratios_2032": [], "interest_2032": [], "above_90": 0, "above_100": 0}

for _ in range(N):
    D = D0; GDP = GDP0; i_eff = I_EFF_25
    for t in range(7):
        # Stochasticize around baseline
        g_t = 0.025 + random.gauss(0, 0.010)       # ±1% kasvu-sokki
        i_m = 0.032 + 0.002*t + random.gauss(0, 0.008)  # ±80bps korko-sokki
        i_m = max(0.015, min(0.070, i_m))           # bounds
        pd_t = (0.025 + random.gauss(0, 0.005)) * GDP

        interest, i_eff = interest_cost(D, i_eff, i_m)
        D = D + pd_t + interest
        GDP = GDP * (1 + g_t)

    ratio = D/GDP*100
    results_mc["debt_ratios_2032"].append(ratio)
    results_mc["interest_2032"].append(interest)
    if ratio > 90: results_mc["above_90"] += 1
    if ratio > 100: results_mc["above_100"] += 1

ratios = sorted(results_mc["debt_ratios_2032"])
p10 = ratios[int(0.10*N)]
p50 = ratios[int(0.50*N)]
p90 = ratios[int(0.90*N)]

print(f"\n  Velka/BKT 2032 (N={N}):")
print(f"    P10 (optimistinen):   {p10:.1f}%")
print(f"    P50 (mediaani):       {p50:.1f}%")
print(f"    P90 (stressi):        {p90:.1f}%")
print(f"\n  Todennäköisyydet:")
print(f"    P(velka/BKT > 90%)  = {results_mc['above_90']/N*100:.0f}%")
print(f"    P(velka/BKT > 100%) = {results_mc['above_100']/N*100:.0f}%")
print(f"\n  Johtopäätös:")
print(f"    Mediaanipolussa velka/BKT {p50:.0f}% — lähellä 1990-luvun kriisihuippua")
print(f"    90. persentiilin polussa {p90:.0f}% — historiallisesti ennenkuulumatonta rauhanaikana")

# Add MC results to JSON
import json
with open('/home/claude/repo/scripts/wp019_stress_results.json', 'r') as f:
    data = json.load(f)
data['monte_carlo'] = {
    'n_simulations': N, 'shock_params': {'g_std': 0.010, 'i_std': 0.008},
    'debt_ratio_2032': {'p10': round(p10,1), 'p50': round(p50,1), 'p90': round(p90,1)},
    'prob_above_90pct': round(results_mc['above_90']/N*100,0),
    'prob_above_100pct': round(results_mc['above_100']/N*100,0)
}
with open('/home/claude/repo/scripts/wp019_stress_results.json', 'w') as f:
    json.dump(data, f, indent=2)
print(f"\n  MC results added to wp019_stress_results.json")
