---
title: 'Module: src/torch_tpu/_internal/utils/test_fixtures.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/test_fixtures.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.test_fixtures`/
symbols:
  SingletonMathModule.forward: SingletonMathModule#forward().
  IntWeightInitMixin: IntWeightInitMixin#
  SimpleModule.forward: SimpleModule#forward().
  ContainerModule.initialize_weights_to_ints: ContainerModule#initialize_weights_to_ints().
  SingletonMathModule.initialize_weights_to_ints: SingletonMathModule#initialize_weights_to_ints().
  SimpleModule.initialize_weights_to_ints: SimpleModule#initialize_weights_to_ints().
  IntWeightInitMixin._init_linear: IntWeightInitMixin#_init_linear().
  _T: _T.
  CrashOnForward.forward: CrashOnForward#forward().
  CrashBackwardFunction.backward: CrashBackwardFunction#backward().
  ContainerModule.forward: ContainerModule#forward().
  ModuleListModule.initialize_weights_to_ints: ModuleListModule#initialize_weights_to_ints().
  CrashOnBackward.forward: CrashOnBackward#forward().
  ContainerModule.simple: ContainerModule#simple.
  NestedAddModule.add1: NestedAddModule#add1.
  SimpleModule: SimpleModule#
  SimpleModule.adder: SimpleModule#adder.
  CrashBackwardFunction: CrashBackwardFunction#
  NestedAddModule.forward: NestedAddModule#forward().
  ContainerModule: ContainerModule#
  SingletonMathModule: SingletonMathModule#
  ModuleListModule: ModuleListModule#
  ModuleListModule.forward: ModuleListModule#forward().
  UnusualSequence.push: UnusualSequence#push().
  UnusualSequence.pop: UnusualSequence#pop().
  Identity.forward: Identity#forward().
  CrashBackwardFunction.forward: CrashBackwardFunction#forward().
  AddModule: AddModule#
  SimpleModule.linear1: SimpleModule#linear1.
  SimpleModule.linear2: SimpleModule#linear2.
  ContainerModule.linear3: ContainerModule#linear3.
  SingletonMathModule.layer1: SingletonMathModule#layer1.
  SingletonMathModule.layer2: SingletonMathModule#layer2.
  SingletonMathModule.layer3: SingletonMathModule#layer3.
  ModuleListModule.layers: ModuleListModule#layers.
  UnusualSequence.items: UnusualSequence#items.
  SimpleModule.relu: SimpleModule#relu.
  SingletonMathModule.sigmoid1: SingletonMathModule#sigmoid1.
  SingletonMathModule.sigmoid2: SingletonMathModule#sigmoid2.
  SingletonMathModule.sigmoid3: SingletonMathModule#sigmoid3.
  CrashOnForward.crash: CrashOnForward#crash.
  CrashOnForward.crash_message: CrashOnForward#crash_message.
  CrashBackwardFunction.crash: CrashBackwardFunction#crash.
  CrashBackwardFunction.crash_message: CrashBackwardFunction#crash_message.
  AddModule.forward: AddModule#forward().
  NestedAddModule: NestedAddModule#
  NestedAddModule.__init__: NestedAddModule#__init__().
  IntWeightInitMixin.initialize_weights_to_ints: IntWeightInitMixin#initialize_weights_to_ints().
  SimpleModule.__init__: SimpleModule#__init__().
  ContainerModule.__init__: ContainerModule#__init__().
  NonTensorModule: NonTensorModule#
  NonTensorModule.forward: NonTensorModule#forward().
  SingletonMathModule.__init__: SingletonMathModule#__init__().
  ModuleListModule.__init__: ModuleListModule#__init__().
  UnusualSequence: UnusualSequence#
  UnusualSequence.__init__: UnusualSequence#__init__().
  Identity: Identity#
  CrashOnForward: CrashOnForward#
  CrashOnForward.__init__: CrashOnForward#__init__().
  CrashOnBackward: CrashOnBackward#
---
# Module: [`src/torch_tpu/_internal/utils/test_fixtures.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py)

## Classes
### <a id="AddModule"></a>`AddModule`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:21`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L21)
- doc: A module that adds two tensors.
- signature: `class AddModule(torch.nn.Module):`
- members:
  - <a id="AddModule.forward"></a>`forward(self, x, y)` — [`L24`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L24)
- used by: (2 test-only callers)

