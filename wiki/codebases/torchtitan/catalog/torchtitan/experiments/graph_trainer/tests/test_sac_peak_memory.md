---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_sac_peak_memory`/
symbols:
  TestGraphSACPeakMemory.test_llama3_debugmodel_peak_memory_matches_eager_selective_ac: TestGraphSACPeakMemory#test_llama3_debugmodel_peak_memory_matches_eager_selective_ac().
  TestGraphSACPeakMemory.test_llama3_debugmodel_full_ac_numerics_match_eager: TestGraphSACPeakMemory#test_llama3_debugmodel_full_ac_numerics_match_eager().
  _measure_step: _measure_step().
  _build_model: _build_model().
  TestGraphSACPeakMemory.tokens: TestGraphSACPeakMemory#tokens.
  TestGraphSACPeakMemory.labels: TestGraphSACPeakMemory#labels.
  DEBUGMODEL: DEBUGMODEL.
  StepResult.loss: StepResult#loss.
  TestGraphSACPeakMemory.setUp: TestGraphSACPeakMemory#setUp().
  StepResult.grads: StepResult#grads.
  StepResult.reserved_gib: StepResult#reserved_gib.
  StepResult.active_gib: StepResult#active_gib.
  TestGraphSACPeakMemory.state_dict: TestGraphSACPeakMemory#state_dict.
  NUM_TOKENS: NUM_TOKENS.
  MAX_PEAK_MEMORY_RATIO: MAX_PEAK_MEMORY_RATIO.
  StepResult: StepResult#
  DTYPE: DTYPE.
  _set_deterministic: _set_deterministic().
  TestGraphSACPeakMemory: TestGraphSACPeakMemory#
  TestGraphSACPeakMemory.tearDown: TestGraphSACPeakMemory#tearDown().
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="DEBUGMODEL"></a>`DEBUGMODEL` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L27)
- <a id="DTYPE"></a>`DTYPE` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L24)
- <a id="MAX_PEAK_MEMORY_RATIO"></a>`MAX_PEAK_MEMORY_RATIO` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L26)
- <a id="NUM_TOKENS"></a>`NUM_TOKENS` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L25)
- <a id="StepResult"></a>`StepResult` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L49)
- <a id="StepResult.active_gib"></a>`StepResult.active_gib` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L53)
- <a id="StepResult.grads"></a>`StepResult.grads` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L51)
- <a id="StepResult.loss"></a>`StepResult.loss` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L50)
- <a id="StepResult.reserved_gib"></a>`StepResult.reserved_gib` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L52)
- <a id="TestGraphSACPeakMemory"></a>`TestGraphSACPeakMemory` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L86)
- <a id="TestGraphSACPeakMemory.labels"></a>`TestGraphSACPeakMemory.labels` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L97)
- <a id="TestGraphSACPeakMemory.setUp"></a>`TestGraphSACPeakMemory.setUp` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L87)
- <a id="TestGraphSACPeakMemory.state_dict"></a>`TestGraphSACPeakMemory.state_dict` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L90)
- <a id="TestGraphSACPeakMemory.tearDown"></a>`TestGraphSACPeakMemory.tearDown` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L99)
- <a id="TestGraphSACPeakMemory.test_llama3_debugmodel_full_ac_numerics_match_eager"></a>`TestGraphSACPeakMemory.test_llama3_debugmodel_full_ac_numerics_match_eager` — [`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L163) — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="TestGraphSACPeakMemory.test_llama3_debugmodel_peak_memory_matches_eager_selective_ac"></a>`TestGraphSACPeakMemory.test_llama3_debugmodel_peak_memory_matches_eager_selective_ac` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L102) — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="TestGraphSACPeakMemory.tokens"></a>`TestGraphSACPeakMemory.tokens` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L96)
- <a id="_build_model"></a>`_build_model` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L36)
- <a id="_measure_step"></a>`_measure_step` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L56)
- <a id="_set_deterministic"></a>`_set_deterministic` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py#L30)
