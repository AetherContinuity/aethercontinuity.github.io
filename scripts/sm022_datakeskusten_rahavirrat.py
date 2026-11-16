# Datakeskusten rahavirrat Suomessa: kuka maksaa, kuka saa. Vuositaso, vakiintunut tila.
# [M] mitattu/lähde, [L] laskettu, [A] oletus.
LF = 0.80                    # [A] käyttöaste
SAHKOVERO_I = 22.4           # [M] €/MWh, VaVM 28/2025
SAHKOVERO_II = 0.5           # [M] €/MWh, voimassa datakeskuksille 30.6.2026 asti (vastaskenaario)
YHTEISOVERO_PER_MW = 11.6e3  # [A] €/MW/v: kululisä 5 % kulupohjasta 1,16 M€/MW (sähkö+poistot), 20 %
KV_TALVI, KV_MUU, KV_OTTO = 10.47, 2.97, 1.07   # [M] Fingrid 2026 €/MWh
TALVI_OSUUS = 0.10           # [A] talviarkipäivätuntien osuus vuodesta (~64 pv x 14 h)
KV_KESKI = TALVI_OSUUS*KV_TALVI + (1-TALVI_OSUUS)*KV_MUU + KV_OTTO   # [L]
FG_INVEST = 5.2e9            # [M] Fingrid 2026-2035
ANNUITEETTI = 0.05/(1-1.05**-40)   # [A] 5 %, 40 v
KULUTUS_2025, KULUTUS_2035 = 85, 160   # [M] TWh (ET 2025; Fingrid kehittämissuunnitelma)
HINTA_2025 = 40.5            # [M] €/MWh, Fingrid (vertailutaso, ei ennuste)
HINTAHERKKYYS = (1, 2, 5, 10) # €/MWh muutos keskihinnassa; hintaa ei mallinneta (riippuu tuulesta, vesitilanteesta, siirroista ja kulutuksen kasvusta)
MUU_KULUTUS = 85             # [A] TWh, muu kuin datakeskus
KOTIT_OSUUS = 0.25           # [A] kotitalouksien osuus kulutuksesta (ALV-vaikutus)
ALV = 0.255                  # [M]

def skenaario(gw):
    e = gw*1000*8760*LF/1e6          # TWh
    out = {}
    out['kulutus_TWh'] = e
    out['sahkovero_I'] = e*1e6*SAHKOVERO_I
    out['sahkovero_II'] = e*1e6*SAHKOVERO_II
    out['yhteisovero_dc'] = gw*1000*YHTEISOVERO_PER_MW
    out['kv_maksut_dc'] = e*1e6*KV_KESKI
    out['kv_kustannus_dc'] = FG_INVEST*ANNUITEETTI * min(1, e/(KULUTUS_2035-KULUTUS_2025))
    for m in (0.02, 0.05, 0.10):       # [A] kululisäherkkyys
        out[f'yhteisovero_{int(m*100)}pct'] = gw*1000*1.16e6*m*0.20
    return out

if __name__ == '__main__':
    print(f'Kantaverkkomaksu tasaiselle kuormalle {KV_KESKI:.2f} €/MWh; investointien annuiteetti {FG_INVEST*ANNUITEETTI/1e6:.0f} M€/v')
    print('Hintaherkkyys (riippumaton datakeskusskenaariosta): muiden käyttäjien kustannus / ALV kotitalouksilta, M€/v')
    for d in HINTAHERKKYYS:
        print(f'  +{d} €/MWh ({d/HINTA_2025:.0%} vuoden 2025 tasosta): {d*MUU_KULUTUS:.0f} / {d*MUU_KULUTUS*KOTIT_OSUUS*ALV:.0f}')
    for gw in (1.5, 2.5, 4.0):
        o = skenaario(gw); M = lambda k: o[k]/1e6
        print(f'\n== {gw} GW lisäkuormaa, {o["kulutus_TWh"]:.1f} TWh/v')
        print(f'Valtio: sähkövero I {M("sahkovero_I"):.0f} M€ (luokka II olisi {M("sahkovero_II"):.0f}), yhteisövero DC {M("yhteisovero_dc"):.0f} M€')
        print(f'Kantaverkko: DC maksaa {M("kv_maksut_dc"):.0f} M€, DC:lle kohdistuva investointikulu {M("kv_kustannus_dc"):.0f} M€ -> muille {M("kv_kustannus_dc")-M("kv_maksut_dc"):.0f} M€')
        print(f'Yhteisövero kululisällä 2/5/10 %: {M("yhteisovero_2pct"):.0f} / {M("yhteisovero_5pct"):.0f} / {M("yhteisovero_10pct"):.0f} M€')
