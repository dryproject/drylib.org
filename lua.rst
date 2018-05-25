.. index:: pair: Lua; language
.. highlight:: lua

**************
DRYlib for Lua
**************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- `Lua <https://en.wikipedia.org/wiki/Lua_(programming_language)>`__
  5.3+

Installation
------------

http://luarocks.org/modules/dryproject/drylib

To install the library locally, execute:

.. code-block:: bash

   $ luarocks install drylib

To uninstall the library, execute:

.. code-block:: bash

   $ luarocks remove drylib

Library Usage
-------------

To load the library, do::

   dry = require 'drylib'

Reference
=========

Modules
-------

======================================= ========================================
DRY                                     Lua
======================================= ========================================
TODO                                    TODO
======================================= ========================================

Module ``base``
---------------

======================================= ========================================
DRY                                     Lua
======================================= ========================================
``bool``                                ``dry.bool(x)`` (function)
``char``                                ``dry.char(c)`` (function)
``complex``                             ``dry.complex(r,i)`` (function), ``dry.Complex`` (metatable)
``float``                               ``dry.float(r)`` (function)
``float32``                             ``dry.float32(r)`` (function)
``float64``                             ``dry.float64(r)`` (function)
``int``                                 ``dry.int(z)`` (function)
``int8``                                ``dry.int8(z)`` (function)
``int16``                               ``dry.int16(z)`` (function)
``int32``                               ``dry.int32(z)`` (function)
``int64``                               ``dry.int64(z)`` (function)
``int128``                              ``dry.int128(x)`` (function)
``integer``                             ``dry.integer(z)`` (function), ``dry.Integer`` (metatable)
``natural``                             ``dry.natural(n)`` (function)
``rational``                            ``dry.rational(n,d)`` (function), ``dry.Rational`` (metatable)
``real``                                ``dry.real(r)`` (function), ``dry.Real`` (metatable)
``word``                                ``dry.word(n)`` (function)
``word8``                               ``dry.word8(n)`` (function)
``word16``                              ``dry.word16(n)`` (function)
``word32``                              ``dry.word32(n)`` (function)
``word64``                              ``dry.word64(n)`` (function)
======================================= ========================================

Module ``math``
---------------

======================================= ========================================
DRY                                     Lua
======================================= ========================================
TODO                                    TODO
======================================= ========================================

Module ``text``
---------------

======================================= ========================================
DRY                                     Lua
======================================= ========================================
TODO                                    TODO
======================================= ========================================

See Also
========

- `Arto's Notes re: Lua <http://ar.to/notes/lua>`__
