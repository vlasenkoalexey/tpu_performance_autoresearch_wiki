#!/usr/bin/env python3
"""Interactive Pallas kernel-optimization explorer (kernel-lane sibling of explorer_lib.py).

Scans every kernel family under wiki/kernel_experiments/<family>/pallas/ —
RESULTS.tsv is the primary ledger (schemas differ per family; parsing is
header-driven and normalized), experiment pages supplement verdicts/titles,
contribute "pending / no-metric" rows for v-pages the TSV doesn't list yet,
and provide the per-experiment K7 candidate ledger (cand1, cand2, … including
failures), which the viewer renders as small sub-points clustered around each
experiment's vNNN tick.

Outputs (next to this script, or $KERNEL_EXPLORER_OUTDIR):
  kernel-explorer.html   static Plotly viewer — no server needed
  kernel_data.json       the extracted records

Multi-arm: each LLM ran the same K0–K9 process on its own campaign branch, and
all arms are loaded side by side (see DEFAULT_ARMS). A Kernel dropdown plus one
checkbox per LLM select the view, both mirrored into the URL:
  ?kernel=<family-slug>       one family, or "all"
  ?llm=all | <key>,<key>,…    which arms are checked
  kernel=X   + several arms  → one frontier per LLM on kernel X (the comparison)
  kernel=all + one arm       → one frontier per family for that LLM
  kernel=X   + one arm       → detail view: verdict-colored points + K7 candidates
  kernel=all + several arms  → every (family, arm) pair
At least one arm stays checked. MaxKernel's published best (MK⁵) is available as
a toggleable reference line on the speedup view, drawn from MK_BEST.
Experiment links resolve to the file on that arm's OWN branch — none of this
content is on main, so a blob/main URL would 404.

Record schema (per experiment):
  family, id, vnum, verdict (canonical), time_ms, baseline_ms, speedup,
  tflops, util (%), parity, cls, desc, link, has_metric, arm, branch,
  cands: [{cid, n, time_ms, speedup, parity, note, failed}]

Roofline is NOT a metric: on the TFLOP/s view a dotted line marks each family's
implied ceiling — max over receipts of tflops/(util) — with measured util kept
in the hover text.

Regenerate: python3 tools/kernel_explorer/kernel_explorer.py

Each arm's ledgers are read straight out of its branch via `git archive` into a
cache dir, so no checkout is needed and the working tree is never touched (safe
to run while a campaign is live). Env overrides:
  KERNEL_EXPLORER_REPO    repo to read refs from (default: two dirs up)
  KERNEL_EXPLORER_OUTDIR  where the html/json land (default: next to this file)
  KERNEL_EXPLORER_CACHE   staging dir for the per-arm trees
  KERNEL_EXPLORER_ARMS    'key|Label|branch,…' to override DEFAULT_ARMS

Promoted from wiki/analyses/kernel_explorer_lib.py; the "_lib" suffix was a
misnomer (it is an executable generator, not a library).
"""
import os, re, json, glob, shutil, subprocess, tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# REPO defaults to two dirs up (tools/kernel_explorer/ -> repo root, same depth as the original
# wiki/analyses/ home). Override when the ledgers live in another tree — e.g. running from `main`,
# which does not track wiki/kernel_experiments/**; point it at a checkout of the campaign branch.
REPO = os.environ.get("KERNEL_EXPLORER_REPO") or os.path.dirname(os.path.dirname(SCRIPT_DIR))
OUTDIR = os.environ.get("KERNEL_EXPLORER_OUTDIR") or SCRIPT_DIR
LANE = "pallas"

# ---- arms: one campaign branch per LLM ------------------------------------------------
# Each arm is an independent run of the SAME K0–K9 process by a different model, on its own
# branch. Ledgers are read straight out of each branch (git archive → cache dir), so no
# checkout happens and the working tree is never touched — safe while a campaign is live.
# Labels are what the branch's own artifacts say the model was, not what the branch is named.
DEFAULT_ARMS = [
    ("opus5",  "Claude Opus 5",    "pallas-kernel-optimization-opus5-process"),
    ("codex",  "Codex GPT-5.6",    "pallas-kernel-optimization-codex-process"),
    ("gemini", "Gemini Flash 3.6", "pallas-kernel-optimization-antigravity-process6"),
]
CACHE = (os.environ.get("KERNEL_EXPLORER_CACHE")
         or os.path.join(tempfile.gettempdir(), "kernel_explorer_arms"))

# Slug aliases. program.md's Quick-start rule 1 requires two agents given the SAME kernel to derive
# the SAME family slug; where an arm deviated, map it onto the canonical slug so the cross-LLM view
# lines up instead of showing the same kernel twice. Paths keep the on-disk directory name.
FAMILY_ALIAS = {
    "gqa-attn": "gqa-attention",   # gemini arm deviated from the canonical slug
}

# MaxKernel published best (MK⁵ = best-of-5), the external reference bar per problem.
#   slug -> (problem id, MK⁵ speedup or None, is_artifact)
# Source: wiki/analyses/2026-07-17-combined-kernel-scoreboard.md, MK⁵ column, on the campaign
# branch. `is_artifact` mirrors that page's ✗ marker — cells that are device-framing or physically
# impossible. Those are drawn dashed-and-labelled rather than dropped, because "MK claims 26.86×
# and it isn't real" is itself the useful fact; they must never be treated as a bar to beat.
# A speedup-only reference: it has no meaning on the p50-ms or TFLOP/s axes, so the line is drawn
# on the speedup metric only.
MK_BEST = {
    "flash-attn-mha":                            ("1p",  2.38,  False),
    "gqa-attention":                             ("2p",  2.48,  False),
    "mla-attention":                             ("3p",  1.06,  False),
    "sparse-attention":                          ("4p",  2.44,  False),
    "flex-attention":                            ("5p",  2.35,  False),
    "paged-attention":                           ("6p",  1.13,  False),
    "ragged-paged-attention":                    ("7p",  4.44,  True),
    "gemm":                                      ("8p",  1.00,  False),
    "swiglu-mlp":                                ("9p",  None,  True),   # MK failed outright
    "sparse-moe":                                ("10p", 2.83,  False),
    "megablox-gmm":                              ("11p", 1.77,  False),
    "rms-norm":                                  ("12p", 1.63,  True),   # invalidated, real bar 1.39
    "cross-entropy":                             ("13p", 1.22,  False),
    "ragged-dot":                                ("14p", 1.00,  False),
    "retnet-retention":                          ("15p", 5.61,  False),
    "mamba2-ssd":                                ("16p", 5.11,  False),
    "triangle-multiplication":                   ("17p", 1.00,  False),
    "matmul-subtract-multiply-relu":             ("19k", 1.37,  False),
    "gemm-divide-sum-scaling":                   ("21k", 15.11, True),
    "bmm-instancenorm-sum-residualadd-multiply": ("26k", 10.10, True),
    "matmul-mish-mish":                          ("27k", 1.21,  False),
    "matmul-scaling-residualadd":                ("30k", 26.86, True),
    "matmul-swish-scaling":                      ("37k", 1.35,  False),
    "matmul-avgpool-gelu-scale-max":             ("49k", 1.85,  False),
}


