---
title: 'Module: torchtitan/distributed/cudagraph.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/cudagraph.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.cudagraph`/
symbols:
  CUDAGraphWrapper.__call__: CUDAGraphWrapper#__call__().
  wrap_with_cuda_graph: wrap_with_cuda_graph().
  _CUDAGraphManager.teardown: _CUDAGraphManager#teardown().
  cudagraph_teardown: cudagraph_teardown().
  CUDAGraphInputSpec.unflatten: CUDAGraphInputSpec#unflatten().
  CUDAGraphWrapper.teardown: CUDAGraphWrapper#teardown().
  _manager: _manager.
  CUDAGraphInputSpec.flatten: CUDAGraphInputSpec#flatten().
  CUDAGraphWrapper: CUDAGraphWrapper#
  CUDAGraphInputSpec._num_flat_leaves: CUDAGraphInputSpec#_num_flat_leaves.
  _CUDAGraphManager.maybe_initialize: _CUDAGraphManager#maybe_initialize().
  wrap_with_cuda_graph.run: wrap_with_cuda_graph().run().
  CUDAGraphWrapper._static_input_addresses: CUDAGraphWrapper#_static_input_addresses.
  get_cudagraph_annotations: get_cudagraph_annotations().
  CUDAGraphWrapper._static_input_indices: CUDAGraphWrapper#_static_input_indices.
  CUDAGraphWrapper._validate_inputs: CUDAGraphWrapper#_validate_inputs().
  CUDAGraphInputSpec._leaf_specs: CUDAGraphInputSpec#_leaf_specs.
  CUDAGraphWrapper._input_indices_to_copy: CUDAGraphWrapper#_input_indices_to_copy.
  _CUDAGraphManager.stream: _CUDAGraphManager#stream().
  _CUDAGraphManager.register: _CUDAGraphManager#register().
  CUDAGraphWrapper._graph: CUDAGraphWrapper#_graph.
  CUDAGraphWrapper._record_static_input_addresses: CUDAGraphWrapper#_record_static_input_addresses().
  _CUDAGraphManager._wrappers: _CUDAGraphManager#_wrappers.
  _CUDAGraphManager._initialized: _CUDAGraphManager#_initialized.
  _CUDAGraphManager._graph_pool: _CUDAGraphManager#_graph_pool.
  _CUDAGraphManager._stream: _CUDAGraphManager#_stream.
  CUDAGraphWrapper._args: CUDAGraphWrapper#_args.
  _CUDAGraphManager.graph_pool: _CUDAGraphManager#graph_pool().
  CUDAGraphWrapper._check_static_input_addresses: CUDAGraphWrapper#_check_static_input_addresses().
  wrap_with_cuda_graph.run.flat_fn: wrap_with_cuda_graph().run().flat_fn().
  CUDAGraphWrapper._num_inputs: CUDAGraphWrapper#_num_inputs.
  CUDAGraphWrapper._output: CUDAGraphWrapper#_output.
  _BlockMaskInputSpec: _BlockMaskInputSpec#
  _BlockMaskInputSpec.num_leaves: _BlockMaskInputSpec#num_leaves.
  _BlockMaskInputSpec.context: _BlockMaskInputSpec#context.
  CUDAGraphInputSpec: CUDAGraphInputSpec#
  CUDAGraphInputSpec._tree_spec: CUDAGraphInputSpec#_tree_spec.
  _CUDAGraphManager._dummy_graph: _CUDAGraphManager#_dummy_graph.
  _CUDAGraphManager.all_annotations: _CUDAGraphManager#all_annotations.
  CUDAGraphWrapper._fn: CUDAGraphWrapper#_fn.
  CUDAGraphWrapper._non_tensor_inputs: CUDAGraphWrapper#_non_tensor_inputs.
  CUDAGraphWrapper._warmup_remaining: CUDAGraphWrapper#_warmup_remaining.
  _CUDAGraphManager: _CUDAGraphManager#
  CUDAGraphWrapper._tensor_metadata: CUDAGraphWrapper#_tensor_metadata.
  CUDAGraphWrapper._should_check_address: CUDAGraphWrapper#_should_check_address.
  ForwardBackwardFn: ForwardBackwardFn.
  CUDAGraphInputSpec.__init__: CUDAGraphInputSpec#__init__().
  _CUDAGraphManager.__init__: _CUDAGraphManager#__init__().
  CUDAGraphWrapper.__init__: CUDAGraphWrapper#__init__().
---
# Module: [`torchtitan/distributed/cudagraph.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py)

