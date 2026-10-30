---
title: 'Module: src/torch_tpu/_internal/pallas/pallas.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/pallas/pallas.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.pallas.pallas`/
symbols:
  JaxCallable.__call__: JaxCallable#__call__().
  jax_op.dec: jax_op().dec().
  JaxCallable.kernel_key_to_mlir_fingerprint: JaxCallable#kernel_key_to_mlir_fingerprint.
  JaxCallable._get_jax_placeholders: JaxCallable#_get_jax_placeholders().
  JaxCallable._normalize_invocation_args: JaxCallable#_normalize_invocation_args().
  _to_hashable_jax_static_arg: _to_hashable_jax_static_arg().
  JaxCallable._orig_params_by_name: JaxCallable#_orig_params_by_name.
  _strip_optional: _strip_optional().
  _get_torch_signature: _get_torch_signature().
  JaxCallable._orig_params: JaxCallable#_orig_params.
  jax_op.dec.fake_fn: jax_op().dec().fake_fn().
  _map_jax_return_to_torch: _map_jax_return_to_torch().
  _map_jax_return_to_schema_str: _map_jax_return_to_schema_str().
  JaxCallable._static_param_names: JaxCallable#_static_param_names.
  _is_valid_argument_type: _is_valid_argument_type().
  _map_jax_param_to_torch: _map_jax_param_to_torch().
  jax_placeholder: jax_placeholder().
  _verify_signature.is_valid_result: _verify_signature().is_valid_result().
  _normalize_caller_arg: _normalize_caller_arg().
  JaxCallable.static_argnums: JaxCallable#static_argnums.
  JaxCallable._param_is_tensor: JaxCallable#_param_is_tensor.
  _is_tensor_annotation: _is_tensor_annotation().
  _get_pallas_mesh: _get_pallas_mesh().
  JaxCallable.__init__: JaxCallable#__init__().
  JaxCallable.__repr__: JaxCallable#__repr__().
  torch_placeholder: torch_placeholder().
  JaxCallable.mesh: JaxCallable#mesh.
  JaxCallable._add_tensor_arg: JaxCallable#_add_tensor_arg().
  custom_jax_kernel.decorator: custom_jax_kernel().decorator().
  _get_kernel_invocation_key.get_hash: _get_kernel_invocation_key().get_hash().
  custom_jax_kernel: custom_jax_kernel().
  _get_enum_type: _get_enum_type().
  _get_sequence_element_type: _get_sequence_element_type().
  _verify_signature: _verify_signature().
  JaxCallable.name: JaxCallable#name.
  JaxCallable.input_output_aliases: JaxCallable#input_output_aliases.
  JAX_TO_TORCH_DTYPE_MAP: JAX_TO_TORCH_DTYPE_MAP.
  JaxCallable.unwrap_elem: JaxCallable#unwrap_elem().
  jax_placeholders: jax_placeholders().
  _get_kernel_invocation_key: _get_kernel_invocation_key().
  TORCH_TO_JAX_DTYPE_MAP: TORCH_TO_JAX_DTYPE_MAP.
  _unwrap_annotated: _unwrap_annotated().
  JaxCallable: JaxCallable#
  JaxCallable._orig_signature: JaxCallable#_orig_signature.
  get_global_shape: get_global_shape().
  get_local_shape: get_local_shape().
  _is_valid_base_type: _is_valid_base_type().
  _is_valid_sequence_element_type: _is_valid_sequence_element_type().
  _is_valid_argument: _is_valid_argument().
  _infer_static_argnums: _infer_static_argnums().
  _infer_static_argnames: _infer_static_argnames().
  _generate_torch_schema: _generate_torch_schema().
  JaxCallable._param_name_to_idx: JaxCallable#_param_name_to_idx.
  JaxCallable._donate_argnums_set: JaxCallable#_donate_argnums_set.
  JaxCallable._validate_args: JaxCallable#_validate_args().
  get_pallas_mesh: get_pallas_mesh().
  get_default_pallas_mesh: get_default_pallas_mesh().
  ex: ex.
  JaxCallable.trace_key: JaxCallable#trace_key.
  JaxCallable.donate_argnums: JaxCallable#donate_argnums.
  JaxCallable.exported: JaxCallable#exported.
  _validate_pallas_mesh_world_size: _validate_pallas_mesh_world_size().
  jax_op: jax_op().
  _JaxCustomOpDef.__call__: _JaxCustomOpDef#__call__().
  _convert_shape: _convert_shape().
  _normalize_output_partition_specs: _normalize_output_partition_specs().
  _get_bound_names: _get_bound_names().
  _generate_torch_schema.dummy_fn: _generate_torch_schema().dummy_fn().
  JaxCallable.jit_fn: JaxCallable#jit_fn.
  JaxCallable.input_partition_specs: JaxCallable#input_partition_specs.
  JaxCallable.output_partition_specs: JaxCallable#output_partition_specs.
  JaxCallable.static_argnames: JaxCallable#static_argnames.
  JaxCallable.__signature__: JaxCallable#__signature__.
  JaxCallable.output_shapes: JaxCallable#output_shapes.
  _verify_signature.is_valid_return_base_type: _verify_signature().is_valid_return_base_type().
  _map_jax_base_to_torch: _map_jax_base_to_torch().
  _is_torch_supported_default: _is_torch_supported_default().
  _KernelResultT: _KernelResultT.
  _JaxCustomOpDef: _JaxCustomOpDef#
  JaxCallable.__globals__: JaxCallable#__globals__.
  JaxCallable.wrap: JaxCallable#wrap().
  __all__: __all__.
