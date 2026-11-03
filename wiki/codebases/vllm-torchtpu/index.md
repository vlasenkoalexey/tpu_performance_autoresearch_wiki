---
slug: vllm-torchtpu
commit: bf318e424febf494c5a1d6cb0104038548888c4b
scip_tool: scip-python
updated: 2026-11-03
okf_version: "0.2"
sources:
  - {resource: ../../../raw/code/vllm-torchtpu, title: vllm-torchtpu @ bf318e424f}
---

# vllm-torchtpu internals wiki

Generated, grounded wiki. Start from a concept (or an area); drill into cited symbols.
The commit pin above is the single source version for every page in this silo.

**Start here → [Overview](overview.md)** — vllm-project/vllm-torchtpu at commit bf318e424: the out-of-tree vLLM TPU platform plugin that serves vLLM's PyTorch models on TorchTPU (torch_tpu) by precompiling one program per token bucket and calling JAX/Pallas kernels for paged attention, MLA, Gated DeltaNet, fused MoE and quantized matmul, with 6D parallelism, disaggregated prefill/decode and host KV offload.

## Areas
One page per top-level area: what it is for, the units inside it with their entry points, and the small units that have no page of their own.
- [compilation](areas/compilation.md) — The TorchTPU compile backend vLLM calls once per (subgraph, token bucket): it lowers the captured FX graph to one PjRt executable per bucket, keys and persists the AOT cache, and keeps trace-time shape decisions correct per bucket.
- [core](areas/core.md) — Narrow scheduler extensions for TPU serving: time-budgeted pipeline-parallel prefill chunking, a lazy-push engine stepper for deep pipelines, opt-in admission policies, and scheduler-init patches for disaggregated prefill/decode.
- [distributed](areas/distributed.md) — Process groups, op-local JAX meshes and transport for multi-device TPU serving: 6D parallelism (TP/DP/PP/EP/PCP/DCP), pipeline-stage hand-off, multi-host bootstrap, and the KV-transfer connector for prefill/decode disaggregation.
- [executors](areas/executors.md) — vLLM executor subclasses the TPU platform selects to spawn and drive one TPU worker per device: a multiprocess executor for single-host and non-Ray multi-host runs, and Ray V1/V2 executors for Ray multi-host slices.
- [experimental](areas/experimental.md) — Ahead-of-time exporter that lowers a vllm serve configuration into a shard-local StableHLO serving directory, plus a launcher that hands that artifact to an external Rust runtime with no Python in the serving process.
- [kernels](areas/kernels.md) — The repo's Pallas TPU kernel library: ragged paged attention (standard, MLA, sparse, PCP ring, batched), fused and decode-specialized MoE, Gated DeltaNet, DeepSeek-V4 and Kimi-K3 model kernels, SparseCore gather/top-k, quantized matmul and KV-pool utilities.
- [layers](areas/layers.md) — The seam between vLLM's torch model code and the JAX/Pallas kernels: per-step attention metadata and shard_map wrappers (core), the Pallas attention backends, quantization methods and custom-op registrations (adapter), and the TPU samplers.
- [lora](areas/lora.md) — Multi-LoRA serving inside the compiled TPU backbone: a Punica wrapper whose shrink/expand ops compute every adapter slot with a one-hot mask, and LoRA managers that write an adapter into its HBM slot with one precompiled program.
- [megakernel](areas/megakernel.md) — A self-contained JAX + Pallas library for a decode megakernel: one Pallas kernel per step that runs every layer and streams weights through VMEM rings, declared from composable modules and planned at build time, with a unified fp8 KV/recurrent-state pool.
- [models](areas/models.md) — TPU-native model implementations and in-place patches for vLLM's model registry: DeepSeek-V4, Kimi-Linear/K3 and Qwen4Exp, upstream-class patches for Qwen families, and the process-global wrapper context that lets kernels find the mesh and KV cache.
- [offload](areas/offload.md) — Host-DRAM offload of vLLM prefix-cache KV blocks on TPU: a controller-driven OffloadingConnector backed by a C++ KV store that owns the directory, LRU, pins and DMAs, with TPU workers acting as passive DMA endpoints.
- [omni](areas/omni.md) — vLLM-Omni platform for TPU: a platform subclass that combines vLLM-Omni's OmniPlatform with TpuPlatform and applies run-once performance patches for diffusion transformers (Wan2.2, LTX-2, Qwen-Image), plus diffusion attention and RoPE hooks and a TPU profiler.
- [platforms](areas/platforms.md) — vLLM platform plugin entry for TorchTPU: TpuPlatform, a startup-time config compiler that rewrites a GPU-shaped vLLM config into a TPU-servable one (compile mode, token-bucket ladder, dtype, executor, backends) and validates PP/PCP support.
- [runner](areas/runner.md) — TPUModelRunner and its managers: drives every forward at a padded shape from a precompiled bucket ladder, chunks oversized steps, prepares inputs on the host, and owns KV cache materialization, sampling, speculative-decoding and multimodal-encoder orchestration.
- [spec_decode](areas/spec_decode.md) — TPU speculative-decoding drafters (Eagle3/MTP autoregressive heads and DFlash/DSpark block-diffusion drafters), built to keep every draft-path shape stable so drafting never triggers a recompile.
- [structured_decoding](areas/structured_decoding.md) — Grammar-constrained decoding on TPU: a runner-owned manager that stages vLLM's grammar bitmask in pinned host buffers and applies it to padded logits, including speculative target and bonus rows, inside one fixed-shape compiled region.
- [tools](areas/tools.md) — Offline profiling utility: merges a multi-chip run's per-rank xplane trace captures into a single XSpace file, renumbering device planes and deduplicating host metadata.
- [tracing](areas/tracing.md) — Shared profiler vocabulary: TraceAnnotation regions that cost nothing unless a profiler is recording and label each step with batch metadata, plus resolution of vLLM start_profile requests into TorchTPU trace directories and options.
- [worker](areas/worker.md) — TPUWorker, the per-device vLLM worker: binds its rank to one TPU chip, bootstraps distributed state, sizes the KV budget from a profile run, and forwards execute, sample, pipeline, LoRA, profiling and kernel-reload calls to the model runner.

