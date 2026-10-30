---
title: 'Module: csrc/ops/prod/prod_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/prod/prod_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenProdDimOut: AtenProdDimOut(f0a0e84b64653c26).
  AtenProd: AtenProd(9a630782726e6f51).
  AtenProdHelper: '`$anonymous_namespace_csrc/ops/prod/prod_aten_kernels.cc`/AtenProdHelper(4d7205f79456bd59).'
  ProdZeroDim: '`$anonymous_namespace_csrc/ops/prod/prod_aten_kernels.cc`/ProdZeroDim(2a652ff0464b8655).'
  GetSizesAfterProd: '`$anonymous_namespace_csrc/ops/prod/prod_aten_kernels.cc`/GetSizesAfterProd(591e1f0e9deaf2cb).'
  InferProdDtype: '`$anonymous_namespace_csrc/ops/prod/prod_aten_kernels.cc`/InferProdDtype(17de5c52a7844446).'
---
# Module: [`csrc/ops/prod/prod_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc)

## Functions
- <a id="AtenProd"></a>`AtenProd(const at::Tensor& self, std::optional<at::ScalarType> dtype)` — [`L158`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L158)
- <a id="AtenProdDimOut"></a>`AtenProdDimOut(const at::Tensor& self, int64_t dim, bool keep_dim, std::optional<at::ScalarType> dtype, at::Tensor& out)` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L169)
- <a id="AtenProdHelper"></a>`AtenProdHelper(const at::Tensor& self, std::optional<int64_t> dim, bool keep_dim, std::optional<at::ScalarType> dtype, OpParamCacheKeys param_keys)` — [`L114`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L114)
- <a id="GetSizesAfterProd"></a>`GetSizesAfterProd(at::IntArrayRef self_size, std::optional<int64_t> dim, bool keep_dim)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L62)
- <a id="InferProdDtype"></a>`InferProdDtype(at::ScalarType input_dtype, std::optional<at::ScalarType> dtype)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L49)
- <a id="ProdZeroDim"></a>`ProdZeroDim(const at::Tensor& self, at::ScalarType inferred_dtype, OpParamCacheKeys param_keys)` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/prod/prod_aten_kernels.cc#L88) — Helper function to handle 0-dimensional tensor (scalar) product reduction.

