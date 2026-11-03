---
title: 'Module: src/vllm_torchtpu/megakernel/profile.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/profile.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.profile`/
symbols:
  approx_features: approx_features().
  Profile.exec_for: Profile#exec_for().
  Profile.name: Profile#name.
  DEFAULT_PROFILE: DEFAULT_PROFILE.
  Profile.__post_init__: Profile#__post_init__().
  register_profile: register_profile().
  Profile.model: Profile#model.
  Profile.tile_rule: Profile#tile_rule().
  _REGISTRY._REGISTRY: _REGISTRY._REGISTRY.
  _check_exact: _check_exact().
  Profile.with_overrides: Profile#with_overrides().
  Profile: Profile#
  model_default_profile: model_default_profile().
  Profile.tiles_for: Profile#tiles_for().
  get_profile: get_profile().
  Profile.model_default: Profile#model_default.
  _MODEL_DEFAULTS._MODEL_DEFAULTS: _MODEL_DEFAULTS._MODEL_DEFAULTS.
  Profile.pool_gather: Profile#pool_gather.
  _knob: _knob().
  Profile.numerics: Profile#numerics.
  Profile.tiles: Profile#tiles.
  Profile.fused_pool_io: Profile#fused_pool_io.
  TileRule: TileRule.
  _NUMERICS_GRID_B: _NUMERICS_GRID_B.
  list_profiles: list_profiles().
  Profile.baseline: Profile#baseline.
  DEFAULT_PROFILE_NAME: DEFAULT_PROFILE_NAME.
  _DERIVED_PROFILE_FIELDS: _DERIVED_PROFILE_FIELDS.
  Baseline: Baseline#
  Profile.description: Profile#description.
  _NUMERICS_GRID_R: _NUMERICS_GRID_R.
  Baseline.ref: Baseline#ref.
  Baseline.commit: Baseline#commit.
  Baseline.job: Baseline#job.
  Baseline.config: Baseline#config.
  Baseline.bench: Baseline#bench.
  Profile.buckets: Profile#buckets.
  Profile.verify_buckets: Profile#verify_buckets.
  Profile.fused_pool_io_max_b: Profile#fused_pool_io_max_b.
  Profile.fused_pool_io_min_b_hi: Profile#fused_pool_io_min_b_hi.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/profile.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py)

## Classes
### <a id="Baseline"></a>`Baseline`
- def: [`src/vllm_torchtpu/megakernel/profile.py:65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L65)
- doc: Provenance of the reference a profile is tuned against.
- signature: `class Baseline:`
- members:
  - <a id="Baseline.bench"></a>`bench` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L72)
  - <a id="Baseline.commit"></a>`commit` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L69)
  - <a id="Baseline.config"></a>`config` — [`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L71)
  - <a id="Baseline.job"></a>`job` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L70)
  - <a id="Baseline.ref"></a>`ref` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L68)
- used by: [`baseline`](profile.md#Profile.baseline)

### <a id="Profile"></a>`Profile`
- def: [`src/vllm_torchtpu/megakernel/profile.py:76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L76)
- doc: Named bundle of execution tuning (tiles, flags, buckets, pool I/O).
- signature: `class Profile:`
- members:
  - <a id="Profile.exec_for"></a>`exec_for(self, base: ExecSpec, *, B: int, T: int, g: Any = None)` — [`L179`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L179) — Specialize `base` for bucket `(T, B)` under this profile. — documented in [megakernel-pool](../../../../concepts/megakernel-pool.md)
  - <a id="Profile.tile_rule"></a>`tile_rule(self)` — [`L158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L158) — This profile's tile rule (None: the library default rule).
  - <a id="Profile.tiles_for"></a>`tiles_for(self, B: int, *, R: int, moe_tp: bool = False)` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L170) — Return this profile's tiles for a bucket of `B` rows on `R` ranks.
  - <a id="Profile.with_overrides"></a>`with_overrides(self, **overrides: Any)` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L130) — Return this profile with `overrides` applied, re-labelled if changed.
  - <a id="Profile.baseline"></a>`baseline` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L99)
  - <a id="Profile.buckets"></a>`buckets` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L87)
  - <a id="Profile.description"></a>`description` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L100)
  - <a id="Profile.fused_pool_io"></a>`fused_pool_io` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L92)
  - <a id="Profile.fused_pool_io_max_b"></a>`fused_pool_io_max_b` — [`L93`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L93)
  - <a id="Profile.fused_pool_io_min_b_hi"></a>`fused_pool_io_min_b_hi` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L94)
  - <a id="Profile.model"></a>`model` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L80)
  - <a id="Profile.model_default"></a>`model_default` — [`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L103)
  - <a id="Profile.name"></a>`name` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L79)
  - <a id="Profile.numerics"></a>`numerics` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L81)
  - <a id="Profile.pool_gather"></a>`pool_gather` — [`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L98)
  - <a id="Profile.tiles"></a>`tiles` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L86)
  - <a id="Profile.verify_buckets"></a>`verify_buckets` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L88)
