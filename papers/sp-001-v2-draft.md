# SP-001 (v2 draft) — Reserve Duration and the Disappearing Buffer

**Why Wind-Dominant Adequacy Is Structurally Non-Robust in the Finnish–Baltic System**

Aether Continuity Institute · Supporting Paper No. 001 · v2.0 draft
Domain D-1 · Cross-references WP-001 · WP-008 · DA-001 · DA-003 · SM-007 · CN-004

> **Status note (v2.0).** This version withdraws the central quantitative claim of
> v1.0 — that extending reserve duration from 48 h to 72 h eliminates P99 LOLE
> outcomes. That result was non-robust to its own dominant parameter (wind
> persistence) and was internally inconsistent with the paper's own compound-stress
> premise (constrained import). v2.0 does not replace it with another sufficiency
> claim. It states a structural condition that does not depend on any reserve being
> adequate. Quantitative parameters are taken from the published literature and
> cited; they are not calibrated here. The only original empirical input is a
> single-zone Finnish measurement, labelled as such.

---

## Abstract

Adequacy risk in a wind-dominant power system is treated here as a structural
condition rather than a reserve-sizing problem. Two findings support this. First,
reserve-duration adequacy is non-robust to wind persistence: at the persistence and
low-wind durations established in the Northern European literature, no single
reserve layer of plausible size bounds the right tail of the loss-of-load
distribution; the reserve-sizing question is mis-specified, not merely unsolved.
Second, the historical adequacy buffer for Finland — decorrelated, dispatchable
cross-border import — is both correlated with the stress it is meant to offset and
is being removed on a legislated schedule, replaced by generation that is itself
calm during the same synoptic event. The continuity gap identified in WP-001 is
therefore, in this system, not closable by reserve sizing alone. The loss is not a
forecasting failure; it is an unowned mandate. The paper contributes one datapoint
to the convergence documented in SM-007 and one sharpening of CN-004: a buffer loss
that is statutory and dated — detection delay near zero — yet still converts to no
present decision cost for any identifiable actor.

---

## §1 What this version withdraws

SP-001 v1.0 reported that a reserve layer of 300 MW power and 72 h energy budget
reduced the 99th-percentile loss-of-load expectation to zero in a Monte Carlo of a
wind-dominant Finnish system, where a 48 h budget did not. The result is withdrawn
for two independent reasons established during review.

The result depended on the wind-persistence coefficient ρ. The paper's own
sensitivity analysis showed the 72 h result holding near ρ = 0.92 and failing
catastrophically near ρ = 1.0, with no simulated point between — and the
empirically relevant hourly persistence of aggregate wind sits in that unsimulated
interval, close to the failing end. A result that inverts across the range of its
dominant parameter, evaluated at a value where it fails, is not a finding.

Independently, the result was incommensurate with the paper's own compound-stress
definition. Under constrained import — a stated condition of the modelled stress —
the residual supply deficit during a cold, calm period is on the order of thousands
of megawatts, while the reserve power was 300 MW. A 300 MW layer can be the margin
between adequacy and shortfall only if import remains nearly unconstrained, which
contradicts the premise. The reserve-sizing result existed only in a regime that
the paper's own scenario excludes.

This version does not attempt a better-calibrated sufficiency claim. It states what
survives.

## §2 Parameters are cited, not estimated

This paper does not estimate meteorological parameters. The quantities that govern
adequacy under wind dominance are established in the peer-reviewed literature, and
that literature is more authoritative than any single-zone calibration this
institute could perform.

**Spatial and temporal structure.** Multi-day variability in European wind power is
organised by large-scale weather regimes operating on a spatial scale of roughly
1000 km and time scales exceeding five days. Blocked regimes bring high surface
pressure, strongly reduced winds, and — in winter — fog and cold (Grams, Beerli,
Pfenninger, Staffell & Wernli, 2017, *Nature Climate Change* 7:557–562). The same
study establishes the property that matters most here: a lull is not local. It
removes wind power across neighbouring countries simultaneously, and it coincides
with the cold conditions that raise demand. Balancing this variability requires
deploying wind capacity in regions of *contrasting* regime behaviour — the authors'
example is the Balkans versus the North Sea — because adjacent, synoptically
similar regions rise and fall together. Solar could offset low-wind regimes locally
only by expanding capacity roughly tenfold, which in Finnish winter is not a
mitigation at all.

**Cross-country simultaneity.** A climatology of low-wind, low-solar events over the
North and Baltic Sea areas (Li et al., 2021, *Energies* 14:6508, ERA5/MERRA-2,
1985–2016) quantifies the correlation that determines whether neighbours can help.
Event correlation between neighbouring countries is approximately 0.3–0.4, peaking
at 0.5–0.6 for closely coupled pairs such as Denmark–Sweden; individual country
pairs overlap in 30–40 % of drought events. Simultaneous occurrence across all
analysed countries is rare — which is the basis for the interconnection argument —
but the decorrelation that helps comes from *distant, contrasting* regions, not
from the synoptically coupled Nordic–Baltic zone in which Finland's import
neighbours sit. Almost all events longer than 24 h fall in November, December and
January.