### <a id="ContainerModule"></a>`ContainerModule`  ·  implements/extends IntWeightInitMixin
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:90`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L90)
- doc: A nested module for testing.
- signature: `class ContainerModule(torch.nn.Module, IntWeightInitMixin):`
- members:
  - <a id="ContainerModule.forward"></a>`forward(self, x)` — [`L98`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L98)
  - <a id="ContainerModule.initialize_weights_to_ints"></a>`initialize_weights_to_ints(self)` — [`L102`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L102) — See IntWeightInitMixin.
  - <a id="ContainerModule.linear3"></a>`linear3` — [`L96`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L96)
  - <a id="ContainerModule.simple"></a>`simple` — [`L95`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L95)
- protocol/private: <a id="ContainerModule.__init__"></a>`__init__`[`L93`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L93)
- uses (calls/refs, reference-scoped): (4 test-only callers)
- used by: (1 test-only callers)

### <a id="CrashBackwardFunction"></a>`CrashBackwardFunction`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:217`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L217)
- doc: A custom autograd function that crashes on backward pass.
- signature: `class CrashBackwardFunction(torch.autograd.Function):`
- members:
  - <a id="CrashBackwardFunction.backward"></a>`backward(ctx: Any, grad_output: Any)` — [`L245`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L245) — The backward pass intentionally raises an exception.
  - <a id="CrashBackwardFunction.forward"></a>`forward(ctx: Any, x: _T)` — [`L230`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L230) — The forward pass is an identity function.
  - <a id="CrashBackwardFunction.crash"></a>`crash` — [`L225`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L225)
  - <a id="CrashBackwardFunction.crash_message"></a>`crash_message` — [`L226`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L226)
- uses (calls/refs, reference-scoped): (1 test-only callers)
- used by: (1 test-only callers)

### <a id="CrashOnBackward"></a>`CrashOnBackward`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:260`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L260)
- doc: A module that crashes on backward pass.
- signature: `class CrashOnBackward(torch.nn.Module):`
- members:
  - <a id="CrashOnBackward.forward"></a>`forward(self, x: _T)` — [`L263`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L263)
- uses (calls/refs, reference-scoped): (2 test-only callers)

### <a id="CrashOnForward"></a>`CrashOnForward`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:198`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L198)
- doc: A module that crashes on forward.
- signature: `class CrashOnForward(torch.nn.Module):`
- members:
  - <a id="CrashOnForward.forward"></a>`forward(self, x: _T)` — [`L211`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L211)
  - <a id="CrashOnForward.crash"></a>`crash` — [`L208`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L208)
  - <a id="CrashOnForward.crash_message"></a>`crash_message` — [`L209`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L209)
- protocol/private: <a id="CrashOnForward.__init__"></a>`__init__`[`L206`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L206)
- uses (calls/refs, reference-scoped): (1 test-only callers)

### <a id="Identity"></a>`Identity`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:191`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L191)
- doc: An identity module.
- signature: `class Identity(torch.nn.Module):`
- members:
  - <a id="Identity.forward"></a>`forward(self, x: _T)` — [`L194`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L194)
- uses (calls/refs, reference-scoped): (1 test-only callers)

### <a id="IntWeightInitMixin"></a>`IntWeightInitMixin`  ·  implements/extends ABC
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L39)
- doc: Mixin for modules to init Linear weights to integers values.
- signature: `class IntWeightInitMixin(abc.ABC):`
- members:
  - <a id="IntWeightInitMixin._init_linear"></a>`_init_linear(self, linear_module: torch.nn.Linear)` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L56) — Helper to initialize a single Linear layer's weights to integers.
  - <a id="IntWeightInitMixin.initialize_weights_to_ints"></a>`initialize_weights_to_ints(self)` — [`L48`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L48) — Initializes all Linear layer weights and biases to integers.
- uses (calls/refs, reference-scoped): (4 test-only callers)
- used by: (8 test-only callers)

