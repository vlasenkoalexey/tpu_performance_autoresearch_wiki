#!/usr/bin/env python3
"""Reconstruct REAL model-code diffs for the Antigravity (ag) lane and merge them into the ag
diff manifest — for EVERY experiment whose model fork is preserved (supported OR refuted).

The ag lane's per-experiment model forks are scattered across many per-experiment git branches
under `…/jax/.repo/<slug>/…/modeling_qwen3.py` (+ fused_rope.py / fused_glu.py / sharding.py).
This harvests all of them across all refs, dedups to one fork per vNNN (preferring the variant whose
slug best matches the manifest experiment), orders by vNNN, diffs consecutive model files, and
PREPENDS the model diff before the experiment's existing run.sh flag diff (diff_kind → code). The
deck's model_first() then shows model files above run.sh. See README "Recovering real model-code
diffs". Run after any flag-diff refresh:

    python tools/demo/precompute_ag_model_diffs.py
"""
import os, re, json, subprocess, difflib

REPO = "/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki"
os.chdir(REPO)
PREFIX = "wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/"
MANIFEST = "tools/demo/diffs/qwen3-ag-jax/manifest.json"
DIFFS_DIR = "tools/demo/diffs/qwen3-ag-jax"
MODEL_FILES = ("modeling_qwen3.py", "fused_rope.py", "fused_glu.py", "sharding.py")
ARC = re.compile(r"^2026-06-0[2-5]-v(\d+)")          # the main ag arc (exclude the June-26/27 rerun)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True).stdout


def refs():
    return [r for r in git("for-each-ref", "--format=%(refname)").splitlines() if r]


def harvest():
    """slug -> {ref, files:{basename: repo_path}} for the shortest-depth model paths."""
    forks = {}
    for ref in refs():
        tree = git("ls-tree", "-r", "--name-only", ref)
        if PREFIX not in tree:
            continue
        for line in tree.splitlines():
            if PREFIX not in line:
                continue
            rel = line.split(PREFIX, 1)[1]
            slug = rel.split("/")[0]
            if not ARC.match(slug):
                continue
            fn = os.path.basename(line)
            if fn not in MODEL_FILES:
                continue
            e = forks.setdefault(slug, {"ref": ref, "files": {}})
            cur = e["files"].get(fn)
            if cur is None or line.count("/") < cur.count("/"):
                e["files"][fn] = line
                if fn == "modeling_qwen3.py":
                    e["ref"] = ref            # anchor the ref to the canonical modeling file
    return {s: v for s, v in forks.items() if "modeling_qwen3.py" in v["files"]}


def vnum(slug):
    return int(ARC.match(slug).group(1))


def blob(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def pick_per_vnum(forks, man_by_v):
    """One fork per vNNN, preferring the fork slug that shares the most tokens with the
    manifest experiment's slug (so v042 picks gate-up-fusion, not v042-scan)."""
    chosen = {}
    for slug, info in forks.items():
        v = vnum(slug)
        me = man_by_v.get(v)
        toks = set(re.split(r"[-_]", slug))
        score = len(toks & set(re.split(r"[-_]", me["slug"]))) if me else 0
        if v not in chosen or score > chosen[v][1]:
            chosen[v] = (slug, score, info)
    return {v: (slug, info) for v, (slug, score, info) in chosen.items()}


def file_diff(prev_ref, prev_path, cur_ref, cur_path, name):
    a = blob(prev_ref, prev_path) if prev_path else ""
    b = blob(cur_ref, cur_path) if cur_path else ""
    if a == b:
        return ""
    ud = difflib.unified_diff(a.splitlines(), b.splitlines(),
                              fromfile=f"a/model/{name}", tofile=f"b/model/{name}", lineterm="")
    return "\n".join(ud)


def main():
    man = json.load(open(MANIFEST))
    # prefer the experiment whose slug carries a descriptive lever (longest slug) per vNNN,
    # so v042 references the gate-up-fusion page, not a bare variant
    man_by_v = {}
    for e in man["experiments"]:
        if e["vnum"] not in man_by_v or len(e["slug"]) > len(man_by_v[e["vnum"]]["slug"]):
            man_by_v[e["vnum"]] = e
    chosen = pick_per_vnum(harvest(), man_by_v)
    order = sorted(chosen)                      # vNNN ascending
    print(f"Harvested model forks for vNNN: {order}")

    updated = []
    prev = None
    for v in order:
        slug, info = chosen[v]
        ref, files = info["ref"], info["files"]
        blocks = []
        if prev is not None:
            pslug, pinfo = prev
            for name in sorted(set(files) | set(pinfo["files"])):
                d = file_diff(pinfo["ref"], pinfo["files"].get(name),
                              ref, files.get(name), name)
                if d.strip():
                    blocks.append(d)
        prev = (slug, info)
        if not blocks:
            continue                            # first fork = baseline, or no model change this step
        model_diff = "\n".join(blocks)
        # inject into EVERY manifest experiment sharing this vNNN (variants may both be in the deck)
        for e in [x for x in man["experiments"] if x["vnum"] == v]:
            flag_path = os.path.join(DIFFS_DIR, e["diff_file"])
            flag = open(flag_path, encoding="utf-8").read() if os.path.exists(flag_path) else ""
            merged = model_diff.rstrip() + ("\n\n" + flag.lstrip() if flag.strip() else "")
            open(flag_path, "w").write(merged)
            e["diff_kind"] = "code"
            lever = re.split(rf"v0*{v}-", e["slug"], 1)[-1].replace("-", " ").strip()
            e["diff_summary"] = "Model change — " + (lever or f"v{v}")
            updated.append((f"v{v}", e["slug"], e.get("verdict", ""), len(model_diff.splitlines())))

    json.dump(man, open(MANIFEST, "w"), indent=1, ensure_ascii=False)
    print(f"\nInjected real model-code diffs into {len(updated)} ag experiments "
          f"(supported AND refuted):")
    for v, slug, verdict, n in updated:
        print(f"  {v:<5} {verdict:<12} {slug[:46]:48} (+{n} model-diff lines)")


if __name__ == "__main__":
    main()