**Event scale.** Reported Dunkelflaute frequency for Northern Europe is on the order
of 2–10 events per year, concentrated October–February, totalling roughly 50–150
hours annually, with individual events lasting from several hours to multiple days
(see Li et al., 2021; review summaries in the Dunkelflaute literature). The point
relevant here is not the European-scale storage figure — that is a continental
copperplate result and a different question of scale — but the structural fact it
rests on: in a wind-dominant system the binding constraint on firming capacity is
set by the extreme-duration tail of low-generation events, not by their mean or
typical variability. Designing to the typical event leaves the tail uncovered.

**Finnish single-zone measurement (the one original input, now reproduced and
sourced).** From the Finnish national hourly production series (2022–2025, wind
power column), normalising each year's hourly wind output by that year's
published cumulative installed capacity (Suomen Tuulivoimayhdistys / Suomen
uusiutuvat ry annual statistics: 5,677 MW end-2022; 6,949 MW end-2023; 8,358 MW
end-2024; 9,433 MW end-2025) and counting contiguous hours below 10 % capacity
factor, the matched-fleet window 2022–2025 yields 173.5 wind-lull episodes per
year, mean duration 13.3 h, P90 31 h, and a maximum of 159 h. Reproduced
independently 2026-07-07; figures confirmed against the original claim within
rounding. Note that annual mean capacity factor over the same window (23–28 %)
rose year over year, meaning year-specific — not fleet-averaged — capacity
normalisation is required even within this four-year window; the fleet itself
grew by roughly 66 % (5,677 to 9,433 MW) over the period and is not, strictly,
"matched." Two points are worth stating
plainly. First, these durations are several times longer than the values used in
SP-001 v1.0 (mean 3.19 h, maximum 45 h), which understated the phenomenon in every
dimension and in the direction that made the v1.0 result appear safe. Second, the
measured maximum (159 h, about 6.5 days) is consistent with the >5-day synoptic
blocking scale of Grams et al. (2017), whereas the v1.0 maximum was not. The
single-zone framework is necessary but not sufficient: it cannot represent the
cross-border simultaneity of §2, which is the variable that decides whether import
is available during the event.

## §3 The non-robustness finding

The structure is standard and is not re-derived here: aggregate wind output during
blocking regimes falls and stays low for the synoptic duration of the regime, and a
reserve layer with finite energy budget can span an event only if the event is
shorter than the budget. The persistence of the low-wind state therefore governs
whether any given reserve duration bounds the adequacy tail.

The consequence is qualitative and robust, and it is a statement about cost, not
about possibility. At the low-wind durations established above — P90 on the order of
a day, maxima on the order of several days, concentrated in the cold months when
demand peaks — a single reserve layer sized to span the *typical* event does not
span the *tail* event, and the tail is where loss-of-load lives. A reserve large
enough to span the tail can always be specified in principle; the difficulty is not
impossibility. It is that the marginal cost of firming rises non-linearly with the
duration to be covered, while the tail duration is set by synoptic meteorology and,
on the evidence, is lengthening into the design horizon rather than shrinking. So
the honest statement is not "no reserve bounds the tail" but: *there is no reserve
duration of economically plausible scale that bounds the tail, and the cost of the
one that would is borne by no identifiable actor.* Framed this way, §3 is not a
separate technical result competing with §5 for the paper's contribution — it is
§5 expressed in the language of cost. The reserve-sizing question is mis-specified
in the same way and for the same reason the buffer question is: the quantity that
would close the gap exists, but nothing converts its future necessity into a present
cost anyone holds.

A Monte Carlo realisation of this mechanism is given in Appendix A. It is
illustrative, not probative: it shows the persistence sensitivity and the
duration-threshold behaviour, and it is used only to locate where a single reserve
layer ceases to bound the tail. It certifies no reserve size.

## §4 The buffer, historically

The reason Finnish adequacy has not failed under past cold, calm periods is import.
In the national hourly series, net import rises during Finnish low-wind hours (mean
on the order of 1.4–2.0 GW against an all-hours mean well below that), and only a
small fraction of low-wind hours coincide with net export. Empirically, when
Finland was calm, neighbours generally had surplus to send. This historical fact
contradicts the constrained-import premise of SP-001 v1.0 for the period observed:
the buffer was real and was usually available.

The buffer's character differs by interface, and none of the interfaces is a firm
constant of the kind v1.0's capacity table assumed.

