---
title: 'Module: torchtitan/experiments/graph_trainer/qwen3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/qwen3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.qwen3.model`/GraphTrainerQwen3Model#
symbols:
  GraphTrainerQwen3Model: ''
  GraphTrainerQwen3Model.Config: Config#
  GraphTrainerQwen3Model.__init__: __init__().
  GraphTrainerQwen3Model.init_states: init_states().
---
# Module: [`torchtitan/experiments/graph_trainer/qwen3/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/model.py)

## Classes
### <a id="GraphTrainerQwen3Model"></a>`GraphTrainerQwen3Model`  ·  implements/extends Qwen3Model
- def: [`torchtitan/experiments/graph_trainer/qwen3/model.py:16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/model.py#L16)
- signature: `class GraphTrainerQwen3Model(Qwen3Model):`
- members:
  - <a id="GraphTrainerQwen3Model.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/model.py#L24)
- protocol/private: <a id="GraphTrainerQwen3Model.__init__"></a>`__init__`[`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/model.py#L21)
- uses (calls/refs, reference-scoped): [`Qwen3Model`](../../../models/qwen3/model.md#Qwen3Model), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`disable_active_parametrization`](../simple_fsdp.md#disable_active_parametrization), [`__init__`](../../../models/common/decoder.md#Decoder.__init__), [`Config`](model.md#GraphTrainerQwen3Model.Config), [`MaxTextTpuGraphTrainerQwen3Model`](../../tpu/graph_trainer/qwen3.md#MaxTextTpuGraphTrainerQwen3Model)
- used by: [`Qwen3Model`](../../../models/qwen3/model.md#Qwen3Model), [`parallelize_qwen3`](parallelize.md#parallelize_qwen3), [`model_registry`](__init__.md#model_registry), [`_use_maxtext_flops`](../../tpu/qwen3/config_registry.md#_use_maxtext_flops), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`parallelize_qwen3`](../../tpu/graph_trainer/qwen3.md#parallelize_qwen3), [`annotate_qwen3`](parallelize.md#annotate_qwen3), [`with_maxtext_flops`](../../tpu/graph_trainer/qwen3.md#with_maxtext_flops), [`Config`](../../tpu/graph_trainer/qwen3.md#MaxTextTpuGraphTrainerQwen3Model.Config), [`MaxTextTpuGraphTrainerQwen3Model`](../../tpu/graph_trainer/qwen3.md#MaxTextTpuGraphTrainerQwen3Model)  (3 test-only)

### <a id="GraphTrainerQwen3Model.Config"></a>`GraphTrainerQwen3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/qwen3/model.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/qwen3/model.py#L18)
- signature: `class Config(Qwen3Model.Config):`
- uses (calls/refs, reference-scoped): [`Qwen3Model`](../../../models/qwen3/model.md#Qwen3Model), [`Config`](../../../models/qwen3/model.md#Qwen3Model.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`_use_maxtext_flops`](../../tpu/qwen3/config_registry.md#_use_maxtext_flops), [`with_maxtext_flops`](../../tpu/graph_trainer/qwen3.md#with_maxtext_flops), [`Config`](../../tpu/graph_trainer/qwen3.md#MaxTextTpuGraphTrainerQwen3Model.Config), [`__init__`](model.md#GraphTrainerQwen3Model.__init__)  (1 test-only)

