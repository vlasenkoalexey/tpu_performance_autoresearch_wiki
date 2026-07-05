#!/usr/bin/env python3
"""Build the autoresearch DEMO player — a self-contained, offline, cinematic HTML
walkthrough of one completed optimization series, for screen-recording a marketing video.

    python tools/demo/build_demo.py --series qwen3-cc-jax --seq 2048
    python tools/demo/build_demo.py --series qwen3-cc-jax --seq all --speed 3.5 --out tools/demo/demo.html

The player steps through the series experiment-by-experiment, three screens each:
  1. Hypothesis  — the idea the agent came up with (falsifiable statement)
  2. Change      — the diff it applied, rendered red-/green+ (code OR flag diff)
  3. Result      — the MFU chart filtered to experiments so far, with a big
                   "Best MFU: XX.X%" label in the agent's color, frontier climbing.

Playback: auto-advances at --speed; `<` / `>` (or arrows) step, Space pauses.

Data sources (join by slug):
  - tools/demo/diffs/<series>/manifest.json  (produced by the diff-precompute step) —
    carries hypothesis text + diff refs + metrics. Preferred.
  - wiki/analyses/qwen3/mfu_data.json         — authoritative per-experiment metrics.
  - Fallback: if the manifest is absent, one is synthesized from mfu_data.json +
    the experiment/hypothesis markdown pages so the player is previewable early
    (diffs then show a "pending" placeholder).

Self-contained: no external CDN. The SVG chart is bespoke (animatable, offline).
"""
import argparse, json, os, re, sys, html

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# Agent-type identity (keep in sync with wiki/analyses/qwen3/build_explorer.py).
AGENTS = {
    "cc":  {"name": "Claude",      "color": "#1f77b4"},
    "ag":  {"name": "Antigravity", "color": "#ff7f0e"},
    "cx":  {"name": "Codex",       "color": "#2ca02c"},
    "cc5": {"name": "Fable 5",     "color": "#d62728"},
}
# MaxText causal-adjusted SOTA reference (from build_explorer.py) — the line the agent climbs toward.
MAXTEXT_MFU = {2048: 36.6, 8192: 39.8}

# Monogram shown when no real logo SVG is dropped into tools/demo/assets/<agent>.svg
MONOGRAM = {"cc": "C", "ag": "AG", "cx": "CX", "cc5": "F5"}


def agent_icon(agent, color):
    """Inline SVG for the agent's top-left icon.
    Priority: real logo at tools/demo/assets/<agent>.svg  →  built-in monogram badge.
    Drop the actual brand SVG into assets/ for the real logo."""
    p = os.path.join(SCRIPT_DIR, "assets", f"{agent}.svg")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read()
    label = MONOGRAM.get(agent, agent[:2].upper())
    fs = 52 if len(label) == 1 else (40 if len(label) == 2 else 32)
    return (f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="100" height="100" rx="26" fill="{color}"/>'
            f'<text x="50" y="54" fill="#fff" font-family="-apple-system,Segoe UI,Roboto,sans-serif" '
            f'font-size="{fs}" font-weight="800" text-anchor="middle" '
            f'dominant-baseline="central">{label}</text></svg>')


def parse_series(series):
    """qwen3-cc-jax -> (model, agent, lane)."""
    m = re.match(r"^([a-z0-9]+)-(cc5|cc|cx|ag)-([a-z]+)$", series)
    if not m:
        sys.exit(f"--series must look like 'qwen3-cc-jax'; got {series!r}")
    return m.group(1), m.group(2), m.group(3)


def vkey(fn):
    m = re.search(r"v(\d{1,3})", fn); n = int(m.group(1)) if m else 999
    s = re.search(r"v\d{1,3}([a-z]?)", fn); return (n, s.group(1) if s else "", fn)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm


def extract_statement(hyp_text, exp_text):
    """One-to-three sentence falsifiable statement. Prefer the hypothesis page's
    '*Hypothesis*:' line; fall back to the experiment's 'Hypothesis under test'."""
    for txt in (hyp_text, exp_text):
        if not txt:
            continue
        m = re.search(r"\*+Hypothesis\*+:?\s*(.+?)(?:\n\n|\n\*+Mechanism)", txt, re.S | re.I)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip().strip("*").strip()
    if exp_text:
        m = re.search(r"##\s*Hypothesis under test\s*\n+(.+?)(?:\n\n|\n##)", exp_text, re.S | re.I)
        if m:
            return re.sub(r"\s+", " ", re.sub(r"\*+", "", m.group(1))).strip()
    return ""


def load_mfu_data():
    p = os.path.join(REPO, "wiki", "analyses", "qwen3", "mfu_data.json")
    if not os.path.exists(p):
        return {}
    recs = json.load(open(p))
    return {(r["lane"], r["slug"]): r for r in recs}


