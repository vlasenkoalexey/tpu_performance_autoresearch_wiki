---
title: 'Module: torchtitan/experiments/graph_trainer/llama3/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/llama3/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.llama3.config_registry`/
symbols:
  graph_trainer_llama3_debugmodel_sdpa: graph_trainer_llama3_debugmodel_sdpa().
  graph_trainer_llama3_debugmodel_sdc_replay: graph_trainer_llama3_debugmodel_sdc_replay().
  graph_trainer_llama3_debugmodel_mxfp8: graph_trainer_llama3_debugmodel_mxfp8().
  graph_trainer_llama3_8b_c4_test: graph_trainer_llama3_8b_c4_test().
  graph_trainer_llama3_8b_mxfp8: graph_trainer_llama3_8b_mxfp8().
  graph_trainer_llama3_debugmodel_sdpa_cross_entropy_loss: graph_trainer_llama3_debugmodel_sdpa_cross_entropy_loss().
  graph_trainer_llama3_debugmodel: graph_trainer_llama3_debugmodel().
  graph_trainer_llama3_8b: graph_trainer_llama3_8b().
  graph_trainer_llama3_debugmodel_dist_gemm: graph_trainer_llama3_debugmodel_dist_gemm().
  graph_trainer_llama3_debugmodel_sdpa_eager: graph_trainer_llama3_debugmodel_sdpa_eager().
  graph_trainer_llama3_70b: graph_trainer_llama3_70b().
  graph_trainer_llama3_405b: graph_trainer_llama3_405b().
---
# Module: [`torchtitan/experiments/graph_trainer/llama3/config_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py)

## Functions
- <a id="graph_trainer_llama3_405b"></a>`graph_trainer_llama3_405b()` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L159)
- <a id="graph_trainer_llama3_70b"></a>`graph_trainer_llama3_70b()` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L153)
- <a id="graph_trainer_llama3_8b"></a>`graph_trainer_llama3_8b()` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L123)
- <a id="graph_trainer_llama3_8b_c4_test"></a>`graph_trainer_llama3_8b_c4_test()` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L129)
- <a id="graph_trainer_llama3_8b_mxfp8"></a>`graph_trainer_llama3_8b_mxfp8()` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L137)
- <a id="graph_trainer_llama3_debugmodel"></a>`graph_trainer_llama3_debugmodel()` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L32)
- <a id="graph_trainer_llama3_debugmodel_dist_gemm"></a>`graph_trainer_llama3_debugmodel_dist_gemm()` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L48) — Debug model with the attention and FFN TP collectives folded into the GEMMs.
- <a id="graph_trainer_llama3_debugmodel_mxfp8"></a>`graph_trainer_llama3_debugmodel_mxfp8()` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L64)
- <a id="graph_trainer_llama3_debugmodel_sdc_replay"></a>`graph_trainer_llama3_debugmodel_sdc_replay()` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L38)
- <a id="graph_trainer_llama3_debugmodel_sdpa"></a>`graph_trainer_llama3_debugmodel_sdpa()` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L78) — Debug model on the test-only SDPA backend.
- <a id="graph_trainer_llama3_debugmodel_sdpa_cross_entropy_loss"></a>`graph_trainer_llama3_debugmodel_sdpa_cross_entropy_loss()` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L99) — SDPA debug model with standard cross-entropy loss.
- <a id="graph_trainer_llama3_debugmodel_sdpa_eager"></a>`graph_trainer_llama3_debugmodel_sdpa_eager()` — [`L109`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/llama3/config_registry.py#L109) — SDPA debug model run eagerly (no graph tracing).

