---
title: 'Module: torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.sbd_splash.mask_export`/
symbols:
  dropout_keep_mask: dropout_keep_mask().
  _mask_kernel: _mask_kernel().
---
# Module: [`torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py)

## Functions
- <a id="_mask_kernel"></a>`_mask_kernel(seed_ref, out_ref, *, thresh, band_width, version, thresh8, block_q_rows=None)` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py#L23)
- <a id="dropout_keep_mask"></a>`dropout_keep_mask(seed_words, *, num_heads, q_seq, kv_seq, rate, interpret=False, version=1, band_width=None, block_q=None)` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py#L69) — Returns int8 [num_heads, q_seq, kv_seq]; 1 == KEEP.

