---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.tags`/
symbols:
  class_tag: class_tag().
  TAG_FA: TAG_FA.
  TAG_GDN_CONV: TAG_GDN_CONV.
  TAG_GDN_SSM: TAG_GDN_SSM.
  libtpu_key: libtpu_key().
  TAG_MLA_NOPE: TAG_MLA_NOPE.
  TAG_MLA_ROPE: TAG_MLA_ROPE.
  TAG_DSV4_CSA_NOPE: TAG_DSV4_CSA_NOPE.
  layer_tag: layer_tag().
  split_layer_tag: split_layer_tag().
  TAG_DSA_IDX: TAG_DSA_IDX.
  TAG_DSV4_IDX: TAG_DSV4_IDX.
  TAG_DSV4_HCA: TAG_DSV4_HCA.
  TAG_DSV4_CSA_ROPE: TAG_DSV4_CSA_ROPE.
  TAG_DSV4_SWA: TAG_DSV4_SWA.
  TAG_DSV4_STATE_CSA: TAG_DSV4_STATE_CSA.
  TAG_DSV4_STATE_IDX: TAG_DSV4_STATE_IDX.
  TAG_DSV4_STATE_HCA: TAG_DSV4_STATE_HCA.
  dsv4_group_tag: dsv4_group_tag().
  _LAYER_SUFFIX: _LAYER_SUFFIX.
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py)

## Functions
- <a id="class_tag"></a>`class_tag(tag: str)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L74) — The tag with any per-layer suffix removed.
- <a id="dsv4_group_tag"></a>`dsv4_group_tag(base_tag: str, group_index: int)` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L47) — ``dsv4.swa`` + group 3 -> ``dsv4.swa.g3``.
- <a id="layer_tag"></a>`layer_tag(tag: str, layer_index: int)` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L59) — Tag of one layer's pool under the per-layer tagging policy.
- <a id="libtpu_key"></a>`libtpu_key(package_version: Callable[[str], str] | None)` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L79) — libtpu identity for a layout fingerprint.
- <a id="split_layer_tag"></a>`split_layer_tag(tag: str)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L66) — (class tag, layer index) of a tag; the index is None when absent.

## Module values
- <a id="TAG_DSA_IDX"></a>`TAG_DSA_IDX` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L27)
- <a id="TAG_DSV4_CSA_NOPE"></a>`TAG_DSV4_CSA_NOPE` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L35)
- <a id="TAG_DSV4_CSA_ROPE"></a>`TAG_DSV4_CSA_ROPE` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L36)
- <a id="TAG_DSV4_HCA"></a>`TAG_DSV4_HCA` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L38)
- <a id="TAG_DSV4_IDX"></a>`TAG_DSV4_IDX` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L37)
- <a id="TAG_DSV4_STATE_CSA"></a>`TAG_DSV4_STATE_CSA` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L42)
- <a id="TAG_DSV4_STATE_HCA"></a>`TAG_DSV4_STATE_HCA` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L44)
- <a id="TAG_DSV4_STATE_IDX"></a>`TAG_DSV4_STATE_IDX` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L43)
- <a id="TAG_DSV4_SWA"></a>`TAG_DSV4_SWA` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L39)
- <a id="TAG_FA"></a>`TAG_FA` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L24)
- <a id="TAG_GDN_CONV"></a>`TAG_GDN_CONV` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L25)
- <a id="TAG_GDN_SSM"></a>`TAG_GDN_SSM` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L26)
- <a id="TAG_MLA_NOPE"></a>`TAG_MLA_NOPE` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L28)
- <a id="TAG_MLA_ROPE"></a>`TAG_MLA_ROPE` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L29)
- <a id="_LAYER_SUFFIX"></a>`_LAYER_SUFFIX` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/tags.py#L56)

