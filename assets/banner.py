"""Generates assets/banner.svg: a brick house that breaks into its parts and rebuilds as a rocket.

Run: python3 assets/banner.py
"""
import random
from pathlib import Path

W, H = 1280, 420
UNIT, GAP = 26, 4
PITCH = UNIT + GAP
LOOP = 9  # seconds

# The article's own picture: a Lego house taken apart and rebuilt as something else.
HOUSE = """
....#....
...###...
..#####..
.#######.
..#####..
..##.##..
..##.##..
"""
ROCKET = """
....#....
...###...
...###...
...#.#...
...###...
...###...
..#####..
.##.#.##.
.#..#..#.
....#....
"""
PALETTE = ["#FFB547", "#FF6B35", "#FF2E88", "#B44CFF", "#7B5CFF", "#22D3EE"]
CENTER = (1012, 214)


def cells(art):
    rows = [r for r in art.strip("\n").splitlines()]
    pts = [(c, r) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "#"]
    cx = (len(rows[0]) * PITCH - GAP) / 2
    cy = (len(rows) * PITCH - GAP) / 2
    return [(CENTER[0] - cx + c * PITCH, CENTER[1] - cy + r * PITCH) for c, r in pts]


def lerp_color(t):
    t = max(0.0, min(1.0, t)) * (len(PALETTE) - 1)
    i = min(int(t), len(PALETTE) - 2)
    f = t - i
    a, b = PALETTE[i], PALETTE[i + 1]
    ch = lambda h, k: int(h[1 + 2 * k: 3 + 2 * k], 16)
    return "#" + "".join(f"{round(ch(a, k) + (ch(b, k) - ch(a, k)) * f):02X}" for k in range(3))


def build():
    rng = random.Random(7)
    house, rocket = cells(HOUSE), cells(ROCKET)
    n = max(len(house), len(rocket))
    # Sort both shapes top-to-bottom so each brick travels a short, readable path.
    house.sort(key=lambda p: (p[1], p[0]))
    rocket.sort(key=lambda p: (p[1], p[0]))

    css, bricks = [], []
    for i in range(n):
        a = house[i] if i < len(house) else None
        b = rocket[i] if i < len(rocket) else None
        s1 = (rng.uniform(750, 1220), rng.uniform(40, 330), rng.uniform(-140, 140))
        s2 = (rng.uniform(750, 1220), rng.uniform(40, 330), rng.uniform(-140, 140))
        def frame(p, scatter, rot=0):
            if p:
                return f"transform:translate({p[0]:.1f}px,{p[1]:.1f}px) rotate({rot}deg);opacity:1"
            return f"transform:translate({scatter[0]:.1f}px,{scatter[1]:.1f}px) rotate({scatter[2]:.0f}deg);opacity:0"
        sc1 = f"transform:translate({s1[0]:.1f}px,{s1[1]:.1f}px) rotate({s1[2]:.0f}deg);opacity:.9"
        sc2 = f"transform:translate({s2[0]:.1f}px,{s2[1]:.1f}px) rotate({s2[2]:.0f}deg);opacity:.9"
        css.append(
            f"@keyframes b{i}{{0%,16%{{{frame(a, s1)}}}30%,38%{{{sc1}}}54%,80%{{{frame(b, s2)}}}"
            f"90%{{{sc2}}}100%{{{frame(a, s1)}}}}}"
            f".b{i}{{animation:b{i} {LOOP}s cubic-bezier(.7,0,.2,1) {i * 0.012:.3f}s infinite;{frame(a, s1)}}}"
        )
        color = lerp_color(i / (n - 1))
        bricks.append(
            f'<g class="brick b{i}"><rect width="{UNIT}" height="{UNIT}" rx="5" fill="{color}"/>'
            f'<rect x="3" y="3" width="{UNIT - 6}" height="{UNIT / 2 - 3}" rx="3" fill="#fff" opacity=".18"/></g>'
        )

    chips = []
    x = 72
    for label in ["Dev", "Product", "Strategy"]:
        w = 22 + len(label) * 10.2
        chips.append(
            f'<g transform="translate({x},318)"><rect width="{w:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity=".06" stroke="#ffffff" stroke-opacity=".16"/>'
            f'<text x="{w / 2:.0f}" y="22" text-anchor="middle" class="chip">{label}</text></g>'
        )
        x += w + 12

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">first principles</title>
<desc id="d">A house made of bricks breaks into its parts and rebuilds as a rocket. Break a problem down to what is true, then rebuild from there.</desc>
<defs>
  <radialGradient id="glowA" cx="0.82" cy="0.2" r="0.6"><stop offset="0" stop-color="#7B5CFF" stop-opacity=".45"/><stop offset="1" stop-color="#7B5CFF" stop-opacity="0"/></radialGradient>
  <radialGradient id="glowB" cx="0.12" cy="1" r="0.7"><stop offset="0" stop-color="#FF2E88" stop-opacity=".30"/><stop offset="1" stop-color="#FF2E88" stop-opacity="0"/></radialGradient>
  <linearGradient id="title" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#FFB547"/><stop offset=".45" stop-color="#FF2E88"/><stop offset="1" stop-color="#7B5CFF"/></linearGradient>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#fff" opacity=".07"/></pattern>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<style>
  .brick{{transform-box:fill-box;transform-origin:center}}
  .mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
  .sans{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Helvetica,Arial,sans-serif}}
  .chip{{font:600 15px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:#E9E6FF}}
  .caret{{animation:blink 1.1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  {"".join(css)}
  @media (prefers-reduced-motion:reduce){{.brick,.caret{{animation:none}}}}
</style>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="#0A0912"/>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <rect width="{W}" height="{H}" fill="url(#glowA)"/>
  <rect width="{W}" height="{H}" fill="url(#glowB)"/>
  <text x="72" y="112" class="mono" font-size="17" fill="#9D96C8">// an agent skill for reasoning that skips the analogy</text>
  <text x="68" y="208" class="sans" font-size="92" font-weight="800" letter-spacing="-3" fill="url(#title)">first principles</text>
  <text x="72" y="262" class="sans" font-size="24" fill="#E9E6FF">Break it down to what is true. Rebuild from there.<tspan class="caret" fill="#FF2E88">&#9612;</tspan></text>
  {"".join(chips)}
  <text x="{W - 48}" y="{H - 30}" text-anchor="end" class="mono" font-size="14" fill="#6E6896">$600/kWh &#8594; $80/kWh</text>
  {"".join(bricks)}
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="none" stroke="#ffffff" stroke-opacity=".10"/>
</g>
</svg>
"""


if __name__ == "__main__":
    out = Path(__file__).with_name("banner.svg")
    out.write_text(build())
    print(f"wrote {out}")
