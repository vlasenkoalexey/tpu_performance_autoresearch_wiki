---
title: 'Module: torchtitan/models/llama3/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/models/llama3/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.llama3.config_registry`/
symbols:
  llama3_debugmodel: llama3_debugmodel().
  llama3_405b: llama3_405b().
  sft_debugmodel: sft_debugmodel().
  llama3_70b: llama3_70b().
  llama3_8b: llama3_8b().
  llama3_debugmodel_first_85_pct_layers_nvfp4: llama3_debugmodel_first_85_pct_layers_nvfp4().
  llama3_8b_first_85_pct_layers_nvfp4: llama3_8b_first_85_pct_layers_nvfp4().
  llama3_debugmodel_float8_emulate_lora: llama3_debugmodel_float8_emulate_lora().
  llama3_debugmodel_nvfp4: llama3_debugmodel_nvfp4().
  llama3_debugmodel_float8: llama3_debugmodel_float8().
  llama3_debugmodel_mxfp8: llama3_debugmodel_mxfp8().
  llama3_debugmodel_varlen_attn: llama3_debugmodel_varlen_attn().
  llama3_debugmodel_ce_loss: llama3_debugmodel_ce_loss().
  llama3_8b_mxfp8: llama3_8b_mxfp8().
  llama3_debugmodel_dist_gemm: llama3_debugmodel_dist_gemm().
  llama3_mxfp8_linear_converter_config: llama3_mxfp8_linear_converter_config().
  sft_debugmodel.process_sample: sft_debugmodel().process_sample().
---
# Module: [`torchtitan/models/llama3/config_registry.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py)

## Functions
- <a id="llama3_405b"></a>`llama3_405b(seq_len: int | None = None)` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L370) — documented in [debug-and-profiling-tools](../../../../concepts/debug-and-profiling-tools.md)
- <a id="llama3_70b"></a>`llama3_70b(seq_len: int | None = None)` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L332) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_8b"></a>`llama3_8b(seq_len: int | None = None)` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L257) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_8b_first_85_pct_layers_nvfp4"></a>`llama3_8b_first_85_pct_layers_nvfp4(seq_len: int | None = None)` — [`L292`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L292) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_8b_mxfp8"></a>`llama3_8b_mxfp8(seq_len: int | None = None)` — [`L316`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L316) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_debugmodel"></a>`llama3_debugmodel(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L63) — documented in [data-loading](../../../../concepts/data-loading.md)
- <a id="llama3_debugmodel_ce_loss"></a>`llama3_debugmodel_ce_loss(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L245) — Debug model with standard (non-chunked) CrossEntropyLoss.
- <a id="llama3_debugmodel_dist_gemm"></a>`llama3_debugmodel_dist_gemm(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L122) — Async-TP: the attention TP collectives are folded into their GEMMs. — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_debugmodel_first_85_pct_layers_nvfp4"></a>`llama3_debugmodel_first_85_pct_layers_nvfp4(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L198)
- <a id="llama3_debugmodel_float8"></a>`llama3_debugmodel_float8(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L142)
- <a id="llama3_debugmodel_float8_emulate_lora"></a>`llama3_debugmodel_float8_emulate_lora(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L225`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L225) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_debugmodel_mxfp8"></a>`llama3_debugmodel_mxfp8(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L159)
- <a id="llama3_debugmodel_nvfp4"></a>`llama3_debugmodel_nvfp4(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L174) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_debugmodel_varlen_attn"></a>`llama3_debugmodel_varlen_attn(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L110) — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="llama3_mxfp8_linear_converter_config"></a>`llama3_mxfp8_linear_converter_config(*, model_compile_enabled: bool)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L41) — Build the MXFP8 policy shared by eager and GraphTrainer configs. — documented in [llama3-model](../../../../concepts/llama3-model.md)
- <a id="sft_debugmodel.process_sample"></a>`process_sample(sample)` — [`L430`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L430)
- <a id="sft_debugmodel"></a>`sft_debugmodel(seq_len: int | None = DEFAULT_DEBUG_MODEL_SEQ_LEN)` — [`L425`](../../../../../../../raw/code/torchtitan/torchtitan/models/llama3/config_registry.py#L425) — SFT debug config with Llama3 debugmodel and local test data. — documented in [llama3-model](../../../../concepts/llama3-model.md)

