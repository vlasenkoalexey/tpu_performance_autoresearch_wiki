---
title: 'Module: src/vllm_torchtpu/megakernel/module.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/module.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.module`/
symbols:
  Module._resolve_binding: Module#_resolve_binding().
  Module.bind: Module#bind().
  Module.name: Module#name.
  Module: Module#
  Module.__init__: Module#__init__().
  Module.__init_subclass__: Module#__init_subclass__().
  Module.tunables: Module#tunables().
  Module.debug_flags: Module#debug_flags().
  Module._from_resolved: Module#_from_resolved().
  Module.weights: Module#weights().
  Module.Debug: Module#Debug.
  Module.OPTIONS: Module#OPTIONS.
  Module.states: Module#states().
  Module.outputs: Module#outputs().
  Module.extra_inputs: Module#extra_inputs().
  Module.smalls: Module#smalls().
  Module.cache_decl: Module#cache_decl().
  Module.GEOMETRY_FIELDS: Module#GEOMETRY_FIELDS.
  Module.scratch: Module#scratch().
  Module.input_norm: Module#input_norm.
  Module.Tunables: Module#Tunables.
  Module.options: Module#options.
  Module.shared_widths: Module#shared_widths().
  Module.plan_params: Module#plan_params().
  Module.hf_params: Module#hf_params().
  Module.reduction: Module#reduction.
  Module.FIELD_ALIASES: Module#FIELD_ALIASES.
  Module._validate_options: Module#_validate_options().
  Module.host_update_states: Module#host_update_states().
  Module._require_geometry: Module#_require_geometry().
  Module.geometry: Module#geometry.
  Module.prefix: Module#prefix.
  Module.reference: Module#reference().
  Module.GEOMETRY_METHODS: Module#GEOMETRY_METHODS.
  Module.PARAM_NAMES: Module#PARAM_NAMES.
  Module.prologue: Module#prologue().
  Module.init_buffers: Module#init_buffers().
  Module.on_layer_start: Module#on_layer_start().
  Module.emit: Module#emit().
  Module.epilogue: Module#epilogue().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/module.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py)

