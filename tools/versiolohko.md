# ACI-instrumenttien versiolohko

Kaava, jota WEM, HEM, OGAS2 ja tulevat instrumentit voivat käyttää.
Otettu käyttöön OGAS2 v2.3:ssa 6.9.2026.

## Miksi

Versiostring oli kovakoodattuna **kahdessa paikassa** (header ja
footer), eikä kumpikaan päivittynyt kolmessa muutoserässä 3.–6.9.2026.
Otsikossa luki yhä `v2.0 · build 2026-04-25d`, vaikka kolme neljästä
kerroksesta oli määritelty uudelleen ja viisi vikaa korjattu.

**Seuraus oli konkreettinen.** Samannimisiä latauksia oli kolme, eikä
tiedostosta voinut nähdä mikä niistä oli käsillä. Keskustelu kulki eri
versioista puolin ja toisin: toinen osapuoli raportoi vikoja, jotka
oli jo korjattu, ja toinen kuvasi korjauksia, joita vastaanottaja ei
nähnyt.

Se on sama vikaluokka kuin muutkin tässä projektissa löydetyt: teksti
kertoo mitä pitäisi olla, ei mitä on.

## Kolme osaa

### 1 · Yksi totuuden lähde

```js
const VERSION = '2.3';
const VERSION_DATE = '2026-09-06';
```

Kaikki näkyvät versiomerkinnät johdetaan näistä. Ei kovakoodattuja
versiostringejä HTML:ssä — vain `id`-ankkurit, jotka `renderVersion()`
täyttää.

### 2 · Muutosloki koodissa, ei erillisessä tiedostossa

```js
const CHANGELOG = [
  ['2.3','2026-09-06','Mitä muuttui...'],
  ['2.2','2026-09-05','...'],
];
```

Koodissa siksi, että se **seuraa tiedostoa mukana** kun se ladataan tai
kopioidaan. Erillinen `CHANGELOG.md` jää repoon eikä kulje mukana.

Uusin merkintä on ensimmäisenä, ja sen versionumeron on oltava sama
kuin `VERSION`. Se on tarkistettavissa yhdellä rivillä.

### 3 · Sisältötiiviste

```js
function contentHash(){
  const s = document.documentElement.outerHTML;
  let h = 0x811c9dc5;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h.toString(16).padStart(8, '0');
}
```

FNV-1a, kahdeksan merkkiä, laskettu dokumentin omasta lähdekoodista.

**Versio kertoo mitä pitäisi olla, tiiviste mitä on.** Jos versio
unohtuu päivittämättä, tiiviste muuttuu silti. Ja kaksi osapuolta voi
verrata "katsommeko samaa tiedostoa" ilman että kumpikaan luottaa
muistiin.

Ei kryptografinen — tarkoitus on havaita ero, ei estää väärennöstä.

## Näkymä

Footer renderöi:

    Version 2.3 · 2026-09-06 · sha a3f21c8e
    ▸ Muutosloki

Muutosloki on `<details>`-lohkossa eli suljettuna oletuksena.

## Mitä tämä ei ratkaise

Versionumero on yhä käsin päivitettävä. Perusteellinen ratkaisu olisi
injektoida commit-SHA build-vaiheessa, mutta instrumentit ovat
staattisia HTML-tiedostoja GitHub Pagesissa eikä siellä ole
rakennusvaihetta.

Tiiviste kattaa tämän osittain: jos versio unohtuu, tiiviste paljastaa
että tiedosto on eri.
