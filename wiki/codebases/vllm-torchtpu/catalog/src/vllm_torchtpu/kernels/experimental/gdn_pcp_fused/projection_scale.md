---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.projection_scale`/
symbols:
  projection_scale_layout: projection_scale_layout().
  normalize_projection_scale: normalize_projection_scale().
  ProjectionScaleLayout: ProjectionScaleLayout#
  ProjectionScaleLayout.TENSOR: ProjectionScaleLayout#TENSOR.
  ProjectionScaleLayout.CHANNEL: ProjectionScaleLayout#CHANNEL.
  ProjectionScaleLayout.BLOCK_GRID: ProjectionScaleLayout#BLOCK_GRID.
  ProjectionScaleLayout.LINEAR_RUNTIME: ProjectionScaleLayout#LINEAR_RUNTIME.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py)

## Classes
### <a id="ProjectionScaleLayout"></a>`ProjectionScaleLayout`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py:28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L28) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- signature: `class ProjectionScaleLayout(Enum):`
- members:
  - <a id="ProjectionScaleLayout.BLOCK_GRID"></a>`BLOCK_GRID` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L31)
  - <a id="ProjectionScaleLayout.CHANNEL"></a>`CHANNEL` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L30)
  - <a id="ProjectionScaleLayout.LINEAR_RUNTIME"></a>`LINEAR_RUNTIME` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L32)
  - <a id="ProjectionScaleLayout.TENSOR"></a>`TENSOR` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L29)
- used by: [`normalize_projection_scale`](projection_scale.md#normalize_projection_scale), [`projection_scale_layout`](projection_scale.md#projection_scale_layout)

## Functions
- <a id="normalize_projection_scale"></a>`normalize_projection_scale(weight_shape, scale)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L74) — Return [N] for a full-K scale or [K_blocks, N] for blocked weights. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="projection_scale_layout"></a>`projection_scale_layout(weight_shape, scale_shape)` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/projection_scale.py#L35) — Validate N-major weights and return (layout, N blocks, K blocks). — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)

