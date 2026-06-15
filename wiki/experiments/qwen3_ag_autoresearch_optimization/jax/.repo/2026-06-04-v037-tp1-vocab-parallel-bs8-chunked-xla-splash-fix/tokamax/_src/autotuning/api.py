
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

