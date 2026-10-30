---
title: 'Module: csrc/distributed/handshake.h'
type: catalog
provenance: extracted
module: csrc/distributed/handshake.h
status: fresh
symbol_base: cxx . . $ torch_tpu/HandshakeStage#
symbols:
  HandshakeStage: ''
  HandshakeStage.kDispatchStage: kDispatchStage.
  HandshakeStage.kCompileStage: kCompileStage.
  HandshakeStage.kOff: kOff.
---
# Module: [`csrc/distributed/handshake.h`](../../../../../../raw/code/torch_tpu/csrc/distributed/handshake.h)

## Classes
### <a id="HandshakeStage"></a>`HandshakeStage`
- def: [`csrc/distributed/handshake.h:23`](../../../../../../raw/code/torch_tpu/csrc/distributed/handshake.h#L23)
- doc: Options for TORCH_TPU_SPMD_HANDSHAKE_STAGE.
- signature: `enum class HandshakeStage`
- members:
  - <a id="HandshakeStage.kCompileStage"></a>`kCompileStage` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/distributed/handshake.h#L25)
  - <a id="HandshakeStage.kDispatchStage"></a>`kDispatchStage` — [`L26`](../../../../../../raw/code/torch_tpu/csrc/distributed/handshake.h#L26)
  - <a id="HandshakeStage.kOff"></a>`kOff` — [`L24`](../../../../../../raw/code/torch_tpu/csrc/distributed/handshake.h#L24)
- uses (calls/refs, reference-scoped): [`GetHandshakeStageEnvVarOnce`](handshake.cc.md#GetHandshakeStageEnvVarOnce)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`GetHandshakeStageEnvVarOnce`](handshake.cc.md#GetHandshakeStageEnvVarOnce)

