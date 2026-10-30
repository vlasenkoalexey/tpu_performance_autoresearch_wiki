---
slug: torchtitan
commit: 2ad96c9390ea7206a154b1cade409b589ef6d9e7
scip_tool: scip-python
updated: 2026-10-29
okf_version: "0.2"
sources:
  - {resource: ../../../raw/code/torchtitan, title: torchtitan @ 2ad96c9390}
---

# torchtitan internals wiki

Generated, grounded wiki. Start from a concept (or an area); drill into cited symbols.
The commit pin above is the single source version for every page in this silo.

**Start here → [Overview](overview.md)** — The google-pytorch fork of TorchTitan at commit 2ad96c939: upstream's config-built PyTorch LLM trainer (ModelSpec registry, one device mesh with FSDP/TP/PP/CP/EP views, per-block torch.compile, graph trainer) plus the TorchTPU backend in torchtitan/experiments/tpu, which retunes recipes, parallelism, Pallas kernels and libtpu flags for Cloud TPU, alongside a pure-JAX lane and a GPU-only RL stack.

## Areas
One page per top-level area: what it is for, the units inside it with their entry points, and the small units that have no page of their own.
- [components](areas/components.md) — Training components of torchtitan: data loading, checkpointing, optimizers and LR schedulers, quantization converters, loss/metrics/validation.
- [config](areas/config.md) — Job configuration of torchtitan: the frozen Config tree, recipe registry functions and the CLI that selects and overrides them.
- [distributed](areas/distributed.md) — Distributed layer of torchtitan: ParallelDims and the device mesh, FSDP/TP/PP/CP/EP application, activation checkpointing, FlexShard, and the async/DeepEP expert-parallel paths.
- [experiments](areas/experiments.md) — Experimental lanes of torchtitan: the TorchTPU backend (experiments/tpu), the JAX lane, the graph trainer and RL.
- [hf_datasets](areas/hf_datasets.md) — Hugging Face dataset sources of torchtitan: text and multimodal datasets, chat formatting and sample packing.
- [models](areas/models.md) — Model zoo of torchtitan: shared building blocks plus Llama3, Qwen3/3.5, DeepSeek-V3/V4, Kimi, GPT-OSS, Muse Glimmer and Flux, each with its parallelize function and recipes.
- [observability](areas/observability.md) — Observability in torchtitan: metrics and MFU, structured logging, and silent-data-corruption replay checks.
- [overrides](areas/overrides.md) — Kernel/module overrides of torchtitan: config-driven replacement of RoPE, norms, fused SwiGLU/MLA and grouped experts with Triton/Helion implementations.
- [protocols](areas/protocols.md) — Protocols of torchtitan: Module/Configurable, ModelSpec and the sharding/param-init contracts every model implements.
- [tools](areas/tools.md) — Debug and profiling tools of torchtitan: torch/JAX profiler wiring, memory snapshots, device-info and peak-FLOPS helpers.

## Concepts (deep)
Grouped by the source area each page's citations point into.

### `torchtitan/experiments/tpu`
| Concept | Description | Status |
|---|---|---|
| [tpu-context-parallel-attention](concepts/tpu-context-parallel-attention.md) | How the experiments/tpu lane implements context parallelism as CP mixins over the single-device SDPA/Varlen inner attentions - MaxText-style load-balanced KV all-gather with head-tail sequence order and per-rank Splash masks, or Ulysses all-to-all head resharding - including input sharding, segment-id precomputation, the pluggable Splash kernel and the config validator. Read before enabling or debugging CP on TPU. | fresh |
| [tpu-layer-loop-remat-and-layouts](concepts/tpu-layer-loop-remat-and-layouts.md) | How the TorchTPU lane controls what XLA sees per decoder layer - the TpuLayerLoop seam that makes scan-over-layers possible, the copy-free scan backward patch, the TPU selective-AC policies and remat region names, and the [B, L] block layout, packed QKV and uneven-shard fixes; read when tuning memory, recompute or layout on TPU. | fresh |
| [tpu-moe-dispatch-and-grouped-experts](concepts/tpu-moe-dispatch-and-grouped-experts.md) | How the experiments/tpu lane swaps the standard MoE token dispatcher, routed-experts block and grouped experts for TPU versions - row-gather VJPs instead of collision scatters, an FP32 fixed-K combine, route scaling before W2 so remat skips the W2 forward, and opt-in Pallas grouped matmuls with a kernel-native weight layout. Read before tuning or debugging MoE step time on TPU. | fresh |
| [tpu-trainer-and-job-config](concepts/tpu-trainer-and-job-config.md) | How the TorchTPU lane turns a Python recipe into a running job - the TPUTrainerConfig blocks (splash, Pallas loss, flags, compile policy), the XLA/libtpu flag layering, the kernel patches applied right before parallelize, and the TPUTrainer forward/backward split; read before tuning or adding a TPU recipe. | fresh |

