---
title: Avoiding host syncs in training loops (detach-and-accumulate)
type: doc-concept
provenance: doc
source: docs/markdown/porting_vit_mnist.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Avoiding host syncs in training loops (detach-and-accumulate)

## Definition
The ViT/MNIST porting tutorial's one explicit performance rule: do not pull a scalar back to the host every step. Instead of `epoch_loss += loss.item()`, accumulate `epoch_loss += loss.detach()` on the device and call `.item()` once per epoch. The doc's rationale is that per-step materialization "stalls the CPU" and pays an expensive TPU -> CPU DMA each iteration; batching it amortizes the transfer.

## In torch_tpu (grounded)
- `.item()` lowers to `aten::_local_scalar_dense`, implemented by [`AtenLocalScalarDense`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenLocalScalarDense "csrc/ops/copy_from/copy_from_aten_kernels.cc:L254"); `.cpu()` goes through [`AtenCopyFrom`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#AtenCopyFrom "csrc/ops/copy_from/copy_from_aten_kernels.cc:L232") with copy type [`kTpuToCpu`](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md#CopyType.kTpuToCpu "csrc/ops/copy_from/copy_from_aten_kernels.cc:L58") into [`CopyTpuToCpu`](../catalog/csrc/ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu "csrc/ops/copy_from/tpu_to_cpu.cc:L77"). Both block the Python thread until the value exists on the host.
- Under a deferring eager mode, a host read is also a materialization trigger: queued work must be compiled and run first ([`MaterializeAndReturn`](../catalog/csrc/eager/tensor_to_buffer.cc.md#MaterializeAndReturn "csrc/eager/tensor_to_buffer.cc:L663"); the reason is recorded as a [`MaterializationReason`](../catalog/csrc/eager/structured_log_buffer.h.md#MaterializationReason "csrc/eager/structured_log_buffer.h:L36")). A per-step `.item()` therefore cuts every step's deferred graph at the loss and serializes host and device.
- `loss.detach()` + device-side `+=` is just another TPU op, so the accumulation stays asynchronous.

## Why it matters / when it applies
- Applies to any logging, metric, early-stopping or `if tensor:` check inside the step. Each one is a host round trip plus, in deferred modes, a graph boundary.
- The tutorial's other porting notes: build the model with ordinary `nn` modules and move it with `model.to(device)`; move each batch with `.to(device)` (the tutorial slices CPU tensors then copies - a real input pipeline should use a `DataLoader`); a standard `torch.optim.Adam` and `nn.CrossEntropyLoss` work unchanged. For faster optimizer steps see the fused kernels in [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md).
- Inference runs under `model.eval()` + `torch.no_grad()` and pulls the single prediction back with `.argmax(...).cpu().item()` - one sync per request, which is fine.
- The tutorial also filters a PJRT warning about `.grad` on non-leaf tensors during training; it is noise, not a correctness issue.
- Attention in the tutorial is hand-written for a reason covered in [sdpa-backend-selection-when-porting](sdpa-backend-selection-when-porting.md).

## Connections
- Code concepts: [tensor-synchronization](../concepts/tensor-synchronization.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [host-device-copy](../concepts/host-device-copy.md), [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [batch-host-device-transfer](../concepts/batch-host-device-transfer.md), [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md)
- Module catalogs: [csrc/ops/copy_from/copy_from_aten_kernels.cc](../catalog/csrc/ops/copy_from/copy_from_aten_kernels.cc.md), [csrc/ops/copy_from/tpu_to_cpu.cc](../catalog/csrc/ops/copy_from/tpu_to_cpu.cc.md), [csrc/eager/tensor_to_buffer.cc](../catalog/csrc/eager/tensor_to_buffer.cc.md)
- Related doc-concepts: [sdpa-backend-selection-when-porting](sdpa-backend-selection-when-porting.md), [tpu-device-backend-initialization](tpu-device-backend-initialization.md), [defer-and-fuse-materialization](defer-and-fuse-materialization.md), [eager-execution-modes](eager-execution-modes.md), [trace-red-flags](trace-red-flags.md)

## Source
Extracted from `docs/markdown/porting_vit_mnist.md` (kept in place).
