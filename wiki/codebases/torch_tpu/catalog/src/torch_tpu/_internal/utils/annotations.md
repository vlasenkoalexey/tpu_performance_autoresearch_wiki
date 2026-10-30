---
title: 'Module: src/torch_tpu/_internal/utils/annotations.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/annotations.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.annotations`/
symbols:
  _resolve_module_attribute: _resolve_module_attribute().
  _annotate_target: _annotate_target().
  _attach_stage_metadata: _attach_stage_metadata().
  _T: _T.
  Stage.warning_category: Stage#warning_category().
  Stage: Stage#
  internal_or_experimental: internal_or_experimental().
  Stage.format_warning_message: Stage#format_warning_message().
  _create_warning_wrapper.wrapper: _create_warning_wrapper().wrapper().
  experimental: experimental().
  stable: stable().
  deprecated: deprecated().
  _create_warning_wrapper: _create_warning_wrapper().
  forbid_in_torch_compile.decorator: forbid_in_torch_compile().decorator().
  ApiStageInfo.stage: ApiStageInfo#stage.
  ApiStageInfo.value: ApiStageInfo#value.
  _safe_setattr: _safe_setattr().
  forbid_in_torch_compile: forbid_in_torch_compile().
  _is_framework_caller_frame: _is_framework_caller_frame().
  Stage.INTERNAL: Stage#INTERNAL.
  Stage.EXPERIMENTAL: Stage#EXPERIMENTAL.
  Stage.DEPRECATED: Stage#DEPRECATED.
  get_torch_version: get_torch_version().
  ApiStageInfo.reason: ApiStageInfo#reason.
  ApiStageInfo.version: ApiStageInfo#version.
  TT_API_STAGE: TT_API_STAGE.
  TT_API_STAGE_REASON: TT_API_STAGE_REASON.
  TT_API_DEPRECATED_VERSION: TT_API_DEPRECATED_VERSION.
  TT_API_PREFER: TT_API_PREFER.
  parse_version: parse_version().
  Stage.STABLE: Stage#STABLE.
  ApiStageInfo: ApiStageInfo#
  _FRAMEWORK_PACKAGES._FRAMEWORK_PACKAGES: _FRAMEWORK_PACKAGES._FRAMEWORK_PACKAGES.
  _internal_apis_allowed_for_testing._internal_apis_allowed_for_testing: _internal_apis_allowed_for_testing._internal_apis_allowed_for_testing.
  TT_API_STAGES_MAP: TT_API_STAGES_MAP.
---
# Module: [`src/torch_tpu/_internal/utils/annotations.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py)

