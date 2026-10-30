---
title: 'Module: csrc/distributed/window_tpu.cc'
type: catalog
provenance: extracted
module: csrc/distributed/window_tpu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PySetWindowStripeChunkMb: PySetWindowStripeChunkMb(1624ee8275b10bda).
  PySetWindowNumStripes: PySetWindowNumStripes(d4f767463ce0a6b3).
  PyComputeWindowStripeCount: PyComputeWindowStripeCount(a9e4e82268fd7bfa).
  PyGetWindowStripeChunkMb: PyGetWindowStripeChunkMb(da6335ded91d79c2).
  PyGetWindowNumStripes: PyGetWindowNumStripes(b126dc7c1de90089).
  GetStripeChunkSizeBytes: '`$anonymous_namespace_csrc/distributed/window_tpu.cc`/GetStripeChunkSizeBytes(da6335ded91d79c2).'
  GetMaxStripes: '`$anonymous_namespace_csrc/distributed/window_tpu.cc`/GetMaxStripes(b126dc7c1de90089).'
  g_window_num_stripes: g_window_num_stripes.
  g_window_stripe_chunk_mb: g_window_stripe_chunk_mb.
---
# Module: [`csrc/distributed/window_tpu.cc`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc)

## Functions
- <a id="GetMaxStripes"></a>`GetMaxStripes()` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L76) — Retrieves maximum parallel DMA streams/stripes. Default is 4 (for TPU
- <a id="GetStripeChunkSizeBytes"></a>`GetStripeChunkSizeBytes()` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L70) — Retrieves configured stripe chunk size in bytes (minimum bytes per DMA
- <a id="PyComputeWindowStripeCount"></a>`PyComputeWindowStripeCount(int64_t total_bytes)` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L86) — Computes the optimal stripe count for a tensor of given byte size.
- <a id="PyGetWindowNumStripes"></a>`PyGetWindowNumStripes()` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L56)
- <a id="PyGetWindowStripeChunkMb"></a>`PyGetWindowStripeChunkMb()` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L64)
- <a id="PySetWindowNumStripes"></a>`PySetWindowNumStripes(int num_stripes)` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L50) — Sets and gets the maximum concurrent DMA stripes for WindowTpu peer — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)
- <a id="PySetWindowStripeChunkMb"></a>`PySetWindowStripeChunkMb(int64_t chunk_mb)` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L58) — Sets and gets the minimum payload size in MB per parallel DMA stripe.

## Module values
- <a id="g_window_num_stripes"></a>`g_window_num_stripes` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L47)
- <a id="g_window_stripe_chunk_mb"></a>`g_window_stripe_chunk_mb` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/distributed/window_tpu.cc#L48)

