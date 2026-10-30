---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4`/
symbols:
  _build_gemma4_layers: _build_gemma4_layers().
  _make_moe_config: _make_moe_config().
  _build_flavor_config: _build_flavor_config().
  model_registry: model_registry().
  _testmodel: _testmodel().
  _testmodel_moe: _testmodel_moe().
  _gemma4_lm_head: _gemma4_lm_head().
  _gemma4_norm: _gemma4_norm().
  _gemma4_factories: _gemma4_factories.
  _set_weight_tying: _set_weight_tying().
  gemma4_configs: gemma4_configs.
  _EMBEDDING_SKIP_INIT._EMBEDDING_SKIP_INIT: _EMBEDDING_SKIP_INIT._EMBEDDING_SKIP_INIT.
  _LOGIT_SOFT_CAP: _LOGIT_SOFT_CAP.
  _make_param_init: _make_param_init().
  _NORM_INIT._NORM_INIT: _NORM_INIT._NORM_INIT.
  _EMBEDDING_INIT._EMBEDDING_INIT: _EMBEDDING_INIT._EMBEDDING_INIT.
  _OUTPUT_INIT._OUTPUT_INIT: _OUTPUT_INIT._OUTPUT_INIT.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/__init__.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py)

## Functions
- <a id="_build_flavor_config"></a>`_build_flavor_config(flavor: str, attn_backend: str = "sdpa", use_fused_qkv: bool = False, moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, enable_sp: bool = True, enable_ep: bool = False, converters: list[ModelConfigConverter.Config] | None = None, enable_weight_tying: bool = True)` — [`L540`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L540)
- <a id="_build_gemma4_layers"></a>`_build_gemma4_layers(n_layers: int, dim: int, hidden_dim: int, n_heads: int, n_kv_heads: int, n_global_kv_heads: int, head_dim: int, global_head_dim: int, norm_eps: float, local_rope_theta: float = 10, global_rope_theta: float = 1, global_partial_rotary_factor: float = 0.25, max_seq_len: int = 131072, sliding_window_size: int = 1024, global_attn_every_n_layers: int = 6, use_k_eq_v_on_global: bool = True, moe_enabled: bool = False, num_experts: int = 128, top_k: int = 8, moe_inter_dim: int = 704, load_balance_coeff: float | None = None, aux_loss_coeff: float = 0, attn_backend: str = "sdpa", use_fused_qkv: bool = False, comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None)` — [`L165`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L165) — documented in [model-building-blocks](../../../../../../concepts/model-building-blocks.md)
- <a id="_gemma4_lm_head"></a>`_gemma4_lm_head(dim: int, vocab_size: int)` — [`L71`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L71)
- <a id="_gemma4_norm"></a>`_gemma4_norm(dim: int, eps: float = 0.000001)` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L80)
- <a id="_make_moe_config"></a>`_make_moe_config(*, dim: int, hidden_dim: int, num_experts: int, top_k: int, norm_eps: float, param_init: dict[str, dict[str, Callable]], comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, load_balance_coeff: float | None = None, aux_loss_coeff: float = 0)` — [`L104`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L104) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="_make_param_init"></a>`_make_param_init(depth: int)` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L86) — Create standard parameter initializers scaled by depth.
- <a id="_set_weight_tying"></a>`_set_weight_tying(config: Gemma4Model.Config, enable: bool)` — [`L528`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L528) — Tie ``lm_head`` to the token embedding (HF default) or untie it.
- <a id="_testmodel"></a>`_testmodel(attn_backend: str = "sdpa")` — [`L322`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L322)
- <a id="_testmodel_moe"></a>`_testmodel_moe(attn_backend: str = "sdpa", moe_comm_backend: str = "standard")` — [`L361`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L361)
- <a id="model_registry"></a>`model_registry(flavor: str, attn_backend: str = "sdpa", use_fused_qkv: bool = False, moe_comm_backend: str = "standard", non_blocking_capacity_factor: float | None = None, enable_sp: bool = True, enable_ep: bool = False, converters: list[ModelConfigConverter.Config] | None = None, enable_weight_tying: bool = True)` — [`L593`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L593)

## Module values
- <a id="_EMBEDDING_INIT._EMBEDDING_INIT"></a>`_EMBEDDING_INIT` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L61)
- <a id="_EMBEDDING_SKIP_INIT._EMBEDDING_SKIP_INIT"></a>`_EMBEDDING_SKIP_INIT` — [`L64`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L64)
- <a id="_LOGIT_SOFT_CAP"></a>`_LOGIT_SOFT_CAP` — [`L68`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L68)
- <a id="_NORM_INIT._NORM_INIT"></a>`_NORM_INIT` — [`L60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L60)
- <a id="_OUTPUT_INIT._OUTPUT_INIT"></a>`_OUTPUT_INIT` — [`L65`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L65)
- <a id="__all__"></a>`__all__` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L44)
- <a id="_gemma4_factories"></a>`_gemma4_factories` — [`L408`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L408)
- <a id="gemma4_configs"></a>`gemma4_configs` — [`L583`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/__init__.py#L583)