## Concepts (deep)
Grouped by the source area each page's citations point into.

### `src/vllm_torchtpu`
| Concept | Description | Status |
|---|---|---|
| [kv-cache-layout-and-hbm-budget](concepts/kv-cache-layout-and-hbm-budget.md) | How the TPU plugin decides how many bytes a KV page really costs (lane/packing padding, hybrid GDN state fit), how many blocks fit in HBM (gpu_memory_utilization cap minus resident bytes minus post-profile reserves), and how the pages are materialized as per-layer caches, a shared attention cache, the unified hybrid pool, or a block-major pool; read it when sizing KV capacity, chasing a KV-init OOM, or touching any consumer of pool geometry (kernels, offload, Raiden transfer). | fresh |

### `src/vllm_torchtpu/compilation`
| Concept | Description | Status |
|---|---|---|
| [compilation-and-graph-capture](concepts/compilation-and-graph-capture.md) | How vllm-torchtpu compiles vLLM's captured FX graph into one TPU PjRt executable per token bucket - the compiler adaptor's compile/load path and its bundled on-disk artifacts, the TPU compilation hash that keys every cache, peer replay of compiled buckets across a host's ranks, per-bucket re-tracing when a model branches on the token count (shape_variants), trace-first deferred precompile, and TPU_KERNEL_ITER_MODE kernel hot-reload. Read when startup/precompile is slow, a warm start unexpectedly recompiles, or a model fails with ShapeSpecializationError. | fresh |

