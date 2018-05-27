#############
DRYlib Manual
#############

*This is a semi-public, pre-alpha, work-in-progress project.*

**Here be dragons.**

**Caveat utilitor:** assume nothing works, and you may be pleasantly
surprised; and when it breaks, you get to keep both pieces.

***************
Getting Started
***************

.. toctree::
   :maxdepth: 2

   intro
   faq
   tutorial

*********
Reference
*********

.. _module-reference:

Module Reference
================

.. table::
   :widths: 50 50

   ====================================== ======================================
   Module                                 Description
   ====================================== ======================================
   :doc:`base <base/index>`               Base library & types.
   :doc:`bits <bits/index>`               Bitwise operations.
   :doc:`code <code/index>`               Code generation.
   :doc:`crypto <crypto/index>`           Cryptographic algorithms.
   :doc:`data <data/index>`               Generic data structures.
   :doc:`ffi <ffi/index>`                 Foreign-function interfaces (FFI).
   :doc:`geo <geo/index>`                 Geographic information support.
   :doc:`io <io/index>`                   Input/output (I/O) support.
   :doc:`lang <lang/index>`               Natural language support.
   :doc:`logic <logic/index>`             Logical operations.
   :doc:`math <math/index>`               Mathematical operations.
   :doc:`media <media/index>`             Audiovisual media support.
   :doc:`meta <meta/index>`               Metadata support.
   :doc:`net <net/index>`                 Networking data structures.
   :doc:`qty <qty/index>`                 Units & quantities.
   :doc:`std <std/index>`                 Standards.
   :doc:`sys <sys/index>`                 System interfaces (POSIX, Linux, etc).
   :doc:`text <text/index>`               Text processing.
   :doc:`time <time/index>`               Date & time calculations.
   :doc:`util <util/index>`               Miscellaneous utilities.
   ====================================== ======================================

.. _language-reference:

Language Reference
==================

.. table::
   :widths: 50 50

   ====================================== ======================================
   Language                               Usage
   ====================================== ======================================
   :doc:`C <c>`                           ``#include "drylib.h"``
   :doc:`C++ <cpp>`                       ``#include "drylib.hpp"``
   :doc:`Common Lisp <lisp>`              ``(require :drylib)``
   :doc:`D <d>`                           ``import dry = drylib;``
   :doc:`Dart <dart>`                     TODO
   :doc:`Elixir <elixir>`                 TODO
   :doc:`Go <go>`                         ``import "github.com/dryproject/drylib.go"``
   :doc:`Java <java>`                     ``import dry.*;``
   :doc:`JS <js>`                         ``import * as dry from 'drylib';``
   :doc:`Julia <julia>`                   ``using DRYlib``
   :doc:`Kotlin <kotlin>`                 ``import dry.*``
   :doc:`Lua <lua>`                       ``dry = require 'drylib'``
   :doc:`OCaml <ocaml>`                   ``open DRY``
   :doc:`PHP <php>`                       ``require_once 'drylib.php';``
   :doc:`Python <python>`                 ``import drylib``
   :doc:`Ruby <ruby>`                     ``require 'drylib'``
   :doc:`Rust <rust>`                     ``extern crate drylib as dry;``
   ====================================== ======================================
