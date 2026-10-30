---
title: 'Module: csrc/ops/random/random_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/random/random_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRandom_: AtenRandom_(654039c1bc1b5689).
  AtenRandom_To: AtenRandom_To(16045db4646972c8).
  AtenRandom_From: AtenRandom_From(4e88c361e459fd3d).
  Random: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/Random(7c9528fdedc44cff).'
  FromToInRange: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/FromToInRange(377b22be506d844e).'
  ComputeToValue: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/ComputeToValue(b1e38ecf206840a0).'
  GetRandomFunctional: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/GetRandomFunctional(93133262e778a2b5).'
  ComputeToValue.-anonymous_type_6.operator-.scalar_t: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/ComputeToValue(b1e38ecf206840a0).$anonymous_type_6#`operator()`(83f5f38750778ac8).scalar_t#'
  ComputeToValue.-anonymous_type_1.operator-.scalar_t: '`$anonymous_namespace_csrc/ops/random/random_aten_kernels.cc`/ComputeToValue(b1e38ecf206840a0).$anonymous_type_1#`operator()`(83f5f38750778ac8).scalar_t#'
---
# Module: [`csrc/ops/random/random_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc)

## Classes
### <a id="ComputeToValue.-anonymous_type_1.operator-.scalar_t"></a>`ComputeToValue.-anonymous_type_1.operator-.scalar_t`
- def: [`csrc/ops/random/random_aten_kernels.cc:78`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L78)
- signature: `AT_DISPATCH_FLOATING_TYPES_AND2(at::ScalarType::Half, at::ScalarType::BFloat16, dtype, "random_float_to_value_calc", [&] { constexpr int64_t scalar_t_max = static_cast<int64_t>(1) << std::numeric_limits<scalar_t>::digits; maybe_to = scalar_t_max > std::numeric_limits<int64_t>::max() ? std::numeric_limits<int64_t>::max() : static_cast<int64_t>(scalar_t_max); })`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="ComputeToValue.-anonymous_type_6.operator-.scalar_t"></a>`ComputeToValue.-anonymous_type_6.operator-.scalar_t`
- def: [`csrc/ops/random/random_aten_kernels.cc:88`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L88)
- signature: `AT_DISPATCH_V2(dtype, "random_integral_to_value_calc", AT_WRAP([&] { if constexpr (std::is_same_v<scalar_t, bool>) { maybe_to = static_cast<int64_t>(true); } else { maybe_to = static_cast<int64_t>(std::numeric_limits<scalar_t>::max()); } }), AT_EXPAND(AT_INTEGRAL_TYPES_V2), at::kBool)`
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="AtenRandom_"></a>`AtenRandom_(at::Tensor& self, c10::optional<at::Generator> generator)` — [`L143`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L143)
- <a id="AtenRandom_From"></a>`AtenRandom_From(at::Tensor& self, int64_t from, c10::optional<int64_t> to, c10::optional<at::Generator> generator)` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L152)
- <a id="AtenRandom_To"></a>`AtenRandom_To(at::Tensor& self, int64_t to, c10::optional<at::Generator> generator)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L161)
- <a id="ComputeToValue"></a>`ComputeToValue(at::ScalarType dtype)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L72) — See https://docs.pytorch.org/docs/stable/generated/torch.Tensor.random_.html
- <a id="FromToInRange"></a>`FromToInRange(int64_t from, int64_t to, at::ScalarType dtype)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L101)
- `GetRandomFunctional(Dimensions dims, mlir::ElementType output_dtype, int64_t from, int64_t to)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L59)
- <a id="GetRandomFunctional"></a>`GetRandomFunctional(Dimensions dims, mlir::ElementType output_dtype, int64_t from, int64_t to)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L59)
- <a id="Random"></a>`Random(at::Tensor& self, c10::optional<at::Generator> generator, int64_t from, c10::optional<int64_t> to_opt, OpParamCacheKeys param_keys)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/random/random_aten_kernels.cc#L109)