### `torchtitan`
| Concept | Description | Status |
|---|---|---|
| [trainer-and-train-loop](concepts/trainer-and-train-loop.md) | How a parsed job config becomes a running job - the Trainer constructor's fixed build order (mesh -> meta model -> overrides -> parallelize_fn/pipelining_fn -> init -> optimizer -> data -> checkpoint), and the train -> train_step -> forward_backward_step -> clip -> optimizer/lr -> metrics/checkpoint loop with its host-sync avoidance; plus what the TPU lane's TPUTrainer / TpuGraphTrainer overrides change. Read it before changing where a parallelism, compile or remat decision is applied, or when reasoning about per-step host overhead on TPU. | fresh |

### `torchtitan/components`
| Concept | Description | Status |
|---|---|---|
| [training-components](concepts/training-components.md) | How the pluggable non-model pieces of a torchtitan training job are structured and wired - every component is a Configurable built by the Trainer with runtime kwargs, stateful ones share one Stateful checkpoint contract, and the perf-relevant knobs (chunked / loss-parallel cross-entropy, optimizer implementation, async checkpointing, packed Grain batches, MFU accounting) live on their configs. Read when choosing a loss/optimizer/checkpoint policy for a recipe, interpreting tps/MFU numbers, or seeing why the TPU lane rejects or replaces some of these components. | fresh |

### `torchtitan/components/checkpointer`
| Concept | Description | Status |
|---|---|---|
| [checkpointing](concepts/checkpointing.md) | How torchtitan saves and restores training state - the BaseCheckpointManager contract and its shared retention/latest-step/load policies, the DCP CheckpointManager (sync, async, pinned-memory async, HF safetensors export) and the torch_checkpointing-backed manager - and how the trainer and TPU recipes use it (seed checkpoints, HF initial load, load_only). Read before changing checkpoint config, debugging resume, or measuring checkpoint stalls. | fresh |

### `torchtitan/components/data`
| Concept | Description | Status |
|---|---|---|
| [data-loading](concepts/data-loading.md) | How torchtitan/components/data turns a composable dataset config into a per-DP-rank Grain pipeline (source -> filter/process -> shuffle/shard/repeat -> pack -> collate -> prefetch) that always emits one fixed-shape, pre-padded, page-locked token batch, and how that pipeline is checkpointed; read before changing batch size, packing, or dataset sources, or when debugging input stalls or recompiles. | fresh |

### `torchtitan/components/optimizer`
| Concept | Description | Status |
|---|---|---|
| [optimizers-and-lr-schedulers](concepts/optimizers-and-lr-schedulers.md) | How torchtitan/components/optimizer builds one optimizer per (model part, optimizer type) from regex param groups, which implementation knobs (fused / foreach / bf16 states) it exposes and how the TPU lane uses or replaces them, how the warmup-stable-decay LambdaLR schedule is computed and checkpointed, how optimizer state is flattened to FQN keys for DCP, and the MoE load-balancing step pre-hook; read when tuning optimizer memory/speed, adding an optimizer, or resuming across a parallelism change. | fresh |

### `torchtitan/components/quantization`
| Concept | Description | Status |
|---|---|---|
| [quantization](concepts/quantization.md) | How torchtitan's low-precision training works - QuantizationConverter subclasses rewrite the model config tree before build (Linear.Config -> Float8/MXFP8/NVFP4 Linear.Config, GroupedExperts.Config -> quantized experts), how MXFP8 weights quantize once per FSDP unshard via a sharded/unsharded tensor-subclass pair, and what the TPU lane reuses or bypasses. Read before enabling FP8 on any lane or reasoning about MFU under quantization. | fresh |

