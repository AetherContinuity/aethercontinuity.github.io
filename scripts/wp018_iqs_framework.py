"""
WP-018 — Integration Quality Score (IQS)
Pilot framework: three cases

IQS = weighted sum of four dimensions, each scored 0–10.

Dimension weights (v0.1, theoretical priors):
  D1 Physical capacity     w=0.15  (size of investment — partially bond-visible)
  D2 Systemic linkage      w=0.40  (integration layer — bond-invisible, core)
  D3 Policy anchor         w=0.30  (legislative/strategic mandate — bond-invisible)
  D4 Export potential      w=0.15  (commercial pathway — partially visible)

IQS = 0.15·D1 + 0.40·D2 + 0.30·D3 + 0.15·D4

Scoring rubric (each dimension 0–10):
  0–2:  Absent or nascent — no evidence of integration
  3–4:  Planned — announced but not operationalised
  5–6:  Partial — some elements operational, gaps remain
  7–8:  Substantial — operational with documented gaps
  9–10: Full — integrated, governed, commercially active
"""

DIMENSIONS = {
    "D1": {
        "name": "Physical capacity",
        "weight": 0.15,
        "indicators": [
            "Installed or committed MW/GW",
            "Capacity factor / utilisation",
            "Grid connection status",
        ]
    },
    "D2": {
        "name": "Systemic linkage",
        "weight": 0.40,
        "indicators": [
            "Demand-response / flexibility framework (binding or voluntary?)",
            "Industrial coupling (offtake agreements, PtX pipeline, waste heat)",
            "Grid balancing participation",
            "Cross-sector integration (energy ↔ industry ↔ transport)",
        ]
    },
    "D3": {
        "name": "Policy anchor",
        "weight": 0.30,
        "indicators": [
            "Legislative mandate (capacity mechanism, integration obligation)",
            "National strategy with measurable targets",
            "State ownership or formal mandate",
            "EU funding integration (RRF, CEF, IPCEI)",
        ]
    },
    "D4": {
        "name": "Export potential",
        "weight": 0.15,
        "indicators": [
            "Commercial export pathway operational",
            "International partnerships or PPAs",
            "Technology export (IP, manufacturer base)",
        ]
    }
}

CASES = {
    "FI_wind": {
        "label": "Finland — Onshore wind (7,000 MW)",
        "D1": None,  # to be scored
        "D2": None,
        "D3": None,
        "D4": None,
    },
    "FI_dc": {
        "label": "Finland — Data centres (500 MW op. / 3–5 GW pipeline)",
        "D1": None,
        "D2": None,
        "D3": None,
        "D4": None,
    },
    "DK_orsted": {
        "label": "Denmark — Ørsted offshore wind (~5 GW + Bornholm)",
        "D1": None,
        "D2": None,
        "D3": None,
        "D4": None,
    }
}

def iqs(scores):
    return round(
        0.15 * scores["D1"] +
        0.40 * scores["D2"] +
        0.30 * scores["D3"] +
        0.15 * scores["D4"], 2
    )

if __name__ == "__main__":
    print("IQS Framework v0.1 — WP-018 Pilot")
    print("="*55)
    for dim, info in DIMENSIONS.items():
        print(f"\n{dim} — {info['name']} (w={info['weight']})")
        for ind in info['indicators']:
            print(f"  · {ind}")
    print("\n" + "="*55)
    print("Cases to score:")
    for k, v in CASES.items():
        print(f"  {k}: {v['label']}")
