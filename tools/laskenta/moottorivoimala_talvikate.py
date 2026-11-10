# Moottorivoimalan talvikate: day-ahead vs. yläraja max(day-ahead, ylössäätö DS 244)
from _lue import sarja
da=sarja('da-fi-2025-11_2026-10.json')
up=sarja('rp-244-talvi-2025-2026.json')
keys=[k for k in up if k in da]
print("yhteisiä 15 min -pisteitä",len(keys),keys[0][:10],keys[-1][:10])
dt=0.25
for name,fuel in (("LNG 45",45),("LNG 45 + päästöoikeus (60)",60),("biometaani 90",90)):
    mc=fuel/0.45+8
    m_da=sum(max(0,da[k]-mc)*dt for k in keys)/1000
    m_up=sum(max(0,max(da[k],up[k])-mc)*dt for k in keys)/1000
    h_da=sum(dt for k in keys if da[k]>mc); h_up=sum(dt for k in keys if max(da[k],up[k])>mc)
    print("%-28s DA: %4.0f h %5.0f €/kW | yläraja max(DA, ylössäätö): %4.0f h %5.0f €/kW"%(name,h_da,m_da,h_up,m_up))
