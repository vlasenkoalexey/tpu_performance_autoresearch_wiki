---
title: 'Module: src/torch_tpu/_internal/optimizers/single_trace_trainer.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/optimizers/single_trace_trainer.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.optimizers.single_trace_trainer`/
symbols:
  SingleTraceTrainer.make_compiled_train_step: SingleTraceTrainer#make_compiled_train_step().
  SingleTraceTrainer.train_step: SingleTraceTrainer#train_step().
  SingleTraceTrainer._param_group: SingleTraceTrainer#_param_group.
  SingleTraceTrainer._buffers: SingleTraceTrainer#_buffers.
  SingleTraceTrainer._update: SingleTraceTrainer#_update().
  SingleTraceTrainer.bound_loss: SingleTraceTrainer#bound_loss().
  SingleTraceTrainer._unwrap_sparse: SingleTraceTrainer#_unwrap_sparse().
  SingleTraceTrainer.flattened_stateless_train_step: SingleTraceTrainer#flattened_stateless_train_step().
  SingleTraceTrainer._key_map: SingleTraceTrainer#_key_map.
  SingleTraceTrainer._bufs: SingleTraceTrainer#_bufs().
  SingleTraceTrainer._optimizer: SingleTraceTrainer#_optimizer.
  _SparseGradPlaceholder: _SparseGradPlaceholder#
  SingleTraceTrainer.params: SingleTraceTrainer#params().
  SingleTraceTrainer._model: SingleTraceTrainer#_model.
  _sparse_grad_placeholder_unflatten: _sparse_grad_placeholder_unflatten().
  _decomp_embedding_backward: _decomp_embedding_backward().
  _decomp_embedding_bag_backward: _decomp_embedding_bag_backward().
  SingleTraceTrainer._wrap_sparse: SingleTraceTrainer#_wrap_sparse().
  _decomp_embedding_sparse_backward: _decomp_embedding_sparse_backward().
  Optimizer: Optimizer.
  ReferenceAdamW: ReferenceAdamW.
  AdamW: AdamW.
  ReferenceSgd: ReferenceSgd.
  Sgd: Sgd.
  ReferenceMuon: ReferenceMuon.
  Muon: Muon.
  SingleTraceTrainer.param_group: SingleTraceTrainer#param_group().
  _declare_tracing_to_transformers: _declare_tracing_to_transformers().
  _compute_loss: _compute_loss().
  _invoke_compile_fn: _invoke_compile_fn().
  _SparseGradPlaceholder.indices: _SparseGradPlaceholder#indices.
  _SparseGradPlaceholder.values: _SparseGradPlaceholder#values.
  _SparseGradPlaceholder.size: _SparseGradPlaceholder#size.
  SingleTraceTrainer._compile_fn: SingleTraceTrainer#_compile_fn.
  SingleTraceTrainer._compute_loss_fn: SingleTraceTrainer#_compute_loss_fn.
  __all__: __all__.
  SingleTraceTrainer: SingleTraceTrainer#
  SingleTraceTrainer.__init__: SingleTraceTrainer#__init__().
---
# Module: [`src/torch_tpu/_internal/optimizers/single_trace_trainer.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py)

## Classes
### <a id="SingleTraceTrainer"></a>`SingleTraceTrainer`
- def: [`src/torch_tpu/_internal/optimizers/single_trace_trainer.py:265`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L265)
- doc: Facilitates compiled train steps with a single offload containing the optimizer step.
- signature: `class SingleTraceTrainer:`
- members:
  - <a id="SingleTraceTrainer.__init__"></a>`__init__(self, model: torch.nn.Module, optimizer: Any = None, compile_fn: Callable[..., Any] | None = None, compute_loss_fn: Callable[..., torch.Tensor] | None = None)` — [`L277`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L277) — Initializes the SingleTraceTrainer.
  - <a id="SingleTraceTrainer._bufs"></a>`_bufs(self)` — [`L366`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L366) — Returns buffers with their original names. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="SingleTraceTrainer.bound_loss"></a>`bound_loss(target, bufs_arg)` — [`L408`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L408) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="SingleTraceTrainer.flattened_stateless_train_step"></a>`flattened_stateless_train_step(*flat_args)` — [`L399`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L399) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="SingleTraceTrainer.make_compiled_train_step"></a>`make_compiled_train_step(self, example_inputs: Any, example_targets: Any = None, compile_fn: Callable[..., Any] | None = None)` — [`L374`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L374) — Returns a callable for the training step with the model compiled. — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
  - <a id="SingleTraceTrainer.param_group"></a>`param_group(self)` — [`L344`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L344) — Returns the parameters and optimizer state that the train step updates.
  - <a id="SingleTraceTrainer.params"></a>`params(self)` — [`L356`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L356) — Returns parameters with their original names.
  - <a id="SingleTraceTrainer.train_step"></a>`train_step(inputs: Any, targets: Any = None)` — [`L515`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L515) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- protocol/private: <a id="SingleTraceTrainer._buffers"></a>`_buffers`[`L316`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L316), <a id="SingleTraceTrainer._compile_fn"></a>`_compile_fn`[`L299`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L299), <a id="SingleTraceTrainer._compute_loss_fn"></a>`_compute_loss_fn`[`L300`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L300), <a id="SingleTraceTrainer._key_map"></a>`_key_map`[`L309`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L309), <a id="SingleTraceTrainer._model"></a>`_model`[`L297`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L297), <a id="SingleTraceTrainer._optimizer"></a>`_optimizer`[`L298`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L298), <a id="SingleTraceTrainer._param_group"></a>`_param_group`[`L323`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L323), <a id="SingleTraceTrainer._unwrap_sparse"></a>`_unwrap_sparse`[`L539`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L539), <a id="SingleTraceTrainer._update"></a>`_update`[`L335`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L335), <a id="SingleTraceTrainer._wrap_sparse"></a>`_wrap_sparse`[`L435`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L435)
