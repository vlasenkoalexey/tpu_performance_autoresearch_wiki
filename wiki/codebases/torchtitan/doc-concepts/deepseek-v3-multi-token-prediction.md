---
title: DeepSeek-V3 multi-token prediction (MTP) under CP/TP/SP/FSDP/EP
type: doc-concept
provenance: doc
source: torchtitan/models/deepseek_v3/MTP.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# DeepSeek-V3 multi-token prediction (MTP) under CP/TP/SP/FSDP/EP

## Definition
Multi-token prediction adds N extra decoder blocks ("MTP depths") after the main DeepSeek-V3
decoder. Depth k combines the previous depth's hidden state at each position with the embedding of
the token shifted by k, and is trained with an auxiliary cross-entropy against labels shifted by k.
TorchTitan follows the paper-style architecture (hidden state + shifted embedding per depth), not a
"shift only the loss" design, but derives all shifted inputs from the ordinary fixed-length batch
instead of a longer window.

## In torchtitan (grounded)
- Enabled by `num_mtp_layers=N` on [`model_registry`](../catalog/torchtitan/models/deepseek_v3/__init__.md#model_registry "torchtitan/models/deepseek_v3/__init__.py:L723");
  [`_build_mtp_layers`](../catalog/torchtitan/models/deepseek_v3/__init__.md#_build_mtp_layers "torchtitan/models/deepseek_v3/__init__.py:L304") derives
  MTP layer configs from the last main decoder layer. Example recipe:
  [`deepseek_v3_debugmodel_mtp`](../catalog/torchtitan/models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel_mtp "torchtitan/models/deepseek_v3/config_registry.py:L105")
  (one depth, [`ChunkedLossWrapper`](../catalog/torchtitan/components/loss.md#ChunkedLossWrapper "torchtitan/components/loss.py:L515")
  around [`MTPLoss`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPLoss) with default
  [`mtp_scale`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPLoss.mtp_scale) 0.3).
- [`DeepSeekV3Model`](../catalog/torchtitan/models/deepseek_v3/model.md#DeepSeekV3Model "torchtitan/models/deepseek_v3/model.py:L237") inherits
  [`MTPDecoder`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPDecoder "torchtitan/models/deepseek_v3/mtp.py:L170"); with empty
  [`mtp_layers`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPDecoder.mtp_layers "torchtitan/models/deepseek_v3/mtp.py:L212") its
  [`forward`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPDecoder.forward "torchtitan/models/deepseek_v3/mtp.py:L321") is the plain decoder.
  [`MTPDecoder.preprocess_inputs`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPDecoder.preprocess_inputs "torchtitan/models/deepseek_v3/mtp.py:L224")
  builds per-depth token/label pairs before CP sharding.
- Each [`MTPTransformerBlock`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPTransformerBlock)
  adds [`enorm`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPTransformerBlock.enorm),
  [`hnorm`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPTransformerBlock.hnorm),
  [`eh_proj`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPTransformerBlock.eh_proj), and
  [`mtp_norm`](../catalog/torchtitan/models/deepseek_v3/mtp.md#MTPTransformerBlock.mtp_norm) to a
  normal decoder layer (attention + FFN or MoE).
- Shifting: [`roll_mtp_sequence`](../catalog/torchtitan/models/deepseek_v3/mtp.md#roll_mtp_sequence)
  (fill token id 0 for inputs, [`IGNORE_INDEX`](../catalog/torchtitan/components/loss.md#IGNORE_INDEX)
  for labels; optional valid mask).
- Parallelism: [`apply_fsdp_to_mtp_decoder`](../catalog/torchtitan/models/deepseek_v3/mtp.md#apply_fsdp_to_mtp_decoder)
  and [`_set_deepseek_v3_mtp_sharding`](../catalog/torchtitan/models/deepseek_v3/sharding.md#_set_deepseek_v3_mtp_sharding "torchtitan/models/deepseek_v3/sharding.py:L155").

## Why it matters / when it applies
- **Packed documents are respected.** When `positions` reset (a new packed document), the shifted
  slot is filled/ignored rather than reading the next document's token; MTP blocks get the
  *original* positions so RoPE/attention stay anchored at the destination position. Each extra depth
  has one fewer valid target per row than the previous one (differs from the paper's Figure 3,
  which assumes a longer window).
- **SP correctness:** shifting a sequence-sharded hidden state locally would be wrong across shard
  boundaries, so shifting happens at the token-id level and the shared `tok_embeddings` is re-run per
  depth; the valid mask is aligned to the SP layout by the block's `ShardingConfig`, with no explicit
  `redistribute` in forward. Cost: one extra embedding lookup per depth.
- **CP:** shifted tokens, labels, and masks are built before CP sharding, so the same load balancer
  shards main and MTP tensors together - no boundary exchange between CP ranks.
- **FSDP/EP reuse the main policy:** MTP layers are temporarily appended to `model.layers` for
  FSDP wrapping and config updates, so they get identical wrapping, expert FSDP, and reshard
  policy; MoE in MTP layers uses the normal EP placements.
- **Loss:** `total = main + mtp_scale * mean(mtp_losses)` (each depth weighted
  `mtp_scale / num_mtp_layers`), normalized by global valid tokens; with `ChunkedLossWrapper` the
  model returns hidden states (`_skip_lm_head`) and the wrapper applies the shared LM head per chunk.
  MTP adds N decoder blocks plus N LM-head/loss passes of compute per step - account for it in
  FLOP/MFU math.
- **PP is unsupported** (code raises "MTP does not support pipeline parallelism yet"); stage
  ownership and loss routing are open TODOs.
- The doc's `deepseek_v3_debugmodel_mtp` description passes `mtp_scale=0.3` explicitly; the recipe
  relies on the same value as the `MTPLoss.Config` default. No TPU recipe enables MTP at this commit.

## Connections
- Code concepts: [deepseek-v3-model](../concepts/deepseek-v3-model.md),
  [deepseek-v4-model](../concepts/deepseek-v4-model.md),
  [training-components](../concepts/training-components.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md).
- Module catalogs: [torchtitan/models/deepseek_v3/mtp](../catalog/torchtitan/models/deepseek_v3/mtp.md),
  [torchtitan/models/deepseek_v3/sharding](../catalog/torchtitan/models/deepseek_v3/sharding.md),
  [torchtitan/components/loss](../catalog/torchtitan/components/loss.md).
- Related doc-concepts: [declarative-sharding-config](declarative-sharding-config.md),
  [moe-sharding-placements](moe-sharding-placements.md),
  [dataset-mixing-and-packing](dataset-mixing-and-packing.md),
  [model-support-overview](model-support-overview.md).

## Source
Extracted from `torchtitan/models/deepseek_v3/MTP.md` (kept in place).
