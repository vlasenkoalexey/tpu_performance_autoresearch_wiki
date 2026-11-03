---
title: 'Module: src/vllm_torchtpu/megakernel/spec.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/spec.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.spec`/
symbols:
  ModelSpec.all_modules: ModelSpec#all_modules().
  WeightDecl.name: WeightDecl#name.
  SwitchSlot.active_branches: SwitchSlot#active_branches().
  SmallField.name: SmallField#name.
  LayerType.slots: LayerType#slots.
  SwitchSlot.active_pairs: SwitchSlot#active_pairs().
  StateDecl: StateDecl#
  StateDecl.name: StateDecl#name.
  ModelSpec: ModelSpec#
  WeightDecl: WeightDecl#
  SwitchSlot: SwitchSlot#
  ModelSpec.layer_type: ModelSpec#layer_type.
  SwitchSlot.branch_counts: SwitchSlot#branch_counts.
  SwitchSlot.branches: SwitchSlot#branches.
  SwitchSlot.active_counts: SwitchSlot#active_counts().
  Spec: Spec#
  WeightDecl.dtype: WeightDecl#dtype.
  WeightDecl.stream_ring: WeightDecl#stream_ring.
  StateDecl.shape: StateDecl#shape.
  StateDecl.dtype: StateDecl#dtype.
  ExtraInput: ExtraInput#
  SwitchSlot.period: SwitchSlot#period().
  WeightDecl.N: WeightDecl#N.
  SwitchSlot.__post_init__: SwitchSlot#__post_init__().
  ModelSpec.config: ModelSpec#config.
  WeightDecl.K: WeightDecl#K.
  WeightDecl.lead_dims: WeightDecl#lead_dims.
  SwitchSlot.name: SwitchSlot#name.
  StateDecl.per_layer: StateDecl#per_layer.
  SmallField: SmallField#
  ScratchReq: ScratchReq#
  WeightDecl.layout: WeightDecl#layout.
  StateDecl.tupled: StateDecl#tupled.
  SmallField.width: SmallField#width.
  LayerType: LayerType#
  StateDecl.access: StateDecl#access.
  ExtraInput.name: ExtraInput#name.
  ModelSpec.name: ModelSpec#name.
  Spec.shape: Spec#shape.
  Spec.dtype: Spec#dtype.
  StateDecl.memory_space: StateDecl#memory_space.
  ExtraInput.memory_space: ExtraInput#memory_space.
  ExtraInput.shape: ExtraInput#shape.
  ExtraInput.dtype: ExtraInput#dtype.
  ScratchReq.name: ScratchReq#name.
  ScratchReq.spec: ScratchReq#spec.
  ScratchReq.phase: ScratchReq#phase.
  LayerType.name: LayerType#name.
  ModelSpec.cache_backend: ModelSpec#cache_backend.
---
# Module: [`src/vllm_torchtpu/megakernel/spec.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py)

## Classes
### <a id="ExtraInput"></a>`ExtraInput`
- def: [`src/vllm_torchtpu/megakernel/spec.py:90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L90)
- doc: Positional input after the states, declared by a module.
- signature: `class ExtraInput:`
- members:
  - <a id="ExtraInput.dtype"></a>`dtype` — [`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L102)
  - <a id="ExtraInput.memory_space"></a>`memory_space` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L100)
  - <a id="ExtraInput.name"></a>`name` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L99)
  - <a id="ExtraInput.shape"></a>`shape` — [`L101`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L101)
- used by: [`extra_inputs`](planner.md#extra_inputs), [`extra_inputs`](module.md#Module.extra_inputs)

### <a id="LayerType"></a>`LayerType`
- def: [`src/vllm_torchtpu/megakernel/spec.py:162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L162)
- doc: Sequence of slots executed in a single transformer layer.
- signature: `class LayerType:`
- members:
  - <a id="LayerType.name"></a>`name` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L165)
  - <a id="LayerType.slots"></a>`slots` — [`L166`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L166)
- uses (calls/refs, reference-scoped): [`Module`](module.md#Module), [`SwitchSlot`](spec.md#SwitchSlot)
- used by: [`plan`](planner.md#plan), [`_discover_schedule`](planner.md#_discover_schedule), [`all_modules`](spec.md#ModelSpec.all_modules), [`layer_type`](spec.md#ModelSpec.layer_type)

### <a id="ModelSpec"></a>`ModelSpec`
- def: [`src/vllm_torchtpu/megakernel/spec.py:170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L170)
- doc: Complete declarative model architecture specification.
- signature: `class ModelSpec:`
- members:
  - <a id="ModelSpec.all_modules"></a>`all_modules(self)` — [`L180`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L180) — Return unique active modules in deterministic declaration order. — documented in [megakernel](../../../../concepts/megakernel.md)
  - <a id="ModelSpec.cache_backend"></a>`cache_backend` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L178)
  - <a id="ModelSpec.config"></a>`config` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L174)
  - <a id="ModelSpec.layer_type"></a>`layer_type` — [`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L175)
  - <a id="ModelSpec.name"></a>`name` — [`L173`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L173)
- uses (calls/refs, reference-scoped): [`name`](module.md#Module.name), [`Module`](module.md#Module), [`active_branches`](spec.md#SwitchSlot.active_branches), [`slots`](spec.md#LayerType.slots), [`SwitchSlot`](spec.md#SwitchSlot), [`LayerType`](spec.md#LayerType)
- used by: [`plan`](planner.md#plan), [`weight_shapes`](planner.md#weight_shapes), [`kernel_out_shapes`](planner.md#kernel_out_shapes), [`_discover_schedule`](planner.md#_discover_schedule), [`state_shapes`](planner.md#state_shapes), [`extra_inputs`](planner.md#extra_inputs), [`model_spec`](planner.md#Plan.model_spec)

### <a id="ScratchReq"></a>`ScratchReq`
- def: [`src/vllm_torchtpu/megakernel/spec.py:114`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L114)
- doc: VMEM / SMEM / Semaphore buffer request declared by a Module or Core.
- signature: `class ScratchReq:`
- members:
  - <a id="ScratchReq.name"></a>`name` — [`L117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L117)
  - <a id="ScratchReq.phase"></a>`phase` — [`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L119)
  - <a id="ScratchReq.spec"></a>`spec` — [`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L118)
