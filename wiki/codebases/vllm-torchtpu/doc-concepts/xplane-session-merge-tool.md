---
title: merge_xplane - combining per-rank XPlane captures into one file
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/viewing.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# merge_xplane - combining per-rank XPlane captures into one file

## Definition
`python -m vllm_torchtpu.tools.merge_xplane <path>` combines a capture session's
per-rank `.xplane.pb` files into a single XSpace file. It is **not** needed for
`xprof --logdir`, which already reads a `plugins/profile/<ts>/` directory as one
distributed session; it exists for consumers that take exactly one file (an offline
XProf upload, a bug attachment). Merging is plane-level, not file concatenation.

## In vllm-torchtpu (grounded)
Module `src/vllm_torchtpu/tools/merge_xplane.py` (with a vendored `xplane_pb2`):
- [`discover_sessions`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#discover_sessions)
  finds every capture session under the given path(s) - a run root yields one session
  per phase; naming the phase dir, `plugins/profile`, or the timestamp dir all resolve
  to the same session. Already-merged outputs sitting in a phase directory are
  recognised and skipped, so re-running is safe.
- [`Session`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#Session) /
  [`Capture`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#Capture) model one
  profile window; `Session.default_output_dir` is the **phase directory** (one level
  above `plugins/`), and `Session.missing_ranks` reports gaps in the rank set so a
  merge that lost a rank warns instead of silently describing less of the slice.
- [`merge_session`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#merge_session)
  renumbers planes globally (every rank calls its chip `/device:TPU:0`), collapses the
  duplicate `/host:metadata` planes (each carries the HLO protos) to one, and tags each
  rank's `/host:CPU` plane; it returns a
  [`MergeResult`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#MergeResult).
- [`main`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#main) - CLI with
  `--dry-run`, `-o` (single output; only when inputs resolve to one session) and `-d`
  (output dir). Both are refused when they point inside a session directory
  ([`_is_inside_session_dir`](../catalog/src/vllm_torchtpu/tools/merge_xplane.md#_is_inside_session_dir)).

## Why it matters / when it applies
- Size: each rank ships a full `/host:metadata` copy, so the merged output is roughly
  half the input size (the doc's v6e TP=4 example: 4 captures x 5 planes = 20 planes
  -> 17 written; 1164 MB -> 572 MB over three phases). Merging on the TPU VM before
  copying traces down moves much less data.
- A phased run yields one merged file **per phase**, because each phase is an
  independent capture window anchored at its own zero.
- Pitfall the tool guards against: a merged file placed inside
  `plugins/profile/<ts>/` appears to XProf as an extra host holding a second copy of
  every rank - a 4-rank capture reports 8 TPU cores and double the events with no
  visible error. The phase directory is safe because XProf enumerates runs only at
  `*/plugins/profile/*`.

## Connections
- Code concepts: [tracing-annotations](../concepts/tracing-annotations.md)
- Module catalogs: [tools/merge_xplane](../catalog/src/vllm_torchtpu/tools/merge_xplane.md),
  [profiler_trace](../catalog/src/vllm_torchtpu/profiler_trace.md)
- Related doc-concepts: [multi-rank-trace-capture](multi-rank-trace-capture.md),
  [phased-profiler](phased-profiler.md)

## Source
Extracted from `docs/developers_guide/profiling/viewing.md` (kept in place).
