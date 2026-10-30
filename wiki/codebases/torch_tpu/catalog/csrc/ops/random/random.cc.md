---
title: 'Module: csrc/ops/random/random.cc'
type: catalog
provenance: extracted
module: csrc/ops/random/random.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildRandomShlo: BuildRandomShlo(ec11d8b6664aa609).
  BitsToRandomIntegersInRange: BitsToRandomIntegersInRange(acf7f2a23e7a58c7).
  AddLowerBound: AddLowerBound(869ef1e1f81b6807).
---
# Module: [`csrc/ops/random/random.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random.cc)

## Functions
- <a id="AddLowerBound"></a>`AddLowerBound(mlir::MlirOp random_in_range_integers, mlir::RankedTensorType output_type, mlir::MlirOp lower_bound)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random.cc#L89)
- <a id="BitsToRandomIntegersInRange"></a>`BitsToRandomIntegersInRange(mlir::MlirOp random_bits, mlir::MlirOp diff, bool range_is_single_bit)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random.cc#L55) — Returns a random integer in [from, to) as follows:
- `BuildRandomShlo(mlir::MlirOp state, Dimensions dims, mlir::ElementType output_dtype, int64_t from, int64_t to)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random.cc#L106)
- <a id="BuildRandomShlo"></a>`BuildRandomShlo(mlir::MlirOp state, Dimensions dims, mlir::ElementType output_dtype, int64_t from, int64_t to)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random.cc#L106)

