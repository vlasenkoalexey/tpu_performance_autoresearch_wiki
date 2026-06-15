FROM us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260603-v026-tp1-vocab-parallel-bs4-no-outer-ckpt

COPY modeling_qwen3.py /app/trainer/model/modeling_qwen3.py
COPY train.py /app/trainer/train.py
COPY sharding.py /app/trainer/model/sharding.py
