# The World on Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kainze29/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kainze29/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

One front page, one day: Thursday 19 November 2026, told in 50
stories. The masthead carries the date and a date check, the six
biggest stories of the day each get a photograph with a headline and
a short summary, stories 7 to 50 run as a numbered list below, and a
strip at the bottom places the day's turning points on a UTC timeline.
Every item on the page happened, or was first reported, on 19
November 2026.

## The six top stories

1. **Trump, Xi and Putin hold the first trilateral summit.** The
   three leaders met in Shenzhen for 80-90 minutes and signed a
   four-point declaration covering the UN, oil production and nuclear
   arms.
2. **The World Court finds Myanmar committed genocide.** The ICJ
   ruled 9-6 that Myanmar committed genocide against the Rohingya,
   the first time it has held a state guilty of genocide, and ordered
   reparations.
3. **Ukraine hits the Crimea Bridge a third time.** A new strike shut
   road traffic across the Kerch Bridge, and Putin vowed a "much more
   painful" response.
4. **Iran hits Gulf states after the US strike.** Iran attacked
   Kuwait and Bahrain after US jets struck Qeshm Island, and a Houthi
   missile was aimed at Riyadh.
5. **Anthropic's record $81bn IPO.** The Claude maker priced at $83
   a share, the largest IPO ever, valuing the company at $1.5
   trillion as it debuted on Nasdaq.
6. **Bangladesh burns as Hasina's return looms.** Muhammad Yunus's
   ancestral home was torched, violence hit 28 districts, and
   paramilitary forces were deployed.

## Stories 7 to 50

GTA VI goes on sale after a 13-year wait; COP31 stays deadlocked as
ministers meet in Antalya; the IEA calls the Hormuz crisis the top
threat to energy security; markets fall with the S&P down 0.23% and
the Hang Seng down 1.9%; the Dow drops 561 points for a fifth day
down; Nvidia falls 2.9% and Huang will not return; Trump says
Blackwell chips may one day go to China; Fed minutes flag AI risks
and stay open to bigger hikes; the IMF warns world debt is near 100%
of GDP; an IMF deal unlocks $2.3bn for Egypt; South Korean exports
top $1tn for the first time; Australian unemployment rises to 4.9%;
UK energy bills are set to rise £443 a year; Brent crude $89.59,
gold $3,739, bitcoin $63,552; the EU proposes €45bn more for
Ukraine; the EU approves an Indonesia trade deal; the US and
Venezuela sign a military pact; Israel runs a ground operation beyond
the Gaza yellow line and delays the E1 settlement; Ethiopia and
Eritrea mass troops at their border; drones drive the civilian toll
up in Sudan; 1 in 4 children live in conflict zones; five EU states
plan a Rwanda asylum hub; North Korea expanded uranium enrichment,
the IAEA says; Cyclone Aqwan nears the India coast; California sees
record rain from an atmospheric river; Fiji and Tonga declare a
drought emergency; the US loses its measles elimination status; Ebola
vaccine trials are to start in Congo; Waymo pulls driverless cars off
the roads; Webb confirms a rare star merger; blue whales are up
tenfold since whaling; NASA sets coverage for the CRS-25 launch;
Intel signs its first outside 18A customer; a Van Gogh sells for
$190.4m, a record for the artist; Imamoglu is sentenced in the Turkey
CHP case; Jeffries becomes the first Black Speaker nominee; Senegal's
ruling party splits from President Faye; a pastor is found guilty in
the Haiti president murder; Indonesia counts 3m hectares burned in
fires; Pakistan is hit by a nationwide internet outage; Assadi wins
the National Book Award; Alcaraz beats Medvedev at the ATP Finals;
Chelsea beat PSG 1-0 in the Women's Champions League.

## The day in UTC

02:00, the APEC plenary opens in Shenzhen; morning, Trump meets Putin
and then Xi one on one; midday, the first trilateral summit is held;
10:00, the ICJ rules Myanmar committed genocide; 14:30, Anthropic
debuts on Nasdaq; 21:00, Wall Street closes with the S&P at 7,324.

## Running it

`main.py` is Python 3.13, standard library only. It reads the
bundled `news.png`, checks it is a whole PNG under the 1 MiB limit
and no larger than 1024x1024 pixels, and writes it unchanged to
`entry.png` in the output directory. No network is used, so two runs
produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Contents

- `main.py` — the entry program described above
- `news.png` — the front page, 1024x1024 PNG, under 1 MiB
- `LICENSE` — MIT

The reporting behind each story comes from One Turn, Reuters, AP,
BBC, CNN, The Guardian, the Financial Times and Horizon, all dated 19
November 2026.