---
# Module: [`src/torch_tpu/_internal/pallas/pallas.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py)

## Classes
### <a id="JaxCallable"></a>`JaxCallable`
- def: [`src/torch_tpu/_internal/pallas/pallas.py:930`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L930) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- doc: A torch callable function that wraps a JAX function.
- signature: `class JaxCallable:`
- members:
  - <a id="JaxCallable.__init__"></a>`__init__(self, name: str, jit_fn: Any, trace_key: str, mesh: jax.sharding.Mesh | None = None, input_partition_specs: tuple[tuple[str, ...], ...] | None = None, output_partition_specs: tuple[tuple[str, ...], ...] | None = None, static_argnums: tuple[int, ...] = (), donate_argnums: list[int] | None = None, input_output_aliases: dict[int, int] | None = None, static_argnames: tuple[str, ...] = ())` — [`L951`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L951) — Initializes a JaxCallable, a cached callable for custom kernels. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable._get_jax_placeholders"></a>`_get_jax_placeholders(self, norm_args: Sequence[Any], norm_kwargs: dict[str, Any] | None = None)` — [`L1164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1164) — Converts normalized args and kwargs into JAX placeholders for tracing. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable._normalize_invocation_args"></a>`_normalize_invocation_args(self, args: Sequence[Any], kwargs: dict[str, Any])` — [`L1100`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1100) — Binds arguments to signature and normalizes static arguments. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable._validate_args"></a>`_validate_args(self, *args)` — [`L1078`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1078) — Validates that the arguments are supported by the kernel. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.unwrap_elem"></a>`unwrap_elem(x)` — [`L1217`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1217) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.wrap"></a>`wrap(x)` — [`L1232`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1232)
  - <a id="JaxCallable.donate_argnums"></a>`donate_argnums` — [`L945`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L945)
  - <a id="JaxCallable.exported"></a>`exported` — [`L947`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L947) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.input_output_aliases"></a>`input_output_aliases` — [`L946`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L946) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.input_partition_specs"></a>`input_partition_specs` — [`L941`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L941)
  - <a id="JaxCallable.jit_fn"></a>`jit_fn` — [`L939`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L939)
  - <a id="JaxCallable.kernel_key_to_mlir_fingerprint"></a>`kernel_key_to_mlir_fingerprint` — [`L1006`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1006) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.mesh"></a>`mesh` — [`L940`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L940) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.name"></a>`name` — [`L937`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L937) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.output_partition_specs"></a>`output_partition_specs` — [`L942`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L942)
  - <a id="JaxCallable.output_shapes"></a>`output_shapes` — [`L998`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L998)
  - <a id="JaxCallable.static_argnames"></a>`static_argnames` — [`L944`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L944)
  - <a id="JaxCallable.static_argnums"></a>`static_argnums` — [`L943`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L943) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
  - <a id="JaxCallable.trace_key"></a>`trace_key` — [`L938`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L938) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- protocol/private: <a id="JaxCallable.__call__"></a>`__call__`[`L1198`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1198), <a id="JaxCallable.__globals__"></a>`__globals__`[`L949`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L949), <a id="JaxCallable.__repr__"></a>`__repr__`[`L1072`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1072), <a id="JaxCallable.__signature__"></a>`__signature__`[`L948`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L948), <a id="JaxCallable._add_tensor_arg"></a>`_add_tensor_arg`[`L1305`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1305), <a id="JaxCallable._donate_argnums_set"></a>`_donate_argnums_set`[`L1068`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1068), <a id="JaxCallable._orig_params"></a>`_orig_params`[`L1044`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1044), <a id="JaxCallable._orig_params_by_name"></a>`_orig_params_by_name`[`L1045`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1045), <a id="JaxCallable._orig_signature"></a>`_orig_signature`[`L1043`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1043), <a id="JaxCallable._param_is_tensor"></a>`_param_is_tensor`[`L1052`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1052), <a id="JaxCallable._param_name_to_idx"></a>`_param_name_to_idx`[`L1065`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1065), <a id="JaxCallable._static_param_names"></a>`_static_param_names`[`L1059`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1059)
