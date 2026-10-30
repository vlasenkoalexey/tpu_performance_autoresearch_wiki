---
title: 'Module: csrc/internal/mosaic/kiln/core/kernel.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/kernel.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  BuildKernel: BuildKernel(91d1616d362eea45).
  EmitIndexMapFunction: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/EmitIndexMapFunction(e26ef2c7e0b5da78).'
  KernelScope.KernelScope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#KernelScope(326d491cd21c54de).'
  ProgramId: ProgramId(81db6cfdad59847b).
  SetGridAttributes: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/SetGridAttributes(184e4347fd400706).'
  Kernel.Serialize: Kernel#Serialize(4a56ef89112eedbf).
  Kernel.Verify: Kernel#Verify(654e21e32f56641d).
  BlockType: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/BlockType(afbafad80e9c14dd).'
  KernelScope.spec: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#spec.'
  Kernel.ToString: Kernel#ToString(219584694fe2b248).
  CurrentScope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/CurrentScope(e79625b02e6cc37c).'
  KernelScope.tls_scope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#tls_scope.'
  ToMlirDimensionSemantics: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/ToMlirDimensionSemantics(15a1ad4eaf2056ba).'
  ScalarPrefetch: ScalarPrefetch(20b5302d452b24d).
  KernelScope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#'
  GetAt: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/GetAt(16805c98cab10ba2).'
  Scratch: Scratch(20b5302d452b24d).
  NumPrograms: NumPrograms(dc1f09c09fbff20f).
  In: In(20b5302d452b24d).
  Out: Out(20b5302d452b24d).
  Kernel.Impl: Kernel#Impl#
  GridRank: GridRank(b126dc7c1de90089).
  Kernel.Impl.module: Kernel#Impl#module.
  KernelScope.builder: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#builder.'
  Kernel.Kernel: Kernel#Kernel(5ab7830430de0292).
  KernelScope.-KernelScope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#`~KernelScope`(ced63f7c635d850d).'
  PrintModule: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/PrintModule(291a31be4e3220f4).'
  KernelScope.prev: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#prev.'
  KernelScope.scratch: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#scratch.'
  KernelScope.program_ids: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#program_ids.'
  KernelScope.scalar_prefetch: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#scalar_prefetch.'
  Kernel.Impl.context: Kernel#Impl#context.
  KernelScope.inputs: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#inputs.'
  KernelScope.outputs: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#outputs.'
  KernelScope.builder_scope: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/kernel.cc`/KernelScope#builder_scope.'
  Kernel.operator: Kernel#`operator=`(7578feef96f4a1b0).
  Kernel.-Kernel: Kernel#`~Kernel`(ced63f7c635d850d).
  is_status_or_ref: is_status_or_ref#
---
# Module: [`csrc/internal/mosaic/kiln/core/kernel.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc)

## Classes
### <a id="Kernel.Impl"></a>`Kernel.Impl`
- def: [`csrc/internal/mosaic/kiln/core/kernel.cc:230`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L230)
- signature: `struct Kernel::Impl`
- members:
  - <a id="Kernel.Impl.context"></a>`context` — [`L231`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L231)
  - <a id="Kernel.Impl.module"></a>`module` — [`L232`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L232)
- uses (calls/refs, reference-scoped): [`Kernel`](kernel.h.md#Kernel)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`Kernel`](kernel.h.md#Kernel), [`Serialize`](kernel.cc.md#Kernel.Serialize), [`Verify`](kernel.cc.md#Kernel.Verify), [`ToString`](kernel.cc.md#Kernel.ToString), [`Kernel`](kernel.cc.md#Kernel.Kernel)

### <a id="KernelScope"></a>`KernelScope`
- def: [`csrc/internal/mosaic/kiln/core/kernel.cc:67`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L67)
- signature: `struct KernelScope`
- members:
  - <a id="KernelScope.KernelScope"></a>`KernelScope(mlir::func::FuncOp fn, const KernelSpec& s)` — [`L68`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L68)
  - <a id="KernelScope.-KernelScope"></a>`~KernelScope()` — [`L96`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L96)
  - <a id="KernelScope.builder"></a>`builder` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L98)
  - <a id="KernelScope.builder_scope"></a>`builder_scope` — [`L100`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L100)
  - <a id="KernelScope.inputs"></a>`inputs` — [`L103`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L103)
  - <a id="KernelScope.outputs"></a>`outputs` — [`L104`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L104)
  - <a id="KernelScope.prev"></a>`prev` — [`L106`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L106)
  - <a id="KernelScope.program_ids"></a>`program_ids` — [`L101`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L101)
  - <a id="KernelScope.scalar_prefetch"></a>`scalar_prefetch` — [`L102`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L102)
  - <a id="KernelScope.scratch"></a>`scratch` — [`L105`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L105)
  - <a id="KernelScope.spec"></a>`spec` — [`L99`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L99)
  - <a id="KernelScope.tls_scope"></a>`tls_scope` — [`L108`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L108) — CPP_THREAD_LOCAL_OK=C++ scope
