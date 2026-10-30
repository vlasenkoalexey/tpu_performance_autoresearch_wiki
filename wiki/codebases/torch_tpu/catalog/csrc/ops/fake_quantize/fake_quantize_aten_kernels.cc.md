---
title: 'Module: csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  FakeQuantizePerTensorAffineCachemask: FakeQuantizePerTensorAffineCachemask(493b44247737806b).
  FakeQuantizePerTensorAffineCachemaskHelper: '`$anonymous_namespace_csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`/FakeQuantizePerTensorAffineCachemaskHelper(f325683812466a20).'
  BuildFakeQuantizePerTensorAffineCachemaskShlo: '`$anonymous_namespace_csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`/BuildFakeQuantizePerTensorAffineCachemaskShlo(a879e4db397de1b9).'
  FakeQuantizePerTensorAffineCachemaskResult.mask: '`$anonymous_namespace_csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`/FakeQuantizePerTensorAffineCachemaskResult#mask.'
  FakeQuantizePerTensorAffineCachemaskResult: '`$anonymous_namespace_csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`/FakeQuantizePerTensorAffineCachemaskResult#'
  FakeQuantizePerTensorAffineCachemaskResult.output: '`$anonymous_namespace_csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`/FakeQuantizePerTensorAffineCachemaskResult#output.'
---
# Module: [`csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc)

## Classes
### <a id="FakeQuantizePerTensorAffineCachemaskResult"></a>`FakeQuantizePerTensorAffineCachemaskResult`
- def: [`csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc:80`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L80)
- signature: `struct FakeQuantizePerTensorAffineCachemaskResult`
- members:
  - <a id="FakeQuantizePerTensorAffineCachemaskResult.mask"></a>`mask` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L82)
  - <a id="FakeQuantizePerTensorAffineCachemaskResult.output"></a>`output` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L81)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef)
- used by: [`FakeQuantizePerTensorAffineCachemaskHelper`](fake_quantize_aten_kernels.cc.md#FakeQuantizePerTensorAffineCachemaskHelper)

## Functions
- <a id="BuildFakeQuantizePerTensorAffineCachemaskShlo"></a>`BuildFakeQuantizePerTensorAffineCachemaskShlo(mlir::MlirOp self, double scale, int64_t zero_point, int64_t quant_min, int64_t quant_max)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L48)
- <a id="FakeQuantizePerTensorAffineCachemask"></a>`FakeQuantizePerTensorAffineCachemask(const at::Tensor& self, double scale, int64_t zero_point, int64_t quant_min, int64_t quant_max)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L112)
- <a id="FakeQuantizePerTensorAffineCachemaskHelper"></a>`FakeQuantizePerTensorAffineCachemaskHelper(const at::Tensor& self, double scale, int64_t zero_point, int64_t quant_min, int64_t quant_max, OpParamCacheKeys param_keys)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/fake_quantize/fake_quantize_aten_kernels.cc#L86)

