---
title: 'Module: torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.compiled_optimizers.separate_graph`/
symbols:
  _build_compiled_optimizer_groups: _build_compiled_optimizer_groups().
  _build_compiled_optimizer_groups._run: _build_compiled_optimizer_groups()._run().
  apply_compiled_optimizer: apply_compiled_optimizer().
  _tpu_backend_compile_pass: _tpu_backend_compile_pass().
  _build_compiled_optimizer_groups._adamw_step: _build_compiled_optimizer_groups()._adamw_step().
  apply_compiled_optimizer._patched_step: apply_compiled_optimizer()._patched_step().
  _tpu_backend_compile_pass._compiled_forward: _tpu_backend_compile_pass()._compiled_forward().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py)

## Functions
- <a id="_build_compiled_optimizer_groups._adamw_step"></a>`_adamw_step(state, _n=n_params, _b1=beta1, _b2=beta2, _wd=wd, _eps=eps, _maximize=maximize, _capturable=is_capturable)` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L104) — Tracing adapter: unpacks dict state and calls functional_adamw_step.
- <a id="_build_compiled_optimizer_groups"></a>`_build_compiled_optimizer_groups(opt: torch.optim.Optimizer)` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L68)
- <a id="_tpu_backend_compile_pass._compiled_forward"></a>`_compiled_forward(*flat_inputs)` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L53)
- <a id="apply_compiled_optimizer._patched_step"></a>`_patched_step(closure: Any = None)` — [`L204`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L204)
- <a id="_build_compiled_optimizer_groups._run"></a>`_run(live_params, live_grads, live_exp_avgs, live_exp_avg_sqs, live_steps, live_lr, _gm=traced.gm, _n=n_params, _state_fqns=state_fqns, _layouts=traced.output_subclass_layouts, _num_flat=traced.num_flat_outputs)` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L157)
- <a id="_tpu_backend_compile_pass"></a>`_tpu_backend_compile_pass(gm: torch.fx.GraphModule, example_inputs: tuple)` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L25)
- <a id="apply_compiled_optimizer"></a>`apply_compiled_optimizer(trainer: Any)` — [`L190`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L190) — Wraps trainer.optimizers.step() to run AdamW in 1 compiled XLA graph.

## Module values
- <a id="__all__"></a>`__all__` — [`L247`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py#L247)