- uses (calls/refs, reference-scoped): [`_SparseGradPlaceholder`](single_trace_trainer.md#_SparseGradPlaceholder), [`_decomp_embedding_backward`](single_trace_trainer.md#_decomp_embedding_backward), [`_decomp_embedding_bag_backward`](single_trace_trainer.md#_decomp_embedding_bag_backward), [`_decomp_embedding_sparse_backward`](single_trace_trainer.md#_decomp_embedding_sparse_backward), [`_compute_loss`](single_trace_trainer.md#_compute_loss), [`_declare_tracing_to_transformers`](single_trace_trainer.md#_declare_tracing_to_transformers), [`_invoke_compile_fn`](single_trace_trainer.md#_invoke_compile_fn), [`indices`](single_trace_trainer.md#_SparseGradPlaceholder.indices), [`size`](single_trace_trainer.md#_SparseGradPlaceholder.size), [`values`](single_trace_trainer.md#_SparseGradPlaceholder.values)

### <a id="_SparseGradPlaceholder"></a>`_SparseGradPlaceholder`
- def: [`src/torch_tpu/_internal/optimizers/single_trace_trainer.py:171`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L171) — documented in [python-optimizers](../../../../../concepts/python-optimizers.md)
- signature: `class _SparseGradPlaceholder:`
- members:
  - <a id="_SparseGradPlaceholder.indices"></a>`indices` — [`L172`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L172)
  - <a id="_SparseGradPlaceholder.size"></a>`size` — [`L174`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L174)
  - <a id="_SparseGradPlaceholder.values"></a>`values` — [`L173`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L173)
- used by: [`train_step`](single_trace_trainer.md#SingleTraceTrainer.train_step), [`_unwrap_sparse`](single_trace_trainer.md#SingleTraceTrainer._unwrap_sparse), [`_sparse_grad_placeholder_unflatten`](single_trace_trainer.md#_sparse_grad_placeholder_unflatten), [`_wrap_sparse`](single_trace_trainer.md#SingleTraceTrainer._wrap_sparse)

## Functions
- <a id="_compute_loss"></a>`_compute_loss(model: torch.nn.Module, key_map: dict[str, str], params: dict[str, torch.Tensor], buffers: dict[str, torch.Tensor], inputs: Any, targets: Any, compute_loss_fn: Callable[..., torch.Tensor] | None = None)` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L76) — Computes loss for functional execution.
- <a id="_declare_tracing_to_transformers"></a>`_declare_tracing_to_transformers()` — [`L50`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L50) — Makes Hugging Face mask creation take its trace-safe path under make_fx.
- <a id="_decomp_embedding_backward"></a>`_decomp_embedding_backward(grad: torch.Tensor, indices: torch.Tensor, num_weights: int, padding_idx: int, scale_grad_by_freq: bool, sparse: bool)` — [`L211`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L211)
- <a id="_decomp_embedding_bag_backward"></a>`_decomp_embedding_bag_backward(grad: torch.Tensor, indices: torch.Tensor, offsets: torch.Tensor, offset2bag: torch.Tensor, bag_size: torch.Tensor, max_indices: torch.Tensor, num_weights: int, scale_grad_by_freq: bool, mode: int, sparse: bool, per_sample_weights: torch.Tensor | None, padding_idx: int = -1)` — [`L228`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L228)
- <a id="_decomp_embedding_sparse_backward"></a>`_decomp_embedding_sparse_backward(grad: torch.Tensor, indices: torch.Tensor, num_weights: int, padding_idx: int, scale_grad_by_freq: bool)` — [`L189`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L189)
- <a id="_invoke_compile_fn"></a>`_invoke_compile_fn(compile_fn: Callable[..., Any], graph_module: torch.fx.GraphModule, flat_inputs: Sequence[Any])` — [`L139`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L139) — Invokes compile_fn with either (graph_module, flat_inputs) or (graph_module).
- <a id="_sparse_grad_placeholder_unflatten"></a>`_sparse_grad_placeholder_unflatten(children: Any, size: Any)` — [`L177`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L177)

## Module values
- <a id="AdamW"></a>`AdamW` — [`L42`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L42)
- <a id="Muon"></a>`Muon` — [`L46`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L46)
- <a id="Optimizer"></a>`Optimizer` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L40)
- <a id="ReferenceAdamW"></a>`ReferenceAdamW` — [`L41`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L41)
- <a id="ReferenceMuon"></a>`ReferenceMuon` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L45)
- <a id="ReferenceSgd"></a>`ReferenceSgd` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L43)
- <a id="Sgd"></a>`Sgd` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L44)
- <a id="__all__"></a>`__all__` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/optimizers/single_trace_trainer.py#L35)

