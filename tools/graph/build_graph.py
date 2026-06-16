#!/usr/bin/env python3
"""Build graph.json for the wiki force-graph viewer.

Walks every Markdown page under wiki/, emits one node per page and one edge per
resolvable relative Markdown link between pages. Output feeds tools/graph/index.html
(vasturiano/force-graph highlight example).

Node id  = page path relative to the wiki/ root (e.g. "concepts/fsdp.md").
Node group = coloring bucket: top-level category, with experiments split by model family.

Usage:
    python3 tools/graph/build_graph.py            # writes tools/graph/graph.json
    python3 tools/graph/build_graph.py --stdout   # print to stdout instead
"""

import argparse
import json
import os
import re
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
WIKI = os.path.join(REPO, "wiki")

# [text](target)  — capture the target; we filter to local .md afterwards.
LINK_RE = re.compile(r"\]\(([^)]+)\)")
TITLE_RE = re.compile(r'^title:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def page_group(rel: str) -> str:
    """Coloring bucket for a page path relative to wiki/."""
    parts = rel.split("/")
    top = parts[0]
    if top == "experiments" and len(parts) > 1 and not parts[1].endswith(".md"):
        # experiments/<family>_autoresearch_optimization/<lane>/...
        family = parts[1].replace("_autoresearch_optimization", "")
        return f"exp:{family}"
    if top.endswith(".md"):
        return "meta"  # index.md, log.md, etc. at wiki root
    return top


def title_for(path: str, rel: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read(4000)
    except OSError:
        return rel
    m = TITLE_RE.search(text)
    if m:
        return m.group(1).strip()
    m = H1_RE.search(text)
    if m:
        return m.group(1).strip()
    return os.path.basename(rel)


def collect_pages():
    pages = {}  # rel -> abspath
    for dirpath, dirnames, filenames in os.walk(WIKI):
        # skip noise dirs
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".ipynb_checkpoints")]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            ap = os.path.join(dirpath, fn)
            rel = os.path.relpath(ap, WIKI)
            pages[rel] = ap
    return pages


def resolve_link(src_rel: str, target: str):
    """Resolve a markdown link target to a wiki-relative .md path, or None."""
    t = target.strip()
    if not t or t.startswith(("http://", "https://", "mailto:", "#")):
        return None
    t = unquote(t.split("#", 1)[0].split("?", 1)[0]).strip()
    if not t.endswith(".md"):
        return None
    src_dir = os.path.dirname(src_rel)
    resolved = os.path.normpath(os.path.join(src_dir, t))
    if resolved.startswith(".."):  # escaped the wiki root (e.g. into raw/)
        return None
    return resolved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true", help="print JSON to stdout")
    args = ap.parse_args()

    pages = collect_pages()
    nodes = {rel: {"id": rel, "title": title_for(ap_, rel), "group": page_group(rel), "deg": 0}
             for rel, ap_ in pages.items()}

    edges = set()
    for rel, ap_ in pages.items():
        try:
            with open(ap_, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        for target in LINK_RE.findall(text):
            dst = resolve_link(rel, target)
            if dst is None or dst not in pages or dst == rel:
                continue
            edges.add((rel, dst))

    for a, b in edges:
        nodes[a]["deg"] += 1
        nodes[b]["deg"] += 1

    graph = {
        "nodes": list(nodes.values()),
        "links": [{"source": a, "target": b} for a, b in sorted(edges)],
    }

    if args.stdout:
        json.dump(graph, sys.stdout, indent=0)
    else:
        out = os.path.join(HERE, "graph.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(graph, f, separators=(",", ":"))
        n_orphan = sum(1 for v in nodes.values() if v["deg"] == 0)
        print(f"wrote {out}")
        print(f"  {len(graph['nodes'])} nodes, {len(graph['links'])} edges, {n_orphan} orphans")


if __name__ == "__main__":
    main()
