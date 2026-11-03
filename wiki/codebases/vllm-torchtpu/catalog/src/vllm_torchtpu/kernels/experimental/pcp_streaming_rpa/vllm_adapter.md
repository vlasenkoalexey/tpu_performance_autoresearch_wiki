---
title: 'Module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.pcp_streaming_rpa.vllm_adapter`/
symbols:
  pcp_streaming_jax_op: pcp_streaming_jax_op().
  make_pcp_streaming_rpa_kernel: make_pcp_streaming_rpa_kernel().
  get_pcp_streaming_mesh: get_pcp_streaming_mesh().
  PCP_STREAMING_RPA_OUTPUT_PARTITION_SPECS: PCP_STREAMING_RPA_OUTPUT_PARTITION_SPECS.
  PCP_STREAMING_RPA_INPUT_PARTITION_SPECS: PCP_STREAMING_RPA_INPUT_PARTITION_SPECS.
  invoke_pcp_streaming_op: invoke_pcp_streaming_op().
  build_pcp_streaming_callable: build_pcp_streaming_callable().
  make_pcp_streaming_rpa_kernel._pcp_streaming_rpa_kernel: make_pcp_streaming_rpa_kernel()._pcp_streaming_rpa_kernel().
  _PCP_STREAMING_RPA_TENSOR_ARG_COUNT: _PCP_STREAMING_RPA_TENSOR_ARG_COUNT.
  pcp_streaming_jax_op.fake_fn: pcp_streaming_jax_op().fake_fn().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py)

## Functions
- <a id="make_pcp_streaming_rpa_kernel._pcp_streaming_rpa_kernel"></a>`_pcp_streaming_rpa_kernel(kv_cache: jax.Array, query: jax.Array, key: jax.Array, value: jax.Array, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, request_distribution: jax.Array)` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L217)
- <a id="build_pcp_streaming_callable"></a>`build_pcp_streaming_callable(name: str, fn: Callable[..., object], *, donate_argnums: Sequence[int] | None, mesh: jax.sharding.Mesh, input_partition_specs: Sequence[PartitionSpec], output_partition_specs: Sequence[PartitionSpec] | None = None)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L56) — Build the eager JaxCallable for a PCP streaming kernel fn.
- <a id="pcp_streaming_jax_op.fake_fn"></a>`fake_fn(*args, **kwargs)` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L164)
- <a id="get_pcp_streaming_mesh"></a>`get_pcp_streaming_mesh()` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L184) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="invoke_pcp_streaming_op"></a>`invoke_pcp_streaming_op(rpa_kernel_op, kv_cache, args, kwargs)` — [`L259`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L259) — Call the 8-tensor PCP streaming custom op from generic RPA args. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="make_pcp_streaming_rpa_kernel"></a>`make_pcp_streaming_rpa_kernel(*, q_scale: float | None, k_scale: float | None, v_scale: float | None, mesh: jax.sharding.Mesh, sliding_window: int | None, sm_scale: float | None = None, soft_cap: float | None = None, skip_kv_update: bool, cp_kv_cache_interleave_size: int, q_block_size: int = PCP_STREAMING_RPA_LOCAL_COMPILE_TOKEN_MULTIPLE, q_compute_size: int | None = None, kv_layout: batched_rpa_configs.KVLayout = batched_rpa_configs.KVLayout.HEAD_ALONG_SUBLANE, block_major: bool = False)` — [`L188`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L188) — Build a PCP streaming RPA entry with only tensor args in its signature. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="pcp_streaming_jax_op"></a>`pcp_streaming_jax_op(name: str, fn: Callable[..., object], *, donate_argnums: Sequence[int] | None, mesh: jax.sharding.Mesh, input_partition_specs: Sequence[PartitionSpec], output_partition_specs: Sequence[PartitionSpec] | None = None)` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L122) — Register a PCP streaming custom op behind a hot-reload dispatcher. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)

## Module values
- <a id="PCP_STREAMING_RPA_INPUT_PARTITION_SPECS"></a>`PCP_STREAMING_RPA_INPUT_PARTITION_SPECS` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L40)
- <a id="PCP_STREAMING_RPA_OUTPUT_PARTITION_SPECS"></a>`PCP_STREAMING_RPA_OUTPUT_PARTITION_SPECS` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L50) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_PCP_STREAMING_RPA_TENSOR_ARG_COUNT"></a>`_PCP_STREAMING_RPA_TENSOR_ARG_COUNT` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.py#L38)

