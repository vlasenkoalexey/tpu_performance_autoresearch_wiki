---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.flash_attention`/
symbols:
  flash_attention_qk_softmax: flash_attention_qk_softmax().
  flash_attention_pv: flash_attention_pv().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py)

## Functions
- <a id="flash_attention_pv"></a>`flash_attention_pv(p: jax.Array, v: jax.Array, alpha_list: list[jax.Array], o_prev: jax.Array, step: jax.Array, is_last_k: SmemWrapper, cfgs: configs.RpaConfigs, v_scale: jax.Array | None = None)` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py#L124) — Flash attention kernel. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="flash_attention_qk_softmax"></a>`flash_attention_qk_softmax(step: jax.Array, q: jax.Array, k: jax.Array, m_prev: jax.Array, l_prev: jax.Array, is_last_k: SmemWrapper, *, custom_mask: jax.Array, cfgs: configs.RpaConfigs, bq_start: int, k_scale: jax.Array | float | None = None)` — [`L23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/flash_attention.py#L23) — Flash attention kernel. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)