def parse_arms():
    """$KERNEL_EXPLORER_ARMS = 'key|Label|branch,key|Label|branch' overrides DEFAULT_ARMS."""
    raw = os.environ.get("KERNEL_EXPLORER_ARMS")
    if not raw:
        return list(DEFAULT_ARMS)
    arms = []
    for spec in raw.split(","):
        parts = [p.strip() for p in spec.split("|")]
        if len(parts) == 3:
            arms.append(tuple(parts))
    return arms or list(DEFAULT_ARMS)


def git(*args):
    return subprocess.run(("git", "-C", REPO) + args, capture_output=True, text=True)


def gh_repo():
    """owner/repo from origin — absolute blob links don't depend on where the page is served."""
    m = re.search(r"github\.com[:/](.+?)(?:\.git)?\s*$",
                  git("remote", "get-url", "origin").stdout.strip())
    return m.group(1) if m else ""


def resolve_ref(branch):
    """Prefer origin/<branch> when it exists — that is what a blob link can actually reach."""
    for ref in (f"origin/{branch}", branch):
        if git("rev-parse", "--verify", "--quiet", ref).returncode == 0:
            return ref
    return None


def stage_arm(ref, dest):
    """Materialize <ref>:wiki/kernel_experiments into dest. Returns True on success."""
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    p = subprocess.Popen(("git", "-C", REPO, "archive", ref, "wiki/kernel_experiments"),
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    t = subprocess.run(("tar", "-x", "-C", dest), stdin=p.stdout, capture_output=True)
    p.stdout.close()
    return p.wait() == 0 and t.returncode == 0


# ---------------------------------------------------------------- extraction

def norm_verdict(s):
    """Normalize a raw verdict/status string to a canonical verdict."""
    if not s:
        return ""
    s = s.strip().lower()
    if "partial" in s:                                    return "partial"
    if "supported" in s or "confirmed" in s or "accepted" in s: return "supported"
    if "invalid" in s:                                    return "invalid"
    if "refuted" in s or "rejected" in s:                 return "refuted"
    if "inconclusive" in s:                               return "inconclusive"
    if "baseline" in s:                                   return "baseline"
    if "complete" in s or "filed" in s:                   return "completed"
    if any(k in s for k in ("progress", "pending", "open", "running", "tbd")): return "pending"
    return ""


def fnum(x):
    if x is None:
        return None
    x = str(x).strip().rstrip("%xX×").strip("`* ")
    if x.lower() in ("", "-", "—", "n/a", "na", "none"):
        return None
    m = re.search(r"-?\d+(?:\.\d+)?", x)
    return float(m.group(0)) if m else None


def norm_util(raw):
    """roofline util appears as '46.7%', '0.621' or '0.052' → percent float."""
    v = fnum(raw)
    if v is None:
        return None
    return v * 100 if v <= 1.5 else v


def page_meta(path):
    """frontmatter verdict/status + title (or first H1) from an experiment page."""
    fm, title = {}, None
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError:
        return fm, title, []
    in_fm = False
    for ln in lines[:60]:
        if ln.strip() == "---":
            if in_fm:
                break
            in_fm = True
            continue
        if in_fm and ":" in ln:
            k, v = ln.split(":", 1)
            fm[k.strip().lower()] = v.strip().strip('"')
    for ln in lines:
        if ln.startswith("# "):
            title = ln[2:].strip()
            break
    return fm, fm.get("title") or title, parse_candidates(lines)


def parse_candidates(lines):
    """Extract K7 candidate-ledger rows from any markdown table whose rows start
    with candN. Header-driven; handles the four observed layouts:
      candidate|class|SHA|parity|p50 ms (author-side)|vs naive|receipt|why …
      cand_id|commit|p50_ms|speedup|parity|receipt|notes
      Candidate|Config/Tiling|p50 (ms)|Speedup|Parity|Commit|Receipt|Notes
      Candidate|Tile sizes|Grid|p50 (ms)|Speedup vs baseline|Status
    Baseline / Naive Baseline rows are skipped; duplicate cand ids (e.g. a
    results-summary table repeating the ledger) keep the first occurrence."""
    cands, seen = [], set()
    hdr = None
    for ln in lines:
        if not ln.strip().startswith("|"):
            hdr = None
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if not cells:
            continue
        if re.match(r"^:?-{2,}", cells[0]):          # separator row
            continue
        low0 = cells[0].lower()
        if "cand" in low0 and ("candidate" == low0 or "cand_id" == low0 or low0.startswith("candidate")):
            hdr = [c.lower() for c in cells]
            continue
        m = re.match(r"^`?cand(\d+)", low0)
        if not m:
            if hdr and low0 and "baseline" not in low0:
                pass                                  # non-cand data row (e.g. config sweep) — ignore
            continue
        cid = f"cand{int(m.group(1))}"
        if cid in seen:
            continue
        if hdr is None or len(hdr) < len(cells):
            hdr = (hdr or [])[:]
        row = {}
        for i, c in enumerate(cells):
            h = hdr[i] if hdr and i < len(hdr) else f"col{i}"
            row[h] = c
        def pick(*keys):
            for h, v in row.items():
                if any(k in h for k in keys):
                    return v
            return None
        time_ms = fnum(pick("p50"))
        speedup = fnum(pick("speedup", "vs naive"))
        if speedup is not None and speedup <= 0:
            speedup = None
        parity = pick("parity")
        if parity and len(parity) > 24:
            parity = parity[:24]
        note = " · ".join(x for x in (pick("config", "tiling", "tile"),
                                      pick("why", "note"), pick("status")) if x and x not in ("-", "N/A"))
        seen.add(cid)
        cands.append({
            "cid": cid, "n": int(m.group(1)),
            "time_ms": time_ms if (time_ms or 0) > 0 else None,
            "speedup": speedup, "parity": parity or None,
            "note": note[:140], "failed": time_ms is None and speedup is None,
        })
    cands.sort(key=lambda c: c["n"])
    return cands


def parse_tsv(path):
    rows = []
    try:
        lines = [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip()]
    except OSError:
        return rows
    if not lines:
        return rows
    hdr = [h.strip().lower() for h in lines[0].split("\t")]
    for ln in lines[1:]:
        rows.append(dict(zip(hdr, [c.strip() for c in ln.split("\t")])))
    return rows


def collect_records(kdir, arm="", branch=""):
    records, families = [], []
    for fam_dir in sorted(glob.glob(os.path.join(kdir, "*", LANE))):
        raw_fam = os.path.basename(os.path.dirname(fam_dir))   # on-disk dir → used for links
        fam = FAMILY_ALIAS.get(raw_fam, raw_fam)               # canonical slug → used for grouping
        if fam not in families:
            families.append(fam)
        # v-pages in the family dir (excludes retrospectives / program / log)
        pages = {}  # vnum -> (relpath from wiki/analyses/, fm, title, cands)
        for p in sorted(glob.glob(os.path.join(fam_dir, "*.md"))):
            b = os.path.basename(p)
            m = re.search(r"-v(\d+)[-.]", b)
            if not m or "retrospective" in b or b in ("program.md", "log.md"):
                continue
            fm, title, cands = page_meta(p)
            # repo-relative so the viewer can build an absolute GitHub blob URL on the arm's branch
            pages[int(m.group(1))] = (f"wiki/kernel_experiments/{raw_fam}/{LANE}/{b}", fm, title, cands)

        seen = set()
        for row in parse_tsv(os.path.join(fam_dir, "RESULTS.tsv")):
            rid = row.get("exp_id") or row.get("experiment_id") or ""
            m = re.search(r"v(\d+)", rid)
            if not m:
                continue
            vnum = int(m.group(1))
            seen.add(vnum)
            page = pages.get(vnum)
            time_ms = fnum(row.get("p50_ms")) or fnum(row.get("candidate_ms"))
            if time_ms is not None and time_ms <= 0:
                time_ms = None
            speedup = fnum(row.get("speedup"))
            if speedup is not None and speedup <= 0:
                speedup = None
            baseline = fnum(row.get("baseline_ms"))
            if baseline is None and time_ms is not None and speedup is not None:
                baseline = time_ms * speedup
            verdict = norm_verdict(row.get("verdict")) or norm_verdict(row.get("status"))
            if not verdict and page:
                verdict = norm_verdict(page[1].get("verdict")) or norm_verdict(page[1].get("status"))
            desc = row.get("description") or (page[2] if page else "") or rid
            records.append({
                "family": fam, "id": f"v{vnum:03d}", "vnum": vnum, "verdict": verdict,
                "time_ms": time_ms, "baseline_ms": baseline, "speedup": speedup,
                "tflops": fnum(row.get("tflops")), "util": norm_util(row.get("roofline_util")),
                "parity": (row.get("parity") or "").upper() or None,
                "cls": row.get("class") or row.get("intervention_class") or "",
                "desc": desc,
                "link": page[0] if page else f"wiki/kernel_experiments/{raw_fam}/{LANE}/RESULTS.tsv",
                "has_metric": speedup is not None or time_ms is not None,
                "cands": page[3] if page else [],
                "arm": arm, "branch": branch,
            })
        # pages with no TSV row yet → pending / no-metric
        for vnum, (link, fm, title, cands) in sorted(pages.items()):
            if vnum in seen:
                continue
            records.append({
                "family": fam, "id": f"v{vnum:03d}", "vnum": vnum,
                "verdict": norm_verdict(fm.get("verdict")) or norm_verdict(fm.get("status")) or "pending",
                "time_ms": None, "baseline_ms": None, "speedup": None,
                "tflops": None, "util": None, "parity": None,
                "cls": fm.get("intervention_class", ""),
                "desc": title or f"{fam} v{vnum:03d}", "link": link, "has_metric": False,
                "cands": cands,
                "arm": arm, "branch": branch,
            })
    records.sort(key=lambda r: (r["family"], r["vnum"]))
    return records, families


def rooflines(records, families):
    """Per-family roofline projected into every metric's units, derived from the
    receipt with the highest measured util (closest to the ceiling = most
    credible basis; families whose op-point changed mid-stream, e.g.
    mla-attention, make min/max across all receipts misleading):
      tflops ceiling = tflops / util
      speedup ceiling = speedup / util   (max achievable vs naive)
      time_ms floor  = p50 * util        (latency at 100% of roofline)
    """
    out = {}
    for fam in families:
        rs = [r for r in records if r["family"] == fam and r["util"]]
        if not rs:
            out[fam] = None
            continue
        b = max(rs, key=lambda r: r["util"])
        u = b["util"] / 100.0
        out[fam] = {
            "tflops":  round(b["tflops"] / u, 1) if b["tflops"] else None,
            "speedup": round(b["speedup"] / u, 2) if b["speedup"] else None,
            "time_ms": round(b["time_ms"] * u, 3) if b["time_ms"] else None,
            "src": b["id"], "util": round(b["util"], 1),
        }
    return out


# ---------------------------------------------------------------- HTML template

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Pallas kernel explorer</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  :root{--bg:#fafafa;--panel:#fff;--text:#222;--muted:#666;--label:#888;--border:#e5e5e5;--subt:#999}
  body.dark{--bg:#1b1b1b;--panel:#262626;--text:#e8e8e8;--muted:#9aa0a6;--label:#9aa0a6;--border:#3a3a3a;--subt:#888}
  body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0;background:var(--bg);color:var(--text)}
  header{padding:14px 20px 6px}
  h1{font-size:18px;margin:0 0 2px} .sub{color:var(--muted);font-size:12px}
  #controls{display:flex;flex-wrap:wrap;gap:18px;padding:10px 20px;background:var(--panel);border-bottom:1px solid var(--border);align-items:center}
  .group{display:flex;gap:10px;align-items:center;font-size:13px}
  .group b{font-size:11px;color:var(--label);text-transform:uppercase;letter-spacing:.04em;margin-right:2px}
  label{display:inline-flex;gap:4px;align-items:center;cursor:pointer;user-select:none}
  select{background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:5px;padding:3px 8px;font-size:13px}
  .sw{width:11px;height:11px;border-radius:2px;display:inline-block}
  #chart{width:100%;height:72vh}
  .hint{font-size:11px;color:var(--subt);padding:4px 20px}
  #theme{margin-left:auto;cursor:pointer;background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:5px;padding:3px 11px;font-size:12px}
  #legendv{display:flex;gap:12px;padding:2px 20px 6px;font-size:11px;color:var(--muted);flex-wrap:wrap}
  #legendv span{display:inline-flex;gap:4px;align-items:center}
</style>
</head>
<body>
<header>
  <h1 id="title">Pallas kernel explorer</h1>
  <div class="sub" id="subnote">__SUBNOTE__</div>
</header>
<div id="controls"></div>
<div id="legendv"></div>
<div class="hint" id="count"></div>
<div id="chart"></div>
<script>
const DATA = __DATA__;
const FAMILIES = __FAMILIES__;
const ARMS = __ARMS__;             // [[key,label,branch], …] one campaign run per LLM
const GHREPO = __GHREPO__;         // "owner/repo" for absolute blob links
const ROOFLINE = __ROOFLINE__;     // "arm|family" -> implied ceiling per metric, or null
const MK = __MK__;                 // family -> [problem, MK5 speedup|null, isArtifact]
const ARMKEYS = ARMS.map(a=>a[0]);
const ARMLABEL={}, ARMBRANCH={}, ARMCOLORS={};
const ARMPALETTE=["#e67e22","#8e44ad","#2e86de","#27ae60","#c0392b"];
ARMS.forEach((a,i)=>{ARMLABEL[a[0]]=a[1];ARMBRANCH[a[0]]=a[2];ARMCOLORS[a[0]]=ARMPALETTE[i%ARMPALETTE.length];});
const FAMDASH = {};
const DASHES = ["solid","dash","dot","dashdot","longdash","longdashdot"];
const FAMCOLORS = {};
const PALETTE = ["#4c78a8","#f58518","#54a24b","#b279a2","#e45756","#72b7b2","#eeca3b","#9d755d"];
FAMILIES.forEach((f,i)=>{FAMCOLORS[f]=PALETTE[i%PALETTE.length];FAMDASH[f]=DASHES[i%DASHES.length];});
const VCOLOR = {supported:"#2e7d32", partial:"#f9a825", refuted:"#c62828", invalid:"#8e24aa",
                inconclusive:"#757575", baseline:"#1565c0", completed:"#1565c0", pending:"#90a4ae", "":"#90a4ae"};
const VSYM   = {supported:"circle", partial:"diamond", refuted:"x", invalid:"x-open",
                inconclusive:"square", baseline:"star", completed:"circle-open", pending:"square-open", "":"square-open"};
const FAIL = {refuted:1, invalid:1, inconclusive:1};

// ---- state + URL param ----
function kernelFromURL(){
  const q = new URLSearchParams(location.search).get("kernel");
  if(q) return q;
  const h = location.hash.match(/kernel=([\w.-]+)/);
  return h ? h[1] : null;
}
function llmFromURL(){
  const q = new URLSearchParams(location.search).get("llm");
  if(q) return q;
  const h = location.hash.match(/llm=([\w.,-]+)/);
  return h ? h[1] : null;
}
// llm= accepts "all" or a comma list of arm keys; unknown keys are dropped, empty falls back to all
function llmsFromURL(){
  const raw = llmFromURL();
  if(!raw || raw==="all") return ARMKEYS.slice();
  const keep = raw.split(",").map(s=>s.trim()).filter(k=>ARMKEYS.includes(k));
  return keep.length ? keep : ARMKEYS.slice();
}
const state = {
  kernel: (()=>{ const k=kernelFromURL(); return (k && (FAMILIES.includes(k)||k==="all")) ? k : "all"; })(),
  llms: llmsFromURL(),          // array of enabled arm keys
  showMK: true,
  metric: "speedup",
  showFailed: true,
  showNoMetric: true,
  showCands: true,
  showRoofline: true,
  dark: false,
};
function syncURL(){
  const u = new URL(location.href);
  u.searchParams.set("kernel", state.kernel);
  u.searchParams.set("llm", state.llms.length===ARMKEYS.length ? "all" : state.llms.join(","));
  try{ history.replaceState(null,"",u); }catch(e){ /* file:// in some browsers */ }
}

// ---- controls ----
const C = document.getElementById("controls");
function group(title){const g=document.createElement("div"); g.className="group"; const t=document.createElement("b"); t.textContent=title; g.appendChild(t); return g;}
function chk(on,label){
  const l=document.createElement("label");
  const b=document.createElement("input"); b.type="checkbox"; b.checked=on;
  l.appendChild(b); l.appendChild(document.createTextNode(label));
  return {l,b};
}

const gK=group("Kernel");
const sel=document.createElement("select");
[["all","— all kernels —"]].concat(FAMILIES.map(f=>[f,f])).forEach(([v,lab])=>{
  const o=document.createElement("option"); o.value=v; o.textContent=lab; sel.appendChild(o);
});
sel.value=state.kernel;
sel.onchange=()=>{ state.kernel=sel.value; syncURL(); render(); };
gK.appendChild(sel);
C.appendChild(gK);

const gL=group("LLM");
ARMS.forEach(([key,label])=>{
  const {l,b}=chk(state.llms.includes(key),label);
  // colour the label to match the arm's series colour so legend and control agree
  l.style.color=ARMCOLORS[key]; l.style.fontWeight="600";
  b.onchange=()=>{
    if(b.checked){ if(!state.llms.includes(key)) state.llms.push(key); }
    else { state.llms=state.llms.filter(k=>k!==key); }
    // never leave zero arms selected — re-check the box the user just cleared
    if(!state.llms.length){ state.llms=[key]; b.checked=true; }
    state.llms.sort((x,y)=>ARMKEYS.indexOf(x)-ARMKEYS.indexOf(y));
    syncURL(); render();
  };
  gL.appendChild(l);
});
C.appendChild(gL);

const gMetric=group("Metric");
[["speedup","speedup ×"],["time_ms","p50 ms"],["tflops","TFLOP/s"]].forEach(([k,lab])=>{
  const l=document.createElement("label");
  const b=document.createElement("input"); b.type="radio"; b.name="metric"; b.value=k; b.checked=(state.metric===k);
  b.onchange=()=>{ if(b.checked){ state.metric=k; render(); } };
  l.appendChild(b); l.appendChild(document.createTextNode(lab));
  gMetric.appendChild(l);
});
C.appendChild(gMetric);

// Candidates get their own group: it is the single biggest change to how busy the plot looks,
// so it should not be buried among the four "Show" toggles.
const gCand=group("Candidates");
let candBox=null, candHint=null;
{const {l,b}=chk(state.showCands,"show K7 candidates");
 candBox=b;
 b.onchange=()=>{state.showCands=b.checked;render();};
 gCand.appendChild(l);
 candHint=document.createElement("span");
 candHint.style.cssText="font-size:10px;color:var(--subt);margin-left:2px";
 gCand.appendChild(candHint);}
C.appendChild(gCand);

const gShow=group("Show");
{const {l,b}=chk(state.showFailed,"refuted / invalid / inconcl."); b.onchange=()=>{state.showFailed=b.checked;render();}; gShow.appendChild(l);}
{const {l,b}=chk(state.showNoMetric,"pending / no-metric"); b.onchange=()=>{state.showNoMetric=b.checked;render();}; gShow.appendChild(l);}
{const {l,b}=chk(state.showRoofline,"roofline (rescales y)"); b.onchange=()=>{state.showRoofline=b.checked;render();}; gShow.appendChild(l);}
{const {l,b}=chk(state.showMK,"MaxKernel best (MK⁵)"); b.onchange=()=>{state.showMK=b.checked;render();}; gShow.appendChild(l);}
C.appendChild(gShow);

const themeBtn=document.createElement("button");
themeBtn.id="theme"; themeBtn.textContent="🌙 Dark";
themeBtn.onclick=()=>{ state.dark=!state.dark; document.body.classList.toggle("dark",state.dark);
  themeBtn.textContent=state.dark?"☀ Light":"🌙 Dark"; render(); };
C.appendChild(themeBtn);

// verdict color legend
{
  const lv=document.getElementById("legendv");
  // COLOUR = model
  {const s=document.createElement("span"); s.innerHTML="<b>colour = model:</b>"; lv.appendChild(s);}
  ARMS.forEach(([key,label])=>{
    const s=document.createElement("span");
    s.innerHTML=`<i class="sw" style="background:${ARMCOLORS[key]}"></i>${label}`;
    lv.appendChild(s);
  });
  // SHAPE = experiment verdict
  {const s=document.createElement("span"); s.innerHTML="&nbsp;&nbsp;<b>shape = verdict:</b>"; lv.appendChild(s);}
  Object.entries({"●":"supported","◆":"partial","✕":"refuted","✖":"invalid",
                  "■":"inconclusive","□":"pending/no-metric","○":"candidate (ran)",
                  "✗":"candidate (failed)"}).forEach(([glyph,lab])=>{
    const s=document.createElement("span");
    s.innerHTML=`<span style="font-size:13px;line-height:1">${glyph}</span>${lab}`;
    lv.appendChild(s);
  });
  const s=document.createElement("span");
  s.innerHTML=`<i class="sw" style="background:transparent;border:1px dashed #888"></i>small hollow = candidate (per-experiment ledger); dotted = roofline in the current metric's units (ceiling × / floor ms / ceiling TFLOP/s); black dotted = MaxKernel MK⁵ best (speedup view only), <span style="color:#b0399a">magenta dash-dot = MK cell flagged as an artifact</span>`;
  lv.appendChild(s);
}

// ---- metric config + traces ----
const METRIC = {
  speedup:{title:"speedup vs naive baseline (×)", better:"max", fmt:v=>v.toFixed(3)+"×", ref:1.0, refLabel:"naive baseline 1.0×"},
  time_ms:{title:"p50 latency (ms)", better:"min", fmt:v=>v.toFixed(3)+" ms"},
  tflops:{title:"TFLOP/s", better:"max", fmt:v=>v.toFixed(1)},
};
// Candidates carry p50 and speedup only — the ledger has no per-candidate TFLOP/s — so the
// candidate layer is genuinely unavailable on that metric rather than merely switched off.
function CANDS_OK(){ return state.metric!=="tflops"; }
function visible(d){
  if(state.kernel!=="all" && d.family!==state.kernel) return false;
  if(!state.llms.includes(d.arm)) return false;
  if(!d.has_metric) return state.showNoMetric;
  if(FAIL[d.verdict] && !state.showFailed) return false;
  return true;
}
function inScope(d){
  return (state.kernel==="all"||d.family===state.kernel) && state.llms.includes(d.arm);
}
function hover(d, M){
  const val = d[state.metric];
  const extra = [
    val!==null&&val!==undefined ? METRIC[state.metric].title.split(" (")[0]+": "+M.fmt(val) : "no metric",
    d.time_ms!==null&&state.metric!=="time_ms" ? "p50 "+d.time_ms.toFixed(3)+" ms" : null,
    d.util!==null&&d.util!==undefined ? "util "+d.util.toFixed(1)+"% of roofline" : null,
    d.parity ? "parity "+d.parity : null,
  ].filter(Boolean).join(" · ");
  return `<b>${d.family} ${d.id}</b> · ${ARMLABEL[d.arm]||d.arm} · ${d.verdict||"—"}`
       + `<br>${(d.desc||"").slice(0,90)}`
       + `<br>${extra}<br><i>click → open page on ${d.branch||"?"}</i>`;
}
function candHover(d, c, M){
  const v = c[state.metric];
  const extra = [
    v!==null&&v!==undefined ? METRIC[state.metric].fmt(v) : "no metric (failed before timing)",
    c.time_ms!==null&&state.metric!=="time_ms"&&c.time_ms!==undefined ? "p50 "+c.time_ms.toFixed(3)+" ms" : null,
    c.parity ? "parity "+c.parity : null,
  ].filter(Boolean).join(" · ");
  return `<b>${d.family} ${d.id} · ${c.cid}</b>`
       + `<br>${(c.note||"").slice(0,90)||"—"}`
       + `<br>${extra}<br><i>click → open page</i>`;
}
function frontier(rows, F, better){
  const pts = rows.filter(d=>d[F]!==null && d[F]!==undefined && d.verdict!=="invalid")
                  .sort((a,b)=>a.vnum-b.vnum);
  let m=null, xs=[], ys=[];
  for(const d of pts){
    if(m===null || (better==="max" ? d[F]>m : d[F]<m)) m=d[F];
    xs.push(d.vnum); ys.push(m);
  }
  return {xs,ys};
}
function buildTraces(){
  const M=METRIC[state.metric], F=state.metric, traces=[];
  const fams = state.kernel==="all" ? FAMILIES : [state.kernel];
  const arms = state.llms;
  // "single" = one kernel AND exactly one LLM: the detail view (verdict-colored + candidates).
  // Otherwise a series is a (family, arm) pair, colored by whichever axis is being compared.
  const single = state.kernel!=="all" && arms.length===1;
  const byArm = arms.length>1 && state.kernel!=="all";   // comparing LLMs on one kernel
  for(const fam of fams){
  for(const arm of arms){
    const seriesColor = byArm ? ARMCOLORS[arm] : FAMCOLORS[fam];
    const seriesName = state.kernel==="all"
        ? (arms.length>1 ? `${fam} · ${ARMLABEL[arm]}` : fam)
        : (ARMLABEL[arm]||arm);
    const gid = fam+"|"+arm;
    const rows = DATA.filter(d=>d.family===fam && d.arm===arm && visible(d));
    if(!rows.length) continue;
    const pts = rows.filter(d=>d[F]!==null && d[F]!==undefined);
    if(pts.length) traces.push({
      x:pts.map(d=>d.vnum), y:pts.map(d=>d[F]), customdata:pts.map(d=>[d.link,d.branch]),
      text:pts.map(d=>hover(d,M)), hovertemplate:"%{text}<extra></extra>",
      mode:"markers", name:seriesName, legendgroup:gid,
      // ENCODING (single rule everywhere): COLOUR = model, SHAPE = experiment verdict.
      marker:{
        color: ARMCOLORS[arm],
        size:10, symbol:pts.map(d=>VSYM[d.verdict]||"square-open"),
        line:{width:0},
      },
    });
    const fr=frontier(DATA.filter(d=>d.family===fam && d.arm===arm), F, M.better);
    if(fr.xs.length>1) traces.push({
      x:fr.xs, y:fr.ys, mode:"lines", legendgroup:gid, showlegend:false,
      // colour still = model; when many families share the plot, the dash pattern (NOT colour)
      // is what separates them, so the colour axis stays exclusively about the model.
      line:{color:ARMCOLORS[arm], width:2.2, shape:"hv",
            dash: state.kernel==="all" ? FAMDASH[fam] : "solid"},
      hoverinfo:"skip", opacity:0.85,
    });
    if(state.showNoMetric){
      const cpts = rows.filter(d=>d[F]===null || d[F]===undefined);
      if(cpts.length) traces.push({
        x:cpts.map(d=>d.vnum), y:cpts.map(()=>0), customdata:cpts.map(d=>[d.link,d.branch]),
        text:cpts.map(d=>hover(d,M)), hovertemplate:"%{text}<extra></extra>",
        mode:"markers", name:seriesName+" · no metric", legendgroup:gid, showlegend:false,
        marker:{color: ARMCOLORS[arm], size:8,
                symbol:cpts.map(d=>VSYM[d.verdict]||"square-open"), opacity:0.5},
      });
    }
    // candidates within each experiment: sequenced steps at vnum + 0.1·(k-1)
    // (cand1 → v.0, cand2 → v.1, …) with a thin step line showing the
    // within-experiment progression; one trace per experiment so lines
    // never connect across experiments.
    if(state.showCands && CANDS_OK()){
      for(const d of rows){
        const cands=(d.cands||[]);
        if(!cands.length) continue;
        const n=cands.length;
        const step = Math.min(0.1, 0.85/Math.max(n,1));
        const cx=[], cy=[], ct=[], cl=[], cc=[], cs=[];
        cands.forEach((c,i)=>{
          const v = c[F];
          cx.push(d.vnum + i*step);
          cy.push(v!==null&&v!==undefined ? v : 0);
          ct.push(candHover(d,c,M));
          cl.push([d.link,d.branch]);
          const failed = c.failed || v===null || v===undefined;
          cc.push(ARMCOLORS[arm]);                        // colour = model, no exceptions
          cs.push(failed ? "x-thin-open" : "circle-open"); // shape carries failed-vs-ran
        });
        traces.push({
          x:cx, y:cy, customdata:cl, text:ct, hovertemplate:"%{text}<extra></extra>",
          mode: n>1 ? "lines+markers" : "markers",
          name:seriesName+" · "+d.id+" candidates", legendgroup:gid, showlegend:false,
          line:{color: ARMCOLORS[arm], width:1, shape:"hv", dash:"solid"},
          opacity:0.75,
          marker:{color:cc, size:6.5, symbol:cs, line:{width:1.3}},
        });
      }
    }
  }
  }
  return traces;
}
function theme(){ return state.dark
  ? {paper:"#262626",plot:"#202020",font:"#e8e8e8",grid:"#333",line:"#888"}
  : {paper:"#fff",plot:"#fff",font:"#222",grid:"#eee",line:"#555"}; }
function render(){
  const M=METRIC[state.metric], T=theme();
  const traces=buildTraces();
  const shapes=[], annotations=[];
  if(M.ref!==undefined){
    shapes.push({type:"line",xref:"paper",x0:0,x1:1,yref:"y",y0:M.ref,y1:M.ref,
                 line:{color:T.line,width:1,dash:"dash"}});
    annotations.push({xref:"paper",x:0.005,yref:"y",y:M.ref,yanchor:"bottom",showarrow:false,
                      text:M.refLabel,font:{size:10,color:T.line}});
  }
  // roofline: dotted per-family line on EVERY metric view, in that metric's
  // units — ceiling speedup (speedup/util), floor latency (p50*util), or
  // ceiling TFLOP/s (tflops/util); all from the family's highest-util receipt.
  // NB: Plotly shapes are NOT included in autorange, so we pin the y-range
  // explicitly to keep the line on-screen.
  const fams = state.kernel==="all" ? FAMILIES : [state.kernel];
  const rarms = state.llms;
  let ytop = 0;
  for(const d of DATA){
    const v = d[state.metric];
    if(inScope(d) && v!==null && v!==undefined && v>ytop) ytop=v;
  }
  const RLABEL = {speedup:v=>`roofline ceiling ≈ ${v}×`,
                  time_ms:v=>`roofline floor ≈ ${v} ms`,
                  tflops:v=>`implied roofline ≈ ${v.toLocaleString()} TFLOP/s`};
  for(const fam of fams){
    if(!state.showRoofline) break;
    for(const arm of rarms){
      const rl=ROOFLINE[arm+"|"+fam]; if(!rl) continue;
      const val=rl[state.metric]; if(val==null) continue;
      if(state.metric!=="time_ms" && val>ytop) ytop=val;
      const col = state.kernel==="all" ? FAMCOLORS[fam]
                : (rarms.length>1 ? ARMCOLORS[arm] : T.line);
      shapes.push({type:"line",xref:"paper",x0:0,x1:1,yref:"y",y0:val,y1:val,
                   line:{color:col,width:1.3,dash:"dot"},opacity:0.8});
      const tag = [state.kernel==="all"?fam:null, rarms.length>1?ARMLABEL[arm]:null]
                    .filter(Boolean).join(" · ");
      annotations.push({xref:"paper",x:0.995,xanchor:"right",yref:"y",y:val,
                        yanchor:state.metric==="time_ms"?"top":"bottom",showarrow:false,
                        text:`${tag?tag+" · ":""}${RLABEL[state.metric](val)} (${rl.src} @ ${rl.util}% util)`,
                        font:{size:10,color:col}});
    }
  }
  // MaxKernel published best (MK⁵) — the external reference bar. Speedup-only: it has no meaning
  // on the ms or TFLOP/s axes, so it is drawn on the speedup metric only.
  if(state.showMK && state.metric==="speedup"){
    const dataTop = ytop;                     // before MK, so artifacts can't silently rescale
    const offscale = [];
    for(const fam of fams){
      const mk=MK[fam]; if(!mk) continue;
      const [prob,val,artifact]=mk;
      if(val==null){ offscale.push(`MK⁵ ${prob} FAILED`); continue; }
      // A flagged artifact is not a bar to beat, so it never gets to rescale the y-axis for the
      // real data (MK 30k claims 26.86× against data at 0.23×). Off-scale ones become a note.
      if(artifact && val > dataTop*1.15){ offscale.push(`MK⁵ ${prob} ${val.toFixed(2)}× ⚠`); continue; }
      if(!artifact && val>ytop) ytop=val;
      const col = artifact ? "#b0399a" : (state.dark ? "#e0e0e0" : "#111");
      shapes.push({type:"line",xref:"paper",x0:0,x1:1,yref:"y",y0:val,y1:val,
                   line:{color:col,width:1.5,dash:artifact?"dashdot":"dot"},opacity:0.9});
      annotations.push({xref:"paper",x:0.5,xanchor:"center",yref:"y",y:val,yanchor:"bottom",
        showarrow:false,
        text:`${state.kernel==="all"?fam+" · ":""}MK⁵ ${prob} best ${val.toFixed(2)}×`
             +(artifact?" ⚠ flagged artifact — not a real bar":""),
        font:{size:10,color:col}});
    }
    if(offscale.length) annotations.push({xref:"paper",x:0.005,xanchor:"left",yref:"paper",y:1.0,
      yanchor:"top",showarrow:false,align:"left",
      text:"off-scale / unusable MK: "+offscale.join(", "),
      font:{size:9,color:"#b0399a"}});
  }
  const yrange = ytop>0 ? [0, ytop*1.08] : undefined;
  let xmax=5;
  for(const d of DATA) if(inScope(d) && d.vnum>xmax) xmax=d.vnum;
  Plotly.react("chart",traces,{
    margin:{l:62,r:20,t:10,b:45}, hovermode:"closest",
    showlegend:(state.kernel==="all"||state.llms.length>1),
    font:{color:T.font}, legend:{orientation:"h",y:-0.13,font:{size:11,color:T.font}},
    xaxis:{title:"experiment vNNN — candidates step at v.0, v.1, v.2 … (thin step line = within-experiment progression)",
           range:[0.4,xmax+1.0],dtick:1,gridcolor:T.grid,zerolinecolor:T.grid},
    yaxis:Object.assign({title:M.title,gridcolor:T.grid,zerolinecolor:T.grid},
                        yrange?{range:yrange}:{rangemode:"tozero"}),
    shapes, annotations, plot_bgcolor:T.plot, paper_bgcolor:T.paper,
  },{responsive:true,displaylogo:false});
  // header + count
  const scope = DATA.filter(inScope);
  const shown = scope.filter(visible);
  const candsOn = state.showCands && CANDS_OK();
  const nc = shown.reduce((a,d)=>a+((d.cands&&candsOn)?d.cands.length:0),0);
  if(candBox){
    candBox.disabled = !CANDS_OK();
    candBox.parentElement.style.opacity = CANDS_OK() ? "1" : "0.45";
    candHint.textContent = CANDS_OK() ? "" : "n/a on TFLOP/s (ledger has no per-candidate TFLOP/s)";
  }
  const armTag = state.llms.length===ARMKEYS.length ? "all LLMs"
               : state.llms.map(k=>ARMLABEL[k]||k).join(" vs ");
  document.getElementById("count").textContent=
    `${shown.length} of ${scope.length} experiments shown` + (candsOn?` · ${nc} ledger candidates`:"");
  document.getElementById("title").textContent =
    `Pallas kernel explorer — ${state.kernel==="all"?"all families":state.kernel} · ${armTag}`;
  document.title = `Pallas kernels — ${state.kernel} · ${armTag}`;
  if(state.kernel!=="all"){
    // per-kernel: one frontier line per arm in scope, so the comparison is explicit
    const parts=[];
    for(const arm of state.llms){
      const rs=scope.filter(d=>d.arm===arm && d.speedup!==null && d.verdict!=="invalid");
      if(!rs.length) continue;
      const best=rs.reduce((a,d)=>(!a||d.speedup>a.speedup)?d:a,null);
      parts.push(`${ARMLABEL[arm]||arm}: ${best.id} ${best.speedup.toFixed(3)}×`
                 +(best.time_ms!==null?` (${best.time_ms.toFixed(3)} ms)`:""));
    }
    document.getElementById("subnote").textContent =
      parts.length ? "frontier — "+parts.join("  ·  ") : "no measured frontier yet";
  } else {
    document.getElementById("subnote").textContent = "__SUBNOTE__";
  }
}
// Links resolve to the file on the arm's OWN branch — each LLM ran on its own campaign branch,
// and none of this content is on main, so a blob/main URL would 404.
function ghBlob(rel, branch){
  if(GHREPO && branch) return `https://github.com/${GHREPO}/blob/${branch}/${rel}`;
  return new URL(rel, location.href).href;
}
Plotly.newPlot("chart",[],{}).then(()=>{
  syncURL(); render();
  document.getElementById("chart").on("plotly_click",ev=>{
    const p=ev.points&&ev.points[0];
    if(p&&p.customdata) window.open(ghBlob(p.customdata[0],p.customdata[1]),"_blank");
  });
});
</script>
</body>
</html>
"""


def all_rooflines(records, arms):
    """Rooflines are per (arm, family) — each arm measured its own op-point on its own rig,
    so one family's ceiling is NOT shared across arms. Keyed "arm|family" for the viewer."""
    out = {}
    for key, _label, _branch in arms:
        recs = [r for r in records if r["arm"] == key]
        fams = sorted({r["family"] for r in recs})
        for fam, val in rooflines(recs, fams).items():
            out[f"{key}|{fam}"] = val
    return out


def build_explorer(records, families, arms):
    n_sup = sum(1 for r in records if r["verdict"] == "supported")
    n_cand = sum(len(r["cands"]) for r in records)
    per_arm = " · ".join(f"{label} {sum(1 for r in records if r['arm']==k)}"
                         for k, label, _b in arms)
    subnote = (f"{len(records)} experiments / {n_cand} ledger candidates across "
               f"{len(families)} kernel families, {len(arms)} LLM arms ({n_sup} supported) · "
               f"{per_arm} · big points = experiments (verdict-colored when one kernel + one LLM "
               f"is selected), small hollow = K7 candidates · step lines = running frontier · "
               f"select via the dropdowns or ?kernel=<slug>&llm=<arm>")
    html = (HTML
            .replace("__DATA__", json.dumps(records))
            .replace("__FAMILIES__", json.dumps(families))
            .replace("__ARMS__", json.dumps([list(a) for a in arms]))
            .replace("__GHREPO__", json.dumps(gh_repo()))
            .replace("__MK__", json.dumps({k:[v[0],v[1],v[2]] for k,v in MK_BEST.items()}))
            .replace("__ROOFLINE__", json.dumps(all_rooflines(records, arms)))
            .replace("__SUBNOTE__", subnote))
    os.makedirs(OUTDIR, exist_ok=True)
    json.dump(records, open(os.path.join(OUTDIR, "kernel_data.json"), "w"), indent=0)
    open(os.path.join(OUTDIR, "kernel-explorer.html"), "w").write(html)


def summarize(records, families, arms):
    n_cand = sum(len(r["cands"]) for r in records)
    print(f"extracted {len(records)} experiments ({n_cand} ledger candidates) across "
          f"{len(families)} families and {len(arms)} LLM arms")
    rl = all_rooflines(records, arms)
    for key, label, branch in arms:
        recs = [r for r in records if r["arm"] == key]
        fams = sorted({r["family"] for r in recs})
        print(f"\n  {label}  [{branch}]  {len(recs)} exp / {len(fams)} families")
        for fam in fams:
            rs = [r for r in recs if r["family"] == fam]
            best = max((r["speedup"] for r in rs if r["speedup"] is not None), default=None)
            line = (f"    {fam}: {len(rs)} exp, {sum(len(r['cands']) for r in rs)} cands, "
                    f"{sum(1 for r in rs if r['verdict']=='supported')} supported")
            if best is not None:
                line += f", frontier {best:.3f}x"
            r = rl.get(f"{key}|{fam}")
            if r and r.get("speedup"):
                line += f", roofline ceil {r['speedup']}x @ {r['util']}% util ({r['src']})"
            print(line)


if __name__ == "__main__":
    arms, records, families = parse_arms(), [], []
    resolved = []
    for key, label, branch in arms:
        ref = resolve_ref(branch)
        if not ref:
            print(f"  ! {label}: branch {branch} not found — arm skipped")
            continue
        dest = os.path.join(CACHE, key)
        if not stage_arm(ref, dest):
            print(f"  ! {label}: could not stage {ref} — arm skipped")
            continue
        recs, fams = collect_records(os.path.join(dest, "wiki", "kernel_experiments"),
                                     arm=key, branch=branch)
        print(f"  staged {label}: {ref} → {len(recs)} experiments, {len(fams)} families")
        records += recs
        families += [f for f in fams if f not in families]
        resolved.append((key, label, branch))
    if not records:
        raise SystemExit("no arm produced any records — check the branch names in DEFAULT_ARMS")
    families.sort()
    records.sort(key=lambda r: (r["family"], r["arm"], r["vnum"]))
    build_explorer(records, families, resolved)
    summarize(records, families, resolved)
    print(f"\nwrote {os.path.join(OUTDIR, 'kernel-explorer.html')}")
    print(f"view: python3 -m http.server 8000 --directory {OUTDIR}  →  "
          "http://localhost:8000/kernel-explorer.html?kernel=<slug>&llm=<arm>")
