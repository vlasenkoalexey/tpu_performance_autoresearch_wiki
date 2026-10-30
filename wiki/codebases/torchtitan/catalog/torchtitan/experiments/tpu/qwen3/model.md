---
title: 'Module: torchtitan/experiments/tpu/qwen3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.model`/MaxTextQwen3Config#
symbols:
  MaxTextQwen3Config: ''
  MaxTextQwen3Config.from_qwen3: from_qwen3().
  MaxTextQwen3Config.get_nparams_and_flops: get_nparams_and_flops().
---
# Module: [`torchtitan/experiments/tpu/qwen3/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/model.py)

## Classes
### <a id="MaxTextQwen3Config"></a>`MaxTextQwen3Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qwen3/model.py:19`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/model.py#L19)
- doc: Qwen3 config that builds the upstream model but uses MaxText FLOPs.
- signature: `class MaxTextQwen3Config(Qwen3Model.Config):`
- members:
  - <a id="MaxTextQwen3Config.from_qwen3"></a>`from_qwen3(cls, config: Qwen3Model.Config)` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/model.py#L29)
  - <a id="MaxTextQwen3Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/model.py#L40)
- uses (calls/refs, reference-scoped): [`Qwen3Model`](../../../models/qwen3/model.md#Qwen3Model), [`get_maxtext_decoder_nparams_and_flops`](../mfu_flops.md#get_maxtext_decoder_nparams_and_flops), [`Config`](../../../models/qwen3/model.md#Qwen3Model.Config)
- used by: [`_use_maxtext_flops`](config_registry.md#_use_maxtext_flops), [`maybe_use_maxtext_flops`](../graph_trainer/config.md#maybe_use_maxtext_flops)  (2 test-only)

