---
title: 'Module: torchtitan/experiments/rl/models/gdn.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/gdn.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.gdn`/VLLMInnerGatedDeltaNet#
symbols:
  VLLMInnerGatedDeltaNet.get_state_shape: get_state_shape().
  VLLMInnerGatedDeltaNet._split_qkv: _split_qkv().
  VLLMInnerGatedDeltaNet._forward: _forward().
  VLLMInnerGatedDeltaNet.forward: forward().
  VLLMInnerGatedDeltaNet.conv_kernel_size: conv_kernel_size.
  VLLMInnerGatedDeltaNet.head_k_dim: head_k_dim.
  VLLMInnerGatedDeltaNet.prefix: prefix.
  VLLMInnerGatedDeltaNet.local_key_dim: local_key_dim.
  VLLMInnerGatedDeltaNet.local_num_k_heads: local_num_k_heads.
  VLLMInnerGatedDeltaNet.Config: Config#
  VLLMInnerGatedDeltaNet.local_num_v_heads: local_num_v_heads.
  VLLMInnerGatedDeltaNet.num_k_heads: num_k_heads.
  VLLMInnerGatedDeltaNet.num_v_heads: num_v_heads.
  VLLMInnerGatedDeltaNet.head_v_dim: head_v_dim.
  VLLMInnerGatedDeltaNet.tensor_parallel_size: tensor_parallel_size.
  VLLMInnerGatedDeltaNet.cache_config: cache_config.
  VLLMInnerGatedDeltaNet.get_state_dtype: get_state_dtype().
  VLLMInnerGatedDeltaNet: ''
  VLLMInnerGatedDeltaNet.num_speculative_tokens: num_speculative_tokens.
  VLLMInnerGatedDeltaNet.__init__: __init__().
  VLLMInnerGatedDeltaNet.Config.layer_idx: Config#layer_idx.
  VLLMInnerGatedDeltaNet.Config.num_k_heads: Config#num_k_heads.
  VLLMInnerGatedDeltaNet.Config.num_v_heads: Config#num_v_heads.
  VLLMInnerGatedDeltaNet.Config.head_k_dim: Config#head_k_dim.
  VLLMInnerGatedDeltaNet.Config.head_v_dim: Config#head_v_dim.
  VLLMInnerGatedDeltaNet.Config.conv_kernel_size: Config#conv_kernel_size.
  VLLMInnerGatedDeltaNet.kv_cache: kv_cache.
  VLLMInnerGatedDeltaNet.model_config: model_config.
  VLLMInnerGatedDeltaNet.mamba_type: mamba_type().
---
# Module: [`torchtitan/experiments/rl/models/gdn.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py)

