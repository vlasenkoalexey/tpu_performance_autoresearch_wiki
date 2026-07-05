#!/usr/bin/env python3
"""Precompute per-experiment demo diffs for the qwen3-cc-jax series.

Emits tools/demo/diffs/qwen3-cc-jax/<slug>.diff + manifest.json.
Diff hierarchy: (1) real git model-code diff for code experiments,
(2) synthesized launch-flag diff vs the previous experiment, (3) none for baseline.
"""
import json, os, re, subprocess, difflib, sys

REPO = "/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki"
os.chdir(REPO)

SERIES = "qwen3-cc-jax"
AGENT = "cc"
AGENT_NAME = "Claude"
COLOR = "#1f77b4"
LANE = "cc"
EXPDIR = f"wiki/experiments/qwen3_cc_autoresearch_optimization/jax/experiments"
MODELDIR = f"wiki/experiments/qwen3_cc_autoresearch_optimization/jax/model"
OUTDIR = f"tools/demo/diffs/{SERIES}"

# ---- libtpu flag bundles (exact names from the experiment pages) ----
VMEM = ["--xla_tpu_scoped_vmem_limit_kib=98304"]
SCHED7 = [
    "--xla_tpu_enable_all_experimental_scheduler_features=true",
    "--xla_tpu_enable_scheduler_memory_pressure_tracking=true",
    "--xla_tpu_enable_ag_backward_pipelining=true",
    "--xla_tpu_host_transfer_overlap_limit=24",
    "--xla_tpu_scheduler_percent_shared_memory_limit=100",
    "--xla_latency_hiding_scheduler_rerun=2",
    "--xla_max_concurrent_host_send_recv=100",
]
OVERLAP4 = [
    "--xla_tpu_enable_async_collective_fusion=true",
    "--xla_tpu_enable_async_collective_fusion_fuse_all_gather=true",
    "--xla_tpu_enable_async_collective_fusion_fuse_reduce_scatter=true",
    "--xla_tpu_enable_async_collective_fusion_multiple_steps=true",
]
SPARSECORE3 = [
    "--xla_tpu_enable_sparse_core_collective_offload_all_reduce=true",
    "--xla_tpu_enable_sparse_core_collective_offload_reduce_scatter=true",
    "--xla_tpu_enable_sparse_core_collective_offload_all_gather=true",
]
MAXTEXT11 = ["# + 11 MaxText layout/overlap/offload flags "
             "(LAYOUT_RS x3, DATA_PARALLEL_OVERLAP x2, CF x2, HOST_OFFLOAD x4)"]
UMBRELLA1 = ["--xla_tpu_enable_all_experimental_scheduler_features=true"]

BASE12 = VMEM + SCHED7 + OVERLAP4          # the "12-flag base bundle" / "v035 LIBTPU bundle"
MT23 = BASE12 + MAXTEXT11                  # the "23-flag MaxText superset"


def cfg(image, seqlen, batch_size, tp=1, remat=False, splash=False, scan=False,
        tokamax_ce=None, maxtext_ce=False, offload_remat=False, shard_acts=False,
        libtpu=None, env=None):
    return dict(image=image, seqlen=seqlen, batch_size=batch_size, tp=tp,
                remat=remat, splash=splash, scan=scan, tokamax_ce=tokamax_ce,
                maxtext_ce=maxtext_ce, offload_remat=offload_remat,
                shard_acts=shard_acts, libtpu=libtpu or [], env=env or {})


IMG_L = "qwen3-8b-jax:latest"
BASELINE_REF = cfg(IMG_L, 2048, 1)   # the v6e-8 baseline (bs=1, seq2048, no opt)

