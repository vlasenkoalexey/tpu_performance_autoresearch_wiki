---
title: 'Module: src/vllm_torchtpu/distributed/chip_topology.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/chip_topology.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.chip_topology`/
symbols:
  hierarchical_moe_split: hierarchical_moe_split().
  get_chip_topology: get_chip_topology().
  logger: logger.
  ChipTopology.describe: ChipTopology#describe().
  ChipTopology.cores_per_chip: ChipTopology#cores_per_chip.
  ChipTopology.chip_of: ChipTopology#chip_of().
  ChipTopology.device_ids: ChipTopology#device_ids.
  ChipTopology.chips: ChipTopology#chips.
  ChipTopology: ChipTopology#
  ChipTopology.num_chips: ChipTopology#num_chips.
  ChipTopology.__init__: ChipTopology#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/chip_topology.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py)

## Classes
### <a id="ChipTopology"></a>`ChipTopology`
- def: [`src/vllm_torchtpu/distributed/chip_topology.py:26`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L26) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- doc: The chip/chiplet grouping of the devices this process can see.
- signature: `class ChipTopology:`
- members:
  - <a id="ChipTopology.chip_of"></a>`chip_of(self, rank: int)` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L35) — ``(chip_index, core_on_chip)`` for a global device rank.
  - <a id="ChipTopology.describe"></a>`describe(self)` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L52)
  - <a id="ChipTopology.chips"></a>`chips` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L30)
  - <a id="ChipTopology.cores_per_chip"></a>`cores_per_chip` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L33)
  - <a id="ChipTopology.device_ids"></a>`device_ids` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L31)
  - <a id="ChipTopology.num_chips"></a>`num_chips` — [`L32`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L32)
- protocol/private: <a id="ChipTopology.__init__"></a>`__init__`[`L29`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L29)
- used by: [`hierarchical_moe_split`](chip_topology.md#hierarchical_moe_split), [`_chip_rank_groups`](intra_chip.md#_chip_rank_groups), [`get_chip_topology`](chip_topology.md#get_chip_topology), [`stage_chips`](pp_wave.md#stage_chips)

## Functions
- <a id="get_chip_topology"></a>`get_chip_topology()` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L60) — Group the visible devices by physical chip, or ``None`` if unknowable. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="hierarchical_moe_split"></a>`hierarchical_moe_split(world_size: int, rank: int)` — [`L108`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L108) — ``(ep_size, ep_rank, tp_size, tp_rank)`` for hierarchical MoE. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="logger"></a>`logger` — [`L23`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/chip_topology.py#L23)

