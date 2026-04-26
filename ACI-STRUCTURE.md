# ACI Structural Invariants
## Governance Layer for the Aether Continuity Institute Research System

**Version:** 1.0  
**Date:** March 2026  
**Status:** Active — binding on all content operations

This document defines the structural invariants of the ACI research system. It governs what may be changed, extended, or added — and what may not be modified without explicit decision. It applies to human authorship, LLM-assisted authorship, and automated content operations equally.

---

## 1. Publication Types

Each publication type has a fixed purpose and format. Adding a new type requires explicit decision and an update to this document.

### Working Papers (WP-NNN)
**Purpose:** Theoretical frameworks, diagnostic models, formal propositions.  
**Required elements:** Abstract, Keywords, numbered §-sections, Limitations section, Research Programme or falsification conditions, Version History, domain tags.  
**Domain assignment:** Every WP must be tagged to at least one D-domain.  
**Cross-references:** Must explicitly state which prior WPs it builds on.  
**What it is not:** Not policy advocacy, not implementation guidance, not case study without theoretical framing.

### Diagnostic Assessments (DA-NNN)
**Purpose:** Applied evaluation of a specific system, region, or institution using ACI frameworks.  
**Required elements:** Diagnostic question stated explicitly, framework reference (which WP), findings as classified outcomes (not recommendations), scope and limits.  
**What it is not:** Not a policy report, not a forecast, not a recommendation document.

### Technical Notes (TN-NNN)
**Purpose:** Architectural or operational specifications that implement a WP framework in a concrete system.  
**Required elements:** Parent WP reference, domain tags, specification structure (not essay structure).  
**What it is not:** Not a working paper, not a product specification, not marketing.

### Supporting Papers (SP-NNN)
**Purpose:** Extensions, elaborations, or empirical applications that build on WPs but do not stand alone as primary contributions.  
**Required elements:** Explicit parent WP reference, domain tags, limitations section.  
**Scope:** May extend a WP into adjacent territory (e.g., cognitive layer, computing architecture) but must maintain explicit causal connection to core ACI framework.

### Concept Notes (CN-NNN)
**Purpose:** Short epistemological anchors — design posture before evidence, boundary conditions, scope clarifications.  
**Required elements:** Explicit statement of what is and is not claimed. Revision condition (under what evidence this note would be updated).  
**Length:** Maximum ~20KB. If longer, it should be a WP or SP.

### Research Query Memos (RQM-NNN)
**Purpose:** Open research questions that do not yet have sufficient basis for a WP or DA. A RQM poses a question — it does not answer it.  
**Required elements:** The question stated precisely, why existing frameworks do not resolve it, what evidence would allow progression to a WP or DA.

### Supplements (TN, RQM, MESA, etc.)
Applied instruments, questionnaires, audit tools. Must reference parent WP or TN.

---

## 2. Research Domains

The six domains are fixed. They may be elaborated but not renamed, split, or merged without explicit decision.

| Domain | Name | Core question |
|--------|------|---------------|
| D-1 | Duration adequacy in low-inertia energy systems | When does energy infrastructure run out of decision time before physical capacity is exhausted? |
| D-2 | Distributed continuity doctrines | How should small states structure continuity architecture under prolonged compound pressure? |
| D-3 | Temporal decision capacity and institutional diagnostics | Under what conditions does governance lose causal influence over outcomes? |
| D-4 | Compound stress evaluation frameworks | How do simultaneous pressures interact to produce outcomes single-variable analysis cannot detect? |
| D-5 | Continuity-oriented computing systems | How must computation be architected when decision capacity is the primary invariant? |
| D-6 | Situational awareness persistence | How does awareness of system state survive infrastructure failure? |

**Domain assignment rules:**
- Every publication must be tagged to at least one domain
- A publication may be tagged to multiple domains if genuinely cross-domain
- Domain tags appear in publication headers and index listings
- New publications do not create new domains — they are assigned to existing ones or trigger an explicit domain extension decision

---

## 3. Numbering and Naming