# hand-encoded per-experiment launch config (keyed by v-id)
CONF = {
 "v001": cfg(IMG_L, 2048, 2),
 "v002": cfg(IMG_L, 2048, 4),
 "v003": cfg(IMG_L, 2048, 1, libtpu=SPARSECORE3),
 "v004": cfg("qwen3-8b-jax:v004-remat", 2048, 2, remat=True),
 "v005": cfg("qwen3-8b-jax:v004-remat", 2048, 3, remat=True),
 "v006": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True),
 "v007": cfg("qwen3-8b-jax:v006-splash", 8192, 1, remat=True, splash=True),
 "v008": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM),
 "v009": cfg("qwen3-8b-jax:v006-splash", 8192, 1, remat=True, splash=True, libtpu=VMEM),
 "v010": cfg("qwen3-8b-jax:v010-ce", 2048, 2, remat=True, tokamax_ce="chunked_xla"),
 "v011": cfg("qwen3-8b-jax:v010-ce", 2048, 2, remat=True, tokamax_ce="mosaic_tpu"),
 "v012": cfg("qwen3-8b-jax:v010-ce", 2048, 6, remat=True, splash=True, tokamax_ce="mosaic_tpu"),
 "v013": cfg("qwen3-8b-jax:v013-ce", 2048, 2, remat=True, tokamax_ce="mosaic_tpu"),
 "v014": cfg("qwen3-8b-jax:v013-ce", 2048, 6, remat=True, splash=True, tokamax_ce="mosaic_tpu"),
 "v016": cfg("qwen3-8b-jax:v013-ce", 8192, 2, remat=True, splash=True, tokamax_ce="mosaic_tpu", libtpu=VMEM),
 "v017": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + SPARSECORE3),
 "v018": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + SCHED7),
 "v019": cfg("qwen3-8b-jax:v006-splash", 8192, 1, remat=True, splash=True, libtpu=VMEM + SCHED7),
 "v020": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + SCHED7, env={"USE_TOKAMAX_SPLASH": "1"}),
 "v021": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + SCHED7, env={"SPLASH_BQ": "1024"}),
 "v022": cfg("qwen3-8b-jax:v006-splash", 8192, 1, remat=True, splash=True, libtpu=VMEM + SCHED7, env={"SPLASH_BQ": "4096", "SPLASH_BKV": "2048"}),
 "v023": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + SCHED7 + OVERLAP4),
 "v024": cfg("qwen3-8b-jax:v006-splash", 2048, 4, remat=True, splash=True, libtpu=VMEM + UMBRELLA1),
 "v025": cfg("qwen3-8b-jax:v025-offload", 8192, 2, remat=True, splash=True, offload_remat=True, libtpu=VMEM + SCHED7),
 "v026": cfg("qwen3-8b-jax:v025-offload", 8192, 3, remat=True, splash=True, offload_remat=True, tokamax_ce="mosaic_tpu", libtpu=VMEM + SCHED7),
 "v027": cfg("qwen3-8b-jax:v027-offload-named", 8192, 3, remat=True, splash=True, offload_remat=True, tokamax_ce="mosaic_tpu", libtpu=VMEM + SCHED7),
 "v028": cfg("qwen3-8b-jax:v028-scan", 8192, 1, remat=True, splash=True, scan=True, libtpu=BASE12),
 "v029": cfg("qwen3-8b-jax:v029-full", 8192, 3, remat=True, splash=True, scan=True, offload_remat=True, tokamax_ce="mosaic_tpu", libtpu=BASE12),
 "v030": cfg("qwen3-8b-jax:v030-scan-full", 8192, 3, remat=True, splash=True, scan=True, offload_remat=True, tokamax_ce="mosaic_tpu", libtpu=BASE12),
 "v031": cfg("qwen3-8b-jax:v030-scan-full", 8192, 2, remat=True, splash=True, scan=True, tokamax_ce="mosaic_tpu", libtpu=BASE12),
 "v032": cfg("qwen3-8b-jax:v030-scan-full", 2048, 4, remat=True, splash=True, scan=True, libtpu=BASE12),
 "v033": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 1, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v034": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 2, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v035": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v036": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, offload_remat=True, libtpu=BASE12),
 "v037": cfg("qwen3-8b-jax:v033-maxtext-ce", 2048, 4, remat=True, splash=True, maxtext_ce=True, libtpu=BASE12),
 "v038": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=MT23),
 "v039": cfg("qwen3-8b-jax:v039-offload-recipe", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, offload_remat=True, libtpu=MT23),
 "v040": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12, env={"SPLASH_BKV": "2048", "SPLASH_BKV_COMPUTE": "2048"}),
 "v041": cfg("qwen3-8b-jax:v041-shard-acts", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, shard_acts=True, libtpu=BASE12),
 "v042": cfg("qwen3-8b-jax:v042-rmsnorm-bf16", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v043": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 3, tp=2, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v043b": cfg("qwen3-8b-jax:v033-maxtext-ce", 8192, 6, tp=2, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12),
 "v045": cfg("qwen3-8b-jax:v045-save-norm-stats", 8192, 3, remat=True, splash=True, scan=True, maxtext_ce=True, libtpu=BASE12, env={"SAVE_NORM_STATS": "1"}),
}

