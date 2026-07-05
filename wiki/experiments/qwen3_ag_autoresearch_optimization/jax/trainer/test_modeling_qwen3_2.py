import sys
import os

# Note: We must insert the model package directory so `import model.modeling_qwen3` works.
# In the container, PYTHONPATH=/app/trainer, and the file is /app/trainer/model/modeling_qwen3.py
# So `model.modeling_qwen3` is importable.
sys.path.insert(0, '/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v016-fused-glu-bwd')

# But the trainer directory ALSO has a `model` dir!
import trainer.model.modeling_qwen3 as mq
print("Has _SPLASH_MESH:", hasattr(mq, "_SPLASH_MESH"))

