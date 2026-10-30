---
title: 'Module: csrc/distributed/utils.cc'
type: catalog
provenance: extracted
module: csrc/distributed/utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ValidateReductionOp: ValidateReductionOp(8e31e58bae9c83c2).
  BuildReplicaGroupsAttr: BuildReplicaGroupsAttr(c5af8690386dffe9).
  EnterSpmdSafeRegion: EnterSpmdSafeRegion(49f6e7a06ebc5aa8).
  IsSpmdSafe: IsSpmdSafe(c9857a73d68e59ba).
  ExitSpmdSafeRegion: ExitSpmdSafeRegion(49f6e7a06ebc5aa8).
  BuildChannelHandleAttr: BuildChannelHandleAttr(bfff2f1eb4a6127).
---
# Module: [`csrc/distributed/utils.cc`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc)

## Functions
- <a id="BuildChannelHandleAttr"></a>`BuildChannelHandleAttr(mlir::MlirBuilder& builder, int handle, int type)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L60) — Given a channel handle and type, construct a MLIR constant used for the
- `BuildChannelHandleAttr(mlir::MlirBuilder& builder, int handle, int type)` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L60) — Given a channel handle and type, construct a MLIR constant used for the
- <a id="BuildReplicaGroupsAttr"></a>`BuildReplicaGroupsAttr(mlir::MlirBuilder& builder, const DeviceGroupList& device_groups)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L40) — Given device ids organized into (sub)groups, construct a MLIR constant
- <a id="EnterSpmdSafeRegion"></a>`EnterSpmdSafeRegion()` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L87) — Enter SPMD safe region by setting the top of the python thread stack
- <a id="ExitSpmdSafeRegion"></a>`ExitSpmdSafeRegion()` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L92) — Exit the SPMD safe region by popping the top of the python thread stack.
- <a id="IsSpmdSafe"></a>`IsSpmdSafe()` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L94) — Returns true if the current execution is within a SPMD safe region.
- <a id="ValidateReductionOp"></a>`ValidateReductionOp(c10d::ReduceOp reduce_op, c10::ScalarType scalar_type)` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/distributed/utils.cc#L66) — documented in [process-group-and-collectives](../../../concepts/process-group-and-collectives.md)

