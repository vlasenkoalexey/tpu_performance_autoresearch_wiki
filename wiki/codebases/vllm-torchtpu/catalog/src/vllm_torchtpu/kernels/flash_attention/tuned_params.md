---
title: 'Module: src/vllm_torchtpu/kernels/flash_attention/tuned_params.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/flash_attention/tuned_params.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.flash_attention.tuned_params`/
symbols:
  _vision_tuning_key: _vision_tuning_key().
  make_tuning_key: make_tuning_key().
  TunableParams: TunableParams#
  get_tuned_params: get_tuned_params().
  tuned_params_mapping.tuned_params_mapping: tuned_params_mapping.tuned_params_mapping.
  TuningKey: TuningKey#
  TuningKey.device_kind: TuningKey#device_kind.
  TuningKey.batch_size: TuningKey#batch_size.
  TuningKey.num_heads: TuningKey#num_heads.
  TuningKey.q_seq_len: TuningKey#q_seq_len.
  TuningKey.kv_seq_len: TuningKey#kv_seq_len.
  TuningKey.head_dim: TuningKey#head_dim.
  TuningKey.q_dtype: TuningKey#q_dtype.
  TuningKey.kv_dtype: TuningKey#kv_dtype.
  TuningKey.v_dtype: TuningKey#v_dtype.
  TuningKey.causal: TuningKey#causal.
  TuningKey.has_segment_ids: TuningKey#has_segment_ids.
  TuningKey.has_attention_bias: TuningKey#has_attention_bias.
  TuningKey.vmem_limit_bytes: TuningKey#vmem_limit_bytes.
  TunableParams.block_q: TunableParams#block_q.
  TunableParams.block_k_major: TunableParams#block_k_major.
  TunableParams.block_k: TunableParams#block_k.
  TunableParams.block_b: TunableParams#block_b.
  current_device_kind: current_device_kind().
---
# Module: [`src/vllm_torchtpu/kernels/flash_attention/tuned_params.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py)

## Classes
### <a id="TunableParams"></a>`TunableParams`
- def: [`src/vllm_torchtpu/kernels/flash_attention/tuned_params.py:43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L43)
- signature: `class TunableParams:`
- members:
  - <a id="TunableParams.block_b"></a>`block_b` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L47)
  - <a id="TunableParams.block_k"></a>`block_k` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L46)
  - <a id="TunableParams.block_k_major"></a>`block_k_major` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L45)
  - <a id="TunableParams.block_q"></a>`block_q` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L44)
- used by: [`flash_attention`](kernel.md#flash_attention), [`get_tuned_params`](tuned_params.md#get_tuned_params), [`tuned_params_mapping`](tuned_params.md#tuned_params_mapping.tuned_params_mapping)

### <a id="TuningKey"></a>`TuningKey`
- def: [`src/vllm_torchtpu/kernels/flash_attention/tuned_params.py:24`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L24)
- doc: Static inputs which can change the best flash-attention tiling.
- signature: `class TuningKey:`
- members:
  - <a id="TuningKey.batch_size"></a>`batch_size` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L28)
  - <a id="TuningKey.causal"></a>`causal` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L36)
  - <a id="TuningKey.device_kind"></a>`device_kind` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L27)
  - <a id="TuningKey.has_attention_bias"></a>`has_attention_bias` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L38)
  - <a id="TuningKey.has_segment_ids"></a>`has_segment_ids` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L37)
  - <a id="TuningKey.head_dim"></a>`head_dim` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L32)
  - <a id="TuningKey.kv_dtype"></a>`kv_dtype` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L34)
  - <a id="TuningKey.kv_seq_len"></a>`kv_seq_len` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L31)
  - <a id="TuningKey.num_heads"></a>`num_heads` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L29)
  - <a id="TuningKey.q_dtype"></a>`q_dtype` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L33)
  - <a id="TuningKey.q_seq_len"></a>`q_seq_len` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L30)
  - <a id="TuningKey.v_dtype"></a>`v_dtype` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L35)
  - <a id="TuningKey.vmem_limit_bytes"></a>`vmem_limit_bytes` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L39)
- used by: [`_vision_tuning_key`](tuned_params.md#_vision_tuning_key), [`make_tuning_key`](tuned_params.md#make_tuning_key), [`get_tuned_params`](tuned_params.md#get_tuned_params), [`tuned_params_mapping`](tuned_params.md#tuned_params_mapping.tuned_params_mapping)

## Functions
- <a id="_vision_tuning_key"></a>`_vision_tuning_key(*, num_heads: int, seq_len: int, head_dim: int)` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L50)
- <a id="current_device_kind"></a>`current_device_kind()` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L133) — Return the JAX device kind used to compile the kernel.
- <a id="get_tuned_params"></a>`get_tuned_params(tuning_key: TuningKey)` — [`L170`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L170)
- <a id="make_tuning_key"></a>`make_tuning_key(q, k, v, *, causal: bool, has_segment_ids: bool, has_attention_bias: bool, vmem_limit_bytes: int | None, device_kind: str | None = None)` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L139) — Build a lookup key from static kernel inputs.

## Module values
- <a id="tuned_params_mapping.tuned_params_mapping"></a>`tuned_params_mapping` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/flash_attention/tuned_params.py#L70)

