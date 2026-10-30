---
title: 'Module: torchtitan/experiments/tpu/grad_norm.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/grad_norm.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.grad_norm`/
symbols:
  CompiledGradNorm.clip_grad_norm_: CompiledGradNorm#clip_grad_norm_().
  CompiledGradNorm: CompiledGradNorm#
  _grad_signature: _grad_signature().
  CompiledGradNorm._runner: CompiledGradNorm#_runner.
  CompiledGradNorm._signature: CompiledGradNorm#_signature.
  CompiledGradNorm.__init__: CompiledGradNorm#__init__().
  GradSignature: GradSignature.
  global_grad_norm: global_grad_norm().
---
# Module: [`torchtitan/experiments/tpu/grad_norm.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py)

## Classes
### <a id="CompiledGradNorm"></a>`CompiledGradNorm`
- def: [`torchtitan/experiments/tpu/grad_norm.py:61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L61)
- doc: Compile and cache the global norm calculation for a trainer's gradients.
- signature: `class CompiledGradNorm:`
- members:
  - <a id="CompiledGradNorm.clip_grad_norm_"></a>`clip_grad_norm_(self, parameters: list[torch.Tensor], max_norm: float)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L69)
- protocol/private: <a id="CompiledGradNorm.__init__"></a>`__init__`[`L64`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L64), <a id="CompiledGradNorm._runner"></a>`_runner`[`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L65), <a id="CompiledGradNorm._signature"></a>`_signature`[`L66`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L66)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`gm`](../graph_trainer/make_fx_tracer.md#TracedResult.gm), [`minimal_fx_tracer`](../graph_trainer/make_fx_tracer.md#minimal_fx_tracer), [`run_traced`](../graph_trainer/make_fx_tracer.md#run_traced), [`example_inputs`](../graph_trainer/make_fx_tracer.md#TracedResult.example_inputs), [`tpu_backend_compile_pass`](graph_trainer/tpu_backend_pass.md#tpu_backend_compile_pass), [`_grad_signature`](grad_norm.md#_grad_signature), [`GradSignature`](grad_norm.md#GradSignature), [`global_grad_norm`](grad_norm.md#global_grad_norm)
- used by: [`_compiled_grad_norm`](train.md#TPUTrainer._compiled_grad_norm), [`_compiled_grad_norm`](graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._compiled_grad_norm), [`_clip_grad_norm`](train.md#TPUTrainer._clip_grad_norm), [`_clip_grad_norm`](graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._clip_grad_norm)  (1 test-only)

## Functions
- <a id="_grad_signature"></a>`_grad_signature(grads: list[torch.Tensor])` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L37)
- <a id="global_grad_norm"></a>`global_grad_norm(grads: list[torch.Tensor])` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L46) — Compute the global L2 norm while preserving DTensor placement semantics.

## Module values
- <a id="GradSignature"></a>`GradSignature` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/grad_norm.py#L26)

