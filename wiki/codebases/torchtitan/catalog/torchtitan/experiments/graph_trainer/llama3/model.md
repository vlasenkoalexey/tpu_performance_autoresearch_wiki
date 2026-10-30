---
title: 'Module: torchtitan/experiments/graph_trainer/llama3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/llama3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.llama3.model`/GraphTrainerLlama3Model#
symbols:
  GraphTrainerLlama3Model: ''
  GraphTrainerLlama3Model.Config: Config#
  GraphTrainerLlama3Model.__init__: __init__().
  GraphTrainerLlama3Model.init_states: init_states().
---
# Module: [`torchtitan/experiments/graph_trainer/llama3/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/model.py)

## Classes
### <a id="GraphTrainerLlama3Model"></a>`GraphTrainerLlama3Model`  ·  implements/extends Llama3Model
- def: [`torchtitan/experiments/graph_trainer/llama3/model.py:16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/model.py#L16)
- signature: `class GraphTrainerLlama3Model(Llama3Model):`
- members:
  - <a id="GraphTrainerLlama3Model.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/model.py#L24)
- protocol/private: <a id="GraphTrainerLlama3Model.__init__"></a>`__init__`[`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/model.py#L21)
- uses (calls/refs, reference-scoped): [`Llama3Model`](../../../models/llama3/model.md#Llama3Model), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`disable_active_parametrization`](../simple_fsdp.md#disable_active_parametrization), [`__init__`](../../../models/common/decoder.md#Decoder.__init__), [`Config`](model.md#GraphTrainerLlama3Model.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`Llama3Model`](../../../models/llama3/model.md#Llama3Model), [`parallelize_llama`](parallelize.md#parallelize_llama), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`annotate_llama`](parallelize.md#annotate_llama)

### <a id="GraphTrainerLlama3Model.Config"></a>`GraphTrainerLlama3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/llama3/model.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/model.py#L18)
- signature: `class Config(Llama3Model.Config):`
- uses (calls/refs, reference-scoped): [`Llama3Model`](../../../models/llama3/model.md#Llama3Model), [`Config`](../../../models/llama3/model.md#Llama3Model.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`__init__`](model.md#GraphTrainerLlama3Model.__init__)

