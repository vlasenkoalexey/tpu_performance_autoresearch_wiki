---
title: 'Module: torchtitan/experiments/jax/splash_attn.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/splash_attn.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.splash_attn`/
symbols:
  make_splash_attention_fn: make_splash_attention_fn().
  logger: logger.
  build_splash_attention_callable: build_splash_attention_callable().
  build_splash_attention_callable._wrap_flash_attention: build_splash_attention_callable()._wrap_flash_attention().
  P: P.
  _build_splash_config: _build_splash_config().
---
# Module: [`torchtitan/experiments/jax/splash_attn.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py)

## Functions
- <a id="_build_splash_config"></a>`_build_splash_config(config, query_shape, key_shape, attn_logits_soft_cap)` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L18)
- <a id="build_splash_attention_callable._wrap_flash_attention"></a>`_wrap_flash_attention(query, key, value, segment_ids)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L63)
- <a id="build_splash_attention_callable"></a>`build_splash_attention_callable(mesh, q_sharding, config, *, apply_shard_map: bool = True, attn_logits_soft_cap: float | None = None, local_window: int | None = None)` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L41) — Return a jitted, sharded splash-attention callable. — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="make_splash_attention_fn"></a>`make_splash_attention_fn(mesh, splash_cfg, *, local_window: int | None = None)` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L106) — Build a splash-attention callable for the jax experiment. — documented in [jax-lane](../../../../concepts/jax-lane.md)

## Module values
- <a id="P"></a>`P` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L15)
- <a id="logger"></a>`logger` — [`L13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/splash_attn.py#L13)

