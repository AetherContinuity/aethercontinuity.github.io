#!/usr/bin/env python3
"""ACI — julkaisurekisteri ja etusivun lohkot.

    python3 scripts/build-index.py            # päivitä rekisteri + etusivu
    python3 scripts/build-index.py --check    # älä kirjoita; raportoi erot

MIKSI
Etusivun luettelo kirjoitettiin käsin ja vanheni (WEM v2.7.5, "Twenty
working papers", syyskuun julkaisut listan keskellä). Tässä luettelo
johdetaan tiedostoista:

  1. data/registry.json  — yksi rivi per julkaisu. Uudet tiedostot lisätään
     automaattisesti; olemassa olevia rivejä EI ylikirjoiteta, joten otsikon,
     päivän, piilotuksen ja kuvauksen voi korjata käsin ja korjaus pysyy.
  2. index.html          — lohkot merkkien <!-- GEN:nimi --> … <!-- /GEN:nimi -->
     välissä kirjoitetaan uudelleen. Muu sivu on käsin kirjoitettua.

PÄIVÄMÄÄRÄ = tiedoston ensimmäinen commit (git). Asetetaan kerran, kun
rivi luodaan; sen jälkeen rekisterin arvo on voimassa. Committoimaton uusi
tiedosto saa kuluvan päivän.

Ei riippuvuuksia vakiokirjaston ulkopuolelta.
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "data" / "registry.json"
INDEX = ROOT / "index.html"

GROUPS = {"papers": "pub", "supplements": "pub", "tools": "tool",
          "fiction": "fiction", "decisions": "decision"}

TYPES = {"WP": "Working Paper", "SM": "Synthesis Memo", "CN": "Concept Note",
         "TN": "Technical Note", "DA": "Diagnostic Assessment", "SP": "Supporting Paper",
         "DRD": "Resilience Doctrine", "RQM": "Research Query Memo", "DT": "Decision Track",
         "DASC": "Protocol", "DEMO": "Demonstration", "AN": "Analysis", "REPORT": "Report"}

# Tiedostot, jotka eivät ole julkaisuja: hakemistot, varmuuskopiot, vanhat
# versiot, apusivut. Uusi osuma saa hidden: true; käsin voi kumota.
AUTO_HIDE = re.compile(
    r"(^|/)(index|Oldindex|papers-index)\.html$|backup|wp-tbd|v2old|vold\d|"
    r"INSTRUMENT-v1\.|wem-historia|wem-harvest|fetch-tool|-liite\.html$", re.I)

ID_IN_TITLE = re.compile(r"^(?:ACI\s+)?((?:WP|SM|CN|TN|DA|SP|DRD|RQM|DT|DASC|DEMO)-\d+[A-Za-z]?)\s*[—–·:\-]\s*(.+)$")
ID_IN_NAME = re.compile(r"(?:^|[_/])(wp|sm|cn|tn|da|sp|drd|rqm|dt|dasc)[-_]?(\d{1,3})(?=[-_.]|$)", re.I)
TITLE_TAIL = re.compile(r"\s*[|·—–-]\s*(ACI(\s+(Fiktio|Fiction|Tools|Analyysi|Synthesis Memo))?|Aether Continuity Institute)\s*$", re.I)
TITLE_HEAD = re.compile(r"^(ACI(\s+Tools)?\s*[—–·:-]\s*|ACI\s+(?=[A-Z]{2,4}-\d))")
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


# ── git ──────────────────────────────────────────────────────────────
def first_commit_dates() -> dict[str, str]:
    """polku -> aikaisin lisäyspäivä. Tyhjä, jos git ei ole käytettävissä."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--name-only", "--format=@%ad", "--date=short"],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return {}
    dates, d = {}, None
    for line in out.splitlines():
        if line.startswith("@"):
            d = line[1:]
        elif line:
            dates[line] = d          # loki on uusin ensin -> viimeinen kirjoitus = vanhin
    return dates


def followed_date(rel: str) -> str | None:
    """Uudelleennimetylle tiedostolle: historian vanhin commit."""
    try:
        out = subprocess.run(["git", "log", "--follow", "--format=%ad", "--date=short", "--", rel],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    except (OSError, subprocess.CalledProcessError):
        return None
    return out[-1] if out else None


# ── tiedostosta rivi ─────────────────────────────────────────────────
def scan(rel: str, dates: dict[str, str]) -> dict:
    text = (ROOT / rel).read_text(encoding="utf-8", errors="ignore")
    m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    title = html.unescape(m.group(1)).strip() if m else Path(rel).stem
    title = re.sub(r"\s+", " ", TITLE_HEAD.sub("", TITLE_TAIL.sub("", title)))
    lang = (re.search(r"<html[^>]*\blang=\"([a-zA-Z-]+)\"", text) or [None, "en"])[1][:2].lower()

    pid = None
    m = ID_IN_TITLE.match(title)
    if m:
        pid, title = m.group(1).upper(), m.group(2).strip()
    else:
        m = ID_IN_NAME.search(Path(rel).name)
        if m and GROUPS[rel.split("/")[0]] in ("pub", "decision"):
            pid = f"{m.group(1).upper()}-{int(m.group(2)):03d}"
    kind = pid.split("-")[0] if pid else None

    entry = {
        "path": "/" + rel,
        "group": GROUPS[rel.split("/")[0]],
        "id": pid,
        "type": kind,
        "title": title,
        "lang": lang,
        "date": dates.get(rel) or followed_date(rel) or date.today().isoformat(),
    }
    if AUTO_HIDE.search(rel):
        entry["hidden"] = True
    return entry


def load_registry() -> list[dict]:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))["items"] if REGISTRY.exists() else []


