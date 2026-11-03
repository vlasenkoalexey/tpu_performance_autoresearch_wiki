---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.kv_scatter`/
symbols:
  multi_layer_scatter_into: multi_layer_scatter_into().
  smoke_test_multi_layer_scatter: smoke_test_multi_layer_scatter().
  _jax_import_error._jax_import_error: _jax_import_error._jax_import_error.
  e: e.
  logger: logger.
  _make_multi_layer_scatter_kernel: _make_multi_layer_scatter_kernel().
  scatter_available: scatter_available().
  _scatter_kernel_body: _scatter_kernel_body().
  _make_multi_layer_scatter_kernel._jax_multi_layer_scatter: _make_multi_layer_scatter_kernel()._jax_multi_layer_scatter().
  prepare_scatter_args: prepare_scatter_args().
  _scatter_kernel_body.body: _scatter_kernel_body().body().
  _scatter_kernel_body.body._start: _scatter_kernel_body().body()._start().
  _scatter_kernel_body.body._wait: _scatter_kernel_body().body()._wait().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py)

## Functions
- <a id="_make_multi_layer_scatter_kernel._jax_multi_layer_scatter"></a>`_jax_multi_layer_scatter(num_chunks, src_offsets, dest_offsets, *srcs_and_dsts)` — [`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L112)
- <a id="_make_multi_layer_scatter_kernel"></a>`_make_multi_layer_scatter_kernel(num_layers: int)` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L105) — Build (and cache) a torch_tpu-wrapped kernel that scatters
- <a id="_scatter_kernel_body"></a>`_scatter_kernel_body(num_chunks_ref, src_offsets_ref, dest_offsets_ref, src_ref, dst_ref_in, dst_ref_out)` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L75)
- <a id="_scatter_kernel_body.body._start"></a>`_start(i)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L87)
- <a id="_scatter_kernel_body.body._wait"></a>`_wait(i)` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L95)
- <a id="_scatter_kernel_body.body"></a>`body(sem)` — [`L85`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L85)
- <a id="multi_layer_scatter_into"></a>`multi_layer_scatter_into(srcs: list[torch.Tensor], dsts: list[torch.Tensor], local_blocks: torch.Tensor, *, prebuilt_args: tuple[torch.Tensor, torch.Tensor, torch.Tensor] | None = None)` — [`L171`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L171) — Scatter ``srcs[l][i]`` into ``dsts[l][local_blocks[i]]`` for all
- <a id="prepare_scatter_args"></a>`prepare_scatter_args(local_blocks: torch.Tensor, device: torch.device)` — [`L158`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L158) — Build the three scalar-prefetch tensors once per scatter call
- <a id="scatter_available"></a>`scatter_available()` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L67) — Whether the scatter kernel can be used. Callers must guard with
- <a id="smoke_test_multi_layer_scatter"></a>`smoke_test_multi_layer_scatter(device: torch.device, num_layers: int = 2, num_blocks: int = 4, trailing_shape: tuple[int, ...] = (16, 2, 128), dtype: torch.dtype = torch.bfloat16)` — [`L211`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L211) — Round-trip a small multi-layer scatter and check contents per

## Module values
- <a id="_jax_import_error._jax_import_error"></a>`_jax_import_error` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L54)
- <a id="e"></a>`e` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L60)
- <a id="logger"></a>`logger` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/kv_scatter.py#L50)

