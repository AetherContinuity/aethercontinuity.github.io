# Tuulen saama hinta (capture) suhteessa keskihintaan
from _lue import sarja
da=sarja('da-fi-2025-11_2026-10.json')
w=sarja('wind-fi-2025-11_2026-10.json')
keys=sorted(k for k in w if k in da and '2025-11-01'<=k[:10]<'2026-11-01')
n=len(keys); P=[da[k] for k in keys]; W=[w[k] for k in keys]
mean=sum(P)/n; cap=sum(p*x for p,x in zip(P,W))/sum(W)
print("yhteisiä vartteja",n)
print("tuulituotanto %.1f TWh, keskiteho %.0f MW, max %.0f, min %.0f"%(sum(W)*0.25/1e6,sum(W)/n,max(W),min(W)))
print("keskihinta %.1f  tuulen saama hinta %.1f  suhde %.2f"%(mean,cap,cap/mean))
# tuulen kvartiilit
idx=sorted(range(n),key=lambda i:W[i]); q=n//4
for name,sl in (("tyynin neljännes",idx[:q]),("2.",idx[q:2*q]),("3.",idx[2*q:3*q]),("tuulisin neljännes",idx[3*q:])):
    print("%-20s tuuli ka %5.0f MW  hinta ka %6.1f"%(name,sum(W[i] for i in sl)/len(sl),sum(P[i] for i in sl)/len(sl)))
mx=sum(P)/n; mw=sum(W)/n
cov=sum((p-mx)*(x-mw) for p,x in zip(P,W)); r=cov/(sum((p-mx)**2 for p in P)**.5*sum((x-mw)**2 for x in W)**.5)
print("korrelaatio hinta–tuuli r = %.3f"%r)
