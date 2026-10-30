---
title: 'Module: torchtitan/experiments/graph_trainer/deepseek_v3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/deepseek_v3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.deepseek_v3.model`/GraphTrainerDeepSeekV3Model#
symbols:
  GraphTrainerDeepSeekV3Model: ''
  GraphTrainerDeepSeekV3Model.Config: Config#
  GraphTrainerDeepSeekV3Model.__init__: __init__().
  GraphTrainerDeepSeekV3Model.init_states: init_states().
---
# Module: [`torchtitan/experiments/graph_trainer/deepseek_v3/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/model.py)

## Classes
### <a id="GraphTrainerDeepSeekV3Model"></a>`GraphTrainerDeepSeekV3Model`  ·  implements/extends DeepSeekV3Model
- def: [`torchtitan/experiments/graph_trainer/deepseek_v3/model.py:16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/model.py#L16)
- signature: `class GraphTrainerDeepSeekV3Model(DeepSeekV3Model):`
- members:
  - <a id="GraphTrainerDeepSeekV3Model.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/model.py#L24)
- protocol/private: <a id="GraphTrainerDeepSeekV3Model.__init__"></a>`__init__`[`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/model.py#L21)
- uses (calls/refs, reference-scoped): [`DeepSeekV3Model`](../../../models/deepseek_v3/model.md#DeepSeekV3Model), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`disable_active_parametrization`](../simple_fsdp.md#disable_active_parametrization), [`__init__`](../../../models/deepseek_v3/mtp.md#MTPDecoder.__init__), [`Config`](model.md#GraphTrainerDeepSeekV3Model.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`parallelize_deepseekv3`](parallelize.md#parallelize_deepseekv3), [`DeepSeekV3Model`](../../../models/deepseek_v3/model.md#DeepSeekV3Model), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`annotate_deepseekv3`](parallelize.md#annotate_deepseekv3)

### <a id="GraphTrainerDeepSeekV3Model.Config"></a>`GraphTrainerDeepSeekV3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/deepseek_v3/model.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/deepseek_v3/model.py#L18)
- signature: `class Config(DeepSeekV3Model.Config):`
- uses (calls/refs, reference-scoped): [`DeepSeekV3Model`](../../../models/deepseek_v3/model.md#DeepSeekV3Model), [`Config`](../../../models/deepseek_v3/model.md#DeepSeekV3Model.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`__init__`](model.md#GraphTrainerDeepSeekV3Model.__init__)

