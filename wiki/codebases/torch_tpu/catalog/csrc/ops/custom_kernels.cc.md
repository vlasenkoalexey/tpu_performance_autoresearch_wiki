---
title: 'Module: csrc/ops/custom_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/custom_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CustomKernelRegistry.LoadCustomKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#LoadCustomKernel(e9159f33045cca59).'
  PartitionGlobalToLocal: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/PartitionGlobalToLocal(46eaf757e0ddf986).'
  InjectCustomKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/InjectCustomKernel(836832f7f01b5b10).'
  RegisterCustomKernel: RegisterCustomKernel(4f5e29323fb5dc39).
  MoveCustomMlirKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/MoveCustomMlirKernel(2a2610568217480a).'
  ValidateAndEraseShapeAssertions: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/ValidateAndEraseShapeAssertions(1810fd72177fe2ee).'
  SpecializeCustomMlirKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/SpecializeCustomMlirKernel(5367cb4df16f0545).'
  CallCustomKernel: CallCustomKernel(b90e01880e730056).
  AddTpuPartitioningPasses: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/AddTpuPartitioningPasses(acd38c9ce4c44385).'
  BuildSpecializedMlirKernel: BuildSpecializedMlirKernel(eac48c915493fb80).
  LookupCustomKernel: LookupCustomKernel(3c7df3f261a805ca).
  CustomKernelId.Hash.operator: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Hash#`operator()`(47bcf86e7d2873c).'
  GetUniqueCustomKernelName: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/GetUniqueCustomKernelName(2dd72884347d23f0).'
  CustomKernelRegistry.LookupCustomKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#LookupCustomKernel(3c7df3f261a805ca).'
  CustomKernelRegistry: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#'
  CustomKernelRegistry.RegisterCustomKernel: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#RegisterCustomKernel(4f5e29323fb5dc39).'
  CustomKernelRegistry.registry_: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#registry_.'
  CustomKernelRegistry.GetInstance: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#GetInstance(79d33175a99fe065).'
  CustomKernelId: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#'
  RemoveSpmdModuleShardings: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/RemoveSpmdModuleShardings(1eec3824a7432d71).'
  ContainsSdyManualComputation: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/ContainsSdyManualComputation(5f146d1a9d83a370).'
  CustomKernelRegistry.mutex_: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#mutex_.'
  CustomKernelRegistry.operator: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#`operator=`(c458e2dd016dd3a6).'
  CustomKernelRegistry.CustomKernelRegistry: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelRegistry#CustomKernelRegistry(1aaa4573443b24f8).'
  CustomKernelIdRef: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelIdRef#'
  CustomKernelIdRef.name: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelIdRef#name.'
  CustomKernelId.Hash: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Hash#'
  CustomKernelId.kwargs: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#kwargs.'
  CustomKernelId.Eq: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Eq#'
  CustomKernelIdRef.kwargs: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelIdRef#kwargs.'
  CustomKernelId.name: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#name.'
  CustomKernelId.Hash.is_transparent: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Hash#is_transparent#'
  CustomKernelId.Eq.operator: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Eq#`operator()`(3ac64f90aa5a27ad).'
  CustomKernelId.Eq.is_transparent: '`$anonymous_namespace_csrc/ops/custom_kernels.cc`/CustomKernelId#Eq#is_transparent#'
---
# Module: [`csrc/ops/custom_kernels.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc)

## Classes
### <a id="CustomKernelId"></a>`CustomKernelId`
- def: [`csrc/ops/custom_kernels.cc:449`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L449)
- doc: The identifier for a custom kernel, without the specialized shapes.
- signature: `struct CustomKernelId`
- members:
  - <a id="CustomKernelId.kwargs"></a>`kwargs` — [`L480`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L480) — A string representation of the keyword arguments to the custom kernel.
  - <a id="CustomKernelId.name"></a>`name` — [`L476`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L476) — The name of the custom kernel (user-provided).
- used by: [`LoadCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.LoadCustomKernel), [`operator()`](custom_kernels.cc.md#CustomKernelId.Hash.operator), [`LookupCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.LookupCustomKernel), [`RegisterCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.RegisterCustomKernel)

### <a id="CustomKernelId.Eq"></a>`CustomKernelId.Eq`
- def: [`csrc/ops/custom_kernels.cc:466`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L466)
- doc: A transparent equality functor for CustomKernelId and
- signature: `struct Eq`
- members:
  - <a id="CustomKernelId.Eq.operator"></a>`operator()()` — [`L470`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L470)
- used by: [`LoadCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.LoadCustomKernel)

### <a id="CustomKernelId.Eq.is_transparent"></a>`CustomKernelId.Eq.is_transparent`
- def: [`csrc/ops/custom_kernels.cc:467`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L467)
- signature: `using is_transparent = void`

