#!/usr/bin/env python3
"""One-slide cross-agent comparison: all 4 agents' best-MFU hill-climb, split 2k vs 8k.

    python tools/demo/build_comparison_slide.py --out /path/compare.pptx

Two panels (2k, 8k); each plots every agent's running-best MFU frontier over optimization
progress, in brand-aligned colours (Claude brown/orange, Antigravity blue, Codex teal,
Fable5 red). Legend uses the agent logos (Claude rendered in its brown/orange brand colour,
not the default black sunburst). Data from wiki/analyses/qwen3/mfu_data.json.
"""
import argparse, json, os, tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(SCRIPT_DIR, "..", "..", "wiki", "analyses", "qwen3", "mfu_data.json")

AGENTS = ["cc", "ag", "cx", "cc5"]
NAME = {"cc": "Claude", "ag": "Antigravity", "cx": "Codex", "cc5": "Fable 5"}
# brand-aligned colours (Claude = brown/orange per request; Antigravity = its blue; Codex = OpenAI teal)
COLOR = {"cc": "#C4623C", "ag": "#3186FF", "cx": "#10A37F", "cc5": "#D62728"}
MAXTEXT = {2048: 36.6, 8192: 39.8}
INK, MUTE, SUBT, LINE = "#1a1d21", "#5b6570", "#8a929c", "#e6e9ee"
SW, SH = Inches(13.333), Inches(7.5)


def hexrgb(h):
    h = h.lstrip("#"); return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def frontier(rows):
    """running-best MFU over experiment order → (normalized x [0..1], y)."""
    rows = sorted([r for r in rows if r.get("mfu") is not None
                   and (r.get("verdict") or "").lower() != "invalid"], key=lambda r: r["order"])
    xs, ys, b = [], [], None
    for i, r in enumerate(rows):
        b = r["mfu"] if b is None or r["mfu"] > b else b
        xs.append(i); ys.append(b)
    n = len(xs)
    if n == 0:
        return [], [], None
    xn = [x / (n - 1) for x in xs] if n > 1 else [0.0]
    return xn, ys, b


def render_icon(agent, tmp):
    """Legend logo: Claude/Codex tinted to brand colour; Antigravity natural; Fable5 monogram."""
    svg = os.path.join(SCRIPT_DIR, "assets", f"{agent}.svg")
    out = os.path.join(tmp, f"leg_{agent}.png")
    if agent in ("cc", "cx") and os.path.exists(svg):
        import resvg_py
        s = open(svg, encoding="utf-8").read().replace("currentColor", COLOR[agent])
        open(out, "wb").write(bytes(resvg_py.svg_to_bytes(svg_string=s, width=256)))
        return out
    if agent == "ag" and os.path.exists(svg):
        import resvg_py
        open(out, "wb").write(bytes(resvg_py.svg_to_bytes(
            svg_string=open(svg, encoding="utf-8").read(), width=256)))
        return out
    # Fable5 monogram
    im = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    c = tuple(hexrgb(COLOR[agent])) + (255,)
    dr.rounded_rectangle([8, 8, 248, 248], radius=54, fill=c)
    try:
        fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
    except Exception:
        fnt = ImageFont.load_default()
    dr.text((128, 128), "F5", font=fnt, fill=(255, 255, 255, 255), anchor="mm")
    im.save(out); return out


