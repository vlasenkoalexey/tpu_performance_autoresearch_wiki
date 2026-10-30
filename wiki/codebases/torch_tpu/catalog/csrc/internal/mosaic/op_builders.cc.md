---
title: 'Module: csrc/internal/mosaic/op_builders.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/op_builders.cc
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  GetVmemMemRefType: GetVmemMemRefType(3081f1e7b0ccc294).
  CreateMatmul: CreateMatmul(e6211091e1b5db7).
  GetDimensionSemanticsAttr: GetDimensionSemanticsAttr(3ec7ae9c9b1ac477).
  CreateIotaOp: CreateIotaOp(2d24cd8577226ac).
  CreateRepeatOp: CreateRepeatOp(2fbd2eb2a2feedb).
  GetSmemMemRefType: GetSmemMemRefType(3081f1e7b0ccc294).
  CreateMlirContextWithDialects: CreateMlirContextWithDialects(83ad5685f0f25dcd).
  SerializeMosaicKernel: SerializeMosaicKernel(2657b5498cc9ea2b).
  CreateReciprocal: CreateReciprocal(a47e99fbf7f93d66).
  SetTcCoreTypeAttr: SetTcCoreTypeAttr(4605be22b28972f4).
---
# Module: [`csrc/internal/mosaic/op_builders.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc)

## Functions
- <a id="CreateIotaOp"></a>`CreateIotaOp(ImplicitLocOpBuilder& builder, Type type, int32_t dimension)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L82) — Helper to build a tpu::IotaOp.
- <a id="CreateMatmul"></a>`CreateMatmul(ImplicitLocOpBuilder& builder, Value lhs, Value rhs, const MatmulOptions& options)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L49) — Creates a matmul for two 2D vectors. — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `CreateMatmul(ImplicitLocOpBuilder& builder, Value lhs, Value rhs, const MatmulOptions& options)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L49)
- <a id="CreateMlirContextWithDialects"></a>`CreateMlirContextWithDialects()` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L137) — Helper to create an MLIR context with the dialects needed for TorchTPU
- `CreateMlirContextWithDialects()` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L137) — Helper to create an MLIR context with the dialects needed for TorchTPU
- <a id="CreateReciprocal"></a>`CreateReciprocal(ImplicitLocOpBuilder& b, Value input)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L106)
- <a id="CreateRepeatOp"></a>`CreateRepeatOp(ImplicitLocOpBuilder& builder, Value input, int64_t dimension, int64_t target_dim_size)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L87) — Helper to build a tpu::RepeatOp.
- <a id="GetDimensionSemanticsAttr"></a>`GetDimensionSemanticsAttr(MLIRContext* context, DimensionSemantics semantics)` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L125) — Helper to build a tpu:: dimension semantics attribute.
- `GetDimensionSemanticsAttr(MLIRContext* context, DimensionSemantics semantics)` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L125)
- <a id="GetSmemMemRefType"></a>`GetSmemMemRefType(MLIRContext* context, ArrayRef<int64_t> shape, Type element_type)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L118) — Helper to build a memref type with smem tpu::Smem memory space.
- <a id="GetVmemMemRefType"></a>`GetVmemMemRefType(MLIRContext* context, ArrayRef<int64_t> shape, Type element_type)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L111) — Helper to build a memref type with vmem tpu::Vmem memory space. — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- <a id="SerializeMosaicKernel"></a>`SerializeMosaicKernel(ModuleOp module, int serialization_version)` — [`L153`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L153) — Serialize the given module to a string.
- `SetTcCoreTypeAttr(func::FuncOp fn)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L148) — Add tpu.core_type = #tpu.core_type<kTc> attribute to the function.
- <a id="SetTcCoreTypeAttr"></a>`SetTcCoreTypeAttr(func::FuncOp fn)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/op_builders.cc#L148) — Add tpu.core_type = #tpu.core_type<kTc> attribute to the function.

