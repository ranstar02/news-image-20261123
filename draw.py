#!/usr/bin/env python3
"""Draw the front page of THE WORLD IN ONE DAY, Monday 23 November 2026.

Renders a 1024x1024 newspaper front page from scratch with PIL: masthead,
date, a 2x3 grid of news cards (tag + pictogram + headline + sub-text) and a
one-line footer. All pictograms are simple shapes drawn with PIL primitives.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
RED = (185, 28, 28)
BLUE = (30, 58, 95)
CARD_BG = (255, 253, 247)
CARD_LINE = (216, 210, 196)
GOLD = (212, 160, 23)
ORANGE = (234, 88, 12)

FDIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FDIR + "DejaVuSerif-Bold.ttf"
SANS_B = FDIR + "DejaVuSans-Bold.ttf"
SANS = FDIR + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_burst(d, cx, cy, r):
    """Explosion starburst: alternating long/short spikes."""
    pts = []
    for i in range(24):
        ang = math.pi * 2 * i / 24
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=(234, 88, 12), outline=RED)
    d.ellipse([cx - r * 0.32, cy - r * 0.32, cx + r * 0.32, cy + r * 0.32],
              fill=RED)


def draw_ship(d, cx, cy, s):
    """Warship silhouette: hull, deck, mast, waves."""
    d.polygon([(cx - 42 * s, cy + 6 * s), (cx + 42 * s, cy + 6 * s),
               (cx + 30 * s, cy + 22 * s), (cx - 30 * s, cy + 22 * s)],
              fill=(51, 65, 85))
    d.rectangle([cx - 22 * s, cy - 10 * s, cx + 8 * s, cy + 6 * s],
                fill=(71, 85, 105))
    d.rectangle([cx - 8 * s, cy - 24 * s, cx + 2 * s, cy - 10 * s],
                fill=(71, 85, 105))
    d.line([cx + 16 * s, cy - 26 * s, cx + 16 * s, cy + 6 * s],
           fill=(51, 65, 85), width=3)
    d.polygon([(cx + 16 * s, cy - 26 * s), (cx + 30 * s, cy - 18 * s),
               (cx + 16 * s, cy - 14 * s)], fill=RED)
    for k, yy in enumerate((cy + 30 * s, cy + 38 * s)):
        d.arc([cx - 44 * s, yy - 6 * s, cx + 44 * s, yy + 6 * s],
              0, 180, fill=BLUE, width=3)


def draw_coin(d, cx, cy, r):
    """One-cent coin: gold disc, rim, 1c mark."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD, outline=(146, 100, 10),
              width=3)
    d.ellipse([cx - r * 0.72, cy - r * 0.72, cx + r * 0.72, cy + r * 0.72],
              outline=(146, 100, 10), width=2)
    f = font(SANS_B, int(r * 0.85))
    d.text((cx, cy), "1c", font=f, fill=(120, 80, 5), anchor="mm")


def draw_plane(d, cx, cy, s):
    """Airliner in side view: fuselage, tail, wings."""
    d.polygon([(cx - 44 * s, cy), (cx + 38 * s, cy - 10 * s),
               (cx + 48 * s, cy - 2 * s), (cx + 38 * s, cy + 8 * s),
               (cx - 30 * s, cy + 10 * s)], fill=BLUE)
    d.polygon([(cx - 40 * s, cy - 2 * s), (cx - 28 * s, cy - 24 * s),
               (cx - 18 * s, cy - 24 * s), (cx - 22 * s, cy - 2 * s)],
              fill=BLUE)
    d.polygon([(cx - 6 * s, cy + 8 * s), (cx + 6 * s, cy + 26 * s),
               (cx + 16 * s, cy + 26 * s), (cx + 12 * s, cy + 6 * s)],
              fill=(30, 58, 95))
    d.ellipse([cx + 34 * s, cy - 6 * s, cx + 44 * s, cy + 2 * s],
              fill=(255, 255, 255))


def draw_flame(d, cx, cy, s):
    """Flame: outer orange teardrop, inner red core."""
    d.polygon([(cx, cy - 34 * s), (cx + 16 * s, cy - 8 * s),
               (cx + 24 * s, cy + 12 * s), (cx + 12 * s, cy + 30 * s),
               (cx - 12 * s, cy + 30 * s), (cx - 24 * s, cy + 12 * s),
               (cx - 16 * s, cy - 8 * s)], fill=ORANGE)
    d.polygon([(cx, cy - 12 * s), (cx + 10 * s, cy + 6 * s),
               (cx + 8 * s, cy + 24 * s), (cx - 8 * s, cy + 24 * s),
               (cx - 10 * s, cy + 6 * s)], fill=RED)


