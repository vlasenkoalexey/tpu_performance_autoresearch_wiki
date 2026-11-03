---
title: 'Module: src/vllm_torchtpu/kernels/diffusion_attention/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/diffusion_attention/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.diffusion_attention.kernel`/
symbols:
  flash_attention_bshd: flash_attention_bshd().
  _splash_attention_forward: _splash_attention_forward().
  BlockSizes: BlockSizes#
  _flash_attention_kernel._update: _flash_attention_kernel()._update().
  NUM_SUBLANES: NUM_SUBLANES.
  _splash_vmem_limit_bytes: _splash_vmem_limit_bytes().
  _flash_attention_kernel: _flash_attention_kernel().
  _flash_attention_kernel._compute_body: _flash_attention_kernel()._compute_body().
  fixed_m_operands: fixed_m_operands().
  _flash_attention_kernel._compute_body.compute_body: _flash_attention_kernel()._compute_body().compute_body().
  _flash_attention_kernel.last_compute_body: _flash_attention_kernel().last_compute_body().
  _flash_attention_kernel._run_last: _flash_attention_kernel()._run_last().
  _local_blocks: _local_blocks().
  flash_attention_bshd._kernel_3d: flash_attention_bshd()._kernel_3d().
  _flash_attention_kernel._run_main: _flash_attention_kernel()._run_main().
  BlockSizes.__init__: BlockSizes#__init__().
  _flash_attention_kernel.init.init_fixed: _flash_attention_kernel().init().init_fixed().
  _flash_attention_kernel.body_fixed: _flash_attention_kernel().body_fixed().
  _flash_attention_kernel.body_online: _flash_attention_kernel().body_online().
  _flash_attention_kernel.body: _flash_attention_kernel().body().
  _flash_attention_kernel.last_body: _flash_attention_kernel().last_body().
  FIXED_M_RECENTER: FIXED_M_RECENTER.
  max_row_norm_per_head: max_row_norm_per_head().
  _exp2: _exp2().
  _splash_attention_forward.kv_index_map: _splash_attention_forward().kv_index_map().
  _splash_attention_forward.kv_column_map: _splash_attention_forward().kv_column_map().
  DEFAULT_MASK_VALUE: DEFAULT_MASK_VALUE.
  NT_DIM_NUMBERS: NT_DIM_NUMBERS.
  LOG2_E: LOG2_E.
  FIXED_M_SAFE_BOUND: FIXED_M_SAFE_BOUND.
  _splash_attention_forward.q_index_map: _splash_attention_forward().q_index_map().
  _splash_attention_forward.out_index_map: _splash_attention_forward().out_index_map().
  _splash_attention_forward.q_column_map: _splash_attention_forward().q_column_map().
  BlockSizes.__slots__: BlockSizes#__slots__.
  _flash_attention_kernel.init: _flash_attention_kernel().init().
  _flash_attention_kernel.init.init_online: _flash_attention_kernel().init().init_online().
  _flash_attention_kernel.end: _flash_attention_kernel().end().
---
# Module: [`src/vllm_torchtpu/kernels/diffusion_attention/kernel.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py)

