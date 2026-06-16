#!/usr/bin/env python3
"""Build the interactive Qwen3 MFU/TPS experiment explorer.

Re-run this after new experiments land:

    python wiki/analyses/qwen3/build_explorer.py

Outputs (next to this script):
  - mfu_data.json     : the extracted per-experiment data source (diffable)
  - mfu-explorer.html : self-contained interactive viewer (data embedded,
                        opens directly via file:// — no server needed)

Data source design: the HTML embeds mfu_data.json at build time, so updating is
a one-command re-run. Edit mfu_data.json by hand if you ever need to override a
point; then run with --from-json to rebuild the HTML without re-extracting.
"""
import re, glob, os, json, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))

LANES = ["cc", "ag", "cx", "cc5"]
LANE_NAME = {"cc": "cc (Claude)", "ag": "ag (Antigravity)", "cx": "cx (Codex)", "cc5": "cc5 (Fable5)"}
COLORS = {"cc": "#1f77b4", "ag": "#ff7f0e", "cx": "#2ca02c", "cc5": "#d62728"}
MAXTEXT = {"mfu": {"2048": 38.0, "8192": 45.3}, "tps": {"2048": 7116, "8192": 6942}}
CX_ADJ = {}                            # cx reports its causal MFU directly (no ÷ adjustment);
                                       # the causal value is already on the shared lane basis.
                                       # Its inflated "MaxText-style" (non-causal) figure is
                                       # discarded by the VERIFIED clamp (e.g. 49.2%→43.2% @8k).
VERIFIED = {"cc": {2048: 35.8, 8192: 34.8}, "ag": {2048: 33.0, 8192: 30.6},
            "cx": {2048: 47.3, 8192: 43.2}, "cc5": {2048: 40.5, 8192: 39.9}}
MT_CONSTS = {45.3, 45.0, 44.9, 44.6, 38.0, 37.7, 36.8}
MT_TPS = {6942, 7116, 6953, 6883, 6601}

mfu_pats = [re.compile(r"approx MFU\s*[:=]\s*([0-9]{1,2}\.[0-9])", re.I),
            re.compile(r"([0-9]{1,2}\.[0-9])\s*%\s*MFU", re.I),
            re.compile(r"MFU[:\s*]*\**\s*([0-9]{1,2}\.[0-9])\s*%", re.I),
            re.compile(r"MFU[^0-9%]{0,14}([0-9]{1,2}\.[0-9])\s*%", re.I)]
tps_pat = re.compile(r"([0-9],?[0-9]{3})\s*tok/s/chip", re.I)
verdict_pat = re.compile(r"^verdict:\s*([^\n]+)", re.I | re.M)
status_pat = re.compile(r"^status:\s*([^\n]+)", re.I | re.M)


def norm_verdict(txt):
    # Lanes are inconsistent: some use `verdict:`, most of cx uses `status:`. Prefer
    # an explicit verdict; otherwise normalize the status string to a canonical verdict.
    m = verdict_pat.search(txt) or status_pat.search(txt)
    if not m:
        return ""
    s = m.group(1).strip().lower()
    if "supported" in s or "confirmed" in s: return "supported"
    if "invalid" in s or "failed" in s:      return "invalid"        # invalid wins over refuted
    if "refuted" in s or "tie" in s:         return "refuted"
    if "inconclusive" in s:                  return "inconclusive"
    if "baseline" in s:                      return "baseline"
    if any(k in s for k in ("completed", "complete", "filed")): return "completed"
    if any(k in s for k in ("running", "pending", "open", "tbd")): return "pending"
    return ""


def vkey(fn):
    m = re.search(r"v(\d{1,3})", fn); n = int(m.group(1)) if m else 999
    s = re.search(r"v\d{1,3}([a-z]?)", fn); return (n, s.group(1) if s else "", fn)


def seqlen(fn, txt):
    f = fn.lower()
    if any(k in f for k in ["8192", "s8k", "seq8k", "-8k", "8k-", "8kbase", "8kbs"]): return 8192
    if any(k in f for k in ["2048", "s2k", "seq2k", "-2k", "2k-", "2kbase", "2kbs", "2kctl",
                            "2kunroll", "2kscan", "2kio", "2kce", "2kbatch", "batch1", "batch2"]): return 2048
    if "2k" in f: return 2048
    if "8k" in f: return 8192
    c8, c2 = txt.count("8192"), txt.count("2048")
    return 8192 if (c8 > c2 and c8 > 0) else (2048 if c2 > 0 else None)


def modal(cands):
    from collections import Counter
    if not cands: return None
    cnt = Counter(cands); mx = cnt.most_common(1)[0][1]
    return max(m for m in cnt if cnt[m] == mx)