- uses (calls/refs, reference-scoped): [`Ref`](ref.h.md#Ref), [`Scalar`](scalar.h.md#Scalar), [`wrap`](context.h.md#wrap), [`Int32Type`](dtype.h.md#Int32Type), [`grid`](specs.h.md#KernelSpec.grid), [`BuilderScope`](context.h.md#BuilderScope), [`KernelSpec`](specs.h.md#KernelSpec), [`BuilderScope`](context.cc.md#BuilderScope.BuilderScope), [`grid`](specs.h.md#GridSpec.grid), [`scalar_prefetch`](specs.h.md#KernelSpec.scalar_prefetch), [`in_specs`](specs.h.md#KernelSpec.in_specs), [`out_specs`](specs.h.md#KernelSpec.out_specs), [`dtype`](specs.h.md#BasicBlockSpec.dtype), [`scratch`](specs.h.md#KernelSpec.scratch), [`dtype`](specs.h.md#ScratchSpec.dtype), [`dtype`](specs.h.md#ScalarPrefetchSpec.dtype)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`ProgramId`](kernel.cc.md#ProgramId), [`CurrentScope`](kernel.cc.md#CurrentScope), [`ScalarPrefetch`](kernel.cc.md#ScalarPrefetch), [`Scratch`](kernel.cc.md#Scratch), [`NumPrograms`](kernel.cc.md#NumPrograms), [`In`](kernel.cc.md#In), [`Out`](kernel.cc.md#Out), [`GridRank`](kernel.cc.md#GridRank)

### <a id="is_status_or_ref"></a>`is_status_or_ref`
- def: [`csrc/internal/mosaic/kiln/core/kernel.cc:63`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L63)
- signature: `using torch_tpu::is_status_or_ref`
- uses (calls/refs, reference-scoped): [`is_status_or_ref`](../../../../common/error_utils.h.md#is_status_or_ref)

## Functions
- <a id="BlockType"></a>`BlockType(mlir::MLIRContext* ctx, llvm::ArrayRef<int64_t> shape, DType dtype, MemorySpace space)` — [`L120`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L120) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="BuildKernel"></a>`BuildKernel(const KernelSpec& spec, absl::FunctionRef<void()> body)` — [`L275`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L275) — Low-level entry point taking an assembled `KernelSpec`. Prefer `CreateKernel` — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="CurrentScope"></a>`CurrentScope()` — [`L114`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L114)
- <a id="EmitIndexMapFunction"></a>`EmitIndexMapFunction(mlir::ImplicitLocOpBuilder& b, mlir::func::FuncOp kernel_fn, const KernelSpec& spec, llvm::ArrayRef<mlir::Type> prefetch_types, const IndexMap& map, int64_t block_rank, int64_t index)` — [`L147`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L147) — Emits the private function backing an `IndexMap::IndexFn`.
- <a id="GetAt"></a>`GetAt(const RangeT& range, int64_t idx, std::string_view name)` — [`L221`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L221)
- <a id="GridRank"></a>`GridRank()` — [`L266`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L266)
- <a id="In"></a>`In(int i)` — [`L271`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L271)
- <a id="NumPrograms"></a>`NumPrograms(int axis)` — [`L263`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L263) — Grid bound along `axis` (Pallas `pl.num_programs(axis)`).
- <a id="Out"></a>`Out(int i)` — [`L272`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L272)
- <a id="PrintModule"></a>`PrintModule(mlir::ModuleOp module)` — [`L139`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L139)
- <a id="ProgramId"></a>`ProgramId(int axis)` — [`L260`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L260) — Current iteration index along `axis` (Pallas `pl.program_id(axis)`).
- <a id="ScalarPrefetch"></a>`ScalarPrefetch(int i)` — [`L268`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L268) — Access to kernel ref arguments by position (used by `CreateKernel` to unpack
- <a id="Scratch"></a>`Scratch(int i)` — [`L273`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L273)
- <a id="SetGridAttributes"></a>`SetGridAttributes(mlir::ImplicitLocOpBuilder& b, mlir::func::FuncOp fn, const KernelSpec& spec, llvm::ArrayRef<mlir::Type> prefetch_types)` — [`L175`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L175) — documented in [mosaic-matmul](../../../../../../concepts/mosaic-matmul.md)
- <a id="ToMlirDimensionSemantics"></a>`ToMlirDimensionSemantics(DimensionSemantics s)` — [`L129`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L129) — documented in [mosaic-matmul](../../../../../../concepts/mosaic-matmul.md)

## Other members
- `Kernel` — [`L236`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L236)
- <a id="Kernel.-Kernel"></a>`Kernel.-Kernel` — [`L238`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L238)
- <a id="Kernel.Kernel"></a>`Kernel.Kernel` — [`L235`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L235)
- <a id="Kernel.Serialize"></a>`Kernel.Serialize` — [`L242`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L242)
- <a id="Kernel.ToString"></a>`Kernel.ToString` — [`L240`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L240)
- <a id="Kernel.Verify"></a>`Kernel.Verify` — [`L251`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L251) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Kernel.operator"></a>`Kernel.operator` — [`L237`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.cc#L237)

