---
title: 'Module: csrc/ops/gru/gru_common.h'
type: catalog
provenance: extracted
module: csrc/ops/gru/gru_common.h
status: fresh
symbol_base: cxx . . $ torch_tpu/GruGateAdjoints#
symbols:
  GruGateAdjoints.delta_hx_skip: delta_hx_skip.
  GruGateAdjoints.delta_pre_r: delta_pre_r.
  GruGateAdjoints: ''
  GruGateAdjoints.delta_pre_z: delta_pre_z.
  GruGateAdjoints.delta_h_n: delta_h_n.
  GruGateAdjoints.delta_pre_n: delta_pre_n.
---
# Module: [`csrc/ops/gru/gru_common.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h)

## Classes
### <a id="GruGateAdjoints"></a>`GruGateAdjoints`
- def: [`csrc/ops/gru/gru_common.h:49`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L49)
- doc: Encapsulates the pre-activation gate adjoints and the hidden skip adjoint
- signature: `struct GruGateAdjoints`
- members:
  - <a id="GruGateAdjoints.delta_h_n"></a>`delta_h_n` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L54) — Pre-activation candidate hidden gradient (d_hn_pre
  - <a id="GruGateAdjoints.delta_hx_skip"></a>`delta_hx_skip` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L56) — Gradient propagating through direct skip
  - <a id="GruGateAdjoints.delta_pre_n"></a>`delta_pre_n` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L53) — Pre-activation candidate input gradient (d_n_pre)
  - <a id="GruGateAdjoints.delta_pre_r"></a>`delta_pre_r` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L50) — Pre-activation reset gate gradient (d_r_pre)
  - <a id="GruGateAdjoints.delta_pre_z"></a>`delta_pre_z` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/gru/gru_common.h#L51) — Pre-activation update gate gradient (d_z_pre)
- uses (calls/refs, reference-scoped): [`ComputeGruGateAdjoints`](gru_common.cc.md#ComputeGruGateAdjoints)
- used by: [`BuildGruCellBackwardShlo`](../thnn_fused_gru_cell/thnn_fused_gru_cell_aten_kernels.cc.md#BuildGruCellBackwardShlo), [`ComputeGruBackwardStep`](gru_aten_kernels.cc.md#ComputeGruBackwardStep)

