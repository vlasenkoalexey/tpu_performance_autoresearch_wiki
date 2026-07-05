#!/usr/bin/env python3
"""Precompute per-experiment demo diffs for the flag-only qwen3 lanes (ag / cx / cc5).

These lanes were batch-imported (no per-vNNN model-code commits), so every
experiment is a launch-flag change (rule 2) or 'none' (baseline / no documented
change). Each run's config is reconstructed from (a) the flags documented in the
page's `## Setup`, and (b) the experiment's own filename descriptors (the agent's
canonical per-run config label). No flag names are invented: confirmed trainer
flags render as `--flags`; unmapped descriptors render as `# lever:` comment lines.

Usage: python gen_series.py <lane>
"""
import json, os, re, glob, difflib, sys

REPO = "/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki"
os.chdir(REPO)

META = {
 "ag":  ("qwen3-ag-jax",  "ag",  "Antigravity", "#ff7f0e"),
 "cx":  ("qwen3-cx-jax",  "cx",  "Codex",       "#2ca02c"),
 "cc5": ("qwen3-cc5-jax", "cc5", "Fable5",      "#d62728"),
}

# confirmed trainer boolean flags for these lanes (shared JAX trainer)
BOOL_FLAGS = ["use_remat", "use_splash", "use_scan", "use_tokamax_ce",
              "use_maxtext_ce", "offload_remat", "shard_acts"]
# filename token -> boolean flag
TOK_BOOL = {
 "splash": "use_splash", "tokamax": "use_tokamax_ce", "scan": "use_scan",
 "remat": "use_remat", "offload": "offload_remat",
}


def vkey(fn):
    m = re.search(r"v(\d{1,3})", fn); n = int(m.group(1)) if m else 999
    s = re.search(r"v\d{1,3}([a-z]?)", fn); return (n, s.group(1) if s else "", fn)


def setup_text(txt):
    m = re.search(r"^## Setup\s*\n(.*?)(?:\n## |\Z)", txt, re.S | re.M)
    return m.group(1) if m else ""


def parse_image(s):
    m = re.search(r"qwen3-8b-jax:([^\s`'\"]+)", s)
    return "qwen3-8b-jax:" + m.group(1).rstrip(".,);") if m else None


# descriptor tokens that name the experiment/hypothesis, not a config lever
STOP = {"scaling", "baseline", "repro", "reference", "test", "planned",
        "batch", "bundle", "phase2", "phase", "arc"}


def parse_setup_flags(s):
    """Extract documented train + xla flags and env from the Setup text."""
    d = {}
    # numeric train flags
    for k in ("batch_size", "tp_parallelism", "seqlen"):
        m = re.search(rf"--{k}[= ]([0-9]+)", s)
        if m:
            d[k] = int(m.group(1))
    # boolean train flags (--use_x or --use_x=True/False)
    bools = {}
    for fl in BOOL_FLAGS:
        m = re.search(rf"--{fl}(?:=(True|False))?\b", s)
        if m:
            bools[fl] = (m.group(1) != "False")
    d["bools"] = bools
    m = re.search(r"--tokamax_ce_impl[= ]([a-z_]+)", s)
    if m:
        d["ce_impl"] = m.group(1)
    # xla / libtpu flags (exclude the noisy dump flags)
    xla = set()
    for m in re.finditer(r"--xla_[a-z0-9_]+(?:=[^\s`'\"]+)?", s):
        f = m.group(0)
        if "xla_dump" in f:
            continue
        xla.add(f)
    d["xla"] = xla
    # env toggles (uppercase NAME=VAL), whitelist meaningful ones
    env = {}
    for m in re.finditer(r"\b([A-Z][A-Z0-9_]{2,})=([^\s`'\"]+)", s):
        k, v = m.group(1), m.group(2)
        if k in ("JAX_COMPILATION_CACHE_DIR", "XLA_FLAGS", "LIBTPU_INIT_ARGS") or \
           k.startswith("JAX_PERSISTENT") or k.startswith("GS") or "CACHE" in k:
            continue
        if k.startswith(("USE_", "TOKAMAX_", "SPLASH_", "SAVE_", "SKIP_", "REMAT",
                         "JAX_ATTENTION", "NSA_", "CHUNK")):
            env[k] = v
    d["env"] = env
    return d


def descriptors(slug):
    """Return (vid, [descriptor tokens]) from the filename."""
    base = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    base = re.sub(r"^qwen3-jax-", "", base)
    toks = base.split("-")
    vid = toks[0] if toks else ""
    return vid, toks[1:]