- **SE1 / SE3 (Sweden).** Northern Sweden is hydro-dominated; its capacity to export
  during a Finnish lull depends on reservoir state, not on Swedish wind. Hydro is a
  conditional, storage-limited buffer, not a firm block. The Saimaa drawdown of
  early 2026 is direct evidence of the conditionality on the Finnish side: after a
  multi-year dry period, Vuoksi outflow was restricted (≈ 490 m³/s against a normal
  ≈ 600), and Imatra hydro output fell to 60–70 % of normal (Yle, 13 March 2026).
  Dry periods are not independent of calm periods — blocking highs bring both — so
  hydro availability correlates positively with wind lulls on seasonal and synoptic
  scales. The buffer is partly down for the same reason the stress is present.
- **EE (Estonia).** Estonia is not a wind neighbour but a dispatchable one: its
  historical exports to Finland during cold spells came from oil-shale plant called
  on price spikes, delivered via EstLink. The interconnector is bounded at roughly
  1000 MW combined, against an Estonian peak demand near 1.6 GW — a small system.

## §5 The disappearing buffer (original contribution)

The historical buffer is not stable. It is being removed on a legislated schedule,
and what replaces it is correlated with the stress.

Estonian oil-shale electricity is under a statutory phase-out, with targets that
have moved between roughly 2030 and 2035 — and the revision toward later dates has
been driven explicitly by grid-stability concern, which is itself evidence that the
dispatchable role is recognised as load-bearing even as it is retired. Its
replacement is wind and solar, on a path toward a fully renewable Estonian system.
The consequence is not that the buffer shrinks; it is that the buffer **inverts**.
The claim is deliberately not that all wind correlates everywhere — that would be
false and unnecessary. It is narrower and testable: *the probability that
neighbouring systems can provide firm support declines under precisely the synoptic
regimes that create Finnish scarcity.* A decorrelated, dispatchable interface
becomes a scarcity-correlated, intermittent one. The neighbour that exported during
a Finnish blocking lull — drawing on dispatchable oil shale — becomes a neighbour
whose replacement wind is itself low in the same lull, because, per §2, the blocking
regime that calms Finland calms the synoptically coupled Baltic with it. The same
scarcity correlation threatens the Swedish hydro interface to the extent that Nordic
reservoirs are drawn down by the same multi-year dry-and-calm regimes — the Saimaa
drawdown being the Finnish-side instance of exactly that coupling. What disappears
is not the interface but its *independence from the event*: support remains
available on ordinary days and withdraws on the days that matter.

This is where the paper makes a claim that is its own rather than the corpus's.
In most instances catalogued in SM-007, the structural failure is associated with a
high *detection delay* — the degradation is real but not yet visible, and the
analytically critical variable in CN-004's framework is the interval between
threshold crossing and political recognition. The disappearing buffer is the
opposite case. The loss is **statutory and dated**: the phase-out is written into
law, the interconnector limits are published, the reservoir hydrology is measured
daily, and the meteorological correlation is in the peer-reviewed literature.
Detection delay is near zero. Everyone who would need to see it can see it.

And still no mechanism converts the dated future loss into a present cost for any
identifiable actor. Finnish system operation governs reserves and grid stability,
not the generation mix of a neighbouring state. Estonian decarbonisation policy
governs Estonian emissions, not Finnish winter adequacy. Nordic market design
prices energy and capacity within its mechanisms, none of which holds a mandate over
"what replaces the cross-border dispatchable buffer when it is legislated away."
The replacement question falls between every mandate that touches it.

This sharpens CN-004's structural-property interpretation. If the failure persisted
only where detection delay is high, it could be read as a correctable information
problem — build the monitoring, transmit the signal, and correction follows. The
buffer case removes that escape: detection is not the binding constraint. A loss
that is legislated, dated, measured, and published still does not convert to present
cost. What is missing is not visibility but ownership. That is a structural
property of distributed mandates, not a coordination fault to be fixed with better
information — exactly the distinction CN-004 frames, here instantiated in a case
where the usual confound (latency) is absent.

## §6 What this paper does not argue

The general structures invoked above are owned elsewhere in the corpus and are
cited, not restated:

- The general condition — no mechanism converts future failure probability into
  present decision cost — is **SM-007**. This paper is one further instance feeding
  that convergence.
- The energy-domain allocation bias (stability-providing infrastructure earns less
  political visibility than consumption-binding investment; no actor sees the
  aggregate) is **WP-008**.
- The Black Period energy-requirement-versus-instrument-capacity gap (storage
  covering a negligible fraction of the requirement) is **DA-003**.
- The active early-warning signal state for Finland is **DA-001**.
- The anatomy of the mandate gap across Fingrid, TEM, and system endurance is
  **SM-007 §02**.
- The correctable-versus-structural question, the A/R/D regime framework, and the
  detection-delay variable are **CN-004**.