### Sequential numbering
- WP-001 through WP-NNN — sequential, never reused
- SP-001 through SP-NNN — sequential, never reused
- DA-001 through DA-NNN — sequential, never reused
- TN-001 through TN-NNN — sequential, never reused
- CN-001 through CN-NNN — sequential, never reused

### File naming convention
```
[type]-[NNN]-[short-slug].html
```
Examples: `wp-003-itt.html`, `da-001-finland-pre-shortage.html`, `cn-001-framing-capacity-uncertainty.html`

**Rules:**
- Lowercase, hyphens only, no underscores, no version numbers in filename
- Slug must be human-readable and descriptive
- Never rename a published file (breaks links and sitemap)

### Version management
- Version history lives inside the document, not in the filename
- `v1.0` = initial publication
- `v1.1`, `v1.2` etc. = substantive revisions (new sections, corrected claims)
- Minor corrections (typos, formatting) do not require version increment
- When a document is substantially revised, the old version is not archived separately — version history section inside the document is the record

---

## 4. Document Structure Invariants

### §-section structure
All WPs and SPs use numbered §-sections. The following are required:
1. Every section has a `§ NN` prefix
2. Abstract appears before §01
3. Limitations appears as a dedicated section (not buried in conclusion)
4. Version History appears at the end
5. Cross-references to related papers appear in a dedicated block at the end

### The Non-Goals principle
Every publication should be clear about what it does not do. This is not optional boilerplate — it is part of ACI's diagnostic identity. The clearer the scope, the more credible the claims within it.

### Falsification conditions
Working Papers must state how the framework could be shown to be wrong. If a WP cannot specify falsification conditions, it is not yet ready for publication. This is the minimum bar for scientific credibility.

---

## 5. Cross-Reference Integrity

### Required cross-references
- Every SP must reference its parent WP(s)
- Every TN must reference its parent WP(s)
- Every DA must reference the diagnostic framework WP it applies
- When a new WP builds on prior WPs, the relationship must be stated explicitly in the introduction

### Bidirectional linking
When document A references document B, document B should reference document A (in its "Related Papers" or "Companion Documents" section). This is checked before publication.

### The coherence test
Before publishing any new document, verify:
1. Does it reference the correct parent WPs?
2. Does the parent WP's related papers section reference back to it?
3. Are domain tags consistent with actual content?
4. Does the sitemap include the new file?

---

## 6. What LLM Operations May and May Not Do

### Permitted without explicit decision
- Draft new content within an existing publication type and domain
- Translate existing documents to English from Finnish (or vice versa)
- Add meta descriptions, fix broken links, update sitemap
- Improve formatting, typography, or HTML structure
- Add cross-references between existing documents
- Generate meta descriptions from abstracts
- Renumber sections when inserting new content

### Requires explicit human decision
- Creating a new publication type
- Adding, renaming, or merging research domains
- Changing the canonical §-section structure of a publication type
- Archiving or removing a published document
- Publishing a new WP (working paper) — these must be human-authored or explicitly reviewed
- Changing ACI's positioning or non-goals
- Modifying this document

### Never permitted
- Changing the content of a published WP's core claims without a version increment and explicit decision
- Removing falsification conditions from a WP
- Adding claims that exceed the stated scope of a document
- Modifying the structural invariants defined in this document without updating the document itself

---

## 7. Positioning Invariants

The following are fixed characteristics of ACI that do not change through content operations:

**ACI is diagnostic, not prescriptive.** It identifies failure conditions — it does not recommend solutions, advocate policies, or promote investment programmes.

**ACI publishes, it does not consult.** All output is open access. ACI does not provide paid analysis, advisory services, or implementation support.

**ACI's authority derives from analytical transparency.** Claims must be falsifiable, scope must be stated, limitations must be acknowledged. Authority does not derive from institutional affiliation, credentials, or endorsement.

**ACI is not affiliated with any government, company, or political organisation.** Independence is structural, not aspirational.

---

## 8. The Coherence Budget

