# The World in One Day — 23 November 2026

A newspaper front page summing up Monday 23 November 2026 in one image:
six stories from Ukraine, Libya, the United States, Indonesia and sport,
plus the day's other headlines in the footer.

The image (`entry.png`, 1024×1024) is drawn from scratch by `draw.py`
(Python + PIL: masthead, date, six news cards with hand-drawn pictograms).
`main.ts` (Node 22, standard library only) copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png`.

Run it:

```sh
python3 draw.py            # re-render entry.png
MAKEFUN_OUTPUT_DIR=out node main.ts
```
