---
title: TorchFT semi-synchronous training (DiLoCo / Local SGD)
type: doc-concept
provenance: doc
source: torchtitan/experiments/torchft/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TorchFT semi-synchronous training (DiLoCo / Local SGD)

## Definition
Semi-synchronous training lets TorchFT replica groups ("islands") train independently and synchronize weights only every N steps instead of all-reducing gradients every step. Two algorithms are supported: **Local SGD** (periodic parameter averaging) and **(Streaming) DiLoCo** (an inner optimizer per island plus an outer Nesterov-SGD step on the averaged pseudo-gradient, optionally per model fragment with staggered sync).

## In torchtitan (grounded)
- Selector: [`TorchFTManager.Config.semi_sync_method`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.semi_sync_method) (`None`, `"local_sgd"`, `"diloco"`); [`maybe_semi_sync_training`](../catalog/torchtitan/experiments/torchft/manager.md#maybe_semi_sync_training) returns the torchft `LocalSGD` / `DiLoCo` context manager wrapping [`FaultTolerantTrainer.train`](../catalog/torchtitan/experiments/torchft/trainer.md#FaultTolerantTrainer.train). For DiLoCo it builds one outer `SGD(lr=0.7, momentum=0.9, nesterov=True)` per fragment.
- Extended config [`FaultTolerance`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance): [`sync_steps`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.sync_steps) (default 5), [`should_quantize`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.should_quantize) (quantize before all-reduce), [`fragment_sync_delay`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.fragment_sync_delay) (Streaming DiLoCo "tau"), [`fragment_update_alpha`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.fragment_update_alpha), [`module_fqns_per_model_fragment`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.module_fqns_per_model_fragment), [`num_fragments`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerance.num_fragments).
- Fragmenting: models opt in via [`FaultTolerantModelSpec.fragment_fn`](../catalog/torchtitan/experiments/torchft/config/job_config.md#FaultTolerantModelSpec.fragment_fn); the LLM implementation is [`fragment_llm`](../catalog/torchtitan/experiments/torchft/diloco/utils.md#fragment_llm) / [`module_split`](../catalog/torchtitan/experiments/torchft/diloco/utils.md#module_split).
- The debug recipe [`llama3_torchft_debugmodel`](../catalog/torchtitan/experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel) enables DiLoCo by default (`sync_steps=10`, `num_fragments=2`).

## Why it matters / when it applies
- **Token accounting:** `--training.num_tokens_per_train_step` is the **global** budget across all islands; each island's inner token count is that divided by the number of replica groups, and the number of fwd/bwd iterations accumulated per optimizer step is derived from it.
- Communication/quality trade-offs called out in the config docstrings: `fragment_sync_delay > 0` improves comm/compute overlap but can hurt model quality; `should_quantize` saves bandwidth at the cost of GPU work and extra collectives; `fragment_update_alpha` mixes local and global parameters (0 = take global).
- **Semantics caution for perf work:** DiLoCo/Local SGD change the optimization algorithm, so a step-time gain from switching to them is not a like-for-like speedup under this wiki's rules.
- **TPU relevance.** None at this commit (torchft process groups are gloo/NCCL). Conceptually it targets the same slow cross-island links as DCN between TPU slices.

**Doc vs code at this commit:** the README's "Example 2" commands never pass `--fault_tolerance.semi_sync_method`; semi-sync happens only because the debug config hard-codes `semi_sync_method="diloco"`. The base fields (`semi_sync_method`, `group_size`, ...) live on `TorchFTManager.Config` in `manager.py`; `config/job_config.py` only adds the DiLoCo extensions.

## Connections
- Code concepts: [trainer-and-train-loop](../concepts/trainer-and-train-loop.md), [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md), [model-spec-protocols](../concepts/model-spec-protocols.md)
- Module catalogs: [torchft/manager](../catalog/torchtitan/experiments/torchft/manager.md), [torchft/config/job_config](../catalog/torchtitan/experiments/torchft/config/job_config.md), [torchft/diloco/utils](../catalog/torchtitan/experiments/torchft/diloco/utils.md)
- Related doc-concepts: [torchft-replica-group-fault-tolerance](torchft-replica-group-fault-tolerance.md), [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md)

## Source
Extracted from `torchtitan/experiments/torchft/README.md` (kept in place).