Every research system has a finite coherence budget — the amount of structural complexity it can maintain before internal contradictions accumulate and credibility erodes. ACI's current structure (12 WPs, 6 SPs, 6 DAs, 6 TNs, 1 CN, 6 domains) is near the point where this requires active management.

The following signals indicate coherence is degrading:
- New publications that cannot be cleanly assigned to an existing domain
- Cross-references that are missing or incorrect
- Scope creep in WPs (claiming more than the framework supports)
- Publication type confusion (SPs that should be WPs, TNs that are policy documents)
- Inconsistent terminology across documents for the same concept

When these signals appear, the correct response is to stop adding content and consolidate — not to continue publishing.

---

## 9. Core Axiom

> Continuity is not guaranteed by capacity, intent, or optimization.  
> It emerges only where systems retain decision capability under stress.

This axiom is the foundation of all ACI work. Publications that contradict or substantially reframe this axiom require a new foundational note — not a paper update or revision.

---

## 10. Current Publication Inventory

As of March 2026 — update this table when new publications are added.

| Type | Range | Next ID |
|------|-------|---------|
| Working Papers (WP) | WP-001 – WP-013 | WP-014 |
| Supporting Papers (SP) | SP-001 – SP-006 | SP-007 |
| Diagnostic Assessments (DA) | DA-001 – DA-007 | DA-008 |
| Technical Notes (TN) | TN-001 – TN-006 | TN-007 |
| Concept Notes (CN) | CN-001 – CN-002 | CN-003 |
| Research Query Memos (RQM) | RQM-001 | RQM-002 |

**Homepage §-structure** (index.html) — these sections are fixed:

| § | Title | Editable? |
|---|-------|-----------|
| 01 | Purpose | Content only |
| 02 | Why Systems Fail Under Pressure | Content only |
| 03 | Methodological Principle | Content only |
| 04 | Institutional Position | Content only |
| 05 | Publication Principle | Content only |
| 06 | Working Domains | Grows with new domains only |
| 07 | Non-Goals | Content only |
| 08 | Publications | Grows with new publications |

Adding a §09 or beyond requires explicit decision and an update to this document.

---

*This document governs ACI's research system structure. It is itself subject to revision, but only through explicit decision — not through content operations.*

*ACI-STRUCTURE.md · v1.1 · March 2026*

**Version History**  
v1.0 · March 2026 · Initial governance definition  
v1.1 · March 2026 · Added core axiom (§9), publication inventory table (§10), homepage §-structure invariants, RQM definition, fixed duplicate DA entry
v1.2 · March 2026 · CN-002 added to inventory
v1.3 · March 2026 · WP-013 added to inventory

---

## WP-017 — Parliamentary Decision Latency and Market Signal Correlation
**Status:** Concept | **Luotu:** 2026-04-26
**Huomio:** WP-016 on julkaistu (Health Data Continuity Index). Tämä on erillinen paperi — numeroitu WP-017.

### Hypoteesi (tarkennettu 2026-04-26)
Lainamarkkinat **viivästävät** D-suppression hinnoittelun — ne reagoivat institutionaalisen päätöksentekokyvyn heikkenemiseen tyypillisesti 2–5 vuoden viiveellä ja vasta kun ongelma on realisoitunut, ei ennakoivasti. Tämä on empiiristen havaintojen tukema rakenne (vrt. Acemoglu et al. sovereign spread -tutkimus).

WP-017 ei tutki ennakoivatko markkinat D-suppressiota, vaan: **missä instrumentissa signaali näkyy ensin ja millä viiveellä** — bondispread, CDS, osakemarkkinavolatiliteetti vai jokin muu.

Markkinat määrittelevät maan kyvyn investoida — mutta eivät lähtökohtaisesti arvioi onko tehty päätös sisällöllisesti oikea.

### Tutkimuskysymys
Korreloivatko markkinasignaalit (10v korko, CDS, OMXH) D-suppression vaiheiden (D1/D2/D3) kanssa — ja kuinka pitkä ennakoiva ikkuna markkinoilla on suhteessa parlamentaariseen päätökseen tai päättämättä jättämiseen?