# code experiments: v-id -> (commit sha, one-line summary)
CODE = {
 "v004": ("100be90b", "Implement per-layer gradient remat (jax.checkpoint, nothing_saveable) + wire splash; enable --use_remat at bs=2"),
 "v025": ("ff103597", "Add --offload_remat lever (offload_dot_with_no_batch_dims -> pinned_host) to the trainer"),
 "v027": ("1d7f12e3", "Named host-offload (save_and_offload_only_these_names) tagging proj/mlpwi activations"),
 "v028": ("e454c82b", "Scan-over-layers: stacked-param refactor (split_rngs+vmap init, lax.scan forward)"),
 "v039": ("067a79d1", "Correct host-offload set to MaxText's exact recipe (offload decoder_layer_input + qkvo, recompute mlpwi)"),
 "v041": ("404e96b6", "Add activation sharding constraints (with_sharding_constraint at layer boundaries, --shard_acts)"),
 "v042": ("1a540ac4", "RMSNorm bf16 weight-multiply (downcast before weight scale, matches MaxText)"),
}

# flag-diff one-line summaries (keyed by v-id) for readability in the manifest
FLAG_SUMMARY = {
 "v001": "batch_size 1 -> 2 (baseline batch-scaling probe)",
 "v002": "batch_size 2 -> 4",
 "v003": "Add 3 SparseCore collective-offload libtpu flags (bs back to 1)",
 "v005": "batch_size 2 -> 3 on the remat image",
 "v006": "Enable --use_splash + batch_size 3 -> 4 (splash image)",
 "v007": "seqlen 2048 -> 8192, batch_size 4 -> 1 (splash @ 8k, no vmem yet)",
 "v008": "Add --xla_tpu_scoped_vmem_limit_kib=98304 (seq2048 bs4)",
 "v009": "seqlen 2048 -> 8192, batch_size 4 -> 1 with the vmem fix",
 "v010": "Enable tokamax cross-entropy (chunked_xla), drop splash, bs 1 -> 2",
 "v011": "tokamax CE impl chunked_xla -> mosaic_tpu",
 "v012": "Add splash, batch_size 2 -> 6 with mosaic_tpu CE",
 "v013": "absl-guarded CE image; mosaic_tpu CE at bs2 (no splash)",
 "v014": "Add splash + batch_size 2 -> 6 (absl-guarded CE image)",
 "v016": "seqlen 2048 -> 8192, bs 6 -> 2, add scoped-vmem (splash + CE @ 8k)",
 "v017": "Retry SparseCore collective-offload at bs4/seq2048 (splash image)",
 "v018": "Swap SparseCore flags for the 7 MaxText XLA scheduler flags (bs4/seq2048)",
 "v019": "seqlen 2048 -> 8192, batch_size 4 -> 1 (scheduler stack @ 8k)",
 "v020": "Enable env USE_TOKAMAX_SPLASH=1 (tokamax splash kernel)",
 "v021": "Enable env SPLASH_BQ=1024 (symmetric splash blocks)",
 "v022": "seq8192 shape + env SPLASH_BQ=4096 SPLASH_BKV=2048",
 "v023": "Add 4 async-collective-fusion overlap flags (bs4/seq2048)",
 "v024": "Ablation: keep only the umbrella scheduler flag (drop the other 6)",
 "v026": "Add mosaic_tpu CE + batch_size 2 -> 3 on the offload image",
 "v029": "Full stack: add scan + overlap flags @ bs3 seq8192",
 "v030": "scan + offload + mosaic_tpu CE @ bs3 seq8192 (rebuilt image)",
 "v031": "Drop --offload_remat, batch_size 3 -> 2 (scan + CE, no offload)",
 "v032": "seqlen 8192 -> 2048, bs 2 -> 4, drop offload/CE (scan @ 2k)",
 "v033": "Swap tokamax CE for MaxText custom_vjp CE (--use_maxtext_ce), bs4->1 seq8192",
 "v034": "batch_size 1 -> 2 (MaxText CE @ seq8192)",
 "v035": "batch_size 2 -> 3 (MaxText CE @ seq8192)",
 "v036": "Add --offload_remat on the v035 config",
 "v037": "seqlen 8192 -> 2048, drop scan + offload, bs 3 -> 4",
 "v038": "Add the 11-flag MaxText XLA superset (flags-only probe)",
 "v040": "Enable env SPLASH_BKV=2048 (match MaxText block value)",
 "v043": "Enable tp_parallelism=2 (activation sharding; global batch halved)",
 "v043b": "tp=2 with batch_size 3 -> 6 (equal global batch control)",
 "v045": "Enable env SAVE_NORM_STATS=1 (save norm rsqrt stats on-device)",
}


