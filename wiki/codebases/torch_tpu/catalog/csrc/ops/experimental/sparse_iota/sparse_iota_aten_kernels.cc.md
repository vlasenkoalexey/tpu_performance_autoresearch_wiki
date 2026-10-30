---
title: 'Module: csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenSparseIota: AtenSparseIota(f37005713c1d1986).
  ValidateSparseIotaInputs: ValidateSparseIotaInputs(2f09ac6860a7e469).
  SparseIotaBuilder: '`$anonymous_namespace_csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`/SparseIotaBuilder(62b32c54a912d533).'
  kWaitThreshold: '`$anonymous_namespace_csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`/kWaitThreshold.'
  kMaxPadPerRow: '`$anonymous_namespace_csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`/kMaxPadPerRow.'
  kPadValue: '`$anonymous_namespace_csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`/kPadValue.'
---
# Module: [`csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc)

## Functions
- <a id="AtenSparseIota"></a>`AtenSparseIota(const at::Tensor& row_pointers, int64_t max_non_zeroes, int64_t max_non_zeroes_per_row)` — [`L113`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L113) — @brief Applies SparseIota to a CSR matrix on TPU SparseCore. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="SparseIotaBuilder"></a>`SparseIotaBuilder(int64_t max_non_zeroes, int64_t max_non_zeroes_per_row)` — [`L52`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L52)
- <a id="ValidateSparseIotaInputs"></a>`ValidateSparseIotaInputs(const at::Tensor& row_pointers, int64_t max_non_zeroes, int64_t max_non_zeroes_per_row)` — [`L92`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L92) — @brief Validates the inputs to the sparse iota op. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

## Module values
- <a id="kMaxPadPerRow"></a>`kMaxPadPerRow` — [`L49`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L49)
- <a id="kPadValue"></a>`kPadValue` — [`L48`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L48)
- <a id="kWaitThreshold"></a>`kWaitThreshold` — [`L50`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_iota/sparse_iota_aten_kernels.cc#L50)