def extract():
    records = []
    for L in LANES:
        d = f"wiki/experiments/qwen3_{L}_autoresearch_optimization/jax/experiments"
        files = sorted(glob.glob(os.path.join(d, "*.md")), key=lambda f: vkey(os.path.basename(f)))
        order = 0
        for f in files:
            txt = open(f, encoding="utf-8", errors="ignore").read()
            bn = os.path.basename(f)[:-3]
            order += 1
            sl = seqlen(bn, txt)
            cands = [float(m) for p in mfu_pats for m in p.findall(txt)
                     if 5.0 <= float(m) <= 52.0 and float(m) not in MT_CONSTS]
            mfu = max(cands) if (L == "cx" and cands) else modal(cands)
            adj = mfu
            if mfu is not None and L == "cx" and sl in CX_ADJ:
                adj = round(mfu / CX_ADJ[sl], 1)
            if adj is not None and sl in VERIFIED.get(L, {}):
                adj = min(adj, VERIFIED[L][sl])
            tcands = [int(m.replace(",", "")) for m in tps_pat.findall(txt)
                      if 1000 <= int(m.replace(",", "")) <= 15000 and int(m.replace(",", "")) not in MT_TPS]
            tps = max(tcands) if tcands else None
            vd = norm_verdict(txt)
            records.append({
                "lane": L, "slug": bn, "vnum": vkey(bn)[0], "order": order,
                "seq": sl, "mfu": adj, "tps": tps, "verdict": vd,
                "success": vd == "supported",
                "maxtext": ("maxtext" in bn.lower()) or ("maxtext" in txt.lower()),
                "has_metric": (adj is not None) or (tps is not None),
                "link": f"../../experiments/qwen3_{L}_autoresearch_optimization/jax/experiments/{bn}.md",
            })
    return records


HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Qwen3-8B v6e-8 — experiment explorer</title>
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
  .sw{width:11px;height:11px;border-radius:2px;display:inline-block}
  #chart{width:100%;height:74vh}
  .hint{font-size:11px;color:var(--subt);padding:4px 20px}
  #theme{margin-left:auto;cursor:pointer;background:var(--panel);color:var(--text);border:1px solid var(--border);border-radius:5px;padding:3px 11px;font-size:12px}
</style>
</head>
<body>
<header>
  <h1>Qwen3-8B v6e-8 — adjusted MFU &amp; throughput per experiment</h1>
  <div class="sub">Pick MFU or TPS · MFU on causal basis (cx uses its causal value, not its inflated MaxText-style number) · line = running-best frontier · ○ 8k / △ 2k · dashed = MaxText · click a point to open its experiment page · drag to zoom</div>
</header>
<div id="controls"></div>
<div class="hint" id="count"></div>
<div id="chart"></div>
<script>
const DATA = __DATA__;
const COLORS = __COLORS__;
const MAXTEXT = __MAXTEXT__;
const LANE_NAME = __LANENAMES__;
const LANES = ["cc","ag","cx","cc5"];
const MTMARK = {};   // lane -> order of the first experiment that engaged MaxText
for(const r of DATA){ if(r.maxtext && (!(r.lane in MTMARK) || r.order<MTMARK[r.lane])) MTMARK[r.lane]=r.order; }

const state = {
  lane: {cc:true, ag:true, cx:true, cc5:true},
  seq: {"2048":true, "8192":true},
  metric: "mfu",            // radio: "mfu" | "tps"
  showUnsuccessful: true,   // refuted / invalid / inconclusive / unverdicted, WITH a metric
  showCrashed: false,       // no metric at all (crash / OOM) — drawn as ✕ at the floor
  showMtMark: true,         // dotted vertical line where each lane first engaged MaxText
  dark: false,              // color scheme
};

// ---- controls ----
const C = document.getElementById("controls");
function chk(id, on, label, swatch){
  const l=document.createElement("label");
  const b=document.createElement("input"); b.type="checkbox"; b.checked=on; b.dataset.id=id;
  l.appendChild(b);
  if(swatch){const s=document.createElement("span"); s.className="sw"; s.style.background=swatch; l.appendChild(s);}
  l.appendChild(document.createTextNode(label));
  return {l,b};
}
function group(title){const g=document.createElement("div"); g.className="group"; const t=document.createElement("b"); t.textContent=title; g.appendChild(t); return g;}

const gLane=group("Variation");
LANES.forEach(L=>{const {l,b}=chk("lane:"+L,state.lane[L],LANE_NAME[L],COLORS[L]); b.onchange=()=>{state.lane[L]=b.checked;render();}; gLane.appendChild(l);});
C.appendChild(gLane);

