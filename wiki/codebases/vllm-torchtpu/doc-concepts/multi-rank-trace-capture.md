---
title: Multi-rank trace capture and rank-prefix merge
type: doc-concept
provenance: doc
source: docs/developers_guide/profiling/output.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Multi-rank trace capture and rank-prefix merge

## Definition
Every TPU worker process drives its own profiler session and can only trace the chips
it owns, so a whole-slice trace is one capture per worker. Because XPlane files are
named after the **host**, co-located ranks would overwrite each other in a shared
directory. vllm-torchtpu therefore has each rank capture into a private sandbox,
agree on one canonical run timestamp published by rank 0, and on stop move its files
into a shared `plugins/profile/<timestamp>/` directory with a `rank<N>_` prefix - so
XProf loads the whole slice as one distributed session.

## In vllm-torchtpu (grounded)
All helpers are in `src/vllm_torchtpu/profiler_trace.py`, shared by the standard
profiler ([`TPUWorker.profile`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.profile))
and the [phased profiler](phased-profiler.md):
- [`rank_capture_dir`](../catalog/src/vllm_torchtpu/profiler_trace.md#rank_capture_dir) -
  per-rank sandbox `<root>/rank_<N>/`.
- [`resolve_canonical_dst_ts`](../catalog/src/vllm_torchtpu/profiler_trace.md#resolve_canonical_dst_ts) -
  rank 0 writes a marker file; other ranks poll it for
  `CANONICAL_TS_POLL_TIMEOUT_S` = 5 s, else fall back to their own timestamp (logged as
  `did not find rank 0's canonical-ts marker`).
- [`profile_session_id`](../catalog/src/vllm_torchtpu/profiler_trace.md#profile_session_id) -
  keys markers by `TORCH_TPU_DP_MASTER_PORT` (or the parent pid when DP=1) so a stale
  marker from an earlier server run is never reused;
  [`clear_canonical_ts_marker`](../catalog/src/vllm_torchtpu/profiler_trace.md#clear_canonical_ts_marker)
  drops it after merge.
- [`merge_rank_capture`](../catalog/src/vllm_torchtpu/profiler_trace.md#merge_rank_capture) -
  moves `<sandbox>/plugins/profile/*` into `<root>/plugins/profile/<canonical_ts>/`,
  adding the `rank<N>_` prefix when the **slice-global** world size (TP x PP x DP) is
  greater than 1, so the prefix is on every file of a run or none.

## Output layout
- Standard run: `<dir>/plugins/profile/<ts>/rank<N>_<host>.xplane.pb` (one per rank),
  `<dir>/rank_<N>/<host>_<pid>.pt.trace.json.gz` (Chrome-format PyTorch host +
  Kineto TPU trace, one per rank), plus `*.async_llm.*.pt.trace.json.gz` frontend
  traces unless `--profiler-config.ignore_frontend true`.
- Phased run: the same under one subdirectory per phase, plus one
  `batch_composition_stats_<ts>.json` per rank per profiled step left in the
  `rank_<N>/` sandbox (batch id, scheduled/prefill/decode token counts, request count,
  minimum KV length, assigned phase). At TP=4, three phases, `max_iterations=5`:
  12 XPlane, 12 JSON traces, 72 stats files.
- The rank is slice-global on purpose: `parallel_config`'s rank is TP x PP scoped, so
  with DP > 1 every replica would call itself rank 0 and collide on merge.

## Viewing
- `xprof --logdir <dir>` (or TensorBoard's profile plugin); forward port 6006 if not
  using VS Code Remote-SSH. When copying traces off the VM keep the
  `plugins/profile/<ts>/` hierarchy (`rsync --include='*/' --include='*.xplane.pb'
  --include='*.pt.trace.json.gz' --exclude='*'`).
- Each phase is a separate run in the dropdown; the host picker switches between ranks
  of the merged session. Trace Viewer shows kernel timelines; Memory Profile and Op
  Profile cover HBM use and MXU utilization.
- The Chrome JSON traces are not merged: each stays under its `rank_<N>/`, one rank per
  file in Perfetto / Chrome Tracing.
- For a single-file artifact use [xplane-session-merge-tool](xplane-session-merge-tool.md).

## Why it matters / when it applies
- Without the merge, every rank of a TP/EP/DP run would be a separate session (or
  silently overwrite a co-located rank). With it, per-rank skew - for example MoE
  load imbalance or a straggling collective - is visible side by side.
- **Multi-host slices:** the trace directory must be on a filesystem every rank shares
  with rank 0, or ranks land in separate run directories (no trace lost, but split).
- Under expert parallelism a single device's profile only reflects the experts routed
  to it. Setting upstream vLLM's `VLLM_MOE_ROUTING_SIMULATION_STRATEGY=uniform_random`
  makes one device representative of the whole EP mesh (implemented in
  [`maybe_simulate_routing`](../catalog/src/vllm_torchtpu/layers/adapter/moe_routing.md#maybe_simulate_routing),
  which keeps a data dependency on real activations; output is meaningless - never
  serve with it). The fused-EP kernel path refuses other strategies because the kernel
  routes by itself.

## Doc vs code at this commit
- `profiling/index.md` opens by saying only the two non-phased modes write
  Chrome-format JSON, and `viewing.md` says the JSON rsync pattern "matches nothing on
  a phased run". Both are stale: the phased profiler uses the same
  `tensorboard_trace_handler`, and `output.md` plus the index's own table show
  per-phase `rank_<N>/*.pt.trace.json.gz` files.
- The docs say "PyTorch/XLA profiler"; the code uses `torch.profiler` with TorchTPU's
  `TpuProfilerConfig` (its log line says "Starting TorchTPU profiler trace").

## Connections
- Code concepts: [tracing-annotations](../concepts/tracing-annotations.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md)
- Module catalogs: [profiler_trace](../catalog/src/vllm_torchtpu/profiler_trace.md),
  [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [moe_routing](../catalog/src/vllm_torchtpu/layers/adapter/moe_routing.md)
- Related doc-concepts: [phased-profiler](phased-profiler.md),
  [xplane-session-merge-tool](xplane-session-merge-tool.md),
  [server-side-profiling-and-trace-options](server-side-profiling-and-trace-options.md)

## Source
Extracted from `docs/developers_guide/profiling/output.md`, `profiling/index.md`,
`profiling/viewing.md` and `profiling/troubleshooting.md` (kept in place).
