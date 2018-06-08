.. index:: languages
.. highlight:: none

******************
Language Reference
******************

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

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Language
     - Usage

   * - :doc:`C <c>`
     - ``#include "drylib.h"``

   * - :doc:`C++ <cpp>`
     - ``#include "drylib.hpp"``

   * - :doc:`Common Lisp <lisp>`
     - ``(require :drylib)``

   * - :doc:`D <d>`
     - ``import dry = drylib;``

   * - :doc:`Dart <dart>`
     - TODO

   * - :doc:`Elixir <elixir>`
     - TODO

   * - :doc:`Go <go>`
     - ``import "github.com/dryproject/drylib.go"``

   * - :doc:`Java <java>`
     - ``import dry.*;``

   * - :doc:`JS <js>`
     - ``import * as dry from 'drylib';``

   * - :doc:`Julia <julia>`
     - ``using DRYlib``

   * - :doc:`Kotlin <kotlin>`
     - ``import dry.*``

   * - :doc:`Lua <lua>`
     - ``dry = require 'drylib'``

   * - :doc:`OCaml <ocaml>`
     - ``open DRY``

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
   :widths: 16 12 12 12 12 12 12 12
   :header-rows: 1

   * - Language
     - `Type Checking <https://en.wikipedia.org/wiki/Type_system#Type_checking>`__
     - `Type Safety <https://en.wikipedia.org/wiki/Type_safety>`__
     - `Memory Mgmt <https://en.wikipedia.org/wiki/Memory_management>`__
     - `Exceptions? <https://en.wikipedia.org/wiki/Exception_handling>`__
     - `Closures? <https://en.wikipedia.org/wiki/Closure_(computer_programming)>`__
     - `Bignums? <https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic>`__
     - `Macros? <https://en.wikipedia.org/wiki/Macro_(computer_science)>`__

   * - :doc:`C <c>`
     - Static
     - Weak
     - Manual
     - No
     - No
     - No
     - No

   * - :doc:`C++ <cpp>`
     - Static
     - Weak
     - RAII/RC
     - Yes
     - Yes
     - No
     - No

   * - :doc:`Common Lisp <lisp>`
     - Dynamic
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - Yes

   * - :doc:`D <d>`
     - Static
     - Weak?
     - GC/Manual
     - Yes
     - Yes
     - Yes
     - No

   * - :doc:`Dart <dart>`
     - Static
     - Strong
     - GC
     - Yes
     - Yes
     - No
     - No

   * - :doc:`Elixir <elixir>`
     - Dynamic
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - Yes

   * - :doc:`Go <go>`
     - Static
     - Strong
     - GC
     - No [#go-exn]_
     - Yes
     - Yes
     - No

   * - :doc:`Java <java>`
     - Static
     - Strong
     - GC
     - Yes
     - Yes [#java-fns]_
     - Yes
     - No

   * - :doc:`JS <js>`
     - Dynamic
     - Weak
     - GC
     - Yes
     - Yes
     - No [#js-bns]_
     - No

   * - :doc:`Julia <julia>`
     - Dynamic
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - Yes

   * - :doc:`Kotlin <kotlin>`
     - Static
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - No

   * - :doc:`Lua <lua>`
     - Dynamic
     - Strong
     - GC
     - No [#lua-exn]_
     - Yes
     - No
     - No

   * - :doc:`OCaml <ocaml>`
     - Static
     - Strong
     - GC
     - Yes
     - Yes
     - No [#ocaml-bns]_
     - No

   * - :doc:`PHP <php>`
     - Dynamic
     - Weak
     - GC
     - Yes
     - Yes
     - Yes
     - No

   * - :doc:`Python <python>`
     - Dynamic
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - No

   * - :doc:`Ruby <ruby>`
     - Dynamic
     - Strong
     - GC
     - Yes
     - Yes
     - Yes
     - No

   * - :doc:`Rust <rust>`
     - Static
     - Strong
     - RAII/RC
     - No
     - Yes
     - No [#rust-bns]_
     - Yes

.. rubric:: Footnotes

.. [#go-exn]    https://github.com/golang/go/wiki/PanicAndRecover
.. [#java-fns]  https://dzone.com/articles/java-8-lambas-limitations-closures
.. [#js-bns]    https://github.com/tc39/proposal-bigint
.. [#lua-exn]   http://lua-users.org/wiki/ErrorHandling
.. [#ocaml-bns] https://github.com/ocaml/num
.. [#rust-bns]  https://github.com/rust-num/num-bigint
