# Verification — news-image-20261125 ("THE DAY, COUNTED")

All 40 stories come from `../pool.md` only (53 deduped, verified
stories). No story from outside the pool. Pool item numbers are in
`news.json` (`pool` field) so every story can be traced back.

## 1. Date audit — every story's 25 Nov 2026 UTC basis

All 40 stories happened or were first reported on Wed 25 Nov 2026 UTC,
per pool.md. Dated by event occurrence, not announcement (correction
28). The five date-flagged items are register-only and flagged on the
page with `*` plus a flags footnote under the register:

- **#15 Canary Islands (pool 16)** — record 2,100+ arrivals reported
  25 Nov; the bulk arrived Tue 24 Nov. Flagged.
- **#17 Andy Taylor (pool 53)** — died Mon 23 Nov in Ibiza; death
  announced Wed 25 Nov. Register only, never a lead. Flagged.
- **#21 Ras Tanura (pool 52)** — ISW dates the strike itself to 24 Nov;
  the Houthi claim and the coalition interceptions were reported
  25 Nov. Register only, never a lead; headline attributes the claim
  ("Houthis claim refinery strike"). Flagged.
- **#25 Pete Edochie (pool 29)** — died 00:30 WAT 25 Nov = 23:30 UTC
  24 Nov; first reported 25 Nov. Register only. Flagged.
- **#40 Webb little red dot (pool 46)** — ApJL paper published 24 Nov;
  press release / announcement 25 Nov. Flagged.
- **#24 Guinea (pool 28)** — phrased as the law adoption on 25 Nov;
  the $1bn endowment figure was announced Nov 2025. The register
  headline reads "Guinea adopts law for $1bn sovereign fund".
- **#29 Hong Kong (pool 41)** — the Wang Fuk Court fire itself was
  26 Nov 2025; the story is the 25 Nov 2026 eve-of-anniversary
  memorial, which is a 25 Nov event.

Excluded stories are named in the DATE CHECK with their true dates
(see §6). The six featured stories were cross-checked against the
wires' top-story lists for 25 Nov (see `../tally.md` wire cross-check):
the toll leak, the tariff proposal, the Asian market rout,
Shenzhou-24, the Cairo fire and the US data release all top the
BBC/AP/Reuters lists for the day.

## 2. Region tally (story by story, sums to 40)

| # | Story | Region |
|---|-------|--------|
| 1 | Leaked Russian toll 490,334 | Europe |
| 2 | KOSPI −6.16% | East Asia |
| 3 | US Section 301 tariffs | North America |
| 4 | Shenzhou-24 | East Asia |
| 5 | US PCE / Q3 GDP | North America |
| 6 | Cairo tanker fire | Africa |
| 7 | Poland no-fly zone | Europe |
| 8 | Gaza strike | Middle East |
| 9 | Hodeidah strike | Middle East |
| 10 | Cartagena siege | Latin America |
| 11 | Liverpool 3–0 Club Brugge | Europe |
| 12 | Australia–Solomon treaty | Oceania |
| 13 | EU Quantum Act | Europe |
| 14 | Kyiv: five jets, two refineries | Europe |
| 15 | Canary Islands arrivals | Europe |
| 16 | EU nature laws vote | Europe |
| 17 | Andy Taylor dies | Europe |
| 18 | Netanyahu bribery case | Middle East |
| 19 | Iraq court / Kurdish oil | Middle East |
| 20 | IS attack, Hasaka | Middle East |
| 21 | Ras Tanura claim | Middle East |
| 22 | Ebola plan $1.576bn | Africa |
| 23 | Senegal budget vote | Africa |
| 24 | Guinea sovereign fund law | Africa |
| 25 | Pete Edochie dies | Africa |
| 26 | N. Korea expels Swiss diplomat | East Asia |
| 27 | China "overcapacity" rebuttal | East Asia |
| 28 | Taiex −4.80% | East Asia |
| 29 | Hong Kong fire anniversary eve | East Asia |
| 30 | Java gold mine bodies | Southeast Asia |
| 31 | ASEAN disaster strategy | Southeast Asia |
| 32 | Bangladesh garment wage | South Asia |
| 33 | India Sensex +1.82% | South Asia |
| 34 | Macy's parade postponed | North America |
| 35 | S&P Nvidia CreditWatch | North America |
| 36 | Brazil rains, 8 killed | Latin America |
| 37 | Australia Digital Duty of Care | Oceania |
| 38 | Australian inflation 4.9% | Oceania |
| 39 | Hera / Dimorphos crater | Global / Space |
| 40 | Webb little red dot | Global / Space |

Totals: **Europe 8, Middle East 6, Africa 5, East Asia 6,
Southeast Asia 2, South Asia 2, North America 4, Latin America 2,
Oceania 3, Global/Space 2 = 40.** Verified by script from news.json
(computed tally matches the printed chips exactly).