const gSeq=group("Context");
[["2048","2k"],["8192","8k"]].forEach(([k,lab])=>{const {l,b}=chk("seq:"+k,state.seq[k],lab); b.onchange=()=>{state.seq[k]=b.checked;render();}; gSeq.appendChild(l);});
C.appendChild(gSeq);

const gMetric=group("Metric");
[["mfu","MFU"],["tps","TPS"]].forEach(([k,lab])=>{
  const l=document.createElement("label");
  const b=document.createElement("input"); b.type="radio"; b.name="metric"; b.value=k; b.checked=(state.metric===k);
  b.onchange=()=>{ if(b.checked){ state.metric=k; render(); } };
  l.appendChild(b); l.appendChild(document.createTextNode(lab));
  gMetric.appendChild(l);
});
C.appendChild(gMetric);

const gShow=group("Show");
{const {l,b}=chk("unsucc",state.showUnsuccessful,"unsuccessful (refuted/invalid/inconcl.)"); b.onchange=()=>{state.showUnsuccessful=b.checked;render();}; gShow.appendChild(l);}
{const {l,b}=chk("crashed",state.showCrashed,"crashed / no-metric"); b.onchange=()=>{state.showCrashed=b.checked;render();}; gShow.appendChild(l);}
{const {l,b}=chk("mtmark",state.showMtMark,"MaxText onset (dotted)"); b.onchange=()=>{state.showMtMark=b.checked;render();}; gShow.appendChild(l);}
C.appendChild(gShow);

const themeBtn=document.createElement("button");
themeBtn.id="theme"; themeBtn.textContent="🌙 Dark";
themeBtn.onclick=()=>{ state.dark=!state.dark; document.body.classList.toggle("dark",state.dark);
  themeBtn.textContent=state.dark?"☀ Light":"🌙 Dark"; render(); };
C.appendChild(themeBtn);

// ---- filtering + trace building ----
const SYM = {"2048":"triangle-up", "8192":"circle", "null":"square"};
const METRIC = {
  mfu: {field:"mfu", title:"adjusted MFU (%)", range:[8,52], floor:9,
        fmt:v=>v+"%", ulabel:"", mt:MAXTEXT.mfu, unit:"MFU"},
  tps: {field:"tps", title:"tok/s/chip", range:[1500,10000], floor:1700,
        fmt:v=>Number(v).toLocaleString(), ulabel:" tok/s/chip", mt:MAXTEXT.tps, unit:"TPS"},
};
const FAIL = {refuted:1, invalid:1, inconclusive:1};   // the "unsuccessful" verdicts
function visible(d){
  if(!state.lane[d.lane]) return false;
  const sk = d.seq===null ? null : String(d.seq);
  if(sk!==null && !state.seq[sk]) return false;
  if(sk===null && !(state.seq["2048"]||state.seq["8192"])) return false;
  if(!d.has_metric) return state.showCrashed;                  // crashed / no-metric → its own toggle
  if(FAIL[d.verdict] && !state.showUnsuccessful) return false; // hide ONLY explicitly-failed runs
  return true;                                                 // unverdicted / supported / baseline → always shown
}
function hover(d, label){
  const seq = d.seq===null?"?":(d.seq===2048?"2k":"8k");
  const v = d.verdict||"—";
  return `<b>${d.slug}</b><br>${LANE_NAME[d.lane]} · seq ${seq} · ${v}`
       + `<br>${label}<br><i>click → open page</i>`;
}
function frontierLine(L, s, F){
  // running-best of the active metric over (lane, seqlen); monotonic non-decreasing;
  // excludes invalid runs so a bogus value can never raise the line. Independent of the
  // unsuccessful/crashed toggles so the frontier stays stable.
  const rows = DATA.filter(d=>d.lane===L && d.seq===s && d[F]!==null && d.verdict!=="invalid")
                   .sort((a,b)=>a.order-b.order);
  let m=-1, xs=[], ys=[];
  for(const d of rows){ if(d[F]>m) m=d[F]; xs.push(d.order); ys.push(m); }
  return {xs,ys};
}
function buildTraces(){
  const M=METRIC[state.metric], F=M.field, traces=[];
  for(const L of LANES){
    if(!state.lane[L]) continue;
    const rows = DATA.filter(d=>d.lane===L && visible(d));
    // markers for the active metric — every visible run, no connecting line
    const pts = rows.filter(d=>d[F]!==null);
    if(pts.length) traces.push({
      x:pts.map(d=>d.order), y:pts.map(d=>d[F]), customdata:pts.map(d=>d.link),
      text:pts.map(d=>hover(d, M.unit+": "+M.fmt(d[F])+M.ulabel)), hovertemplate:"%{text}<extra></extra>",
      mode:"markers", name:LANE_NAME[L], legendgroup:L, yaxis:"y",
      marker:{color:COLORS[L],size:7,symbol:pts.map(d=>SYM[String(d.seq)]),line:{width:0}},
    });
    // running-best frontier line per seqlen (only ever rises — over the best results)
    for(const s of [2048,8192]){
      if(!state.seq[String(s)]) continue;
      const fr=frontierLine(L,s,F);
      if(fr.xs.length>1) traces.push({
        x:fr.xs, y:fr.ys, mode:"lines", yaxis:"y", legendgroup:L, showlegend:false,
        line:{color:COLORS[L],width:2.4,shape:"hv"}, hoverinfo:"skip",
      });
    }
    // crashed / no-metric — floor markers
    if(state.showCrashed){
      const cpts = rows.filter(d=>!d.has_metric);
      if(cpts.length) traces.push({
        x:cpts.map(d=>d.order), y:cpts.map(()=>M.floor), customdata:cpts.map(d=>d.link),
        text:cpts.map(d=>hover(d,"crashed / no metric")), hovertemplate:"%{text}<extra></extra>",
        mode:"markers", name:LANE_NAME[L]+" · crashed", legendgroup:L, yaxis:"y",
        marker:{color:COLORS[L],size:7,symbol:"x",opacity:0.5}, showlegend:false,
      });
    }
  }
  return traces;
}
function theme(){ return state.dark
  ? {paper:"#262626",plot:"#202020",font:"#e8e8e8",grid:"#333",mt:"#aaa",line:"#888"}
  : {paper:"#fff",plot:"#fff",font:"#222",grid:"#eee",mt:"#555",line:"#555"}; }
