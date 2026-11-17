"""Ennakkokirjaus G: energiaintensiivisen kasvun inkrementaalinen nettovaikutus
julkisyhteisöjen (S13) rahoitusasemaan 2030, S1 ja S2 suhteessa S0:aan.
Säännöt: SEURANTA.md, G ja lisäykset 1-3. Vain vakiokirjasto.
[M] lähde, [L] laskettu, [A] oletus."""

H = 8760
H2_MWH_T = 55.0             # [A] lisäys 2
CF_EL = 0.60                # [A] lisäys 2, herkkyys 0.4 / 0.8

def el_twh(mw, cf=CF_EL): return mw * H * cf / 1e6

def hankkeet(cf=CF_EL):
    """Täyttöjärjestys lisäys 3 kohta 2. (nimi, TWh, hyvitys M€, työpaikat)"""
    return [
        ("Arctic Sisu, Kotka", 56.1e3 * H2_MWH_T / 1e6, 150.0, 100),          # [M] 56,1 kt H2 -> [L]
        ("Freija, Nokia (VE1 160 MW)", el_twh(160, cf), 110.6, 100),
        ("VolagHy, Kuopio", 50e3 * 0.5 * H2_MWH_T / 1e6, 150.0, 100),        # [A] 0,5 t H2 / t eSAF
        ("Koppö, Kristiinankaupunki (200 MW)", el_twh(200, cf), 116.5, 100),
        ("Vetyalfa, Utajärvi (VE1 500 MW)", el_twh(500, cf), 150.0, 100),
        ("Arctial, Kokkola", 7.0, 150.0, 1000),
    ]

def tayta(kehys_twh, cf=CF_EL):
    out, jaljella = [], kehys_twh
    for nimi, twh, hyv, tp in hankkeet(cf):
        if jaljella <= 1e-9: break
        osa = min(1.0, jaljella / twh)
        out.append((nimi, twh * osa, hyv * osa, tp * osa, osa))
        jaljella -= twh * osa
    return out, jaljella

# Verokannat [M]
SV_I, SV_II, HVM = 22.4, 0.5, 0.85          # €/MWh
YV_DC_PER_TWH = 11.6e3 * 1e6 / (8760 * 0.8) / 1e6   # M€/TWh: 11,6 k€/MW / 7008 MWh/MW  -> €/MWh
YV_METALLI = 18.9                            # €/MWh, verot_304 ryhmä 24, 2022-2024 [M]/[L]
TP_DC_PER_TWH = 120                          # [A] lisäys 3 kohta 6
TYOKUSTANNUS, S13_OSUUS = 70e3, 0.40         # [A]

def skenaario(nimi, dc_twh, muu_twh, cf=CF_EL, nettouusi=1.0, yv_p2x=YV_METALLI):
    taytto, yli = tayta(muu_twh, cf)
    p2x_twh = sum(t for _, t, *_ in taytto)
    hyv = sum(h for _, _, h, _, _ in taytto)
    tp_p2x = sum(tp for *_, tp, _ in taytto)
    r = {}
    r['sahkovero'] = dc_twh * SV_I + p2x_twh * SV_II                    # M€ (TWh * €/MWh = M€)
    r['hvm'] = (dc_twh + p2x_twh) * HVM
    yv_dc = dc_twh * YV_DC_PER_TWH
    yv_p2x_brutto = p2x_twh * yv_p2x
    yv_p2x_netto = max(0.0, yv_p2x_brutto - 0.10 * hyv)
    r['yhteisovero'] = yv_dc + yv_p2x_netto
    tp = dc_twh * TP_DC_PER_TWH + tp_p2x
    r['palkkaverot'] = tp * TYOKUSTANNUS * S13_OSUUS * nettouusi / 1e6
    r['summa'] = r['sahkovero'] + r['hvm'] + r['yhteisovero'] + r['palkkaverot']
    r['_menetetty_verotuki_II'] = p2x_twh * (SV_I - SV_II)
    r['_tyopaikat'] = tp
    r['_p2x_twh'] = p2x_twh
    r['_yli'] = yli
    r['_taytto'] = taytto
    r['_hyvitys_vahennys'] = min(yv_p2x_brutto, 0.10 * hyv)
    return r

def bkt_2030():
    b = 281.783e3                                           # M€ 2025 [M] Tilastokeskus 15a9
    for g in (0.008, 0.017, 0.017, 0.015, 0.015): b *= (1 + g) * 1.02
    return b

if __name__ == '__main__':
    B = bkt_2030(); ERO = 0.014 * B
    print(f"BKT 2030 ≈ {B/1e3:.0f} mrd €; vertailuero 1,4 %-yks ≈ {ERO:.0f} M€\n")
    SKEN = {"S1": (0.0, 3.2), "S2": (13.7, 7.5)}
    for s, (dc, muu) in SKEN.items():
        r = skenaario(s, dc, muu)
        print(f"== {s}: datakeskukset +{dc} TWh, muu +{muu} TWh (täytetty {r['_p2x_twh']:.2f}, kehyksestä jäi {r['_yli']:.2f})")
        for n, t, h, tp, o in r['_taytto']:
            print(f"   {n:38} {t:5.2f} TWh  osuus {o:4.0%}  hyvitys {h:5.1f} M€  tp {tp:5.0f}")
        for k in ('sahkovero', 'hvm', 'yhteisovero', 'palkkaverot', 'summa'):
            print(f"   {k:14} {r[k]:7.1f} M€")
        print(f"   osuus vertailuerosta {r['summa']/ERO:6.1%}")
        print(f"   (verohyvityksen vähennys {r['_hyvitys_vahennys']:.1f} M€; menetetty luokan II verotuki {r['_menetetty_verotuki_II']:.0f} M€; työpaikat {r['_tyopaikat']:.0f})")
        # Epävarmuusväli: nettouusi 0/50/100 %, P2X-yhteisövero 0..metalli, käyttöaste 0.4/0.8
        vals = [skenaario(s, dc, muu, cf=c, nettouusi=n, yv_p2x=y)['summa']
                for c in (0.4, 0.6, 0.8) for n in (0.0, 0.5, 1.0) for y in (0.0, YV_METALLI)]
        lo, hi = min(vals), max(vals)
        mid = skenaario(s, dc, muu, nettouusi=0.5)['summa']
        print(f"   väli: {lo:.0f} … {hi:.0f} M€ (keski, nettouusi 50 %: {mid:.0f}) = {lo/ERO:.1%} … {hi/ERO:.1%}\n")
    # Herkkyys: S1 vaihtoehtoinen tulkinta (datakeskusten lisäys 2025->2030 = 3,8-2,0)
    r = skenaario("S1alt", 0.0, 7 - 1.8)
    print(f"Herkkyys S1 (muu = 7 - DC-lisäys 1,8 = 5,2 TWh): {r['summa']:.0f} M€ = {r['summa']/ERO:.1%}")
    for dc in (11 - 3.8, 18 - 3.8):
        r = skenaario("DC", dc, 0.0)
        print(f"Herkkyys: vain datakeskukset {dc+3.8:.0f} TWh (ET 10–15 %): {r['summa']:.0f} M€ = {r['summa']/ERO:.1%}")
