#!/usr/bin/env python3
"""Animated hill-climb GIF for a kernel family — the kernel-lane sibling of the
Qwen3 model-lane animation used in the README case study.

Reads `kernel_data.json` (produced by kernel_explorer.py, so no re-scan of the
branches is needed) and renders one running-best-speedup staircase per arm, in
the same colours the interactive explorer uses, against MaxKernel's published
best as a dashed reference.

    python3 tools/kernel_explorer/build_hillclimb_gif.py \
        --kernel gqa-attention --out raw/assets/kernel-gqa-hillclimb.gif

    --kernel all   one panel per family (grid), running best across arms

Frames are emitted one experiment at a time, so the animation shows what the
static chart cannot: long flat stretches of refuted hypotheses punctuated by
step changes. Filled marker = this experiment raised the arm's best; hollow =
it did not.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))

# Must match kernel_explorer.py's DEFAULT_ARMS order and ARMPALETTE, so the GIF
# and the interactive explorer agree on which colour means which arm.
ARMS = [("opus5", "Claude Opus 5", "#e67e22"),
        ("codex", "Codex GPT-5.6", "#8e44ad"),
        ("gemini", "Gemini Flash 3.6", "#2e86de")]
GREY = "#5B6570"


def load(path, kernel, arms):
    recs = json.load(open(path))
    out = {}
    for a, _, _ in arms:
        rows = [r for r in recs
                if r.get("arm") == a and r.get("family") == kernel
                and r.get("has_metric") and r.get("speedup")]
        rows.sort(key=lambda r: r.get("vnum") or 0)
        out[a] = rows
    return out


def running_best(rows):
    """(x, y, improved) per experiment — y is the best speedup seen so far."""
    xs, ys, hit = [], [], []
    best = 0.0
    for i, r in enumerate(rows, 1):
        s = float(r["speedup"])
        improved = s > best
        best = max(best, s)
        xs.append(i); ys.append(best); hit.append((improved, s))
    return xs, ys, hit


def render(series, kernel, mk, outfile, fps_ms=260, tail=8):
    n = max((len(v[0]) for v in series.values()), default=0)
    if not n:
        sys.exit(f"no metric-bearing experiments for kernel '{kernel}'")
    ymax = max([max(v[1]) for v in series.values() if v[1]] + [mk or 0]) * 1.18
    ymin = 0.9

    tmp = tempfile.mkdtemp(prefix="hillclimb-")
    frames = []
    for f in range(1, n + 1 + tail):          # tail frames hold the final state
        k = min(f, n)
        fig, ax = plt.subplots(figsize=(11, 5.2), dpi=110)
        if mk:
            ax.axhline(mk, ls="--", lw=1.6, color=GREY, zorder=1)
            ax.text(n * 0.995, mk + ymax * 0.012, f"MaxKernel best {mk:.2f}x",
                    ha="right", va="bottom", color=GREY, fontsize=11)
        for arm, label, colour in ARMS:
            xs, ys, hit = series.get(arm, ([], [], []))
            if not xs:
                continue
            cut = min(k, len(xs))
            if cut == 0:
                continue
            ax.step(xs[:cut], ys[:cut], where="post", lw=2.4, color=colour, zorder=3)
            for i in range(cut):
                improved, raw = hit[i]
                ax.plot(xs[i], raw, "o", ms=6, zorder=4,
                        mfc=colour if improved else "none", mec=colour, mew=1.5)
            ax.text(xs[cut - 1] + n * 0.012, ys[cut - 1], f"{ys[cut-1]:.2f}x",
                    color=colour, fontsize=12, fontweight="bold", va="center")
        ax.set_xlim(0.4, n * 1.10)
        ax.set_ylim(ymin, ymax)
        ax.set_xlabel("experiment #", fontsize=11)
        ax.set_ylabel("best speedup vs naive (x)", fontsize=11)
        ax.set_title(f"{kernel} — kernel-lane hill climb  "
                     f"(filled = new best, hollow = no gain, dashed = MaxKernel)",
                     fontsize=13, fontweight="bold")
        ax.grid(alpha=.25, lw=.7)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.legend(handles=[Line2D([], [], color=c, lw=2.4, label=l)
                           for _, l, c in ARMS if series.get(_)],
                  loc="lower right", frameon=False, fontsize=11)
        p = os.path.join(tmp, f"f{f:04d}.png")
        fig.tight_layout(); fig.savefig(p); plt.close(fig)
        frames.append(p)

    from PIL import Image
    imgs = [Image.open(p).convert("P", palette=Image.ADAPTIVE, colors=128) for p in frames]
    imgs[0].save(outfile, save_all=True, append_images=imgs[1:],
                 duration=fps_ms, loop=0, optimize=True, disposal=2)
    # gifsicle does real inter-frame diffing; PIL alone bloats the file
    if subprocess.run(["which", "gifsicle"], capture_output=True).returncode == 0:
        subprocess.run(["gifsicle", "-O3", "--colors", "128", "--lossy=40",
                        outfile, "-o", outfile], check=False)
    print(f"  {outfile}  {len(frames)} frames  {os.path.getsize(outfile)//1024} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kernel", default="gqa-attention")
    ap.add_argument("--data", default=os.path.join(HERE, "kernel_data.json"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--ms", type=int, default=260, help="ms per frame")
    a = ap.parse_args()

    sys.path.insert(0, HERE)
    from kernel_explorer import MK_BEST
    mk = None
    if a.kernel in MK_BEST:
        _, val, artifact = MK_BEST[a.kernel]
        mk = None if artifact else val

    series = {k: running_best(v) for k, v in load(a.data, a.kernel, ARMS).items()}
    out = a.out or os.path.join(HERE, f"hillclimb-{a.kernel}.gif")
    render(series, a.kernel, mk, out, fps_ms=a.ms)


if __name__ == "__main__":
    main()