def draw_trophy(d, cx, cy, s):
    """Trophy cup with handles, stem, base, and a tennis ball."""
    d.polygon([(cx - 22 * s, cy - 26 * s), (cx + 22 * s, cy - 26 * s),
               (cx + 14 * s, cy + 2 * s), (cx - 14 * s, cy + 2 * s)],
              fill=GOLD)
    d.arc([cx - 34 * s, cy - 26 * s, cx - 14 * s, cy - 2 * s], 90, 270,
          fill=GOLD, width=4)
    d.arc([cx + 14 * s, cy - 26 * s, cx + 34 * s, cy - 2 * s], -90, 90,
          fill=GOLD, width=4)
    d.rectangle([cx - 3 * s, cy + 2 * s, cx + 3 * s, cy + 18 * s], fill=GOLD)
    d.rectangle([cx - 16 * s, cy + 18 * s, cx + 16 * s, cy + 26 * s],
                fill=(146, 100, 10))
    d.ellipse([cx + 16 * s, cy + 8 * s, cx + 40 * s, cy + 32 * s],
              fill=(168, 200, 60), outline=(90, 120, 20), width=2)
    d.arc([cx + 16 * s, cy + 8 * s, cx + 40 * s, cy + 32 * s], 200, 340,
          fill=(255, 255, 255), width=2)


ICONS = {
    "burst": lambda d, cx, cy: draw_burst(d, cx, cy, 34),
    "ship": lambda d, cx, cy: draw_ship(d, cx, cy, 0.85),
    "coin": lambda d, cx, cy: draw_coin(d, cx, cy, 32),
    "plane": lambda d, cx, cy: draw_plane(d, cx, cy, 0.85),
    "flame": lambda d, cx, cy: draw_flame(d, cx, cy, 0.85),
    "trophy": lambda d, cx, cy: draw_trophy(d, cx, cy, 0.85),
}

CARDS = [
    ("UKRAINE", "Russian strike kills 11 in Dymer",
     "Apartment block hit near Kyiv; rescuers pull bodies from rubble.", "burst"),
    ("LIBYA", "Ukraine sinks Russian warship",
     "Sea drones strike the corvette Merkury at Benghazi naval base.", "ship"),
    ("UNITED STATES", "Trump signs law to end the penny",
     "Common Cents Act closes the coin's 232-year run.", "coin"),
    ("UNITED STATES", "Delta outage delays 1,600 flights",
     "Thanksgiving travel snarled by weight-and-balance failure.", "plane"),
    ("INDONESIA", "Factory fire kills 24",
     "Candy plant blaze; dozens still missing.", "flame"),
    ("SPORT", "Alcaraz wins first ATP Finals",
     "Beats Zverev in straight sets to take the title.", "trophy"),
]

FOOTER = ("ALSO: NATO meets on Russian missiles in Poland \u2022 "
          "'Trump Route' breaks ground in Armenia \u2022 "
          "COP31 climate talks collapse")


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)

    # Masthead
    f_mast = font(SERIF_B, 62)
    d.text((W // 2, 78), "THE WORLD IN ONE DAY", font=f_mast, fill=INK,
           anchor="mm")
    f_date = font(SANS_B, 44)
    d.text((W // 2, 142), "MONDAY 23 NOVEMBER 2026", font=f_date, fill=RED,
           anchor="mm")
    d.rectangle([40, 178, W - 40, 184], fill=RED)
    d.rectangle([40, 190, W - 40, 192], fill=INK)

    # Grid 2 x 3
    gx, gy = 40, 206
    cw = (W - 2 * gx - 24) // 2
    ch = 232
    gap = 24
    f_tag = font(SANS_B, 17)
    f_head = font(SANS_B, 27)
    f_sub = font(SANS, 19)

    for i, (tag, head, sub, icon) in enumerate(CARDS):
        x = gx + (i % 2) * (cw + gap)
        y = gy + (i // 2) * (ch + 16)
        d.rectangle([x, y, x + cw, y + ch], fill=CARD_BG, outline=CARD_LINE,
                    width=2)
        d.rectangle([x, y, x + cw, y + 5], fill=RED)
        # tag top-left, icon top-right in the tag row
        d.text((x + 16, y + 18), tag, font=f_tag, fill=BLUE, anchor="la")
        ICONS[icon](d, x + cw - 52, y + 46)
        # headline below the tag/icon row, full card width, max 2 lines
        lines = wrap(d, head, f_head, cw - 32)
        hy = y + 88
        for ln in lines[:2]:
            d.text((x + 16, hy), ln, font=f_head, fill=INK, anchor="la")
            hy += 34
        # sub-text, wrapped to 2 lines
        slines = wrap(d, sub, f_sub, cw - 32)
        sy = y + 88 + 2 * 34 + 10
        for ln in slines[:2]:
            d.text((x + 16, sy), ln, font=f_sub, fill=(60, 60, 60),
                   anchor="la")
            sy += 25

    # Footer: one line, shrink font until it fits
    f_foot = font(SANS, 18)
    while d.textlength(FOOTER, font=f_foot) > W - 80 and f_foot.size > 12:
        f_foot = font(SANS, f_foot.size - 1)
    d.text((W // 2, 962), FOOTER, font=f_foot, fill=INK, anchor="mm")

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