def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)


def vid_of(slug):
    if "baseline" in slug:
        return "baseline"
    m = re.search(r"-(v\d{1,3}[a-z]?)-", slug + "-")
    return m.group(1) if m else None


def render_runsh(c):
    L = []
    L.append("#!/usr/bin/env bash")
    L.append("# Qwen3-8B jax launch on TPU v6e-8 (2 hosts x 4 chips)")
    L.append(f"IMAGE={c['image']}")
    L.append("")
    L.append("# --- XLA / libtpu flags ---")
    L.append("LIBTPU_INIT_ARGS='")
    for f in c["libtpu"]:
        L.append(f"  {f}")
    L.append("'")
    L.append("")
    L.append("# --- env toggles ---")
    for k in sorted(c["env"]):
        L.append(f"export {k}={c['env'][k]}")
    L.append("")
    L.append("# --- train.py flags ---")
    L.append("python -u train.py \\")
    L.append("  --model_id=Qwen/Qwen3-8B \\")
    L.append("  --use_real_data=False \\")
    L.append("  --train_steps=20 \\")
    L.append("  --weights_dtype=bf16 \\")
    L.append(f"  --seqlen={c['seqlen']} \\")
    L.append(f"  --batch_size={c['batch_size']} \\")
    L.append(f"  --tp_parallelism={c['tp']} \\")
    if c["remat"]:
        L.append("  --use_remat \\")
    if c["splash"]:
        L.append("  --use_splash \\")
    if c["scan"]:
        L.append("  --use_scan \\")
    if c["offload_remat"]:
        L.append("  --offload_remat \\")
    if c["tokamax_ce"]:
        L.append("  --use_tokamax_ce \\")
        L.append(f"  --tokamax_ce_impl={c['tokamax_ce']} \\")
    if c["maxtext_ce"]:
        L.append("  --use_maxtext_ce \\")
    if c["shard_acts"]:
        L.append("  --shard_acts \\")
    L.append("  --profile_start_step=12 --profile_steps=3")
    return [ln + "\n" for ln in L]


def flag_diff(prev_c, cur_c):
    a = render_runsh(prev_c)
    b = render_runsh(cur_c)
    ud = difflib.unified_diff(a, b, fromfile="a/run.sh", tofile="b/run.sh", n=3)
    return "".join(ud)


def code_diff(sha):
    out = sh(f"git show {sha} --format='' -- {MODELDIR}")
    return out.lstrip("\n")


def read_fm(path):
    txt = open(path, encoding="utf-8", errors="ignore").read()
    def g(k):
        m = re.search(rf"^{k}:\s*(.+)$", txt, re.M)
        return m.group(1).strip().strip('"') if m else ""
    return g("title"), g("hypothesis"), txt