## Classes
### <a id="CUDAGraphInputSpec"></a>`CUDAGraphInputSpec`
- def: [`torchtitan/distributed/cudagraph.py:37`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L37)
- doc: Flatten structured inputs while exposing tensors stored in `BlockMask`.
- signature: `class CUDAGraphInputSpec:`
- members:
  - <a id="CUDAGraphInputSpec.flatten"></a>`flatten(self, tree: Any)` — [`L58`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L58)
  - <a id="CUDAGraphInputSpec.unflatten"></a>`unflatten(self, flat_leaves: Sequence[Any])` — [`L98`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L98)
- protocol/private: <a id="CUDAGraphInputSpec.__init__"></a>`__init__`[`L40`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L40), <a id="CUDAGraphInputSpec._leaf_specs"></a>`_leaf_specs`[`L45`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L45), <a id="CUDAGraphInputSpec._num_flat_leaves"></a>`_num_flat_leaves`[`L46`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L46), <a id="CUDAGraphInputSpec._tree_spec"></a>`_tree_spec`[`L41`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L41)
- uses (calls/refs, reference-scoped): [`_BlockMaskInputSpec`](cudagraph.md#_BlockMaskInputSpec), [`context`](cudagraph.md#_BlockMaskInputSpec.context), [`num_leaves`](cudagraph.md#_BlockMaskInputSpec.num_leaves)
- used by: [`wrap_with_cuda_graph`](cudagraph.md#wrap_with_cuda_graph), [`run`](cudagraph.md#wrap_with_cuda_graph.run), [`flat_fn`](cudagraph.md#wrap_with_cuda_graph.run.flat_fn)

### <a id="CUDAGraphWrapper"></a>`CUDAGraphWrapper`
- def: [`torchtitan/distributed/cudagraph.py:193`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L193)
- members:
  - <a id="CUDAGraphWrapper.teardown"></a>`teardown(self)` — [`L349`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L349)
- protocol/private: <a id="CUDAGraphWrapper.__call__"></a>`__call__`[`L312`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L312), <a id="CUDAGraphWrapper.__init__"></a>`__init__`[`L212`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L212), <a id="CUDAGraphWrapper._args"></a>`_args`[`L258`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L258), <a id="CUDAGraphWrapper._check_static_input_addresses"></a>`_check_static_input_addresses`[`L272`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L272), <a id="CUDAGraphWrapper._fn"></a>`_fn`[`L224`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L224), <a id="CUDAGraphWrapper._graph"></a>`_graph`[`L256`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L256), <a id="CUDAGraphWrapper._input_indices_to_copy"></a>`_input_indices_to_copy`[`L237`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L237), <a id="CUDAGraphWrapper._non_tensor_inputs"></a>`_non_tensor_inputs`[`L251`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L251), <a id="CUDAGraphWrapper._num_inputs"></a>`_num_inputs`[`L225`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L225), <a id="CUDAGraphWrapper._output"></a>`_output`[`L259`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L259), <a id="CUDAGraphWrapper._record_static_input_addresses"></a>`_record_static_input_addresses`[`L266`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L266), <a id="CUDAGraphWrapper._should_check_address"></a>`_should_check_address`[`L260`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L260), <a id="CUDAGraphWrapper._static_input_addresses"></a>`_static_input_addresses`[`L261`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L261), <a id="CUDAGraphWrapper._static_input_indices"></a>`_static_input_indices`[`L226`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L226), <a id="CUDAGraphWrapper._tensor_metadata"></a>`_tensor_metadata`[`L246`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L246), <a id="CUDAGraphWrapper._validate_inputs"></a>`_validate_inputs`[`L284`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L284), <a id="CUDAGraphWrapper._warmup_remaining"></a>`_warmup_remaining`[`L257`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L257)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`_manager`](cudagraph.md#_manager), [`maybe_initialize`](cudagraph.md#_CUDAGraphManager.maybe_initialize), [`stream`](cudagraph.md#_CUDAGraphManager.stream), [`register`](cudagraph.md#_CUDAGraphManager.register), [`graph_pool`](cudagraph.md#_CUDAGraphManager.graph_pool), [`all_annotations`](cudagraph.md#_CUDAGraphManager.all_annotations)
- used by: [`_make_fx_forward_backward_step`](../experiments/graph_trainer/trainer.md#GraphTrainer._make_fx_forward_backward_step), [`cudagraph_pass`](../experiments/graph_trainer/cudagraph.md#cudagraph_pass), [`wrap_with_cuda_graph`](cudagraph.md#wrap_with_cuda_graph), [`teardown`](cudagraph.md#_CUDAGraphManager.teardown), [`run`](cudagraph.md#wrap_with_cuda_graph.run), [`register`](cudagraph.md#_CUDAGraphManager.register), [`_wrappers`](cudagraph.md#_CUDAGraphManager._wrappers)  (3 test-only)

### <a id="_BlockMaskInputSpec"></a>`_BlockMaskInputSpec`
- def: [`torchtitan/distributed/cudagraph.py:30`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L30)
- signature: `class _BlockMaskInputSpec:`
- members:
  - <a id="_BlockMaskInputSpec.context"></a>`context` — [`L32`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L32)
  - <a id="_BlockMaskInputSpec.num_leaves"></a>`num_leaves` — [`L31`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L31)
- used by: [`unflatten`](cudagraph.md#CUDAGraphInputSpec.unflatten), [`flatten`](cudagraph.md#CUDAGraphInputSpec.flatten), [`_num_flat_leaves`](cudagraph.md#CUDAGraphInputSpec._num_flat_leaves), [`_leaf_specs`](cudagraph.md#CUDAGraphInputSpec._leaf_specs)

### <a id="_CUDAGraphManager"></a>`_CUDAGraphManager`
- def: [`torchtitan/distributed/cudagraph.py:123`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L123)
- doc: Singleton that owns a shared graph pool, stream, and annotations.
- signature: `class _CUDAGraphManager:`
- members:
  - <a id="_CUDAGraphManager.graph_pool"></a>`graph_pool(self)` — [`L135`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L135)
  - <a id="_CUDAGraphManager.maybe_initialize"></a>`maybe_initialize(self)` — [`L144`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L144)
  - <a id="_CUDAGraphManager.register"></a>`register(self, wrapper: CUDAGraphWrapper)` — [`L165`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L165)
  - <a id="_CUDAGraphManager.stream"></a>`stream(self)` — [`L140`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L140)
  - <a id="_CUDAGraphManager.teardown"></a>`teardown(self)` — [`L168`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L168)
  - <a id="_CUDAGraphManager.all_annotations"></a>`all_annotations` — [`L132`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L132)
- protocol/private: <a id="_CUDAGraphManager.__init__"></a>`__init__`[`L126`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L126), <a id="_CUDAGraphManager._dummy_graph"></a>`_dummy_graph`[`L131`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L131), <a id="_CUDAGraphManager._graph_pool"></a>`_graph_pool`[`L129`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L129), <a id="_CUDAGraphManager._initialized"></a>`_initialized`[`L127`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L127), <a id="_CUDAGraphManager._stream"></a>`_stream`[`L130`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L130), <a id="_CUDAGraphManager._wrappers"></a>`_wrappers`[`L128`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L128)
- uses (calls/refs, reference-scoped): [`teardown`](cudagraph.md#CUDAGraphWrapper.teardown), [`CUDAGraphWrapper`](cudagraph.md#CUDAGraphWrapper)
- used by: [`__call__`](cudagraph.md#CUDAGraphWrapper.__call__), [`cudagraph_teardown`](cudagraph.md#cudagraph_teardown), [`_manager`](cudagraph.md#_manager), [`_static_input_addresses`](cudagraph.md#CUDAGraphWrapper._static_input_addresses), [`get_cudagraph_annotations`](cudagraph.md#get_cudagraph_annotations)

## Functions
- <a id="cudagraph_teardown"></a>`cudagraph_teardown()` — [`L183`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L183) — Destroy all CUDA graphs and release the shared memory pool.
- <a id="wrap_with_cuda_graph.run.flat_fn"></a>`flat_fn(*flat_inputs: Any)` — [`L417`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L417)
- <a id="get_cudagraph_annotations"></a>`get_cudagraph_annotations()` — [`L188`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L188) — Return all kernel annotations accumulated across CUDA graph captures.
- <a id="wrap_with_cuda_graph.run"></a>`run(*args: Any, **kwargs: Any)` — [`L411`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L411)
- <a id="wrap_with_cuda_graph"></a>`wrap_with_cuda_graph(fn: Callable[..., torch.Tensor], *, gradient_accumulation_steps: int, sdc_num_steps: int, sdc_num_replays: int, num_warmup_steps: int = 2)` — [`L358`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L358) — Decorate a structured callable with CUDA graph capture and replay.

## Module values
- <a id="ForwardBackwardFn"></a>`ForwardBackwardFn` — [`L23`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L23)
- <a id="_manager"></a>`_manager` — [`L180`](../../../../../../raw/code/torchtitan/torchtitan/distributed/cudagraph.py#L180)

