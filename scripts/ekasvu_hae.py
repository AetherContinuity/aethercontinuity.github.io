"""Hakee toimialoittaiset luvut energiaintensiivisen kasvun kartoitukseen ACI PxWeb -proxyn kautta.
Vain vakiokirjasto. Tallentaa raakavastaukset tools/data/ekasvu/raw/-hakemistoon."""
import json, os, urllib.request

P = "https://aci-pxweb-proxy.ruotsalainen-marko.workers.dev/"
os.makedirs("tools/data/ekasvu/raw", exist_ok=True)

def post(up, path, query, name):
    body = json.dumps({"query": query, "response": {"format": "json-stat2"}}).encode()
    req = urllib.request.Request(f"{P}?up={up}&p={path}", data=body,
                                 headers={"Content-Type": "application/json", "User-Agent": "curl/8.5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    json.dump(d, open(f"tools/data/ekasvu/raw/{name}.json", "w"), ensure_ascii=False)
    return d

def sel(code, vals):
    return {"code": code, "selection": {"filter": "item", "values": vals}}

TENE = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "SS"]
YRS = ["2022", "2023", "2024"]
post("statfin", "StatFin/tene/12bu.px",
     [sel("timeperiod_y", YRS), sel("alue_22_20180101", ["SSS"]),
      sel("toimiala_500_20110101", TENE), sel("contentscode", ["sahko_gwh"])], "sahko")

NTP = ["B", "C10TC12", "C13TC15", "C16_C17", "C19TC22", "C24", "C25", "C28", "C29", "C30",
       "C33", "C26_C27", "C18", "C23", "C31_C32", "C", "SSS", "D35", "J"]
post("statfin", "StatFin/ntp/15ad.px",
     [sel("sektoriluokitus_7_20230101", ["S1"]),
      sel("taloustoimi_1_20180101", ["B1GPH", "D1K", "B2N", "P51CK"]),
      sel("toimiala_79_20180101", NTP), sel("timeperiod_y", YRS), sel("contentscode", ["ntp-cp"])],
     "arvonlisays")

VERO = ["B", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
        "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "C", "SSS", "D", "J", "63"]
post("vero", "Vero/Elinkeinoverotilasto/verot/verot_304.px",
     [sel("Erä", ["VEROT_70"]), sel("Verovuosi", YRS), sel("Toimiala", VERO), sel("Tunnusluvut", ["Sum"])],
     "yhteisovero")

post("statfin", "StatFin/yrtt/13zn.px",
     [sel("timeperiod_y", YRS), sel("yrtt_tol_2_20210101", ["SSS", "C16_C17", "C24TC30_C33", "C10TC15_C18TC23_C31_C32", "J"]),
      sel("yrityskoko_3_20140101", ["S"]), sel("contentscode", ["suora_maks", "suora_myon"])], "tuet")
print("ok")