def sync(items: list[dict]) -> tuple[list[dict], list[str], list[str]]:
    """Lisää uudet tiedostot, merkitsee kadonneet. Ei muuta olemassa olevia."""
    known = {e["path"] for e in items}
    on_disk = sorted(str(p.relative_to(ROOT)) for d in GROUPS for p in (ROOT / d).glob("*.html"))
    new = [r for r in on_disk if "/" + r not in known]
    dates = first_commit_dates() if new else {}
    added = [scan(r, dates) for r in new]
    gone = sorted(e["path"] for e in items if not (ROOT / e["path"].lstrip("/")).exists())
    items = [e for e in items if e["path"] not in gone] + added
    items.sort(key=lambda e: (e["group"], e["date"], e["path"]))
    return items, [e["path"] for e in added], gone


# ── renderöinti ──────────────────────────────────────────────────────
def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def nice_date(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def visible(items: list[dict], group: str) -> list[dict]:
    return [e for e in items if e["group"] == group and not e.get("hidden") and not e.get("variant_of")]


def row(pid: str, href: str, title: str, meta: str) -> str:
    return (f'      <div class="pub-item">\n'
            f'        <span class="pub-id">{esc(pid)}</span>\n'
            f'        <div class="pub-body">\n'
            f'          <div class="pub-title"><a href="{esc(href)}">{esc(title)}</a></div>\n'
            f'          <div class="pub-meta">{meta}</div>\n'
            f'        </div>\n'
            f'      </div>')


def render_latest(items: list[dict], n: int = 10) -> str:
    pubs = sorted(visible(items, "pub"), key=lambda e: (e["date"], e.get("id") or ""), reverse=True)[:n]
    out = []
    for e in pubs:
        meta = [nice_date(e["date"]), TYPES.get(e.get("type"), "Document"), e["lang"].upper()]
        if e.get("domains"):
            meta.append(esc(" · ".join(e["domains"])))
        out.append(row(e.get("id") or "—", e["path"], e["title"], " &middot; ".join(meta)))
    return "\n".join(out)


def render_tools(items: list[dict]) -> str:
    tools = sorted((e for e in visible(items, "tool") if e.get("featured")), key=lambda e: e["featured"])
    return "\n".join(
        row(e.get("label") or "—", e["path"], e["title"], esc(e.get("blurb", ""))) for e in tools)


def render_fiction(items: list[dict], n: int = 4) -> str:
    all_f = [e for e in items if e["group"] == "fiction" and not e.get("hidden")]
    out = []
    for e in sorted(visible(items, "fiction"), key=lambda e: e["date"], reverse=True)[:n]:
        langs = [e["lang"].upper()] + sorted(v["lang"].upper() for v in all_f if v.get("variant_of") == e["path"])
        meta = [nice_date(e["date"]), " / ".join(dict.fromkeys(langs))]
        if e.get("blurb"):
            meta.append(esc(e["blurb"]))
        out.append(row("—", e["path"], e["title"], " &middot; ".join(meta)))
    return "\n".join(out)


def render_decisions(items: list[dict]) -> str:
    return "\n".join(
        row(e.get("id") or "—", e["path"], e["title"], esc(e.get("blurb") or "Decision Track"))
        for e in sorted(visible(items, "decision"), key=lambda e: e.get("id") or ""))


def render_counts(items: list[dict]) -> str:
    pubs = visible(items, "pub")
    wp = len({e["id"] for e in pubs if e.get("type") == "WP"})
    live = sum(1 for e in visible(items, "tool") if e.get("featured"))
    return (f"{len(pubs)} open documents, {wp} of them working papers, and {live} live instruments, "
            f"applied to Nordic and small-state operating environments.")


BLOCKS = {"counts": render_counts, "latest": render_latest, "tools": render_tools,
          "fiction": render_fiction, "decisions": render_decisions}


def apply_blocks(page: str, items: list[dict]) -> str:
    for name, fn in BLOCKS.items():
        pat = re.compile(rf"(<!-- GEN:{name} -->)(.*?)(<!-- /GEN:{name} -->)", re.S)
        if not pat.search(page):
            raise SystemExit(f"index.html: merkki GEN:{name} puuttuu")
        body = fn(items)
        inline = name == "counts"
        page = pat.sub(lambda m: m.group(1) + (body if inline else "\n" + body + "\n      ") + m.group(3), page)
    return page


def main() -> int:
    check = "--check" in sys.argv[1:]
    items, added, gone = sync(load_registry())
    page_old = INDEX.read_text(encoding="utf-8")
    page_new = apply_blocks(page_old, items)

    for p in added:
        e = next(x for x in items if x["path"] == p)
        print(f"  + {p}  [{e['date']}] {e.get('id') or ''} {e['title'][:60]}" + ("  (piilotettu)" if e.get("hidden") else ""))
    for p in gone:
        print(f"  - {p}  (tiedosto poistunut)")
    stale = page_new != page_old
    if check:
        if added or gone or stale:
            print("rekisteri tai etusivu ei ole ajan tasalla — aja scripts/build-index.py")
            return 1
        print("ajan tasalla")
        return 0
    REGISTRY.parent.mkdir(exist_ok=True)
    REGISTRY.write_text(json.dumps({
        "_note": "Julkaisurekisteri. Uudet tiedostot lisää scripts/build-index.py; olemassa olevia "
                 "rivejä se ei muuta. Käsin muokattavat kentät: title, date, lang, hidden, "
                 "variant_of (käännös: alkuperäisen path), featured + label + blurb (mittarit), "
                 "blurb (fiktio, päätösraidat), domains.",
        "items": items}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    INDEX.write_text(page_new, encoding="utf-8")
    print(f"rekisteri: {len(items)} riviä ({len(added)} uutta, {len(gone)} poistettu) · etusivu "
          + ("päivitetty" if stale else "ennallaan"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
