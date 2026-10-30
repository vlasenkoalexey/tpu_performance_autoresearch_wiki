---
title: 'Module: torchtitan/models/flux/random_loader.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/random_loader.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.random_loader`/
symbols:
  RandomDataloader.batches: RandomDataloader#batches.
  RandomDataloader.__iter__: RandomDataloader#__iter__().
  RandomDataloader.bsz: RandomDataloader#bsz.
  RandomDataloader: RandomDataloader#
  RandomDataloader.img_size: RandomDataloader#img_size.
  logger: logger.
  RandomDataloader.max_steps: RandomDataloader#max_steps.
  RandomDataloader.max_t5_len: RandomDataloader#max_t5_len.
  RandomDataloader.t5_dim: RandomDataloader#t5_dim.
  RandomDataloader.clip_dim: RandomDataloader#clip_dim.
  RandomDataloader.__init__: RandomDataloader#__init__().
  RandomDataloader.close: RandomDataloader#close().
---
# Module: [`torchtitan/models/flux/random_loader.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py)

## Classes
### <a id="RandomDataloader"></a>`RandomDataloader`
- def: [`torchtitan/models/flux/random_loader.py:8`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L8)
- doc: A dataloader that generates random encodings.
- signature: `class RandomDataloader:`
- members:
  - <a id="RandomDataloader.close"></a>`close(self)` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L73) — No-op; called by Trainer.close().
  - <a id="RandomDataloader.batches"></a>`batches` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L31)
  - <a id="RandomDataloader.bsz"></a>`bsz` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L24)
  - <a id="RandomDataloader.clip_dim"></a>`clip_dim` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L29)
  - <a id="RandomDataloader.img_size"></a>`img_size` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L26)
  - <a id="RandomDataloader.max_steps"></a>`max_steps` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L25)
  - <a id="RandomDataloader.max_t5_len"></a>`max_t5_len` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L27)
  - <a id="RandomDataloader.t5_dim"></a>`t5_dim` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L28)
- protocol/private: <a id="RandomDataloader.__init__"></a>`__init__`[`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L14), <a id="RandomDataloader.__iter__"></a>`__iter__`[`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L50)
- uses (calls/refs, reference-scoped): [`IMAGE_LATENT_SIZE_RATIO`](utils.md#IMAGE_LATENT_SIZE_RATIO), [`LATENT_CHANNELS`](utils.md#LATENT_CHANNELS), [`logger`](random_loader.md#logger)
- used by: [`t5_encoder`](trainer.md#FluxTrainer.t5_encoder)

## Module values
- <a id="logger"></a>`logger` — [`L6`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/random_loader.py#L6)

