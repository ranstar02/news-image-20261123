# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ranstar02/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ranstar02/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up Monday 23 November 2026 in one image: six stories from Ukraine, Libya, the United States, Indonesia and sport, plus the day's other headlines in the footer.

The image (`entry.png`, 1024×1024) is drawn from scratch by `draw.py` (Python + PIL: masthead, date, six news cards with hand-drawn pictograms). `main.ts` (Node 22, standard library only) copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Run it

```sh
python3 draw.py            # re-render entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=0m7x29es&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
