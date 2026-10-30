---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/components/env_server.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/components/env_server.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.components.env_server`/
symbols:
  VerifiersEnvServer.start: VerifiersEnvServer#start().
  VerifiersEnvServer.close: VerifiersEnvServer#close().
  VerifiersEnvServer.Config.to_dict: VerifiersEnvServer#Config#to_dict().
  VerifiersEnvServer.Config: VerifiersEnvServer#Config#
  VerifiersEnvServer.Config.environment: VerifiersEnvServer#Config#environment.
  VerifiersEnvServer: VerifiersEnvServer#
  _run_env_server_process: _run_env_server_process().
  VerifiersEnvServer.Config.serve: VerifiersEnvServer#Config#serve.
  VerifiersEnvServer.config: VerifiersEnvServer#config.
  VerifiersEnvServer.Config.startup_timeout_sec: VerifiersEnvServer#Config#startup_timeout_sec.
  VerifiersEnvServer.address: VerifiersEnvServer#address.
  VerifiersEnvServer.Config.local_taskset_module: VerifiersEnvServer#Config#local_taskset_module.
  VerifiersEnvServer.process: VerifiersEnvServer#process.
  VerifiersEnvServer.address_queue: VerifiersEnvServer#address_queue.
  VerifiersEnvServer.parent_conn: VerifiersEnvServer#parent_conn.
  VerifiersEnvServer._close_server_process_resources: VerifiersEnvServer#_close_server_process_resources().
  VerifiersEnvServer.Config.__post_init__: VerifiersEnvServer#Config#__post_init__().
  VerifiersEnvServer.__init__: VerifiersEnvServer#__init__().
  _setup_env_server_process: _setup_env_server_process().
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/components/env_server.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py)

## Classes
### <a id="VerifiersEnvServer"></a>`VerifiersEnvServer`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/verifiers/components/env_server.py:68`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L68)
- doc: Spawn and own a Verifiers EnvServer process on the controller host.
- signature: `class VerifiersEnvServer(Configurable):`
- members:
  - <a id="VerifiersEnvServer.close"></a>`close(self)` — [`L164`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L164) — Stop the EnvServer and release its multiprocessing resources.
  - <a id="VerifiersEnvServer.start"></a>`start(self)` — [`L108`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L108) — Start the server and return its resolved ZMQ address.
  - <a id="VerifiersEnvServer.address"></a>`address` — [`L106`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L106)
  - <a id="VerifiersEnvServer.address_queue"></a>`address_queue` — [`L104`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L104)
  - <a id="VerifiersEnvServer.config"></a>`config` — [`L102`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L102)
  - <a id="VerifiersEnvServer.parent_conn"></a>`parent_conn` — [`L105`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L105)
  - <a id="VerifiersEnvServer.process"></a>`process` — [`L103`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L103)
- protocol/private: <a id="VerifiersEnvServer.__init__"></a>`__init__`[`L101`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L101), <a id="VerifiersEnvServer._close_server_process_resources"></a>`_close_server_process_resources`[`L180`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L180)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable)  (6 test-only)
- used by: [`Configurable`](../../../../../config/configurable.md#Configurable)  (2 test-only)

### <a id="VerifiersEnvServer.Config"></a>`VerifiersEnvServer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/components/env_server.py:72`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L72)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="VerifiersEnvServer.Config.to_dict"></a>`to_dict(self)` — [`L93`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L93)
  - <a id="VerifiersEnvServer.Config.environment"></a>`environment` — [`L73`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L73) — ---
  - <a id="VerifiersEnvServer.Config.local_taskset_module"></a>`local_taskset_module` — [`L83`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L83) — ---
  - <a id="VerifiersEnvServer.Config.serve"></a>`serve` — [`L76`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L76) — ---
  - <a id="VerifiersEnvServer.Config.startup_timeout_sec"></a>`startup_timeout_sec` — [`L86`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L86) — ---
- protocol/private: <a id="VerifiersEnvServer.Config.__post_init__"></a>`__post_init__`[`L89`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L89)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable), [`Config`](../../../../../config/configurable.md#Configurable.Config)
- used by: (6 test-only callers)

## Functions
- <a id="_run_env_server_process"></a>`_run_env_server_process(environment: dict[str, Any], serve: VerifiersServeConfig, local_taskset_module: str | None, address_queue: Any, death_pipe: Any)` — [`L38`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L38) — Run a Verifiers EnvServer from config data in a spawned process.
- <a id="_setup_env_server_process"></a>`_setup_env_server_process()` — [`L33`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/env_server.py#L33) — Configure logging in the spawned environment-server process.

