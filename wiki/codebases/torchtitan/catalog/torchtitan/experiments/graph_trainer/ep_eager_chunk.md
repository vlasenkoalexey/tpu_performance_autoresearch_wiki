---
title: 'Module: torchtitan/experiments/graph_trainer/ep_eager_chunk.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/ep_eager_chunk.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.ep_eager_chunk`/
symbols:
  maybe_apply_ep_overlap_eager_chunking: maybe_apply_ep_overlap_eager_chunking().
  _EagerChunkedForward.split_transformer_block_inputs: _EagerChunkedForward#split_transformer_block_inputs().
  _EagerChunkedForward.__call__: _EagerChunkedForward#__call__().
  _contract_error: _contract_error().
  _EagerChunkedForward.split_tensor: _EagerChunkedForward#split_tensor().
  _EagerChunkedForward.split_attention_masks: _EagerChunkedForward#split_attention_masks().
  _EagerChunkedForward.split_positions: _EagerChunkedForward#split_positions().
  _EagerChunkedForward.root_fqn: _EagerChunkedForward#root_fqn.
  _EagerChunkedForward.split_moe_inputs: _EagerChunkedForward#split_moe_inputs().
  _EagerChunkedForward.chunk_dim: _EagerChunkedForward#chunk_dim.
  _EagerChunkedForward.root_kind: _EagerChunkedForward#root_kind.
  _wrap_forward_with_eager_chunking: _wrap_forward_with_eager_chunking().
  populate_eager_chunk_metadata_pass: populate_eager_chunk_metadata_pass().
  _EagerChunkedForward.dim: _EagerChunkedForward#dim.
  _cat_chunked_outputs: _cat_chunked_outputs().
  _describe_value: _describe_value().
  _EagerChunkedForward.split_block_mask: _EagerChunkedForward#split_block_mask().
  _chunk_dim_index: _chunk_dim_index().
  _describe_inputs: _describe_inputs().
  _EagerChunkedForward.__init__: _EagerChunkedForward#__init__().
  _EagerChunkedForward: _EagerChunkedForward#
  _expected_contract: _expected_contract().
  _EagerChunkedForward.inner_forward: _EagerChunkedForward#inner_forward.
---
# Module: [`torchtitan/experiments/graph_trainer/ep_eager_chunk.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py)

## Classes
### <a id="_EagerChunkedForward"></a>`_EagerChunkedForward`
- def: [`torchtitan/experiments/graph_trainer/ep_eager_chunk.py:128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L128)
- signature: `class _EagerChunkedForward:`
- members:
  - <a id="_EagerChunkedForward.split_attention_masks"></a>`split_attention_masks(value: Any)` — [`L266`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L266)
  - <a id="_EagerChunkedForward.split_block_mask"></a>`split_block_mask(value: Any)` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L144)
  - <a id="_EagerChunkedForward.split_moe_inputs"></a>`split_moe_inputs()` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L202)
  - <a id="_EagerChunkedForward.split_positions"></a>`split_positions(value: Any)` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L284)
  - <a id="_EagerChunkedForward.split_tensor"></a>`split_tensor(value: torch.Tensor, *, logical_name: str)` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L166)
  - <a id="_EagerChunkedForward.split_transformer_block_inputs"></a>`split_transformer_block_inputs()` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L214)
  - <a id="_EagerChunkedForward.chunk_dim"></a>`chunk_dim` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L139)
  - <a id="_EagerChunkedForward.dim"></a>`dim` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L141)
  - <a id="_EagerChunkedForward.inner_forward"></a>`inner_forward` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L137)
  - <a id="_EagerChunkedForward.root_fqn"></a>`root_fqn` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L138)
  - <a id="_EagerChunkedForward.root_kind"></a>`root_kind` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L140)
- protocol/private: <a id="_EagerChunkedForward.__call__"></a>`__call__`[`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L143), <a id="_EagerChunkedForward.__init__"></a>`__init__`[`L129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L129)
- uses (calls/refs, reference-scoped): [`_contract_error`](ep_eager_chunk.md#_contract_error), [`EpOverlapChunkDim`](configs.md#EpOverlapChunkDim), [`_cat_chunked_outputs`](ep_eager_chunk.md#_cat_chunked_outputs), [`_chunk_dim_index`](ep_eager_chunk.md#_chunk_dim_index)
- used by: [`_wrap_forward_with_eager_chunking`](ep_eager_chunk.md#_wrap_forward_with_eager_chunking)

## Functions
- <a id="_cat_chunked_outputs"></a>`_cat_chunked_outputs(outputs: list[Any], dim: int, root_fqn: str)` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L40) — Recursively cat Tensor outputs while preserving tuple/list structure.
- <a id="_chunk_dim_index"></a>`_chunk_dim_index(mode: EpOverlapChunkDim)` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L35) — Map logical EP chunk mode to the tensor dimension used by eager wrappers.
- <a id="_contract_error"></a>`_contract_error(*, root_fqn: str, root_kind: str, chunk_dim: EpOverlapChunkDim, args: tuple[Any, ...], kwargs: dict[str, Any], reason: str)` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L109)
- <a id="_describe_inputs"></a>`_describe_inputs(args: tuple[Any, ...], kwargs: dict[str, Any])` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L91)
- <a id="_describe_value"></a>`_describe_value(value: Any)` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L77)
- <a id="_expected_contract"></a>`_expected_contract(root_kind: str)` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L99)
- <a id="_wrap_forward_with_eager_chunking"></a>`_wrap_forward_with_eager_chunking(module: nn.Module, *, root_fqn: str, chunk_dim: EpOverlapChunkDim, root_kind: str)` — [`L343`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L343) — Install an idempotent two-chunk forward wrapper on ``module``.
- <a id="maybe_apply_ep_overlap_eager_chunking"></a>`maybe_apply_ep_overlap_eager_chunking(model: nn.Module, compile_config: GraphTrainerCompileConfig)` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L363) — Wrap selected module forwards so tracing observes eager chunking. — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- <a id="populate_eager_chunk_metadata_pass"></a>`populate_eager_chunk_metadata_pass(gm: torch.fx.GraphModule, example_inputs: tuple[Any, ...] | None = None)` — [`L403`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_eager_chunk.py#L403) — Promote eager traceback chunk annotations into pass metadata.

