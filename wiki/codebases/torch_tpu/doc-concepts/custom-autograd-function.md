---
title: Custom backward passes (torch.autograd.Function vs custom-op register_autograd)
type: doc-concept
provenance: doc
source: docs/markdown/customizing_autograd_via_torch_autograd_function.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Custom backward passes (torch.autograd.Function vs custom-op register_autograd)

## Definition
The doc presents `torch.autograd.Function` as the second rung of extending PyTorch: subclass it, override static `forward(ctx, ...)` and `backward(ctx, grad_output)`, save what the backward needs with `ctx.save_for_backward`, and call it through `.apply`. Its toy example is a sigmoid whose gradient is clamped to a floor (0.25 in the mid-range, 0.01 in the saturated tails) to avoid vanishing gradients; the forward output is identical to `torch.sigmoid`, only the gradient differs. The doc carries an explicit warning: in PyTorch 2.x, custom ops have first-class support and should *not* be implemented with `torch.autograd.Function` (that was the PyTorch 1.0 mechanism).

## In torch_tpu (grounded)
- The example itself is pure PyTorch: it runs on CPU tensors and compiles with `torch.compile(..., backend="aot_eager")`, with `torch._logging.set_logs(aot_graphs=True)` to print the forward/backward graphs AOTAutograd produces. There is no torch_tpu symbol involved; the same `Function` works unchanged on `"tpu"` tensors because its body is ordinary ATen ops ([eager-op-dispatch](../concepts/eager-op-dispatch.md)).
- On TPU, swapping `backend="aot_eager"` for `backend="tpu"` routes the traced forward/backward graphs to the TorchTPU backend ([`TpuBackend.__call__`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend.__call__ "src/torch_tpu/_internal/compile/_backend.py:L654")); a `Function` is inlined by dynamo/AOTAutograd, so its backward is traced and compiled with the rest of the graph.
- The custom-op path the warning points to is what torch_tpu uses for kernels: [`jax_op`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#jax_op) returns a `CustomOpDef` subclass ([`_JaxCustomOpDef`](../catalog/src/torch_tpu/_internal/pallas/pallas.md#_JaxCustomOpDef)), and the backward is attached with `register_autograd(backward, setup_context=...)` instead of a `Function` subclass ([pallas-jax-op-bridge](pallas-jax-op-bridge.md)).

## Why it matters / when it applies
- **Use `autograd.Function` for gradient rewrites composed of existing ops** (clamping, straight-through tricks, custom recompute) - it is traceable and costs nothing extra once compiled.
- **Use a custom op + `register_autograd` when the forward is an opaque kernel** (Pallas/JAX): AOTAutograd needs a fake kernel for both directions, which `jax_op` supplies; wrapping an opaque kernel in an `autograd.Function` is the legacy pattern the doc warns against.
- `ctx.save_for_backward` decides what is kept alive between forward and backward - saving the output (as the sigmoid example does) rather than the input is a memory/recompute choice that carries over to TPU HBM budgeting.
- For TPU perf inspection, the doc's `aot_graphs` logging is the cheap way to confirm the backward graph contains only the intended ops before looking at HLO.

## Connections
- Code concepts: [torch-compile-backend](../concepts/torch-compile-backend.md), [fx-graph-passes](../concepts/fx-graph-passes.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [eager-op-dispatch](../concepts/eager-op-dispatch.md)
- Module catalogs: [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md), [src/torch_tpu/_internal/pallas/pallas](../catalog/src/torch_tpu/_internal/pallas/pallas.md)
- Related doc-concepts: [pytorch-extension-ladder](pytorch-extension-ladder.md), [extending-via-composition](extending-via-composition.md), [pallas-jax-op-bridge](pallas-jax-op-bridge.md)

## Source
Extracted from `docs/markdown/customizing_autograd_via_torch_autograd_function.md` (kept in place).
