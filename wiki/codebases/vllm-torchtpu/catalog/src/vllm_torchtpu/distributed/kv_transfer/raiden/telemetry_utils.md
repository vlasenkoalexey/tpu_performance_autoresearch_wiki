---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.telemetry_utils`/
symbols:
  parse_raiden_metric_key: parse_raiden_metric_key().
  normalize_raiden_metric_name: normalize_raiden_metric_name().
  RAIDEN_METRIC_PREFIX: RAIDEN_METRIC_PREFIX.
  _LABELED_METRIC_KEY_REGEX: _LABELED_METRIC_KEY_REGEX.
  _LABEL_PAIR_REGEX: _LABEL_PAIR_REGEX.
  _UNESCAPE_PATTERN: _UNESCAPE_PATTERN.
  _unescape_match: _unescape_match().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py)

## Functions
- <a id="_unescape_match"></a>`_unescape_match(match: re.Match)` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L28)
- <a id="normalize_raiden_metric_name"></a>`normalize_raiden_metric_name(name: str)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L55) — Ensures a Raiden metric name starts with RAIDEN_METRIC_PREFIX.
- <a id="parse_raiden_metric_key"></a>`parse_raiden_metric_key(raw_key: str)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L33) — Parses Prometheus text-formatted keys emitted by Raiden telemetry, e.g.:

## Module values
- <a id="RAIDEN_METRIC_PREFIX"></a>`RAIDEN_METRIC_PREFIX` — [`L19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L19)
- <a id="_LABELED_METRIC_KEY_REGEX"></a>`_LABELED_METRIC_KEY_REGEX` — [`L21`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L21)
- <a id="_LABEL_PAIR_REGEX"></a>`_LABEL_PAIR_REGEX` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L22)
- <a id="_UNESCAPE_PATTERN"></a>`_UNESCAPE_PATTERN` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/telemetry_utils.py#L25)

