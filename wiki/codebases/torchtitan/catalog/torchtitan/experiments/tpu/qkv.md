---
title: 'Module: torchtitan/experiments/tpu/qkv.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qkv.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qkv`/
symbols:
  _packed_param_init: _packed_param_init().
  TpuPackedQKVLinear.kv_rows: TpuPackedQKVLinear#kv_rows.
  TpuPackedQKVConverter.convert: TpuPackedQKVConverter#convert().
  TpuPackedQKVLinear.wqkv_packed: TpuPackedQKVLinear#wqkv_packed.
  TpuPackedQKVLinear: TpuPackedQKVLinear#
  TpuPackedQKVLinear.Config: TpuPackedQKVLinear#Config#
  TpuPackedQKVLinear.forward: TpuPackedQKVLinear#forward().
  _PackedQKVInit.__call__: _PackedQKVInit#__call__().
  TpuPackedQKVLinear.__init__: TpuPackedQKVLinear#__init__().
  TpuPackedQKVConverter.Config: TpuPackedQKVConverter#Config#
  TpuPackedQKVConverter: TpuPackedQKVConverter#
  TpuPackedQKVLinear.q_rows: TpuPackedQKVLinear#q_rows.
  TpuPackedQKVLinear.parallelize: TpuPackedQKVLinear#parallelize().
  TpuPackedQKVLinear.heads_per_kv: TpuPackedQKVLinear#heads_per_kv.
  TpuPackedQKVLinear.n_heads: TpuPackedQKVLinear#n_heads.
  TpuPackedQKVLinear.n_kv_heads: TpuPackedQKVLinear#n_kv_heads.
  TpuPackedQKVLinear.r_dim: TpuPackedQKVLinear#r_dim.
  TpuPackedQKVConverter.__init__: TpuPackedQKVConverter#__init__().
  _PackedQKVInit.n_kv_heads: _PackedQKVInit#n_kv_heads.
  _PackedQKVInit: _PackedQKVInit#
  _PackedQKVInit.interleaved_init: _PackedQKVInit#interleaved_init.
  _PackedQKVInit.n_heads: _PackedQKVInit#n_heads.
  _PackedQKVInit.head_dim: _PackedQKVInit#head_dim.
  TpuPackedQKVLinear._split_qkv_on_save: TpuPackedQKVLinear#_split_qkv_on_save().
  TpuPackedQKVLinear._merge_qkv_on_load: TpuPackedQKVLinear#_merge_qkv_on_load().
  _PackedQKVInit.__init__: _PackedQKVInit#__init__().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/qkv.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py)

## Classes
### <a id="TpuPackedQKVConverter"></a>`TpuPackedQKVConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/tpu/qkv.py:198`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L198) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: Select packed QKV projections before model construction.
- signature: `class TpuPackedQKVConverter(ModelConfigConverter):`
- members:
  - <a id="TpuPackedQKVConverter.convert"></a>`convert(self, model_config)` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L208)