## Classes
### <a id="Module"></a>`Module`
- def: [`src/vllm_torchtpu/megakernel/module.py:37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L37) — documented in [megakernel](../../../../concepts/megakernel.md)
- doc: Composable megakernel module (attention, recurrent, FFN, norm, etc.).
- signature: `class Module:`
- members:
  - <a id="Module._validate_options"></a>`_validate_options(cls, options: Mapping[str, Any])` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L170) — Hook for subclasses to reject unsupported option values.
  - <a id="Module.bind"></a>`bind(cls, prefix: str = "", **hf_fields_or_options: Any)` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L174) — Bind this module class to a checkpoint `prefix` and HF config fields.
  - <a id="Module.cache_decl"></a>`cache_decl(self, g: Any = None)` — [`L266`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L266)
  - <a id="Module.debug_flags"></a>`debug_flags(self, ex: ExecSpec)` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L100) — This module's `Debug` flags in `ex.debug.modules` (defaults when unset).
  - <a id="Module.emit"></a>`emit(self, ctx: Any, l: Any, slot: Any)` — [`L151`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L151) — Execute module for layer `l` and return partial `[MB, H]` output.
  - <a id="Module.epilogue"></a>`epilogue(self, ctx: Any)` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L155) — Executed once after the main layer loop.
  - <a id="Module.extra_inputs"></a>`extra_inputs(self, g: Any, ex: ExecSpec)` — [`L122`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L122) — Positional inputs after the states (see `ExtraInput`).
  - <a id="Module.hf_params"></a>`hf_params(self, prefix: str | None = None, g: Any = None)` — [`L263`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L263)
  - <a id="Module.host_update_states"></a>`host_update_states(self, g: Any, ex: ExecSpec, pos: Any, states: dict[str, Any], raw_outputs: dict[str, Any])` — [`L158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L158) — Host-side state update inside `shard_map` after `pallas_call` returns.
  - <a id="Module.init_buffers"></a>`init_buffers(self, ctx: Any)` — [`L145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L145) — Executed once after the inter-rank barrier and before the main layer loop.
  - <a id="Module.on_layer_start"></a>`on_layer_start(self, ctx: Any, lyr: Any, slot: Any)` — [`L148`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L148) — Executed at the start of layer `lyr` alongside `smalls` double-buffering.
  - <a id="Module.outputs"></a>`outputs(self, g: Any, ex: ExecSpec)` — [`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L119)
  - <a id="Module.plan_params"></a>`plan_params(self, g: Any, ex: ExecSpec, plan: Any)` — [`L133`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L133) — Optional module-specific derived parameters computed at build time.
  - <a id="Module.prologue"></a>`prologue(self, ctx: Any)` — [`L142`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L142) — Executed once before the inter-rank barrier and main layer loop.
  - <a id="Module.reference"></a>`reference(self, *args: Any, **kwargs: Any)` — [`L269`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L269)
  - <a id="Module.scratch"></a>`scratch(self, g: Any, ex: ExecSpec, plan: Any)` — [`L137`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L137)
  - <a id="Module.shared_widths"></a>`shared_widths(self, g: Any, ex: ExecSpec)` — [`L129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L129) — Minimum column widths required on shared core VMEM buffers.
  - <a id="Module.smalls"></a>`smalls(self, g: Any, ex: ExecSpec)` — [`L126`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L126)
  - <a id="Module.states"></a>`states(self, g: Any, ex: ExecSpec)` — [`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L116)
  - <a id="Module.tunables"></a>`tunables(self, ex: ExecSpec)` — [`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L95) — This module's `Tunables` in `ex`'s tiles (class defaults when unset).
  - <a id="Module.weights"></a>`weights(self, g: Any, ex: ExecSpec)` — [`L113`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L113)
  - <a id="Module.Debug"></a>`Debug` — [`L51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L51)
  - <a id="Module.FIELD_ALIASES"></a>`FIELD_ALIASES` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L53)
  - <a id="Module.GEOMETRY_FIELDS"></a>`GEOMETRY_FIELDS` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L52)
  - <a id="Module.GEOMETRY_METHODS"></a>`GEOMETRY_METHODS` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L54)
  - <a id="Module.OPTIONS"></a>`OPTIONS` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L55)
  - <a id="Module.PARAM_NAMES"></a>`PARAM_NAMES` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L56)
  - <a id="Module.Tunables"></a>`Tunables` — [`L50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L50)
  - <a id="Module.geometry"></a>`geometry` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L57)
  - <a id="Module.input_norm"></a>`input_norm` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L49)
  - <a id="Module.name"></a>`name` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L47) — documented in [megakernel](../../../../concepts/megakernel.md)
  - <a id="Module.options"></a>`options` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L59)
  - <a id="Module.prefix"></a>`prefix` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L58)
  - <a id="Module.reduction"></a>`reduction` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L48)
- protocol/private: <a id="Module.__init__"></a>`__init__`[`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L61), <a id="Module.__init_subclass__"></a>`__init_subclass__`[`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L79), <a id="Module._from_resolved"></a>`_from_resolved`[`L250`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L250), <a id="Module._require_geometry"></a>`_require_geometry`[`L254`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L254), <a id="Module._resolve_binding"></a>`_resolve_binding`[`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L218)
- uses (calls/refs, reference-scoped): [`ExecSpec`](exec_spec.md#ExecSpec), [`resolved_tiles`](exec_spec.md#ExecSpec.resolved_tiles), [`FrozenDict`](decls.md#FrozenDict), [`KVCacheDecl`](decls.md#KVCacheDecl), [`RecurrentCacheDecl`](decls.md#RecurrentCacheDecl), [`validate_rename_and_transforms`](decls.md#validate_rename_and_transforms), [`HFParamDecl`](decls.md#HFParamDecl), [`module`](exec_spec.md#Tiles.module), [`StateDecl`](spec.md#StateDecl), [`ResolvedModuleGeometry`](decls.md#ResolvedModuleGeometry), [`WeightDecl`](spec.md#WeightDecl), [`_resolve_field_spec`](decls.md#_resolve_field_spec), [`debug`](exec_spec.md#ExecSpec.debug), [`modules`](exec_spec.md#DebugOptions.modules), [`options`](decls.md#ModuleBinding.options), [`ExtraInput`](spec.md#ExtraInput), [`ModuleBinding`](decls.md#ModuleBinding), [`register_debug`](module_options.md#register_debug), [`register_tunables`](module_options.md#register_tunables), [`rename`](decls.md#ModuleBinding.rename), [`transforms`](decls.md#ModuleBinding.transforms), [`fields`](decls.md#ModuleBinding.fields), [`module_cls`](decls.md#ModuleBinding.module_cls), [`module_cls`](decls.md#ResolvedModuleGeometry.module_cls), [`options`](decls.md#ResolvedModuleGeometry.options), [`rename`](decls.md#ResolvedModuleGeometry.rename), [`transforms`](decls.md#ResolvedModuleGeometry.transforms), [`values`](decls.md#ResolvedModuleGeometry.values), [`ScratchReq`](spec.md#ScratchReq), [`SmallField`](spec.md#SmallField), [`explicit_fields`](decls.md#ModuleBinding.explicit_fields), [`prefix`](decls.md#ModuleBinding.prefix), [`prefix`](decls.md#ResolvedModuleGeometry.prefix)
- used by: [`plan`](planner.md#plan), [`_discover_schedule`](planner.md#_discover_schedule), [`all_modules`](spec.md#ModelSpec.all_modules), [`extra_inputs`](planner.md#extra_inputs), [`active_branches`](spec.md#SwitchSlot.active_branches), [`to_module`](decls.md#ResolvedModuleGeometry.to_module), [`validate_rename_and_transforms`](decls.md#validate_rename_and_transforms), [`cache_decl`](decls.md#ResolvedModuleGeometry.cache_decl), [`hf_params`](decls.md#ResolvedModuleGeometry.hf_params), [`resolve`](decls.md#ModuleBinding.resolve), [`slots`](spec.md#LayerType.slots), [`active_pairs`](spec.md#SwitchSlot.active_pairs), [`to_module`](decls.md#ModuleBinding.to_module), [`branches`](spec.md#SwitchSlot.branches), [`reference`](decls.md#ResolvedModuleGeometry.reference), [`module_cls`](decls.md#ModuleBinding.module_cls), [`module_cls`](decls.md#ResolvedModuleGeometry.module_cls)

## Module values
- <a id="__all__"></a>`__all__` — [`L273`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module.py#L273)

