---
title: 'Module: torchtitan/experiments/graph_trainer/muse_glimmer/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/muse_glimmer/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.muse_glimmer.model`/GraphTrainerMuseGlimmerModel#
symbols:
  GraphTrainerMuseGlimmerModel: ''
  GraphTrainerMuseGlimmerModel.Config: Config#
  GraphTrainerMuseGlimmerModel.__init__: __init__().
  GraphTrainerMuseGlimmerModel.init_states: init_states().
---
# Module: [`torchtitan/experiments/graph_trainer/muse_glimmer/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/muse_glimmer/model.py)

## Classes
### <a id="GraphTrainerMuseGlimmerModel"></a>`GraphTrainerMuseGlimmerModel`  ·  implements/extends MuseGlimmerModel
- def: [`torchtitan/experiments/graph_trainer/muse_glimmer/model.py:16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/muse_glimmer/model.py#L16)
- signature: `class GraphTrainerMuseGlimmerModel(MuseGlimmerModel):`
- members:
  - <a id="GraphTrainerMuseGlimmerModel.init_states"></a>`init_states(self, *, buffer_device: torch.device | None = None)` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/muse_glimmer/model.py#L24)
- protocol/private: <a id="GraphTrainerMuseGlimmerModel.__init__"></a>`__init__`[`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/muse_glimmer/model.py#L21)
- uses (calls/refs, reference-scoped): [`MuseGlimmerModel`](../../../models/muse_glimmer/model.md#MuseGlimmerModel), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`disable_active_parametrization`](../simple_fsdp.md#disable_active_parametrization), [`__init__`](../../../models/muse_glimmer/model.md#MuseGlimmerModel.__init__), [`Config`](model.md#GraphTrainerMuseGlimmerModel.Config)
- used by: [`MuseGlimmerModel`](../../../models/muse_glimmer/model.md#MuseGlimmerModel), [`parallelize_muse_glimmer`](parallelize.md#parallelize_muse_glimmer), [`model_registry`](__init__.md#model_registry), [`init_states`](../../../models/common/decoder.md#Decoder.init_states), [`parallelize_muse_glimmer`](../../tpu/graph_trainer/muse_glimmer.md#parallelize_muse_glimmer), [`model_registry`](../../tpu/graph_trainer/muse_glimmer.md#model_registry)

### <a id="GraphTrainerMuseGlimmerModel.Config"></a>`GraphTrainerMuseGlimmerModel.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/muse_glimmer/model.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/muse_glimmer/model.py#L18)
- signature: `class Config(MuseGlimmerModel.Config):`
- uses (calls/refs, reference-scoped): [`MuseGlimmerModel`](../../../models/muse_glimmer/model.md#MuseGlimmerModel), [`Config`](../../../models/muse_glimmer/model.md#MuseGlimmerModel.Config)
- used by: [`model_registry`](__init__.md#model_registry), [`model_registry`](../../tpu/graph_trainer/muse_glimmer.md#model_registry), [`__init__`](model.md#GraphTrainerMuseGlimmerModel.__init__)

