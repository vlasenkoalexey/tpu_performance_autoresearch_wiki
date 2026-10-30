---
title: 'Module: torchtitan/experiments/graph_trainer/storage.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/storage.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.storage`/
symbols:
  DiskStorageAdapter: DiskStorageAdapter#
  DiskStorageAdapter.save: DiskStorageAdapter#save().
  DiskStorageAdapter.exists: DiskStorageAdapter#exists().
  StorageAdapter: StorageAdapter#
  DiskStorageAdapter._path_for: DiskStorageAdapter#_path_for().
  DiskStorageAdapter.load: DiskStorageAdapter#load().
  DiskStorageAdapter.delete: DiskStorageAdapter#delete().
  StorageAdapter.save: StorageAdapter#save().
  StorageAdapter.load: StorageAdapter#load().
  StorageAdapter.exists: StorageAdapter#exists().
  StorageAdapter.delete: StorageAdapter#delete().
  DiskStorageAdapter.base_dir: DiskStorageAdapter#base_dir.
  DiskStorageAdapter.__init__: DiskStorageAdapter#__init__().
---
# Module: [`torchtitan/experiments/graph_trainer/storage.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py)

## Classes
### <a id="DiskStorageAdapter"></a>`DiskStorageAdapter`  ·  implements/extends StorageAdapter
- def: [`torchtitan/experiments/graph_trainer/storage.py:49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L49)
- signature: `class DiskStorageAdapter(StorageAdapter):`
- members:
  - <a id="DiskStorageAdapter.delete"></a>`delete(self, key: str)` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L83)
  - <a id="DiskStorageAdapter.exists"></a>`exists(self, key: str)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L80)
  - <a id="DiskStorageAdapter.load"></a>`load(self, key: str)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L74)
  - <a id="DiskStorageAdapter.save"></a>`save(self, key: str, data: bytes)` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L59)
  - <a id="DiskStorageAdapter.base_dir"></a>`base_dir` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L51)
- protocol/private: <a id="DiskStorageAdapter.__init__"></a>`__init__`[`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L50), <a id="DiskStorageAdapter._path_for"></a>`_path_for`[`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L53)
- uses (calls/refs, reference-scoped): [`StorageAdapter`](storage.md#StorageAdapter)
- used by: [`_precompile_aot_fx_trace`](precompile_main.md#_precompile_aot_fx_trace), [`_load_precompiled_fx_trace`](trainer.md#GraphTrainer._load_precompiled_fx_trace), [`StorageAdapter`](storage.md#StorageAdapter), [`load`](storage.md#StorageAdapter.load), [`save`](storage.md#StorageAdapter.save), [`delete`](storage.md#StorageAdapter.delete), [`exists`](storage.md#StorageAdapter.exists)  (11 test-only)

### <a id="StorageAdapter"></a>`StorageAdapter`  ·  implements/extends ABC
- def: [`torchtitan/experiments/graph_trainer/storage.py:14`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L14)
- doc: Interface for storing and retrieving precompiled artifacts.
- signature: `class StorageAdapter(ABC):`
- members:
  - <a id="StorageAdapter.delete"></a>`delete(self, key: str)` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L44) — Delete an artifact for the given key. No-op if it doesn't exist.
  - <a id="StorageAdapter.exists"></a>`exists(self, key: str)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L39) — Check if an artifact exists for the given key.
  - <a id="StorageAdapter.load"></a>`load(self, key: str)` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L31) — Load data for the given key.
  - <a id="StorageAdapter.save"></a>`save(self, key: str, data: bytes)` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/storage.py#L23) — Save data under the given key. Returns the path/URI of the saved artifact.
- uses (calls/refs, reference-scoped): [`DiskStorageAdapter`](storage.md#DiskStorageAdapter), [`save`](storage.md#DiskStorageAdapter.save), [`exists`](storage.md#DiskStorageAdapter.exists), [`load`](storage.md#DiskStorageAdapter.load), [`delete`](storage.md#DiskStorageAdapter.delete)
- used by: [`precompile_fx_trace_load`](precompile.md#precompile_fx_trace_load), [`precompile_fx_trace_save`](precompile.md#precompile_fx_trace_save), [`DiskStorageAdapter`](storage.md#DiskStorageAdapter)

