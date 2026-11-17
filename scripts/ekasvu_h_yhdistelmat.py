"""H: kaikkien yhdistelmien julkaisu (H §5), sama laskenta kuin ekasvu_h_laskenta.py. Ei muuta tulosta."""
import csv, itertools, sys
sys.path.insert(0, 'scripts')
import ekasvu_h_laskenta as h
ERO = 0.014 * h.bkt_2030()
with open('tools/data/ekasvu/h_yhdistelmat_2026-11-17.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['D', 'D_TWh', 'P', 'ajoitus', 'nettouusi', 'p2x_yhteisovero_eur_mwh', 'kayttoaste', 'dc_tp_per_twh',
                'valtio', 'kunnat', 'tyoelake', 'muut_sosrahastot', 'summa_meur', 'osuus_vertailuerosta', 'p2x_twh', 'tyopaikat'])
    for (dn, dv), p, t, n, y, c, j in itertools.product(h.DC_TASOT.items(), h.TASOT, (0, 0.5, 1), (0, 0.5, 1),
                                                         (0, h.YV_P2X_YLA), (0.4, 0.6, 0.8), (120, 400)):
        r = h.solu(dv, p, t, n, y, c, j); s = r['sek']
        w.writerow([dn, dv, p, t, n, y, c, j] + [round(s[k], 2) for k in ('valtio', 'kunnat', 'tyoelake', 'muut_sosrahastot')]
                   + [round(r['summa'], 2), round(r['summa'] / ERO, 5), round(r['p2x_twh'], 3), round(r['tyopaikat'], 1)])
print('ok')
