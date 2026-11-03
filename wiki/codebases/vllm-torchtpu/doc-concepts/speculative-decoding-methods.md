---
title: Speculative decoding methods on TPU (EAGLE-3, MTP, DFlash, DSpark, n-gram)
type: doc-concept
provenance: doc
source: docs/user_guide/speculative_decoding.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Speculative decoding methods on TPU (EAGLE-3, MTP, DFlash, DSpark, n-gram)

## Definition
Speculative decoding proposes `K` draft tokens per step and verifies them in one target
forward pass, cutting median TPOT and end-to-end latency. The guide enables it through
the normal vLLM `--speculative-config` JSON and lists five methods: **EAGLE-3**
(`eagle3`, separate draft checkpoint, high acceptance on chat/code/reasoning), **MTP**
(`mtp`, the checkpoint's own multi-token-prediction heads - Qwen3.5, DeepSeek-V3/R1,
GLM-5 - no external draft), **DFlash** (`dflash`, block-diffusion draft heads proposing
up to 16 tokens in one forward), **n-gram** (`ngram`, prompt lookup, no draft model) and
**suffix decoding** (`suffix`, suffix tree over prompt and prior responses).

## In vllm-torchtpu (grounded)
- Drafter selection: [`TPUModelRunner._init_speculative_decoding`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._init_speculative_decoding)
  builds the drafter on the last pipeline stage only: `ngram` -> vLLM's `NgramProposer`,
  `dflash` -> [`DFlashProposer`](../catalog/src/vllm_torchtpu/spec_decode/dflash.md#DFlashProposer),
  `dspark` -> [`DSparkProposer`](../catalog/src/vllm_torchtpu/spec_decode/dspark.md#DSparkProposer),
  any EAGLE-family method (`eagle3`, `mtp`) -> [`Eagle3Proposer`](../catalog/src/vllm_torchtpu/spec_decode/eagle3.md#Eagle3Proposer);
  **anything else raises `NotImplementedError`**.
- Proposing and verify plumbing: [`SpeculativeDecodingManager.propose_draft_token_ids`](../catalog/src/vllm_torchtpu/runner/speculative_decoding_manager.md#SpeculativeDecodingManager.propose_draft_token_ids)
  (n-gram drafts on host; EAGLE-3 / MTP / DFlash are "async drafters" that can seed and
  return drafts on device), [`SpecDecodeMetadata`](../catalog/src/vllm_torchtpu/runner/speculative_decoding_manager.md#SpecDecodeMetadata).
- MTP fast path: [`MtpDraftModel`](../catalog/src/vllm_torchtpu/spec_decode/mtp_fused_loop.md#MtpDraftModel)
  compiles draft steps 1..K-1 into one program (positions, seq_lens and input ids advance
  on device), replacing two host dispatches plus a metadata build per step.
- DSpark ([`DSparkProposer`](../catalog/src/vllm_torchtpu/spec_decode/dspark.md#DSparkProposer)):
  a DFlash-style parallel block forward followed by a small sequential Markov head; the
  module docstring scopes it as a PoC with greedy draft sampling only.
- Verify windows of `1 + K` tokens are placed first in the batch so attention can use a
  static query length ([`static_verify_q_len`](../catalog/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#static_verify_q_len)).
- The spec config (`model`, `draft_tensor_parallel_size`, `num_speculative_tokens`) is a
  compile-cache-key factor ([`compute_tpu_compilation_hash`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#compute_tpu_compilation_hash)).

## Doc-vs-code disagreements
- **Suffix decoding** is listed with a launch example, but the runner at this commit has
  no branch for `method="suffix"` and raises `NotImplementedError` ("Unsupported
  speculative decoding method").
- **DSpark** is implemented (and validated per the supported-models page on
  DeepSeek-V4-Flash and Qwen3-4B) but absent from the speculative-decoding guide.
- Combination limits not in the guide: under PCP only MTP with
  `num_speculative_tokens=1` is accepted
  ([`PcpStaticSupportValidator.validate_platform_config`](../catalog/src/vllm_torchtpu/platforms/pcp_validation.md#PcpStaticSupportValidator.validate_platform_config));
  under PP only prefill-only MTP (`K=1`) on a KV producer
  ([`validate_pipeline_parallel_config`](../catalog/src/vllm_torchtpu/platforms/pp_validation.md#validate_pipeline_parallel_config));
  n-gram is incompatible with async scheduling (vLLM config validation, noted in the
  manager).

## Why it matters / when it applies
- Speculation trades extra verify compute for fewer sequential decode steps; on TPU it
  helps most when decode is HBM-bandwidth bound at small batch.
- Draft-model methods add a draft forward per step: async drafters keep that on device,
  and the MTP fused loop removes most host dispatch overhead for `K > 1`.
- Changing `num_speculative_tokens` or the draft model recompiles (cache key).

## Connections
- Code concepts: [speculative-decoding](../concepts/speculative-decoding.md), [tpu-model-runner](../concepts/tpu-model-runner.md), [deepseek-v4-model](../concepts/deepseek-v4-model.md)
- Module catalogs: [eagle3](../catalog/src/vllm_torchtpu/spec_decode/eagle3.md), [dflash](../catalog/src/vllm_torchtpu/spec_decode/dflash.md), [dspark](../catalog/src/vllm_torchtpu/spec_decode/dspark.md), [mtp_fused_loop](../catalog/src/vllm_torchtpu/spec_decode/mtp_fused_loop.md), [speculative_decoding_manager](../catalog/src/vllm_torchtpu/runner/speculative_decoding_manager.md)
- Related doc-concepts: [supported-models-and-feature-matrix](supported-models-and-feature-matrix.md), [context-parallelism-pcp-dcp](context-parallelism-pcp-dcp.md), [pipeline-parallel-stage-handoff](pipeline-parallel-stage-handoff.md)

## Source
Extracted from `docs/user_guide/speculative_decoding.md` (kept in place).