def build_fallback_manifest(model, agent, lane):
    """Synthesize a manifest from mfu_data.json + the markdown pages (no diffs)."""
    exp_dir = os.path.join(
        REPO, "wiki", "experiments",
        f"{model}_{agent}_autoresearch_optimization", lane, "experiments")
    if not os.path.isdir(exp_dir):
        sys.exit(f"no experiments dir: {exp_dir}")
    mfu = load_mfu_data()
    files = sorted([f for f in os.listdir(exp_dir) if f.endswith(".md")], key=vkey)
    hyp_dir = os.path.join(REPO, "wiki", "hypotheses")
    exps = []
    for order, fn in enumerate(files, 1):
        slug = fn[:-3]
        txt = open(os.path.join(exp_dir, fn), encoding="utf-8", errors="ignore").read()
        fm = frontmatter(txt)
        rec = mfu.get((agent, slug), {})
        hyp_slug = fm.get("hypothesis", "")
        hyp_txt = ""
        hp = os.path.join(hyp_dir, hyp_slug + ".md")
        if hyp_slug and os.path.exists(hp):
            hyp_txt = open(hp, encoding="utf-8", errors="ignore").read()
        hyp_fm = frontmatter(hyp_txt) if hyp_txt else {}
        exps.append({
            "slug": slug, "vnum": vkey(fn)[0], "order": order,
            "seq": rec.get("seq"), "title": fm.get("title", slug),
            "hypothesis_slug": hyp_slug,
            "hypothesis_title": hyp_fm.get("title", ""),
            "hypothesis_statement": extract_statement(hyp_txt, txt),
            "expected_gain": hyp_fm.get("expected_gain", ""),
            "verdict": rec.get("verdict", fm.get("verdict", "")),
            "mfu": rec.get("mfu"), "tps": rec.get("tps"),
            "diff_kind": "none", "diff_summary": "", "diff": "",
        })
    return {"series": f"{model}-{agent}-{lane}", "agent": agent,
            "agent_name": AGENTS[agent]["name"], "color": AGENTS[agent]["color"],
            "model": model, "lane": lane, "experiments": exps}


def load_manifest(series, model, agent, lane, diffs_root):
    """Prefer the precomputed manifest; inline each experiment's diff text."""
    mdir = os.path.join(diffs_root, series)
    mpath = os.path.join(mdir, "manifest.json")
    if os.path.exists(mpath):
        man = json.load(open(mpath))
        mfu = load_mfu_data()
        for e in man["experiments"]:
            # inline diff text
            df = e.get("diff_file")
            if df and not e.get("diff"):
                dp = os.path.join(mdir, df)
                e["diff"] = open(dp, encoding="utf-8", errors="ignore").read() if os.path.exists(dp) else ""
            # ensure metrics present (join to authoritative mfu_data.json)
            rec = mfu.get((agent, e["slug"]), {})
            e.setdefault("mfu", rec.get("mfu"))
            e.setdefault("tps", rec.get("tps"))
            e.setdefault("seq", rec.get("seq"))
            e.setdefault("verdict", rec.get("verdict", ""))
        man.setdefault("color", AGENTS[agent]["color"])
        man.setdefault("agent_name", AGENTS[agent]["name"])
        return man, True
    return build_fallback_manifest(model, agent, lane), False


def compute_frontier(exps):
    """Annotate each experiment with running-best MFU (excluding invalid), delta, isNewBest."""
    best = None
    for e in exps:
        prev = best
        e["prevBest"] = prev
        mfu = e.get("mfu")
        if mfu is not None and e.get("verdict") != "invalid":
            if best is None or mfu > best:
                best = mfu
        e["bestMfu"] = best
        e["isNewBest"] = (mfu is not None and e.get("verdict") != "invalid"
                          and (prev is None or mfu > prev))
        e["delta"] = (None if (mfu is None or prev is None) else round(mfu - prev, 1))
    return exps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", default="qwen3-cc-jax")
    ap.add_argument("--seq", default="2048", help="2048 | 8192 | all")
    ap.add_argument("--speed", type=float, default=3.2, help="base seconds per screen")
    ap.add_argument("--diffs-dir", default=os.path.join(SCRIPT_DIR, "diffs"))
    ap.add_argument("--out", default=os.path.join(SCRIPT_DIR, "demo.html"))
    ap.add_argument("--include", default="metric",
                    help="which experiments to show: 'all' | 'metric' (only metric-bearing)")
    args = ap.parse_args()

    model, agent, lane = parse_series(args.series)
    man, from_manifest = load_manifest(args.series, model, agent, lane, args.diffs_dir)

    exps = man["experiments"]
    # context-length filter
    if args.seq != "all":
        seqv = int(args.seq)
        exps = [e for e in exps if e.get("seq") == seqv]
    # inclusion policy
    if args.include == "metric":
        exps = [e for e in exps if e.get("mfu") is not None or e.get("tps") is not None]
    exps = compute_frontier(exps)

    color = man.get("color", AGENTS[agent]["color"])
    seq_for_target = int(args.seq) if args.seq != "all" else 2048
    payload = {
        "series": man["series"], "agent": agent,
        "agentName": man.get("agent_name", AGENTS[agent]["name"]),
        "color": color, "model": model, "lane": lane,
        "icon": agent_icon(agent, color),
        "seq": args.seq, "speed": args.speed,
        "maxtextTarget": MAXTEXT_MFU.get(seq_for_target),
        "fromManifest": from_manifest,
        "experiments": exps,
    }
    tpl_path = os.path.join(SCRIPT_DIR, "player.html.template")
    template = open(tpl_path, encoding="utf-8").read()
    html_out = template.replace("__PAYLOAD__", json.dumps(payload))
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as f:
        f.write(html_out)
    n_diff = sum(1 for e in exps if e.get("diff"))
    print(f"Wrote {args.out}")
    print(f"  series={args.series} seq={args.seq} experiments={len(exps)} "
          f"with-diff={n_diff} manifest={'yes' if from_manifest else 'FALLBACK (diffs pending)'}")
    if exps:
        print(f"  MFU range: {exps[0].get('mfu')} -> best {exps[-1].get('bestMfu')}")


if __name__ == "__main__":
    main()