def apply_descriptors(cfg, toks):
    """Overlay filename descriptors onto cfg (fresh booleans/levers per run)."""
    levers = []
    for t in toks:
        m = re.fullmatch(r"bs(\d+)", t) or re.fullmatch(r"batch(\d+)", t)
        if m:
            cfg["batch_size"] = int(m.group(1)); continue
        m = re.fullmatch(r"tp(\d+)", t)
        if m:
            cfg["tp_parallelism"] = int(m.group(1)); continue
        m = re.fullmatch(r"seq(\d+)", t)
        if m:
            cfg["seqlen"] = int(m.group(1)); continue
        m = re.fullmatch(r"s?(\d+)k", t)
        if m:
            cfg["seqlen"] = int(m.group(1)) * 1024; continue
        m = re.fullmatch(r"splash(\d+)", t)
        if m:
            cfg["bools"]["use_splash"] = True
            levers.append("splash-block-" + m.group(1)); continue
        if t in TOK_BOOL:
            cfg["bools"][TOK_BOOL[t]] = True
            continue
        if t == "chunked":
            cfg["ce_impl"] = "chunked_xla"; continue
        if t == "mosaic":
            cfg["ce_impl"] = "mosaic_tpu"; continue
        if t == "vocab":
            levers.append("vocab-parallel-CE"); continue
        if t == "parallel":
            continue  # part of the vocab-parallel lever
        if t in ("tpu", "xla", "ce", "bundle", "b", "c", "d", "e", "f", "g", "h",
                 "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"):
            # ce-impl qualifiers / attempt suffixes already handled or noise
            if t not in ("tpu", "xla", "ce"):
                levers.append("attempt-" + t)
            continue
        if t in STOP:
            continue
        levers.append(t)
    cfg["levers"] = levers
    return cfg


def new_cfg():
    return {"image": IMG_DEFAULT, "batch_size": 1, "tp_parallelism": 1,
            "seqlen": 2048, "bools": {}, "ce_impl": None, "xla": set(),
            "env": {}, "levers": []}


IMG_DEFAULT = "qwen3-8b-jax:latest"


def build_cfg(prev, slug, txt):
    """Reconstruct this run's config. Carry forward image + numeric axes only."""
    s = setup_text(txt)
    doc = parse_setup_flags(s)
    img = parse_image(s)
    c = {"image": img or (prev["image"] if prev else IMG_DEFAULT),
         "batch_size": prev["batch_size"] if prev else 1,
         "tp_parallelism": prev["tp_parallelism"] if prev else 1,
         "seqlen": prev["seqlen"] if prev else 2048,
         "bools": {}, "ce_impl": None, "xla": set(), "env": {}, "levers": []}
    # 1) filename descriptors (fresh booleans/levers)
    vid, toks = descriptors(slug)
    apply_descriptors(c, toks)
    # 2) documented Setup flags override (authoritative)
    for k in ("batch_size", "tp_parallelism", "seqlen"):
        if k in doc:
            c[k] = doc[k]
    for fl, on in doc.get("bools", {}).items():
        c["bools"][fl] = on
    if doc.get("ce_impl"):
        c["ce_impl"] = doc["ce_impl"]
    c["xla"] = doc.get("xla", set())
    c["env"] = doc.get("env", {})
    return c, vid


def render(c):
    L = ["#!/usr/bin/env bash",
         "# Qwen3-8B jax launch on TPU v6e-8 (2 hosts x 4 chips)",
         f"IMAGE={c['image']}", "",
         "# --- XLA / libtpu flags ---", "LIBTPU_INIT_ARGS='"]
    for f in sorted(c["xla"]):
        L.append(f"  {f}")
    L.append("'")
    L += ["", "# --- env toggles ---"]
    for k in sorted(c["env"]):
        L.append(f"export {k}={c['env'][k]}")
    L += ["", "# --- train.py flags ---", "python -u train.py \\",
          "  --model_id=Qwen/Qwen3-8B \\",
          "  --use_real_data=False \\",
          "  --weights_dtype=bf16 \\",
          f"  --seqlen={c['seqlen']} \\",
          f"  --batch_size={c['batch_size']} \\",
          f"  --tp_parallelism={c['tp_parallelism']} \\"]
    for fl in BOOL_FLAGS:
        if c["bools"].get(fl):
            L.append(f"  --{fl} \\")
            if fl == "use_tokamax_ce" and c["ce_impl"]:
                L.append(f"  --tokamax_ce_impl={c['ce_impl']} \\")
    if c["levers"]:
        L.append("  # levers (this run's descriptors):")
        for lv in c["levers"]:
            L.append(f"  #   {lv}")
    L.append("  --profile_start_step=12 --profile_steps=3")
    return [ln + "\n" for ln in L]


def summarize(prev, cur):
    """One-line delta between two configs for the manifest."""
    parts = []
    if prev is None:
        return "initial documented config"
    for k, lbl in (("seqlen", "seqlen"), ("batch_size", "batch_size"),
                   ("tp_parallelism", "tp")):
        if prev[k] != cur[k]:
            parts.append(f"{lbl} {prev[k]} -> {cur[k]}")
    pb, cb = set(k for k, v in prev["bools"].items() if v), \
             set(k for k, v in cur["bools"].items() if v)
    for f in sorted(cb - pb):
        parts.append("+" + f)
    for f in sorted(pb - cb):
        parts.append("-" + f)
    if prev.get("ce_impl") != cur.get("ce_impl") and cur.get("ce_impl"):
        parts.append("ce_impl=" + cur["ce_impl"])
    pe, ce = set(prev["env"]), set(cur["env"])
    for k in sorted(ce - pe):
        parts.append("+env " + k)
    pl, cl = set(prev["levers"]), set(cur["levers"])
    for lv in sorted(cl - pl):
        parts.append("+" + lv)
    for lv in sorted(pl - cl):
        parts.append("-" + lv)
    xa = cur["xla"] - prev["xla"]
    if xa:
        parts.append(f"+{len(xa)} xla flag(s)")
    return "; ".join(parts) if parts else "no documented launch change vs previous"


