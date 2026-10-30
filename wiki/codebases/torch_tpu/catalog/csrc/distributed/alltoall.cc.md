---
title: 'Module: csrc/distributed/alltoall.cc'
type: catalog
provenance: extracted
module: csrc/distributed/alltoall.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildDistributedAllToAllShlo: BuildDistributedAllToAllShlo(f18f7ac28c427b1b).
  BuildDistributedAllToAllBaseShlo: BuildDistributedAllToAllBaseShlo(fec5608fa65bdd55).
  BuildDistributedAllToAllBaseUnevenSplitsShlo: BuildDistributedAllToAllBaseUnevenSplitsShlo(cfa480f60da0d6a4).
  SliceTensorsAlongDim0: SliceTensorsAlongDim0(22984c861abd8726).
  ConcatenateTensorsAlongDim0: ConcatenateTensorsAlongDim0(1a77c29d1493f431).
---
# Module: [`csrc/distributed/alltoall.cc`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc)

## Functions
- <a id="BuildDistributedAllToAllBaseShlo"></a>`BuildDistributedAllToAllBaseShlo(mlir::MlirOp input, const DeviceGroupList& device_groups)` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L42)
- <a id="BuildDistributedAllToAllBaseUnevenSplitsShlo"></a>`BuildDistributedAllToAllBaseUnevenSplitsShlo(mlir::MlirOp input, mlir::MlirOp output, absl::Span<const int32_t> input_offsets, absl::Span<const int32_t> send_sizes, absl::Span<const int32_t> output_offsets, absl::Span<const int32_t> recv_sizes, const DeviceGroupList& device_groups)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L71) — Builds and emits a StableHLO ragged all-to-all custom call for
- `BuildDistributedAllToAllShlo(absl::Span<mlir::MlirOp> inputs, const DeviceGroupList& device_groups)` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L108)
- <a id="BuildDistributedAllToAllShlo"></a>`BuildDistributedAllToAllShlo(absl::Span<mlir::MlirOp> inputs, const DeviceGroupList& device_groups)` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L108)
- <a id="ConcatenateTensorsAlongDim0"></a>`ConcatenateTensorsAlongDim0(absl::Span<mlir::MlirOp> inputs, mlir::ElementType output_dtype, absl::Span<const int64_t> total_input_shape, mlir::MlirBuilder& builder)` — [`L154`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L154) — Concatenates non-empty input tensors along dimension 0, or emits a zero-sized
- <a id="SliceTensorsAlongDim0"></a>`SliceTensorsAlongDim0(mlir::MlirOp tensor, absl::Span<const int32_t> split_sizes)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L163) — Slices a concatenated tensor along dimension 0 into individual tensors
- `SliceTensorsAlongDim0(mlir::MlirOp tensor, absl::Span<const int32_t> split_sizes)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/distributed/alltoall.cc#L163) — Slices a concatenated tensor along dimension 0 into individual tensors