### `src/vllm_torchtpu/core`
| Concept | Description | Status |
|---|---|---|
| [tpu-schedulers](concepts/tpu-schedulers.md) | How the plugin's core/ package bends vLLM's v1 scheduler and engine-core step loop for TPU - sizing pipeline-parallel prefill chunks against a profiled per-step time model, a lazy-push engine loop that keeps deep pipelines busy without empty steps, opt-in SRPT and prefix-aware admission, a DP-aligned prefill scheduler, and scheduler patches for disaggregated serving; read it when tuning PP/DP throughput or TTFT, or when a scheduler choice is silently disabled. | fresh |

### `src/vllm_torchtpu/distributed`
| Concept | Description | Status |
|---|---|---|
| [distributed-parallelism-and-meshes](concepts/distributed-parallelism-and-meshes.md) | How vllm-torchtpu composes TP, DP, EP, PCP, DCP and PP on TPU - one worker per device with torch.distributed collectives, plus op-local multi-device JAX meshes (EP, PCP, DCP, stage, PP) for Pallas kernels, their device-order rules, the sharded_jax_op bridge, the pipeline wave/ring hand-off, the TPU device communicator and multi-host bootstrap; read before choosing a parallelism layout or debugging a mesh / DeviceAssignment error. | fresh |

### `src/vllm_torchtpu/distributed/kv_transfer`
| Concept | Description | Status |
|---|---|---|
| [kv-transfer-and-disaggregated-serving](concepts/kv-transfer-and-disaggregated-serving.md) | How vllm-torchtpu moves prefill KV cache from a kv_producer engine to a kv_consumer engine - the ZMQ/shared-memory pull transport, the Raiden legacy pull, and the controller-planned Raiden Stage-3 resharding path - plus the completion, failure, NaN-check and metrics contracts; read before deploying or profiling prefill/decode disaggregation on TPU. | fresh |

### `src/vllm_torchtpu/experimental/export`
| Concept | Description | Status |
|---|---|---|
| [model-export-and-rust-launcher](concepts/model-export-and-rust-launcher.md) | How the experimental exporter turns a vLLM model into a Python-free serving artifact (per-bucket shard-local StableHLO modules, metadata.json, Orbax weights) and how the Rust launcher wraps the `vllm serve` command line around it; read when you need to know what an exported artifact bakes in, how KV capacity and buckets are fixed, or why a `vllm serve` flag is rejected. | fresh |

### `src/vllm_torchtpu/kernels/deepseek_v4/compress_and_store`
| Concept | Description | Status |
|---|---|---|
| [deepseek-v4-compress-and-store-kernel](concepts/deepseek-v4-compress-and-store-kernel.md) | How the DSv4 KV compressor runs on TPU as two Pallas kernels - proj_and_save_state (per-token f32 KV+score state written into the paged cache) and compress_norm_rope_store (windowed-softmax compression, RMSNorm, RoPE, FP8 packing and paged store for boundary tokens) - across the HCA, CSA and CSA-indexer storage modes, including the page geometry, the state/KV buffer overlay and the SEQ_ALONG_LANE indexer layout. Read before touching DSv4 cache geometry, compressor block sizes, or profiling the compressor. | fresh |

### `src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk`
| Concept | Description | Status |
|---|---|---|
| [deepseek-v4-streamindex-topk-kernel](concepts/deepseek-v4-streamindex-topk-kernel.md) | How the sparse-attention indexer picks each query's top-k compressed KV positions on TPU - the streamindex_topk Pallas scoring pipeline (decode/verify/mixed passes, relu(q.k) weighted over heads, FP8 keys with UE8M0 scales), the SEQ_ALONG_LANE vs HEAD_ALONG_SUBLANE packed cache layouts, chunked TensorCore/SparseCore overlap, the DCP-sharded exact global top-k, and the granule-based KV-append writer. Read before tuning indexer block sizes, choosing VLLM_TPU_INDEXER_KV_CACHE_MODE, or profiling the indexer. | fresh |

