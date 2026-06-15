import jax
import functools

@functools.partial(jax.custom_vjp, nondiff_argnums=(4,))
def my_func(x, weight, cos, sin, eps=1e-6):
    return x * eps

def my_func_fwd(x, weight, cos, sin, eps):
    return my_func(x, weight, cos, sin, eps), (x,)

def my_func_bwd(eps, res, g):
    return (g * eps, None, None, None)

my_func.defvjp(my_func_fwd, my_func_bwd)

print(jax.grad(lambda x: jax.numpy.sum(my_func(x, 1., 1., 1., 2.)))(jax.numpy.ones(2)))
