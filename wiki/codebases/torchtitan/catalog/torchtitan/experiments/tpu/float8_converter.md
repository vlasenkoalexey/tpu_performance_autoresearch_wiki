---
title: 'Module: torchtitan/experiments/tpu/float8_converter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/float8_converter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.float8_converter`/
symbols:
  TpuFloat8LinearConverter: TpuFloat8LinearConverter#
  TpuFloat8LinearConverter.Config: TpuFloat8LinearConverter#Config#
  TpuFloat8LinearConverter.config: TpuFloat8LinearConverter#config.
  TpuFloat8LinearConverter.filter_fn: TpuFloat8LinearConverter#filter_fn.
  TpuFloat8LinearConverter.enabled: TpuFloat8LinearConverter#enabled.
  TpuFloat8LinearConverter.__init__: TpuFloat8LinearConverter#__init__().
  TpuFloat8LinearConverter.torchao_config: TpuFloat8LinearConverter#torchao_config.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/float8_converter.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py)

## Classes
### <a id="TpuFloat8LinearConverter"></a>`TpuFloat8LinearConverter`  ·  implements/extends Float8LinearConverter
- def: [`torchtitan/experiments/tpu/float8_converter.py:21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L21)
- doc: Replaces matching `Linear.Config`s with torchao `Float8Linear` on TPU.
- signature: `class TpuFloat8LinearConverter(Float8LinearConverter):`
- members:
  - <a id="TpuFloat8LinearConverter.config"></a>`config` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L32)
  - <a id="TpuFloat8LinearConverter.enabled"></a>`enabled` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L52)
  - <a id="TpuFloat8LinearConverter.filter_fn"></a>`filter_fn` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L51)
  - <a id="TpuFloat8LinearConverter.torchao_config"></a>`torchao_config` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L45)
- protocol/private: <a id="TpuFloat8LinearConverter.__init__"></a>`__init__`[`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L31)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`Float8LinearConverter`](../../components/quantization/float8.md#Float8LinearConverter), [`module_filter_fn`](../../components/quantization/utils.md#module_filter_fn), [`Config`](float8_converter.md#TpuFloat8LinearConverter.Config), [`recipe_name`](../../components/quantization/float8.md#Float8LinearConverter.Config.recipe_name), [`filter_fqns`](../../components/quantization/float8.md#Float8LinearConverter.Config.filter_fqns), [`emulate`](../../components/quantization/float8.md#Float8LinearConverter.Config.emulate)
- used by: [`qwen3_moe_235b_scan_torchao_float8`](qwen3/config_registry.md#qwen3_moe_235b_scan_torchao_float8), [`_with_float8`](llama3/config_registry.md#_with_float8), [`Float8LinearConverter`](../../components/quantization/float8.md#Float8LinearConverter)  (5 test-only)

### <a id="TpuFloat8LinearConverter.Config"></a>`TpuFloat8LinearConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/float8_converter.py:25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L25)
- signature: `class Config(Float8LinearConverter.Config):`
- uses (calls/refs, reference-scoped): [`Float8LinearConverter`](../../components/quantization/float8.md#Float8LinearConverter), [`Config`](../../components/quantization/float8.md#Float8LinearConverter.Config)
- used by: [`qwen3_moe_235b_scan_torchao_float8`](qwen3/config_registry.md#qwen3_moe_235b_scan_torchao_float8), [`_with_float8`](llama3/config_registry.md#_with_float8), [`__init__`](float8_converter.md#TpuFloat8LinearConverter.__init__)  (5 test-only)

## Module values
- <a id="__all__"></a>`__all__` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/float8_converter.py#L56)