### `src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe`
| Concept | Description | Status |
|---|---|---|
| [adaptive-fused-moe-kernel](concepts/adaptive-fused-moe-kernel.md) | How kernels/experimental/adaptive_fused_moe differs from the production fused_ep_moe_v2 kernel - separate gate/up (W1) and down (W2) weight rings sized once against VMEM, a W2 DMA that hides under the W1 matmul, softmax-only always-sharded routing, and a strict serving bridge (MOE_FUSED_EP_KERNEL_IMPL=adaptive) that raises instead of falling back. Read when choosing between the two fused-EP MoE paths or when a large expert shape does not fit VMEM. | fresh |

### `src/vllm_torchtpu/kernels/experimental/batched_rpa`
| Concept | Description | Status |
|---|---|---|
| [batched-ragged-paged-attention-kernel](concepts/batched-ragged-paged-attention-kernel.md) | How the experimental batched RPA Pallas kernel turns a ragged decode/prefill batch into a precomputed SMEM DMA schedule and runs B (query-block, KV-block) tiles per pipeline step; read before tuning block sizes, KV layout, or context-parallel attention on the CUSTOM attention backend. | fresh |

### `src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused`
| Concept | Description | Status |
|---|---|---|
| [gdn-pcp-fused-kernel](concepts/gdn-pcp-fused-kernel.md) | How the experimental gdn_pcp_fused Pallas kernel fuses the QKVZ projection, the PCP token-to-head remote-DMA exchange and the GDN v3 conv1d + delta-rule pipeline into one call for pooled PCP prefill; read before touching GDN PCP prefill performance, its stage metadata, or the unified-pool state write-back. | fresh |

### `src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa`
| Concept | Description | Status |
|---|---|---|
| [pcp-streaming-rpa-kernel](concepts/pcp-streaming-rpa-kernel.md) | How vllm-torchtpu runs long-prefill attention under prefill context parallelism (PCP): rank-major token packing, a page-striped KV cache, a compact JAX tile plan, and a split current/history pair of Pallas ring kernels that stream KV pages between ranks and fuse the KV-cache write into the ring. Read before touching PCP prefill, cp_kv_cache_interleave_size, or the PCP compile buckets. | fresh |

### `src/vllm_torchtpu/kernels/fused_moe/v2`
| Concept | Description | Status |
|---|---|---|
| [fused-moe-kernels](concepts/fused-moe-kernels.md) | How kernels/fused_moe/v2 runs a whole MoE layer under expert parallelism as one shard_map program - in-kernel top-k routing, a host-built routing plan, a Pallas kernel that streams expert weights through a VMEM ring, computes the FFN per tile and pushes each result row by remote DMA to the token's owner, and a Pallas combine. Read before tuning MoE under EP, adding a weight format, or diagnosing VMEM refusals and MoE step time. | fresh |

### `src/vllm_torchtpu/kernels/gdn/v3`
| Concept | Description | Status |
|---|---|---|
| [gated-deltanet-kernels](concepts/gated-deltanet-kernels.md) | How the GDN v3 Pallas kernel fuses the causal short Conv1D and the Gated DeltaNet (or Kimi Delta Attention) recurrence into one ragged, double-buffered pipeline over decode/verify and prefill/mixed segments, how its tile sizes and VMEM budget are chosen, how state checkpoints back speculative decoding, and how GDN heads are sharded across TP/PCP ranks. Read before tuning GDN tile sizes, touching the hybrid state pool, or debugging GDN numerics. | fresh |

### `src/vllm_torchtpu/kernels/kimi_k3`
| Concept | Description | Status |
|---|---|---|
| [kimi-k3-kernels](concepts/kimi-k3-kernels.md) | How the kernels under kernels/kimi_k3 work - the three-ring bidirectional BF16 all-gather / reduce-scatter over a 2x2x4 slice, the matmul-fused ring variants for KDA and MLA, the packed MoE-input gather, the Block Attention Residual kernel, and the standalone KDA decode / chunked-prefill kernels; read when profiling K3 prefill collectives or porting these kernels. | fresh |

