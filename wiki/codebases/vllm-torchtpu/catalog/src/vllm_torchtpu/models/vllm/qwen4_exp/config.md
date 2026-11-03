---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen4_exp/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen4_exp/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen4_exp.config`/TPUQwen4ExpConfig#
symbols:
  TPUQwen4ExpConfig: ''
  TPUQwen4ExpConfig.verify_and_update_config: verify_and_update_config().
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen4_exp/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/config.py)

## Classes
### <a id="TPUQwen4ExpConfig"></a>`TPUQwen4ExpConfig`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/config.py:26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/config.py#L26)
- doc: Upstream Qwen4Exp checks, plus the features the TPU model lacks yet.
- signature: `class TPUQwen4ExpConfig(Qwen4ExpForCausalLMConfig):`
- members:
  - <a id="TPUQwen4ExpConfig.verify_and_update_config"></a>`verify_and_update_config(vllm_config: VllmConfig)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/config.py#L30)
- used by: [`register_models`](../__init__.md#register_models)

