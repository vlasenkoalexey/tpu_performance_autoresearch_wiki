import jax.numpy as jnp
try:
    print(jnp.broadcast_shapes((64, 8, 2048, 128), (64, 1, 8, 2048, 128)))
except Exception as e:
    print("Error:", e)