def draw_panel(ax, seq, data):
    tv = MAXTEXT[seq]
    ax.axhline(tv, ls=(0, (6, 5)), color="#9aa0a6", lw=1.4, zorder=2)
    ax.text(0.02, tv, f"MaxText SOTA {tv:.1f}%", ha="left", va="bottom", color="#8a929c",
            fontsize=10.5, transform=ax.get_yaxis_transform())
    ymax = tv
    for ag in AGENTS:
        xn, ys, best = data[(ag, seq)]
        if not xn:
            continue
        ymax = max(ymax, max(ys))
        if len(xn) == 1:
            ax.scatter(xn, ys, color=COLOR[ag], s=70, zorder=6)
        else:
            ax.step(xn, ys, where="post", color=COLOR[ag], lw=3, zorder=5, solid_capstyle="round")
        ax.scatter([xn[-1]], [ys[-1]], color=COLOR[ag], s=42, zorder=7)
        ax.annotate(f"{best:.1f}%", (xn[-1], ys[-1]), textcoords="offset points",
                    xytext=(6, 2), fontsize=11, fontweight="bold", color=COLOR[ag])
    ax.set_title(f"{seq // 1024}k context", fontsize=15, fontweight="bold", color=INK, pad=10)
    ax.set_xlim(-0.02, 1.12); ax.set_ylim(18, ymax * 1.1)
    ax.set_xlabel("optimization progress →", fontsize=11, color=MUTE)
    ax.set_ylabel("best MFU (%, causal)", fontsize=11, color=MUTE)
    ax.grid(True, axis="y", color="#eceff3", lw=1)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#d7dbe0")
    ax.tick_params(colors="#8a929c", labelsize=9)
    ax.set_xticks([0, 0.5, 1.0]); ax.set_xticklabels(["start", "50%", "100%"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(SCRIPT_DIR, "compare.pptx"))
    args = ap.parse_args()
    rows = json.load(open(DATA))
    data, best = {}, {}
    for ag in AGENTS:
        for seq in (2048, 8192):
            sub = [r for r in rows if r["lane"] == ag and r["seq"] == seq]
            xn, ys, b = frontier(sub)
            data[(ag, seq)] = (xn, ys, b); best[(ag, seq)] = b

    tmp = tempfile.mkdtemp()
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.9), dpi=150)
    fig.patch.set_facecolor("white")
    for ax, seq in zip(axes, (2048, 8192)):
        ax.set_facecolor("white"); draw_panel(ax, seq, data)
    fig.tight_layout(pad=1.5)
    chart = os.path.join(tmp, "compare.png"); fig.savefig(chart, facecolor="white"); plt.close(fig)

    icons = {ag: render_icon(ag, tmp) for ag in AGENTS}

    prs = Presentation(); prs.slide_width = SW; prs.slide_height = SH
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid(); s.background.fill.fore_color.rgb = hexrgb("#ffffff")
    tb = s.shapes.add_textbox(Inches(0.6), Inches(0.34), Inches(12.1), Inches(1.0)).text_frame
    tb.word_wrap = True
    r = tb.paragraphs[0].add_run(); r.text = "Four agents, one problem — the autonomous MFU climb"
    r.font.size = Pt(26); r.font.bold = True; r.font.name = "Calibri"; r.font.color.rgb = hexrgb(INK)
    p = tb.add_paragraph(); r = p.add_run()
    r.text = "Qwen3-8B · TPU v6e-8 · best MFU (causal) vs experiments — dashed = MaxText SOTA"
    r.font.size = Pt(13); r.font.name = "Calibri"; r.font.color.rgb = hexrgb(MUTE)
    s.shapes.add_picture(chart, Inches(0.7), Inches(1.45), width=Inches(11.9))

    # icon legend row
    x0, y = Inches(1.15), Inches(6.55); step = Inches(2.95)
    for i, ag in enumerate(AGENTS):
        x = x0 + step * i
        s.shapes.add_picture(icons[ag], x, y, height=Inches(0.5))
        tf = s.shapes.add_textbox(x + Inches(0.62), y - Inches(0.02), Inches(2.3), Inches(0.6)).text_frame
        tf.word_wrap = True
        rn = tf.paragraphs[0].add_run(); rn.text = NAME[ag]
        rn.font.size = Pt(14); rn.font.bold = True; rn.font.name = "Calibri"; rn.font.color.rgb = hexrgb(COLOR[ag])
        pp = tf.add_paragraph(); rn = pp.add_run()
        b2, b8 = best[(ag, 2048)], best[(ag, 8192)]
        rn.text = f"2k {b2:.1f}%" + (f" · 8k {b8:.1f}%" if b8 else "")
        rn.font.size = Pt(11); rn.font.name = "Calibri"; rn.font.color.rgb = hexrgb(MUTE)

    prs.save(args.out)
    print(f"Wrote {args.out} ({os.path.getsize(args.out)//1024}KB)")
    for ag in AGENTS:
        print(f"  {NAME[ag]:12} 2k={best[(ag,2048)]}  8k={best[(ag,8192)]}")


if __name__ == "__main__":
    main()