### `torchtitan/config`
| Concept | Description | Status |
|---|---|---|
| [job-config](concepts/job-config.md) | How a torchtitan run is described as a Python-built tree of `Configurable.Config` dataclasses - the `Configurable` / `build()` auto-wiring, the shared `TrainingConfig` / `ParallelismConfig` / `CompileConfig` knobs, `ConfigManager`'s --module/--config + frozen CLI, model-config transforms, cross-section validation and the `@override` swap mechanism; read it before adding a knob, writing a recipe (including TPU recipes), or reasoning about which config value actually reaches the model. | fresh |

### `torchtitan/distributed`
| Concept | Description | Status |
|---|---|---|
| [parallel-dims-and-parallelization](concepts/parallel-dims-and-parallelization.md) | How torchtitan turns parallelism degrees into one world DeviceMesh with many named views, and how TP, activation checkpointing, torch.compile, FSDP/HSDP, PP and EP are applied on top of it - including what the TPU lane changes (topology-aware mesh, SimpleFSDP, TPU selective-AC policies). Read before touching mesh axes, parallelize functions or AC/compile order. | fresh |

### `torchtitan/distributed/flex_shard`
| Concept | Description | Status |
|---|---|---|
| [flex-shard](concepts/flex-shard.md) | How torchtitan.distributed.flex_shard lets an optimizer (DistMuon) run on a temporary compute layout that differs from the FSDP/EP DTensor storage layout - ComputeLayout/Owned/BlockShard declarations, bucket planning, packed all-to-all schedules and the two-slot stream pipeline. Read before configuring Muon for a sharded model or reasoning about optimizer-step communication. | fresh |

### `torchtitan/experiments/graph_trainer`
| Concept | Description | Status |
|---|---|---|
| [graph-trainer](concepts/graph-trainer.md) | How GraphTrainer traces forward + loss + backward into one FX graph with make_fx, expresses FSDP as in-graph collectives (SimpleFSDP), and turns remat, offload, comm bucketing/overlap, EP overlap, Inductor compilation and CUDA graphs into ordered graph passes; plus precompile, GraphPP pipeline parallelism, AutoParallel, and the hook TpuGraphTrainer uses to swap in a TPU pass pipeline. Read before changing a pass, a memory policy, or the config conversion that feeds the TPU graph lane. | fresh |

### `torchtitan/experiments/jax`
| Concept | Description | Status |
|---|---|---|
| [jax-lane](concepts/jax-lane.md) | How the pure-JAX TorchTitan lane trains Llama3 on TPU without PyTorch in the step - flag application, the (fsdp, tp) mesh, path-pattern sharding maps, scan-over-layers with jax.checkpoint remat, the tokamax splash-attention callable, the donated nnx.jit train step, and how its MFU number is computed. Read before benchmarking or tuning the jax lane, or when comparing it against the TorchTPU lane. | fresh |

### `torchtitan/experiments/rl`
| Concept | Description | Status |
|---|---|---|
| [rl-training](concepts/rl-training.md) | How the RL experiment wires a TorchTitan PolicyTrainer and one or more vLLM generators on separate process meshes into an asynchronous rollout -> batch -> train loop with a bounded off-policy buffer and overlapped weight sync; what the GRPO/DAPO losses and group-relative advantages compute; and which knobs set throughput. Read before sizing an RL run, reasoning about off-policy lag, or asking whether this path applies to TPU (it is GPU/vLLM-only in this checkout). | fresh |

### `torchtitan/experiments/tpu/graph_trainer`
| Concept | Description | Status |
|---|---|---|
| [tpu-graph-trainer](concepts/tpu-graph-trainer.md) | How TpuGraphTrainer traces forward+loss+backward (and optionally AdamW) into one make_fx graph, rewrites it with the TPU pass pipeline (memory policies, remat and FSDP scheduling barriers, MoE combine barriers, reduce-scatter -> all-reduce), optionally scans stacked decoder layers or splits the graph into several executables, and lowers each piece to a static XLA executable. Read before choosing compile.memory_policy / use_scan_layers / graph_split / fsdp_barrier_policy for a large TPU run. | fresh |

### `torchtitan/experiments/tpu/kernels`
| Concept | Description | Status |
|---|---|---|
| [tpu-pallas-kernels](concepts/tpu-pallas-kernels.md) | How the experiments/tpu backend swaps PyTorch attention, MoE expert matmuls and the LM-head loss for JAX/Pallas kernels bridged into torch_tpu - the three splash attention backends and their config channels, block-sparse MaskInfo and document-aware skipping, the SBD fork's bias/dropout/base2 knobs, Megablox GMM and the FP8 grouped matmul, and the VMEM-sized fused cross-entropy. Read before tuning splash block sizes, choosing an attention backend, or debugging why a kernel config did not take effect. | fresh |

