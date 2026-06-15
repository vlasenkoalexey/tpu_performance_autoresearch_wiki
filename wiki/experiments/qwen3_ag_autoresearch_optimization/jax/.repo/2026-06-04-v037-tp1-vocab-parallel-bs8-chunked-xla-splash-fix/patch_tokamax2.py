import re

path_cache = 'tokamax/_src/autotuning/cache.py'
with open(path_cache, 'r') as f:
    text_cache = f.read()

# Make _load_cache return {}
text_cache = re.sub(r'def _load_cache\(.*?\):.*?return out', r'def _load_cache(self, device_kind, cache_path=None):\n    return {}', text_cache, flags=re.DOTALL)

with open(path_cache, 'w') as f:
    f.write(text_cache)

path_api = 'tokamax/_src/autotuning/api.py'
with open(path_api, 'r') as f:
    text_api = f.read()

# Replace the whole api.py file to disable autotuning completely and just use the wrapped function directly.
new_api = """
import functools
import jax

def autotune(*args, **kwargs):
  def wrapper(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        # By removing the autotuning wrapper entirely, we avoid the compilation loop
        return f(*args, **kwargs)
    return inner
  return wrapper

"""
with open(path_api, 'w') as f:
    f.write(new_api)

path_op = 'tokamax/_src/ops/op.py'
with open(path_op, 'r') as f:
    text_op = f.read()

# Need to disable Op autotuning
# Look for Op._register_custom_vjp and bypass autotuning.
new_op = text_op.replace('self.autotuning_config = autotuner.get_config(', '# self.autotuning_config = autotuner.get_config(')

with open(path_op, 'w') as f:
    f.write(new_op)

print('Patched api.py and op.py')