### `src/vllm_torchtpu/kernels/mla`
| Concept | Description | Status |
|---|---|---|
| [mla-attention-kernels](concepts/mla-attention-kernels.md) | How kernels/mla serves Multi-head Latent Attention on TPU - the dense v2 ragged paged attention kernel with its tuned-params table, the sparse (DeepSeek Sparse Attention) gather-then-attend kernel with SparseCore gathers over a split NOPE/ROPE fp8 cache, the opt-in masked-dense router, and the cache writers (including DCP). Read before tuning MLA block sizes, changing the sparse cache layout, or debugging MLA perf. | fresh |

### `src/vllm_torchtpu/kernels/ragged_paged_attention/v3`
| Concept | Description | Status |
|---|---|---|
| [ragged-paged-attention-kernel](concepts/ragged-paged-attention-kernel.md) | How the default Pallas ragged paged attention kernel serves mixed prefill/decode batches against the paged KV cache - KV packing layout, the decode/prefill/mixed three-pass split, the double-buffered DMA pipeline that fuses the KV-cache write into attention, the head_dim=64 variant, block-size heuristics and the bundled block-major entry; read before tuning attention block sizes or reading an RPA profile. | fresh |

### `src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2`
| Concept | Description | Status |
|---|---|---|
| [sparsecore-ragged-gather-scatter](concepts/sparsecore-ragged-gather-scatter.md) | How vllm-torchtpu moves MoE tokens on the TPU SparseCore - the ragged_gather_v2 dispatch kernel, the three ragged_gather_reduce combine kernels (v1, v2, destination-major v3), ragged_scatter, the shared pl.kernel launcher, and the knobs that pick between them; read before touching MoE permute/unpermute performance. | fresh |

### `src/vllm_torchtpu/layers/adapter`
| Concept | Description | Status |
|---|---|---|
| [vllm-layer-adapters](concepts/vllm-layer-adapters.md) | How the torch-facing adapter layer plugs TPU attention backends, quantization configs, MoE kernels, GDN/MLA ops and the rejection sampler into vLLM's v1 model classes, and why most of the work happens once at load time rather than per step; read this before changing a backend, a quant method or a MoE arming path. | fresh |

### `src/vllm_torchtpu/layers/adapter/custom_ops`
| Concept | Description | Status |
|---|---|---|
| [custom-ops](concepts/custom-ops.md) | How the plugin wraps JAX/Pallas kernels as torch custom ops (pallas.jax_op) with donated in-place state, fake implementations and config-named op caches, and how it swaps vLLM's MLA, GDN, KDA, DeepSeek-V4, MoE-runner and block-copy layers onto them; read this before adding or changing a kernel-backed layer. | fresh |

### `src/vllm_torchtpu/layers/adapter/quantization`
| Concept | Description | Status |
|---|---|---|
| [quantization-methods](concepts/quantization-methods.md) | How vllm-torchtpu swaps vLLM's GPU quantization configs for TPU ones, converts every checkpoint format (FP8 block, NVFP4, MXFP4, compressed-tensors INT4/MXFP4/FP8, BF16) into the few runtime layouts the TPU matmul and GMM kernels consume, and which env vars pick the runtime precision; read before touching quantized linear/MoE layers or tuning W8A8/W4A8/W4A16. | fresh |

### `src/vllm_torchtpu/layers/core`
| Concept | Description | Status |
|---|---|---|
| [attention-and-layer-core](concepts/attention-and-layer-core.md) | How the framework-neutral JAX layer core turns per-step runner state into AttentionMetadata and dispatches ragged paged attention, MLA, GDN, fused MoE and block quantization across the TPU mesh; read this before touching any attention/MoE call site or the metadata walk. | fresh |

