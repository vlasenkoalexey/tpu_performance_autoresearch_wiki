#!/usr/bin/env python3
"""Merge cluster-scan TSV rows into the combined gke-tpu-cluster-scan.md.

Companion to scan-gke-clusters.sh. Reads a TSV produced by the probe script
(restricted to one project's clusters — see --project filter) and a combined
Markdown file. Replaces the project's rows in each TPU-gen table, re-sorts
per the existing rule (largest single-slice topology first, then cluster
name), and rewrites the file. Prose between tables is preserved verbatim.

The TSV format (11 columns produced by scan-gke-clusters.sh):
  project  cluster  location  status  xpk  tpu_ready  tpu_total  our_uses
    xpk_type  topology  machine_type

The Markdown table format (9 columns):
  | Cluster | Project | Loc | XPK type | Topology (slices) | TPU Ready
    | XPK | gcsfuse | Spot |

Mapping (TSV → Markdown):
  cluster      → Cluster (backtick-quoted)
  project      → Project
  location     → Loc
  xpk_type     → XPK type
  (rendered)   → Topology (slices)  — see render_topology() below
  tpu_ready    → TPU Ready
  xpk          → XPK (with translation: Y → Y, js-only → js-only, N → N,
                       cred-fail → cred-fail, timeout → timeout)
  ?            → gcsfuse  (NOT in TSV; new rows get "?" — gcsfuse status
                          requires kubectl probe, not in scan)
  ?            → Spot     (NOT in TSV; new rows get "?" — spot detection
                          requires gcloud node-pool inspection, not in scan)

For existing rows from OTHER projects, the merger preserves the gcsfuse + Spot
columns verbatim. Only the project being scanned has its rows fully replaced.

Usage:
  python merge_cluster_scan.py \\
    --tsv /tmp/<project>.tsv \\
    --combined .env/gke-tpu-cluster-scan.md \\
    --project <project>
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

# ----------------------------------------------------------------------------
# TPU family → chips-per-host mapping (mirrors the awk logic in scan-gke-clusters.sh)
# ----------------------------------------------------------------------------

MACHINE_FAMILY = [
    (re.compile(r"^ct5p-hightpu-4t"),     ("v5p", 4)),
    (re.compile(r"^ct6e-standard-4t"),    ("v6e", 4)),
    (re.compile(r"^ct6e-standard-1t"),    ("v6e", 1)),
    (re.compile(r"^ct6e-standard-8t"),    ("v6e", 8)),
    (re.compile(r"^ct5lp-hightpu-1t"),    ("v5e", 1)),
    (re.compile(r"^ct5lp-hightpu-4t"),    ("v5e", 4)),
    (re.compile(r"^ct5lp-hightpu-8t"),    ("v5e", 8)),
    (re.compile(r"^ct5(e|lp)-"),          ("v5e", 4)),
    (re.compile(r"^ct4p-hightpu-4t"),     ("v4",  4)),
    (re.compile(r"^tpu7x-standard-4t"),   ("v7x", 4)),
]


def family_and_chips_per_host(machine_type: str) -> tuple[str, int] | None:
    for pat, info in MACHINE_FAMILY:
        if pat.match(machine_type):
            return info
    return None


# ----------------------------------------------------------------------------
# Topology rendering (TSV → Markdown table cell)
# ----------------------------------------------------------------------------


def render_topology(topology_tsv: str, machine_type_tsv: str) -> str:
    """Render TSV topology field as the Markdown Topology (slices) cell.

    TSV topology: ";"-joined "<placement>:<node_count>" pairs
                  e.g. "4x4x16:64;4x4x8:32"
                  "1-host" placement means single-host pool (placement was empty)
    TSV machine: ";"-joined machine types
                 e.g. "ct5p-hightpu-4t"

    Markdown rendering rules (mirror the existing combined-file format):
      - Per pool, compute chips_per_slice = product(placement axes)
      - Compute nodes_per_slice = chips_per_slice / chips_per_host
      - Compute slices = node_count / nodes_per_slice
      - Format: "<N>× <fam> <placement> (<chips>c)" if slices > 1
                "<fam> <placement> (<chips>c)" if single slice
                "<fam> 1-host" if placement was empty
      - Pools joined with ", "

    If we can't compute (missing machine type, weird placement), returns
    the raw TSV value with "(raw)" marker so the user can fix manually.
    """
    if topology_tsv in ("-", "", "?"):
        return topology_tsv

    # Use the first machine type for family lookup; multi-pool clusters
    # almost always share a single family.
    primary_mt = machine_type_tsv.split(";")[0] if machine_type_tsv != "-" else ""
    fam_info = family_and_chips_per_host(primary_mt)
    if fam_info is None:
        return f"{topology_tsv} (raw)"
    fam, chips_per_host = fam_info

    rendered_pools = []
    for pool in topology_tsv.split(";"):
        if ":" not in pool:
            rendered_pools.append(f"{pool} (raw)")
            continue
        placement, count_str = pool.split(":", 1)
        try:
            node_count = int(count_str)
        except ValueError:
            rendered_pools.append(f"{pool} (raw)")
            continue

        if placement == "1-host":
            # 1-host pool: chips = nodes × chips_per_host
            chips_total = node_count * chips_per_host
            if node_count > 1:
                rendered_pools.append(f"{node_count}× {fam} 1-host")
            else:
                rendered_pools.append(f"{fam} 1-host")
            continue

        # Multi-host placement: parse "4x4x16" or "8x8"
        try:
            axes = [int(a) for a in placement.split("x")]
        except ValueError:
            rendered_pools.append(f"{pool} (raw)")
            continue
        chips_per_slice = 1
        for a in axes:
            chips_per_slice *= a
        nodes_per_slice = max(1, chips_per_slice // chips_per_host)
        slices = max(1, node_count // nodes_per_slice)

        if slices > 1:
            rendered_pools.append(f"{slices}× {fam} {placement} ({chips_per_slice}c)")
        else:
            rendered_pools.append(f"{fam} {placement} ({chips_per_slice}c)")

    return ", ".join(rendered_pools)


# ----------------------------------------------------------------------------
# Sort key (mirror the existing combined-file sort rule)
# ----------------------------------------------------------------------------


_CHIP_COUNT_RE = re.compile(r"(\d+)c\b")


def max_chip_count(topology_md: str) -> int:
    """Extract max single-slice chip count from a rendered Topology cell.

    Sort rule (from the combined file's intro):
      "largest single-slice topology first, then cluster name. Multi-slice
       clusters show all slice sizes in the topology column; the sort key
       uses the maximum single-slice chip count."

    Pulls every "(Nc)" out and returns the max. Returns 0 if none found
    (puts unknowns at the bottom).
    """
    matches = _CHIP_COUNT_RE.findall(topology_md)
    if not matches:
        return 0
    return max(int(m) for m in matches)


def sort_key(row: dict) -> tuple:
    """(neg chip count, cluster name) so largest topology first, then by name."""
    return (-max_chip_count(row["topology_md"]), row["cluster"].strip("`"))


# ----------------------------------------------------------------------------
# TSV → row dict
# ----------------------------------------------------------------------------

TSV_COLUMNS = [
    "project", "cluster", "location", "status", "xpk",
    "tpu_ready", "tpu_total", "our_uses", "xpk_type", "topology",
    "machine_type",
]


def tsv_to_row(tsv_line: str) -> dict | None:
    """Parse one TSV row into a markdown-row dict, or None if skip."""
    fields = tsv_line.rstrip("\n").split("\t")
    if len(fields) != len(TSV_COLUMNS):
        return None
    rec = dict(zip(TSV_COLUMNS, fields))
    # Skip non-RUNNING + non-TPU clusters: the combined file omits "dead" rows.
    if rec["status"] != "RUNNING":
        return None
    if rec["topology"] in ("-", ""):
        # No TPU pool — not in inventory.
        return None
    if rec["xpk"] in ("cred-fail", "timeout"):
        # Couldn't probe — omit from inventory (user can re-run).
        return None
    return {
        "cluster": f"`{rec['cluster']}`",
        "project": rec["project"],
        "location": rec["location"],
        "xpk_type": rec["xpk_type"],
        "topology_md": render_topology(rec["topology"], rec["machine_type"]),
        "tpu_ready": rec["tpu_ready"],
        "xpk": rec["xpk"],
        "gcsfuse": "?",   # not in TSV; new rows get "?"
        "spot": "?",      # not in TSV; new rows get "?"
        "_family": _topology_family(rec["xpk_type"], rec["machine_type"]),
    }


def _topology_family(xpk_type: str, machine_type: str) -> str | None:
    """Pick a family from xpk_type (or machine_type fallback) for table routing."""
    if xpk_type and xpk_type != "-":
        first = xpk_type.split(";")[0].strip()
        m = re.match(r"^(v\d+[a-z]*)", first)
        if m:
            return m.group(1)
    primary_mt = machine_type.split(";")[0] if machine_type else ""
    fi = family_and_chips_per_host(primary_mt)
    return fi[0] if fi else None


# ----------------------------------------------------------------------------
# Markdown parser (combined file → structured tables)
# ----------------------------------------------------------------------------

_TABLE_HEADER_RE = re.compile(r"^\|\s*Cluster\s*\|.*\|\s*Spot\s*\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|\s*$")
_SECTION_RE = re.compile(r"^##\s+(v\d+[a-z]*)\s+—\s+(\d+)\s+clusters?\s*$")


def parse_md_row(line: str) -> dict | None:
    """Parse one markdown table row into a dict, or None if not a data row."""
    if not line.startswith("|") or _TABLE_SEP_RE.match(line):
        return None
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 9:
        return None
    cluster, project, loc, xpk_type, topology_md, tpu_ready, xpk, gcsfuse, spot = cells
    return {
        "cluster": cluster,
        "project": project,
        "location": loc,
        "xpk_type": xpk_type,
        "topology_md": topology_md,
        "tpu_ready": tpu_ready,
        "xpk": xpk,
        "gcsfuse": gcsfuse,
        "spot": spot,
    }


def render_md_row(row: dict) -> str:
    """Render row dict back to markdown table line."""
    return (
        f"| {row['cluster']} | {row['project']} | {row['location']} "
        f"| {row['xpk_type']} | {row['topology_md']} "
        f"| {row['tpu_ready']} | {row['xpk']} | {row['gcsfuse']} | {row['spot']} |"
    )


def parse_combined(combined_path: Path) -> dict:
    """Parse the combined file into (preamble, sections, postamble).

    Returns:
        {
          "preamble": str,                       # everything before first ## v* section
          "sections": {fam: {"header_line", "table_header_lines", "rows": [..]}},
          "postamble": str,                      # everything after last data row
          "last_audit_line_index": int | None,   # for updating
        }

    Section ordering is preserved by recording the order of family-keys.
    """
    text = combined_path.read_text()
    lines = text.split("\n")

    state = "preamble"
    preamble_lines: list[str] = []
    sections: dict[str, dict] = {}
    section_order: list[str] = []
    current_family: str | None = None
    postamble_lines: list[str] = []

    last_audit_idx = None

    for i, line in enumerate(lines):
        if last_audit_idx is None and line.startswith("**Last audit**"):
            last_audit_idx = i

        sec_m = _SECTION_RE.match(line)
        if sec_m:
            fam = sec_m.group(1)
            current_family = fam
            section_order.append(fam)
            sections[fam] = {
                "header_line": line,
                "table_header_lines": [],
                "rows": [],
                "trailing_blank": False,
            }
            state = "section_header"
            continue

        if state == "preamble":
            preamble_lines.append(line)
            continue

        if state == "section_header":
            # Table header rows (the |---|---| lines + the |Cluster|...| header)
            # come right after the section H2. Collect until we hit the first
            # data row.
            sections[current_family]["table_header_lines"].append(line)
            if _TABLE_SEP_RE.match(line):
                state = "section_rows"
            continue

        if state == "section_rows":
            row = parse_md_row(line)
            if row is not None:
                sections[current_family]["rows"].append(row)
                continue
            # Hit non-row line — section is done. Could be another ## section
            # or postamble.
            sec_m2 = _SECTION_RE.match(line)
            if sec_m2:
                fam = sec_m2.group(1)
                current_family = fam
                section_order.append(fam)
                sections[fam] = {
                    "header_line": line,
                    "table_header_lines": [],
                    "rows": [],
                }
                state = "section_header"
                continue
            # Not a section header — transition to postamble.
            state = "postamble"
            postamble_lines.append(line)
            continue

        if state == "postamble":
            postamble_lines.append(line)

    return {
        "preamble": "\n".join(preamble_lines),
        "sections": sections,
        "section_order": section_order,
        "postamble": "\n".join(postamble_lines),
        "last_audit_idx": last_audit_idx,
        "raw_lines": lines,
    }


# ----------------------------------------------------------------------------
# Merge + render
# ----------------------------------------------------------------------------


def merge_and_render(parsed: dict, new_rows: list[dict], project: str,
                     timestamp_utc: str) -> str:
    """Produce the rewritten combined-file text."""
    sections = parsed["sections"]
    section_order = parsed["section_order"]

    # 1. Delete existing rows where project matches
    deleted_count = 0
    for fam, sec in sections.items():
        kept = []
        for r in sec["rows"]:
            if r["project"] == project:
                deleted_count += 1
                continue
            kept.append(r)
        sec["rows"] = kept

    # 2. Add new rows to the right section, creating section if absent
    added_count = 0
    for nr in new_rows:
        fam = nr.pop("_family", None) or _fallback_family_from_xpk(nr["xpk_type"])
        if fam is None:
            print(f"WARNING: couldn't determine TPU family for {nr['cluster']} "
                  f"(xpk_type={nr['xpk_type']}); skipping",
                  file=sys.stderr)
            continue
        if fam not in sections:
            # New family — create section in sort order (alphabetical: v4, v5e, v5p, v6e, v7x)
            sections[fam] = {
                "header_line": f"## {fam} — 0 clusters",  # count fixed below
                "table_header_lines": _default_table_header_lines(),
                "rows": [],
            }
            section_order.append(fam)
        sections[fam]["rows"].append(nr)
        added_count += 1

    # 3. Sort each section
    for fam, sec in sections.items():
        sec["rows"].sort(key=sort_key)

    # 4. Update section header counts
    for fam, sec in sections.items():
        n = len(sec["rows"])
        sec["header_line"] = re.sub(
            r"^##\s+(v\d+[a-z]*)\s+—\s+\d+\s+clusters?",
            lambda m: f"## {m.group(1)} — {n} cluster{'s' if n != 1 else ''}",
            sec["header_line"],
        )

    # 5. Render sections
    out_blocks = [parsed["preamble"].rstrip("\n")]
    for fam in section_order:
        sec = sections[fam]
        if not sec["rows"]:
            # Empty section — skip rendering
            continue
        block = [sec["header_line"]]
        block.extend(sec["table_header_lines"])
        block.extend(render_md_row(r) for r in sec["rows"])
        block.append("")  # trailing blank
        out_blocks.append("\n".join(block))
    out_blocks.append(parsed["postamble"].lstrip("\n"))

    rendered = "\n".join(out_blocks)

    # 6. Update Last audit line — append note about this project's refresh
    audit_note = f" + `{project}` refreshed @ {timestamp_utc} ({added_count} clusters, replaced {deleted_count})"
    rendered = re.sub(
        r"(^\*\*Last audit\*\*:[^\n]+?)(\s+—\s+|\s+\+\s+`[^`]+`\s+refreshed\s+@\s+)",
        lambda m: m.group(1) + audit_note + (" — " if m.group(2).startswith(" —") else m.group(2)),
        rendered,
        count=1,
        flags=re.MULTILINE,
    )
    # If the above didn't match (no audit line), append a fallback note at top
    if audit_note not in rendered:
        # Try simpler: append after the first "**Last audit**:" content
        rendered = re.sub(
            r"(\*\*Last audit\*\*:\s*[^\n]+)$",
            lambda m: m.group(1) + audit_note,
            rendered,
            count=1,
            flags=re.MULTILINE,
        )

    return rendered


def _fallback_family_from_xpk(xpk_type: str) -> str | None:
    if not xpk_type or xpk_type == "-":
        return None
    first = xpk_type.split(";")[0].strip()
    m = re.match(r"^(v\d+[a-z]*)", first)
    return m.group(1) if m else None


def _default_table_header_lines() -> list[str]:
    return [
        "",
        "| Cluster | Project | Loc | XPK type | Topology (slices) | TPU Ready | XPK | gcsfuse | Spot |",
        "|---|---|---|---|---|---:|:---:|:---:|:---:|",
    ]


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tsv", required=True, help="Path to TSV produced by scan-gke-clusters.sh")
    p.add_argument("--combined", required=True, help="Path to combined gke-tpu-cluster-scan.md")
    p.add_argument("--project", required=True, help="Project being merged (rows with this project are replaced)")
    args = p.parse_args()

    tsv_path = Path(args.tsv)
    combined_path = Path(args.combined)
    if not tsv_path.exists():
        print(f"ERROR: TSV not found: {tsv_path}", file=sys.stderr)
        return 1
    if not combined_path.exists():
        print(f"ERROR: Combined file not found: {combined_path}", file=sys.stderr)
        return 1

    # Read TSV (skip header line; expect tab-separated)
    new_rows = []
    with tsv_path.open() as f:
        header = f.readline()
        if not header.startswith("project\t"):
            print(f"WARNING: TSV header looks wrong: {header.strip()!r}", file=sys.stderr)
        for line in f:
            row = tsv_to_row(line)
            if row is not None and row["project"] == args.project:
                new_rows.append(row)

    print(f"[merge_cluster_scan] read {len(new_rows)} rows for project '{args.project}' from {tsv_path}",
          file=sys.stderr)

    parsed = parse_combined(combined_path)
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rendered = merge_and_render(parsed, new_rows, args.project, timestamp)

    combined_path.write_text(rendered)
    print(f"[merge_cluster_scan] wrote {combined_path} ({len(rendered)} bytes)",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
