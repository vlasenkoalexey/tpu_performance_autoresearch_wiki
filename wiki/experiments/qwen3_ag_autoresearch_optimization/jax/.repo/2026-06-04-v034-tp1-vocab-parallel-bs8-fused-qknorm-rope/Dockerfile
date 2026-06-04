FROM us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260603-v027-tp1-vocab-parallel-bs8-no-outer-ckpt

COPY train.py /app/trainer/train.py
COPY model/fused_rope.py /app/trainer/model/fused_rope.py
COPY model/modeling_qwen3.py /app/trainer/model/modeling_qwen3.py