## Classes
### <a id="VLLMInnerGatedDeltaNet"></a>`VLLMInnerGatedDeltaNet`  ·  implements/extends Module
- def: [`torchtitan/experiments/rl/models/gdn.py:53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L53)
- doc: Paged-cache inner GDN implementation.
- signature: `class VLLMInnerGatedDeltaNet(Module, MambaBase):`
- members:
  - <a id="VLLMInnerGatedDeltaNet._forward"></a>`_forward(self, mixed_qkv: torch.Tensor, a: torch.Tensor, b: torch.Tensor, conv_weight: torch.Tensor, conv_bias: torch.Tensor | None, A_log: torch.Tensor, dt_bias: torch.Tensor, output: torch.Tensor)` — [`L191`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L191) — Run convolution and recurrence against vLLM's paged state in place.
  - <a id="VLLMInnerGatedDeltaNet._split_qkv"></a>`_split_qkv(self, mixed_qkv: torch.Tensor)` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L165) — Split local fused channels and add a singleton batch dim.
  - <a id="VLLMInnerGatedDeltaNet.forward"></a>`forward(self, query_TC: torch.Tensor, key_TC: torch.Tensor, value_TC: torch.Tensor, a_TH: torch.Tensor, b_TH: torch.Tensor, conv_q_weight_C1W: torch.Tensor, conv_k_weight_C1W: torch.Tensor, conv_v_weight_C1W: torch.Tensor, A_log_H: torch.Tensor, dt_bias_H: torch.Tensor, cu_seqlens: torch.Tensor, *, key_head_dim: int, value_head_dim: int, use_varlen_kernels: bool = False)` — [`L359`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L359) — Run the flattened vLLM cache operation on rank-local tensors.
  - <a id="VLLMInnerGatedDeltaNet.get_state_dtype"></a>`get_state_dtype(self)` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L137) — Return the (conv_state, ssm_state) cache dtypes.
  - <a id="VLLMInnerGatedDeltaNet.get_state_shape"></a>`get_state_shape(self)` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L149) — Return the per-slot (conv_state, ssm_state) cache shapes.
  - <a id="VLLMInnerGatedDeltaNet.mamba_type"></a>`mamba_type(self)` — [`L134`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L134)
  - <a id="VLLMInnerGatedDeltaNet.cache_config"></a>`cache_config` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L78)
  - <a id="VLLMInnerGatedDeltaNet.conv_kernel_size"></a>`conv_kernel_size` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L92)
  - <a id="VLLMInnerGatedDeltaNet.head_k_dim"></a>`head_k_dim` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L90)
  - <a id="VLLMInnerGatedDeltaNet.head_v_dim"></a>`head_v_dim` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L91)
  - <a id="VLLMInnerGatedDeltaNet.kv_cache"></a>`kv_cache` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L125)
  - <a id="VLLMInnerGatedDeltaNet.local_key_dim"></a>`local_key_dim` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L107)
  - <a id="VLLMInnerGatedDeltaNet.local_num_k_heads"></a>`local_num_k_heads` — [`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L105)
  - <a id="VLLMInnerGatedDeltaNet.local_num_v_heads"></a>`local_num_v_heads` — [`L106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L106)
  - <a id="VLLMInnerGatedDeltaNet.model_config"></a>`model_config` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L77)
  - <a id="VLLMInnerGatedDeltaNet.num_k_heads"></a>`num_k_heads` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L88)
  - <a id="VLLMInnerGatedDeltaNet.num_speculative_tokens"></a>`num_speculative_tokens` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L80)
  - <a id="VLLMInnerGatedDeltaNet.num_v_heads"></a>`num_v_heads` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L89)
  - <a id="VLLMInnerGatedDeltaNet.prefix"></a>`prefix` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L127)
  - <a id="VLLMInnerGatedDeltaNet.tensor_parallel_size"></a>`tensor_parallel_size` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L76)
- protocol/private: <a id="VLLMInnerGatedDeltaNet.__init__"></a>`__init__`[`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L72)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`is_in_batch_invariant_mode`](../../../distributed/utils.md#is_in_batch_invariant_mode), [`Config`](gdn.md#VLLMInnerGatedDeltaNet.Config), [`conv_kernel_size`](gdn.md#VLLMInnerGatedDeltaNet.Config.conv_kernel_size), [`head_k_dim`](gdn.md#VLLMInnerGatedDeltaNet.Config.head_k_dim), [`head_v_dim`](gdn.md#VLLMInnerGatedDeltaNet.Config.head_v_dim), [`layer_idx`](gdn.md#VLLMInnerGatedDeltaNet.Config.layer_idx), [`num_k_heads`](gdn.md#VLLMInnerGatedDeltaNet.Config.num_k_heads), [`num_v_heads`](gdn.md#VLLMInnerGatedDeltaNet.Config.num_v_heads)
- used by: [`Module`](../../../protocols/module.md#Module), [`_replace_vllm_layer_configs`](vllm_wrapper.md#_replace_vllm_layer_configs)

### <a id="VLLMInnerGatedDeltaNet.Config"></a>`VLLMInnerGatedDeltaNet.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/models/gdn.py:64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L64)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VLLMInnerGatedDeltaNet.Config.conv_kernel_size"></a>`conv_kernel_size` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L70)
  - <a id="VLLMInnerGatedDeltaNet.Config.head_k_dim"></a>`head_k_dim` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L68)
  - <a id="VLLMInnerGatedDeltaNet.Config.head_v_dim"></a>`head_v_dim` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L69)
  - <a id="VLLMInnerGatedDeltaNet.Config.layer_idx"></a>`layer_idx` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L65)
  - <a id="VLLMInnerGatedDeltaNet.Config.num_k_heads"></a>`num_k_heads` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L66)
  - <a id="VLLMInnerGatedDeltaNet.Config.num_v_heads"></a>`num_v_heads` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/gdn.py#L67)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`_replace_vllm_layer_configs`](vllm_wrapper.md#_replace_vllm_layer_configs), [`conv_kernel_size`](gdn.md#VLLMInnerGatedDeltaNet.conv_kernel_size), [`head_k_dim`](gdn.md#VLLMInnerGatedDeltaNet.head_k_dim), [`prefix`](gdn.md#VLLMInnerGatedDeltaNet.prefix), [`head_v_dim`](gdn.md#VLLMInnerGatedDeltaNet.head_v_dim), [`num_k_heads`](gdn.md#VLLMInnerGatedDeltaNet.num_k_heads), [`num_v_heads`](gdn.md#VLLMInnerGatedDeltaNet.num_v_heads), [`__init__`](gdn.md#VLLMInnerGatedDeltaNet.__init__)

