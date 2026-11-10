# Ennakkokirjaus W3: SE1/FI-hintasuhde, keskiero ja BCI (|FI−SE1| > 0,5 €/MWh) tallennetuista sarjoista
from _lue import sarja
fi=sarja('da-fi-2025-11_2026-10.json'); se=sarja('da-se1-2025-11_2026-10.json')
ks=sorted(k for k in fi if k in se); n=len(ks)
mf=sum(fi[k] for k in ks)/n; ms=sum(se[k] for k in ks)/n
bci=sum(1 for k in ks if abs(fi[k]-se[k])>0.5)/n
print("n %d · FI ka %.2f · SE1 ka %.2f · suhde %.3f · keskiero %.2f · BCI %.1f %%"%(n,mf,ms,ms/mf,mf-ms,100*bci))
