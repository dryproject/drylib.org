.. index:: languages
.. highlight:: none

******************
Language Reference
******************

At the time of writing (summer 2018), the :doc:`C++ <cpp>`, :doc:`Go <go>`,
:doc:`Java <java>`, and :doc:`OCaml <ocaml>` ports are being actively
developed and fleshed out.

Current Ports
=============

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Language
     - Usage

   * - :doc:`C++ <cpp>`
     - ``#include "drylib.hpp"``

   * - :doc:`Go <go>`
     - ``import "github.com/dryproject/drylib.go"``

   * - :doc:`Java <java>`
     - ``import dry.*;``

   * - :doc:`OCaml <ocaml>`
     - ``open DRY``

Planned Ports
=============

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Language
     - Usage

   * - :doc:`C <c>`
     - ``#include "drylib.h"``

   * - :doc:`Common Lisp <lisp>`
     - ``(require :drylib)``

   * - :doc:`D <d>`
     - ``import dry = drylib;``

   * - :doc:`Dart <dart>`
     - TODO

   * - :doc:`Elixir <elixir>`
     - TODO

   * - :doc:`JS <js>`
     - ``import * as dry from 'drylib';``

   * - :doc:`Julia <julia>`
     - ``using DRYlib``

   * - :doc:`Kotlin <kotlin>`
     - ``import dry.*``

   * - :doc:`Lua <lua>`
     - ``dry = require 'drylib'``

   * - :doc:`PHP <php>`
     - ``require_once 'drylib.php';``

   * - :doc:`Python <python>`
     - ``import drylib``

   * - :doc:`Ruby <ruby>`
     - ``require 'drylib'``

   * - :doc:`Rust <rust>`
     - ``extern crate drylib as dry;``

Language Features
=================

.. list-table::
   :widths: 12 12 12 12 12 10 10 10 10
   :header-rows: 1

   * - Language
     - `Type Checking <https://en.wikipedia.org/wiki/Type_system#Type_checking>`__
     - `Type Safety <https://en.wikipedia.org/wiki/Type_safety>`__
     - `Memory Mgmt <https://en.wikipedia.org/wiki/Memory_management>`__
     - `Strings <https://en.wikipedia.org/wiki/Unicode>`__
     - `Bignums? <https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic>`__
     - `Exceptions? <https://en.wikipedia.org/wiki/Exception_handling>`__
     - `Closures? <https://en.wikipedia.org/wiki/Closure_(computer_programming)>`__
     - `Macros? <https://en.wikipedia.org/wiki/Macro_(computer_science)>`__

   * - :doc:`C <c>`
     - Static
     - Weak
     - Manual
     - ✗ bytes
     - ✗
     - ✗
     - ✗
     - ✗

   * - :doc:`C++ <cpp>`
     - Static
     - Weak
     - RAII/RC
     - ✗ bytes
     - ✗
     - ✓
     - ✓
     - ✗

   * - :doc:`Common Lisp <lisp>`
     - Dynamic
     - Strong
     - GC
     - ✗ UTF-{16,32} [#lisp-utf]_
     - ✓
     - ✓
     - ✓
     - ✓

   * - :doc:`D <d>`
     - Static
     - Weak?
     - GC/Manual
     - ✓ UTF-{8,16,32}
     - ✓
     - ✓
     - ✓
     - ✗

   * - :doc:`Dart <dart>`
     - Static
     - Strong
     - GC
     - ✗ UTF-16 [#dart-utf]_
     - ✗
     - ✓
     - ✓
     - ✗

   * - :doc:`Elixir <elixir>`
     - Dynamic
     - Strong
     - GC
     - ✓ UTF-8
     - ✓
     - ✓
     - ✓
     - ✓

   * - :doc:`Go <go>`
     - Static
     - Strong
     - GC
     - ✓ UTF-8
     - ✓
     - ✗ [#go-exn]_
     - ✓
     - ✗

   * - :doc:`Java <java>`
     - Static
     - Strong
     - GC
     - ✗ UTF-16
     - ✓
     - ✓
     - ✓ [#java-fns]_
     - ✗

   * - :doc:`JS <js>`
     - Dynamic
     - Weak
     - GC
     - ✗ UTF-16
     - ✗ [#js-bns]_
     - ✓
     - ✓
     - ✗

   * - :doc:`Julia <julia>`
     - Dynamic
     - Strong
     - GC
     - ✓ UTF-8
     - ✓
     - ✓
     - ✓
     - ✓

   * - :doc:`Kotlin <kotlin>`
     - Static
     - Strong
     - GC
     - ✗ UTF-16
     - ✓
     - ✓
     - ✓
     - ✗

   * - :doc:`Lua <lua>`
     - Dynamic
     - Strong
     - GC
     - ✗ bytes
     - ✗
     - ✗ [#lua-exn]_
     - ✓
     - ✗

   * - :doc:`OCaml <ocaml>`
     - Static
     - Strong
     - GC
     - ✗ bytes
     - ✗ [#ocaml-bns]_
     - ✓
     - ✓
     - ✗

   * - :doc:`PHP <php>`
     - Dynamic
     - Weak
     - GC
     - ✗ bytes
     - ✓
     - ✓
     - ✓
     - ✗

   * - :doc:`Python <python>`
     - Dynamic
     - Strong
     - GC
     - ✗ UTF-{16,32}?
     - ✓
     - ✓
     - ✓
     - ✗

   * - :doc:`Ruby <ruby>`
     - Dynamic
     - Strong
     - GC
     - ✓ UTF-8
     - ✓
     - ✓
     - ✓
     - ✗

   * - :doc:`Rust <rust>`
     - Static
     - Strong
     - RAII/RC
     - ✓ UTF-8
     - ✗ [#rust-bns]_
     - ✗
     - ✓
     - ✓

.. rubric:: Footnotes

.. [#dart-utf]  https://github.com/dart-lang/sdk/issues/28404
.. [#go-exn]    https://github.com/golang/go/wiki/PanicAndRecover
.. [#java-fns]  https://dzone.com/articles/java-8-lambas-limitations-closures
.. [#js-bns]    https://github.com/tc39/proposal-bigint
.. [#lisp-utf]  https://www.cliki.net/Unicode%20support
.. [#lua-exn]   http://lua-users.org/wiki/ErrorHandling
.. [#ocaml-bns] https://github.com/ocaml/num
.. [#rust-bns]  https://github.com/rust-num/num-bigint

.. toctree::
   :hidden:

   c
   cpp
   lisp
   d
   dart
   elixir
   go
   java
   js
   julia
   kotlin
   lua
   ocaml
   php
   python
   ruby
   rust
