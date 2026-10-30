---
title: 'Module: src/torch_tpu/_internal/device_utils/annotations.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/device_utils/annotations.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.device_utils.annotations`/
symbols:
  TpuLayout: TpuLayout#
  LayoutContext.__enter__: LayoutContext#__enter__().
  TpuLayout.tiles: TpuLayout#tiles.
  TpuLayout.minor_to_major: TpuLayout#minor_to_major.
  LayoutContext: LayoutContext#
  dataclass: dataclass.
  LayoutContext._layout: LayoutContext#_layout.
  LayoutContext.__init__: LayoutContext#__init__().
  field: field.
  TpuLayout.element_size_in_bits: TpuLayout#element_size_in_bits.
  LayoutContext.__exit__: LayoutContext#__exit__().
---
# Module: [`src/torch_tpu/_internal/device_utils/annotations.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py)

## Classes
### <a id="LayoutContext"></a>`LayoutContext`
- def: [`src/torch_tpu/_internal/device_utils/annotations.py:47`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L47)
- doc: Context manager to set the layout hint for TPU tensors.
- signature: `class LayoutContext:`
- members:
  - <a id="LayoutContext.__init__"></a>`__init__(self, layout: TpuLayout)` — [`L58`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L58) — Initializes the LayoutContext.
- protocol/private: <a id="LayoutContext.__enter__"></a>`__enter__`[`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L72), <a id="LayoutContext.__exit__"></a>`__exit__`[`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L79), <a id="LayoutContext._layout"></a>`_layout`[`L70`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L70)
- uses (calls/refs, reference-scoped): [`TpuLayout`](annotations.md#TpuLayout), [`tiles`](annotations.md#TpuLayout.tiles), [`minor_to_major`](annotations.md#TpuLayout.minor_to_major), [`element_size_in_bits`](annotations.md#TpuLayout.element_size_in_bits)
- used by: [`test_layout_context_1d_tiling`](annotations_test.md#AnnotationsTest.test_layout_context_1d_tiling), [`test_layout_context_device_arg`](annotations_test.md#AnnotationsTest.test_layout_context_device_arg), [`test_layout_context_nested`](annotations_test.md#AnnotationsTest.test_layout_context_nested), [`test_layout_context_to_device`](annotations_test.md#AnnotationsTest.test_layout_context_to_device)

### <a id="TpuLayout"></a>`TpuLayout`
- def: [`src/torch_tpu/_internal/device_utils/annotations.py:27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L27)
- doc: Mimics layout class from xla/layout.h.
- signature: `class TpuLayout:`
- members:
  - <a id="TpuLayout.element_size_in_bits"></a>`element_size_in_bits` — [`L40`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L40)
  - <a id="TpuLayout.minor_to_major"></a>`minor_to_major` — [`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L38)
  - <a id="TpuLayout.tiles"></a>`tiles` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L39)
- uses (calls/refs, reference-scoped): [`field`](annotations.md#field)
- used by: [`__enter__`](annotations.md#LayoutContext.__enter__), [`test_layout_context_1d_tiling`](annotations_test.md#AnnotationsTest.test_layout_context_1d_tiling), [`test_layout_context_device_arg`](annotations_test.md#AnnotationsTest.test_layout_context_device_arg), [`test_layout_context_nested`](annotations_test.md#AnnotationsTest.test_layout_context_nested), [`test_layout_context_to_device`](annotations_test.md#AnnotationsTest.test_layout_context_to_device), [`__init__`](annotations.md#LayoutContext.__init__)

## Module values
- <a id="dataclass"></a>`dataclass` — [`L23`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L23)
- <a id="field"></a>`field` — [`L22`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/device_utils/annotations.py#L22)

