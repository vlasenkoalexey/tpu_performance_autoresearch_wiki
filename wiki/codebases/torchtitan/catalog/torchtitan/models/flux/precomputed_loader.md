---
title: 'Module: torchtitan/models/flux/precomputed_loader.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/precomputed_loader.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.precomputed_loader`/PrecomputedDataloader#
symbols:
  PrecomputedDataloader.files: files.
  PrecomputedDataloader.__iter__: __iter__().
  PrecomputedDataloader.max_steps: max_steps.
  PrecomputedDataloader: ''
  PrecomputedDataloader.__init__: __init__().
  PrecomputedDataloader.data_dir: data_dir.
  PrecomputedDataloader.rank: rank.
  PrecomputedDataloader.close: close().
---
# Module: [`torchtitan/models/flux/precomputed_loader.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py)

## Classes
### <a id="PrecomputedDataloader"></a>`PrecomputedDataloader`
- def: [`torchtitan/models/flux/precomputed_loader.py:6`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L6)
- doc: A dataloader that loads precomputed batches from a directory.
- signature: `class PrecomputedDataloader:`
- members:
  - <a id="PrecomputedDataloader.close"></a>`close(self)` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L45) — No-op; called by Trainer.close().
  - <a id="PrecomputedDataloader.data_dir"></a>`data_dir` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L15)
  - <a id="PrecomputedDataloader.files"></a>`files` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L20)
  - <a id="PrecomputedDataloader.max_steps"></a>`max_steps` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L16)
  - <a id="PrecomputedDataloader.rank"></a>`rank` — [`L17`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L17)
- protocol/private: <a id="PrecomputedDataloader.__init__"></a>`__init__`[`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L14), <a id="PrecomputedDataloader.__iter__"></a>`__iter__`[`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/precomputed_loader.py#L32)
- used by: [`t5_encoder`](trainer.md#FluxTrainer.t5_encoder)

