#!/usr/bin/env python3
"""Render Wednesday 25 November 2026's world news as one 1024x1024 image.

Reads news.json next to this script and writes /output/entry.png
(and entry.png beside itself when run locally). Deterministic: fixed
geometry, fixed fonts, no clock, no randomness, no network.

Editorial concept — THE DAY, COUNTED: the day as a ledger /
balance-sheet broadsheet. Six ledger entries built around big
numerals (3 large leads + 10 small illustrated cards), a numbers
band, an exact-time UTC strip, a locator map with 13 numbered pins,
a compact register grouped by region, and a red-bordered DATE CHECK.
This is a fresh concept: 23 Nov was map-first (Atlas), 24 Nov was
wire-feed timeline-first. Flat PIL vector scenes illustrate all 13
featured stories; no external images.

The 40 stories and every fact are the verified ones in news.json /
verification.md (53-story deduped pool, 10 genuinely independent
ranking passes). Labels use only OFFICIAL / REPORTED / CLAIM
(pool CONFIRMED maps to REPORTED).
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.environ.get("MAKEFUN_OUTPUT_PATH") or "/output/entry.png"

W, H = 1024, 1024
MARGIN = 28
CW = W - 2 * MARGIN  # 968 content width

PAPER = (247, 244, 236)      # ledger paper
INK = (24, 28, 34)
MUTED = (96, 104, 112)
RED = (176, 38, 28)
DARKRED = (140, 28, 20)
TEAL = (13, 110, 110)
BLUE = (30, 80, 140)
AMBER = (178, 112, 16)
RULE = (24, 28, 34)
CARD = (255, 255, 255)
CARD_LINE = (205, 210, 214)
TILE = (232, 230, 222)
SEA = (214, 226, 232)
LAND = (176, 188, 196)
LAND_LINE = (140, 156, 168)
PANEL_DARK = (28, 38, 52)
GREEN = (34, 110, 60)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LABEL_COLOR = {"REPORTED": TEAL, "OFFICIAL": BLUE, "CLAIM": AMBER}

# --- simplified continent outlines in (lon, lat) ---
NORTH_AMERICA = [(-168, 66), (-150, 70), (-130, 71), (-110, 72), (-95, 72),
                 (-85, 70), (-80, 73), (-70, 62), (-60, 55), (-55, 47),
                 (-65, 44), (-70, 41), (-75, 35), (-80, 32), (-84, 30),
                 (-90, 21), (-87, 13), (-83, 9), (-79, 8), (-86, 12),
                 (-92, 15), (-97, 20), (-105, 23), (-114, 29), (-120, 34),
                 (-124, 42), (-124, 48), (-130, 54), (-140, 60),
                 (-155, 58), (-165, 60)]
GREENLAND = [(-45, 60), (-35, 66), (-25, 70), (-20, 74), (-30, 80),
             (-45, 80), (-55, 76), (-58, 70), (-52, 64)]
SOUTH_AMERICA = [(-79, 9), (-77, 4), (-80, -3), (-79, -9), (-75, -15),
                 (-70, -20), (-70, -30), (-72, -38), (-73, -48),
                 (-68, -54), (-65, -45), (-60, -35), (-52, -32),
                 (-44, -23), (-39, -15), (-35, -8), (-38, -4), (-45, -2),
                 (-50, 0), (-54, 5), (-60, 8), (-68, 11), (-75, 10)]
AFRICA = [(-6, 35), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28),
          (40, 18), (43, 12), (48, 11), (51, 10), (45, 2), (41, -5),
          (39, -13), (35, -20), (32, -28), (27, -34), (20, -35),
          (15, -28), (12, -18), (9, -1), (9, 4), (-8, 5), (-13, 8),
          (-17, 15), (-17, 22), (-15, 28), (-10, 31)]
EUROPE = [(-10, 36), (-9, 43), (-2, 48), (-4, 50), (2, 51), (5, 53),
          (8, 57), (10, 59), (18, 56), (21, 55), (24, 59), (28, 60),
          (30, 62), (30, 66), (35, 66), (40, 68), (42, 66), (45, 60),
          (40, 55), (35, 50), (30, 46), (28, 44), (23, 40), (19, 42),
          (15, 44), (12, 44), (8, 44), (3, 43), (0, 40), (-2, 37),
          (-6, 36), (-9, 38)]
ASIA = [(30, 62), (40, 68), (55, 68), (68, 73), (80, 73), (95, 76),
        (110, 76), (125, 72), (140, 72), (155, 70), (165, 69), (175, 66),
        (178, 64), (170, 60), (162, 56), (158, 52), (150, 59), (142, 54),
        (140, 45), (135, 42), (130, 40), (127, 38), (122, 37), (120, 32),
        (115, 28), (110, 21), (108, 18), (105, 10), (100, 8), (97, 12),
        (94, 17), (91, 22), (88, 22), (85, 19), (80, 13), (77, 8),
        (75, 12), (72, 20), (68, 23), (62, 25), (57, 26), (54, 27),
        (50, 29), (48, 30), (44, 29), (40, 32), (36, 36), (33, 36),
        (30, 36), (28, 40), (30, 44), (32, 48), (35, 52), (38, 58),
        (36, 62), (32, 64)]
AUSTRALIA = [(114, -22), (114, -30), (115, -35), (120, -34), (125, -33),
             (130, -32), (135, -35), (138, -35), (140, -38), (145, -38),
             (150, -37), (153, -32), (153, -27), (150, -23), (146, -19),
             (142, -15), (142, -11), (137, -12), (135, -15), (132, -12),
             (130, -13), (126, -14), (122, -17), (118, -20)]
NEW_ZEALAND = [(167, -45), (170, -43), (174, -41), (177, -38), (175, -37),
               (173, -35), (172, -41), (168, -44)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51),
      (-2, 50)]
CONTINENTS = [NORTH_AMERICA, GREENLAND, SOUTH_AMERICA, AFRICA, EUROPE,
              ASIA, AUSTRALIA, NEW_ZEALAND, UK]

REGION_COLOR = {"Europe": (176, 38, 28), "Middle East": (178, 112, 16),
                "Africa": (34, 110, 60), "East Asia": (30, 80, 140),
                "Southeast Asia": (13, 110, 110), "South Asia": (120, 60, 140),
                "North America": (90, 60, 30), "Latin America": (200, 90, 40),
                "Oceania": (20, 120, 140), "Global / Space": (80, 80, 90)}


def main():
    with open(os.path.join(HERE, "news.json"), encoding="utf-8") as f:
        data = json.load(f)

    def font(path, size):
        return ImageFont.truetype(path, size)

    F = {
        "kicker": font(SANS_BOLD, 10),
        "title": font(SERIF_BOLD, 34),
        "spec": font(SANS_BOLD, 10),
        "subhead": font(SERIF_ITALIC, 13),
        "legend": font(SANS, 9),
        "chip": font(SANS_BOLD, 9),
        "tl_head": font(SANS_BOLD, 9),
        "tl_time": font(SANS_BOLD, 10),
        "tl_event": font(SANS, 9),
        "tag": font(SANS_BOLD, 9),
        "src": font(SANS, 8),
        "lead_h": font(SERIF_BOLD, 15),
        "lead_s": font(SANS, 10),
        "feat_h": font(SERIF_BOLD, 10),
        "feat_s": font(SANS, 8),
        "num_v": font(SERIF_BOLD, 18),
        "num_l": font(SANS, 8),
        "map_t": font(SANS_BOLD, 9),
        "reg_h": font(SANS_BOLD, 9),
        "reg_i": font(SANS, 9),
        "dc_t": font(SANS_BOLD, 11),
        "dc": font(SANS, 11),
        "foot": font(SANS, 8),
        "pin": font(SANS_BOLD, 9),
        "numchip": font(SANS_BOLD, 10),
    }

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    def text_w(s, f):
        return d.textbbox((0, 0), s, font=f)[2]

    def wrap(s, f, width):
        words = s.split()
        lines, cur = [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if text_w(t, f) <= width:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w_
        if cur:
            lines.append(cur)
        return lines

    def draw_wrapped(d, x, y, s, f, width, fill, spacing=2, max_lines=None):
        lines = wrap(s, f, width)
        if max_lines is not None and len(lines) > max_lines:
            lines = lines[:max_lines]
            # ellipsize the last line to fit
            while lines and text_w(lines[-1] + "…", f) > width:
                lines[-1] = lines[-1][:-1]
            if lines:
                lines[-1] += "…"
        for line in lines:
            d.text((x, y), line, font=f, fill=fill)
            y += f.size + spacing
        return y

    y = 8
    # ---------- masthead ----------
    d.text((MARGIN, y), data["kicker"], font=F["kicker"], fill=RED)
    y += 14
    d.text((MARGIN, y), data["title"], font=F["title"], fill=INK)
    y += 38
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=2)
    y += 5
    d.text((MARGIN, y), data["spec"], font=F["spec"], fill=INK)
    y += 14
    d.text((MARGIN, y), data["subhead"], font=F["subhead"], fill=RED)
    y += 17
    d.text((MARGIN, y), data["legend"], font=F["legend"], fill=MUTED)
    y += 13
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RULE, width=1)
    y += 5

    # ---------- region chips row (first content row) ----------
    chip_h = 22
    cx = MARGIN
    for name, n in data["regions"]:
        label = "%s %d" % (name, n)
        wch = text_w(label, F["chip"]) + 16
        col = REGION_COLOR[name.title().replace(" / ", " / ")] if name != "GLOBAL / SPACE" else REGION_COLOR["Global / Space"]
        d.rectangle([cx, y, cx + wch, y + chip_h], outline=col, width=1)
        d.rectangle([cx, y, cx + wch, y + chip_h], fill=col)
        d.text((cx + 8, y + 6), label, font=F["chip"], fill=(255, 255, 255))
        cx += wch + 6
    y += chip_h + 5

    # ---------- numbers band ----------
    num_h = 40
    d.rectangle([MARGIN, y, W - MARGIN, y + num_h], fill=TILE)
    cell_w = CW // 6
    for i, n in enumerate(data["numbers"]):
        x = MARGIN + i * cell_w
        if i:
            d.line([(x, y + 7), (x, y + num_h - 7)], fill=CARD_LINE)
        vx = x + 9
        d.text((vx, y + 4), n["value"], font=F["num_v"], fill=INK)
        draw_wrapped(d, vx, y + 24, n["label"], F["num_l"], cell_w - 16,
                     MUTED, spacing=0, max_lines=2)
    y += num_h + 5

    # ---------- 3 large ledger leads ----------
    lead_h = 176
    col_w = 312
    gap = (CW - 3 * col_w) // 2
    cols = [MARGIN + i * (col_w + gap) for i in range(3)]
    for cx, story in zip(cols, data["featured"][:3]):
        draw_lead(d, F, cx, y, col_w, lead_h, story, wrap, text_w,
                  draw_wrapped)
    y += lead_h + 5

    # ---------- 10 small illustrated cards (5 x 2) ----------
    card_w = (CW - 4 * 8) // 5
    card_h = 90
    for row in range(2):
        for col in range(5):
            story = data["featured"][3 + row * 5 + col]
            cx = MARGIN + col * (card_w + 8)
            cy = y + row * (card_h + 5)
            draw_card(d, F, cx, cy, card_w, card_h, story, wrap, text_w,
                      draw_wrapped)
    y += 2 * card_h + 5 + 5

    # ---------- UTC timeline strip (6 exact markers) ----------
    tl_h = 42
    d.text((MARGIN, y), "THE DAY IN UTC — FIRST REPORTS", font=F["tl_head"],
           fill=MUTED)
    tl_y = y + 26
    d.line([(MARGIN, tl_y), (W - MARGIN, tl_y)], fill=RULE, width=1)
    for i, m in enumerate(data["timeline"]):
        hh, mm = m["time"].split(":")
        frac = (int(hh) + int(mm) / 60.0) / 24.0
        x = MARGIN + frac * CW
        d.ellipse([x - 4, tl_y - 4, x + 4, tl_y + 4], fill=RED)
        tw = text_w(m["time"], F["tl_time"])
        tx = max(MARGIN, min(W - MARGIN - tw, x - tw / 2))
        d.text((tx, y + 12), m["time"], font=F["tl_time"], fill=RED)
        if abs(tx + tw / 2 - x) > 1:
            d.line([(x, tl_y - 5), (tx + tw / 2, y + 23)], fill=RED, width=1)
        ew = text_w(m["label"], F["tl_event"])
        ex = max(MARGIN, min(W - MARGIN - ew, x - ew / 2))
        d.text((ex, tl_y + 6), m["label"], font=F["tl_event"], fill=INK)
    y += tl_h + 5

    # ---------- locator map (13 numbered pins) ----------
    map_h = 100
    d.rectangle([MARGIN, y, W - MARGIN, y + map_h], fill=CARD,
                outline=CARD_LINE)
    d.text((MARGIN + 10, y + 6), "WHERE IT HAPPENED — 13 ILLUSTRATED STORIES",
           font=F["map_t"], fill=INK)
    mx, my = MARGIN + 8, y + 20
    mw, mh = CW - 16, map_h - 28
    d.rectangle([mx, my, mx + mw, my + mh], fill=SEA)
    for gx in range(1, 6):
        lx = mx + gx * mw / 6
        d.line([(lx, my), (lx, my + mh)], fill=(205, 214, 220))
    for gy in range(1, 3):
        ly = my + gy * mh / 3
        d.line([(mx, ly), (mx + mw, ly)], fill=(205, 214, 220))
    for poly in CONTINENTS:
        pts = []
        for lon, lat in poly:
            px = mx + (lon + 180) / 360.0 * mw
            py = my + (78 - lat) / 136.0 * mh
            pts.append((px, py))
        d.polygon(pts, fill=LAND, outline=LAND_LINE)
    # pin offsets separate the three collisions: Washington x2,
    # Cairo/Gaza, Bruges/Brussels
    offsets = {1: (0, 0), 2: (0, 0), 3: (-15, -5), 4: (0, 0), 5: (15, 6),
               6: (-16, 7), 7: (0, 0), 8: (14, -7), 9: (0, 0), 10: (0, 0),
               11: (-15, -8), 12: (0, 0), 13: (15, 7)}
    for story in data["featured"]:
        bx = mx + (story["lon"] + 180) / 360.0 * mw
        by = my + (78 - story["lat"]) / 136.0 * mh
        ox, oy = offsets[story["num"]]
        px, py = bx + ox, by + oy
        if ox or oy:
            d.line([(bx, by), (px, py)], fill=RED, width=1)
            d.ellipse([bx - 2, by - 2, bx + 2, by + 2], fill=RED)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        nw = text_w(str(story["num"]), F["pin"])
        d.text((px - nw / 2, py - 6), str(story["num"]), font=F["pin"],
               fill=(255, 255, 255))
    y += map_h + 5

    # ---------- DATE CHECK (red-bordered, legible) ----------
    dc_lines = wrap(data["datecheck"], F["dc"], CW - 20)
    dc_h = 8 + 17 + len(dc_lines) * 14 + 8
    d.rectangle([MARGIN, y, W - MARGIN, y + dc_h],
                fill=(253, 240, 238), outline=RED, width=2)
    d.text((MARGIN + 10, y + 8), "DATE CHECK", font=F["dc_t"], fill=RED)
    yy = y + 25
    for line in dc_lines:
        d.text((MARGIN + 10, yy), line, font=F["dc"], fill=INK)
        yy += 14
    y += dc_h + 5

    # ---------- compact register, grouped by region ----------
    # Compute the total line count BEFORE setting the band height.
    groups = [("EUROPE", "Europe"), ("MIDDLE EAST", "Middle East"),
              ("AFRICA", "Africa"), ("EAST ASIA", "East Asia"),
              ("SOUTHEAST ASIA", "Southeast Asia"),
              ("SOUTH ASIA", "South Asia"),
              ("NORTH AMERICA", "North America"),
              ("LATIN AMERICA", "Latin America"), ("OCEANIA", "Oceania"),
              ("GLOBAL / SPACE", "Global / Space")]
    by_region = {}
    for s in data["secondary"]:
        by_region.setdefault(s["region"], []).append(s)
    col_groups = [groups[0:3], groups[3:6], groups[6:10]]
    col_px = []
    for gl in col_groups:
        px = 0
        for gname, key in gl:
            items = by_region.get(key, [])
            if items:
                px += 11 + len(items) * 10 + 1  # header + items + gap
        col_px.append(px - 1 if px else 0)
    max_col_px = max(col_px)
    reg_h = 15 + max_col_px + 4 + 12  # title + columns + gap + flags line
    print("register columns px:", col_px, "band height:", reg_h)
    d.text((MARGIN, y), "THE REST OF THE DAY — STORIES 14–40, BY REGION",
           font=F["map_t"], fill=INK)
    col_w = CW // 3
    for ci, gl in enumerate(col_groups):
        cx = MARGIN + ci * col_w
        cy = y + 15
        for gname, key in gl:
            items = by_region.get(key, [])
            if not items:
                continue
            d.text((cx, cy), gname, font=F["reg_h"],
                   fill=REGION_COLOR[key])
            cy += 11
            for s in items:
                d.text((cx, cy), "%d." % s["num"], font=F["reg_i"], fill=RED)
                d.text((cx + 20, cy), s["headline"], font=F["reg_i"],
                       fill=INK)
                cy += 10
            cy += 1
    d.text((MARGIN, y + reg_h - 12), data["flags_note"], font=F["foot"],
           fill=MUTED)
    assert text_w(data["flags_note"], F["foot"]) <= CW, "flags note overflows"
    y += reg_h + 5

    # ---------- footer: every cited source, expanded ----------
    fy = draw_wrapped(d, MARGIN, y, data["sources"], F["foot"], CW, MUTED,
                      spacing=2)
    print("final y:", fy, "page height:", H)

    local = os.path.join(HERE, "entry.png")
    img.save(local, "PNG", optimize=True)
    os.chmod(local, 0o644)
    if OUTPUT != local:
        try:
            os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
            img.save(OUTPUT, "PNG", optimize=True)
            os.chmod(OUTPUT, 0o644)
            print("wrote", OUTPUT, os.path.getsize(OUTPUT), "bytes")
        except OSError as e:
            print("could not write", OUTPUT, e)
    print("wrote", local, os.path.getsize(local), "bytes")
    return 0


def draw_scene(d, F, x, y, w, h, kind):
    """Render the scene at a fixed reference size, then scale to fit,
    so the same scene works in a 72px lead panel and a 30px card strip."""
    from PIL import Image
    tmp = Image.new("RGB", (300, 72), PAPER)
    td = ImageDraw.Draw(tmp)
    _scene(td, F, 0, 0, 300, 72, kind)
    tmp = tmp.resize((max(1, int(w)), max(1, int(h))), Image.LANCZOS)
    d._image.paste(tmp, (int(x), int(y)))


def _scene(d, F, x, y, w, h, kind):
    """Flat vector-style scene for one featured story."""
    if kind == "toll":
        d.rectangle([x, y, x + w, y + h], fill=(52, 44, 50))
        d.rectangle([x, y, x + w, y + 14], fill=(176, 38, 28))
        for i in range(9):
            cx = x + 18 + (i % 5) * 56
            cy = y + 30 + (i // 5) * 26
            d.rectangle([cx - 2, cy, cx + 2, cy + 18], fill=(230, 225, 215))
            d.rectangle([cx - 7, cy + 4, cx + 7, cy + 8], fill=(230, 225, 215))
        d.rectangle([x, y + h - 8, x + w, y + h], fill=(30, 26, 30))
    elif kind == "kospi":
        d.rectangle([x, y, x + w, y + h], fill=(250, 240, 235))
        for gx in range(5):
            d.line([(x + 10 + gx * 60, y + 8), (x + 10 + gx * 60, y + h - 8)],
                   fill=(230, 220, 215))
        pts = [(x + 8, y + 12), (x + 60, y + 22), (x + 110, y + 18),
               (x + 160, y + 38), (x + 210, y + 34), (x + 260, y + 58),
               (x + w - 8, y + h - 10)]
        d.line(pts, fill=RED, width=3)
        for px, py in pts[1:-1]:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
        d.polygon([(x + w - 26, y + h - 26), (x + w - 8, y + h - 26),
                   (x + w - 8, y + h - 8)], fill=RED)
    elif kind == "tariffs":
        d.rectangle([x, y, x + w, y + h], fill=(30, 80, 140))
        d.rectangle([x + 14, y + h - 30, x + w - 14, y + h - 14],
                    fill=(24, 28, 34))
        for i, c in enumerate([(176, 38, 28), (240, 200, 90), (13, 110, 110),
                               (176, 38, 28)]):
            d.rectangle([x + 22 + i * 62, y + h - 52, x + 76 + i * 62,
                         y + h - 32], fill=c)
        d.ellipse([x + w - 52, y + 8, x + w - 8, y + 44], fill=(255, 255, 255))
        d.text((x + w - 42, y + 14), "%", font=F["numchip"],
               fill=RED)
    elif kind == "shenzhou":
        d.rectangle([x, y, x + w, y + h], fill=(16, 22, 40))
        for sx, sy in [(16, 10), (48, 18), (90, 8), (150, 14), (210, 10),
                       (250, 20), (285, 12), (120, 26)]:
            d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1],
                      fill=(230, 230, 210))
        cx = x + w // 2
        d.polygon([(cx, y + 6), (cx - 10, y + 26), (cx + 10, y + 26)],
                  fill=RED)
        d.rectangle([cx - 10, y + 26, cx + 10, y + 56], fill=(240, 240, 235))
        d.polygon([(cx - 10, y + 56), (cx - 20, y + 66), (cx - 10, y + 60)],
                  fill=(200, 120, 60))
        d.polygon([(cx + 10, y + 56), (cx + 20, y + 66), (cx + 10, y + 60)],
                  fill=(200, 120, 60))
        d.polygon([(cx - 5, y + 56), (cx + 5, y + 56), (cx, y + 74)],
                  fill=(245, 180, 60))
        d.ellipse([x + w - 60, y + h - 22, x + w - 6, y + h + 22],
                  fill=(120, 110, 100))
    elif kind == "pce":
        d.rectangle([x, y, x + w, y + h], fill=(232, 238, 232))
        base = y + h - 8
        vals = [18, 26, 22, 34, 30, 44]
        for i, v in enumerate(vals):
            bx = x + 16 + i * 44
            d.rectangle([bx, base - v, bx + 28, base], fill=TEAL)
        d.rectangle([x + w - 46, y + 6, x + w - 10, y + 30], fill=INK)
        d.text((x + w - 38, y + 9), "$", font=F["numchip"],
               fill=(255, 255, 255))
    elif kind == "cairo":
        d.rectangle([x, y, x + w, y + h], fill=(40, 36, 34))
        for fx, fh in [(30, 26), (52, 36), (76, 24), (100, 30)]:
            d.polygon([(x + fx, y + h - 34), (x + fx + 8, y + h - 34 - fh),
                       (x + fx + 16, y + h - 34)], fill=(245, 140, 40))
        d.rectangle([x + 20, y + h - 34, x + 120, y + h - 20],
                    fill=(200, 200, 195))
        d.ellipse([x + 34, y + h - 18, x + 48, y + h - 4], fill=INK)
        d.ellipse([x + 96, y + h - 18, x + 110, y + h - 4], fill=INK)
        d.rectangle([x + 120, y + h - 30, x + 138, y + h - 20],
                    fill=(200, 200, 195))
    elif kind == "poland":
        d.rectangle([x, y, x + w, y + h], fill=(214, 226, 232))
        cx, cy = x + w // 2, y + h // 2
        d.polygon([(cx - 34, cy), (cx + 30, cy - 8), (cx + 40, cy),
                   (cx + 30, cy + 8)], fill=(24, 28, 34))
        d.polygon([(cx - 6, cy - 4), (cx + 2, cy - 18), (cx + 8, cy - 4)],
                  fill=(24, 28, 34))
        d.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], outline=RED, width=4)
        d.line([(cx - 28, cy + 28), (cx + 28, cy - 28)], fill=RED, width=4)
    elif kind == "gaza":
        d.rectangle([x, y, x + w, y + h], fill=(232, 214, 190))
        base = y + h
        for bx, bw, bh in [(10, 40, 40), (56, 34, 58), (96, 44, 34),
                           (146, 36, 50)]:
            d.rectangle([x + bx, base - bh, x + bx + bw, base],
                        fill=(90, 80, 72))
        for sx, sy, r in [(120, 16, 8), (132, 26, 11), (146, 36, 9)]:
            d.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r],
                      fill=(120, 120, 118))
    elif kind == "hodeidah":
        d.rectangle([x, y, x + w, y + h], fill=(214, 226, 232))
        d.rectangle([x, y + h - 16, x + w, y + h], fill=(30, 80, 140))
        for cx in [50, 130, 210]:
            d.line([(x + cx, y + 10), (x + cx, y + h - 16)], fill=INK, width=3)
            d.line([(x + cx, y + 10), (x + cx + 34, y + 22)], fill=INK, width=2)
        d.rectangle([x + 18, y + h - 34, x + 54, y + h - 18], fill=RED)
        d.rectangle([x + 60, y + h - 34, x + 96, y + h - 18],
                    fill=(240, 200, 90))
        d.rectangle([x + 200, y + h - 36, x + 260, y + h - 16],
                    fill=(240, 240, 235))
    elif kind == "cartagena":
        d.rectangle([x, y, x + w, y + h], fill=(240, 232, 220))
        d.rectangle([x + 14, y + 14, x + w - 14, y + 34], fill=RED)
        for i in range(5):
            d.polygon([(x + 14 + i * 26, y + 34), (x + 27 + i * 26, y + 34),
                       (x + 20 + i * 26, y + 44)], fill=(255, 255, 255))
        d.rectangle([x + 30, y + 46, x + w - 30, y + h - 8], fill=(90, 80, 72))
        d.rectangle([x + w // 2 - 14, y + 52, x + w // 2 + 14, y + h - 8],
                    fill=(240, 200, 90))
        d.ellipse([x + w - 40, y + 6, x + w - 12, y + 30], fill=GREEN)
        d.text((x + w - 34, y + 9), "✓", font=F["numchip"],
               fill=(255, 255, 255))
    elif kind == "liverpool":
        d.rectangle([x, y, x + w, y + h], fill=(34, 110, 60))
        d.line([(x, y + h // 2), (x + w, y + h // 2)], fill=(255, 255, 255),
               width=2)
        d.ellipse([x + w // 2 - 16, y + h // 2 - 16, x + w // 2 + 16,
                   y + h // 2 + 16], outline=(255, 255, 255), width=2)
        d.rectangle([x + 10, y + 10, x + 44, y + 34], outline=(255, 255, 255),
                    width=2)
        d.ellipse([x + w - 44, y + h - 34, x + w - 18, y + h - 8],
                  fill=(255, 255, 255), outline=INK)
        d.polygon([(x + w - 38, y + h - 30), (x + w - 30, y + h - 22),
                   (x + w - 24, y + h - 30)], fill=INK)
    elif kind == "solomon":
        d.rectangle([x, y, x + w, y + h], fill=(232, 238, 232))
        d.rectangle([x + w // 2 - 34, y + 10, x + w // 2 + 34, y + h - 10],
                    fill=(255, 255, 255), outline=INK)
        d.line([(x + w // 2 - 24, y + 22), (x + w // 2 + 24, y + 22)],
               fill=INK, width=2)
        d.line([(x + w // 2 - 24, y + 32), (x + w // 2 + 24, y + 32)],
               fill=(150, 150, 150), width=1)
        d.line([(x + w // 2 - 24, y + 40), (x + w // 2 + 12, y + 40)],
               fill=(150, 150, 150), width=1)
        d.ellipse([x + w // 2 - 8, y + h - 26, x + w // 2 + 8, y + h - 14],
                  fill=RED)
        for fx in [14, w - 30]:
            d.line([(x + fx, y + 8), (x + fx, y + h - 8)], fill=INK, width=2)
            d.rectangle([x + fx, y + 8, x + fx + 18, y + 22], fill=TEAL)
    elif kind == "quantum":
        d.rectangle([x, y, x + w, y + h], fill=(24, 28, 52))
        cx, cy = x + w // 2, y + h // 2
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(245, 180, 60))
        for rx, ry in [(34, 12), (34, 12), (12, 34)]:
            d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry],
                      outline=(120, 180, 220), width=2)
        for ex, ey in [(cx + 34, cy), (cx - 26, cy - 8), (cx + 8, cy + 30)]:
            d.ellipse([ex - 3, ey - 3, ex + 3, ey + 3], fill=(240, 200, 90))
    else:
        d.rectangle([x, y, x + w, y + h], fill=TILE)


def draw_lead(d, F, x, y, w, h, story, wrap, text_w, draw_wrapped):
    """One large ledger entry: scene + number chip + tag/source + text."""
    ph = 72
    draw_scene(d, F, x, y, w, ph, story["scene"])
    # number badge + big-number chip on the scene
    d.rectangle([x, y, x + 20, y + 20], fill=RED)
    nw = text_w(str(story["num"]), F["pin"])
    d.text((x + 10 - nw / 2, y + 4), str(story["num"]), font=F["pin"],
           fill=(255, 255, 255))
    chw = text_w(story["chip"], F["numchip"]) + 16
    d.rectangle([x + w - chw, y + ph - 22, x + w, y + ph], fill=INK)
    d.text((x + w - chw + 8, y + ph - 19), story["chip"], font=F["numchip"],
           fill=(255, 255, 255))
    ty = y + ph + 6
    tag = story["label"]
    col = LABEL_COLOR[tag]
    d.rectangle([x, ty, x + text_w(tag, F["tag"]) + 12, ty + 15], fill=col)
    d.text((x + 6, ty + 3), tag, font=F["tag"], fill=(255, 255, 255))
    sx = x + text_w(tag, F["tag"]) + 20
    d.text((sx, ty + 3), story["source"], font=F["src"], fill=MUTED)
    hy = ty + 20
    hy = draw_wrapped(d, x, hy, story["headline"], F["lead_h"], w, INK,
                      spacing=1, max_lines=3)
    draw_wrapped(d, x, hy + 2, story["summary"], F["lead_s"], w, (60, 68, 78),
                 spacing=1, max_lines=3)


def draw_card(d, F, x, y, w, h, story, wrap, text_w, draw_wrapped):
    """Small illustrated card: scene + chips + headline + summary + source."""
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=CARD_LINE)
    ph = 30
    draw_scene(d, F, x + 1, y + 1, w - 2, ph, story["scene"])
    # number badge top-left of the scene
    d.rectangle([x + 1, y + 1, x + 17, y + 15], fill=RED)
    nw = text_w(str(story["num"]), F["pin"])
    d.text((x + 9 - nw / 2, y + 3), str(story["num"]), font=F["pin"],
           fill=(255, 255, 255))
    # big-number chip bottom-right of the scene
    chw = text_w(story["chip"], F["chip"]) + 12
    d.rectangle([x + w - chw - 1, y + ph - 13, x + w - 1, y + ph + 1],
                fill=INK)
    d.text((x + w - chw + 5, y + ph - 12), story["chip"], font=F["chip"],
           fill=(255, 255, 255))
    ty = y + ph + 4
    tag = story["label"]
    col = LABEL_COLOR[tag]
    d.rectangle([x + 5, ty, x + 5 + text_w(tag, F["tag"]) + 10, ty + 13],
                fill=col)
    d.text((x + 11, ty + 2), tag, font=F["tag"], fill=(255, 255, 255))
    sx = x + 5 + text_w(tag, F["tag"]) + 16
    d.text((sx, ty + 2), story["source"], font=F["src"], fill=MUTED)
    hy = ty + 16
    hy = draw_wrapped(d, x + 5, hy, story["headline"], F["feat_h"], w - 10,
                      INK, spacing=0, max_lines=2)
    draw_wrapped(d, x + 5, hy + 1, story["summary"], F["feat_s"], w - 10,
                 (60, 68, 78), spacing=0, max_lines=2)


if __name__ == "__main__":
    sys.exit(main())
