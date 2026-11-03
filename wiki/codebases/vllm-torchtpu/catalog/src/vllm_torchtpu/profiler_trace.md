---
title: 'Module: src/vllm_torchtpu/profiler_trace.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/profiler_trace.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.profiler_trace`/
symbols:
  resolve_canonical_dst_ts: resolve_canonical_dst_ts().
  clear_canonical_ts_marker: clear_canonical_ts_marker().
  logger: logger.
  merge_rank_capture: merge_rank_capture().
  profile_session_id: profile_session_id().
  rank_capture_dir: rank_capture_dir().
  CANONICAL_TS_FORMAT: CANONICAL_TS_FORMAT.
  CANONICAL_TS_POLL_TIMEOUT_S: CANONICAL_TS_POLL_TIMEOUT_S.
  canonical_ts_marker_path: canonical_ts_marker_path().
  CANONICAL_TS_POLL_INTERVAL_S: CANONICAL_TS_POLL_INTERVAL_S.
---
# Module: [`src/vllm_torchtpu/profiler_trace.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py)

## Functions
- <a id="canonical_ts_marker_path"></a>`canonical_ts_marker_path(dst_root: str, session_key: str)` — [`L76`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L76)
- <a id="clear_canonical_ts_marker"></a>`clear_canonical_ts_marker(dst_root: str, session_key: str | None = None)` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L138) — Drop the marker once the run it describes is merged (rank 0 only). — documented in [omni-diffusion-support](../../../concepts/omni-diffusion-support.md)
- <a id="merge_rank_capture"></a>`merge_rank_capture(capture_dir: str, dst_root: str, canonical_ts: str, worker_rank: int, world_size: int = 1)` — [`L148`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L148) — Move this rank's capture into the shared run directory.
- <a id="profile_session_id"></a>`profile_session_id()` — [`L51`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L51) — Return an id shared by every worker process of this server run.
- <a id="rank_capture_dir"></a>`rank_capture_dir(dst_root: str, worker_rank: int)` — [`L67`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L67) — Return the per-rank capture sandbox under `dst_root`.
- <a id="resolve_canonical_dst_ts"></a>`resolve_canonical_dst_ts(dst_root: str, worker_rank: int, *, session_key: str | None = None)` — [`L80`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L80) — Resolve the destination run timestamp shared by all ranks. — documented in [omni-diffusion-support](../../../concepts/omni-diffusion-support.md)

## Module values
- <a id="CANONICAL_TS_FORMAT"></a>`CANONICAL_TS_FORMAT` — [`L46`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L46)
- <a id="CANONICAL_TS_POLL_INTERVAL_S"></a>`CANONICAL_TS_POLL_INTERVAL_S` — [`L48`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L48)
- <a id="CANONICAL_TS_POLL_TIMEOUT_S"></a>`CANONICAL_TS_POLL_TIMEOUT_S` — [`L47`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L47)
- <a id="logger"></a>`logger` — [`L44`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/profiler_trace.py#L44)

