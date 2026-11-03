---
title: 'Module: src/vllm_torchtpu/platforms/tpu_block_size_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/platforms/tpu_block_size_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.platforms.tpu_block_size_utils`/
symbols:
  _derive_tpu_block_slot_config: _derive_tpu_block_slot_config().
  _hybrid_mamba_state_layout: _hybrid_mamba_state_layout().
  unified_kv_layout_enabled: unified_kv_layout_enabled().
  _localize_gdn_state_shapes_for_pcp: _localize_gdn_state_shapes_for_pcp().
  update_tpu_block_size_and_slot_config: update_tpu_block_size_and_slot_config().
  _log_tpu_block_size_derivation: _log_tpu_block_size_derivation().
  _optional_log_value: _optional_log_value().
  logger: logger.
  _tpu_attention_slot_size_bytes: _tpu_attention_slot_size_bytes().
  _resolve_tpu_cache_dtype: _resolve_tpu_cache_dtype().
  _align_block_to_backend: _align_block_to_backend().
  _tpu_attention_page_size_bytes: _tpu_attention_page_size_bytes().
  _pool_row_tokens: _pool_row_tokens().
  _tpu_attention_raw_payload_bytes_per_token: _tpu_attention_raw_payload_bytes_per_token().
  _HybridMambaModel.get_mamba_state_shape_from_config: _HybridMambaModel#get_mamba_state_shape_from_config().
  _SLOT_ALIGNMENT_BYTES: _SLOT_ALIGNMENT_BYTES.
  _round_up_to_multiple: _round_up_to_multiple().
  _TpuBlockSlotDerivation: _TpuBlockSlotDerivation#
  _HybridMambaModel.get_mamba_state_dtype_from_config: _HybridMambaModel#get_mamba_state_dtype_from_config().
  _TPU_CACHE_DTYPE_TO_TORCH_DTYPE: _TPU_CACHE_DTYPE_TO_TORCH_DTYPE.
  _HybridMambaModel: _HybridMambaModel#
  _TpuBlockSlotDerivation.backend: _TpuBlockSlotDerivation#backend.
  _TpuBlockSlotDerivation.block_size_source: _TpuBlockSlotDerivation#block_size_source.
  _TpuBlockSlotDerivation.input_block_size: _TpuBlockSlotDerivation#input_block_size.
  _TpuBlockSlotDerivation.backend_supported_kernel_block_sizes: _TpuBlockSlotDerivation#backend_supported_kernel_block_sizes.
  _TpuBlockSlotDerivation.backend_min_page_size: _TpuBlockSlotDerivation#backend_min_page_size.
  _TpuBlockSlotDerivation.user_block_size_floor: _TpuBlockSlotDerivation#user_block_size_floor.
  _TpuBlockSlotDerivation.mamba_raw_state_bytes: _TpuBlockSlotDerivation#mamba_raw_state_bytes.
  _TpuBlockSlotDerivation.mamba_required_state_bytes: _TpuBlockSlotDerivation#mamba_required_state_bytes.
  _TpuBlockSlotDerivation.fa_raw_payload_bytes_per_token: _TpuBlockSlotDerivation#fa_raw_payload_bytes_per_token.
  _TpuBlockSlotDerivation.fa_pool_row_tokens: _TpuBlockSlotDerivation#fa_pool_row_tokens.
  _TpuBlockSlotDerivation.fa_physical_bytes_per_pool_row: _TpuBlockSlotDerivation#fa_physical_bytes_per_pool_row.
  _TpuBlockSlotDerivation.fa_layout_padding_bytes_per_pool_row: _TpuBlockSlotDerivation#fa_layout_padding_bytes_per_pool_row.
  _TpuBlockSlotDerivation.mamba_fit_block_size: _TpuBlockSlotDerivation#mamba_fit_block_size.
  _TpuBlockSlotDerivation.final_block_size: _TpuBlockSlotDerivation#final_block_size.
  _TpuBlockSlotDerivation.fa_raw_payload_slot_bytes: _TpuBlockSlotDerivation#fa_raw_payload_slot_bytes.
  _TpuBlockSlotDerivation.fa_layout_padding_slot_bytes: _TpuBlockSlotDerivation#fa_layout_padding_slot_bytes.
  _TpuBlockSlotDerivation.fa_physical_slot_bytes: _TpuBlockSlotDerivation#fa_physical_slot_bytes.
  _TpuBlockSlotDerivation.final_block_slot_bytes: _TpuBlockSlotDerivation#final_block_slot_bytes.
  _TpuBlockSlotDerivation.fa_slot_tail_padding_bytes: _TpuBlockSlotDerivation#fa_slot_tail_padding_bytes.
  _TpuBlockSlotDerivation.mamba_layout_padding_bytes: _TpuBlockSlotDerivation#mamba_layout_padding_bytes.
  _TpuBlockSlotDerivation.mamba_slot_tail_padding_bytes: _TpuBlockSlotDerivation#mamba_slot_tail_padding_bytes.
  _TpuBlockSlotDerivation.mamba_slot_padding_bytes: _TpuBlockSlotDerivation#mamba_slot_padding_bytes.
