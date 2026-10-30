---
title: 'Module: torchtitan/experiments/rl/models/attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.attention`/
symbols:
  VLLMAttentionWrapper.__init__: VLLMAttentionWrapper#__init__().
  PyTorchVarlenInnerAttentionImpl.enable_gqa: PyTorchVarlenInnerAttentionImpl#enable_gqa.
  PyTorchVarlenInnerAttentionImpl.forward: PyTorchVarlenInnerAttentionImpl#forward().
  VLLMAttentionWrapper.Config: VLLMAttentionWrapper#Config#
  VLLMAttentionWrapper: VLLMAttentionWrapper#
  VLLMAttentionWrapper.scale: VLLMAttentionWrapper#scale.
  VLLMAttentionWrapper.forward: VLLMAttentionWrapper#forward().
  VLLMAttentionWrapper.vllm_attn: VLLMAttentionWrapper#vllm_attn.
  PyTorchVarlenInnerAttentionImpl.out_transform: PyTorchVarlenInnerAttentionImpl#out_transform.
  PyTorchVarlenInnerAttentionBackend.get_impl_cls: PyTorchVarlenInnerAttentionBackend#get_impl_cls().
  PyTorchVarlenInnerAttentionBackend.get_builder_cls.PyTorchVarlenInnerAttentionMetadataBuilder._cudagraph_support: PyTorchVarlenInnerAttentionBackend#get_builder_cls().PyTorchVarlenInnerAttentionMetadataBuilder#_cudagraph_support.
  VLLMAttentionWrapper.hidden_size: VLLMAttentionWrapper#hidden_size.
  VLLMAttentionWrapper.Config.hidden_size: VLLMAttentionWrapper#Config#hidden_size.
  VLLMAttentionWrapper.Config.num_heads: VLLMAttentionWrapper#Config#num_heads.
  VLLMAttentionWrapper.Config.num_kv_heads: VLLMAttentionWrapper#Config#num_kv_heads.
  VLLMAttentionWrapper.Config.head_dim: VLLMAttentionWrapper#Config#head_dim.
  VLLMAttentionWrapper.Config.scale: VLLMAttentionWrapper#Config#scale.
  VLLMAttentionWrapper.Config.sliding_window_size: VLLMAttentionWrapper#Config#sliding_window_size.
  logger: logger.
  PyTorchVarlenInnerAttentionBackend.get_builder_cls.PyTorchVarlenInnerAttentionMetadataBuilder: PyTorchVarlenInnerAttentionBackend#get_builder_cls().PyTorchVarlenInnerAttentionMetadataBuilder#
  VLLMAttentionWrapper._layer_counter: VLLMAttentionWrapper#_layer_counter.
  PyTorchVarlenInnerAttentionImpl: PyTorchVarlenInnerAttentionImpl#
  PyTorchVarlenInnerAttentionBackend: PyTorchVarlenInnerAttentionBackend#
  PyTorchVarlenInnerAttentionBackend.get_name: PyTorchVarlenInnerAttentionBackend#get_name().
  PyTorchVarlenInnerAttentionBackend.get_builder_cls: PyTorchVarlenInnerAttentionBackend#get_builder_cls().
  PyTorchVarlenInnerAttentionImpl.__init__: PyTorchVarlenInnerAttentionImpl#__init__().
  VLLMAttentionWrapper.num_heads: VLLMAttentionWrapper#num_heads.
  VLLMAttentionWrapper.num_kv_heads: VLLMAttentionWrapper#num_kv_heads.
  VLLMAttentionWrapper.head_dim: VLLMAttentionWrapper#head_dim.
---
# Module: [`torchtitan/experiments/rl/models/attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py)

