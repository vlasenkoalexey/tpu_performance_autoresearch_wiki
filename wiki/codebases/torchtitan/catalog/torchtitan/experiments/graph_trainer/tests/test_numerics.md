---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_numerics.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_numerics.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_numerics`/
symbols:
  TestSimpleFSDP.parallel_dims: TestSimpleFSDP#parallel_dims.
  _run_graph_pp_deepseek_v3_loss_compare: _run_graph_pp_deepseek_v3_loss_compare().
  TestSimpleFSDP.mode: TestSimpleFSDP#mode.
  TestSimpleFSDP.run_simple_fsdp: TestSimpleFSDP#run_simple_fsdp().
  TestSimpleFSDP.run_simple_fsdp_compiled_aot_eager: TestSimpleFSDP#run_simple_fsdp_compiled_aot_eager().
  TestSimpleFSDP.run_fsdp2: TestSimpleFSDP#run_fsdp2().
  TestSimpleFSDP.test_fullyshard_convergence: TestSimpleFSDP#test_fullyshard_convergence().
  TestSimpleFSDP.test_hybridshard_convergence: TestSimpleFSDP#test_hybridshard_convergence().
  _run_deepseek_v3_loss_compare: _run_deepseek_v3_loss_compare().
  _run_deepseek_v3_ep_overlap_loss_compare: _run_deepseek_v3_ep_overlap_loss_compare().
  _run_deepseek_v3_ep_overlap_moe_seq_loss_compare: _run_deepseek_v3_ep_overlap_moe_seq_loss_compare().
  _run_deepseek_v3_ep_overlap_moe_batch_loss_compare: _run_deepseek_v3_ep_overlap_moe_batch_loss_compare().
  _run_llama3_loss_compare: _run_llama3_loss_compare().
  TestSimpleFSDP.dp_mesh_dim_names: TestSimpleFSDP#dp_mesh_dim_names.
  _run_qwen3_loss_compare: _run_qwen3_loss_compare().
  _run_qwen3_moe_loss_compare: _run_qwen3_moe_loss_compare().
  TestSimpleFSDP.loss_fn: TestSimpleFSDP#loss_fn.
  DEBUGMODEL_TRAINING_OPTIONS: DEBUGMODEL_TRAINING_OPTIONS.
  run_loss_compare: run_loss_compare().
  _run_autoparallel_llama3_loss_compare: _run_autoparallel_llama3_loss_compare().
  _run_autoparallel_deepseek_v3_loss_compare: _run_autoparallel_deepseek_v3_loss_compare().
  DSV3_EP_OVERLAP_GRAPH_BITWISE: DSV3_EP_OVERLAP_GRAPH_BITWISE.
  run_loss_compare_close: run_loss_compare_close().
  AUTOPARALLEL_DSV3_PARALLELISM: AUTOPARALLEL_DSV3_PARALLELISM.
  STEPS: STEPS.
  GRAPH_PP_DSV3_TEST_PARALLELISM: GRAPH_PP_DSV3_TEST_PARALLELISM.
  DSV3_EP_OVERLAP_GRAPH_PARALLELISM: DSV3_EP_OVERLAP_GRAPH_PARALLELISM.
  DSV3_EP_OVERLAP_EAGER: DSV3_EP_OVERLAP_EAGER.
  TestSimpleFSDP.init_test: TestSimpleFSDP#init_test().
  TestSimpleFSDP.optimizer: TestSimpleFSDP#optimizer.
  TestSimpleFSDP.get_input: TestSimpleFSDP#get_input().
  TestGraphTrainerNumerics.test_dense_llama3_aot_fx_trace_vs_eager: TestGraphTrainerNumerics#test_dense_llama3_aot_fx_trace_vs_eager().
  TestGraphTrainerNumerics.test_dense_llama3_jit_vs_eager: TestGraphTrainerNumerics#test_dense_llama3_jit_vs_eager().
  TestGraphTrainerNumerics.test_dense_llama3_auto_bucketing_jit_vs_eager: TestGraphTrainerNumerics#test_dense_llama3_auto_bucketing_jit_vs_eager().
  TestGraphTrainerNumerics.test_dense_llama3_manual_bucketing_jit_vs_eager: TestGraphTrainerNumerics#test_dense_llama3_manual_bucketing_jit_vs_eager().
  TestGraphTrainerNumerics.test_moe_dsv3_jit_vs_eager: TestGraphTrainerNumerics#test_moe_dsv3_jit_vs_eager().
  TestGraphTrainerNumerics.test_moe_dsv3_manual_bucketing_jit_vs_eager: TestGraphTrainerNumerics#test_moe_dsv3_manual_bucketing_jit_vs_eager().
  TestGraphTrainerNumerics.test_moe_dsv3_aot_fx_trace_vs_eager: TestGraphTrainerNumerics#test_moe_dsv3_aot_fx_trace_vs_eager().
  TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_aot_fx_trace_vs_eager_chunked: TestGraphTrainerNumerics#test_moe_dsv3_ep_overlap_aot_fx_trace_vs_eager_chunked().
  TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_seq_aot_fx_trace_vs_eager_chunked: TestGraphTrainerNumerics#test_moe_dsv3_ep_overlap_moe_seq_aot_fx_trace_vs_eager_chunked().
  TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_batch_aot_fx_trace_vs_eager_chunked: TestGraphTrainerNumerics#test_moe_dsv3_ep_overlap_moe_batch_aot_fx_trace_vs_eager_chunked().
  TestGraphTrainerNumerics.test_graph_pp_moe_dsv3_aot_fx_trace_vs_eager: TestGraphTrainerNumerics#test_graph_pp_moe_dsv3_aot_fx_trace_vs_eager().
  TestGraphTrainerNumerics.test_dense_qwen3_aot_fx_trace_vs_eager: TestGraphTrainerNumerics#test_dense_qwen3_aot_fx_trace_vs_eager().
  TestGraphTrainerNumerics.test_moe_qwen3_aot_fx_trace_vs_eager: TestGraphTrainerNumerics#test_moe_qwen3_aot_fx_trace_vs_eager().
  TestGraphTrainerAutoParallelNumerics.test_llama3_aot_fx_trace_autoparallel_vs_eager: TestGraphTrainerAutoParallelNumerics#test_llama3_aot_fx_trace_autoparallel_vs_eager().
  TestGraphTrainerAutoParallelNumerics.test_deepseek_v3_aot_fx_trace_autoparallel_vs_eager: TestGraphTrainerAutoParallelNumerics#test_deepseek_v3_aot_fx_trace_autoparallel_vs_eager().
  _log_rank: _log_rank().
  _extract_losses_from_rank_tensorboard: _extract_losses_from_rank_tensorboard().
  DSV3_EP_OVERLAP_OPTIONS: DSV3_EP_OVERLAP_OPTIONS.
  DSV3_EP_OVERLAP_MOE_SEQ_OPTIONS: DSV3_EP_OVERLAP_MOE_SEQ_OPTIONS.
  DSV3_EP_OVERLAP_MOE_BATCH_OPTIONS: DSV3_EP_OVERLAP_MOE_BATCH_OPTIONS.
  GRAPH_PP_DSV3_PP_OPTIONS: GRAPH_PP_DSV3_PP_OPTIONS.
  AUTOPARALLEL_LLAMA3_PARALLELISM: AUTOPARALLEL_LLAMA3_PARALLELISM.
  _losses_are_equal: _losses_are_equal().
  LLAMA3_PARALLELISM: LLAMA3_PARALLELISM.
  DSV3_PARALLELISM: DSV3_PARALLELISM.
  DSV3_EP_OVERLAP_GRAPH: DSV3_EP_OVERLAP_GRAPH.
  QWEN3_PARALLELISM: QWEN3_PARALLELISM.
  QWEN3_MOE_PARALLELISM: QWEN3_MOE_PARALLELISM.
  TestGraphTrainerNumerics: TestGraphTrainerNumerics#
  TestGraphTrainerAutoParallelNumerics: TestGraphTrainerAutoParallelNumerics#
  TestSimpleFSDP: TestSimpleFSDP#
  TestSimpleFSDP.test_replicate_convergence: TestSimpleFSDP#test_replicate_convergence().
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_numerics.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py)

> **Collapsed catalog** (63 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="AUTOPARALLEL_DSV3_PARALLELISM"></a>`AUTOPARALLEL_DSV3_PARALLELISM` — [`L534`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L534)
- <a id="AUTOPARALLEL_LLAMA3_PARALLELISM"></a>`AUTOPARALLEL_LLAMA3_PARALLELISM` — [`L504`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L504)
- <a id="DEBUGMODEL_TRAINING_OPTIONS"></a>`DEBUGMODEL_TRAINING_OPTIONS` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L231)
- <a id="DSV3_EP_OVERLAP_EAGER"></a>`DSV3_EP_OVERLAP_EAGER` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L282)
- <a id="DSV3_EP_OVERLAP_GRAPH"></a>`DSV3_EP_OVERLAP_GRAPH` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L283)
- <a id="DSV3_EP_OVERLAP_GRAPH_BITWISE"></a>`DSV3_EP_OVERLAP_GRAPH_BITWISE` — [`L284`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L284)
- <a id="DSV3_EP_OVERLAP_GRAPH_PARALLELISM"></a>`DSV3_EP_OVERLAP_GRAPH_PARALLELISM` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L258)
- <a id="DSV3_EP_OVERLAP_MOE_BATCH_OPTIONS"></a>`DSV3_EP_OVERLAP_MOE_BATCH_OPTIONS` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L276)
- <a id="DSV3_EP_OVERLAP_MOE_SEQ_OPTIONS"></a>`DSV3_EP_OVERLAP_MOE_SEQ_OPTIONS` — [`L270`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L270)
- <a id="DSV3_EP_OVERLAP_OPTIONS"></a>`DSV3_EP_OVERLAP_OPTIONS` — [`L264`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L264)
- <a id="DSV3_PARALLELISM"></a>`DSV3_PARALLELISM` — [`L253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L253)
- <a id="GRAPH_PP_DSV3_PP_OPTIONS"></a>`GRAPH_PP_DSV3_PP_OPTIONS` — [`L355`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L355)
- <a id="GRAPH_PP_DSV3_TEST_PARALLELISM"></a>`GRAPH_PP_DSV3_TEST_PARALLELISM` — [`L373`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L373)
- <a id="LLAMA3_PARALLELISM"></a>`LLAMA3_PARALLELISM` — [`L227`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L227)
- <a id="QWEN3_MOE_PARALLELISM"></a>`QWEN3_MOE_PARALLELISM` — [`L480`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L480)
- <a id="QWEN3_PARALLELISM"></a>`QWEN3_PARALLELISM` — [`L458`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L458)
- <a id="STEPS"></a>`STEPS` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L28)
- <a id="TestGraphTrainerAutoParallelNumerics"></a>`TestGraphTrainerAutoParallelNumerics` — [`L662`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L662)
- <a id="TestGraphTrainerAutoParallelNumerics.test_deepseek_v3_aot_fx_trace_autoparallel_vs_eager"></a>`TestGraphTrainerAutoParallelNumerics.test_deepseek_v3_aot_fx_trace_autoparallel_vs_eager` — [`L683`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L683)
- <a id="TestGraphTrainerAutoParallelNumerics.test_llama3_aot_fx_trace_autoparallel_vs_eager"></a>`TestGraphTrainerAutoParallelNumerics.test_llama3_aot_fx_trace_autoparallel_vs_eager` — [`L679`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L679)
- <a id="TestGraphTrainerNumerics"></a>`TestGraphTrainerNumerics` — [`L560`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L560)
- <a id="TestGraphTrainerNumerics.test_dense_llama3_aot_fx_trace_vs_eager"></a>`TestGraphTrainerNumerics.test_dense_llama3_aot_fx_trace_vs_eager` — [`L563`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L563)
- <a id="TestGraphTrainerNumerics.test_dense_llama3_auto_bucketing_jit_vs_eager"></a>`TestGraphTrainerNumerics.test_dense_llama3_auto_bucketing_jit_vs_eager` — [`L575`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L575)
- <a id="TestGraphTrainerNumerics.test_dense_llama3_jit_vs_eager"></a>`TestGraphTrainerNumerics.test_dense_llama3_jit_vs_eager` — [`L569`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L569)
- <a id="TestGraphTrainerNumerics.test_dense_llama3_manual_bucketing_jit_vs_eager"></a>`TestGraphTrainerNumerics.test_dense_llama3_manual_bucketing_jit_vs_eager` — [`L583`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L583)
- <a id="TestGraphTrainerNumerics.test_dense_qwen3_aot_fx_trace_vs_eager"></a>`TestGraphTrainerNumerics.test_dense_qwen3_aot_fx_trace_vs_eager` — [`L645`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L645)
- <a id="TestGraphTrainerNumerics.test_graph_pp_moe_dsv3_aot_fx_trace_vs_eager"></a>`TestGraphTrainerNumerics.test_graph_pp_moe_dsv3_aot_fx_trace_vs_eager` — [`L640`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L640)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_aot_fx_trace_vs_eager"></a>`TestGraphTrainerNumerics.test_moe_dsv3_aot_fx_trace_vs_eager` — [`L612`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L612)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_aot_fx_trace_vs_eager_chunked"></a>`TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_aot_fx_trace_vs_eager_chunked` — [`L624`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L624)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_batch_aot_fx_trace_vs_eager_chunked"></a>`TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_batch_aot_fx_trace_vs_eager_chunked` — [`L630`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L630)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_seq_aot_fx_trace_vs_eager_chunked"></a>`TestGraphTrainerNumerics.test_moe_dsv3_ep_overlap_moe_seq_aot_fx_trace_vs_eager_chunked` — [`L627`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L627)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_jit_vs_eager"></a>`TestGraphTrainerNumerics.test_moe_dsv3_jit_vs_eager` — [`L591`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L591)
- <a id="TestGraphTrainerNumerics.test_moe_dsv3_manual_bucketing_jit_vs_eager"></a>`TestGraphTrainerNumerics.test_moe_dsv3_manual_bucketing_jit_vs_eager` — [`L598`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L598)
- <a id="TestGraphTrainerNumerics.test_moe_qwen3_aot_fx_trace_vs_eager"></a>`TestGraphTrainerNumerics.test_moe_qwen3_aot_fx_trace_vs_eager` — [`L650`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L650)
- <a id="TestSimpleFSDP"></a>`TestSimpleFSDP` — [`L687`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L687)
- <a id="TestSimpleFSDP.dp_mesh_dim_names"></a>`TestSimpleFSDP.dp_mesh_dim_names` — [`L693`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L693)
- <a id="TestSimpleFSDP.get_input"></a>`TestSimpleFSDP.get_input` — [`L715`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L715)
- <a id="TestSimpleFSDP.init_test"></a>`TestSimpleFSDP.init_test` — [`L688`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L688)
- <a id="TestSimpleFSDP.loss_fn"></a>`TestSimpleFSDP.loss_fn` — [`L690`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L690)
- <a id="TestSimpleFSDP.mode"></a>`TestSimpleFSDP.mode` — [`L772`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L772)
- <a id="TestSimpleFSDP.optimizer"></a>`TestSimpleFSDP.optimizer` — [`L689`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L689)
- <a id="TestSimpleFSDP.parallel_dims"></a>`TestSimpleFSDP.parallel_dims` — [`L704`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L704)
- <a id="TestSimpleFSDP.run_fsdp2"></a>`TestSimpleFSDP.run_fsdp2` — [`L721`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L721)
- <a id="TestSimpleFSDP.run_simple_fsdp"></a>`TestSimpleFSDP.run_simple_fsdp` — [`L734`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L734)
- <a id="TestSimpleFSDP.run_simple_fsdp_compiled_aot_eager"></a>`TestSimpleFSDP.run_simple_fsdp_compiled_aot_eager` — [`L751`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L751)
- <a id="TestSimpleFSDP.test_fullyshard_convergence"></a>`TestSimpleFSDP.test_fullyshard_convergence` — [`L790`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L790)
- <a id="TestSimpleFSDP.test_hybridshard_convergence"></a>`TestSimpleFSDP.test_hybridshard_convergence` — [`L810`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L810)
- <a id="TestSimpleFSDP.test_replicate_convergence"></a>`TestSimpleFSDP.test_replicate_convergence` — [`L770`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L770)
- <a id="_extract_losses_from_rank_tensorboard"></a>`_extract_losses_from_rank_tensorboard` — [`L193`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L193)
- <a id="_log_rank"></a>`_log_rank` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L159)
- <a id="_losses_are_equal"></a>`_losses_are_equal` — [`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L171)
- <a id="_run_autoparallel_deepseek_v3_loss_compare"></a>`_run_autoparallel_deepseek_v3_loss_compare` — [`L541`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L541)
- <a id="_run_autoparallel_llama3_loss_compare"></a>`_run_autoparallel_llama3_loss_compare` — [`L510`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L510)
- <a id="_run_deepseek_v3_ep_overlap_loss_compare"></a>`_run_deepseek_v3_ep_overlap_loss_compare` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L316)
- <a id="_run_deepseek_v3_ep_overlap_moe_batch_loss_compare"></a>`_run_deepseek_v3_ep_overlap_moe_batch_loss_compare` — [`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L341)
- <a id="_run_deepseek_v3_ep_overlap_moe_seq_loss_compare"></a>`_run_deepseek_v3_ep_overlap_moe_seq_loss_compare` — [`L328`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L328)
- <a id="_run_deepseek_v3_loss_compare"></a>`_run_deepseek_v3_loss_compare` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L289)
- <a id="_run_graph_pp_deepseek_v3_loss_compare"></a>`_run_graph_pp_deepseek_v3_loss_compare` — [`L380`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L380)
- <a id="_run_llama3_loss_compare"></a>`_run_llama3_loss_compare` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L237)
- <a id="_run_qwen3_loss_compare"></a>`_run_qwen3_loss_compare` — [`L464`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L464)
- <a id="_run_qwen3_moe_loss_compare"></a>`_run_qwen3_moe_loss_compare` — [`L488`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L488)
- <a id="run_loss_compare"></a>`run_loss_compare` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L31)
- <a id="run_loss_compare_close"></a>`run_loss_compare_close` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_numerics.py#L86)
