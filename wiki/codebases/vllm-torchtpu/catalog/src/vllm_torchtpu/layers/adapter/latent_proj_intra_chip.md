---
title: 'Module: src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.latent_proj_intra_chip`/
symbols:
  make_latent_projection: make_latent_projection().
  shard_group_or_none: shard_group_or_none().
  _warn_once: _warn_once().
  logger: logger.
  _warned: _warned.
  IntraChipColumnParallelLinear.forward: IntraChipColumnParallelLinear#forward().
  IntraChipColumnParallelLinear: IntraChipColumnParallelLinear#
  IntraChipColumnParallelLinear._chip_group: IntraChipColumnParallelLinear#_chip_group.
  IntraChipColumnParallelLinear.__init__: IntraChipColumnParallelLinear#__init__().
  IntraChipColumnParallelLinear.extra_repr: IntraChipColumnParallelLinear#extra_repr().
---
# Module: [`src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py)

## Classes
### <a id="IntraChipColumnParallelLinear"></a>`IntraChipColumnParallelLinear`
- def: [`src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py:57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L57)
- doc: Column-parallel over one chip's cores, gathered back on the chip.
- signature: `class IntraChipColumnParallelLinear(ColumnParallelLinear):`
- members:
  - <a id="IntraChipColumnParallelLinear.extra_repr"></a>`extra_repr(self)` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L101)
  - <a id="IntraChipColumnParallelLinear.forward"></a>`forward(self, input_: torch.Tensor)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L91)
- protocol/private: <a id="IntraChipColumnParallelLinear.__init__"></a>`__init__`[`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L65), <a id="IntraChipColumnParallelLinear._chip_group"></a>`_chip_group`[`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L78)
- used by: [`make_latent_projection`](latent_proj_intra_chip.md#make_latent_projection)

## Functions
- <a id="_warn_once"></a>`_warn_once(message: str, *args)` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L50)
- <a id="make_latent_projection"></a>`make_latent_projection(input_size: int, output_size: int, *, bias: bool, quant_config: QuantizationConfig | None, prefix: str)` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L143) — The intra-chip sharded projection when it applies, else the replicated one.
- <a id="shard_group_or_none"></a>`shard_group_or_none(output_size: int)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L110) — The chip group to shard ``output_size`` across, or ``None`` to replicate.

## Module values
- <a id="_warned"></a>`_warned` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L47)
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.py#L45)

