# TN-022 §05: S-2-solmun lisäkate toteutuneilla day-ahead-hinnoilla + moottorivoimalan day-ahead-kate
import statistics as st
from _lue import sarja
from datetime import datetime,timezone
pts=sarja('da-fi-2025-11_2026-10.json')
rows=sorted((datetime.fromisoformat(k.replace('Z','+00:00')),v) for k,v in pts.items())
t0=datetime(2025,11,1,tzinfo=timezone.utc); t1=datetime(2026,11,1,tzinfo=timezone.utc)
rows=[(t,p) for t,p in rows if t0<=t<t1]
# gaps
exp=int((t1-t0).total_seconds()/900)
print("15 min -pisteitä",len(rows),"odotettu",exp)
p=[x[1] for x in rows]; n=len(p); dt=0.25
print("keskihinta %.1f  mediaani %.1f  min %.1f  max %.1f"%(sum(p)/n,st.median(p),min(p),max(p)))
print("osuus <=0: %.1f %%   <=5: %.1f %%   >=100: %.1f %%  >=200: %.1f %%"%tuple(100*sum(1 for x in p if c(x))/n for c in (lambda x:x<=0,lambda x:x<=5,lambda x:x>=100,lambda x:x>=200)))
# validointi SM-020: 17.1.-17.2.2026
w=[x for t,x in rows if datetime(2026,1,17,tzinfo=timezone.utc)<=t<datetime(2026,2,17,8,tzinfo=timezone.utc)]
print("17.1.-17.2.2026 keskihinta %.0f (SM-020: 159)"%(sum(w)/len(w)))
s=sorted(p)
def mean_low(h): k=int(h/dt); return sum(s[:k])/k
def mean_high(h): k=int(h/dt); return sum(s[-k:])/k
for h in (1000,2000,3000,4000,5000,6000): print("halvimmat %d h: %.1f"%(h,mean_low(h)))
for h in (100,300,500,700,1000,1500): print("kalleimmat %d h: %.1f"%(h,mean_high(h)))
# --- TN-022 S-2
P_EL=20.0;ETA=0.65*0.78;HEAT_REC=0.30;ENG_E=0.45;ENG_H=0.40;GRID=5.0;CO2=0.198*50
HAKE=27/0.90;FOM=0.03*90;RES=1.5;ANN=90*0.06/(1-1.06**-20);P_ENG=20.0
print("\nTN-022 S-2 toteutuneilla hinnoilla (varasto rajoittamaton, täydellinen ennakointi)")
print("elektrolyysi h | sähkö GWh | SNG GWh | moottori h | ostohinta | myyntihinta | lisäkate M€ | pääomakulun jälkeen")
best=None
for h in (500,1000,2000,3000,4000,5000,6000,8784):
    h=min(h,n*dt); E=P_EL*h/1000; sng=E*ETA; pe=mean_low(h)
    eout=sng*ENG_E; heng=eout*1000/P_ENG; heng=min(heng,n*dt); pp=mean_high(heng)
    cost=E*(pe+GRID)/1000+sng*CO2/1000+FOM
    rev=eout*pp/1000+(E*HEAT_REC+sng*ENG_H)*HAKE/1000+RES
    eb=rev-cost
    print("%6d | %6.0f | %5.1f | %5.0f | %5.1f | %6.1f | %+5.1f | %+5.1f"%(h,E,sng,heng,pe,pp,eb,eb-ANN))
# --- pelkkä moottori ostopolttoaineella
print("\nMoottorivoimala ostopolttoaineella, day-ahead-kate per MW (hyötysuhde 45 %, muuttuva O&M 8 €/MWh)")
for name,fuel in (("LNG 45 €/MWh",45),("LNG 60 €/MWh",60),("biometaani 90 €/MWh",90),("biometaani 120 €/MWh",120)):
    mc=fuel/0.45+8
    hrs=sum(dt for x in p if x>mc); mar=sum((x-mc)*dt for x in p if x>mc)
    print("%-22s rajakustannus %5.0f €/MWh  käyttötunnit %5.0f  kate %6.0f €/kW/v"%(name,mc,hrs,mar/1000))
print("moottorin pääomakulu 1000 €/kW, 6 %%, 20 v: %.0f €/kW/v + kiinteä O&M ~20"%(1000*0.06/(1-1.06**-20)))
