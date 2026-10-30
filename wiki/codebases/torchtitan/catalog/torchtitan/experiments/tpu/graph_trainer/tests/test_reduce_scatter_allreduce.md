---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_reduce_scatter_allreduce`/
symbols:
  TestReduceScatterAllReduce.test_local_shard_is_not_a_view_of_the_full_result: TestReduceScatterAllReduce#test_local_shard_is_not_a_view_of_the_full_result().
  TestReduceScatterAllReduce._make_graph: TestReduceScatterAllReduce#_make_graph().
  TestReduceScatterAllReduce.test_rewrites_qkv_reduce_scatter: TestReduceScatterAllReduce#test_rewrites_qkv_reduce_scatter().
  TestReduceScatterAllReduce.test_rewrites_output_projection_reduce_scatter: TestReduceScatterAllReduce#test_rewrites_output_projection_reduce_scatter().
  TestReduceScatterAllReduce.test_missing_pattern_errors_without_mutating_graph: TestReduceScatterAllReduce#test_missing_pattern_errors_without_mutating_graph().
  TestReduceScatterAllReduce.test_rewrites_selected_bf16_gradient: TestReduceScatterAllReduce#test_rewrites_selected_bf16_gradient().
  TestReduceScatterAllReduce.test_selected_mixed_dtype_gradient_errors_without_mutating_graph: TestReduceScatterAllReduce#test_selected_mixed_dtype_gradient_errors_without_mutating_graph().
  TestReduceScatterAllReduce.test_selected_subgroup_gradient_errors_without_mutating_graph: TestReduceScatterAllReduce#test_selected_subgroup_gradient_errors_without_mutating_graph().
  TestReduceScatterAllReduce.test_selected_oversized_gradient_errors_without_mutating_graph: TestReduceScatterAllReduce#test_selected_oversized_gradient_errors_without_mutating_graph().
  _MAX_INPUT_BYTES: _MAX_INPUT_BYTES.
  _QKV_PATTERN: _QKV_PATTERN.
  _O_PATTERN: _O_PATTERN.
  _identity_all_reduce: _identity_all_reduce().
  _identity_wait: _identity_wait().
  TestReduceScatterAllReduce: TestReduceScatterAllReduce#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py)

> **Collapsed catalog** (15 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestReduceScatterAllReduce"></a>`TestReduceScatterAllReduce` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L39)
- <a id="TestReduceScatterAllReduce._make_graph"></a>`TestReduceScatterAllReduce._make_graph` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L40)
- <a id="TestReduceScatterAllReduce.test_local_shard_is_not_a_view_of_the_full_result"></a>`TestReduceScatterAllReduce.test_local_shard_is_not_a_view_of_the_full_result` — [`L140`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L140)
- <a id="TestReduceScatterAllReduce.test_missing_pattern_errors_without_mutating_graph"></a>`TestReduceScatterAllReduce.test_missing_pattern_errors_without_mutating_graph` — [`L170`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L170)
- <a id="TestReduceScatterAllReduce.test_rewrites_output_projection_reduce_scatter"></a>`TestReduceScatterAllReduce.test_rewrites_output_projection_reduce_scatter` — [`L117`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L117)
- <a id="TestReduceScatterAllReduce.test_rewrites_qkv_reduce_scatter"></a>`TestReduceScatterAllReduce.test_rewrites_qkv_reduce_scatter` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L78)
- <a id="TestReduceScatterAllReduce.test_rewrites_selected_bf16_gradient"></a>`TestReduceScatterAllReduce.test_rewrites_selected_bf16_gradient` — [`L206`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L206)
- <a id="TestReduceScatterAllReduce.test_selected_mixed_dtype_gradient_errors_without_mutating_graph"></a>`TestReduceScatterAllReduce.test_selected_mixed_dtype_gradient_errors_without_mutating_graph` — [`L226`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L226)
- <a id="TestReduceScatterAllReduce.test_selected_oversized_gradient_errors_without_mutating_graph"></a>`TestReduceScatterAllReduce.test_selected_oversized_gradient_errors_without_mutating_graph` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L186)
- <a id="TestReduceScatterAllReduce.test_selected_subgroup_gradient_errors_without_mutating_graph"></a>`TestReduceScatterAllReduce.test_selected_subgroup_gradient_errors_without_mutating_graph` — [`L244`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L244)
- <a id="_MAX_INPUT_BYTES"></a>`_MAX_INPUT_BYTES` — [`L25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L25)
- <a id="_O_PATTERN"></a>`_O_PATTERN` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L24)
- <a id="_QKV_PATTERN"></a>`_QKV_PATTERN` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L23)
- <a id="_identity_all_reduce"></a>`_identity_all_reduce` — [`L28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L28)
- <a id="_identity_wait"></a>`_identity_wait` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py#L35)
