---
title: 'Module: torchtitan/experiments/graph_trainer/common_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/common_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.common_utils`/
symbols:
  _MODULE_FQN: _MODULE_FQN.
  apply_simple_fsdp: apply_simple_fsdp().
  _is_backward_node: _is_backward_node().
  _get_layer_id: _get_layer_id().
  annotate_moe_ep_regions: annotate_moe_ep_regions().
  annotate_module_fqns: annotate_module_fqns().
  _EP_TOKEN_EXCHANGE: _EP_TOKEN_EXCHANGE.
  PARAMETER_GRADIENT_FQNS_META: PARAMETER_GRADIENT_FQNS_META.
  maybe_register_blockmask_pytree_node: maybe_register_blockmask_pytree_node().
  _get_module_fqn: _get_module_fqn().
  _NOT_IN_LAYERS: _NOT_IN_LAYERS.
  compute_parameter_gradients: compute_parameter_gradients().
  compute_annotated_loss: compute_annotated_loss().
  build_decoder_config_for_backend: build_decoder_config_for_backend().
  accumulate_param_grads_: accumulate_param_grads_().
  ensure_boxed_graph_module: ensure_boxed_graph_module().
  _maybe_materialize_grad_for_param_layout: _maybe_materialize_grad_for_param_layout().
  GraphTrainerScaledDotProductInnerAttention.Config: GraphTrainerScaledDotProductInnerAttention#Config#
  _EP_TOKEN_COUNT_SYNC: _EP_TOKEN_COUNT_SYNC.
  matches_module_fqn_pattern: matches_module_fqn_pattern().
  set_graph_module_boxed_codegen: set_graph_module_boxed_codegen().
  _EP_TOKEN_EXCHANGE_WAIT: _EP_TOKEN_EXCHANGE_WAIT.
  log_timer: log_timer().
  get_transformer_block_buckets: get_transformer_block_buckets().
  get_transformer_block_buckets.convert_modules_to_fqns: get_transformer_block_buckets().convert_modules_to_fqns().
  BOXED_CODEGEN_META: BOXED_CODEGEN_META.
  get_default_transformer_block_buckets: get_default_transformer_block_buckets().
  GraphTrainerScaledDotProductInnerAttention: GraphTrainerScaledDotProductInnerAttention#
  AnnotatedLossFn.AnnotatedLossFn: AnnotatedLossFn.AnnotatedLossFn.
  _EP_TOKEN_COUNT_EXCHANGE: _EP_TOKEN_COUNT_EXCHANGE.
  _MOE_EP_REGIONS_ANNOTATED: _MOE_EP_REGIONS_ANNOTATED.
  GraphTrainerScaledDotProductInnerAttention.forward: GraphTrainerScaledDotProductInnerAttention#forward().
  parallelize_inputs: parallelize_inputs().
  _get_graph_modules: _get_graph_modules().
  _local_stride: _local_stride().
  parallelize_inputs.to_dtensor: parallelize_inputs().to_dtensor().
  register_blockmask_pytree_node: register_blockmask_pytree_node().
  LossResult.LossResult: LossResult.LossResult.
  end_with_pass: end_with_pass().
---
# Module: [`torchtitan/experiments/graph_trainer/common_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py)

