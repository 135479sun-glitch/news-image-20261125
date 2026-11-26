# THE DAY, COUNTED — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/135479sun-glitch/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/135479sun-glitch/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image summary of 25 November 2026's world news, built for the
make.fun `news-image-20261125` competition ("Sum up 25 November's world
news in one image").

## The concept

A ledger / balance-sheet broadsheet: the day as six ledger entries built
around big numerals. Fresh concept for this edition — 23 Nov was
map-first ("The Atlas of a Day"), 24 Nov was wire-feed timeline-first
("Tuesday, As It Came In"). The density components are all present:
masthead spec strip, region chips, numbers band, 13 illustrated stories,
exact-time UTC timeline, locator map with 13 numbered pins, compact
register grouped by region, red-bordered DATE CHECK, full source footer.

## The 40-story spec

- **40 stories**, all from the verified deduped pool in
  `../pool.md` (53 stories; no story from outside the pool).
- **10 regions**: Europe 8, Middle East 6, Africa 5, East Asia 6,
  Southeast Asia 2, South Asia 2, North America 4, Latin America 2,
  Oceania 3, Global/Space 2. Tally computed story-by-story from the
  data in `news.json`; it sums to 40.
- **No single country over 4 stories**: the US appears exactly 4 times
  (Section 301 tariffs, PCE/GDP, Macy's parade, S&P/Nvidia).
- **13 illustrated stories** (3 large ledger leads + 10 small cards),
  each with a drawn PIL vector-style scene, a number badge, a big-number
  chip, an OFFICIAL / REPORTED / CLAIM tag and 2 sources. A card
  without a picture does not count as featured.
- **Featured six** (10 genuinely independent ranking passes, see
  `../tally.md`): leaked Russian toll 490,334 (10/10); KOSPI −6.16%
  (10/10); US Section 301 tariffs (9/10); Shenzhou-24 (8/10);
  US PCE 3.8% / Q3 GDP 4.3% (8/10); Cairo tanker fire, 31 killed (7/10).
- **UTC timeline**: exactly 6 markers, all exact HH:MM, zero "~",
  spanning the full day (00:18–23:04).
- **Numbers band**: exactly 6 hard figures, each tied to a story.
  Estimates are labelled (the ~700,000 toll estimate is marked "est.").
- **DATE CHECK**: red-bordered, 11px, 427 chars; names excluded stories
  with their true dates plus a "Not yet" line.
- **Labels**: only OFFICIAL / REPORTED / CLAIM (pool CONFIRMED maps to
  REPORTED), with a legend. Every claim is attributed inside the text
  ("Kyiv says…", "the Houthis claim…", "the coalition says…").

## Files

- `main.py` — renders the page. Python 3.13, PIL only. Deterministic:
  fixed geometry, fixed fonts, no clock, no randomness, no network.
  Run twice and the output is byte-identical (verified).
- `entry.png` — the 1024×1024 render.
- `news.json` — the 40 stories as structured data (headline, summary,
  sources, tag, region, lat/lon, time).
- `verification.md` — date audit, region tally, coordinate verification,
  timeline times, numbers-band figures, DATE CHECK text, date flags.
- `LICENSE` — MIT (pre-existing, untouched).

## How to run

```sh
python3 main.py
```

Writes `entry.png` beside itself and `/output/entry.png` (when
`/output` exists). Requires Pillow and the DejaVu + Noto Serif fonts
present on the system. No network access is used.

## Date flags honoured

Ras Tanura (52) and Andy Taylor (53) appear only as small register
items, never as leads. Pete Edochie died 23:30 UTC 24 Nov, first
reported 25 Nov — register only, flagged. The Webb "little red dot"
paper was 24 Nov, press release 25 Nov — flagged. Canary Islands
arrivals bulk 24 Nov — flagged. Guinea is phrased as the law adoption
on 25 Nov (the $1bn figure was announced Nov 2025).

---

<sub>Entered on [make.fun](https://make.fun/?ref=j1mbjvhv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
