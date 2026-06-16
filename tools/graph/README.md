# Wiki graph viewer

A standalone, dependency-free force-directed graph of the whole wiki — modeled on
[vasturiano/force-graph](https://github.com/vasturiano/force-graph)'s "highlight" example.
Nodes float in a force layout; **hover** a node to light up it, its neighbors, and the
connecting links; **click** to open the underlying `.md` page.

This is the portable/shareable view. The repo is *also* an Obsidian vault
(`.obsidian/`, graph plugin enabled), so you can alternatively just open the repo
root in Obsidian and press the graph-view icon — same data, no build step.

## Use

```bash
# 1. (re)generate the graph data from the wiki's markdown links
python3 tools/graph/build_graph.py        # writes tools/graph/graph.json

# 2. serve from the repo root so node clicks resolve to /wiki/... pages
python3 -m http.server 8000
#    then open  http://localhost:8000/tools/graph/
```

Opening `index.html` via `file://` shows the graph too, but node-click "open page"
needs the HTTP server (browsers block `file://` cross-directory navigation).

## What it shows

- **One node per `wiki/**/*.md` page**, sized by link degree (hubs like `index.md`
  and the model pages are biggest).
- **One edge per resolvable relative markdown link** between pages (the schema-mandated
  `[text](../dir/page.md)` form). Links into `raw/`, external URLs, and anchors are ignored.
- **Color = category**: top-level wiki folder (`concepts`, `sources`, `hypotheses`, …),
  with experiments split by model family (`exp:qwen3_cx`, `exp:llama3_8B`, …).
- **Legend** toggles groups on/off; **search box** dims everything except matches
  (Enter zooms to them, Esc clears). **☀/☾ button** switches dark/light (remembered
  across visits). Idle nodes drift gently; drift pauses only while you drag.

## Files

| File | Role |
|------|------|
| `build_graph.py` | walks the wiki, emits `graph.json` (`{nodes, links}`) |
| `index.html` | the viewer (loads `force-graph` from unpkg CDN) |
| `graph.json` | generated data — regenerate after wiki edits; safe to delete |

`graph.json` is a generated artifact. Regenerate it whenever the wiki changes
(e.g. wire `build_graph.py` into a stop-experiment/lint step if you want it fresh).
