"""RAPID v2024.1a (tools/rapid_daily.json) vs v2024-2: harha, RMS, korrelaatio 5 vrk ja kk.
Aja: python3 scripts/amoc_rapid_version_compare.py . RAPID_transports_v2024-2.nc
"""
import json,sys,datetime as dt,numpy as np,netCDF4 as nc
REPO,NEW=sys.argv[1],sys.argv[2]
R=json.load(open(REPO+'/tools/rapid_daily.json'))
d=nc.Dataset(NEW); b=dt.date(1950,1,1)
t5=[b+dt.timedelta(days=float(x)) for x in d.variables['time_5d'][:]]; a5=np.array(d.variables['amoc_depth_5d'][:],float)
t1=[b+dt.timedelta(days=float(x)) for x in d.variables['time_1m'][:]]; a1=np.array(d.variables['amoc_depth_1m'][:],float)
old={dt.date.fromisoformat(k):v['moc'] for k,v in R.items() if v.get('moc') is not None}
o5=[];n5=[];dd=[]
for t,v in zip(t5,a5):
    vals=[old.get(t+dt.timedelta(days=k)) for k in range(-2,3)]
    vals=[x for x in vals if x is not None]
    if len(vals)==5: o5.append(np.mean(vals)); n5.append(v); dd.append(t)
o5,n5=np.array(o5),np.array(n5); diff=n5-o5
print('5d overlap',len(o5),dd[0],dd[-1])
print('old mean %.2f new mean %.2f bias %.2f Sv, RMS %.2f, r %.3f, sd old %.2f new %.2f'%(o5.mean(),n5.mean(),diff.mean(),np.sqrt((diff**2).mean()),np.corrcoef(o5,n5)[0,1],o5.std(),n5.std()))
# trend per decade
yrs=np.array([(x-dd[0]).days/365.25 for x in dd])
for nm,s in (('old',o5),('new',n5)): print(nm,'trend Sv/decade %.2f'%(np.polyfit(yrs,s,1)[0]*10))
# monthly
om=[];nm_=[]
for t,v in zip(t1,a1):
    vals=[x for k,x in old.items() if k.year==t.year and k.month==t.month]
    if len(vals)>=25: om.append(np.mean(vals)); nm_.append(v)
om,nm_=np.array(om),np.array(nm_)
print('monthly overlap',len(om),'bias %.2f RMS %.2f r %.3f'%((nm_-om).mean(),np.sqrt(((nm_-om)**2).mean()),np.corrcoef(om,nm_)[0,1]))
# by year bias
for y in range(2004,2025):
    m=[i for i,x in enumerate(dd) if x.year==y]
    if m: print(y,'bias %.2f'%diff[m].mean(), 'n',len(m))
# new period
new=[(t,v) for t,v in zip(t5,a5) if t>dt.date(2024,3,22)]
print('new period',new[0][0],new[-1][0],len(new),'mean %.2f'%np.mean([v for _,v in new]))
print('whole new series mean %.2f sd %.2f'%(a5.mean(),a5.std()), 'monthly mean %.2f'%np.nanmean(a1))
