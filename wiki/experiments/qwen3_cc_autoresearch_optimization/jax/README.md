# Qwen3 — jax lane

Native-JAX (Flax NNX) port of **Qwen3 8B** on **TPU v6e-8**. **Scaffold only** —
not yet implemented. Lit up once the [`../torchax/`](../torchax/README.md) baseline
is stable and a from-scratch JAX port becomes a ranked hypothesis (the torchax
lane is the reference for what the JAX lane must match-or-beat, mirroring the
llama3 program's torchax→jax progression).

## How to run (smoke test)

```bash
# TODO: native-JAX trainer not yet written. Planned entry:
#   python -m train --steps 20 --batch_size 1 --seqlen 8192
```

## Recent issues / debugging notes

(append as encountered)
