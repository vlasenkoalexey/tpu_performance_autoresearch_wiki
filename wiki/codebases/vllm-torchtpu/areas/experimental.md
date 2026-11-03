---
title: 'Area: src/vllm_torchtpu/experimental'
type: area
area: 'src/vllm_torchtpu/experimental'
description: 'Ahead-of-time exporter that lowers a vllm serve configuration into a shard-local StableHLO serving directory, plus a launcher that hands that artifact to an external Rust runtime with no Python in the serving process.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/experimental`

## Purpose
`src/vllm_torchtpu/experimental` is a separate deployment path, not part of the normal `vllm serve` hot loop (no module outside the area imports it). The exporter takes a `vllm serve` command line, loads the model through vLLM and this plugin exactly as serving would, and lowers it into a StableHLO serving directory: one forward module per token bucket, logits and sampler modules per request bucket, a weight-slot definition, a metadata contract and optionally an Orbax weight checkpoint. The launcher splits a `vllm serve` command line between that exporter and an external `rvllm` binary (not in this repo), caches the export by content, and then runs the artifact through PJRT.

The key design idea, documented on [model-export-and-rust-launcher](../concepts/model-export-and-rust-launcher.md), is that every startup decision `vllm serve` makes (block size, KV block count, buckets, sharding, XLA flags, sampler variants) is baked into the artifact, and each module is lowered shard-local with explicit collectives. The runtime then only has to place weights and dispatch programs.

For TPU inference performance this area matters as a way to remove host-side Python overhead from the serving loop. The device programs it exports are the same ones the [model runner](../concepts/tpu-model-runner.md) compiles per bucket, so kernel and layout work elsewhere in the repo carries over.

## How the units connect
One unit, owned by [model-export-and-rust-launcher](../concepts/model-export-and-rust-launcher.md): the `export/` package (command-line parsing, model load, per-bucket lowering, sampler modules, metadata and weight writing) and the `rust/` package (the `serve` launcher that runs the exporter once and then `exec`s the Rust runtime). Because the exporter loads the model exactly as serving would, its buckets, sharding and compile flags come from the same platform config rewriting; see [tpu-platform](../concepts/tpu-platform.md) and [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/experimental`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/experimental` | 14 | 292 | 0 | (internal) | [model-export-and-rust-launcher](../concepts/model-export-and-rust-launcher.md) |

<!-- area:auto:end -->
