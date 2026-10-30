---
title: 'Area: torchtitan/protocols'
type: area
area: 'torchtitan/protocols'
description: 'Protocols of torchtitan: Module/Configurable, ModelSpec and the sharding/param-init contracts every model implements.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/protocols`

## Purpose
`torchtitan/protocols/` defines the contracts the rest of the repo is written against: `Configurable` and `Module` (build-from-config, param init, `parallelize`), `ModelSpec` (model config, `parallelize_fn`, pipelining, state-dict adapter) and the sharding config types; see [model-spec-protocols](../concepts/model-spec-protocols.md). This is what lets the TPU lane override strategy (kernels, `parallelize_fn`) without touching model architecture.

## How the units connect
- [model-spec-protocols](../concepts/model-spec-protocols.md) is implemented by every model package ([model-building-blocks](../concepts/model-building-blocks.md) and the family pages) and consumed by [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) and [config-overrides](../concepts/config-overrides.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/protocols`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/protocols` | 6 | 85 | 761 | [`build`](../catalog/torchtitan/protocols/module.md#Module.Config.build "torchtitan/protocols/module.py:L98"), [`Module`](../catalog/torchtitan/protocols/module.md#Module "torchtitan/protocols/module.py:L43"), [`Config`](../catalog/torchtitan/protocols/module.md#Module.Config "torchtitan/protocols/module.py:L94") | [model-spec-protocols](../concepts/model-spec-protocols.md) |

<!-- area:auto:end -->