def hyp_info(hslug):
    if not hslug:
        return "", ""
    # ag/cc5 sometimes put a full sentence in the hypothesis: field, not a slug
    if " " in hslug or len(hslug) > 80:
        return "", hslug.strip().strip('"')
    p = f"wiki/hypotheses/{hslug}.md"
    if not os.path.exists(p):
        return "", ""
    t = open(p, encoding="utf-8", errors="ignore").read()
    tm = re.search(r'^title:\s*(.+)$', t, re.M)
    title = tm.group(1).strip().strip('"') if tm else ""
    m = re.search(r"\*Hypothesis\*:\s*(.+?)(?:\n\s*\n)", t, re.S) or \
        re.search(r"##\s*Statement\s*\n+(.+?)(?:\n\s*\n)", t, re.S)
    stmt = re.sub(r"[`*]", "", re.sub(r"\s+", " ", m.group(1))).strip() if m else ""
    return title, stmt


def exp_lead(txt):
    m = re.search(r"\*\*Hypothesis\*\*:\s*(.+?)(?:\n\s*\n)", txt, re.S)
    return re.sub(r"[`*]", "", re.sub(r"\s+", " ", m.group(1))).strip() if m else ""


def is_baseline(vid, slug):
    return "baseline" in slug and "repro" not in slug or "baseline" in slug


def main():
    lane = sys.argv[1]
    series, agent, aname, color = META[lane]
    expdir = f"wiki/experiments/qwen3_{lane}_autoresearch_optimization/jax/experiments"
    outdir = f"tools/demo/diffs/{series}"
    os.makedirs(outdir, exist_ok=True)

    data = json.load(open("wiki/analyses/qwen3/mfu_data.json"))
    mfu = {r["slug"]: r for r in data if r["lane"] == lane}

    files = sorted(glob.glob(f"{expdir}/*.md"),
                   key=lambda f: vkey(os.path.basename(f)))
    manifest = {"series": series, "agent": agent, "agent_name": aname,
                "color": color, "model": "qwen3", "lane": "jax", "experiments": []}

    prev = None
    order = 0
    for f in files:
        slug = os.path.basename(f)[:-3]
        order += 1
        txt = open(f, encoding="utf-8", errors="ignore").read()
        tm = re.search(r'^title:\s*(.+)$', txt, re.M)
        title = tm.group(1).strip().strip('"') if tm else slug
        hm = re.search(r'^hypothesis:\s*(.+)$', txt, re.M)
        hslug = hm.group(1).strip().strip('"') if hm else ""
        htitle, hstmt = hyp_info(hslug)
        if not hstmt:
            hstmt = exp_lead(txt)
        rec = mfu.get(slug, {})

        baseline = ("baseline" in slug)
        cur, vid = build_cfg(prev, slug, txt)

        if baseline:
            diff_kind, diff_text = "none", ""
            summary = "baseline reference config (no optimization delta)"
            # baseline resets the chain reference to itself (start of an arc)
            prev = cur
        else:
            a = render(prev) if prev is not None else render(new_cfg())
            b = render(cur)
            diff_text = "".join(difflib.unified_diff(
                a, b, fromfile="a/run.sh", tofile="b/run.sh", n=3))
            diff_kind = "flag" if diff_text.strip() else "none"
            summary = summarize(prev, cur) if diff_kind == "flag" \
                else "no documented launch change vs previous"
            prev = cur

        dfile = f"{slug}.diff"
        with open(f"{outdir}/{dfile}", "w") as fh:
            fh.write(diff_text)

        manifest["experiments"].append({
            "slug": slug, "vnum": vkey(slug)[0], "order": order,
            "seq": rec.get("seq", cur["seqlen"]),
            "title": title, "hypothesis_slug": hslug if " " not in hslug else "",
            "hypothesis_title": htitle, "hypothesis_statement": hstmt,
            "verdict": rec.get("verdict", ""), "mfu": rec.get("mfu"),
            "tps": rec.get("tps"),
            "diff_kind": diff_kind, "diff_file": dfile, "diff_summary": summary,
        })

    json.dump(manifest, open(f"{outdir}/manifest.json", "w"), indent=2)
    kinds = {}
    for e in manifest["experiments"]:
        kinds[e["diff_kind"]] = kinds.get(e["diff_kind"], 0) + 1
    print(f"{series}: {len(manifest['experiments'])} experiments; diff_kind={kinds}")


if __name__ == "__main__":
    main()