### Datasyötteet
- **Eduskunnan avoin API** — äänestykset, asiakirjat, lausunnot, käsittelyvaiheet
- **Eurostat irt_lt_mcby_m** — FI, DE, SE 10v valtionlainakorot kuukausittain (proxy: aci-ecb-proxy)
- **Spreadit:** FI-DE (fiskaalikapasiteetti) + FI-SE (rakenteellinen vertailu)
  - Ruotsi on parempi referenssimaa kuin Saksa: pohjoinen energiajärjestelmä, SE1-kytkennät, CHP-historia
- **CDS-spread** — Suomi 5v sovereign CDS (tuleva)
- **OMXH25** — Helsingin pörssi-indeksi volatiliteetti (tuleva)
- **Aikajänne:** kuukausittain 2023–2026

### Metodologia
1. Parlamentaarisista asiakirjoista koodataan kriittiset energia- ja huoltovarmuuspäätökset D1/D2/D3-vaiheisiin
2. Markkinareaktio mitataan 30/90/180 päivän ikkunoissa suhteessa päätöshetkeen
3. Korrelaatioanalyysi: ennakoivatko markkinat D-suppressiota vai seuraavat päätöksiä?
4. Vertailu OGAS2 SHI-trajektoriin: ovatko markkinat ja malli yhteneväisiä?

### Teoreettinen merkitys
Mittaa päätöksentekokyvyn finanssimarkkinavasteen — tekee tulosvastuun näkyväksi numeroin. Jos markkinat näkevät puutteen 6 kuukautta ennen päättäjiä, se osoittaa että "emme tienneet" -argumentti ei pidä.

### Kytkennät
- WP-015 §9 regiimitunnistus → laajennettu parlamentaariseen dataan
- WP-016 HDCI → terveysjärjestelmän D-suppressio, sama rakenne eri sektorilla
- OGAS2 R_PUBLIC Buffer → markkinapohjainen kalibrointi
- §3.6 legitimiteettivaje → mitattuna euroissa prosessitosiasioiden sijaan
- Eduskunnan avoin API (löydetty 2026-04-25)

### Pilottitulokset (2026-04-26)

**FI-DE spread** (39 kk 2023-01 → 2026-03):
Kapenee trendimäisesti 0.60 pp → 0.40 pp. D-suppressio ei näy.
AAA-Suomi hinnoitellaan lähes Saksan tasoisena riippumatta energiapäätösten viipeestä.

**FI-SE spread** (39 kk 2023-01 → 2026-03):
Ei kapene — päinvastoin levenee 0.43 → 0.88 pp kesällä 2024.
Selitys: Riksbank leikkasi ohjauskorkoa aggressiivisesti 2024 (SE 10Y: 3.02% → 1.93%).
Tämä on rahapolitiikkadivergenssi, ei energiapäätösero.

**Valuuttarakenteen metodologinen vaikutus:**
Suomi on eurojäsen — FI 10Y seuraa EKP:n ohjauskorkoa. Maakohtainen riski näkyy
ainoastaan spreadin muutoksena suhteessa muihin euroalueen maihin.
Ruotsilla on oma valuutta — SE 10Y heijastaa Riksbankin päätöksiä suoraan ja
itsenäisesti. Tämä tekee FI-SE spreadista epäpuhtaan mittarin D-suppression kannalta:
valuuttadivergenssi dominoi energiapäätösdivergenssiin nähden.
FI-DE on metodologisesti puhtaampi vertailu koska rahapolitiikka on yhteinen.

**Metodologinen päälopputulos:**
Bondispread dominoituu rahapolitiikkadivergenssin toimesta. D-suppression
signaalin eristäminen vaatii eksplisiittisen rahapolitiikkakontrollimuuttujan.
Seuraava askel: CDS-spread tai osakemarkkinavolatiliteetti (OMXH25) ovat
potentiaalisesti puhtaampia instrumentteja kotimaiselle päätöskyvyn mittaamiselle.