def hyp_info(hslug):
    """Return (title, statement) from the hypothesis page if it exists."""
    p = f"wiki/hypotheses/{hslug}.md"
    if not os.path.exists(p):
        return "", ""
    txt = open(p, encoding="utf-8", errors="ignore").read()
    tm = re.search(r'^title:\s*(.+)$', txt, re.M)
    title = tm.group(1).strip().strip('"') if tm else ""
    # statement: *Hypothesis*: ... or ## Statement paragraph
    stmt = ""
    m = re.search(r"\*Hypothesis\*:\s*(.+?)(?:\n\s*\n)", txt, re.S)
    if not m:
        m = re.search(r"##\s*Statement\s*\n+(.+?)(?:\n\s*\n)", txt, re.S)
    if m:
        stmt = re.sub(r"\s+", " ", m.group(1)).strip()
        stmt = re.sub(r"[`*]", "", stmt)
    return title, stmt


def exp_lead(txt):
    """Fallback statement from the experiment's Hypothesis-under-test lead."""
    m = re.search(r"\*\*Hypothesis\*\*:\s*(.+?)(?:\n\s*\n)", txt, re.S)
    if m:
        return re.sub(r"\s+", " ", re.sub(r"[`*]", "", m.group(1))).strip()
    return ""


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    data = json.load(open("wiki/analyses/qwen3/mfu_data.json"))
    recs = sorted([r for r in data if r["lane"] == LANE], key=lambda r: r["order"])

    manifest = {"series": SERIES, "agent": AGENT, "agent_name": AGENT_NAME,
                "color": COLOR, "model": "qwen3", "lane": "jax", "experiments": []}

    prev_c = BASELINE_REF
    for r in recs:
        slug = r["slug"]
        vid = vid_of(slug)
        path = f"{EXPDIR}/{slug}.md"
        title, hslug, txt = read_fm(path)
        htitle, hstmt = hyp_info(hslug) if hslug and hslug != "baseline" else ("", "")
        if not hstmt:
            hstmt = exp_lead(txt)

        is_baseline = (vid == "baseline")
        cur_c = CONF.get(vid)

        if is_baseline:
            diff_kind, diff_text = "none", ""
            summary = "v6e-8 baseline config (bs=1, seq2048, no optimizations)"
            # baseline does NOT advance the flag-diff chain
        elif vid in CODE:
            sha, summary = CODE[vid]
            diff_kind, diff_text = "code", code_diff(sha)
            prev_c = cur_c
        else:
            diff_text = flag_diff(prev_c, cur_c)
            if diff_text.strip():
                diff_kind = "flag"
            else:
                diff_kind = "none"
            summary = FLAG_SUMMARY.get(vid, "launch-flag change vs previous experiment")
            prev_c = cur_c

        dfile = f"{slug}.diff"
        with open(f"{OUTDIR}/{dfile}", "w") as fh:
            fh.write(diff_text)

        manifest["experiments"].append({
            "slug": slug, "vnum": r["vnum"], "order": r["order"], "seq": r["seq"],
            "title": title, "hypothesis_slug": hslug,
            "hypothesis_title": htitle, "hypothesis_statement": hstmt,
            "verdict": r["verdict"], "mfu": r["mfu"], "tps": r["tps"],
            "diff_kind": diff_kind, "diff_file": dfile, "diff_summary": summary,
        })

    with open(f"{OUTDIR}/manifest.json", "w") as fh:
        json.dump(manifest, fh, indent=2)

    kinds = {}
    for e in manifest["experiments"]:
        kinds[e["diff_kind"]] = kinds.get(e["diff_kind"], 0) + 1
    print(f"{SERIES}: {len(manifest['experiments'])} experiments; diff_kind={kinds}")
    missing = [e["slug"] for e in manifest["experiments"] if not e["hypothesis_statement"]]
    if missing:
        print("  no hypothesis_statement for:", missing)


if __name__ == "__main__":
    main()
