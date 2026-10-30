---
title: TPU MoE kernel switches (grouped matmul, paired gate/up, dispatch/combine, route score)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TPU MoE kernel switches (grouped matmul, paired gate/up, dispatch/combine, route score)

## Definition
In an MoE layer a router sends each token to its top-k of N experts, so the expert FFN becomes a
**grouped** matmul (different row counts per expert) wrapped in a *dispatch* (sort tokens by expert)
and a *combine* (put them back, weighted by route scores). On stock PyTorch ops both run poorly on
TPU. TorchTitan ships five TPU replacements, swapped in by two model converters and switched on per
module; the guide says **enable all five**, with the Pallas grouped matmul as the largest lever.

## In torchtitan (grounded)
| Kernel | Replaces | Switch |
|---|---|---|
| Grouped expert matmul ([`segment_matmul_pallas_2d`](../catalog/torchtitan/experiments/tpu/kernels/expert_segment_matmul.md#segment_matmul_pallas_2d)) | `torch._grouped_mm` per projection, fwd + bwd | [`TpuGroupedExperts.use_pallas_grouped_mm`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.use_pallas_grouped_mm) |
| Paired gate/up ([`paired_segment_matmul_pallas_2d`](../catalog/torchtitan/experiments/tpu/kernels/paired_segment_matmul.md#paired_segment_matmul_pallas_2d)) | two grouped matmuls (W1, W3) reading the same routed rows twice | [`use_pallas_paired_grouped_mm`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.use_pallas_paired_grouped_mm) |
| Kernel-native weight layout | a transpose of every expert weight per call | [`use_kernel_native_weight_layout`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.use_kernel_native_weight_layout) |
| Dispatch + combine ([`local_reorder`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#local_reorder), [`stable_grouped_reduce`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#stable_grouped_reduce)) | scatter-based autograd for sort-by-expert and top-k combine | [`TpuTokenDispatcherConverter`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuTokenDispatcherConverter) |
| Route-score gradient ([`route_score_grad`](../catalog/torchtitan/experiments/tpu/kernels/route_score.md#route_score_grad), [`scale_route_weights`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#scale_route_weights)) | saved fp32 copy of expert output + separate bwd reduction | [`TpuAllToAllTokenDispatcher.fuse_route_score_backward`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuAllToAllTokenDispatcher.fuse_route_score_backward) |

Enablement (the 30B recipe's values):
```python
cfg.model_spec = model_registry("30B-A3B-global-aux", attn_backend="sdpa",
    converters=[TpuTokenDispatcherConverter.Config(), TpuGroupedExpertsConverter.Config()])
for _, experts, _, _ in cfg.model_spec.model.traverse(TpuGroupedExperts.Config):
    experts.use_pallas_grouped_mm = True
    experts.use_pallas_paired_grouped_mm = True
    experts.use_kernel_native_weight_layout = True
    experts.pallas_grouped_mm_tile_m = 256
    experts.pallas_grouped_mm_tgmm_tiling = (256, 0, 0)
for _, d, _, _ in cfg.model_spec.model.traverse(TpuAllToAllTokenDispatcher.Config):
    d.fuse_route_score_backward = True
cfg.parallelism.expert_parallel_degree = 1
```
Converters: [`TpuGroupedExpertsConverter`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExpertsConverter),
[`TpuTokenDispatcherConverter`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuTokenDispatcherConverter).
Reference recipes: [`qwen3_moe_30b_fsdp_only_full_ac_benchmark`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_benchmark)
(30B), `qwen3_moe_235b_fsdp_activation_offload_*()` (235B, splitter),
[`qwen3_moe_235b_scan`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan) (235B, scan).

### Tiles (VMEM-bounded, tune per shape and generation)
- [`pallas_grouped_mm_tile_m`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tile_m)
  (code default 1024): forward row tile; with the paired kernel `tokens x top_k` must be a multiple of
  it or the kernel raises.
- [`pallas_grouped_mm_tgmm_tiling`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_tgmm_tiling)
  `(m, k, n)` (code default `(128, 128, 128)`): weight-gradient tiles, `0` = full axis; the paired
  kernel requires `n = 0`.
- [`pallas_grouped_mm_w2_tgmm_tiling`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_w2_tgmm_tiling):
  separate W2 tiling; the `k` tile runs along model dim for W1/W3 but expert hidden dim for W2, and an
  oversized `k` is **not clamped** - it allocates the full window and can exhaust VMEM before step 1.
  At large expert shapes the `k` tile is required, not optional (see the 235B recipes). Code also has
  [`pallas_grouped_mm_w2_transposed_tgmm_tiling`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts.pallas_grouped_mm_w2_transposed_tgmm_tiling)
  for the transposed-W2 RHS (W2 FSDP-sharded on its trailing axis), which the guide does not mention.

## Why it matters / when it applies
- **Correctness first:** use the Pallas grouped matmul, not `torch._grouped_mm` - the native op has
  produced incorrect weight gradients on TPU (torch_tpu issue 2668).
- Paired kernel and kernel-native layout both require `use_pallas_grouped_mm` (construction fails
  otherwise).
- Kernel-native layout: model checkpoints are unaffected (state-dict hooks translate to canonical
  keys), but **optimizer state is keyed by live names/shapes** (`w1_EDF` vs `w1_EFD`), so resuming
  optimizer state across a layout change needs a conversion.
- Expert compute is bf16 regardless of surrounding dtype; weight-grad kernels accumulate in fp32 and
  return bf16. Route-score fusion keeps fp32 multiply + reduction (only reduction order changes).
- **EP is not fully implemented: run `expert_parallel_degree=1`** and let FSDP shard expert weights.
  EP > 1 is accepted but loses the optimized path: the paired kernel rejects it; the TPU combine and
  route-score fusion are skipped ([`TpuAllToAllTokenDispatcher.combine`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuAllToAllTokenDispatcher.combine)
  delegates to the standard all-to-all path whenever an EP mesh exists); scan and `compile_grad_norm`
  reject it.
- Scan bodies cannot mutate MoE counters/metrics - see [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md);
  GraphTrainer's `tpu_selective` can save the `moe.routing` region
  ([tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md)).
- Profile dispatch/combine separately: after the kernels are on, reorder/combine around the expert
  matmul should no longer be a visible bucket.
- Keep routing in fp32; capacity factor / token dropping change model quality - not a free perf
  lever. MFU must use **active** params in `num_flops_per_token`.
- Code-only extra: [`TpuRoutedExperts.scale_before_down_proj`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuRoutedExperts.scale_before_down_proj)
  applies scores before W2 so a rematerializing backward does not recompute the W2 forward (not in
  the guide).

## Connections
- Code concepts: [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [qwen3-model](../concepts/qwen3-model.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md)
- Module catalogs: [grouped_experts](../catalog/torchtitan/experiments/tpu/grouped_experts.md),
  [token_dispatcher](../catalog/torchtitan/experiments/tpu/token_dispatcher.md),
  [kernels/expert_segment_matmul](../catalog/torchtitan/experiments/tpu/kernels/expert_segment_matmul.md),
  [kernels/paired_segment_matmul](../catalog/torchtitan/experiments/tpu/kernels/paired_segment_matmul.md),
  [kernels/route_score](../catalog/torchtitan/experiments/tpu/kernels/route_score.md),
  [qwen3/config_registry (tpu)](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md)
- Related doc-concepts: [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [hf-transformers-backend-on-tpu](hf-transformers-backend-on-tpu.md),
  [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 10; kept in
place).