## Classes
### <a id="GraphTrainerScaledDotProductInnerAttention"></a>`GraphTrainerScaledDotProductInnerAttention`  ·  implements/extends ScaledDotProductInnerAttention
- def: [`torchtitan/experiments/graph_trainer/common_utils.py:54`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L54) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- doc: Adapt flat graph-trainer attention inputs to the batched SDPA interface.
- signature: `class GraphTrainerScaledDotProductInnerAttention(ScaledDotProductInnerAttention):`
- members:
  - <a id="GraphTrainerScaledDotProductInnerAttention.forward"></a>`forward(self, q_THK: torch.Tensor, k_THK: torch.Tensor, v_THV: torch.Tensor, **kwargs)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L61)
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`forward`](../../models/common/attention.md#ScaledDotProductInnerAttention.forward)
- used by: [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`forward`](../../models/common/attention.md#ScaledDotProductInnerAttention.forward), [`build_decoder_config_for_backend`](common_utils.md#build_decoder_config_for_backend)

### <a id="GraphTrainerScaledDotProductInnerAttention.Config"></a>`GraphTrainerScaledDotProductInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/common_utils.py:58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L58)
- signature: `class Config(ScaledDotProductInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../models/common/attention.md#ScaledDotProductInnerAttention), [`Config`](../../models/common/attention.md#ScaledDotProductInnerAttention.Config)
- used by: [`build_decoder_config_for_backend`](common_utils.md#build_decoder_config_for_backend)

## Functions
- <a id="_get_graph_modules"></a>`_get_graph_modules(gm: torch.fx.GraphModule, *, recurse: bool, apply_to_root: bool)` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L38)
- <a id="_get_layer_id"></a>`_get_layer_id(node: torch.fx.Node)` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L294) — Extract the layer index from the node's module_fqn metadata. — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)
- <a id="_get_module_fqn"></a>`_get_module_fqn(node: torch.fx.Node)` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L290)
- <a id="_is_backward_node"></a>`_is_backward_node(node: torch.fx.Node)` — [`L286`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L286) — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)
- <a id="_local_stride"></a>`_local_stride(tensor: torch.Tensor)` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L118)
- <a id="_maybe_materialize_grad_for_param_layout"></a>`_maybe_materialize_grad_for_param_layout(param: torch.Tensor, grad: torch.Tensor)` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L124) — Match eager autograd's ``param.grad`` layout contract after graph replay.
- <a id="accumulate_param_grads_"></a>`accumulate_param_grads_(params: Iterable[torch.Tensor], grads: Iterable[torch.Tensor | None], *, clone_grads_to_initialize_param_grad: bool = False)` — [`L262`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L262) — Accumulate explicit graph-produced gradients into live parameters.
- <a id="annotate_module_fqns"></a>`annotate_module_fqns(model: nn.Module)` — [`L310`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L310) — Annotate all modules' forward with their fully-qualified names.
- <a id="annotate_moe_ep_regions"></a>`annotate_moe_ep_regions()` — [`L337`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L337) — Annotate MoE EP compute, dispatch, and combine regions for FX passes.
- <a id="apply_simple_fsdp"></a>`apply_simple_fsdp(model: nn.Module, *, parallel_dims: ParallelDims, training: TrainingConfig)` — [`L503`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L503) — Wrap the model (and any MoE experts) with graph_trainer's simple_fsdp.
- <a id="build_decoder_config_for_backend"></a>`build_decoder_config_for_backend(config_builder: Callable, attn_backend: str, **builder_kwargs)` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L85) — Build a Decoder model config for ``attn_backend``, allowing test-only SDPA.
- <a id="compute_annotated_loss"></a>`compute_annotated_loss(loss_fn: AnnotatedLossFn, pred: torch.Tensor, labels: torch.Tensor, loss_kwargs: dict[str, Any] | None = None)` — [`L242`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L242) — Compute the loss tensor with the same FX metadata convention as GraphTrainer.
- <a id="compute_parameter_gradients"></a>`compute_parameter_gradients(loss: torch.Tensor, named_parameters: Iterable[tuple[str, torch.Tensor]])` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L192) — Compute and identify parameter gradients in the traced graph.
- <a id="get_transformer_block_buckets.convert_modules_to_fqns"></a>`convert_modules_to_fqns(modules, module_to_fqn_mapping)` — [`L486`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L486) — Convert a (possibly nested) list of modules to FQN strings.
- <a id="end_with_pass"></a>`end_with_pass(passes: list[Callable], names: list[str])` — [`L423`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L423)
- <a id="ensure_boxed_graph_module"></a>`ensure_boxed_graph_module(gm: torch.fx.GraphModule)` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L168) — Use boxed FX codegen for runtime-owned graph modules.
- <a id="get_default_transformer_block_buckets"></a>`get_default_transformer_block_buckets(n_layers: int, *, chunked_loss_enabled: bool = False, moe_layer_ids: frozenset[int] = frozenset(), split_moe_expert_buckets: bool = False)` — [`L431`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L431) — Get default transformer block buckets for manual bucketing passes.
- <a id="get_transformer_block_buckets"></a>`get_transformer_block_buckets(model)` — [`L472`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L472) — Get transformer block buckets for manual bucketing passes.
- <a id="log_timer"></a>`log_timer(label: str)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L78)
- <a id="matches_module_fqn_pattern"></a>`matches_module_fqn_pattern(pattern: str, fqn: str)` — [`L324`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L324) — Match one module FQN against a component-wise fnmatch pattern.
- <a id="maybe_register_blockmask_pytree_node"></a>`maybe_register_blockmask_pytree_node()` — [`L413`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L413) — Register flex-attention pytree helpers if they are missing.
- <a id="parallelize_inputs"></a>`parallelize_inputs(parallel_dims, args, kwargs)` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L377)
- <a id="register_blockmask_pytree_node"></a>`register_blockmask_pytree_node()` — [`L400`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L400)
- <a id="set_graph_module_boxed_codegen"></a>`set_graph_module_boxed_codegen(gm: torch.fx.GraphModule, *, boxed: bool)` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L142) — Set the FX calling convention and record it in graph metadata.
- <a id="parallelize_inputs.to_dtensor"></a>`to_dtensor(tensor)` — [`L381`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L381)

## Module values
- <a id="AnnotatedLossFn.AnnotatedLossFn"></a>`AnnotatedLossFn` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L35)
- <a id="BOXED_CODEGEN_META"></a>`BOXED_CODEGEN_META` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L33)
- <a id="LossResult.LossResult"></a>`LossResult` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L34)
- <a id="PARAMETER_GRADIENT_FQNS_META"></a>`PARAMETER_GRADIENT_FQNS_META` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L184)
- <a id="_EP_TOKEN_COUNT_EXCHANGE"></a>`_EP_TOKEN_COUNT_EXCHANGE` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L185)
- <a id="_EP_TOKEN_COUNT_SYNC"></a>`_EP_TOKEN_COUNT_SYNC` — [`L186`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L186)
- <a id="_EP_TOKEN_EXCHANGE"></a>`_EP_TOKEN_EXCHANGE` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L187)
- <a id="_EP_TOKEN_EXCHANGE_WAIT"></a>`_EP_TOKEN_EXCHANGE_WAIT` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L188)
- <a id="_MODULE_FQN"></a>`_MODULE_FQN` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L181) — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)
- <a id="_MOE_EP_REGIONS_ANNOTATED"></a>`_MOE_EP_REGIONS_ANNOTATED` — [`L334`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L334)
- <a id="_NOT_IN_LAYERS"></a>`_NOT_IN_LAYERS` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/common_utils.py#L189)