### <a id="CustomKernelId.Hash"></a>`CustomKernelId.Hash`
- def: [`csrc/ops/custom_kernels.cc:452`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L452)
- doc: A transparent hasher for CustomKernelId and
- signature: `struct Hash`
- members:
  - <a id="CustomKernelId.Hash.operator"></a>`operator()()` — [`L455`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L455)
  - `operator()()` — [`L458`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L458)
- uses (calls/refs, reference-scoped): [`FingerprintCat`](../common/fingerprint_utils.h.md#FingerprintCat), [`FingerprintCat`](../common/fingerprint_utils.h.md#FingerprintCat), [`FingerprintCat`](../common/fingerprint_utils.h.md#FingerprintCat), [`CustomKernelId`](custom_kernels.cc.md#CustomKernelId), [`CustomKernelIdRef`](custom_kernels.cc.md#CustomKernelIdRef), [`kwargs`](custom_kernels.cc.md#CustomKernelId.kwargs), [`kwargs`](custom_kernels.cc.md#CustomKernelIdRef.kwargs), [`name`](custom_kernels.cc.md#CustomKernelId.name), [`name`](custom_kernels.cc.md#CustomKernelIdRef.name)
- used by: [`LoadCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.LoadCustomKernel)

### <a id="CustomKernelId.Hash.is_transparent"></a>`CustomKernelId.Hash.is_transparent`
- def: [`csrc/ops/custom_kernels.cc:453`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L453)
- signature: `using is_transparent = void`

### <a id="CustomKernelIdRef"></a>`CustomKernelIdRef`
- def: [`csrc/ops/custom_kernels.cc:439`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L439)
- doc: An ephemeral, non-owning CustomKernelId.
- signature: `struct CustomKernelIdRef`
- members:
  - <a id="CustomKernelIdRef.kwargs"></a>`kwargs` — [`L445`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L445) — A string representation of the keyword arguments to the custom kernel.
  - <a id="CustomKernelIdRef.name"></a>`name` — [`L441`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L441) — The name of the custom kernel (user-provided).
- used by: [`LoadCustomKernel`](custom_kernels.cc.md#CustomKernelRegistry.LoadCustomKernel), [`operator()`](custom_kernels.cc.md#CustomKernelId.Hash.operator)

### <a id="CustomKernelRegistry"></a>`CustomKernelRegistry`
- def: [`csrc/ops/custom_kernels.cc:484`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L484)
- doc: The global singleton to hold all custom and specialized kernels.
- signature: `class CustomKernelRegistry`
- members:
  - <a id="CustomKernelRegistry.CustomKernelRegistry"></a>`CustomKernelRegistry(CustomKernelRegistry&&)` — [`L491`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L491)
  - `CustomKernelRegistry(const CustomKernelRegistry&)` — [`L489`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L489) — This class is neither copyable nor movable.
  - `CustomKernelRegistry()` — [`L486`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L486)
  - <a id="CustomKernelRegistry.GetInstance"></a>`GetInstance()` — [`L494`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L494)
  - <a id="CustomKernelRegistry.LoadCustomKernel"></a>`LoadCustomKernel(mlir::MlirBuilder& builder, std::string_view name, std::string_view kernel_key, absl::Span<const absl::Span<const int64_t>> input_dims, absl::Span<const mlir::ElementType> input_dtypes)` — [`L540`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L540) — Loads a registered custom kernel's MLIR into the given builder, and
  - <a id="CustomKernelRegistry.LookupCustomKernel"></a>`LookupCustomKernel(std::string_view name, std::string_view kwargs)` — [`L530`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L530)
  - <a id="CustomKernelRegistry.RegisterCustomKernel"></a>`RegisterCustomKernel(std::string_view name, std::string_view kwargs, std::string_view mlir_module_string)` — [`L517`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L517) — Registers a custom kernel. This can be any kernel that has been
  - <a id="CustomKernelRegistry.operator"></a>`operator=(const CustomKernelRegistry&)` — [`L490`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L490)
  - `operator=(CustomKernelRegistry&&)` — [`L492`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L492)
  - <a id="CustomKernelRegistry.mutex_"></a>`mutex_` — [`L593`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L593) — Protects registry_.
  - <a id="CustomKernelRegistry.registry_"></a>`registry_` — [`L592`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L592) — A map from CustomKernelId to the serialized representation of the
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../common/status_builder.h.md#StatusBuilder), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`is_status_or_ref`](../common/error_utils.h.md#is_status_or_ref), [`operator<<`](op_names.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`operator<<`](../common/status_builder.h.md#operator), [`StatusBuilder`](../common/status_builder.cc.md#StatusBuilder.StatusBuilder), [`InjectCustomKernel`](custom_kernels.cc.md#InjectCustomKernel), [`kNotFound`](../common/error_utils.h.md#kNotFound), [`GetUniqueCustomKernelName`](custom_kernels.cc.md#GetUniqueCustomKernelName), [`CustomKernelId`](custom_kernels.cc.md#CustomKernelId), [`CustomKernelIdRef`](custom_kernels.cc.md#CustomKernelIdRef), [`Eq`](custom_kernels.cc.md#CustomKernelId.Eq), [`Hash`](custom_kernels.cc.md#CustomKernelId.Hash)
- used by: [`RegisterCustomKernel`](custom_kernels.cc.md#RegisterCustomKernel), [`CallCustomKernel`](custom_kernels.cc.md#CallCustomKernel), [`LookupCustomKernel`](custom_kernels.cc.md#LookupCustomKernel)

## Functions
- <a id="AddTpuPartitioningPasses"></a>`AddTpuPartitioningPasses(xla::HloModule* module, const xla::AliasInfo* alias_info, xla::HloPassPipeline* pipeline)` — [`L231`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L231)
- `BuildSpecializedMlirKernel(mlir::MlirBuilder& builder, mlir::ModuleOp custom_kernel, absl::Span<mlir::MlirOp> inputs)` — [`L641`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L641) — Build a specialized MLIR kernel from a custom dynamically shaped MLIR
- <a id="BuildSpecializedMlirKernel"></a>`BuildSpecializedMlirKernel(mlir::MlirBuilder& builder, mlir::ModuleOp custom_kernel, absl::Span<mlir::MlirOp> inputs)` — [`L641`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L641) — Build a specialized MLIR kernel from a custom dynamically shaped MLIR
- `CallCustomKernel(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> inputs, std::string_view name, std::string_view kwargs)` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L608) — Calls a registered custom kernel with the given inputs.
- <a id="CallCustomKernel"></a>`CallCustomKernel(mlir::MlirBuilder& builder, absl::Span<const mlir::MlirOp> inputs, std::string_view name, std::string_view kwargs)` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L608) — Calls a registered custom kernel with the given inputs.
- <a id="ContainsSdyManualComputation"></a>`ContainsSdyManualComputation(mlir::ModuleOp module)` — [`L400`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L400) — Returns true if the module contains any sdy.manual_computation operations.
- <a id="GetUniqueCustomKernelName"></a>`GetUniqueCustomKernelName(std::string_view name, std::string_view kwargs, absl::Span<const absl::Span<const int64_t>> input_dims, absl::Span<const mlir::ElementType> input_dtypes)` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L94) — Returns a unique name for a custom kernel, based on the name, kwargs,
- <a id="InjectCustomKernel"></a>`InjectCustomKernel(mlir::MlirBuilder& builder, mlir::ModuleOp custom_kernel, mlir::ArrayRef<mlir::Type> input_types, std::optional<std::string_view> kernel_id_str = std::nullopt)` — [`L412`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L412)
- <a id="LookupCustomKernel"></a>`LookupCustomKernel(std::string_view name, std::string_view kwargs)` — [`L604`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L604) — Looks up a registered custom kernel with the given name and kwargs.
- <a id="MoveCustomMlirKernel"></a>`MoveCustomMlirKernel(mlir::ModuleOp custom_kernel, mlir::ModuleOp dst_module, std::optional<std::string_view> kernel_id_str = std::nullopt)` — [`L122`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L122) — Given a custom MLIR kernel, move it to the destination module and
- <a id="PartitionGlobalToLocal"></a>`PartitionGlobalToLocal(mlir::MLIRContext* context, mlir::ModuleOp module, const xla::PjRtTopologyDescription* client_topology)` — [`L297`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L297)
- <a id="RegisterCustomKernel"></a>`RegisterCustomKernel(std::string_view name, std::string_view kwargs, std::string_view mlir_module_string)` — [`L598`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L598) — Registers a custom kernel. This can be any kernel that has been
- <a id="RemoveSpmdModuleShardings"></a>`RemoveSpmdModuleShardings(mlir::ModuleOp module)` — [`L226`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L226)
- <a id="SpecializeCustomMlirKernel"></a>`SpecializeCustomMlirKernel(mlir::ModuleOp custom_kernel, mlir::ArrayRef<mlir::Type> input_types)` — [`L207`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L207) — Given a custom MLIR kernel, possibly with dynamic shapes, specialize it
- <a id="ValidateAndEraseShapeAssertions"></a>`ValidateAndEraseShapeAssertions(mlir::ModuleOp module)` — [`L102`](../../../../../../raw/code/torch_tpu/csrc/ops/custom_kernels.cc#L102)

