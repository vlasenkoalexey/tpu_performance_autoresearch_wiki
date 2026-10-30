---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.padding_packing_utils`/
symbols:
  patch_varlen_attention: patch_varlen_attention().
  patch_create_varlen_metadata: patch_create_varlen_metadata().
  patch_create_varlen_metadata.padded_create_varlen_metadata: patch_create_varlen_metadata().padded_create_varlen_metadata().
  patch_varlen_attention.cpu_varlen_forward: patch_varlen_attention().cpu_varlen_forward().
  patch_varlen_attention.tpu_varlen_forward: patch_varlen_attention().tpu_varlen_forward().
  pad_train_batch_to_static: pad_train_batch_to_static().
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py)

## Functions
- <a id="patch_varlen_attention.cpu_varlen_forward"></a>`cpu_varlen_forward(self, q_BLNH, k_BLNH, v_BLNH, *, attention_masks, scale=None, **kwargs)` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L68)
- <a id="pad_train_batch_to_static"></a>`pad_train_batch_to_static(local_batch, device, pad_len: int, max_seqs: int)` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L138) — Pads the TrainBatch's token_ids, advantages, and lengths to static sizes.
- <a id="patch_create_varlen_metadata.padded_create_varlen_metadata"></a>`padded_create_varlen_metadata(positions)` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L35)
- <a id="patch_create_varlen_metadata"></a>`patch_create_varlen_metadata(max_seqs: int = 64)` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L23) — Monkey-patch create_varlen_metadata_for_document to pad metadata to static shapes.
- <a id="patch_varlen_attention"></a>`patch_varlen_attention(target_device: str)` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L60) — Monkey-patch VarlenInnerAttention for CPU and TPU execution.
- <a id="patch_varlen_attention.tpu_varlen_forward"></a>`tpu_varlen_forward(self, q_BLNH, k_BLNH, v_BLNH, *, attention_masks, scale=None, **kwargs)` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py#L102)