- protocol/private: <a id="TpuPackedQKVConverter.__init__"></a>`__init__`[`L205`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L205)
- uses (calls/refs, reference-scoped): [`param_init`](../../protocols/module.md#Module.Config.param_init), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`derive`](../../config/override.md#derive), [`traverse`](../../config/configurable.md#Configurable.Config.traverse), [`FusedQKVLinear`](../../models/common/attention.md#FusedQKVLinear), [`Config`](../../models/common/attention.md#FusedQKVLinear.Config), [`wqkv`](../../models/common/attention.md#FusedQKVLinear.Config.wqkv), [`TpuPackedQKVLinear`](qkv.md#TpuPackedQKVLinear), [`Config`](qkv.md#TpuPackedQKVLinear.Config), [`Config`](qkv.md#TpuPackedQKVConverter.Config)
- used by: [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`qwen3_32b`](qwen3/config_registry.md#qwen3_32b), [`convert`](../../protocols/model.md#ModelConfigConverter.convert)  (1 test-only)

### <a id="TpuPackedQKVConverter.Config"></a>`TpuPackedQKVConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qkv.py:202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L202)
- signature: `class Config(ModelConfigConverter.Config):`
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../protocols/model.md#ModelConfigConverter), [`Config`](../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`qwen3_32b`](qwen3/config_registry.md#qwen3_32b), [`__init__`](qkv.md#TpuPackedQKVConverter.__init__)  (1 test-only)

### <a id="TpuPackedQKVLinear"></a>`TpuPackedQKVLinear`  ·  implements/extends BaseQKVLinear
- def: [`torchtitan/experiments/tpu/qkv.py:76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L76) — documented in [tpu-layer-loop-remat-and-layouts](../../../../concepts/tpu-layer-loop-remat-and-layouts.md)
- doc: Run three contiguous Q/K/V projections from one FSDP parameter.
- signature: `class TpuPackedQKVLinear(BaseQKVLinear):`
- members:
  - <a id="TpuPackedQKVLinear.forward"></a>`forward(self, x_TD: torch.Tensor)` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L133)
  - <a id="TpuPackedQKVLinear.parallelize"></a>`parallelize(self, parallel_dims: ParallelDims)` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L115)
  - <a id="TpuPackedQKVLinear.heads_per_kv"></a>`heads_per_kv` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L98)
  - <a id="TpuPackedQKVLinear.kv_rows"></a>`kv_rows` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L101)
  - <a id="TpuPackedQKVLinear.n_heads"></a>`n_heads` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L96)
  - <a id="TpuPackedQKVLinear.n_kv_heads"></a>`n_kv_heads` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L97)
  - <a id="TpuPackedQKVLinear.q_rows"></a>`q_rows` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L100)
  - <a id="TpuPackedQKVLinear.r_dim"></a>`r_dim` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L99)
  - <a id="TpuPackedQKVLinear.wqkv_packed"></a>`wqkv_packed` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L108)
- protocol/private: <a id="TpuPackedQKVLinear.__init__"></a>`__init__`[`L89`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L89), <a id="TpuPackedQKVLinear._merge_qkv_on_load"></a>`_merge_qkv_on_load`[`L184`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L184), <a id="TpuPackedQKVLinear._split_qkv_on_save"></a>`_split_qkv_on_save`[`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L166)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`out_features`](../../models/common/linear.md#Linear.Config.out_features), [`tp`](../../distributed/parallel_dims.md#ParallelDims.tp), [`parallelize`](../../protocols/module.md#Module.parallelize), [`_packed_param_init`](qkv.md#_packed_param_init), [`BaseQKVLinear`](../../models/common/attention.md#BaseQKVLinear), [`wqkv`](../../models/common/attention.md#FusedQKVLinear.Config.wqkv), [`head_dim`](../../models/common/attention.md#BaseQKVLinear.head_dim), [`Config`](qkv.md#TpuPackedQKVLinear.Config), [`head_dim`](../../models/common/attention.md#BaseQKVLinear.Config.head_dim), [`n_heads`](../../models/common/attention.md#FusedQKVLinear.Config.n_heads), [`n_kv_heads`](../../models/common/attention.md#FusedQKVLinear.Config.n_kv_heads), [`__init__`](../../models/common/attention.md#BaseQKVLinear.__init__)
- used by: [`parallelize`](../../protocols/module.md#Module.parallelize), [`_bld_qkv`](bld_layout.md#_BLDGQAttention._bld_qkv), [`BaseQKVLinear`](../../models/common/attention.md#BaseQKVLinear), [`convert`](qkv.md#TpuPackedQKVConverter.convert), [`_QKV_FORWARDS`](bld_layout.md#_QKV_FORWARDS), [`forward`](../../models/common/attention.md#BaseQKVLinear.forward)  (2 test-only)

### <a id="TpuPackedQKVLinear.Config"></a>`TpuPackedQKVLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/qkv.py:86`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L86)
- signature: `class Config(FusedQKVLinear.Config):`
- uses (calls/refs, reference-scoped): [`FusedQKVLinear`](../../models/common/attention.md#FusedQKVLinear), [`Config`](../../models/common/attention.md#FusedQKVLinear.Config)
- used by: [`convert`](qkv.md#TpuPackedQKVConverter.convert), [`__init__`](qkv.md#TpuPackedQKVLinear.__init__)  (2 test-only)

### <a id="_PackedQKVInit"></a>`_PackedQKVInit`
- def: [`torchtitan/experiments/tpu/qkv.py:20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L20)
- signature: `class _PackedQKVInit:`
- members:
  - <a id="_PackedQKVInit.head_dim"></a>`head_dim` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L33)
  - <a id="_PackedQKVInit.interleaved_init"></a>`interleaved_init` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L30)
  - <a id="_PackedQKVInit.n_heads"></a>`n_heads` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L31)
  - <a id="_PackedQKVInit.n_kv_heads"></a>`n_kv_heads` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L32)
- protocol/private: <a id="_PackedQKVInit.__call__"></a>`__call__`[`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L35), <a id="_PackedQKVInit.__init__"></a>`__init__`[`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L22)
- used by: [`_packed_param_init`](qkv.md#_packed_param_init)

## Functions
- <a id="_packed_param_init"></a>`_packed_param_init(config: FusedQKVLinear.Config)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L61)

## Module values
- <a id="__all__"></a>`__all__` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qkv.py#L232)