This paper's contribution is confined to two things: the demonstration that
reserve-duration adequacy is non-robust at literature-level persistence (§3), and
the disappearing-buffer instance with near-zero detection delay (§5).

## §7 Falsification

The claim is structural and is falsified by any one of the following.

1. A single reserve layer of plausible size bounds the adequacy tail at the
   persistence and low-wind durations established in the cited literature. (Refutes §3.)
2. A connected neighbour retains dispatchable export capacity whose availability does
   *not* decline under the synoptic regimes that produce Finnish low-wind scarcity —
   i.e., the support is firm precisely when it is needed, not merely on average. It
   is not enough to show high annual interconnection or positive average import; the
   test is conditional availability during the scarcity regime itself. (Refutes §5's
   premise.)
3. Some identifiable actor holds a mandate under which the dated future loss of the
   buffer is priced into a present decision. (Refutes §5's conclusion and, with it,
   this paper's contribution to SM-007.)

Note that conditions 1 and 2 are empirical and addressable with the cited
literature plus interconnection and phase-out data; condition 3 is institutional and
is the one that matters most. If it can be met, the problem is a coordination fault
and CN-004's Interpretation I applies. On present evidence it cannot.

---

## Appendix A — Monte Carlo illustration (not a proof)

The model is a vectorised hourly simulation of margin = firm dispatchable + wind +
import − demand, with a reserve layer defined by power cap and energy budget, run
over many annual replications. It exists solely to illustrate the §3 mechanism: how
the loss-of-load tail responds as wind persistence is swept across the range
spanning the literature value, and where a fixed reserve duration ceases to bound
the tail. It certifies no reserve size and should not be cited as an adequacy result.

Every constant is flagged as either drawn from the cited literature or as a
modelling choice of the author; none is presented as a calibrated system truth. The
appendix also records the structural caveat surfaced in development: under the
constrained-import condition of a genuine compound stress, the residual deficit is a
large multiple of any plausible reserve power, so the duration-threshold effect is
visible only in an import-available regime — which is precisely the regime a real
Black Period excludes. That caveat is the quantitative shadow of §5: the model can
only "solve" adequacy by assuming the buffer that §5 shows is disappearing.

---

## References (to complete from sources before publication)

- Grams, C. M., Beerli, R., Pfenninger, S., Staffell, I., & Wernli, H. (2017).
  Balancing Europe's wind-power output through spatial deployment informed by
  weather regimes. *Nature Climate Change*, 7(8), 557–562.
- Li, B., Basu, S., Watson, S. J., & Russchenberg, H. W. J. (2021). A Brief
  Climatology of Dunkelflaute Events over and Surrounding the North and Baltic
  Sea Areas. *Energies*, 14(20), 6508.
- Olauson, J., & Bergkvist, M. (2016). Correlation between wind power generation
  in the European countries. *Energy*, 114, 663–670. [Background reference,
  carried over from WP-001 §8; not cited inline in this paper's body text.]
- Staffell, I., & Pfenninger, S. (2018). The increasing impact of weather on
  electricity supply and demand. *Energy*, 145, 65–78. [Background reference,
  carried over from WP-001 §8; not cited inline in this paper's body text.]
- Yle (2026, 13 March). Saimaan vedenkorkeus / Vuoksi outflow restriction; Imatra
  hydro output 60–70 % of normal. [Finnish national broadcaster news report.]
- Estonian oil-shale electricity phase-out schedule and EstLink capacity — [confirm
  primary sources: Estonian national energy and climate plan; TSO interconnector
  specifications].
- Suomen Tuulivoimayhdistys / Suomen uusiutuvat ry. Annual wind power statistics
  ("Tuulivoima Suomessa"), 31.12.2022, 31.12.2023, 31.12.2024, 31.12.2025.
  https://suomenuusiutuvat.fi — cumulative installed capacity figures used for
  capacity-factor normalisation in the single-zone measurement above.
- Finnish national hourly production data, 2010–2025 (author-compiled workbook,
  `tuntidata_2010-2025.xlsx`; wind power column used for §2's single-zone
  measurement, reproduced 2026-07-07).
- ACI corpus: WP-001, WP-008, DA-001, DA-003, SM-007, CN-004.

*Author to verify all bracketed items against primary sources before publication.
No quantitative value in this draft should be published without a confirmed source.
The single-zone Finnish figures have now been reproduced (2026-07-07) against
`tuntidata_2010-2025.xlsx` using published Suomen Tuulivoimayhdistys / Suomen
uusiutuvat ry capacity figures for normalisation — see §2. Grams et al. (2017)
and Li et al. (2021) citations verified against primary sources (2026-07-07):
authors, journal, volume, pages, and DOI confirmed correct as cited. Still
outstanding: the Estonian oil-shale phase-out schedule and EstLink capacity
citation below remains bracketed and unconfirmed.*