- uses (calls/refs, reference-scoped): [`_to_hashable_jax_static_arg`](pallas.md#_to_hashable_jax_static_arg), [`_strip_optional`](pallas.md#_strip_optional), [`_get_torch_signature`](pallas.md#_get_torch_signature), [`_is_tensor_annotation`](pallas.md#_is_tensor_annotation), [`torch_placeholder`](pallas.md#torch_placeholder), [`_get_kernel_invocation_key`](pallas.md#_get_kernel_invocation_key), [`jax_placeholders`](pallas.md#jax_placeholders), [`_validate_pallas_mesh_world_size`](pallas.md#_validate_pallas_mesh_world_size), [`_get_bound_names`](pallas.md#_get_bound_names), [`_normalize_output_partition_specs`](pallas.md#_normalize_output_partition_specs), [`warn_deprecation_with_skip`](_compat.md#warn_deprecation_with_skip), [`_KernelResultT`](pallas.md#_KernelResultT)
- used by: [`dec`](pallas.md#jax_op.dec), [`fake_fn`](pallas.md#jax_op.dec.fake_fn), [`decorator`](pallas.md#custom_jax_kernel.decorator), [`custom_jax_kernel`](pallas.md#custom_jax_kernel)

### <a id="_JaxCustomOpDef"></a>`_JaxCustomOpDef`
- def: [`src/torch_tpu/_internal/pallas/pallas.py:918`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L918)
- doc: CustomOpDef subclass that normalizes caller arguments for Torch schema.
- signature: `class _JaxCustomOpDef(CustomOpDef):`
- protocol/private: <a id="_JaxCustomOpDef.__call__"></a>`__call__`[`L921`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L921)
- uses (calls/refs, reference-scoped): [`_normalize_caller_arg`](pallas.md#_normalize_caller_arg)
- used by: [`dec`](pallas.md#jax_op.dec)

## Functions
- <a id="_convert_shape"></a>`_convert_shape(shape, mesh, partition_spec, op)` — [`L125`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L125) — Converts a shape based on a mesh and partition specification.
- <a id="_generate_torch_schema"></a>`_generate_torch_schema(torch_signature: inspect.Signature, ret_schema_str: str, mutates_args: tuple[str, ...] = ())` — [`L897`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L897) — Generates an explicit PyTorch custom_op schema string. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_get_bound_names"></a>`_get_bound_names(fn: Any)` — [`L472`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L472) — Returns the set of parameter names bound by functools.partial.
- <a id="_get_enum_type"></a>`_get_enum_type(typ: Any)` — [`L359`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L359) — Returns the Enum subclass if typ is or contains an Enum in a Union. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_get_kernel_invocation_key"></a>`_get_kernel_invocation_key(trace_key: str, input_args: Sequence[torch.Tensor | Any], input_kwargs: dict[str, Any], static_argnums: tuple[int, ...] = ())` — [`L290`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L290) — Construct a unique ID for the kernel invocation. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_get_pallas_mesh"></a>`_get_pallas_mesh(axis_names: Sequence[str] | str, mesh_shape: Sequence[int] | None = None, process_group: dist.ProcessGroup | None = None)` — [`L1707`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1707) — Constructs a rank-aligned JAX Mesh using TPU runtime device metadata. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_get_sequence_element_type"></a>`_get_sequence_element_type(typ: Any)` — [`L374`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L374) — If typ is a homogeneous Sequence/list/tuple, returns its element type. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_get_torch_signature"></a>`_get_torch_signature(signature: inspect.Signature, bound_names: collections.abc.Set[str] = frozenset())` — [`L859`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L859) — Converts a JAX signature to a Torch signature for custom_op schema. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_infer_static_argnames"></a>`_infer_static_argnames(signature: inspect.Signature)` — [`L612`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L612) — Infers the static_argnames for keyword-only parameters of a JAX function. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_infer_static_argnums"></a>`_infer_static_argnums(signature: inspect.Signature)` — [`L591`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L591) — Infers the static_argnums for a JAX function. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_is_tensor_annotation"></a>`_is_tensor_annotation(annotation: Any)` — [`L579`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L579) — Returns True if the annotation represents a tensor or sequence of tensors. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_is_torch_supported_default"></a>`_is_torch_supported_default(val: Any)` — [`L790`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L790)
- <a id="_is_valid_argument"></a>`_is_valid_argument(param: inspect.Parameter, bound_names: collections.abc.Set[str] = frozenset())` — [`L488`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L488) — Returns True if the argument is valid for a wrapped JAX function. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_is_valid_argument_type"></a>`_is_valid_argument_type(annotation: Any)` — [`L461`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L461) — Returns True if the argument type is valid for a wrapped JAX function. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_is_valid_base_type"></a>`_is_valid_base_type(annotation: Any)` — [`L394`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L394) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_is_valid_sequence_element_type"></a>`_is_valid_sequence_element_type(elem_type: Any)` — [`L441`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L441) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_map_jax_base_to_torch"></a>`_map_jax_base_to_torch(typ: Any)` — [`L622`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L622)
- <a id="_map_jax_param_to_torch"></a>`_map_jax_param_to_torch(typ: Any)` — [`L696`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L696) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_map_jax_return_to_schema_str"></a>`_map_jax_return_to_schema_str(typ: Any)` — [`L749`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L749) — Converts a JAX return type annotation to a PyTorch C++ schema return string. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_map_jax_return_to_torch"></a>`_map_jax_return_to_torch(typ: Any)` — [`L710`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L710) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_normalize_caller_arg"></a>`_normalize_caller_arg(val: Any)` — [`L796`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L796) — Normalizes JAX values passed by caller into PyTorch custom_op types. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_normalize_output_partition_specs"></a>`_normalize_output_partition_specs(output_specs: Any, num_outputs: int)` — [`L274`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L274) — Normalizes output partition specs across output leaves.
- <a id="_strip_optional"></a>`_strip_optional(typ: Any)` — [`L341`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L341) — Splits an annotation into (non_optional_type, is_optional). — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_to_hashable_jax_static_arg"></a>`_to_hashable_jax_static_arg(val: Any, orig_annotation: Any = None)` — [`L830`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L830) — Converts a PyTorch-dispatched static argument to a hashable JAX value. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_unwrap_annotated"></a>`_unwrap_annotated(typ: Any)` — [`L334`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L334) — Unwraps typing.Annotated wrappers to get the underlying type. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_validate_pallas_mesh_world_size"></a>`_validate_pallas_mesh_world_size(*, mesh: jax.sharding.Mesh | None = None, mesh_shape: Sequence[int] | None = None, process_group: dist.ProcessGroup | None = None)` — [`L1366`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1366) — Validates that Pallas mesh, mesh_shape, and process_group match world size. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_verify_signature"></a>`_verify_signature(signature: inspect.Signature, bound_names: collections.abc.Set[str] = frozenset())` — [`L498`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L498) — Verify that the signature contains only types supported by PyTorch custom_op. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="custom_jax_kernel"></a>`custom_jax_kernel(jax_fn=None, name=None, static_argnums=(), donate_argnums=None, input_output_aliases=None, mesh: jax.sharding.Mesh | None = None, input_partition_specs=None, output_partition_specs=None, *, static_argnames=(), warn_deprecated: bool = True)` — [`L1399`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1399) — Deprecated: Please use `jax_op` instead. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="jax_op.dec"></a>`dec(fn: Callable[..., object])` — [`L1619`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1619) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="custom_jax_kernel.decorator"></a>`decorator(jax_fn: Callable[..., Any])` — [`L1503`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1503)
- <a id="_generate_torch_schema.dummy_fn"></a>`dummy_fn(*args, **kwargs)` — [`L904`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L904)
- <a id="jax_op.dec.fake_fn"></a>`fake_fn(*args, **kwargs)` — [`L1650`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1650) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="get_default_pallas_mesh"></a>`get_default_pallas_mesh(process_group: dist.ProcessGroup | None = None)` — [`L1784`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1784) — Constructs default 1D world rank-aligned JAX Mesh with axis ('rank',).
- <a id="get_global_shape"></a>`get_global_shape(local_shape, mesh, partition_spec)` — [`L143`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L143)
- <a id="_get_kernel_invocation_key.get_hash"></a>`get_hash(i, item)` — [`L314`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L314) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="get_local_shape"></a>`get_local_shape(global_shape, mesh, partition_spec)` — [`L147`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L147)
- <a id="get_pallas_mesh"></a>`get_pallas_mesh(axis_names: Sequence[str] | str, mesh_shape: Sequence[int] | None = None, process_group: dist.ProcessGroup | None = None)` — [`L1773`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1773) — Deprecated alias of `torch.tpu.pallas.get_pallas_mesh`.
- <a id="_verify_signature.is_valid_result"></a>`is_valid_result(result: Any)` — [`L533`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L533) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_verify_signature.is_valid_return_base_type"></a>`is_valid_return_base_type(typ: Any)` — [`L518`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L518)
- <a id="jax_op"></a>`jax_op(name, fn=None, /, *, donate_argnums=None, mesh: jax.sharding.Mesh | None = None, input_partition_specs=None, output_partition_specs=None)` — [`L1547`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L1547) — Registers a JAX function as a custom PyTorch operation.
- <a id="jax_placeholder"></a>`jax_placeholder(tensor: torch.Tensor | Sequence[torch.Tensor], mesh=None, partition_spec=None)` — [`L151`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L151) — Converts a torch tensor (or sequence of tensors) to a jax placeholder for tracing. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="jax_placeholders"></a>`jax_placeholders(tensors: Sequence[Any] | torch.Tensor, mesh=None, partition_specs=None)` — [`L198`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L198) — Converts a sequence of torch tensors to a sequence of jax placeholders. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="torch_placeholder"></a>`torch_placeholder(array: jax.core.ShapedArray | None, mesh: jax.sharding.Mesh | None = None, partition_spec: tuple[str | None, ...] | None = None, device: torch.device | str = "tpu")` — [`L220`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L220) — Converts a jax output to a torch tensor for return type. — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)

## Module values
- <a id="JAX_TO_TORCH_DTYPE_MAP"></a>`JAX_TO_TORCH_DTYPE_MAP` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L111) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="TORCH_TO_JAX_DTYPE_MAP"></a>`TORCH_TO_JAX_DTYPE_MAP` — [`L65`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L65) — documented in [pallas-custom-kernels](../../../../../concepts/pallas-custom-kernels.md)
- <a id="_KernelResultT"></a>`_KernelResultT` — [`L915`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L915)
- <a id="__all__"></a>`__all__` — [`L115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L115)
- <a id="ex"></a>`ex` — [`L55`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/pallas.py#L55)