## Classes
### <a id="ApiStageInfo"></a>`ApiStageInfo`
- def: [`src/torch_tpu/_internal/utils/annotations.py:146`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L146)
- doc: Stage metadata for dynamic module/class attributes.
- signature: `class ApiStageInfo:`
- members:
  - <a id="ApiStageInfo.reason"></a>`reason` — [`L159`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L159) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ApiStageInfo.stage"></a>`stage` — [`L158`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L158) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ApiStageInfo.value"></a>`value` — [`L160`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L160) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="ApiStageInfo.version"></a>`version` — [`L161`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L161) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- uses (calls/refs, reference-scoped): [`Stage`](annotations.md#Stage)
- used by: [`_resolve_module_attribute`](annotations.md#_resolve_module_attribute)

### <a id="Stage"></a>`Stage`  ·  implements/extends Enum, str
- def: [`src/torch_tpu/_internal/utils/annotations.py:104`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L104) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- doc: Lifecycle stages for TorchTPU APIs.
- signature: `class Stage(str, enum.Enum):`
- members:
  - <a id="Stage.format_warning_message"></a>`format_warning_message(self, name: str, reason: str, version: Optional[str] = None)` — [`L125`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L125) — Formats the warning message for this stage. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="Stage.warning_category"></a>`warning_category(self)` — [`L113`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L113) — The TorchTPU warning category for this stage. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="Stage.DEPRECATED"></a>`DEPRECATED` — [`L110`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L110) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="Stage.EXPERIMENTAL"></a>`EXPERIMENTAL` — [`L109`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L109) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="Stage.INTERNAL"></a>`INTERNAL` — [`L107`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L107) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
  - <a id="Stage.STABLE"></a>`STABLE` — [`L108`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L108)
- used by: [`_resolve_module_attribute`](annotations.md#_resolve_module_attribute), [`_annotate_target`](annotations.md#_annotate_target), [`internal_or_experimental`](annotations.md#internal_or_experimental), [`experimental`](annotations.md#experimental), [`wrapper`](annotations.md#_create_warning_wrapper.wrapper), [`deprecated`](annotations.md#deprecated), [`stable`](annotations.md#stable), [`_create_warning_wrapper`](annotations.md#_create_warning_wrapper), [`stage`](annotations.md#ApiStageInfo.stage)

## Functions
- <a id="_annotate_target"></a>`_annotate_target(target: _T, stage: Stage, reason: str, version: Optional[str] = None, prefer: Optional[str] = None, strict: bool = False)` — [`L277`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L277) — Attaches stage metadata and warning wrapper to a target function or class. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_attach_stage_metadata"></a>`_attach_stage_metadata(target: Any, stage: str, reason: str, version: Optional[str] = None, prefer: Optional[str] = None)` — [`L178`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L178) — Attaches stage metadata attributes to a target. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_create_warning_wrapper"></a>`_create_warning_wrapper(fn_to_wrap: Callable[..., Any], display_target: Any, stage: Stage, reason: str, version: Optional[str] = None, strict: bool = False)` — [`L213`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L213) — Wraps a callable to emit a one-time warning per process before execution. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_is_framework_caller_frame"></a>`_is_framework_caller_frame(frame: Any)` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L80) — Checks if a stack frame belongs to torch or torch_tpu framework packages. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_resolve_module_attribute"></a>`_resolve_module_attribute(stages_map: Mapping[str, ApiStageInfo], name: str, module_name: str, tt_api_globals: Optional[dict[str, Any] | type])` — [`L529`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L529) — Resolves a dynamic module attribute from a stages map and emits warnings if applicable. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_safe_setattr"></a>`_safe_setattr(target: Any, name: str, value: Any)` — [`L164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L164) — Safely sets an attribute on target, swallowing AttributeError and TypeError. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="forbid_in_torch_compile.decorator"></a>`decorator(target: _T)` — [`L509`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L509) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="deprecated"></a>`deprecated(version: str, reason: str)` — [`L380`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L380) — Marks a TorchTPU Python API (function or class) as deprecated. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="experimental"></a>`experimental(reason: str)` — [`L339`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L339) — Marks a TorchTPU Python API (function or class) as experimental. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="forbid_in_torch_compile"></a>`forbid_in_torch_compile(reason: str)` — [`L471`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L471) — Forbids a TorchTPU API (function or class) inside `torch.compile` regions. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_torch_version"></a>`get_torch_version()` — [`L75`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L75) — Returns PyTorch runtime version parsed into an integer tuple.
- <a id="internal_or_experimental"></a>`internal_or_experimental(*, internal_when: bool, experimental_msg: str, prefer: Optional[str] = None, strict: bool = True)` — [`L406`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L406) — Marks a TorchTPU Python API (function or class) as internal or experimental. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="parse_version"></a>`parse_version(version: str)` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L59) — Parses leading numeric components from a version string into a tuple.
- <a id="stable"></a>`stable(reason: str = "")` — [`L362`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L362) — Marks a TorchTPU Python API (function or class) as stable. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_create_warning_wrapper.wrapper"></a>`wrapper(*args: Any, **kwargs: Any)` — [`L244`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L244) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)

## Module values
- <a id="TT_API_DEPRECATED_VERSION"></a>`TT_API_DEPRECATED_VERSION` — [`L53`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L53)
- <a id="TT_API_PREFER"></a>`TT_API_PREFER` — [`L54`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L54)
- <a id="TT_API_STAGE"></a>`TT_API_STAGE` — [`L51`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L51)
- <a id="TT_API_STAGES_MAP"></a>`TT_API_STAGES_MAP` — [`L55`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L55)
- <a id="TT_API_STAGE_REASON"></a>`TT_API_STAGE_REASON` — [`L52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L52)
- <a id="_FRAMEWORK_PACKAGES._FRAMEWORK_PACKAGES"></a>`_FRAMEWORK_PACKAGES` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L56)
- <a id="_T"></a>`_T` — [`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L49)
- <a id="_internal_apis_allowed_for_testing._internal_apis_allowed_for_testing"></a>`_internal_apis_allowed_for_testing` — [`L101`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/annotations.py#L101)