### `torchtitan/hf_datasets/multimodal`
| Concept | Description | Status |
|---|---|---|
| [hf-datasets](concepts/hf-datasets.md) | How torchtitan/hf_datasets plugs Hugging Face datasets into the Grain data pipeline - the DATASETS / MM_DATASETS registries of ready-made SingleDatasetConfig leaves, the TextProcessor / ChatProcessor / MultiModalProcessor row processors (tokenize, shift, mask), multimodal packing, and the MultiModalCollator that turns images into patch sequences and MRoPE positions; read when picking or adding a dataset, debugging label masking, or reasoning about VLM input shapes. | fresh |

### `torchtitan/models/common`
| Concept | Description | Status |
|---|---|---|
| [model-building-blocks](concepts/model-building-blocks.md) | How the shared model components in torchtitan/models/common fit together - every layer is a Module built from a nested kw-only Config tree, the Decoder walks a list of TransformerBlock configs, attention is split into an outer GQAttention and a swappable inner kernel backend, and each leaf carries its own ShardingConfig and remat region names. Read before changing a model's structure, swapping an attention/RoPE/linear implementation (as the TPU backend does), or reasoning about where TP/SP/EP placements and activation-checkpoint boundaries come from. | fresh |

### `torchtitan/models/deepseek_v3`
| Concept | Description | Status |
|---|---|---|
| [deepseek-v3-model](concepts/deepseek-v3-model.md) | How torchtitan/models/deepseek_v3 builds a DeepSeek-V3 decoder (multi-head latent attention + dense-then-MoE layers + optional multi-token prediction), how its declarative sharding plan and parallelize_deepseekv3 compose TP/SP/EP/FSDP/CP/AC/compile, how FLOPs are counted for MFU, and how the TPU lane reuses it. Read before tuning or porting DeepSeek-V3 on TPU. | fresh |

### `torchtitan/models/deepseek_v4`
| Concept | Description | Status |
|---|---|---|
| [deepseek-v4-model](concepts/deepseek-v4-model.md) | How torchtitan/models/deepseek_v4 builds DeepSeek-V4 (4-branch hyper-connection residual stream with Sinkhorn mixing, per-layer sliding-window / compressed-sparse / heavily-compressed attention on flex_attention block masks, hash-routed and sqrtsoftplus-routed MoE, optional MTP), how it is sharded and parallelized, how its FLOPs are counted, and which parallelism axes it rejects. Read before profiling or porting DeepSeek-V4. | fresh |

### `torchtitan/models/flux`
| Concept | Description | Status |
|---|---|---|
| [flux-diffusion-model](concepts/flux-diffusion-model.md) | How torchtitan trains the FLUX text-to-image transformer - its own FluxTrainer loop that runs frozen T5/CLIP/autoencoder encoders per step, the FSDP + context-parallel + activation-checkpoint + per-block compile recipe, and what the TPU lane changes; read before touching Flux performance or its configs. | fresh |

### `torchtitan/models/gpt_oss`
| Concept | Description | Status |
|---|---|---|
| [gpt-oss-model](concepts/gpt-oss-model.md) | How torchtitan/models/gpt_oss builds GPT-OSS 20B/120B (GQA attention with learned per-head sinks applied through an LSE epilogue, alternating 128-token sliding-window and full layers, all-MoE blocks whose grouped experts carry biases and a clamped SwiGLU), how masks are built per attention backend, how TP/EP/SP/FSDP/AC/compile compose in parallelize_gptoss, and the bias-scaling trick TP needs. Read before profiling GPT-OSS or porting its attention to a TPU kernel. | fresh |

### `torchtitan/models/kimi_k2_7`
| Concept | Description | Status |
|---|---|---|
| [kimi-k2-7-model](concepts/kimi-k2-7-model.md) | How torchtitan/models/kimi_k2_7 builds a DeepSeek-V3 MLA+MoE decoder plus a MoonViT3d vision tower, how its TP/SP/EP/FSDP/PP plan is composed around the vision scatter, and how the DistMuon optimizer and QK clipping are wired in; read before training or retuning any Kimi or Moonlight flavor. | fresh |

