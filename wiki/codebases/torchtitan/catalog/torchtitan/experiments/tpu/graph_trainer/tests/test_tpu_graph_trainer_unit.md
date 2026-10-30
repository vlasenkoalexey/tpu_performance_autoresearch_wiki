---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_tpu_graph_trainer_unit`/
symbols:
  TpuGraphTrainerUnitTest.test_fwd_bwd_adamw_grad_clipping_tracing: TpuGraphTrainerUnitTest#test_fwd_bwd_adamw_grad_clipping_tracing().
  TpuGraphTrainerUnitTest.test_from_tpu_trainer_config_target_cls: TpuGraphTrainerUnitTest#test_from_tpu_trainer_config_target_cls().
  TpuGraphTrainerUnitTest.test_make_fx_tracing_on_synthetic_model: TpuGraphTrainerUnitTest#test_make_fx_tracing_on_synthetic_model().
  TpuGraphTrainerUnitTest.test_pallas_ce_loss_override: TpuGraphTrainerUnitTest#test_pallas_ce_loss_override().
  TpuGraphTrainerUnitTest.config: TpuGraphTrainerUnitTest#config.
  DummyModule.forward: DummyModule#forward().
  MfuBenchmarkTest.test_mfu_benchmark_bracket: MfuBenchmarkTest#test_mfu_benchmark_bracket().
  TpuGraphTrainerUnitTest.config_manager: TpuGraphTrainerUnitTest#config_manager.
  _make_dummy_fwd_bwd_step: _make_dummy_fwd_bwd_step().
  TpuGraphTrainerUnitTest: TpuGraphTrainerUnitTest#
  TpuGraphTrainerUnitTest.setUp: TpuGraphTrainerUnitTest#setUp().
  DummyModule: DummyModule#
  DummyModule.tok_embeddings: DummyModule#tok_embeddings.
  DummyModule.linear: DummyModule#linear.
  DummyModule.lm_head: DummyModule#lm_head.
  _make_dummy_fwd_bwd_step.fwd_bwd_fn: _make_dummy_fwd_bwd_step().fwd_bwd_fn().
  TpuGraphTrainerUnitTest.loss_fn: TpuGraphTrainerUnitTest#loss_fn().
  DummyModule.__init__: DummyModule#__init__().
  MfuBenchmarkTest: MfuBenchmarkTest#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py)

> **Collapsed catalog** (19 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="DummyModule"></a>`DummyModule` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L29)
- <a id="DummyModule.__init__"></a>`DummyModule.__init__` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L32)
- <a id="DummyModule.forward"></a>`DummyModule.forward` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L38)
- <a id="DummyModule.linear"></a>`DummyModule.linear` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L35)
- <a id="DummyModule.lm_head"></a>`DummyModule.lm_head` — [`L36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L36)
- <a id="DummyModule.tok_embeddings"></a>`DummyModule.tok_embeddings` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L34)
- <a id="MfuBenchmarkTest"></a>`MfuBenchmarkTest` — [`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L56)
- <a id="MfuBenchmarkTest.test_mfu_benchmark_bracket"></a>`MfuBenchmarkTest.test_mfu_benchmark_bracket` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L58)
- <a id="TpuGraphTrainerUnitTest"></a>`TpuGraphTrainerUnitTest` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L93)
- <a id="TpuGraphTrainerUnitTest.config"></a>`TpuGraphTrainerUnitTest.config` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L101)
- <a id="TpuGraphTrainerUnitTest.config_manager"></a>`TpuGraphTrainerUnitTest.config_manager` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L98)
- <a id="TpuGraphTrainerUnitTest.loss_fn"></a>`TpuGraphTrainerUnitTest.loss_fn` — [`L198`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L198)
- <a id="TpuGraphTrainerUnitTest.setUp"></a>`TpuGraphTrainerUnitTest.setUp` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L96)
- <a id="TpuGraphTrainerUnitTest.test_from_tpu_trainer_config_target_cls"></a>`TpuGraphTrainerUnitTest.test_from_tpu_trainer_config_target_cls` — [`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L112)
- <a id="TpuGraphTrainerUnitTest.test_fwd_bwd_adamw_grad_clipping_tracing"></a>`TpuGraphTrainerUnitTest.test_fwd_bwd_adamw_grad_clipping_tracing` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L193)
- <a id="TpuGraphTrainerUnitTest.test_make_fx_tracing_on_synthetic_model"></a>`TpuGraphTrainerUnitTest.test_make_fx_tracing_on_synthetic_model` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L150)
- <a id="TpuGraphTrainerUnitTest.test_pallas_ce_loss_override"></a>`TpuGraphTrainerUnitTest.test_pallas_ce_loss_override` — [`L127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L127)
- <a id="_make_dummy_fwd_bwd_step"></a>`_make_dummy_fwd_bwd_step` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L43)
- <a id="_make_dummy_fwd_bwd_step.fwd_bwd_fn"></a>`_make_dummy_fwd_bwd_step.fwd_bwd_fn` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py#L46)
