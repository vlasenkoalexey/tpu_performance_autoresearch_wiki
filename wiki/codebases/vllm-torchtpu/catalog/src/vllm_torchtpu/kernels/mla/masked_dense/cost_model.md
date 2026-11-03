---
title: 'Module: src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.masked_dense.cost_model`/
symbols:
  GLM52_TPU7X_PREFILL_COST_MODEL: GLM52_TPU7X_PREFILL_COST_MODEL.
  MaskedDensePrefillCostModel: MaskedDensePrefillCostModel#
  MaskedDensePrefillCostModel.sparse_fixed_ns: MaskedDensePrefillCostModel#sparse_fixed_ns.
  MaskedDensePrefillCostModel.sparse_token_ns: MaskedDensePrefillCostModel#sparse_token_ns.
  KV_BLOCK_SIZE: KV_BLOCK_SIZE.
  QUERY_BLOCK_SIZE: QUERY_BLOCK_SIZE.
  MaskedDensePrefillCostModel.analytic_fixed_ns: MaskedDensePrefillCostModel#analytic_fixed_ns.
  MaskedDensePrefillCostModel.analytic_token_ns: MaskedDensePrefillCostModel#analytic_token_ns.
  MaskedDensePrefillCostModel.bitmap_fixed_ns: MaskedDensePrefillCostModel#bitmap_fixed_ns.
  MaskedDensePrefillCostModel.bitmap_token_ns: MaskedDensePrefillCostModel#bitmap_token_ns.
  MaskedDensePrefillCostModel.q_kv_block_ns: MaskedDensePrefillCostModel#q_kv_block_ns.
---
# Module: [`src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py)

## Classes
### <a id="MaskedDensePrefillCostModel"></a>`MaskedDensePrefillCostModel`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py:19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L19)
- signature: `class MaskedDensePrefillCostModel(NamedTuple):`
- members:
  - <a id="MaskedDensePrefillCostModel.analytic_fixed_ns"></a>`analytic_fixed_ns` — [`L20`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L20)
  - <a id="MaskedDensePrefillCostModel.analytic_token_ns"></a>`analytic_token_ns` — [`L21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L21)
  - <a id="MaskedDensePrefillCostModel.bitmap_fixed_ns"></a>`bitmap_fixed_ns` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L22)
  - <a id="MaskedDensePrefillCostModel.bitmap_token_ns"></a>`bitmap_token_ns` — [`L23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L23)
  - <a id="MaskedDensePrefillCostModel.q_kv_block_ns"></a>`q_kv_block_ns` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L24)
  - <a id="MaskedDensePrefillCostModel.sparse_fixed_ns"></a>`sparse_fixed_ns` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L25)
  - <a id="MaskedDensePrefillCostModel.sparse_token_ns"></a>`sparse_token_ns` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L26)
- used by: [`select_tier`](../dispatch.md#select_tier), [`GLM52_TPU7X_PREFILL_COST_MODEL`](cost_model.md#GLM52_TPU7X_PREFILL_COST_MODEL), [`masked_dense_cost`](../dispatch.md#select_tier.masked_dense_cost)

## Module values
- <a id="GLM52_TPU7X_PREFILL_COST_MODEL"></a>`GLM52_TPU7X_PREFILL_COST_MODEL` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L40)
- <a id="KV_BLOCK_SIZE"></a>`KV_BLOCK_SIZE` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L30)
- <a id="QUERY_BLOCK_SIZE"></a>`QUERY_BLOCK_SIZE` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/cost_model.py#L31)

