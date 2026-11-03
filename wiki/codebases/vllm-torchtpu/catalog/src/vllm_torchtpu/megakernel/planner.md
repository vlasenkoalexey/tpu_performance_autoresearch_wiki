---
title: 'Module: src/vllm_torchtpu/megakernel/planner.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/planner.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.planner`/
symbols:
  plan: plan().
  weight_shapes: weight_shapes().
  kernel_out_shapes: kernel_out_shapes().
  _discover_schedule: _discover_schedule().
  state_shapes: state_shapes().
  extra_inputs: extra_inputs().
  k_tile: k_tile().
  Plan: Plan#
  Plan.weight_decls: Plan#weight_decls.
  Plan.state_decls: Plan#state_decls.
  Plan.output_decls: Plan#output_decls.
  Plan.module_layer_counts: Plan#module_layer_counts.
  Plan.model_spec: Plan#model_spec.
  Plan.ex: Plan#ex.
  Plan.hbm_weights: Plan#hbm_weights.
  Plan.weight_owners: Plan#weight_owners.
  Plan.state_owners: Plan#state_owners.
  Plan.output_owners: Plan#output_owners.
  Plan.tk: Plan#tk.
  Plan.nt: Plan#nt.
  Plan.smalls_width: Plan#smalls_width.
  Plan.kinds: Plan#kinds.
  Plan.static_kinds: Plan#static_kinds.
  Plan.dynamic_kinds: Plan#dynamic_kinds.
  Plan.period: Plan#period.
  Plan.branch_counts: Plan#branch_counts.
  Plan.branch_tiles: Plan#branch_tiles.
  Plan.branch_segs: Plan#branch_segs.
  Plan.t_cycle: Plan#t_cycle.
  Plan.T_TOTAL: Plan#T_TOTAL.
  Plan.module_branch_idx: Plan#module_branch_idx.
  Plan.slot_ar_index: Plan#slot_ar_index.
  Plan.smalls_layout: Plan#smalls_layout.
  Plan.shared_widths: Plan#shared_widths.
  Plan.w_names: Plan#w_names.
  Plan.s_names: Plan#s_names.
  Plan.o_names: Plan#o_names.
  Plan.module_params: Plan#module_params.
  encode_ecopy: encode_ecopy().
---
# Module: [`src/vllm_torchtpu/megakernel/planner.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py)

## Classes
### <a id="Plan"></a>`Plan`
- def: [`src/vllm_torchtpu/megakernel/planner.py:53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L53)
- doc: Declarative build-time plan derived from `ModelSpec` and `ExecSpec`.
- signature: `class Plan:`
- members:
  - <a id="Plan.T_TOTAL"></a>`T_TOTAL` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L75)
  - <a id="Plan.branch_counts"></a>`branch_counts` — [`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L71)
  - <a id="Plan.branch_segs"></a>`branch_segs` — [`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L73)
  - <a id="Plan.branch_tiles"></a>`branch_tiles` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L72)
  - <a id="Plan.dynamic_kinds"></a>`dynamic_kinds` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L60)
  - <a id="Plan.ex"></a>`ex` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L57)
  - <a id="Plan.hbm_weights"></a>`hbm_weights` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L61)
  - <a id="Plan.kinds"></a>`kinds` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L58)
  - <a id="Plan.model_spec"></a>`model_spec` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L56)
  - <a id="Plan.module_branch_idx"></a>`module_branch_idx` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L77)
  - <a id="Plan.module_layer_counts"></a>`module_layer_counts` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L76)
  - <a id="Plan.module_params"></a>`module_params` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L85)
  - <a id="Plan.nt"></a>`nt` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L69)
  - <a id="Plan.o_names"></a>`o_names` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L84)
  - <a id="Plan.output_decls"></a>`output_decls` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L66)
  - <a id="Plan.output_owners"></a>`output_owners` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L67)
  - <a id="Plan.period"></a>`period` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L70)
  - <a id="Plan.s_names"></a>`s_names` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L83)
  - <a id="Plan.shared_widths"></a>`shared_widths` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L81)
  - <a id="Plan.slot_ar_index"></a>`slot_ar_index` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L78)
  - <a id="Plan.smalls_layout"></a>`smalls_layout` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L79)
  - <a id="Plan.smalls_width"></a>`smalls_width` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L80)
  - <a id="Plan.state_decls"></a>`state_decls` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L64)
  - <a id="Plan.state_owners"></a>`state_owners` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L65)
  - <a id="Plan.static_kinds"></a>`static_kinds` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L59)
  - <a id="Plan.t_cycle"></a>`t_cycle` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L74)
  - <a id="Plan.tk"></a>`tk` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L68)
  - <a id="Plan.w_names"></a>`w_names` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L82)
  - <a id="Plan.weight_decls"></a>`weight_decls` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L62)
  - <a id="Plan.weight_owners"></a>`weight_owners` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L63)
- uses (calls/refs, reference-scoped): [`ExecSpec`](exec_spec.md#ExecSpec), [`ModelSpec`](spec.md#ModelSpec), [`StateDecl`](spec.md#StateDecl), [`WeightDecl`](spec.md#WeightDecl)
- used by: [`plan`](planner.md#plan), [`weight_shapes`](planner.md#weight_shapes), [`kernel_out_shapes`](planner.md#kernel_out_shapes), [`state_shapes`](planner.md#state_shapes)

## Functions
- <a id="_discover_schedule"></a>`_discover_schedule(model_spec: ModelSpec)` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L88) — Derive repeating cycle `(period, branch_counts)`, layer counts, and AR slots. — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="encode_ecopy"></a>`encode_ecopy(E: int, ER: int, EW: int, moe_tp: bool, cores: Any)` — [`L474`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L474) — Pack per-layer redundant expert copy descriptors into an `[E]` f32 row.
- <a id="extra_inputs"></a>`extra_inputs(model_spec: ModelSpec, ex: ExecSpec)` — [`L518`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L518) — Every module's `extra_inputs`, in module declaration order (unique names).
- <a id="k_tile"></a>`k_tile(K: int, N: int, dtype: Any, bank: int)` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L31) — Largest 128-multiple divisor of K whose `[tk, N]` tile fits `bank` bytes.
- <a id="kernel_out_shapes"></a>`kernel_out_shapes(model_spec: ModelSpec, ex: ExecSpec, p: Plan | None = None)` — [`L452`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L452) — Per-rank output tensor shapes derived from `Module.outputs` plus `hidden`. — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="plan"></a>`plan(model_spec: ModelSpec, ex: ExecSpec)` — [`L189`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L189) — Derive weight tile sizes, stream schedules, smalls layout, and metadata. — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="state_shapes"></a>`state_shapes(model_spec: ModelSpec, ex: ExecSpec, p: Plan | None = None)` — [`L431`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L431) — Per-rank input state shapes derived from `Module.states`. — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="weight_shapes"></a>`weight_shapes(model_spec: ModelSpec, ex: ExecSpec, p: Plan | None = None)` — [`L398`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/planner.py#L398) — Per-rank HBM weight operand shapes derived from `Module.weights`. — documented in [megakernel](../../../../concepts/megakernel.md)

