"""Ennakkokirjaus A1 (SEURANTA.md, 27.10.2026): SST 60N 30W vs RAPID MOC v2024-2,
uusi jakso 28.3.-25.11.2024. Menetelma kopioitu scripts/amoc_sst_rapid_analysis.py:sta.

Aja repon juuresta:
  python3 scripts/amoc_a1_v2024_2.py . RAPID_transports_v2024-2.nc \
      tools/data/amoc-sst-2024-ext.json tools/data/amoc-a1-results.json
RAPID_transports_v2024-2.nc ladataan osoitteesta https://rapid.ac.uk/data/data-download
(ei repossa, 6,7 Mt). AMOC-sarja on myos tiedostossa tools/data/rapid-v2024-2.json.
"""
import json,sys,datetime as dt,numpy as np,netCDF4 as nc
from scipy import stats
REPO,NEW,SSTNEW=sys.argv[1:4]
rng=np.random.default_rng(20261027)
S=dict(json.load(open(REPO+'/tools/data/amoc-sst-daily.json'))['data'])
chk=[(k,S[k],v) for k,v in json.load(open(SSTNEW))['data'] if k in S][:5]
print('SST overlap check',chk)
for k,v in json.load(open(SSTNEW))['data']: S.setdefault(k,v)
d=nc.Dataset(NEW); b=dt.date(1950,1,1)
t5=np.array([float(x) for x in d.variables['time_5d'][:]]); a5=np.array(d.variables['amoc_depth_5d'][:],float)
D0,D1=dt.date(2004,4,7),dt.date(2024,11,25)
N=(D1-D0).days+1; dates=[D0+dt.timedelta(days=i) for i in range(N)]; keys=[str(x) for x in dates]; idx=keys.index
tt=np.array([(x-b).days for x in dates],float)
moc=np.interp(tt,t5,a5)
sst=np.array([S.get(k,np.nan) for k in keys],float)
doy=np.array([x.timetuple().tm_yday for x in dates])
def deseason(x):
    clim=np.array([np.nanmean(x[(np.abs(doy-j)<=15)|(np.abs(doy-j)>=350)]) for j in range(1,367)]); return x-clim[doy-1]
def pear(x,y):
    ok=~(np.isnan(x)|np.isnan(y)); return np.nan if ok.sum()<10 else float(np.corrcoef(x[ok],y[ok])[0,1])
def acf(x,k):
    x=x[~np.isnan(x)]; return 0.0 if k>=len(x)-2 else float(np.corrcoef(x[:-k],x[k:])[0,1])
def neff(x,y,mmax=30):
    ok=~(np.isnan(x)|np.isnan(y)); x,y=x[ok],y[ok]; n=len(x); m=min(n//5,mmax)
    den=1+2*sum(acf(x,k)*acf(y,k) for k in range(1,m+1)); return float(max(2,min(n,n/den if den>0 else n)))
def p_t(r,n):
    if n<3 or abs(r)>=1: return float('nan')
    t=r*np.sqrt((n-2)/(1-r*r)); return float(2*stats.t.sf(abs(t),n-2))
def bh(ps,alpha=0.05):
    ps=np.array(ps); m=len(ps); o=np.argsort(ps); pa=np.where(ps[o]<=(np.arange(1,m+1)/m)*alpha)[0]; k=0 if len(pa)==0 else pa.max()+1
    return sorted(int(i) for i in o[:k])
def lagged(a,b,l):
    if l<0: return a[:l],b[-l:]
    if l>0: return a[l:],b[:-l]
    return a,b
def scan(a,b,i0,i1,L=30,mmax=30):
    wa,wb=a[i0:i1+1],b[i0:i1+1]; ne=neff(wa,wb,mmax); lags=list(range(-L,L+1))
    rs=[pear(*lagged(wa,wb,l)) for l in lags]; ps=[p_t(r,ne) for r in rs]; sig=bh(ps); best=int(np.nanargmax(np.abs(rs)))
    return dict(n=i1-i0+1,neff=round(ne,1),r_m11=round(rs[lags.index(-11)],3),p_m11=round(ps[lags.index(-11)],4),
                paras_viive=lags[best],paras_r=round(rs[best],3),paras_p=round(ps[best],4),bh_merkitsevia=len(sig),bh_viiveet=[lags[i] for i in sig])
def surrogate(x):
    z=x.copy(); z[np.isnan(z)]=np.nanmean(x); f=np.fft.rfft(z-z.mean()); ph=rng.uniform(0,2*np.pi,len(f)); ph[0]=0
    return np.fft.irfft(np.abs(f)*np.exp(1j*ph),n=len(z))
def surrogate_p(a,b,L,n=2000):
    mar=lambda x,y: np.nanmax(np.abs([pear(*lagged(x,y,l)) for l in range(-L,L+1)]))
    obs=mar(a,b); mx=np.array([mar(a,surrogate(b)) for _ in range(n)]); return round(float(np.mean(mx>=obs)),3)
i0,i1=idx('2024-03-28'),idx('2024-11-25')
out={'ajettu':'2026-10-27','ennakkokirjaus':'SEURANTA.md A1 (commit ce69575, 27.10.2026)',
 'poikkeamat':['RAPID v2024-2 julkaisee vain 5 vrk ja kuukausiarvot (ei 12 h / paivasarjaa); paivasarja interpoloitu lineaarisesti 5 vrk:n arvoista','Viimeinen 5 vrk:n arvo 25.11.2024, joten jakso paattyy 25.11. eika 30.11.','Uudessa tiedostossa ei ole komponentteja (Ekman, UMO, Golfvirta): Ekman-erottelua ei voi toistaa'],
 'raaka':scan(sst,moc,i0,i1),'kausisykli_poistettu':scan(deseason(sst),deseason(moc),i0,i1)}
out['raaka']['surrogaatti_p']=surrogate_p(sst[i0:i1+1],moc[i0:i1+1],30)
# alkuperainen ikkuna uudella versiolla vertailuksi
j0,j1=idx('2023-02-21'),idx('2024-03-22')
out['alkuperainen_ikkuna_v2024_2']=scan(sst,moc,j0,j1)
# natiivi 5 vrk
t5d=[b+dt.timedelta(days=float(x)) for x in t5]
s5=np.array([np.nanmean([S.get(str(x+dt.timedelta(days=k)),np.nan) for k in range(-2,3)]) for x in t5d])
k0=next(i for i,x in enumerate(t5d) if x>=dt.date(2024,3,28)); k1=len(t5d)-1
w5a,w5b=s5[k0:k1+1],a5[k0:k1+1]; ne5=neff(w5a,w5b,mmax=10)
r5={l:pear(*lagged(w5a,w5b,l)) for l in range(-6,7)}
out['natiivi_5vrk']={'n':int(k1-k0+1),'neff':round(ne5,1),'r_m2(-10vrk)':round(r5[-2],3),'p_m2':round(p_t(r5[-2],ne5),4),'r':{str(5*l):round(v,3) for l,v in r5.items()}}
print(json.dumps(out,ensure_ascii=False,indent=1))
json.dump(out,open(sys.argv[4],'w'),ensure_ascii=False,indent=1)
