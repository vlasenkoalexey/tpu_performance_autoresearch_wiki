---
title: 'Module: torchtitan/experiments/tpu/llama3/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/llama3/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.llama3.config_registry`/
symbols:
  sft_llama3_8b_metamath: sft_llama3_8b_metamath().
  llama3_70b: llama3_70b().
  llama3_8b: llama3_8b().
  llama3_405b: llama3_405b().
  llama3_debugmodel: llama3_debugmodel().
  llama3_1b: llama3_1b().
  _on_scan_lane: _on_scan_lane().
  graph_trainer_llama3_debugmodel: graph_trainer_llama3_debugmodel().
  _enable_pallas_cross_entropy: _enable_pallas_cross_entropy().
  _LLAMA3_SCAN_FLAGS: _LLAMA3_SCAN_FLAGS.
  _with_float8: _with_float8().
  llama3_8b_scan: llama3_8b_scan().
  llama3_70b_scan: llama3_70b_scan().
  llama3_405b_scan: llama3_405b_scan().
  llama3_70b_float8: llama3_70b_float8().
  _REAL_ROPE_OVERRIDE: _REAL_ROPE_OVERRIDE.
  _FUSED_LOSS_OVERRIDE: _FUSED_LOSS_OVERRIDE.
  sft_llama3_8b_metamath.process_sample: sft_llama3_8b_metamath().process_sample().
---
# Module: [`torchtitan/experiments/tpu/llama3/config_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py)

## Functions
- <a id="_enable_pallas_cross_entropy"></a>`_enable_pallas_cross_entropy(config: TPUTrainerConfig)` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L79) — Select the fused loss and its pre-construction LM-head override together.
- <a id="_on_scan_lane"></a>`_on_scan_lane(config: TPUTrainerConfig)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L85) — Move a recipe onto the graph trainer with scanned layers and host offload. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="_with_float8"></a>`_with_float8(config: TPUTrainerConfig, flavor: str, recipe_name: str = "rowwise")` — [`L504`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L504) — Swaps `config`'s model for one with torchao Float8Linear layers.
- <a id="graph_trainer_llama3_debugmodel"></a>`graph_trainer_llama3_debugmodel()` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L153) — Llama3 debug model using TPU GraphTrainer.
- <a id="llama3_1b"></a>`llama3_1b()` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L165) — Llama3 1B model configuration for TPU.
- <a id="llama3_405b"></a>`llama3_405b()` — [`L334`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L334) — Llama3 405B model configuration for TPU. — documented in [tpu-trainer-and-job-config](../../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="llama3_405b_scan"></a>`llama3_405b_scan()` — [`L499`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L499) — Llama3 405B on the scan lane. Layerwise does not compile at this size.
- <a id="llama3_70b"></a>`llama3_70b()` — [`L269`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L269) — Llama3 70B model configuration for TPU. — documented in [checkpointing](../../../../../concepts/checkpointing.md)
- <a id="llama3_70b_float8"></a>`llama3_70b_float8()` — [`L532`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L532) — `llama3_70b` with torchao rowwise float8 linears.
- <a id="llama3_70b_scan"></a>`llama3_70b_scan()` — [`L494`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L494) — Llama3 70B on the scan lane.
- <a id="llama3_8b"></a>`llama3_8b()` — [`L204`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L204) — Llama3 8B model configuration for TPU. — documented in [tpu-trainer-and-job-config](../../../../../concepts/tpu-trainer-and-job-config.md)
- <a id="llama3_8b_scan"></a>`llama3_8b_scan()` — [`L489`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L489) — Llama3 8B on the scan lane.
- <a id="llama3_debugmodel"></a>`llama3_debugmodel()` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L114) — Llama3 debug model configuration for TPU.
- <a id="sft_llama3_8b_metamath.process_sample"></a>`process_sample(sample)` — [`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L402)
- <a id="sft_llama3_8b_metamath"></a>`sft_llama3_8b_metamath()` — [`L399`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L399) — Llama3 8B SFT on MetaMathQA for TPU. — documented in [checkpointing](../../../../../concepts/checkpointing.md)

## Module values
- <a id="_FUSED_LOSS_OVERRIDE"></a>`_FUSED_LOSS_OVERRIDE` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L58)
- <a id="_LLAMA3_SCAN_FLAGS"></a>`_LLAMA3_SCAN_FLAGS` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L62)
- <a id="_REAL_ROPE_OVERRIDE"></a>`_REAL_ROPE_OVERRIDE` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/config_registry.py#L54)

