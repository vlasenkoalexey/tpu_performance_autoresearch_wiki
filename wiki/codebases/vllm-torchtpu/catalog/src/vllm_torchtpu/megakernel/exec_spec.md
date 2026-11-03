---
title: 'Module: src/vllm_torchtpu/megakernel/exec_spec.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/exec_spec.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.exec_spec`/
symbols:
  ExecSpec: ExecSpec#
  ExecSpec.resolved_tiles: ExecSpec#resolved_tiles().
  ExecSpec.NS: ExecSpec#NS().
  ExecSpec.T: ExecSpec#T.
  Tiles: Tiles#
  ExecSpec.B: ExecSpec#B.
  Tiles.module: Tiles#module().
  Tiles.with_modules: Tiles#with_modules().
  ExecSpec.MB: ExecSpec#MB().
  tile_numerics: tile_numerics().
  ExecSpec.WIDE: ExecSpec#WIDE().
  ExecSpec.R: ExecSpec#R.
  ExecSpec.ctx: ExecSpec#ctx.
  ExecSpec.MR: ExecSpec#MR().
  default_tiles: default_tiles().
  ExecSpec.M: ExecSpec#M().
  Tiles.modules: Tiles#modules.
  DebugOptions.modules: DebugOptions#modules.
  ExecSpec.debug: ExecSpec#debug.
  ExecSpec.resolve_tiles: ExecSpec#resolve_tiles().
  ExecSpec.tiles: ExecSpec#tiles.
  Tiles.__post_init__: Tiles#__post_init__().
  DebugOptions.__post_init__: DebugOptions#__post_init__().
  ExecSpec.skip: ExecSpec#skip().
  ExecSpec.scopes: ExecSpec#scopes().
  ExecSpec.VER: ExecSpec#VER().
  ExecSpec.interpret: ExecSpec#interpret.
  TILE_NUMERICS.TILE_NUMERICS: TILE_NUMERICS.TILE_NUMERICS.
  Tiles.vmem_mib: Tiles#vmem_mib.
  DebugOptions: DebugOptions#
  ExecSpec.__post_init__: ExecSpec#__post_init__().
  _T: _T.
  Tiles.bounds_checks: Tiles#bounds_checks.
  Tiles.mb8: Tiles#mb8.
  MAX_BATCH_ROWS: MAX_BATCH_ROWS.
  ExecSpec.cache: ExecSpec#cache.
  Tiles.bank: Tiles#bank.
  Tiles.ebank: Tiles#ebank.
  Tiles.smem_mib: Tiles#smem_mib.
  Tiles.hier: Tiles#hier.
  Tiles.wide_rows: Tiles#wide_rows.
  DebugOptions.skip: DebugOptions#skip.
  DebugOptions.scopes: DebugOptions#scopes.
  Tiles.nbd: Tiles#nbd.
  Tiles.nbe: Tiles#nbe.
  Tiles.lazy: Tiles#lazy.
  Tiles.inplace: Tiles#inplace.
  Tiles.rsag: Tiles#rsag.
  Tiles.war: Tiles#war.
  Tiles.dense_acc_pair: Tiles#dense_acc_pair.
  Tiles.dmm_unroll: Tiles#dmm_unroll.
  Tiles.rel_fetch: Tiles#rel_fetch.
  ExecSpec.stack_e: ExecSpec#stack_e.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/exec_spec.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py)

## Classes
### <a id="DebugOptions"></a>`DebugOptions`
- def: [`src/vllm_torchtpu/megakernel/exec_spec.py:167`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L167)
- doc: Debug and ablation flags kept separate from model geometry and execution.
- signature: `class DebugOptions:`
- members:
  - <a id="DebugOptions.modules"></a>`modules` — [`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L175)
  - <a id="DebugOptions.scopes"></a>`scopes` — [`L171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L171)
  - <a id="DebugOptions.skip"></a>`skip` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L170)
