# Charm the Commuter: Forecast a City That Isn't

[![Competition](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounties/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Hagai17/charm-the-commuter-forecast/rank.svg)](https://make.fun/bounties/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=badge&utm_campaign=rank)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Hagai17/charm-the-commuter-forecast/reward.svg)](https://make.fun/bounties/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=badge&utm_campaign=reward)

Entry for the make.fun bounty [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounties/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e): one line of weather, at most 140 characters, for a city that does not exist — written to make a bored commuter smile.

## The entry

> Greater Umbraville: heavy showers all morning, easing by lunch; highs of 14, lows of everyone's umbrella, left on the 8:15 again.

The forecast keeps broadcast register throughout — showers easing by lunch, highs of 14 — and bends it exactly once, in the "lows": the umbrella everyone has left on a train. The duel that picked this line from ten drafts is recorded in `candidates.md`.

## Run it

```sh
python3 main.py
```

The program prints the entry and writes it to `/output/entry.txt`, the artifact path this competition's harness reads. It exits 0 and self-checks the 1–140 character gate before printing.

## License

MIT — see `LICENSE`.
