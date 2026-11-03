---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.kimi_vit`/
symbols:
  _materialize_vision_qkv: _materialize_vision_qkv().
  KimiK3MoonViT3dPretrainedModel.__init__: KimiK3MoonViT3dPretrainedModel#__init__().
  KimiK3MoonViT3dPretrainedModel: KimiK3MoonViT3dPretrainedModel#
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py)

## Classes
### <a id="KimiK3MoonViT3dPretrainedModel"></a>`KimiK3MoonViT3dPretrainedModel`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py:53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py#L53)
- doc: Upstream K3 MoonViT with TPU-safe compilation boundaries.
- signature: `class KimiK3MoonViT3dPretrainedModel(MoonViT3dPretrainedModel):`
- protocol/private: <a id="KimiK3MoonViT3dPretrainedModel.__init__"></a>`__init__`[`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py#L56)
- uses (calls/refs, reference-scoped): [`_materialize_vision_qkv`](kimi_vit.md#_materialize_vision_qkv)
- used by: [`vision_tower`](model.md#KimiK3ForConditionalGeneration.vision_tower)

## Functions
- <a id="_materialize_vision_qkv"></a>`_materialize_vision_qkv(module: nn.Module, inputs: tuple[torch.Tensor, ...], output: tuple[torch.Tensor, torch.Tensor | None])` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/kimi_vit.py#L27) — Bound the lazy graph before K3 reshapes and rotates projected QKV.

