FROM us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v004-splash-attention
COPY model/__init__.py /app/trainer/model/__init__.py
COPY model/modeling_qwen3.py /app/trainer/model/modeling_qwen3.py
COPY train.py /app/trainer/train.py