---
# Module: [`src/vllm_torchtpu/platforms/tpu_block_size_utils.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py)

## Classes
### <a id="_HybridMambaModel"></a>`_HybridMambaModel`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/platforms/tpu_block_size_utils.py:35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L35)
- doc: Typing-only view of the mamba state classmethods on a hybrid model.
- signature: `class _HybridMambaModel(Protocol):`
- members:
  - <a id="_HybridMambaModel.get_mamba_state_dtype_from_config"></a>`get_mamba_state_dtype_from_config(cls, vllm_config: VllmConfig)` — [`L44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L44)
  - <a id="_HybridMambaModel.get_mamba_state_shape_from_config"></a>`get_mamba_state_shape_from_config(cls, vllm_config: VllmConfig)` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L39)
- used by: [`_hybrid_mamba_state_layout`](tpu_block_size_utils.md#_hybrid_mamba_state_layout)

### <a id="_TpuBlockSlotDerivation"></a>`_TpuBlockSlotDerivation`  ·  implements/extends _TypedDict
- def: [`src/vllm_torchtpu/platforms/tpu_block_size_utils.py:323`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L323)
- doc: The block-size derivation that the TPU platform logs.
- signature: `class _TpuBlockSlotDerivation(TypedDict):`
- members:
  - <a id="_TpuBlockSlotDerivation.backend"></a>`backend` — [`L326`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L326)
  - <a id="_TpuBlockSlotDerivation.backend_min_page_size"></a>`backend_min_page_size` — [`L330`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L330)
  - <a id="_TpuBlockSlotDerivation.backend_supported_kernel_block_sizes"></a>`backend_supported_kernel_block_sizes` — [`L329`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L329)
  - <a id="_TpuBlockSlotDerivation.block_size_source"></a>`block_size_source` — [`L327`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L327)
  - <a id="_TpuBlockSlotDerivation.fa_layout_padding_bytes_per_pool_row"></a>`fa_layout_padding_bytes_per_pool_row` — [`L337`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L337)
  - <a id="_TpuBlockSlotDerivation.fa_layout_padding_slot_bytes"></a>`fa_layout_padding_slot_bytes` — [`L341`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L341)
  - <a id="_TpuBlockSlotDerivation.fa_physical_bytes_per_pool_row"></a>`fa_physical_bytes_per_pool_row` — [`L336`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L336)
  - <a id="_TpuBlockSlotDerivation.fa_physical_slot_bytes"></a>`fa_physical_slot_bytes` — [`L342`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L342)
  - <a id="_TpuBlockSlotDerivation.fa_pool_row_tokens"></a>`fa_pool_row_tokens` — [`L335`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L335)
  - <a id="_TpuBlockSlotDerivation.fa_raw_payload_bytes_per_token"></a>`fa_raw_payload_bytes_per_token` — [`L334`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L334)
  - <a id="_TpuBlockSlotDerivation.fa_raw_payload_slot_bytes"></a>`fa_raw_payload_slot_bytes` — [`L340`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L340)
  - <a id="_TpuBlockSlotDerivation.fa_slot_tail_padding_bytes"></a>`fa_slot_tail_padding_bytes` — [`L344`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L344)
  - <a id="_TpuBlockSlotDerivation.final_block_size"></a>`final_block_size` — [`L339`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L339)
  - <a id="_TpuBlockSlotDerivation.final_block_slot_bytes"></a>`final_block_slot_bytes` — [`L343`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L343)
  - <a id="_TpuBlockSlotDerivation.input_block_size"></a>`input_block_size` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L328)
  - <a id="_TpuBlockSlotDerivation.mamba_fit_block_size"></a>`mamba_fit_block_size` — [`L338`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L338)
  - <a id="_TpuBlockSlotDerivation.mamba_layout_padding_bytes"></a>`mamba_layout_padding_bytes` — [`L345`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L345)
  - <a id="_TpuBlockSlotDerivation.mamba_raw_state_bytes"></a>`mamba_raw_state_bytes` — [`L332`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L332)
  - <a id="_TpuBlockSlotDerivation.mamba_required_state_bytes"></a>`mamba_required_state_bytes` — [`L333`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L333)
  - <a id="_TpuBlockSlotDerivation.mamba_slot_padding_bytes"></a>`mamba_slot_padding_bytes` — [`L347`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L347)
  - <a id="_TpuBlockSlotDerivation.mamba_slot_tail_padding_bytes"></a>`mamba_slot_tail_padding_bytes` — [`L346`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L346)
  - <a id="_TpuBlockSlotDerivation.user_block_size_floor"></a>`user_block_size_floor` — [`L331`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L331)
- used by: [`_derive_tpu_block_slot_config`](tpu_block_size_utils.md#_derive_tpu_block_slot_config), [`_log_tpu_block_size_derivation`](tpu_block_size_utils.md#_log_tpu_block_size_derivation)

## Functions
- <a id="_align_block_to_backend"></a>`_align_block_to_backend(block_size: int, supported)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L87) — Smallest manager block >= block_size the backend can serve.
- <a id="_derive_tpu_block_slot_config"></a>`_derive_tpu_block_slot_config(vllm_config: VllmConfig, backend_cls, *, input_block_size: int)` — [`L350`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L350) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_hybrid_mamba_state_layout"></a>`_hybrid_mamba_state_layout(vllm_config: VllmConfig, fa_physical_bytes_per_token: int)` — [`L202`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L202) — documented in [gated-deltanet-kernels](../../../../concepts/gated-deltanet-kernels.md)
- <a id="_localize_gdn_state_shapes_for_pcp"></a>`_localize_gdn_state_shapes_for_pcp(vllm_config: VllmConfig, tp_local_shapes: tuple[tuple[int, ...], ...], pcp_size: int)` — [`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L160) — Apply GDN's Q/K replication and V sharding to TP-local shapes. — documented in [gated-deltanet-kernels](../../../../concepts/gated-deltanet-kernels.md)
- <a id="_log_tpu_block_size_derivation"></a>`_log_tpu_block_size_derivation(derivation: _TpuBlockSlotDerivation)` — [`L485`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L485) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_optional_log_value"></a>`_optional_log_value(value: int | None)` — [`L481`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L481)
- <a id="_pool_row_tokens"></a>`_pool_row_tokens(vllm_config: VllmConfig, backend_cls)` — [`L138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L138) — Tokens per physical pool row (the pool's `shape[1]` unit).
- <a id="_resolve_tpu_cache_dtype"></a>`_resolve_tpu_cache_dtype(vllm_config: VllmConfig)` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L103)
- <a id="_round_up_to_multiple"></a>`_round_up_to_multiple(value: int, multiple: int)` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L83)
- <a id="_tpu_attention_page_size_bytes"></a>`_tpu_attention_page_size_bytes(vllm_config: VllmConfig, backend_cls)` — [`L134`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L134)
- <a id="_tpu_attention_raw_payload_bytes_per_token"></a>`_tpu_attention_raw_payload_bytes_per_token(vllm_config: VllmConfig)` — [`L310`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L310)
- <a id="_tpu_attention_slot_size_bytes"></a>`_tpu_attention_slot_size_bytes(vllm_config: VllmConfig, backend_cls, block_size: int)` — [`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L118) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="unified_kv_layout_enabled"></a>`unified_kv_layout_enabled(vllm_config: VllmConfig)` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L54) — Whether the deployment uses the attention-shaped unified KV pool. — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="update_tpu_block_size_and_slot_config"></a>`update_tpu_block_size_and_slot_config(vllm_config: VllmConfig, backend_cls)` — [`L528`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L528) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)

## Module values
- <a id="_SLOT_ALIGNMENT_BYTES"></a>`_SLOT_ALIGNMENT_BYTES` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L80)
- <a id="_TPU_CACHE_DTYPE_TO_TORCH_DTYPE"></a>`_TPU_CACHE_DTYPE_TO_TORCH_DTYPE` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L68)
- <a id="logger"></a>`logger` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_block_size_utils.py#L51)

