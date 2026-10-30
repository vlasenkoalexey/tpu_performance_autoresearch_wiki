---
title: 'Module: torchtitan/config/transform/context_parallel.py'
type: catalog
provenance: extracted
module: torchtitan/config/transform/context_parallel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.transform.context_parallel`/
symbols:
  ContextParallelTransform: ContextParallelTransform#
  ContextParallelTransform.inner_attention: ContextParallelTransform#inner_attention.
  ContextParallelTransform.transform: ContextParallelTransform#transform().
  ContextParallelTransform.__post_init__: ContextParallelTransform#__post_init__().
  __all__: __all__.
---
# Module: [`torchtitan/config/transform/context_parallel.py`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py)

## Classes
### <a id="ContextParallelTransform"></a>`ContextParallelTransform`  ·  implements/extends ModelConfigTransform
- def: [`torchtitan/config/transform/context_parallel.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py#L22) — documented in [job-config](../../../../concepts/job-config.md)
- doc: Run attention under context parallelism.
- signature: `class ContextParallelTransform(ModelConfigTransform):`
- members:
  - <a id="ContextParallelTransform.transform"></a>`transform(self, model: Module.Config)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py#L41)
  - <a id="ContextParallelTransform.inner_attention"></a>`inner_attention` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py#L32) — --- — documented in [job-config](../../../../concepts/job-config.md)
- protocol/private: <a id="ContextParallelTransform.__post_init__"></a>`__post_init__`[`L35`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py#L35)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`BaseAttention`](../../models/common/attention.md#BaseAttention), [`traverse`](../configurable.md#Configurable.Config.traverse), [`Config`](../../models/common/attention.md#BaseAttention.Config), [`CPInnerAttention`](../../models/common/cp_attention.md#CPInnerAttention), [`inner_attention`](../../models/common/attention.md#BaseAttention.Config.inner_attention), [`ModelConfigTransform`](base.md#ModelConfigTransform), [`convert_config_type`](base.md#convert_config_type)
- used by: [`_qwen3_cp`](../../experiments/tpu/qwen3/config_registry.md#_qwen3_cp), [`ModelConfigTransform`](base.md#ModelConfigTransform), [`transform`](base.md#ModelConfigTransform.transform)  (19 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/config/transform/context_parallel.py#L18)

