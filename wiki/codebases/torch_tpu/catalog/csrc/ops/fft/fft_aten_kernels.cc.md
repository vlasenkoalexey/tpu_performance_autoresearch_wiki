---
title: 'Module: csrc/ops/fft/fft_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fft/fft_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFftC2r: AtenFftC2r(8d8c1ff7a6f1d592).
  AtenFftC2c: AtenFftC2c(f3ffed1e9e470290).
  AtenFftC2rOut: AtenFftC2rOut(3b1345022cba1a56).
  AtenFftC2cOut: AtenFftC2cOut(fad6b7504b27180e).
  BuildFftC2cShlo: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/BuildFftC2cShlo(6f111c0e0dc98cb6).'
  BuildFftC2rShlo: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/BuildFftC2rShlo(389209499c11f8d9).'
  AtenFftR2c: AtenFftR2c(f3ffed1e9e470290).
  AtenFftR2cOut: AtenFftR2cOut(fad6b7504b27180e).
  BuildFftR2cShlo: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/BuildFftR2cShlo(6f111c0e0dc98cb6).'
  FFTValidateStaticShape: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FFTValidateStaticShape(d8359b99282c084c).'
  ApplyComplexScaling: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ApplyComplexScaling(2dfbe2d071436f89).'
  GetNormalizedDims: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/GetNormalizedDims(b32fbe9cee727de7).'
  ComputeScaleOp: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ComputeScaleOp(711dadbda19d47ec).'
  ScaleMode: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#'
  AtenFftIfftOut: AtenFftIfftOut(4d739c65a8414ade).
  AtenFftIrfft: AtenFftIrfft(bb46dc2996c03e51).
  AtenFftRfft: AtenFftRfft(bb46dc2996c03e51).
  AtenFftFftOut: AtenFftFftOut(4d739c65a8414ade).
  AtenFftRfftOut: AtenFftRfftOut(4d739c65a8414ade).
  AtenFftIrfftOut: AtenFftIrfftOut(4d739c65a8414ade).
  AtenFftFft: AtenFftFft(bb46dc2996c03e51).
  AtenFftIfft: AtenFftIfft(bb46dc2996c03e51).
  FftNormalization: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftNormalization#'
  PromoteToFloatIfBFloat16: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/PromoteToFloatIfBFloat16(28959186f7a4bda8).'
  TransposePermutations.requires_transpose: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/TransposePermutations#requires_transpose.'
  ComputeFftParams: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ComputeFftParams(75bb4f7d73d00835).'
  ScaleMode.kMulN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#kMulN.'
  ScaleMode.kNone: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#kNone.'
  FftNormalization.kByN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftNormalization#kByN.'
  TransposePermutations.permutation: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/TransposePermutations#permutation.'
  ComputeTransposePermutations: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ComputeTransposePermutations(b813864650451684).'
  FftParams.fft_length: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftParams#fft_length.'
  FftNormalization.kByRootN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftNormalization#kByRootN.'
  TransposePermutations: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/TransposePermutations#'
  FftParams: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftParams#'
  ScaleMode.kMulSqrtN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#kMulSqrtN.'
  ScaleMode.kDivSqrtN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#kDivSqrtN.'
  TransposePermutations.inverse_permutation: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/TransposePermutations#inverse_permutation.'
  ScaleMode.kDivN: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/ScaleMode#kDivN.'
  FftParams.is_fft_dim: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftParams#is_fft_dim.'
  FftNormalization.kNone: '`$anonymous_namespace_csrc/ops/fft/fft_aten_kernels.cc`/FftNormalization#kNone.'
---
# Module: [`csrc/ops/fft/fft_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc)

