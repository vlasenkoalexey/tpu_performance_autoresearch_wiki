---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.online_fp8`/
symbols:
  validate_online_fp8: validate_online_fp8().
  attach_online_fp8: attach_online_fp8().
  quantize_online_fp8: quantize_online_fp8().
  map_online_fp8: map_online_fp8().
  OnlineFp8Policy.select: OnlineFp8Policy#select().
  OnlineFp8Policy: OnlineFp8Policy#
  OnlineFp8Policy.apply_mapper: OnlineFp8Policy#apply_mapper().
  OnlineFp8Policy.weight_block_size: OnlineFp8Policy#weight_block_size.
  logger: logger.
  OnlineFp8Policy.targets: OnlineFp8Policy#targets.
  OnlineFp8Policy.weight_scheme: OnlineFp8Policy#weight_scheme.
  OnlineFp8Policy.from_dict: OnlineFp8Policy#from_dict().
  OnlineFp8Policy.exclude: OnlineFp8Policy#exclude.
  OnlineFp8Policy.matched: OnlineFp8Policy#matched.
  OnlineFp8Policy.selected: OnlineFp8Policy#selected.
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py)

## Classes
### <a id="OnlineFp8Policy"></a>`OnlineFp8Policy`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py:42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L42)
- signature: `class OnlineFp8Policy:`
- members:
  - <a id="OnlineFp8Policy.apply_mapper"></a>`apply_mapper(self, mapper: WeightsMapper)` — [`L111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L111)
  - <a id="OnlineFp8Policy.from_dict"></a>`from_dict(cls, value: dict[str, Any] | None)` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L51)
  - <a id="OnlineFp8Policy.select"></a>`select(self, prefix: str, packed_mapping: dict[str, list[str]])` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L115) — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
  - <a id="OnlineFp8Policy.exclude"></a>`exclude` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L44)
  - <a id="OnlineFp8Policy.matched"></a>`matched` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L47)
  - <a id="OnlineFp8Policy.selected"></a>`selected` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L48)
  - <a id="OnlineFp8Policy.targets"></a>`targets` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L43)
  - <a id="OnlineFp8Policy.weight_block_size"></a>`weight_block_size` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L46)
  - <a id="OnlineFp8Policy.weight_scheme"></a>`weight_scheme` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L45)
- used by: [`validate_online_fp8`](online_fp8.md#validate_online_fp8), [`resolve_online_fp8`](fp8.md#resolve_online_fp8), [`attach_online_fp8`](online_fp8.md#attach_online_fp8), [`quantize_online_fp8`](online_fp8.md#quantize_online_fp8), [`map_online_fp8`](online_fp8.md#map_online_fp8), [`online_fp8_policy`](configs.md#VllmQuantConfig.online_fp8_policy), [`online_fp8_policy`](fp8.md#VllmFp8LinearMethodTPU.online_fp8_policy)

## Functions
- <a id="attach_online_fp8"></a>`attach_online_fp8(config: QuantConfigT, vllm_config: VllmConfig)` — [`L138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L138) — Keep the checkpoint config intact; attach independent per-model state. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="map_online_fp8"></a>`map_online_fp8(config: VllmQuantConfig, mapper: WeightsMapper)` — [`L158`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L158)
- <a id="quantize_online_fp8"></a>`quantize_online_fp8(weight: torch.Tensor, policy: OnlineFp8Policy)` — [`L241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L241) — Quantize a loaded local [N, K] shard; expand only scales along N. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)
- <a id="validate_online_fp8"></a>`validate_online_fp8(model: torch.nn.Module, config: QuantizationConfig | None)` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L164) — Audit once after loading, before compilation or accepting requests. — documented in [quantization-methods](../../../../../../concepts/quantization-methods.md)

## Module values
- <a id="logger"></a>`logger` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.py#L38)