function shapes(){
  const M=METRIC[state.metric], T=theme(), s=[];
  for(const seq of ["2048","8192"]){
    if(!state.seq[seq]) continue;
    s.push({type:"line",xref:"paper",x0:0,x1:1,yref:"y",y0:M.mt[seq],y1:M.mt[seq],
            line:{color:T.line,width:1,dash:"dash"}});
  }
  if(state.showMtMark) for(const L of LANES){
    if(!state.lane[L] || !(L in MTMARK)) continue;
    s.push({type:"line",xref:"x",x0:MTMARK[L],x1:MTMARK[L],yref:"paper",y0:0,y1:1,
            line:{color:COLORS[L],width:1.5,dash:"dot"},opacity:0.6});
  }
  return s;
}
function annotations(){
  const M=METRIC[state.metric], T=theme(), a=[];
  for(const seq of ["2048","8192"]){
    if(!state.seq[seq]) continue;
    a.push({xref:"paper",x:0.005,yref:"y",y:M.mt[seq],yanchor:"bottom",showarrow:false,
            text:`MaxText ${seq==="2048"?"2k":"8k"} ${M.fmt(M.mt[seq])}${M.ulabel}`,font:{size:10,color:T.mt}});
  }
  return a;
}
function xMax(){
  // stable x-extent based on the SELECTED LANES only (not the metric / filters), so
  // switching MFU<->TPS — which changes how many points have a value — never rescales x.
  let mx=10;
  for(const L of LANES){
    if(!state.lane[L]) continue;
    for(const d of DATA) if(d.lane===L && d.order>mx) mx=d.order;
  }
  return mx;
}
function render(){
  const M=METRIC[state.metric], T=theme();
  const traces=buildTraces();
  const layout={
    margin:{l:62,r:20,t:10,b:45}, hovermode:"closest", showlegend:true, font:{color:T.font},
    legend:{orientation:"h",y:-0.13,font:{size:11,color:T.font}},
    xaxis:{title:"experiment (in order, per lane)",range:[0,xMax()+3],gridcolor:T.grid,zerolinecolor:T.grid},
    yaxis:{title:M.title,range:M.range,gridcolor:T.grid,zerolinecolor:T.grid},
    shapes:shapes(), annotations:annotations(), plot_bgcolor:T.plot, paper_bgcolor:T.paper,
  };
  Plotly.react("chart",traces,layout,{responsive:true,displaylogo:false});
  const shown=DATA.filter(visible).length;
  document.getElementById("count").textContent=`${shown} of ${DATA.length} experiments shown`;
}
document.getElementById("chart").on = null;
Plotly.newPlot("chart",[],{}).then(()=>{
  render();
  document.getElementById("chart").on("plotly_click",ev=>{
    const p=ev.points&&ev.points[0];
    if(p&&p.customdata) window.open(p.customdata,"_blank");
  });
});
</script>
</body>
</html>
"""


def write_docs(records):
    """Regenerate the 4 per-lane data docs in wiki/analyses/ from the records."""
    FNAME_DATE = "2026-06-15"   # keep existing filenames
    UPDATED = "2026-06-16"
    def fnum(v): return "—" if v is None else f"{v:,}"
    def fpct(v): return "—" if v is None else f"{v:.1f}%"
    for L in LANES:
        rows = [r for r in records if r["lane"] == L]
        bm = {s: max([r["mfu"] for r in rows if r["seq"] == s and r["mfu"] is not None], default=None) for s in (2048, 8192)}
        bt = {s: max([r["tps"] for r in rows if r["seq"] == s and r["tps"] is not None], default=None) for s in (2048, 8192)}
        if L == "cx":
            note = ('**cx** reports MFU on the causal basis directly — **no ÷ adjustment**. Its inflated '
                    '"MaxText-style" (non-causal) figure (e.g. 49.2% @8k) is discarded in favour of the '
                    'causal value (verified: 2k 47.3% / 8k 43.2%).')
        else:
            note = "MFU is on the causal (MaxText-comparable) basis."
        o = ["---", f'title: "Qwen3-{L} jax — per-experiment MFU/TPS data"', "type: analysis",
             f"created: {FNAME_DATE}", f"updated: {UPDATED}", f"tags: [qwen3-{L}, jax, mfu, tps, data]", "---", "",
             f"# Qwen3-{L} jax — per-experiment MFU/TPS data", "",
             (f"Best-effort per-experiment extraction for the **{L}** lane, in experiment order. {note} "
              f"Frontiers are clamped to the verified model-page best. MaxText MFU targets: 2k = 38.0%, "
              f"8k = 45.3% (native — **different FLOP basis, so compare to MaxText on TPS**). "
              f"`—` = not recoverable (crash / no metric / unparsed). "
              f"Regenerate: `python wiki/analyses/qwen3/build_explorer.py`."), "",
             (f"**Frontier:** 2k = {fpct(bm[2048])} MFU / {fnum(bt[2048])} tok/s/chip · "
              f"8k = {fpct(bm[8192])} MFU / {fnum(bt[8192])} tok/s/chip."), "",
             "| # | Experiment | seq | verdict | MFU (causal) | tok/s/chip |", "|---|---|---|---|---|---|"]
        for i, r in enumerate(rows, 1):
            seq = {2048: "2k", 8192: "8k"}.get(r["seq"], "?")
            o.append(f"| {i} | {r['slug']} | {seq} | {r['verdict'] or '—'} | {fpct(r['mfu'])} | {fnum(r['tps'])} |")
        o += ["", "## See also", "",
              "- [Interactive explorer](qwen3/mfu-explorer.html) · [progression plot](qwen3/mfu-progression.png)",
              f"- [Qwen3 {L} — jax model page](../models/qwen3-{L}-jax.md)", ""]
        path = os.path.join(REPO, "wiki", "analyses", f"{FNAME_DATE}-qwen3-{L}-jax-mfu-progression.md")
        open(path, "w").write("\n".join(o))


def main():
    os.chdir(REPO)
    if "--from-json" in sys.argv:
        records = json.load(open(os.path.join(SCRIPT_DIR, "mfu_data.json")))
    else:
        records = extract()
        json.dump(records, open(os.path.join(SCRIPT_DIR, "mfu_data.json"), "w"), indent=0)
    html = (HTML
            .replace("__DATA__", json.dumps(records))
            .replace("__COLORS__", json.dumps(COLORS))
            .replace("__MAXTEXT__", json.dumps(MAXTEXT))
            .replace("__LANENAMES__", json.dumps(LANE_NAME)))
    open(os.path.join(SCRIPT_DIR, "mfu-explorer.html"), "w").write(html)
    write_docs(records)
    n = len(records); withm = sum(1 for r in records if r["has_metric"])
    print(f"extracted {n} experiments ({withm} with a metric)")
    for L in LANES:
        rs = [r for r in records if r["lane"] == L]
        print(f"  {L}: {len(rs)} exp, "
              f"{sum(1 for r in rs if r['mfu'] is not None)} MFU, "
              f"{sum(1 for r in rs if r['tps'] is not None)} TPS, "
              f"{sum(1 for r in rs if not r['has_metric'])} crashed")
    print("wrote mfu_data.json + mfu-explorer.html + 4 data docs")


if __name__ == "__main__":
    main()