- used by: [`scratch`](module.md#Module.scratch)

### <a id="SmallField"></a>`SmallField`
- def: [`src/vllm_torchtpu/megakernel/spec.py:106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L106)
- doc: Per-layer 1D vector packed into the double-buffered `smalls` table.
- signature: `class SmallField:`
- members:
  - <a id="SmallField.name"></a>`name` — [`L109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L109)
  - <a id="SmallField.width"></a>`width` — [`L110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L110)
- used by: [`plan`](planner.md#plan), [`smalls`](module.md#Module.smalls)

### <a id="Spec"></a>`Spec`
- def: [`src/vllm_torchtpu/megakernel/spec.py:46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L46)
- doc: Shape + dtype descriptor for nested/tupled per-layer HBM tensors.
- signature: `class Spec:`
- members:
  - <a id="Spec.dtype"></a>`dtype` — [`L50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L50)
  - <a id="Spec.shape"></a>`shape` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L49)
- used by: [`weight_shapes`](planner.md#weight_shapes), [`kernel_out_shapes`](planner.md#kernel_out_shapes), [`state_shapes`](planner.md#state_shapes)

### <a id="StateDecl"></a>`StateDecl`
- def: [`src/vllm_torchtpu/megakernel/spec.py:73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L73)
- doc: Declarative specification for a state, cache, or per-layer output tensor.
- signature: `class StateDecl:`
- members:
  - <a id="StateDecl.access"></a>`access` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L83)
  - <a id="StateDecl.dtype"></a>`dtype` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L82)
  - <a id="StateDecl.memory_space"></a>`memory_space` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L85)
  - <a id="StateDecl.name"></a>`name` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L80)
  - <a id="StateDecl.per_layer"></a>`per_layer` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L84)
  - <a id="StateDecl.shape"></a>`shape` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L81)
  - <a id="StateDecl.tupled"></a>`tupled` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L86)
- used by: [`plan`](planner.md#plan), [`kernel_out_shapes`](planner.md#kernel_out_shapes), [`state_shapes`](planner.md#state_shapes), [`outputs`](module.md#Module.outputs), [`states`](module.md#Module.states), [`output_decls`](planner.md#Plan.output_decls), [`state_decls`](planner.md#Plan.state_decls)

### <a id="SwitchSlot"></a>`SwitchSlot`
- def: [`src/vllm_torchtpu/megakernel/spec.py:123`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L123)
- doc: Conditional slot inside a single layer loop body (e.g. two mixer kinds).
- signature: `class SwitchSlot:`
- members:
  - <a id="SwitchSlot.active_branches"></a>`active_branches(self)` — [`L153`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L153)
  - <a id="SwitchSlot.active_counts"></a>`active_counts(self)` — [`L157`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L157)
  - <a id="SwitchSlot.active_pairs"></a>`active_pairs(self)` — [`L148`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L148) — Return `(branch, count)` pairs with `count > 0`.
  - <a id="SwitchSlot.period"></a>`period(self)` — [`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L144)
  - <a id="SwitchSlot.branch_counts"></a>`branch_counts` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L132)
  - <a id="SwitchSlot.branches"></a>`branches` — [`L131`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L131)
  - <a id="SwitchSlot.name"></a>`name` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L130)
- protocol/private: <a id="SwitchSlot.__post_init__"></a>`__post_init__`[`L134`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L134)
- uses (calls/refs, reference-scoped): [`Module`](module.md#Module)
- used by: [`plan`](planner.md#plan), [`_discover_schedule`](planner.md#_discover_schedule), [`all_modules`](spec.md#ModelSpec.all_modules), [`slots`](spec.md#LayerType.slots)

### <a id="WeightDecl"></a>`WeightDecl`
- def: [`src/vllm_torchtpu/megakernel/spec.py:54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L54)
- doc: Declarative specification for a module weight tensor.
- signature: `class WeightDecl:`
- members:
  - <a id="WeightDecl.K"></a>`K` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L62)
  - <a id="WeightDecl.N"></a>`N` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L63)
  - <a id="WeightDecl.dtype"></a>`dtype` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L64)
  - <a id="WeightDecl.layout"></a>`layout` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L66)
  - <a id="WeightDecl.lead_dims"></a>`lead_dims` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L67)
  - <a id="WeightDecl.name"></a>`name` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L61)
  - <a id="WeightDecl.stream_ring"></a>`stream_ring` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/spec.py#L65)
- used by: [`plan`](planner.md#plan), [`weight_shapes`](planner.md#weight_shapes), [`weights`](module.md#Module.weights), [`weight_decls`](planner.md#Plan.weight_decls), [`hbm_weights`](planner.md#Plan.hbm_weights)