- protocol/private: <a id="Profile.__post_init__"></a>`__post_init__`[`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L105)
- uses (calls/refs, reference-scoped): [`cache_exec`](pool/config.md#cache_exec), [`ExecSpec`](exec_spec.md#ExecSpec), [`approx_features`](profile.md#approx_features), [`default_tiles`](profiles/default.md#default_tiles), [`_check_exact`](profile.md#_check_exact), [`Tiles`](exec_spec.md#Tiles), [`model_default_profile`](profile.md#model_default_profile), [`R`](exec_spec.md#ExecSpec.R), [`pool_gather`](pool/config.md#CacheExec.pool_gather), [`with_cache`](pool/config.md#with_cache), [`tiles`](exec_spec.md#ExecSpec.tiles), [`TileRule`](profile.md#TileRule), [`Baseline`](profile.md#Baseline), [`_DERIVED_PROFILE_FIELDS`](profile.md#_DERIVED_PROFILE_FIELDS)
- used by: [`approx_features`](profile.md#approx_features), [`DEFAULT_PROFILE`](profile.md#DEFAULT_PROFILE), [`register_profile`](profile.md#register_profile), [`_REGISTRY`](profile.md#_REGISTRY._REGISTRY), [`_check_exact`](profile.md#_check_exact), [`model_default_profile`](profile.md#model_default_profile), [`get_profile`](profile.md#get_profile)

## Functions
- <a id="_check_exact"></a>`_check_exact(profile: Profile)` — [`L230`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L230)
- <a id="_knob"></a>`_knob(t: Tiles, key: str)` — [`L222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L222) — Value of tile knob `key` (`field` or `<module>.<field>`) in `t`.
- <a id="approx_features"></a>`approx_features(profile: Profile)` — [`L240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L240) — Approx-class features `profile` turns on relative to its reference. — documented in [megakernel-pool](../../../../concepts/megakernel-pool.md)
- <a id="get_profile"></a>`get_profile(name: str | Profile | None)` — [`L376`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L376) — Resolve a profile by name (`None` / `""` -> `default`).
- <a id="list_profiles"></a>`list_profiles()` — [`L371`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L371) — Return the names of all registered profiles.
- <a id="model_default_profile"></a>`model_default_profile(model: str | None)` — [`L365`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L365) — The default profile of `model`, else `default`.
- <a id="register_profile"></a>`register_profile(profile: Profile, *, replace: bool = False)` — [`L304`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L304) — Register `profile` by name (`replace=True` to overwrite an existing one).

## Module values
- <a id="DEFAULT_PROFILE"></a>`DEFAULT_PROFILE` — [`L291`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L291)
- <a id="DEFAULT_PROFILE_NAME"></a>`DEFAULT_PROFILE_NAME` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L57)
- <a id="TileRule"></a>`TileRule` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L59)
- <a id="_DERIVED_PROFILE_FIELDS"></a>`_DERIVED_PROFILE_FIELDS` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L61)
- <a id="_MODEL_DEFAULTS._MODEL_DEFAULTS"></a>`_MODEL_DEFAULTS` — [`L215`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L215)
- <a id="_NUMERICS_GRID_B"></a>`_NUMERICS_GRID_B` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L218)
- <a id="_NUMERICS_GRID_R"></a>`_NUMERICS_GRID_R` — [`L219`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L219)
- <a id="_REGISTRY._REGISTRY"></a>`_REGISTRY` — [`L213`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L213)
- <a id="__all__"></a>`__all__` — [`L389`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/profile.py#L389)

