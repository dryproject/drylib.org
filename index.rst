#############
DRYlib Manual
#############

.. raw:: latex

   \part{Manual}

.. warning::

   **Here be dragons.**
   This is a semi-public, :doc:`pre-alpha, work-in-progress <status>` project.

   **Caveat utilitor:**
   Assume nothing works, and you may be pleasantly surprised;
   and when it breaks, you get to keep both pieces.

Modules
=======

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Module
     - Description

   * - :doc:`base <base/index>`
     - Base library & types.

   * - :doc:`bits <bits/index>`
     - Bitwise operations.

   * - :doc:`code <code/index>`:
       :doc:`code/wasm <code/wasm/index>`,
       :doc:`... <code/index>`
     - Code generation.

   * - :doc:`crypto <crypto/index>`:
       :doc:`crypto/hash <crypto/hash/index>`
     - Cryptographic algorithms.

   * - :doc:`data <data/index>`
     - Generic data structures.

   * - :doc:`ffi <ffi/index>`:
       :doc:`ffi/c <ffi/c/index>`,
       :doc:`... <ffi/index>`
     - Foreign-function interfaces (FFI).

   * - :doc:`geo <geo/index>`
     - Geographic information support.

   * - :doc:`io <io/index>`
     - Input/output (I/O) support.

   * - :doc:`lang <lang/index>`:
       :doc:`lang/en <lang/en/index>`
     - Natural language support.

   * - :doc:`logic <logic/index>`
     - Logical operations.

   * - :doc:`math <math/index>`:
       :doc:`math/blas <math/blas/index>`
     - Mathematical operations.

   * - :doc:`media <media/index>`:
       :doc:`media/audio <media/audio/index>`,
       :doc:`media/image <media/image/index>`,
       :doc:`media/video <media/video/index>`
     - Audiovisual media support.

   * - :doc:`meta <meta/index>`
     - Metadata support.

   * - :doc:`net <net/index>`:
       :doc:`net/ipv4 <net/ipv4/index>`,
       :doc:`net/ipv6 <net/ipv6/index>`,
       :doc:`net/tcp <net/tcp/index>`,
       :doc:`net/udp <net/udp/index>`
     - Networking data structures.

   * - :doc:`qty <qty/index>`
     - Units & quantities.

   * - :doc:`std <std/index>`:
       :doc:`std/ansi <std/ansi/index>`,
       :doc:`std/iana <std/iana/index>`,
       :doc:`std/ietf <std/ietf/index>`,
       :doc:`std/iso <std/iso/index>`,
       :doc:`std/itu <std/itu/index>`,
       :doc:`std/si <std/si/index>`,
       :doc:`std/w3c <std/w3c/index>`,
       :doc:`... <std/index>`
     - Standards.

   * - :doc:`sys <sys/index>`:
       :doc:`sys/linux <sys/linux/index>`,
       :doc:`sys/posix <sys/posix/index>`
     - System interfaces (POSIX, Linux, etc).

   * - :doc:`text <text/index>`:
       :doc:`text/ascii <text/ascii/index>`,
       :doc:`text/printf <text/printf/index>`,
       :doc:`text/utf8 <text/utf8/index>`
     - Text processing.

   * - :doc:`time <time/index>`
     - Date & time calculations.

   * - :doc:`util <util/index>`
     - Miscellaneous utilities.

Languages
=========

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

.. toctree::
   :hidden:

   intro
   tutorial
   faq
   reference
   status
   history
   glossary
   bibliography
