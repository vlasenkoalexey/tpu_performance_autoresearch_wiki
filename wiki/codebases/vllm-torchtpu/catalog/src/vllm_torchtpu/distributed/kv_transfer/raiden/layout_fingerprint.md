---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.layout_fingerprint`/
symbols:
  measured_fa_layout_fingerprint: measured_fa_layout_fingerprint().
  _measure_packed_row_layouts: _measure_packed_row_layouts().
  measured_kimi_k3_layout_fingerprint: measured_kimi_k3_layout_fingerprint().
  fa_page_tokens: fa_page_tokens().
  measured_glm_layout_fingerprint: measured_glm_layout_fingerprint().
  measured_dsv4_layout_fingerprint: measured_dsv4_layout_fingerprint().
  expected_fa_minor_to_major: expected_fa_minor_to_major().
  _row_major_minor_to_major: _row_major_minor_to_major().
  EXPECTED_FA_TILES: EXPECTED_FA_TILES.
  canonical_layout_fingerprint: canonical_layout_fingerprint().
  EXPECTED_FA_MINOR_TO_MAJOR: EXPECTED_FA_MINOR_TO_MAJOR.
  EXPECTED_BLOCK_MAJOR_FA_MINOR_TO_MAJOR: EXPECTED_BLOCK_MAJOR_FA_MINOR_TO_MAJOR.
  ROW_CACHE_MINOR_TO_MAJOR: ROW_CACHE_MINOR_TO_MAJOR.
  _default_layout_getter: _default_layout_getter().
  FA_LAYOUT_FINGERPRINT_SCHEMA: FA_LAYOUT_FINGERPRINT_SCHEMA.
  GLM_MLA_LAYOUT_FINGERPRINT_SCHEMA: GLM_MLA_LAYOUT_FINGERPRINT_SCHEMA.
  KIMI_K3_LAYOUT_FINGERPRINT_SCHEMA: KIMI_K3_LAYOUT_FINGERPRINT_SCHEMA.
  DSV4_LAYOUT_FINGERPRINT_SCHEMA: DSV4_LAYOUT_FINGERPRINT_SCHEMA.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py)

## Functions
- <a id="_default_layout_getter"></a>`_default_layout_getter(tensor: Any)` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L120)
- <a id="_measure_packed_row_layouts"></a>`_measure_packed_row_layouts(manifest: PoolManifest, *, page_tokens: int | None, layout_getter: Callable[[Any], Any] | None, include_page_shape: bool)` — [`L345`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L345) — Validate live packed-row storage for the model-specific fingerprints.
- <a id="_row_major_minor_to_major"></a>`_row_major_minor_to_major(rank: int)` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L45) — Row-major order for a rank-``rank`` tensor.
- <a id="canonical_layout_fingerprint"></a>`canonical_layout_fingerprint(value: str | Mapping[str, Any])` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L67) — Return a stable identity for a calibrated physical-layout payload.
- <a id="expected_fa_minor_to_major"></a>`expected_fa_minor_to_major(kv_layout: str | None)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L108) — Returns the expected FA minor-to-major dimension order for ``kv_layout``.
- <a id="fa_page_tokens"></a>`fa_page_tokens(manifest: PoolManifest)` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L82) — Derive and validate the common page geometry of every FA pool.
- <a id="measured_dsv4_layout_fingerprint"></a>`measured_dsv4_layout_fingerprint(manifest: PoolManifest, *, layout_getter: Callable[[Any], Any] | None = None, package_version: Callable[[str], str] | None = None)` — [`L321`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L321) — Fingerprint of the admitted DeepSeek-V4 cache layout.
- <a id="measured_fa_layout_fingerprint"></a>`measured_fa_layout_fingerprint(manifest: PoolManifest, *, block_major: bool = False, layout_getter: Callable[[Any], Any] | None = None, package_version: Callable[[str], str] | None = None)` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L126) — Measure the admitted FA storage layout and return its E0' identity.
- <a id="measured_glm_layout_fingerprint"></a>`measured_glm_layout_fingerprint(manifest: PoolManifest, *, page_tokens: int, layout_getter: Callable[[Any], Any] | None = None, package_version: Callable[[str], str] | None = None, hash_indexer: bool = True)` — [`L284`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L284) — Fingerprint of the admitted GLM cache layout, compared across peers.
- <a id="measured_kimi_k3_layout_fingerprint"></a>`measured_kimi_k3_layout_fingerprint(manifest: PoolManifest, *, page_tokens: int, state_fragment_heads: int, state_fragments: int, layout_getter: Callable[[Any], Any] | None = None, package_version: Callable[[str], str] | None = None)` — [`L227`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L227) — Normalize the existing packed-row fingerprint across Kimi TP sizes.

## Module values
- <a id="DSV4_LAYOUT_FINGERPRINT_SCHEMA"></a>`DSV4_LAYOUT_FINGERPRINT_SCHEMA` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L64)
- <a id="EXPECTED_BLOCK_MAJOR_FA_MINOR_TO_MAJOR"></a>`EXPECTED_BLOCK_MAJOR_FA_MINOR_TO_MAJOR` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L58)
- <a id="EXPECTED_FA_MINOR_TO_MAJOR"></a>`EXPECTED_FA_MINOR_TO_MAJOR` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L57)
- <a id="EXPECTED_FA_TILES"></a>`EXPECTED_FA_TILES` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L60)
- <a id="FA_LAYOUT_FINGERPRINT_SCHEMA"></a>`FA_LAYOUT_FINGERPRINT_SCHEMA` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L61)
- <a id="GLM_MLA_LAYOUT_FINGERPRINT_SCHEMA"></a>`GLM_MLA_LAYOUT_FINGERPRINT_SCHEMA` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L62)
- <a id="KIMI_K3_LAYOUT_FINGERPRINT_SCHEMA"></a>`KIMI_K3_LAYOUT_FINGERPRINT_SCHEMA` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L63)
- <a id="ROW_CACHE_MINOR_TO_MAJOR"></a>`ROW_CACHE_MINOR_TO_MAJOR` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L59)
- <a id="__all__"></a>`__all__` — [`L209`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/layout_fingerprint.py#L209)