### `torchtitan/models/kimi_k3`
| Concept | Description | Status |
|---|---|---|
| [kimi-k3-model](concepts/kimi-k3-model.md) | How torchtitan/models/kimi_k3 assembles, parallelizes and runs Kimi K3 - the hybrid Kimi Delta Attention / gated MLA decoder with block-level Attention Residuals, latent-space MoE and a MoonViT vision tower - and why it is currently an FSDP2/EP, GPU-only (Blackwell) model with no TPU path; read before trying to port or tune it. | fresh |

### `torchtitan/models/llama3`
| Concept | Description | Status |
|---|---|---|
| [llama3-model](concepts/llama3-model.md) | How the Llama 3 package turns a flavor name into a ModelSpec (per-layer configs, sharding declarations, parallelize_fn, HF adapter) and which knobs - attention backend, fused QKV, AC, compile, FSDP, float8/MXFP8/NVFP4 converters - matter for TPU performance; read before tuning or porting a Llama 3 recipe. | fresh |

### `torchtitan/models/muse_glimmer`
| Concept | Description | Status |
|---|---|---|
| [muse-glimmer-model](concepts/muse-glimmer-model.md) | How torchtitan/models/muse_glimmer builds, shards, parallelizes and feeds the Muse Glimmer decoder (iRoPE + per-layer sliding windows, gated GQA, soft-capped head) and its optional in-model vision encoder; read before changing its parallelism, attention backend or multimodal input path. | fresh |

### `torchtitan/models/qwen3`
| Concept | Description | Status |
|---|---|---|
| [qwen3-model](concepts/qwen3-model.md) | How the Qwen3 package builds dense and MoE decoders from one block type (QK-norm GQA, CosSin RoPE, optional routed-expert MoE), how sharding/EP/expert-FSDP and the MoE load-balancing losses are wired, and what the TPU lane changes (unfused QKV at 8B, SimpleFSDP, Splash, fused loss); read before tuning a Qwen3 recipe on TPU. | fresh |

### `torchtitan/models/qwen3_5`
| Concept | Description | Status |
|---|---|---|
| [qwen3-5-model](concepts/qwen3-5-model.md) | How Qwen3.5 interleaves Gated DeltaNet linear-attention layers with gated full-attention layers (3:1), adds MRoPE, OffsetRMSNorm, a vision encoder and shared-expert MoE, how TP/SP/EP sharding and FSDP are declared for that hybrid, why CP is rejected, and what the TPU lane replaces; read before running or tuning Qwen3.5 on TPU. | fresh |

### `torchtitan/observability/structured_logger`
| Concept | Description | Status |
|---|---|---|
| [observability](concepts/observability.md) | How torchtitan's observability package works - the structured logger (log_trace_span / log_trace_instant / log_trace_scalar stamped with step and step tags, per-rank JSONL, pluggable handlers, a Perfetto Gantt merger) and the SDCReplayer that re-executes a deterministic forward/backward to detect silent data corruption. Read when you need per-phase host timing across ranks, want to tag anomalous steps, or are deciding whether to pay the replay overhead. | fresh |

### `torchtitan/overrides`
| Concept | Description | Status |
|---|---|---|
| [config-overrides](concepts/config-overrides.md) | How the in-repo override modules (fused SwiGLU / dist-GEMM SwiGLU / fused grouped experts, Helion RoPE, fused DeepSeek-V3 MLA, Triton OffsetRMSNorm, MoE dispatcher knobs) replace a component's Config at trainer construction, and the contract each one follows (subclass the target, derive the config, custom op with fake + autograd, sharding and checkpoint parity, non-CUDA fallback); read it before writing a kernel override - including a TPU one - or when deciding why an override is or is not active on TPU. | fresh |

### `torchtitan/protocols`
| Concept | Description | Status |
|---|---|---|
| [model-spec-protocols](concepts/model-spec-protocols.md) | How torchtitan/protocols defines the contract every model obeys - Module (nn.Module + Configurable) with config-driven build, init_states and declarative parallelize; ModelSpec as the per-model bundle the trainer consumes; ShardingConfig/LocalMapConfig placements resolved per mesh axis; ModelConfigConverter for pre-build rewrites; and the HF state-dict adapter. Read to understand the meta-device build -> parallelize -> init lifecycle, where TP/SP/CP redistributions are inserted, and how a backend (e.g. TPU) retunes a model without editing it. | fresh |

