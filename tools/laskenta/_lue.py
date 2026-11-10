"""Yhteinen lukija tools/data-aineistoille. Aja skriptit tästä hakemistosta."""
import json, os
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
def sarja(nimi):
    return json.load(open(os.path.join(DATA, nimi)))['data']
