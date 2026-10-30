---
title: 'Module: torchtitan/models/qwen3/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3.config_registry`/
symbols:
  sft_qwen3_8b_math: sft_qwen3_8b_math().
  qwen3_debugmodel: qwen3_debugmodel().
  qwen3_moe_debug: qwen3_moe_debug().
  qwen3_moe_deepep: qwen3_moe_deepep().
  qwen3_debugmodel_flex_flash: qwen3_debugmodel_flex_flash().
  qwen3_14b: qwen3_14b().
  qwen3_30b_a3b: qwen3_30b_a3b().
  qwen3_32b: qwen3_32b().
  qwen3_0_6b: qwen3_0_6b().
  qwen3_1_7b: qwen3_1_7b().
  qwen3_30b_a3b_global_aux: qwen3_30b_a3b_global_aux().
  qwen3_debugmodel_first_85_pct_layers_nvfp4: qwen3_debugmodel_first_85_pct_layers_nvfp4().
  qwen3_8b_first_85_pct_layers_nvfp4: qwen3_8b_first_85_pct_layers_nvfp4().
  qwen3_debugmodel_nvfp4: qwen3_debugmodel_nvfp4().
  qwen3_debugmodel_moe_param_groups: qwen3_debugmodel_moe_param_groups().
  qwen3_debugmodel_non_fused_qkv: qwen3_debugmodel_non_fused_qkv().
  sft_qwen3_8b_math.process_sample: sft_qwen3_8b_math().process_sample().
---
# Module: [`torchtitan/models/qwen3/config_registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py)

## Functions
- <a id="sft_qwen3_8b_math.process_sample"></a>`process_sample(sample)` — [`L515`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L515)
- <a id="qwen3_0_6b"></a>`qwen3_0_6b(seq_len: int | None = None)` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L203) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_14b"></a>`qwen3_14b(seq_len: int | None = None)` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L288) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_1_7b"></a>`qwen3_1_7b(seq_len: int | None = None)` — [`L233`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L233) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_30b_a3b"></a>`qwen3_30b_a3b(seq_len: int | None = None)` — [`L323`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L323) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_30b_a3b_global_aux"></a>`qwen3_30b_a3b_global_aux(seq_len: int | None = None)` — [`L358`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L358) — Qwen3 30B-A3B with a globally-normalized MoE auxiliary loss. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_32b"></a>`qwen3_32b(seq_len: int | None = None)` — [`L382`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L382) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_8b_first_85_pct_layers_nvfp4"></a>`qwen3_8b_first_85_pct_layers_nvfp4(seq_len: int | None = None)` — [`L262`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L262) — documented in [quantization](../../../../concepts/quantization.md)
- <a id="qwen3_debugmodel"></a>`qwen3_debugmodel(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L40) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_debugmodel_first_85_pct_layers_nvfp4"></a>`qwen3_debugmodel_first_85_pct_layers_nvfp4(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L99) — documented in [quantization](../../../../concepts/quantization.md)
- <a id="qwen3_debugmodel_flex_flash"></a>`qwen3_debugmodel_flex_flash(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L164) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_debugmodel_moe_param_groups"></a>`qwen3_debugmodel_moe_param_groups(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L128) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_debugmodel_non_fused_qkv"></a>`qwen3_debugmodel_non_fused_qkv(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L417`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L417) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_debugmodel_nvfp4"></a>`qwen3_debugmodel_nvfp4(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L77) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_moe_debug"></a>`qwen3_moe_debug(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L427) — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="qwen3_moe_deepep"></a>`qwen3_moe_deepep(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L463`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L463) — Qwen3 debug MoE pretraining with the DeepEP v2 backend (compact training path), EP=4. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)
- <a id="sft_qwen3_8b_math"></a>`sft_qwen3_8b_math(seq_len: int | None = None)` — [`L512`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3/config_registry.py#L512) — Qwen3-8B SFT on GSM8K math dataset. — documented in [qwen3-model](../../../../concepts/qwen3-model.md)

