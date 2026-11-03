---
title: 'Module: src/vllm_torchtpu/distributed/intra_chip.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/intra_chip.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.intra_chip`/
symbols:
  get_intra_chip_group: get_intra_chip_group().
  _chip_rank_groups: _chip_rank_groups().
  _rank_to_device: _rank_to_device().
  logger: logger.
  _group: _group.
  _group_ranks_by_chip: _group_ranks_by_chip().
  _initialized: _initialized.
---
# Module: [`src/vllm_torchtpu/distributed/intra_chip.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py)

## Functions
- <a id="_chip_rank_groups"></a>`_chip_rank_groups()` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L39) — Global ranks grouped by the chip they sit on, or ``None`` if unusable. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_group_ranks_by_chip"></a>`_group_ranks_by_chip(topology, rank_to_device: dict[int, int])` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L84) — Ranks grouped by the chip their device sits on, or ``None`` if unusable.
- <a id="_rank_to_device"></a>`_rank_to_device()` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L64) — Global rank -> the TPU device id it runs on. Collective over the world.
- <a id="get_intra_chip_group"></a>`get_intra_chip_group()` — [`L111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L111) — The ``GroupCoordinator`` over this rank's chip, or ``None``. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)

## Module values
- <a id="_group"></a>`_group` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L35)
- <a id="_initialized"></a>`_initialized` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L36)
- <a id="logger"></a>`logger` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/intra_chip.py#L33)

