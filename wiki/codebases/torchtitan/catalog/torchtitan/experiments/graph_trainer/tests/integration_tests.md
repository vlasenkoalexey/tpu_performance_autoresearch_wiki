---
title: 'Module: torchtitan/experiments/graph_trainer/tests/integration_tests.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/integration_tests.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.integration_tests`/
symbols:
  _build_llama3_tests: _build_llama3_tests().
  _build_deepseek_v3_tests: _build_deepseek_v3_tests().
  _TEST_SUITES_FUNCTION: _TEST_SUITES_FUNCTION.
  build_graph_trainer_test_list: build_graph_trainer_test_list().
  _build_qwen3_tests: _build_qwen3_tests().
  _build_async_tp_tests: _build_async_tp_tests().
  build_graph_trainer_h100_test_list: build_graph_trainer_h100_test_list().
  _JIT_DISABLED: _JIT_DISABLED.
  build_graph_trainer_default_test_list: build_graph_trainer_default_test_list().
  _build_autoparallel_tests: _build_autoparallel_tests().
  _build_autoparallel_h100_tests: _build_autoparallel_h100_tests().
  build_graph_trainer_autoparallel_test_list: build_graph_trainer_autoparallel_test_list().
  build_graph_trainer_autoparallel_h100_test_list: build_graph_trainer_autoparallel_h100_test_list().
  _build_muse_glimmer_tests: _build_muse_glimmer_tests().
  main: main().
  _FLEX_CP_INDUCTOR_DISABLED: _FLEX_CP_INDUCTOR_DISABLED.
  _build_deepseek_v3_tests.ep_overlap_parallelism: _build_deepseek_v3_tests().ep_overlap_parallelism().
---
# Module: [`torchtitan/experiments/graph_trainer/tests/integration_tests.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py)

## Functions
- <a id="_build_async_tp_tests"></a>`_build_async_tp_tests()` — [`L696`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L696) — Async TP tests (require NVLink for symmetric memory).
- <a id="_build_autoparallel_h100_tests"></a>`_build_autoparallel_h100_tests()` — [`L767`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L767) — AutoParallel integration tests that require H100 runners.
- <a id="_build_autoparallel_tests"></a>`_build_autoparallel_tests()` — [`L730`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L730) — AutoParallel integration tests for default runners.
- <a id="_build_deepseek_v3_tests"></a>`_build_deepseek_v3_tests()` — [`L274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L274) — DeepSeek-v3-based integration tests (require H100 machines).
- <a id="_build_llama3_tests"></a>`_build_llama3_tests()` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L31) — Llama3-based integration tests (run on default A10 machines).
- <a id="_build_muse_glimmer_tests"></a>`_build_muse_glimmer_tests()` — [`L648`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L648) — MuseGlimmer integration tests.
- <a id="_build_qwen3_tests"></a>`_build_qwen3_tests()` — [`L607`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L607) — Qwen3-based integration tests (dense + MoE).
- <a id="build_graph_trainer_autoparallel_h100_test_list"></a>`build_graph_trainer_autoparallel_h100_test_list()` — [`L802`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L802) — AutoParallel tests that require H100 runners.
- <a id="build_graph_trainer_autoparallel_test_list"></a>`build_graph_trainer_autoparallel_test_list()` — [`L797`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L797) — AutoParallel tests for default runners.
- <a id="build_graph_trainer_default_test_list"></a>`build_graph_trainer_default_test_list()` — [`L691`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L691) — Dense-model tests for default A10 machines.
- <a id="build_graph_trainer_h100_test_list"></a>`build_graph_trainer_h100_test_list()` — [`L792`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L792) — DeepSeek-v3 + Qwen3 + async_tp tests (for H100 machines).
- <a id="build_graph_trainer_test_list"></a>`build_graph_trainer_test_list()` — [`L681`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L681) — All graph_trainer integration tests.
- <a id="_build_deepseek_v3_tests.ep_overlap_parallelism"></a>`ep_overlap_parallelism()` — [`L330`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L330)
- <a id="main"></a>`main()` — [`L816`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L816)

## Module values
- <a id="_FLEX_CP_INDUCTOR_DISABLED"></a>`_FLEX_CP_INDUCTOR_DISABLED` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L28)
- <a id="_JIT_DISABLED"></a>`_JIT_DISABLED` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L24)
- <a id="_TEST_SUITES_FUNCTION"></a>`_TEST_SUITES_FUNCTION` — [`L807`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/integration_tests.py#L807)