### `src/vllm_torchtpu/megakernel`
| Concept | Description | Status |
|---|---|---|
| [megakernel](concepts/megakernel.md) | How the framework-free vllm_torchtpu.megakernel package describes a whole decode step as one fused Pallas megakernel - Modules composed into a ModelSpec, the ExecSpec/tiles execution config, the build-time planner that derives weight K-tiles, stream schedules and operand shapes, and the paged-pool backend it plugs in. Read before touching megakernel code, tuning its tiles/profiles, or estimating what a megakernel decode path would cost in VMEM. | fresh |

### `src/vllm_torchtpu/megakernel/pool`
| Concept | Description | Status |
|---|---|---|
| [megakernel-pool](concepts/megakernel-pool.md) | How the megakernel stores paged fp8 KV and recurrent (GatedDeltaNet conv + SSM) checkpoints in one per-attention-layer raw pool, how PoolLayout/CacheExec describe it, and how the gather_gdn_states and scatter_pool_states Pallas kernels move state in and out with double-buffered DMA pipelines. Read before changing pool geometry, pool-I/O modes (split / GPR / fused), checkpoint index formats, or debugging a corrupted hybrid-model cache. | fresh |

### `src/vllm_torchtpu/models/vllm`
| Concept | Description | Status |
|---|---|---|
| [vllm-model-patches](concepts/vllm-model-patches.md) | How src/vllm_torchtpu/models/vllm plugs TPU-specific models into vLLM - registering dedicated implementations (DeepSeek-V4, Kimi-K3, Qwen4Exp, DSpark and MTP drafts), monkey-patching upstream model classes for Qwen2 / Qwen3-VL / Qwen3.5, and the process-global VllmModelWrapperContext that hands the mesh, config and bundled KV cache to Pallas op builders; read when a model runs on TPU but behaves differently from upstream vLLM, or when adding a model. | fresh |

### `src/vllm_torchtpu/models/vllm/deepseek_v4`
| Concept | Description | Status |
|---|---|---|
| [deepseek-v4-model](concepts/deepseek-v4-model.md) | How the native DeepSeek-V4 model in models/vllm/deepseek_v4 is assembled for TPU inference - the deferred mHC post/pre fusion, the three lazily-built Pallas attention op variants (SWA / HCA / CSA) and their cache-keyed names, hash-MoE input-id gathering under DP, the optional intra-chip TP attention split, host-staged weight loading, and the DSpark speculative draft. Read before profiling or changing a DSv4 serving configuration. | fresh |

### `src/vllm_torchtpu/models/vllm/kimi_k3`
| Concept | Description | Status |
|---|---|---|
| [kimi-k3-model](concepts/kimi-k3-model.md) | How the dedicated TPU implementation of Kimi-Linear, Kimi-K3 and the K3 DSpark drafter is built - KDA vs MLA layer selection, pooled KDA state, latent MoE, load-time weight folding, and the opt-in TPU_K3_SP_PREFILL path that swaps generic collectives for fused ring kernels; read before profiling or tuning a Kimi-K3 deployment. | fresh |

### `src/vllm_torchtpu/offload`
| Concept | Description | Status |
|---|---|---|
| [host-offload](concepts/host-offload.md) | How vllm-torchtpu offloads prefix-cached KV blocks from TPU HBM to host DRAM (and optionally a POSIX storage tier or peer replicas) through a scheduler-driven Raiden KVCacheStore, and which configs control capacity, DMA granularity and safety; read before enabling --kv-offloading-size or VLLM_TPU_BLOCK_MAJOR_KV on TPU. | fresh |

### `src/vllm_torchtpu/omni`
| Concept | Description | Status |
|---|---|---|
| [omni-diffusion-support](concepts/omni-diffusion-support.md) | How vllm-torchtpu runs vLLM-Omni diffusion pipelines (Wan2.2, LTX-2, Qwen-Image, ...) on TPU - the OmniTpuPlatform plugin and its multi-rank worker setup, the Pallas flash / SDPA diffusion attention backends, the run-once model patches that remove recompiles, relayouts and fusion waste, and the TPU device profiler. Read before debugging an Omni diffusion run on TPU, adding a diffusion patch, or profiling a diffusion step. | fresh |