- protocol/private: <a id="DebugOptions.__post_init__"></a>`__post_init__`[`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L177)
- uses (calls/refs, reference-scoped): [`DebugModulesMap`](module_options.md#DebugModulesMap)
- used by: [`plan`](planner.md#plan), [`debug_flags`](module.md#Module.debug_flags), [`debug`](exec_spec.md#ExecSpec.debug), [`scopes`](exec_spec.md#ExecSpec.scopes), [`skip`](exec_spec.md#ExecSpec.skip)

### <a id="ExecSpec"></a>`ExecSpec`
- def: [`src/vllm_torchtpu/megakernel/exec_spec.py:187`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L187) — documented in [megakernel](../../../../concepts/megakernel.md)
- doc: Execution-time configuration (independent of model architecture).
- signature: `class ExecSpec:`
- members:
  - <a id="ExecSpec.M"></a>`M(self)` — [`L235`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L235)
  - <a id="ExecSpec.MB"></a>`MB(self)` — [`L239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L239)
  - <a id="ExecSpec.MR"></a>`MR(self)` — [`L231`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L231)
  - <a id="ExecSpec.NS"></a>`NS(self)` — [`L226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L226) — documented in [megakernel](../../../../concepts/megakernel.md)
  - <a id="ExecSpec.VER"></a>`VER(self)` — [`L244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L244)
  - <a id="ExecSpec.WIDE"></a>`WIDE(self)` — [`L248`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L248)
  - <a id="ExecSpec.resolve_tiles"></a>`resolve_tiles(self, g: Any = None)` — [`L220`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L220) — Same as `resolved_tiles` (`g` kept for callers; the defaults ignore it).
  - <a id="ExecSpec.resolved_tiles"></a>`resolved_tiles(self)` — [`L217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L217) — documented in [megakernel-pool](../../../../concepts/megakernel-pool.md)
  - <a id="ExecSpec.scopes"></a>`scopes(self)` — [`L256`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L256)
  - <a id="ExecSpec.skip"></a>`skip(self)` — [`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L252)
  - <a id="ExecSpec.B"></a>`B` — [`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L190)
  - <a id="ExecSpec.R"></a>`R` — [`L192`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L192)
  - <a id="ExecSpec.T"></a>`T` — [`L191`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L191) — documented in [megakernel](../../../../concepts/megakernel.md)
  - <a id="ExecSpec.cache"></a>`cache` — [`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L205)
  - <a id="ExecSpec.ctx"></a>`ctx` — [`L193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L193)
  - <a id="ExecSpec.debug"></a>`debug` — [`L201`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L201)
  - <a id="ExecSpec.interpret"></a>`interpret` — [`L198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L198)
  - <a id="ExecSpec.stack_e"></a>`stack_e` — [`L197`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L197)
  - <a id="ExecSpec.tiles"></a>`tiles` — [`L200`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L200)