## Classes
### <a id="PyTorchVarlenInnerAttentionBackend"></a>`PyTorchVarlenInnerAttentionBackend`
- def: [`torchtitan/experiments/rl/models/attention.py:38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L38)
- doc: Custom vLLM attention backend using PyTorch's native FlashAttention kernel.
- signature: `class PyTorchVarlenInnerAttentionBackend(FlashAttentionBackend):`
- members:
  - <a id="PyTorchVarlenInnerAttentionBackend.get_builder_cls"></a>`get_builder_cls()` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L61)
  - <a id="PyTorchVarlenInnerAttentionBackend.get_impl_cls"></a>`get_impl_cls()` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L57)
  - <a id="PyTorchVarlenInnerAttentionBackend.get_name"></a>`get_name()` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L51)
- uses (calls/refs, reference-scoped): [`PyTorchVarlenInnerAttentionImpl`](attention.md#PyTorchVarlenInnerAttentionImpl)

### <a id="PyTorchVarlenInnerAttentionBackend.get_builder_cls.PyTorchVarlenInnerAttentionMetadataBuilder"></a>`PyTorchVarlenInnerAttentionBackend.get_builder_cls.PyTorchVarlenInnerAttentionMetadataBuilder`
- def: [`torchtitan/experiments/rl/models/attention.py:62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L62)
- signature: `class PyTorchVarlenInnerAttentionMetadataBuilder(FlashAttentionMetadataBuilder):`
- protocol/private: <a id="PyTorchVarlenInnerAttentionBackend.get_builder_cls.PyTorchVarlenInnerAttentionMetadataBuilder._cudagraph_support"></a>`_cudagraph_support`[`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L63)

### <a id="PyTorchVarlenInnerAttentionImpl"></a>`PyTorchVarlenInnerAttentionImpl`
- def: [`torchtitan/experiments/rl/models/attention.py:68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L68)
- members:
  - <a id="PyTorchVarlenInnerAttentionImpl.forward"></a>`forward(self, layer: torch.nn.Module, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, kv_cache: torch.Tensor, attn_metadata: FlashAttentionMetadata, output: torch.Tensor | None = None, output_scale: torch.Tensor | None = None, output_block_scale: torch.Tensor | None = None)` — [`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L105) — Forward pass with FlashAttention.
  - <a id="PyTorchVarlenInnerAttentionImpl.enable_gqa"></a>`enable_gqa` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L82)
  - <a id="PyTorchVarlenInnerAttentionImpl.out_transform"></a>`out_transform` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L80)
- protocol/private: <a id="PyTorchVarlenInnerAttentionImpl.__init__"></a>`__init__`[`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L75)
- uses (calls/refs, reference-scoped): [`is_in_batch_invariant_mode`](../../../distributed/utils.md#is_in_batch_invariant_mode), [`warn_once`](../../../tools/logging.md#warn_once), [`get_cuda_flash_attention_impl`](../../../tools/utils.md#get_cuda_flash_attention_impl), [`logger`](attention.md#logger)
- used by: [`get_impl_cls`](attention.md#PyTorchVarlenInnerAttentionBackend.get_impl_cls)

### <a id="VLLMAttentionWrapper"></a>`VLLMAttentionWrapper`  ·  implements/extends Module
- def: [`torchtitan/experiments/rl/models/attention.py:254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L254)
- doc: Adapter from TorchTitan tensor layout to `vllm.Attention`.
- signature: `class VLLMAttentionWrapper(Module):`
- members:
  - <a id="VLLMAttentionWrapper.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, *, attention_masks: AttentionMasksType | None = None, **kwargs)` — [`L335`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L335) — Run vLLM paged attention on local (non-DTensor) tensors.
  - <a id="VLLMAttentionWrapper.head_dim"></a>`head_dim` — [`L315`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L315)
  - <a id="VLLMAttentionWrapper.hidden_size"></a>`hidden_size` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L312)
  - <a id="VLLMAttentionWrapper.num_heads"></a>`num_heads` — [`L313`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L313)
  - <a id="VLLMAttentionWrapper.num_kv_heads"></a>`num_kv_heads` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L314)
  - <a id="VLLMAttentionWrapper.scale"></a>`scale` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L316)
  - <a id="VLLMAttentionWrapper.vllm_attn"></a>`vllm_attn` — [`L324`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L324)
- protocol/private: <a id="VLLMAttentionWrapper.__init__"></a>`__init__`[`L280`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L280), <a id="VLLMAttentionWrapper._layer_counter"></a>`_layer_counter`[`L268`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L268)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`AttentionMasksType`](../../../models/common/attention.md#AttentionMasksType), [`Config`](attention.md#VLLMAttentionWrapper.Config), [`head_dim`](attention.md#VLLMAttentionWrapper.Config.head_dim), [`hidden_size`](attention.md#VLLMAttentionWrapper.Config.hidden_size), [`num_heads`](attention.md#VLLMAttentionWrapper.Config.num_heads), [`num_kv_heads`](attention.md#VLLMAttentionWrapper.Config.num_kv_heads), [`scale`](attention.md#VLLMAttentionWrapper.Config.scale), [`sliding_window_size`](attention.md#VLLMAttentionWrapper.Config.sliding_window_size)
- used by: [`Module`](../../../protocols/module.md#Module), [`_replace_vllm_layer_configs`](vllm_wrapper.md#_replace_vllm_layer_configs)

### <a id="VLLMAttentionWrapper.Config"></a>`VLLMAttentionWrapper.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/models/attention.py:271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L271)
- signature: `class Config(Module.Config):`
- members:
  - <a id="VLLMAttentionWrapper.Config.head_dim"></a>`head_dim` — [`L275`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L275)
  - <a id="VLLMAttentionWrapper.Config.hidden_size"></a>`hidden_size` — [`L272`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L272)
  - <a id="VLLMAttentionWrapper.Config.num_heads"></a>`num_heads` — [`L273`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L273)
  - <a id="VLLMAttentionWrapper.Config.num_kv_heads"></a>`num_kv_heads` — [`L274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L274)
  - <a id="VLLMAttentionWrapper.Config.scale"></a>`scale` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L276)
  - <a id="VLLMAttentionWrapper.Config.sliding_window_size"></a>`sliding_window_size` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L277) — ---
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`_replace_vllm_layer_configs`](vllm_wrapper.md#_replace_vllm_layer_configs), [`__init__`](attention.md#VLLMAttentionWrapper.__init__), [`vllm_attn`](attention.md#VLLMAttentionWrapper.vllm_attn), [`hidden_size`](attention.md#VLLMAttentionWrapper.hidden_size)

## Module values
- <a id="logger"></a>`logger` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/attention.py#L34)

