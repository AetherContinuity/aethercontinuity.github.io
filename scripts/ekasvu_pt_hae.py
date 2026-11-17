import json, urllib.request
P="https://aci-pxweb-proxy.ruotsalainen-marko.workers.dev/"
def post(path,q,name):
    body=json.dumps({"query":q,"response":{"format":"json-stat2"}}).encode()
    r=urllib.request.Request(P+"?up=statfin&p="+path,data=body,headers={"Content-Type":"application/json","User-Agent":"curl/8.5.0"})
    d=json.load(urllib.request.urlopen(r,timeout=60)); json.dump(d,open("tools/data/ekasvu/raw/"+name+".json","w")); return d
def sel(c,v): return {"code":c,"selection":{"filter":"item","values":v}}
prods=["25","26","27","28","33","41_43","71"]
post("StatFin/pt/14yp.px",[sel("timeperiod_y",["2023"]),sel("yhdistelma_2_20180101",[p for p in prods if p!="41_43"]),sel("yhdistelma_1_20180101",["P51K"])],"pt_tuonti")
d=json.load(urllib.request.urlopen(urllib.request.Request(P+"?up=statfin&p=StatFin/pt/14ym.px",headers={"User-Agent":"curl/8.5.0"})))
codes=[v for v in d["variables"] if v["code"]=="yhdistelma_2_20180101"][0]["values"]
post("StatFin/pt/14ym.px",[sel("timeperiod_y",["2023"]),sel("yhdistelma_2_20180101",[p for p in prods if p in codes]),sel("yhdistelma_1_20180101",["P51K"])],"pt_kaytto")
d=json.load(urllib.request.urlopen(urllib.request.Request(P+"?up=statfin&p=StatFin/pt/14yt.px",headers={"User-Agent":"curl/8.5.0"})))
rows=[v for v in d["variables"] if v["code"].endswith("rivi")][0]["values"]
post("StatFin/pt/14yt.px",[sel("timeperiod_y",["2022"]),sel("toimiala_79_20180101-toimiala_rivi",rows),sel("toimiala_79_20180101-toimiala_sarake",["C20","C24","J62_J63","F"])],"pt_leontief")
print("ok", [p for p in prods if p in codes])