### `src/vllm_torchtpu/platforms`
| Concept | Description | Status |
|---|---|---|
| [tpu-platform](concepts/tpu-platform.md) | How vllm-torchtpu plugs into vLLM as an out-of-tree platform - the entry point, the one-shot check_and_update_config rewrite that turns a vLLM config into a TPU-servable one (token-bucket compile sizes, no graph splitting, bf16, executor and TORCH_TPU_* bootstrap env, PCP/PP validation), multihost topology lookup, and the KV block-size / slot derivation. Read before changing any launch flag, env var or parallelism setting, or when a server fails at startup with a config error. | fresh |

### `src/vllm_torchtpu/runner`
| Concept | Description | Status |
|---|---|---|
| [tpu-model-runner](concepts/tpu-model-runner.md) | How TPUModelRunner maps vLLM's v1 GPUModelRunner contract onto TorchTPU - token and request padding buckets, the per-forward request caps that split one scheduler step into several forwards, the execute_model / sample_tokens split, and the profile_run + capture_model warmup that precompiles every bucket; read it before touching input prep, bucket sizing, or anything that could cause a serving-time recompile. | fresh |

### `src/vllm_torchtpu/spec_decode`
| Concept | Description | Status |
|---|---|---|
| [speculative-decoding](concepts/speculative-decoding.md) | How the spec_decode subsystem drafts K tokens per request on TorchTPU - the Eagle3/MTP autoregressive proposer, the DFlash/DSpark parallel block proposer, and the bucketing, compile-region and EP-DP lockstep tricks that keep drafting from recompiling or deadlocking; read before touching draft code, draft parallelism, or the spec-decode warmup. | fresh |

### `src/vllm_torchtpu/tracing`
| Concept | Description | Status |
|---|---|---|
| [tracing-annotations](concepts/tracing-annotations.md) | How vllm-torchtpu labels host-side regions in TorchTPU / Kineto profiler traces - the profiler-gated TraceAnnotation context manager and its name#k=v# metadata encoding, the request-id and KV-length labels the model runner attaches to every ModelForward region, the PP / KV-transfer / structured-decoding annotation vocabulary, and how start_profile options (profile_prefix strings, profiler_kwargs, env defaults) resolve into tracer levels and TPU trace modes. Read before capturing an xprof trace of a vLLM server or adding a new annotated region. | fresh |

