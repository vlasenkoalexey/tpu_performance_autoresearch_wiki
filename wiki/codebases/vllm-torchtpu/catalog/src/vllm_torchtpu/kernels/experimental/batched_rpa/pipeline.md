---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.pipeline`/
symbols:
  run_manual_triple_buffer.steady_state: run_manual_triple_buffer().steady_state().
  _rem: _rem().
  run_manual_triple_buffer: run_manual_triple_buffer().
  run_manual_triple_buffer.steady_state.start_next_fetch: run_manual_triple_buffer().steady_state().start_next_fetch().
  run_manual_triple_buffer.steady_state.start_kv_writeback: run_manual_triple_buffer().steady_state().start_kv_writeback().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py)

## Functions
- <a id="_rem"></a>`_rem(val: int | jax.Array, n: int)` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py#L27) — Computes remainder modulo n for both Python ints and JAX arrays/tracers.
- <a id="run_manual_triple_buffer"></a>`run_manual_triple_buffer(total_steps: int | jax.Array, compute_fn: Callable[..., Any], q_bref: Any, o_bref: Any, kv_bref: Any, lse_bref: Any | None = None)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py#L34) — Executes an explicit triple-buffered pipeline over `total_steps`.
- <a id="run_manual_triple_buffer.steady_state.start_kv_writeback"></a>`start_kv_writeback()` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py#L91)
- <a id="run_manual_triple_buffer.steady_state.start_next_fetch"></a>`start_next_fetch()` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py#L87)
- <a id="run_manual_triple_buffer.steady_state"></a>`steady_state(step)` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/pipeline.py#L68)

