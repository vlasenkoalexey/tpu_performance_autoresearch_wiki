---
title: SingleTraceTrainer - the whole train step as one compiled graph
type: doc-concept
provenance: doc
source: docs/markdown/advanced_compile.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# SingleTraceTrainer - the whole train step as one compiled graph

## Definition
`torch.tpu.optimizers.SingleTraceTrainer` fuses forward, loss, backward and optimizer update into **one static FX graph** so that `torch.compile(..., fullgraph=True)` succeeds with zero graph breaks and the step runs as a single TPU offload. The doc lists its three mechanisms: (1) reverse-mode autodiff done symbolically with `torch.func.grad_and_value` (instead of the eager autograd engine that breaks Dynamo), (2) **functional** optimizer updates (`AdamW` or `Sgd` from `torch.tpu.optimizers`), and (3) capture of the full pipeline with `make_fx`. Usage: build the trainer with a model and optimizer, then `trainer.make_compiled_train_step(x, target, compile_fn=...)`, where `compile_fn` receives the traced graph module and returns e.g. `torch.compile(gm, backend="tpu", dynamic=False, fullgraph=True)`.

## In torch_tpu (grounded)
- [`SingleTraceTrainer`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer) - its docstring: "captures the entire training loop ... into a single functional graph using `make_fx`. This graph is then compiled and executed as a single unit (offload), reducing interpreter overhead and enabling better fusion opportunities by the compiler." Constructor ([`SingleTraceTrainer.__init__`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer.__init__)) takes `model`, `optimizer` (if `None`, only gradients are computed into `param.grad`), a default `compile_fn`, and an optional `compute_loss_fn(model, args, kwargs)`; it calls `model.tie_weights()` if present.
- [`SingleTraceTrainer.make_compiled_train_step`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer.make_compiled_train_step) traces the pure tensor-level step ([`SingleTraceTrainer.flattened_stateless_train_step`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer.flattened_stateless_train_step)) with `make_fx` and hands the result to `compile_fn` (required either here or at construction). [`SingleTraceTrainer.train_step`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#SingleTraceTrainer.train_step) is the uncompiled functional step.
- Functional optimizers usable inside the trace: [`AdamW`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#AdamW), [`Sgd`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#Sgd) and [`Muon`](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md#Muon) (the doc shows `AdamW(use_bfloat16_moments=False)`; bf16 moments are an optimizer-state memory knob).

## Why it matters / when it applies
- The standard `loss.backward(); optimizer.step()` loop under `torch.compile` produces several programs (forward, AOT backward, optimizer) plus interpreter work between them; one trace lets XLA schedule and fuse across the forward/backward/update boundary and removes per-step host dispatch gaps.
- Use it when the training step is the hot loop and the model is traceable with `make_fx` (no data-dependent Python control flow). Shapes still have to be static ([torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md)).
- The doc's `compile_and_verify_breaks` pattern - run `torch._dynamo.explain` on the traced module inside `compile_fn` - is a cheap guard that the step really is one graph ([graph-breaks-on-tpu.md](graph-breaks-on-tpu.md)).
- Alternative with the stock optimizer path: eager `torch.optim` with `capturable=True` and the fused optimizer kernels ([fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md)).

## Connections
- Code concepts: [python-optimizers](../concepts/python-optimizers.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md), [compiled-mode](../concepts/compiled-mode.md), [fx-graph-passes](../concepts/fx-graph-passes.md)
- Module catalogs: [src/torch_tpu/_internal/optimizers/single_trace_trainer](../catalog/src/torch_tpu/_internal/optimizers/single_trace_trainer.md), [src/torch_tpu/_internal/optimizers/adamw](../catalog/src/torch_tpu/_internal/optimizers/adamw.md), [src/torch_tpu/_internal/optimizers/sgd](../catalog/src/torch_tpu/_internal/optimizers/sgd.md)
- Related doc-concepts: [graph-breaks-on-tpu.md](graph-breaks-on-tpu.md), [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md)

## Source
Extracted from `docs/markdown/advanced_compile.md` (section 4) (kept in place).