## Classes
### <a id="FftNormalization"></a>`FftNormalization`
- def: [`csrc/ops/fft/fft_aten_kernels.cc:68`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L68)
- doc: FftNormalization encapsulates PyTorch's three FFT scaling modes.
- signature: `enum class FftNormalization`
- members:
  - <a id="FftNormalization.kByN"></a>`kByN` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L71)
  - <a id="FftNormalization.kByRootN"></a>`kByRootN` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L70)
  - <a id="FftNormalization.kNone"></a>`kNone` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L69)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`AtenFftC2c`](fft_aten_kernels.cc.md#AtenFftC2c), [`AtenFftC2r`](fft_aten_kernels.cc.md#AtenFftC2r), [`AtenFftC2rOut`](fft_aten_kernels.cc.md#AtenFftC2rOut), [`AtenFftC2cOut`](fft_aten_kernels.cc.md#AtenFftC2cOut), [`BuildFftC2cShlo`](fft_aten_kernels.cc.md#BuildFftC2cShlo), [`BuildFftC2rShlo`](fft_aten_kernels.cc.md#BuildFftC2rShlo), [`AtenFftR2c`](fft_aten_kernels.cc.md#AtenFftR2c), [`AtenFftR2cOut`](fft_aten_kernels.cc.md#AtenFftR2cOut), [`BuildFftR2cShlo`](fft_aten_kernels.cc.md#BuildFftR2cShlo)

### <a id="FftParams"></a>`FftParams`
- def: [`csrc/ops/fft/fft_aten_kernels.cc:99`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L99)
- signature: `struct FftParams`
- members:
  - <a id="FftParams.fft_length"></a>`fft_length` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L100)
  - <a id="FftParams.is_fft_dim"></a>`is_fft_dim` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L101)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildFftC2cShlo`](fft_aten_kernels.cc.md#BuildFftC2cShlo), [`BuildFftC2rShlo`](fft_aten_kernels.cc.md#BuildFftC2rShlo), [`BuildFftR2cShlo`](fft_aten_kernels.cc.md#BuildFftR2cShlo)

### <a id="ScaleMode"></a>`ScaleMode`
- def: [`csrc/ops/fft/fft_aten_kernels.cc:177`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L177)
- signature: `enum class ScaleMode`
- members:
  - <a id="ScaleMode.kDivN"></a>`kDivN` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L180) — 1 / N
  - <a id="ScaleMode.kDivSqrtN"></a>`kDivSqrtN` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L179) — 1 / sqrt(N)
  - <a id="ScaleMode.kMulN"></a>`kMulN` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L182) — N
  - <a id="ScaleMode.kMulSqrtN"></a>`kMulSqrtN` — [`L181`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L181) — sqrt(N)
  - <a id="ScaleMode.kNone"></a>`kNone` — [`L178`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L178)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildFftC2cShlo`](fft_aten_kernels.cc.md#BuildFftC2cShlo), [`BuildFftC2rShlo`](fft_aten_kernels.cc.md#BuildFftC2rShlo), [`BuildFftR2cShlo`](fft_aten_kernels.cc.md#BuildFftR2cShlo), [`ComputeScaleOp`](fft_aten_kernels.cc.md#ComputeScaleOp)

### <a id="TransposePermutations"></a>`TransposePermutations`
- def: [`csrc/ops/fft/fft_aten_kernels.cc:129`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L129)
- signature: `struct TransposePermutations`
- members:
  - <a id="TransposePermutations.inverse_permutation"></a>`inverse_permutation` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L131)
  - <a id="TransposePermutations.permutation"></a>`permutation` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L130)
  - <a id="TransposePermutations.requires_transpose"></a>`requires_transpose` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L132)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildFftC2cShlo`](fft_aten_kernels.cc.md#BuildFftC2cShlo), [`BuildFftC2rShlo`](fft_aten_kernels.cc.md#BuildFftC2rShlo), [`BuildFftR2cShlo`](fft_aten_kernels.cc.md#BuildFftR2cShlo)

## Functions
- <a id="ApplyComplexScaling"></a>`ApplyComplexScaling(mlir::MlirOp fft_op, mlir::MlirOp scale_op, mlir::Type float_type)` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L206)
- <a id="AtenFftC2c"></a>`AtenFftC2c(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, bool forward)` — [`L512`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L512)
- <a id="AtenFftC2cOut"></a>`AtenFftC2cOut(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, bool forward, at::Tensor& out)` — [`L550`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L550)
- <a id="AtenFftC2r"></a>`AtenFftC2r(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, int64_t last_dim_size)` — [`L590`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L590)
- <a id="AtenFftC2rOut"></a>`AtenFftC2rOut(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, int64_t last_dim_size, at::Tensor& out)` — [`L638`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L638)
- <a id="AtenFftFft"></a>`AtenFftFft(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm)` — [`L687`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L687)
- <a id="AtenFftFftOut"></a>`AtenFftFftOut(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm, at::Tensor& out)` — [`L693`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L693)
- <a id="AtenFftIfft"></a>`AtenFftIfft(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm)` — [`L700`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L700)
- <a id="AtenFftIfftOut"></a>`AtenFftIfftOut(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm, at::Tensor& out)` — [`L706`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L706)
- <a id="AtenFftIrfft"></a>`AtenFftIrfft(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm)` — [`L726`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L726)
- <a id="AtenFftIrfftOut"></a>`AtenFftIrfftOut(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm, at::Tensor& out)` — [`L732`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L732)
- <a id="AtenFftR2c"></a>`AtenFftR2c(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, bool onesided)` — [`L424`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L424)
- <a id="AtenFftR2cOut"></a>`AtenFftR2cOut(const at::Tensor& self, at::IntArrayRef dim, int64_t normalization, bool onesided, at::Tensor& out)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L467)
- <a id="AtenFftRfft"></a>`AtenFftRfft(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm)` — [`L713`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L713)
- <a id="AtenFftRfftOut"></a>`AtenFftRfftOut(const at::Tensor& self, std::optional<c10::SymInt> n, int64_t dim, std::optional<c10::string_view> norm, at::Tensor& out)` — [`L719`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L719)
- <a id="BuildFftC2cShlo"></a>`BuildFftC2cShlo(mlir::MlirOp input, Dimensions dims, const FftNormalization normalization, bool forward)` — [`L277`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L277)
- <a id="BuildFftC2rShlo"></a>`BuildFftC2rShlo(mlir::MlirOp input, Dimensions dims, const FftNormalization normalization, int64_t last_dim_size)` — [`L347`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L347)
- <a id="BuildFftR2cShlo"></a>`BuildFftR2cShlo(mlir::MlirOp input, Dimensions dims, const FftNormalization normalization, bool onesided)` — [`L215`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L215)
- <a id="ComputeFftParams"></a>`ComputeFftParams(mlir::RankedTensorType input_type, Dimensions dims, std::optional<int64_t> last_dim_size = std::nullopt)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L104)
- <a id="ComputeScaleOp"></a>`ComputeScaleOp(mlir::MlirBuilder& builder, mlir::MlirOp num_elements_op, mlir::Type float_type, ScaleMode scale_mode)` — [`L185`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L185)
- <a id="ComputeTransposePermutations"></a>`ComputeTransposePermutations(int64_t num_dims, const Dimensions& dims)` — [`L140`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L140) — Computes dimension permutations for PyTorch-to-StableHLO FFT mapping.
- <a id="FFTValidateStaticShape"></a>`FFTValidateStaticShape(const at::Tensor& tensor, const std::string_view arg_name)` — [`L412`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L412)
- <a id="GetNormalizedDims"></a>`GetNormalizedDims(const at::Tensor& self, at::IntArrayRef dim)` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L75) — Normalizes the dimensions for the FFT operation
- <a id="PromoteToFloatIfBFloat16"></a>`PromoteToFloatIfBFloat16(const at::Tensor& self)` — [`L418`](../../../../../../../raw/code/torch_tpu/csrc/ops/fft/fft_aten_kernels.cc#L418)