## Doc-derived concepts
Concepts extracted from the project's own docs (README / `docs/`), grounded to the symbol catalog. The source docs stay in place.
- [benchmark-harness-and-regression-gates](doc-concepts/benchmark-harness-and-regression-gates.md)
- [ci-test-markers-and-pipelines](doc-concepts/ci-test-markers-and-pipelines.md)
- [compilation-cache-and-warmup](doc-concepts/compilation-cache-and-warmup.md)
- [composable-6d-parallelism](doc-concepts/composable-6d-parallelism.md)
- [context-parallelism-pcp-dcp](doc-concepts/context-parallelism-pcp-dcp.md)
- [decode-capacity-preemption-abort](doc-concepts/decode-capacity-preemption-abort.md)
- [derive-dont-declare](doc-concepts/derive-dont-declare.md)
- [disaggregated-pd-trace-correlation](doc-concepts/disaggregated-pd-trace-correlation.md)
- [dp-ep-moe-layouts](doc-concepts/dp-ep-moe-layouts.md)
- [env-var-reference-by-subsystem](doc-concepts/env-var-reference-by-subsystem.md)
- [env-var-registry-and-compile-key](doc-concepts/env-var-registry-and-compile-key.md)
- [fail-fast-and-fallback-policy](doc-concepts/fail-fast-and-fallback-policy.md)
- [generic-quantization-machinery](doc-concepts/generic-quantization-machinery.md)
- [gke-multihost-jobset-deployment](doc-concepts/gke-multihost-jobset-deployment.md)
- [kernel-hardware-resource-rules](doc-concepts/kernel-hardware-resource-rules.md)
- [load-time-requantization](doc-concepts/load-time-requantization.md)
- [multi-lora-inference](doc-concepts/multi-lora-inference.md)
- [multi-rank-trace-capture](doc-concepts/multi-rank-trace-capture.md)
- [multihost-execution-backends](doc-concepts/multihost-execution-backends.md)
- [multimodal-encoder-inference](doc-concepts/multimodal-encoder-inference.md)
- [offline-inference-example](doc-concepts/offline-inference-example.md)
- [offline-shape-profiling](doc-concepts/offline-shape-profiling.md)
- [perf-evidence-standard](doc-concepts/perf-evidence-standard.md)
- [phased-profiler](doc-concepts/phased-profiler.md)
- [pipeline-parallel-stage-handoff](doc-concepts/pipeline-parallel-stage-handoff.md)
- [plugin-architecture-and-kernel-bridge](doc-concepts/plugin-architecture-and-kernel-bridge.md)
- [plugin-packaging-and-registration](doc-concepts/plugin-packaging-and-registration.md)
- [profile-cache-and-free-hbm-probe](doc-concepts/profile-cache-and-free-hbm-probe.md)
- [pyrefly-baseline-type-checking](doc-concepts/pyrefly-baseline-type-checking.md)
- [raiden-pd-disaggregation](doc-concepts/raiden-pd-disaggregation.md)
- [roadmap-q4-2026](doc-concepts/roadmap-q4-2026.md)
- [server-side-profiling-and-trace-options](doc-concepts/server-side-profiling-and-trace-options.md)
- [spec-bench-harness](doc-concepts/spec-bench-harness.md)
- [speculative-decoding-methods](doc-concepts/speculative-decoding-methods.md)
- [supported-models-and-feature-matrix](doc-concepts/supported-models-and-feature-matrix.md)
- [token-padding-buckets](doc-concepts/token-padding-buckets.md)
- [tpu-generations-and-logical-devices](doc-concepts/tpu-generations-and-logical-devices.md)
- [tpu-kernel-library-map](doc-concepts/tpu-kernel-library-map.md)
- [tpu-patch-registry](doc-concepts/tpu-patch-registry.md)
- [tpu-quantization-formats](doc-concepts/tpu-quantization-formats.md)
- [tuned-block-size-tables](doc-concepts/tuned-block-size-tables.md)
- [v6e-serving-recipe-matrix](doc-concepts/v6e-serving-recipe-matrix.md)
- [v7x-serving-recipe-matrix](doc-concepts/v7x-serving-recipe-matrix.md)
- [weight-load-time-preprocessing](doc-concepts/weight-load-time-preprocessing.md)
- [xplane-session-merge-tool](doc-concepts/xplane-session-merge-tool.md)

## Coverage
Two tiers: **concept pages** explain mechanisms deeply (selective); the **symbol
index** represents the rest so the whole repo is navigable. Coverage is a
set-difference over the SCIP symbol table, not a graph walk — every documentable
symbol is enumerated and represented.

- documentable symbols: **10190** across 376 modules
- deep (concept pages): **1504** (14.8%)
- index-only: **8686**
- represented total: **10190** (100.0%)
- classes represented: **480/480**

[`catalog/index.md`](catalog/index.md) maps every module; `catalog/symbols/*.tsv` and `catalog/edges/*.tsv` are the greppable symbol index; per-module pages under `catalog/` are a rendering of it (tier `full`).

## Provenance
`extracted` = from SCIP / source. `inferred` = LLM judgment, treat as such.
Design-intent dynamics are labeled; none are runtime-measured (no L4 pass run).
Callers/callees are reference-scoped (SCIP has no call role), labeled "calls/refs".
