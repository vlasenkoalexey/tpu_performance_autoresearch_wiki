---
title: 'Module: csrc/ops/convolution/convolution_checks.cc'
type: catalog
provenance: extracted
module: csrc/ops/convolution/convolution_checks.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ValidateConvolutionSpatialDimensionsMatch: ValidateConvolutionSpatialDimensionsMatch(7a38a96a62752678).
  ValidateConvolutionBias: ValidateConvolutionBias(932dcc979f81fa1d).
  ValidateConvolutionInput: ValidateConvolutionInput(59ba4a10ac858a91).
  ValidateConvolutionWeight: ValidateConvolutionWeight(c32bdb8b6defc4c0).
---
# Module: [`csrc/ops/convolution/convolution_checks.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_checks.cc)

## Functions
- <a id="ValidateConvolutionBias"></a>`ValidateConvolutionBias(absl::Span<const int64_t> bias, const int64_t out_channels)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_checks.cc#L83)
- <a id="ValidateConvolutionInput"></a>`ValidateConvolutionInput(absl::Span<const int64_t> input)` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_checks.cc#L29)
- <a id="ValidateConvolutionSpatialDimensionsMatch"></a>`ValidateConvolutionSpatialDimensionsMatch(int num_spatial_dims, absl::Span<const int64_t> thing, std::string_view arg_name)` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_checks.cc#L38)
- <a id="ValidateConvolutionWeight"></a>`ValidateConvolutionWeight(absl::Span<const int64_t> weight, const int64_t num_spatial_dims, const int64_t in_channels, const int64_t groups, const bool transposed)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_checks.cc#L50)