- protocol/private: <a id="ExecSpec.__post_init__"></a>`__post_init__`[`L207`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L207)
- uses (calls/refs, reference-scoped): [`Tiles`](exec_spec.md#Tiles), [`rup`](ops.md#rup), [`default_tiles`](exec_spec.md#default_tiles), [`DebugOptions`](exec_spec.md#DebugOptions), [`mb8`](exec_spec.md#Tiles.mb8), [`scopes`](exec_spec.md#DebugOptions.scopes), [`skip`](exec_spec.md#DebugOptions.skip), [`wide_rows`](exec_spec.md#Tiles.wide_rows)
- used by: [`plan`](planner.md#plan), [`scatter_pool_states`](pool/scatter.md#scatter_pool_states), [`validate`](pool/layout.md#PoolLayout.validate), [`gather_gdn_states`](pool/gather.md#gather_gdn_states), [`pool_to_states`](pool/pack.md#pool_to_states), [`states_to_pool`](pool/pack.md#states_to_pool), [`cache_exec`](pool/config.md#cache_exec), [`make_pool_backend`](pool/backend.md#make_pool_backend), [`weight_shapes`](planner.md#weight_shapes), [`kernel_out_shapes`](planner.md#kernel_out_shapes), [`can_pool_gather`](pool/backend.md#can_pool_gather), [`state_shapes`](planner.md#state_shapes), [`allocate_test_layout`](pool/pack.md#allocate_test_layout), [`min_num_pages`](pool/layout.md#PoolLayout.min_num_pages), [`exec_for`](profile.md#Profile.exec_for), [`extra_inputs`](planner.md#extra_inputs), [`_scatter`](pool/backend.md#make_pool_backend._scatter), [`resolved_max_pages_per_seq`](pool/config.md#resolved_max_pages_per_seq), [`_gather`](pool/backend.md#make_pool_backend._gather), [`_pages_per_seq`](pool/pack.md#_pages_per_seq), [`debug_flags`](module.md#Module.debug_flags), [`tunables`](module.md#Module.tunables), [`with_cache`](pool/config.md#with_cache), [`weights`](module.md#Module.weights), [`_can_pool_gather`](pool/backend.md#make_pool_backend._can_pool_gather), [`extra_inputs`](module.md#Module.extra_inputs), [`outputs`](module.md#Module.outputs), [`smalls`](module.md#Module.smalls), [`states`](module.md#Module.states), [`scratch`](module.md#Module.scratch), [`RecChunk`](pool/backend.md#RecChunk), [`ex`](planner.md#Plan.ex), [`plan_params`](module.md#Module.plan_params), [`shared_widths`](module.md#Module.shared_widths), [`host_update_states`](module.md#Module.host_update_states)

### <a id="Tiles"></a>`Tiles`
- def: [`src/vllm_torchtpu/megakernel/exec_spec.py:51`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L51)
- doc: Core execution tiling, ring depths, budgets and collectives.
- signature: `class Tiles:`
- members:
  - <a id="Tiles.module"></a>`module(self, name: str, cls: type[_T] | None = None)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L87) — Tunables of module `name` (class defaults when unset).
  - <a id="Tiles.with_modules"></a>`with_modules(self, updates: Mapping[str, Any])` — [`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L104) — Copy with module tunables replaced: `{module name: {field: value}}`.
  - <a id="Tiles.bank"></a>`bank` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L59)
  - <a id="Tiles.bounds_checks"></a>`bounds_checks` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L65)
  - <a id="Tiles.dense_acc_pair"></a>`dense_acc_pair` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L77)
  - <a id="Tiles.dmm_unroll"></a>`dmm_unroll` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L78)
  - <a id="Tiles.ebank"></a>`ebank` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L62)
  - <a id="Tiles.hier"></a>`hier` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L69)
  - <a id="Tiles.inplace"></a>`inplace` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L67)
  - <a id="Tiles.lazy"></a>`lazy` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L66)
  - <a id="Tiles.mb8"></a>`mb8` — [`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L71)
  - <a id="Tiles.modules"></a>`modules` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L81)
  - <a id="Tiles.nbd"></a>`nbd` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L60)
  - <a id="Tiles.nbe"></a>`nbe` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L61)
  - <a id="Tiles.rel_fetch"></a>`rel_fetch` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L79)
  - <a id="Tiles.rsag"></a>`rsag` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L68)
  - <a id="Tiles.smem_mib"></a>`smem_mib` — [`L64`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L64)
  - <a id="Tiles.vmem_mib"></a>`vmem_mib` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L63)
  - <a id="Tiles.war"></a>`war` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L70)
  - <a id="Tiles.wide_rows"></a>`wide_rows` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L74)
- protocol/private: <a id="Tiles.__post_init__"></a>`__post_init__`[`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L83)
- uses (calls/refs, reference-scoped): [`TunablesMap`](module_options.md#TunablesMap), [`tunables_class`](module_options.md#tunables_class), [`_T`](exec_spec.md#_T)
- used by: [`plan`](planner.md#plan), [`scatter_pool_states`](pool/scatter.md#scatter_pool_states), [`gather_gdn_states`](pool/gather.md#gather_gdn_states), [`default_tiles`](profiles/default.md#default_tiles), [`resolved_tiles`](exec_spec.md#ExecSpec.resolved_tiles), [`tunables`](module.md#Module.tunables), [`tiles_for`](profile.md#Profile.tiles_for), [`MB`](exec_spec.md#ExecSpec.MB), [`WIDE`](exec_spec.md#ExecSpec.WIDE), [`_knob`](profile.md#_knob), [`default_tiles`](exec_spec.md#default_tiles), [`resolve_tiles`](exec_spec.md#ExecSpec.resolve_tiles), [`tiles`](exec_spec.md#ExecSpec.tiles), [`TileRule`](profile.md#TileRule)

## Functions
- <a id="default_tiles"></a>`default_tiles(B: int, **kw: Any)` — [`L154`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L154) — Model-agnostic default tiles (`profiles/default.py:default_tiles`).
- <a id="tile_numerics"></a>`tile_numerics()` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L146) — Numerics class of every tile knob: core fields plus `<module>.<field>`.

## Module values
- <a id="MAX_BATCH_ROWS"></a>`MAX_BATCH_ROWS` — [`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L183)
- <a id="TILE_NUMERICS.TILE_NUMERICS"></a>`TILE_NUMERICS` — [`L125`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L125)
- <a id="_T"></a>`_T` — [`L44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L44)
- <a id="__all__"></a>`__all__` — [`L260`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/exec_spec.py#L260)

