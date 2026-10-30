---
title: Large-model structure on TPU - scan over layers, graph splitter, CPU offload
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Large-model structure on TPU - scan over layers, graph splitter, CPU offload

## Definition
One unrolled GraphTrainer step stops working as models grow: compile time and compile-time memory
scale with depth; under ZeRO-3 XLA can merge forward and recomputed all-gathers and keep full params
alive through backward; and even with full recompute every layer's saved input is live at the end of
forward. **Scan** (layers as one loop body) and the **graph splitter** (many per-layer-group programs)
give the step a structure that fixes the first two; **CPU offload** of saved activations fixes the
third and works with either. Large recipes combine ZeRO-3 + full recompute + offload + one of scan or
splitter (never both).

## In torchtitan (grounded)
| | Scan | Graph splitter |
|---|---|---|
| Switch | [`use_scan_layers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.use_scan_layers) | [`GraphSplitterConfig.enabled`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.enabled) |
| Code | [`LayerStack`](../catalog/torchtitan/experiments/tpu/graph_trainer/layer_stack.md#LayerStack), [`StackedLayers`](../catalog/torchtitan/experiments/tpu/graph_trainer/layer_stack.md#StackedLayers), [`with_tpu_stacked_layers`](../catalog/torchtitan/experiments/tpu/graph_trainer/layer_stack.md#with_tpu_stacked_layers) | [`GraphSplitter`](../catalog/torchtitan/experiments/tpu/graph_trainer/graph_split.md#GraphSplitter), [`split_forward_backward_graph`](../catalog/torchtitan/experiments/tpu/graph_trainer/graph_split.md#split_forward_backward_graph), [`split_backward_graph_by_layer`](../catalog/torchtitan/experiments/tpu/graph_trainer/graph_split.md#split_backward_graph_by_layer) |
| Step runs as | one program, layers as one loop | many programs, one per layer group |
| Params | stacked `[n_layers, ...]`; per-layer names gone from `named_parameters()` | unchanged |
| Parallelism | FSDP / HSDP tested; TP, CP, PP, EP rejected ([`check_scan_parallelism`](../catalog/torchtitan/experiments/tpu/graph_trainer/scan_guards.md#check_scan_parallelism)) | unrestricted by config; recipes are FSDP/HSDP |
| In-graph optimizer | allowed, unused | rejected |
| Offload policy | `full_and_scan_offload` | `full_and_offload` (or `tpu_selective_and_offload`) |
| Recipes | `llama3_*_scan()`, [`qwen3_moe_235b_scan`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_scan) | `qwen3_moe_235b_fsdp_activation_offload_*()` (e.g. [`qwen3_moe_235b_fsdp_activation_offload_4x4x4`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_235b_fsdp_activation_offload_4x4x4)) |

Lighter mid-size option keeping one unrolled graph: `compile.fsdp_barrier_policy="prefetch"` or
`"interleave"` with `compile.enable_remat_barriers=True`, as in
[`qwen3_8b_zero3`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b_zero3).

### Scan specifics
- Body compiled once -> depth no longer scales compile time; `llama3_405b_scan()` exists because the
  per-layer path does not compile at 405B ([`_on_scan_lane`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_on_scan_lane)
  also switches to bf16 Adam moments, `fused_opt_states_bf16`).
- FSDP gathers one layer's shard inside the loop body; the body is fully recomputed in backward,
  including its all-gather. Only the layer input is saved per layer.
- Constraints: GraphTrainer + `aot_fx_trace` only (eager scan does not run on TPU); the body must not
  mutate inputs/module state (MoE load-balance counters and routing metrics: see
  `qwen3_moe_235b_scan()` workarounds, `metrics.enable_moe_routing=False`); Llama3 complex RoPE does
  not trace in a scan body, so recipes swap in the bit-identical
  [`TpuRealArithmeticComplexRoPE`](../catalog/torchtitan/experiments/tpu/overrides/real_rope.md#TpuRealArithmeticComplexRoPE);
  model checkpoints keep per-layer keys but **optimizer checkpoints cannot resume across a flip** of
  the flag; generic `*_and_offload` policies are rejected; use the recipe's libtpu bundle (in the 235B
  recipe expert-grad reduce-scatters land at the loop-body end and run measurably slower without it).
  [`check_scan_was_applied`](../catalog/torchtitan/experiments/tpu/graph_trainer/scan_guards.md#check_scan_was_applied)
  guards silent no-ops.

### Graph splitter knobs ([`GraphSplitterConfig`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig))
- [`forward_layers_per_executable`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.forward_layers_per_executable)
  (`-1` = one forward program), [`forward_isolate_prefix`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.forward_isolate_prefix)
  (embedding in its own program),
  [`backward_partition_mode`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.backward_partition_mode)
  (`none` | `by_layer` keeps each layer's FSDP collectives with it | `fsdp_pipeline` moves each AG one
  program earlier and RS one later to overlap with neighbours),
  [`backward_layers_per_executable`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.backward_layers_per_executable),
  [`donate_internal_buffers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.donate_internal_buffers)
  (default True; disable only for diagnostics),
  [`cpu_offload_prefetch_executables`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#GraphSplitterConfig.cpu_offload_prefetch_executables).
- Trade-off: small programs compile fast and bound compile memory, but XLA overlaps comm/compute only
  within one program and each boundary is a host dispatch. Start at 1 layer per executable; raise to
  widen the scheduling window.
- Requires `fsdp_barrier_policy="none"` (remat barriers do compose); no in-graph optimizer; no
  serialized precompiled FX artifacts (the normal TorchTPU compilation cache still works).
- Not to be confused with the regular trainer's `compile.materialize_forward_before_backward`
  ([tpu-per-block-torch-compile](tpu-per-block-torch-compile.md)).

### CPU offload
- Memory lever, not a speed lever: copies each saved `[batch, seq, dim]` layer input to host in
  forward, reloads before its backward.

| Policy | Use with | Offloaded |
|---|---|---|
| `sac_and_offload` | unrolled / splitter | what selective recompute still saves |
| `full_and_offload` | unrolled / splitter | saved layer boundaries |
| `tpu_selective_and_offload` | unrolled / splitter | layer boundaries; save regions stay in HBM |
| `full_and_scan_offload` | scan | the one stacked layer-input tensor ([`offload_scan_activations`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.md#offload_scan_activations)) |

- [`GraphTrainerCompileConfig.cpu_offload_budget_gb`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.cpu_offload_budget_gb)
  (default 100 GiB per rank; largest-first) - not applied to the scan policy. Ensure that much free
  host RAM **per rank** (and mind the MegaScale pool on multi-slice,
  [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md)).
- **With scan, offload is close to mandatory:** per-layer saves form one stacked
  `[n_layers, batch, seq, dim]` tensor that cannot be freed row by row; Llama3 scan recipes above 8B
  need `full_and_scan_offload` to run at all. It puts one offload in the forward body and one reload in
  the backward body.
- **With the splitter, prefetch the reload:** `compile.graph_split.cpu_offload_prefetch_executables=1`
  issues it one backward program earlier (requires a split backward).
- libtpu flags the offload recipes set: `xla_tpu_enable_offloading_copy_to_sparsecore=false` (keep host
  copies off SparseCore, small effect) and `xla_tpu_copy_insertion_use_region_analysis=true` with
  `..._limit=1000` (removed device-to-host waits on the 235B splitter recipe, "clear MFU gain").
- Verify in the profile that H2D / D2H waits are hidden; otherwise offload costs step time.

## Why it matters / when it applies
Use scan or the splitter when the step no longer compiles or fits as one unrolled graph, and add
offload when HBM-bound after full recompute. Pick scan for depth-independent compile and per-layer AG
streaming on pure data-parallel meshes; pick the splitter when you need unrestricted parallelism or
per-layer params, accepting more dispatch boundaries.

## Connections
- Code concepts: [tpu-graph-trainer](../concepts/tpu-graph-trainer.md),
  [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [graph-trainer](../concepts/graph-trainer.md), [llama3-model](../concepts/llama3-model.md),
  [qwen3-model](../concepts/qwen3-model.md), [checkpointing](../concepts/checkpointing.md)
- Module catalogs: [graph_trainer/layer_stack](../catalog/torchtitan/experiments/tpu/graph_trainer/layer_stack.md),
  [graph_trainer/graph_split](../catalog/torchtitan/experiments/tpu/graph_trainer/graph_split.md),
  [graph_trainer/tpu_host_offload](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.md),
  [graph_trainer/scan_guards](../catalog/torchtitan/experiments/tpu/graph_trainer/scan_guards.md),
  [graph_trainer/config (tpu)](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md)
- Related doc-concepts: [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md), [graph-trainer-memory-policy](graph-trainer-memory-policy.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 9; kept in
place).
