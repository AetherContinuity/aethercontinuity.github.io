"""SM-023 v0.3: kiinteistöveron haarukka Haminan rakennusten kiinteistöverosta (Verohallinto kive_301).
Havainnollistus, ei ennakkokirjattu tulos. Haku ACI PxWeb -proxyn kautta."""
import json, itertools, urllib.request
P = "https://aci-pxweb-proxy.ruotsalainen-marko.workers.dev/?up=vero&p=Vero/Kiinteistoverot/kive_301.px"
Q = {"query": [
    {"code": "Alue", "selection": {"filter": "item", "values": ["075", "285", "505", "000"]}},
    {"code": "Rakennustyyppi", "selection": {"filter": "item", "values": ["SSSSSS", "5", "16", "4"]}},
    {"code": "Tiedot", "selection": {"filter": "item", "values": ["Arvo_vero", "Arvo_verotusarvo", "Arvo_jalleenhankinta"]}}],
    "response": {"format": "json-stat2"}}
OUT = "tools/data/ekasvu/raw/vero_kive_301_hamina.json"

def hae():
    r = urllib.request.Request(P, data=json.dumps(Q).encode(), headers={"Content-Type": "application/json", "User-Agent": "curl/8.5.0"})
    d = json.load(urllib.request.urlopen(r)); json.dump(d, open(OUT, "w")); return d

def taulu(d):
    ids = d["id"]; dims = [sorted(d["dimension"][k]["category"]["index"], key=d["dimension"][k]["category"]["index"].get) for k in ids]
    return {tuple(c): v for c, v in zip(itertools.product(*dims), d["value"])}

if __name__ == "__main__":
    t = taulu(hae())
    g = lambda r, y, k: t[("075", r, y, k)] / 1e6
    tv14 = g("5", "2014", "Arvo_verotusarvo") + g("16", "2014", "Arvo_verotusarvo")
    tv26 = g("5", "2026", "Arvo_verotusarvo") + g("16", "2026", "Arvo_verotusarvo")
    vero26 = g("5", "2026", "Arvo_vero") + g("16", "2026", "Arvo_vero")
    pros = vero26 / tv26
    print(f"Hamina teollisuus+muut: verotusarvo 2014 {tv14:.1f} -> 2026 {tv26:.1f} M€, vero 2026 {vero26:.2f} M€ ({pros:.2%})")
    print(f"Lisäys 2014->2026 nykyprosentilla {(tv26-tv14)*pros:.2f} M€/v; brutto {vero26:.2f} M€/v; kaikki rakennukset 2026 {g('SSSSSS','2026','Arvo_vero'):.2f} M€")
    print(f"Jälleenhankinta-arvo teollisuus 2014 {g('5','2014','Arvo_jalleenhankinta'):.0f} -> 2026 {g('5','2026','Arvo_jalleenhankinta'):.0f} M€")