### `torchtitan/tools`
| Concept | Description | Status |
|---|---|---|
| [debug-and-profiling-tools](concepts/debug-and-profiling-tools.md) | How torchtitan/tools works - the Profiler that schedules torch.profiler traces (with a TorchTPU tracer config on TPU) and CUDA-style memory snapshots, the device_type/device_module abstraction that patches torch.tpu, get_peak_flops (the MFU denominator, including TPU per-chip/per-core values), controlled garbage collection, the root console logger, and fsspec-aware path helpers. Read before capturing a profile on any lane or trusting an MFU number. | fresh |

## Doc-derived concepts
Concepts extracted from the project's own docs (README / `docs/`), grounded to the symbol catalog. The source docs stay in place.
- [a3-mega-gpu-multinode-guides](doc-concepts/a3-mega-gpu-multinode-guides.md)
- [configurable-overrides](doc-concepts/configurable-overrides.md)
- [data-parallel-sharding-and-loader-state](doc-concepts/data-parallel-sharding-and-loader-state.md)
- [dataset-mixing-and-packing](doc-concepts/dataset-mixing-and-packing.md)
- [declarative-sharding-config](doc-concepts/declarative-sharding-config.md)
- [deepseek-v3-multi-token-prediction](doc-concepts/deepseek-v3-multi-token-prediction.md)
- [experiments-contribution-contract](doc-concepts/experiments-contribution-contract.md)
- [flexshard-optimizer-compute-layouts](doc-concepts/flexshard-optimizer-compute-layouts.md)
- [float8-training](doc-concepts/float8-training.md)
- [flux-training-notes](doc-concepts/flux-training-notes.md)
- [fsdp-cast-forward-inputs-fp32-rope](doc-concepts/fsdp-cast-forward-inputs-fp32-rope.md)
- [full-configuration-recipes](doc-concepts/full-configuration-recipes.md)
- [grain-data-pipeline](doc-concepts/grain-data-pipeline.md)
- [graph-pp-pipeline-parallelism](doc-concepts/graph-pp-pipeline-parallelism.md)
- [graph-trainer-autoparallel](doc-concepts/graph-trainer-autoparallel.md)
- [graph-trainer-autoresearch-harness](doc-concepts/graph-trainer-autoresearch-harness.md)
- [graph-trainer-ep-overlap](doc-concepts/graph-trainer-ep-overlap.md)
- [graph-trainer-full-step-graph-capture](doc-concepts/graph-trainer-full-step-graph-capture.md)
- [graph-trainer-memory-policy](doc-concepts/graph-trainer-memory-policy.md)
- [graph-trainer-pass-pipeline](doc-concepts/graph-trainer-pass-pipeline.md)
- [graph-trainer-precompile](doc-concepts/graph-trainer-precompile.md)
- [hf-transformers-backend-on-tpu](doc-concepts/hf-transformers-backend-on-tpu.md)
- [jax-flax-nnx-lane](doc-concepts/jax-flax-nnx-lane.md)
- [jax-fsdp-tp-mesh-sharding](doc-concepts/jax-fsdp-tp-mesh-sharding.md)
- [jax-scan-over-layers](doc-concepts/jax-scan-over-layers.md)
- [kimi-k2-7-model-notes](doc-concepts/kimi-k2-7-model-notes.md)
- [model-config-transforms](doc-concepts/model-config-transforms.md)
- [model-folder-contract](doc-concepts/model-folder-contract.md)
- [model-support-overview](doc-concepts/model-support-overview.md)
- [moe-sharding-placements](doc-concepts/moe-sharding-placements.md)
- [muse-glimmer-architecture](doc-concepts/muse-glimmer-architecture.md)
- [mxfp8-training](doc-concepts/mxfp8-training.md)
- [nvfp4-training](doc-concepts/nvfp4-training.md)
- [override-implementation-contract](doc-concepts/override-implementation-contract.md)
- [qwen3-5-hybrid-attention-family](doc-concepts/qwen3-5-hybrid-attention-family.md)
- [rl-batch-invariance-bitwise-parity](doc-concepts/rl-batch-invariance-bitwise-parity.md)
- [rl-dapo-math-recipe](doc-concepts/rl-dapo-math-recipe.md)
- [rl-search-r1-multiturn-tool-use](doc-concepts/rl-search-r1-multiturn-tool-use.md)
- [rl-typed-metrics-reduction](doc-concepts/rl-typed-metrics-reduction.md)
- [rl-verifiers-integration](doc-concepts/rl-verifiers-integration.md)
- [rl-windowed-fifo-scheduling](doc-concepts/rl-windowed-fifo-scheduling.md)
- [sdc-replay-detection](doc-concepts/sdc-replay-detection.md)
- [simple-fsdp](doc-concepts/simple-fsdp.md)
- [structured-trace-logging](doc-concepts/structured-trace-logging.md)
- [titanrl-architecture](doc-concepts/titanrl-architecture.md)
- [titanrl-rollouter-api](doc-concepts/titanrl-rollouter-api.md)
- [torchft-replica-group-fault-tolerance](doc-concepts/torchft-replica-group-fault-tolerance.md)
- [torchft-semi-sync-diloco](doc-concepts/torchft-semi-sync-diloco.md)
- [torchtitan-tpu-distribution](doc-concepts/torchtitan-tpu-distribution.md)
- [tpu-defer-and-fuse-eager-mode](doc-concepts/tpu-defer-and-fuse-eager-mode.md)
- [tpu-dispatch-bound-mental-model](doc-concepts/tpu-dispatch-bound-mental-model.md)
- [tpu-fused-linear-cross-entropy](doc-concepts/tpu-fused-linear-cross-entropy.md)
- [tpu-graph-trainer-memory-policies](doc-concepts/tpu-graph-trainer-memory-policies.md)
- [tpu-launch-and-profiling-workflow](doc-concepts/tpu-launch-and-profiling-workflow.md)
- [tpu-libtpu-xla-flag-layering](doc-concepts/tpu-libtpu-xla-flag-layering.md)
- [tpu-moe-kernel-switches](doc-concepts/tpu-moe-kernel-switches.md)
- [tpu-multislice-hsdp-over-dcn](doc-concepts/tpu-multislice-hsdp-over-dcn.md)
- [tpu-non-colocated-rl-ray](doc-concepts/tpu-non-colocated-rl-ray.md)
- [tpu-per-block-torch-compile](doc-concepts/tpu-per-block-torch-compile.md)
- [tpu-recipe-libtpu-flag-sets](doc-concepts/tpu-recipe-libtpu-flag-sets.md)
- [tpu-recipe-mamba-256k-long-context](doc-concepts/tpu-recipe-mamba-256k-long-context.md)
- [tpu-recipe-matrix](doc-concepts/tpu-recipe-matrix.md)
- [tpu-recipe-memory-policy-and-save-regions](doc-concepts/tpu-recipe-memory-policy-and-save-regions.md)
- [tpu-recipe-precision-and-throughput-accounting](doc-concepts/tpu-recipe-precision-and-throughput-accounting.md)
- [tpu-recipe-simplefsdp-schedules](doc-concepts/tpu-recipe-simplefsdp-schedules.md)
- [tpu-recipe-splash-and-loss-kernel-choices](doc-concepts/tpu-recipe-splash-and-loss-kernel-choices.md)
- [tpu-scan-graph-splitter-cpu-offload](doc-concepts/tpu-scan-graph-splitter-cpu-offload.md)
- [tpu-simplefsdp-and-mixed-precision](doc-concepts/tpu-simplefsdp-and-mixed-precision.md)
- [tpu-splash-attention-tiles-and-vmem](doc-concepts/tpu-splash-attention-tiles-and-vmem.md)
- [transformers-modeling-backend](doc-concepts/transformers-modeling-backend.md)
- [vllm-otel-engine-metrics](doc-concepts/vllm-otel-engine-metrics.md)

## Coverage
Two tiers: **concept pages** explain mechanisms deeply (selective); the **symbol
index** represents the rest so the whole repo is navigable. Coverage is a
set-difference over the SCIP symbol table, not a graph walk — every documentable
symbol is enumerated and represented.

- documentable symbols: **14209** across 690 modules
- deep (concept pages): **1355** (9.5%)
- index-only: **12854**
- represented total: **14209** (100.0%)
- classes represented: **1497/1497**

[`catalog/index.md`](catalog/index.md) maps every module; `catalog/symbols/*.tsv` and `catalog/edges/*.tsv` are the greppable symbol index; per-module pages under `catalog/` are a rendering of it (tier `full`).

## Provenance
`extracted` = from SCIP / source. `inferred` = LLM judgment, treat as such.
Design-intent dynamics are labeled; none are runtime-measured (no L4 pass run).
Callers/callees are reference-scoped (SCIP has no call role), labeled "calls/refs".
