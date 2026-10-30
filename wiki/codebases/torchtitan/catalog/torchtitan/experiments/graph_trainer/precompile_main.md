---
title: 'Module: torchtitan/experiments/graph_trainer/precompile_main.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/precompile_main.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.precompile_main`/
symbols:
  _precompile_aot_fx_trace: _precompile_aot_fx_trace().
  _common_setup: _common_setup().
  main: main().
  _prepare_loss_for_precompile: _prepare_loss_for_precompile().
  _precompile_aot_fx_trace.prepare_trace_inputs: _precompile_aot_fx_trace().prepare_trace_inputs().
  _precompile_aot_fx_trace.prepare_trace_call_inputs: _precompile_aot_fx_trace().prepare_trace_call_inputs().
---
# Module: [`torchtitan/experiments/graph_trainer/precompile_main.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py)

## Functions
- <a id="_common_setup"></a>`_common_setup(config)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L51) — Common setup for precompile: fake PG, CooR, model build.
- <a id="_precompile_aot_fx_trace"></a>`_precompile_aot_fx_trace(config, model, model_config, model_spec, compile_config, parallel_dims, device, tokenizer)` — [`L217`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L217) — aot_fx_trace mode precompilation: make_fx tracing + Inductor.
- <a id="_prepare_loss_for_precompile"></a>`_prepare_loss_for_precompile(model, loss_fn)` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L204) — Match Trainer's post-parallelization loss setup for precompile tracing.
- <a id="main"></a>`main()` — [`L374`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L374)
- <a id="_precompile_aot_fx_trace.prepare_trace_call_inputs"></a>`prepare_trace_call_inputs(args: tuple[Any, ...], kwargs: dict[str, Any])` — [`L310`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L310)
- <a id="_precompile_aot_fx_trace.prepare_trace_inputs"></a>`prepare_trace_inputs(args: tuple[Any, ...], kwargs: dict[str, Any])` — [`L304`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/precompile_main.py#L304)

