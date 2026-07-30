"""Environment capture — every measurement JSON records the substrate it ran on."""
from __future__ import annotations

import os
import platform
import socket
import sys
import time

ENV_KEYS_EXACT = (
    "LIBTPU_INIT_ARGS",
    "XLA_FLAGS",
    "TPU_LIBRARY_PATH",
    "JAX_PLATFORMS",
)
ENV_PREFIXES = ("TPU_", "JAX_", "LIBTPU_", "XLA_")


def _pkg_version(name: str):
    try:
        import importlib.metadata as md
        return md.version(name)
    except Exception:
        return None


def capture(include_devices: bool = True) -> dict:
    env = {}
    for k, v in os.environ.items():
        if k in ENV_KEYS_EXACT or any(k.startswith(p) for p in ENV_PREFIXES):
            env[k] = v
    for k in ENV_KEYS_EXACT:
        env.setdefault(k, None)

    info = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "argv": sys.argv,
        "env": env,
        "versions": {
            "jax": _pkg_version("jax"),
            "jaxlib": _pkg_version("jaxlib"),
            "libtpu": _pkg_version("libtpu") or _pkg_version("libtpu-nightly"),
            "numpy": _pkg_version("numpy"),
        },
    }
    if include_devices:
        try:
            import jax
            devs = jax.devices()
            info["devices"] = {
                "count": len(devs),
                "kind": devs[0].device_kind if devs else None,
                "platform": devs[0].platform if devs else None,
            }
        except Exception as e:
            info["devices"] = {"error": repr(e)}
    return info
