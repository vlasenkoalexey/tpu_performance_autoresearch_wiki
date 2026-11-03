---
title: 'Module: src/vllm_torchtpu/gdn_pool_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/gdn_pool_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.gdn_pool_layout`/
symbols:
  derive_pooled_gdn_state_layout: derive_pooled_gdn_state_layout().
  pooled_gdn_state_itemsize: pooled_gdn_state_itemsize().
  PooledGDNStateLayout.required_bytes: PooledGDNStateLayout#required_bytes().
  pooled_gdn_state_dtypes: pooled_gdn_state_dtypes().
  pooled_gdn_conv_state_bytes: pooled_gdn_conv_state_bytes().
  pooled_gdn_ssm_state_bytes: pooled_gdn_ssm_state_bytes().
  PooledGDNStateLayout.ssm_tokens: PooledGDNStateLayout#ssm_tokens.
  PooledGDNStateLayout.required_tokens: PooledGDNStateLayout#required_tokens().
  PooledGDNStateLayout.conv_tokens: PooledGDNStateLayout#conv_tokens.
  unified_kv_layout_enabled_for_architecture: unified_kv_layout_enabled_for_architecture().
  PooledGDNStateLayout.granules_per_token: PooledGDNStateLayout#granules_per_token().
  DEFAULT_POOLED_GDN_CONV_STATE_DTYPE: DEFAULT_POOLED_GDN_CONV_STATE_DTYPE.
  QWEN_GDN_ARCHITECTURES: QWEN_GDN_ARCHITECTURES.
  PooledGDNStateLayout.ssm_granules: PooledGDNStateLayout#ssm_granules().
  PooledGDNStateLayout.conv_granules: PooledGDNStateLayout#conv_granules().
  PooledGDNStateLayout: PooledGDNStateLayout#
  POOLED_GDN_ARCHITECTURES: POOLED_GDN_ARCHITECTURES.
  GRANULE_BYTES: GRANULE_BYTES.
  PooledGDNStateLayout.token_bytes: PooledGDNStateLayout#token_bytes.
  PooledGDNStateLayout.ssm_bytes: PooledGDNStateLayout#ssm_bytes.
  PooledGDNStateLayout.conv_bytes: PooledGDNStateLayout#conv_bytes.
  DEFAULT_POOLED_GDN_SSM_STATE_DTYPE: DEFAULT_POOLED_GDN_SSM_STATE_DTYPE.
  _ITEMSIZE_BY_DTYPE: _ITEMSIZE_BY_DTYPE.
---
# Module: [`src/vllm_torchtpu/gdn_pool_layout.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py)

## Classes
### <a id="PooledGDNStateLayout"></a>`PooledGDNStateLayout`
- def: [`src/vllm_torchtpu/gdn_pool_layout.py:122`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L122) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- signature: `class PooledGDNStateLayout:`
- members:
  - <a id="PooledGDNStateLayout.conv_granules"></a>`conv_granules(self)` — [`L146`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L146)
  - <a id="PooledGDNStateLayout.granules_per_token"></a>`granules_per_token(self)` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L138)
  - <a id="PooledGDNStateLayout.required_bytes"></a>`required_bytes(self)` — [`L134`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L134)
  - <a id="PooledGDNStateLayout.required_tokens"></a>`required_tokens(self)` — [`L130`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L130)
  - <a id="PooledGDNStateLayout.ssm_granules"></a>`ssm_granules(self)` — [`L142`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L142)
  - <a id="PooledGDNStateLayout.conv_bytes"></a>`conv_bytes` — [`L124`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L124)
  - <a id="PooledGDNStateLayout.conv_tokens"></a>`conv_tokens` — [`L127`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L127)
  - <a id="PooledGDNStateLayout.ssm_bytes"></a>`ssm_bytes` — [`L123`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L123)
  - <a id="PooledGDNStateLayout.ssm_tokens"></a>`ssm_tokens` — [`L126`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L126) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="PooledGDNStateLayout.token_bytes"></a>`token_bytes` — [`L125`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L125)
- uses (calls/refs, reference-scoped): [`GRANULE_BYTES`](gdn_pool_layout.md#GRANULE_BYTES)
- used by: [`_derive_tpu_block_slot_config`](platforms/tpu_block_size_utils.md#_derive_tpu_block_slot_config), [`_pooled_kda_core`](layers/adapter/custom_ops/kda_attention_op.md#_pooled_kda_core), [`_hybrid_mamba_state_layout`](platforms/tpu_block_size_utils.md#_hybrid_mamba_state_layout), [`_pooled_kda_regions`](distributed/kv_transfer/raiden/pool_manifest.md#_pooled_kda_regions), [`derive_pooled_gdn_state_layout`](gdn_pool_layout.md#derive_pooled_gdn_state_layout)

## Functions
- <a id="derive_pooled_gdn_state_layout"></a>`derive_pooled_gdn_state_layout(*, ssm_bytes: int, conv_bytes: int, token_bytes: int)` — [`L150`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L150) — Derive the physical token extent of pooled GDN state regions. — documented in [custom-ops](../../../concepts/custom-ops.md)
- <a id="pooled_gdn_conv_state_bytes"></a>`pooled_gdn_conv_state_bytes(*, kernel_size: int, conv_dim: int)` — [`L99`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L99) — Live bytes of one slot's conv region: (kernel_size - 1) dense bf16
- <a id="pooled_gdn_ssm_state_bytes"></a>`pooled_gdn_ssm_state_bytes(*, num_v_heads: int, head_k_dim: int, head_v_dim: int, dtype: object = DEFAULT_POOLED_GDN_SSM_STATE_DTYPE)` — [`L110`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L110) — Live bytes of one slot's head-major, dense SSM region in ``dtype``.
- <a id="pooled_gdn_state_dtypes"></a>`pooled_gdn_state_dtypes(dtypes: tuple[object, ...])` — [`L66`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L66) — Resolve declared Conv/SSM dtypes to their pooled physical dtypes.
- <a id="pooled_gdn_state_itemsize"></a>`pooled_gdn_state_itemsize(dtype: object)` — [`L73`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L73)
- <a id="unified_kv_layout_enabled_for_architecture"></a>`unified_kv_layout_enabled_for_architecture(architecture: str | None)` — [`L83`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L83) — Whether `architecture` runs on the attention-shaped unified KV pool.

## Module values
- <a id="DEFAULT_POOLED_GDN_CONV_STATE_DTYPE"></a>`DEFAULT_POOLED_GDN_CONV_STATE_DTYPE` — [`L59`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L59)
- <a id="DEFAULT_POOLED_GDN_SSM_STATE_DTYPE"></a>`DEFAULT_POOLED_GDN_SSM_STATE_DTYPE` — [`L60`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L60)
- <a id="GRANULE_BYTES"></a>`GRANULE_BYTES` — [`L63`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L63)
- <a id="POOLED_GDN_ARCHITECTURES"></a>`POOLED_GDN_ARCHITECTURES` — [`L38`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L38)
- <a id="QWEN_GDN_ARCHITECTURES"></a>`QWEN_GDN_ARCHITECTURES` — [`L27`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L27)
- <a id="_ITEMSIZE_BY_DTYPE"></a>`_ITEMSIZE_BY_DTYPE` — [`L61`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gdn_pool_layout.py#L61)