### <a id="ModuleListModule"></a>`ModuleListModule`  ·  implements/extends IntWeightInitMixin
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:140`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L140)
- doc: A module that uses a ModuleList.
- signature: `class ModuleListModule(torch.nn.Module, IntWeightInitMixin):`
- members:
  - <a id="ModuleListModule.forward"></a>`forward(self, x)` — [`L149`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L149)
  - <a id="ModuleListModule.initialize_weights_to_ints"></a>`initialize_weights_to_ints(self)` — [`L154`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L154) — See IntWeightInitMixin.
  - <a id="ModuleListModule.layers"></a>`layers` — [`L145`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L145)
- protocol/private: <a id="ModuleListModule.__init__"></a>`__init__`[`L143`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L143)
- uses (calls/refs, reference-scoped): (2 test-only callers)
- used by: (1 test-only callers)

### <a id="NestedAddModule"></a>`NestedAddModule`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L28)
- doc: A module that adds two tensors.
- signature: `class NestedAddModule(torch.nn.Module):`
- members:
  - <a id="NestedAddModule.forward"></a>`forward(self, x, y)` — [`L35`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L35)
  - <a id="NestedAddModule.add1"></a>`add1` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L33)
- protocol/private: <a id="NestedAddModule.__init__"></a>`__init__`[`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L31)
- uses (calls/refs, reference-scoped): (1 test-only callers)

### <a id="NonTensorModule"></a>`NonTensorModule`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:108`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L108)
- doc: A module that returns a non-tensor value.
- signature: `class NonTensorModule(torch.nn.Module):`
- members:
  - <a id="NonTensorModule.forward"></a>`forward(self, x)` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L111)

### <a id="SimpleModule"></a>`SimpleModule`  ·  implements/extends IntWeightInitMixin
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L67)
- doc: A simple module for testing.
- signature: `class SimpleModule(torch.nn.Module, IntWeightInitMixin):`
- members:
  - <a id="SimpleModule.forward"></a>`forward(self, x)` — [`L77`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L77)
  - <a id="SimpleModule.initialize_weights_to_ints"></a>`initialize_weights_to_ints(self)` — [`L84`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L84) — See IntWeightInitMixin.
  - <a id="SimpleModule.adder"></a>`adder` — [`L75`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L75)
  - <a id="SimpleModule.linear1"></a>`linear1` — [`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L72)
  - <a id="SimpleModule.linear2"></a>`linear2` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L74)
  - <a id="SimpleModule.relu"></a>`relu` — [`L73`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L73)
- protocol/private: <a id="SimpleModule.__init__"></a>`__init__`[`L70`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L70)
- uses (calls/refs, reference-scoped): (3 test-only callers)
- used by: (3 test-only callers)

### <a id="SingletonMathModule"></a>`SingletonMathModule`  ·  implements/extends IntWeightInitMixin
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L115)
- doc: A module with multiple layers processing \[1, 1\] tensors.
- signature: `class SingletonMathModule(torch.nn.Module, IntWeightInitMixin):`
- members:
  - <a id="SingletonMathModule.forward"></a>`forward(self, x)` — [`L127`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L127)
  - <a id="SingletonMathModule.initialize_weights_to_ints"></a>`initialize_weights_to_ints(self)` — [`L133`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L133) — See IntWeightInitMixin.
  - <a id="SingletonMathModule.layer1"></a>`layer1` — [`L120`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L120)
  - <a id="SingletonMathModule.layer2"></a>`layer2` — [`L122`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L122)
  - <a id="SingletonMathModule.layer3"></a>`layer3` — [`L124`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L124)
  - <a id="SingletonMathModule.sigmoid1"></a>`sigmoid1` — [`L121`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L121)
  - <a id="SingletonMathModule.sigmoid2"></a>`sigmoid2` — [`L123`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L123)
  - <a id="SingletonMathModule.sigmoid3"></a>`sigmoid3` — [`L125`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L125)
- protocol/private: <a id="SingletonMathModule.__init__"></a>`__init__`[`L118`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L118)
- uses (calls/refs, reference-scoped): (2 test-only callers)
- used by: (1 test-only callers)

### <a id="UnusualSequence"></a>`UnusualSequence`
- def: [`src/torch_tpu/_internal/utils/test_fixtures.py:162`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L162)
- doc: A container that isn't a subclass of collections.abc.Sequence.
- signature: `class UnusualSequence:`
- members:
  - <a id="UnusualSequence.pop"></a>`pop(self)` — [`L176`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L176) — Pops an item from the sequence.
  - <a id="UnusualSequence.push"></a>`push(self, item: Any)` — [`L168`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L168) — Pushes an item to the sequence.
  - <a id="UnusualSequence.items"></a>`items` — [`L166`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L166)
- protocol/private: <a id="UnusualSequence.__init__"></a>`__init__`[`L165`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L165)

## Module values
- <a id="_T"></a>`_T` — [`L188`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_fixtures.py#L188)