## Classes
### <a id="BlockSizes"></a>`BlockSizes`
- def: [`src/vllm_torchtpu/kernels/diffusion_attention/kernel.py:170`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L170)
- doc: Pallas grid tiling for one splash-attention call.
- signature: `class BlockSizes:`
- protocol/private: <a id="BlockSizes.__init__"></a>`__init__`[`L182`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L182), <a id="BlockSizes.__slots__"></a>`__slots__`[`L180`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L180)
- used by: [`flash_attention_bshd`](kernel.md#flash_attention_bshd), [`_splash_attention_forward`](kernel.md#_splash_attention_forward), [`_local_blocks`](kernel.md#_local_blocks)

## Functions
- <a id="_flash_attention_kernel._compute_body"></a>`_compute_body(fixed: bool)` — [`L312`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L312)
- <a id="_exp2"></a>`_exp2(x: jax.Array)` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L164)
- <a id="_flash_attention_kernel"></a>`_flash_attention_kernel(mk_ref: Any, q_ref: Any, k_ref: Any, v_ref: Any, *refs: Any, mask_value: float, grid_width: int, bkv: int, bkv_compute: int, head_dim_v: int, kv_seq_len: int, use_fixed_m: bool, score_scale: float)` — [`L193`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L193) — Hybrid fixed-m / online-softmax flash attention over one (h, i) tile.
- <a id="flash_attention_bshd._kernel_3d"></a>`_kernel_3d(q_3d, k_3d, v_3d)` — [`L615`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L615)
- <a id="_local_blocks"></a>`_local_blocks(q_seq_len: int, kv_seq_len: int, block_q: int, block_kv: int, block_kv_compute: int)` — [`L512`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L512) — Clamps the requested blocks to one device-local call's extents.
- <a id="_flash_attention_kernel._run_last"></a>`_run_last()` — [`L330`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L330)
- <a id="_flash_attention_kernel._run_main"></a>`_run_main(body_fn)` — [`L327`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L327)
- <a id="_splash_attention_forward"></a>`_splash_attention_forward(q: jax.Array, k: jax.Array, v: jax.Array, mk: jax.Array, block_sizes: BlockSizes, *, score_scale: float, q_seq_len: int | None = None, kv_seq_len: int | None = None, use_fixed_m: bool = False, column_heads: tuple[int, int] | None = None)` — [`L379`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L379) — Runs the fused splash kernel over ``(heads, seq, dim)`` q/k/v.
- <a id="_splash_vmem_limit_bytes"></a>`_splash_vmem_limit_bytes()` — [`L150`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L150) — Mosaic scoped-VMEM ceiling per pallas_call, adapted to the device.
- <a id="_flash_attention_kernel._update"></a>`_update(slice_k, fixed: bool)` — [`L263`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L263) — One KV sub-block update; ``fixed`` selects the softmax variant.
- <a id="_flash_attention_kernel.body"></a>`body()` — [`L358`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L358)
- <a id="_flash_attention_kernel.body_fixed"></a>`body_fixed()` — [`L348`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L348)
- <a id="_flash_attention_kernel.body_online"></a>`body_online()` — [`L352`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L352)
- <a id="_flash_attention_kernel._compute_body.compute_body"></a>`compute_body(kv_compute_index, _)` — [`L313`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L313)
- <a id="_flash_attention_kernel.end"></a>`end()` — [`L370`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L370)
- <a id="fixed_m_operands"></a>`fixed_m_operands(query_scaled: jax.Array, key: jax.Array, *, gate: float, seq_axis: int = 2)` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L111) — Builds the ``(2, heads)`` fixed-m scalar-prefetch operand.
- <a id="flash_attention_bshd"></a>`flash_attention_bshd(query: jax.Array, key: jax.Array, value: jax.Array, *, scale: float | None, use_fixed_m: bool = True)` — [`L543`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L543) — Device-local custom splash attention, normalized.
- <a id="_flash_attention_kernel.init"></a>`init()` — [`L236`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L236)
- <a id="_flash_attention_kernel.init.init_fixed"></a>`init_fixed()` — [`L242`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L242)
- <a id="_flash_attention_kernel.init.init_online"></a>`init_online()` — [`L257`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L257)
- <a id="_splash_attention_forward.kv_column_map"></a>`kv_column_map(h, i, j, *_)` — [`L452`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L452)
- <a id="_splash_attention_forward.kv_index_map"></a>`kv_index_map(h, i, j, *_)` — [`L436`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L436)
- <a id="_flash_attention_kernel.last_body"></a>`last_body()` — [`L366`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L366)
- <a id="_flash_attention_kernel.last_compute_body"></a>`last_compute_body(kv_compute_index)` — [`L320`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L320)
- <a id="max_row_norm_per_head"></a>`max_row_norm_per_head(x: jax.Array, *, seq_axis: int = 2)` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L94) — Max L2 row norm per head over the device-local batch.
- <a id="_splash_attention_forward.out_index_map"></a>`out_index_map(h, i, j, *_)` — [`L439`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L439)
- <a id="_splash_attention_forward.q_column_map"></a>`q_column_map(h, i, j, *_)` — [`L449`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L449)
- <a id="_splash_attention_forward.q_index_map"></a>`q_index_map(h, i, j, *_)` — [`L433`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L433)

## Module values
- <a id="DEFAULT_MASK_VALUE"></a>`DEFAULT_MASK_VALUE` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L66)
- <a id="FIXED_M_RECENTER"></a>`FIXED_M_RECENTER` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L83)
- <a id="FIXED_M_SAFE_BOUND"></a>`FIXED_M_SAFE_BOUND` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L91)
- <a id="LOG2_E"></a>`LOG2_E` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L78)
- <a id="NT_DIM_NUMBERS"></a>`NT_DIM_NUMBERS` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L68)
- <a id="NUM_SUBLANES"></a>`NUM_SUBLANES` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/diffusion_attention/kernel.py#L67)

