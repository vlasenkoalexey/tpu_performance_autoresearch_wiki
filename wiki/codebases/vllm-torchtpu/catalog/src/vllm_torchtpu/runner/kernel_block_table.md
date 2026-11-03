---
title: 'Module: src/vllm_torchtpu/runner/kernel_block_table.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/kernel_block_table.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.kernel_block_table`/
symbols:
  KernelBlockTable.from_block_table: KernelBlockTable#from_block_table().
  install_kernel_block_tables: install_kernel_block_tables().
  KernelBlockTable: KernelBlockTable#
  KernelBlockTable.append_row: KernelBlockTable#append_row().
  KernelBlockTable.blocks_per_kv_block: KernelBlockTable#blocks_per_kv_block.
  KernelBlockTable.kv_cache_block_size: KernelBlockTable#kv_cache_block_size.
---
# Module: [`src/vllm_torchtpu/runner/kernel_block_table.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py)

## Classes
### <a id="KernelBlockTable"></a>`KernelBlockTable`
- def: [`src/vllm_torchtpu/runner/kernel_block_table.py:37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L37)
- doc: A `BlockTable` whose rows hold kernel block ids.
- signature: `class KernelBlockTable(BlockTable):`
- members:
  - <a id="KernelBlockTable.append_row"></a>`append_row(self, block_ids: list[int], row_idx: int)` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L75)
  - <a id="KernelBlockTable.from_block_table"></a>`from_block_table(cls, table: BlockTable, kernel_block_size: int)` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L49) — An empty kernel-block copy of ``table``.
  - <a id="KernelBlockTable.blocks_per_kv_block"></a>`blocks_per_kv_block` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L46)
  - <a id="KernelBlockTable.kv_cache_block_size"></a>`kv_cache_block_size` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L45)
- used by: [`install_kernel_block_tables`](kernel_block_table.md#install_kernel_block_tables)

## Functions
- <a id="install_kernel_block_tables"></a>`install_kernel_block_tables(block_tables: MultiGroupBlockTable, kernel_block_sizes: Sequence[int])` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kernel_block_table.py#L84) — Give each group whose kernel block is smaller than its manager block a