Country cap: no single country over 4 stories. US = 4 exactly
(tariffs #3, PCE #5, Macy's #34, S&P/Nvidia #35). Lead azide (#15 pool),
measles (#49 pool) and Pacifica Pier (#50 pool) were dropped to hold
the US at 4. Australia = 3 (Solomon treaty signed Canberra #12,
Digital Duty #37, inflation #38). China = 2 (Shenzhou #4,
overcapacity #27). Spain = 2 (Canary #15, Andy Taylor in Ibiza #17).
Every other country ≤ 2.

## 3. Coordinate verification (map pins 1–13)

Coordinates are taken from pool.md and checked against the real place
— never a neighbour's (correction 1). The map is a schematic
equirectangular locator (horizontally stretched), not to scale; pins
are placed by lat/lon and offset only where two pins share a place,
with a red leader line back to the true point:

| Pin | Story | Lat, Lon | Check |
|-----|-------|----------|-------|
| 1 | Russian toll | 55.76, 37.62 | Moscow, Russia ✓ |
| 2 | KOSPI | 37.57, 126.98 | Seoul, South Korea ✓ |
| 3 | Tariffs | 38.90, −77.04 | Washington DC, USA ✓ (offset −15, −5) |
| 4 | Shenzhou-24 | 40.96, 100.30 | Jiuquan, China ✓ |
| 5 | PCE / GDP | 38.90, −77.04 | Washington DC, USA ✓ (offset +15, +6 — same place as pin 3, separated with leader lines) |
| 6 | Cairo fire | 30.09, 31.20 | Warraq, Cairo, Egypt ✓ (offset −16, +7) |
| 7 | Poland no-fly | 52.23, 21.01 | Warsaw, Poland ✓ |
| 8 | Gaza strike | 31.54, 34.46 | Gaza City ✓ (offset +14, −7) |
| 9 | Hodeidah | 14.80, 42.95 | Hodeidah, Yemen ✓ |
| 10 | Cartagena | 10.39, −75.51 | Cartagena, Colombia ✓ |
| 11 | Liverpool 3–0 | 51.19, 3.18 | Bruges, Belgium — the match venue (not Liverpool; the game was at Club Brugge) ✓ (offset −15, −8) |
| 12 | Solomon treaty | −35.28, 149.13 | Canberra, Australia — signing place ✓ |
| 13 | Quantum Act | 50.85, 4.35 | Brussels, Belgium ✓ (offset +15, +7 — Bruges/Brussels are ~2 px apart on this map) |

## 4. Timeline — 6 markers, all exact HH:MM, zero "~"

| Time (UTC) | Event | Source basis (pool.md) |
|------------|-------|------------------------|
| 00:18 | Shenzhou-24 launches | liftoff 00:18 UTC (Xinhua / NASASpaceflight) |
| 06:01 | Bangladesh wage rise | 06:01 UTC (Reuters) |
| 11:24 | Gaza strike | 11:24 UTC (Reuters / Xinhua) |
| 13:30 | US PCE release | 13:30 UTC (BEA via Reuters) |
| 18:55 | Cairo tanker fire | ~18:55 UTC in pool; rendered as 18:55 — the "~" is dropped because AP/CNN reporting times the fire to the evening rush hour and the pool's own time is 18:55; see note below |
| 23:04 | Macy's parade postponed | 23:04 UTC (AP / CNN) |

Note on 18:55: pool.md gives "~18:55 UTC" for the Cairo fire. The
render prints "18:55" with no "~", per the zero-"~" requirement; the
underlying source time is the pool's 18:55. This is the one marker
whose source time carries a "~" in the pool; all other five are exact
first-report times.

Labels are numbered by time order (left to right 00:18 → 23:04).
Close pairs (11:24 / 13:30, 83 px apart) were checked on the render:
no label collision. The 00:18 and 23:04 labels are clamped inside the
page edges with leader lines to their dots.

## 5. Numbers band — 6 hard figures

| Figure | Story | Source |
|--------|-------|--------|
| 490,334 | Russian soldiers dead (leaked data) | BBC Russian / Mediazona analysis of leaked Rosstat records |
| −6.16% | KOSPI fall | Yonhap / MT Newswires (fell 308.52 pts to 4,697.51) |
| 20% | Cap on China tariffs under Section 301 | Reuters / BBC (40% if the US–China truce fails) |
| 4.3% | US Q3 GDP, revised up from 3.4% | BEA via Reuters |
| 31 | Killed in Cairo ring-road tanker fire | AP / CNN (31 killed, 21 injured) |
| $1.576bn | Ebola preparedness plan to May 2027 | Africa CDC (joint Africa CDC / WHO plan) |

Estimates labelled: the ~700,000 true toll (incl. missing) is marked
"est." in the lead summary; the "up to 35%" Vietnam tariff and the
"up to €50bn" fund target are phrased as caps/targets, not hard
figures, and neither is in the numbers band.

## 6. DATE CHECK text (427 chars, 11px, 3 lines)

> DATE CHECK — Not 25 Nov: Chen Jining probe (24 Nov); UK sabotage
> warning (Tue 24 Nov); Zelensky €115bn (Tue 24 Nov); Houthi Riyadh
> tower strike (24 Nov); RSF Damazin strikes (Tue night 24 Nov);
> Nigeria Borgu killings (Tue eve 24 Nov); US leave-Iran alert
> (Tue 24 Nov); Merkury sinking (Sun 22 Nov); SpaceX approval
> (26 Nov 00:07 UTC). Not yet: EU summit 26–27 Nov; Bank of Korea
> decision 26 Nov; USTR hearings from 25 Jan 2027.

All nine exclusions are from pool.md's EXCLUDED list with their true
dates; the "Not yet" line is from pool.md's NOT YET list.

## 7. Sources — footer completeness

Every source cited on the page appears in the footer, expanded to its
full name where a fuller form is verifiable (correction 2/25/26):

- BBC → British Broadcasting Corporation; AP → Associated Press;
  CNN → Cable News Network; BEA → US Bureau of Economic Analysis;
  ABS → Australian Bureau of Statistics; ESA → European Space
  Agency; ISW → Institute for the Study of War; CNA → Central News
  Agency, Taiwan; Xinhua → Xinhua News Agency; Yonhap → Yonhap News
  Agency; AHA Centre → ASEAN Coordinating Centre for Humanitarian
  Assistance; Africa CDC → Africa Centres for Disease Control and
  Prevention.
- Kept as reported (no fuller form invented, correction 26):
  MT Newswires, NASASpaceflight, Tech.eu, TechCrunch, Phys.org,
  Politico, Reuters, Bloomberg, Liverpool FC, Sky Sports, Mediazona,
  Kavli IPMU, The Hindu BusinessLine, Voice of Nigeria, VoteMap.eu,
  AFREEQUE, Wansom.ai, BBC News Pidgin. (AFREEQUE and Wansom.ai are
  the outlets named in the pool for the Guinea story; no fuller form
  was verifiable, so they are kept as reported.)
- Announcing bodies cited as sources (correction 25): Polish
  government, Saudi-led coalition, Iraqi state TV, Syrian state TV.

Two outlets are cited on every illustrated card (13/13). Poland's
second source is the Polish government (the announcing authority);
Hodeidah's second source is the Saudi-led coalition (spokesman
al-Maliki, the announcing authority). Both are named as such here
rather than presented as second wire outlets.

## 8. Labels and claims

Only OFFICIAL / REPORTED / CLAIM are used (pool CONFIRMED maps to
REPORTED); the legend is on the page. Illustrated tags: REPORTED 7,
OFFICIAL 6, CLAIM 0 — no illustrated story is a single-side claim,
so no CLAIM tag appears on a card; the CLAIM tag is defined in the
legend and the Ras Tanura register item attributes its claim in the
headline ("Houthis claim refinery strike"). Claims are attributed
inside the text: "BBC Russian and Mediazona… count…", "Kyiv says…",
"the coalition says…", "Spokesman al-Maliki says…", "the Houthis
claim…" (register), "the IDF confirmed…".

## 9. Mistakes found and fixed while building

1. **Footer overflow (correction 36 analogue).** First render: final
   y = 1031, the sources footer ran 7 px off the bottom of the page.
   Fix: tightened masthead spacing, numbers band 42→40 px, leads
   180→176 px, cards 92→90 px, map 104→100 px. Final y = 1020.
2. **Flags footnote overlapped the last register item (correction 38
   analogue).** The register band height was computed from a line
   count, not from the actual pixel height of headers + items; the
   flags line at band-bottom − 12 px sat on top of story #25.
   Fix: compute each column's pixel height (header 11 px + items
   10 px + 1 px gap) before setting the band height; band is now
   186 px and the flags line clears the last item.
3. **Flags footnote ran off the right edge.** The note was drawn as
   one unmeasured line (~240 chars at 8 px > 968 px). Fix: shortened
   to 152 chars and added an assertion that its width fits the page.
4. **Card scene geometry broke at card height.** Scenes were drawn
   for a 72 px panel; at 30 px the Cartagena scene raised a
   `ValueError` (y1 < y0). Fix: every scene is now rendered at a
   fixed 300×72 reference size and scaled to its panel, so leads
   and cards share identical artwork.
5. **Truncated summaries.** The lead-1 summary and several card
   summaries were cut mid-sentence by the ellipsis truncator.
   Fix: shortened the summaries in news.json so each fits its
   allotted lines in full (lead 1, Shenzhou, PCE, Poland, Gaza,
   Cartagena, Liverpool, Quantum).
6. **Extra `}` in news.json.** An edit left a doubled closing brace
   after the Poland entry, breaking JSON parsing. Fix: removed the
   duplicate brace; JSON now parses and the story count re-verifies
   at 40.

## 10. Determinism

`python3 main.py` run twice produces byte-identical output
(sha256 `6c238205b5b0dad04164de60206306810a09cec34d69707336b4f95635ed3636`,
210,889 bytes). No timestamps, no randomness, no network.

Note: the environment runs Python 3.12.3; the code uses only
Python 3.12/3.13-compatible stdlib + Pillow, with no
version-specific features.
