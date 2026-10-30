---
title: Float8 training (rowwise torchao Float8Linear, grouped experts, TPU converter)
type: doc-concept
provenance: doc
source: torchtitan/components/quantization/float8.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Float8 training (rowwise torchao Float8Linear, grouped experts, TPU converter)

## Definition
Float8 training swaps eligible Linear (and MoE grouped-GEMM) modules for torchao float8 versions
that dynamically quantize GEMM inputs. It pays off only when GEMMs are large enough that the float8
matmul speedup outweighs the dynamic-quantization overhead; small layers should be filtered out.
Conversion happens at **config time**: a converter walks the model config tree and swaps config
types so quantized modules are built directly.

## In torchtitan (grounded)
- [`Float8LinearConverter`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter "torchtitan/components/quantization/float8.py:L53")
  with [`Float8LinearConverter.Config`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter.Config "torchtitan/components/quantization/float8.py:L57"):
  [`recipe_name`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter.Config.recipe_name "torchtitan/components/quantization/float8.py:L58")
  (`"rowwise"` default, `"rowwise_with_gw_hp"`),
  [`filter_fqns`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter.Config.filter_fqns),
  [`emulate`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter.Config.emulate),
  and the shared [`model_compile_enabled`](../catalog/torchtitan/components/quantization/__init__.md#QuantizationConverter.Config.model_compile_enabled "torchtitan/components/quantization/__init__.py:L30").
  Filtering goes through [`module_filter_fn`](../catalog/torchtitan/components/quantization/utils.md#module_filter_fn "torchtitan/components/quantization/utils.py:L16").
- MoE: [`Float8GroupedExpertsConverter`](../catalog/torchtitan/components/quantization/float8.md#Float8GroupedExpertsConverter "torchtitan/components/quantization/float8.py:L224")
  for grouped expert GEMMs.
- Both subclass [`ModelConfigConverter`](../catalog/torchtitan/protocols/model.md#ModelConfigConverter "torchtitan/protocols/model.py:L19")
  and are passed to a model's `model_registry(..., converters=[...])`, e.g.
  [`llama3_debugmodel_float8`](../catalog/torchtitan/models/llama3/config_registry.md#llama3_debugmodel_float8 "torchtitan/models/llama3/config_registry.py:L142"),
  [`deepseek_v3_671b_float8`](../catalog/torchtitan/models/deepseek_v3/config_registry.md#deepseek_v3_671b_float8 "torchtitan/models/deepseek_v3/config_registry.py:L292").
- **TPU lane:** [`TpuFloat8LinearConverter`](../catalog/torchtitan/experiments/tpu/float8_converter.md#TpuFloat8LinearConverter)
  inherits the model swap (so the built `Float8Linear` layers are identical) but builds the torchao
  config itself ([`__init__`](../catalog/torchtitan/experiments/tpu/float8_converter.md#TpuFloat8LinearConverter.__init__))
  without the CUDA/ROCm capability check that makes the upstream converter refuse to construct on
  TPU. TPU recipes use it via [`_with_float8`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_with_float8)
  (e.g. [`llama3_70b_float8`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b_float8)),
  filtering `lm_head` / `output`.

## Why it matters / when it applies
- **Hardware.** The doc targets H100-class GPUs (upstream converter accepts NVIDIA SM89+ or AMD
  gfx942+). On TPU, v7x has native float8 matmuls that TorchTPU lowers through `torch._scaled_mm`;
  that is why the TPU converter exists.
- **torch.compile is required for competitive performance** - it fuses the scaling/casting kernels;
  set `model_compile_enabled=True` when the model is compiled.
- **Filter small layers.** `filter_fqns` skips modules (e.g. `output`, `router.gate`,
  `attention.wk`/`wv`). The special token `"auto_filter_small_kn"` auto-skips layers whose (K, N) is
  below **H100-measured** thresholds; the TPU converter rejects it outright ("CUDA-tuned
  thresholds; list the FQNs to skip explicitly on TPU").
- **Accumulation.** torchao enables cuBLAS fast accumulation for the forward GEMM; TPU matmuls
  accumulate in FP32 and TorchTPU treats `use_fast_accum` as a no-op, so on TPU the forward GEMM has
  the same accumulation as the gradient GEMMs.
- **Communication stays high precision**: with rowwise scaling all distributed collectives run in
  high precision (no float8 all-gather savings). Scaling strategy is rowwise dynamic.
- **Doc vs code.** The doc shows `model_registry("405B", quantization=[...])`; the actual keyword at
  this commit is `converters=` (`model_registry(..., converters=[Float8LinearConverter.Config(...)])`).

## Connections
- Code concepts: [quantization](../concepts/quantization.md),
  [model-spec-protocols](../concepts/model-spec-protocols.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [llama3-model](../concepts/llama3-model.md).
- Module catalogs: [torchtitan/components/quantization/float8](../catalog/torchtitan/components/quantization/float8.md),
  [torchtitan/components/quantization/utils](../catalog/torchtitan/components/quantization/utils.md),
  [torchtitan/experiments/tpu/float8_converter](../catalog/torchtitan/experiments/tpu/float8_converter.md).
- Related doc-concepts: [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md), [mxfp8-training](mxfp8-training.md), [nvfp4-training](nvfp4-training.md),
  [configurable-overrides](configurable-overrides.md), [model-config-transforms](model-config-transforms.md).

## Source
Extracted from `torchtitan/components/quantization/float8.md` (kept in place).
