:tocdepth: 1

.. index:: pair: C++; language
.. highlight:: c++

**************
DRYlib for C++
**************

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Getting Started
===============

Prerequisites
-------------

- a `C++14 <https://en.wikipedia.org/wiki/C%2B%2B14>`__ compiler
  (Clang or GCC recommended)

Installation
------------

TODO

Library Usage
-------------

::

   #include "drylib.hpp"

   using namespace dry;

Design Principles
=================

- All exported public symbols are namespaced with ``dry::``.

Caveats
-------

- Some core DRYlib type names are reserved words in C++, even when
  namespaced (specifically, ``bool``, ``char``, ``float``, and ``int``).
  For consistency, we nonetheless define type aliases for them, with an
  added underscore suffix to make these legal symbols (e.g., ``dry::bool_``).
  In generated code, the consistent type aliases will be used; in your own
  code, you can naturally use whichever names you prefer (``bool`` or
  ``dry::bool``), as the types in question are identical. And in case you
  prefer ``using namespace dry``, the distinction becomes moot altogether.

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C++
   ====================================== ======================================
   ``base``                               ``<dry.hpp>`` (header file)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``<dry/math.hpp>`` (header file)
   ``media``                              TODO
   ``meta``                               ``<dry/meta.hpp>`` (header file)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``<dry/text.hpp>`` (header file)
   ``text/ascii``                         ``<dry/text/ascii.hpp>`` (header file)
   ``text/printf``                        ``<dry/text/printf.hpp>`` (header file)
   ``text/utf8``                          ``<dry/text/utf8.hpp>`` (header file)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------
.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C++
   ====================================== ======================================
   ``bool``                               ``dry::bool_`` (type alias for ``bool``)
   ``char``                               ``dry::char_`` (type alias for ``std::uint32_t``)
   ``complex``                            ``dry::complex`` (struct)
   ``float``                              ``dry::float_`` (type alias for ``double``)
   ``float32``                            ``dry::float32`` (type alias for ``float``)
   ``float64``                            ``dry::float64`` (type alias for ``double``)
   ``int``                                ``dry::int_`` (type alias for ``long``)
   ``int8``                               ``dry::int8`` (type alias for ``std::int8_t``)
   ``int16``                              ``dry::int16`` (type alias for ``std::int16_t``)
   ``int32``                              ``dry::int32`` (type alias for ``std::int32_t``)
   ``int64``                              ``dry::int64`` (type alias for ``std::int64_t``)
   ``int128``                             ``dry::int128`` (type alias for ``__int128``)
   ``integer``                            ``dry::integer`` (struct)
   ``natural``                            ``dry::natural`` (type alias ``dry::integer``)
   ``rational``                           ``dry::rational`` (struct)
   ``real``                               ``dry::real`` (struct)
   ``word``                               ``dry::word`` (type alias for ``std::uint64_t`` or ``std::uint32_t``)
   ``word8``                              ``dry::word8`` (type alias for ``std::uint8_t``)
   ``word16``                             ``dry::word16`` (type alias for ``std::uint16_t``)
   ``word32``                             ``dry::word32`` (type alias for ``std::uint32_t``)
   ``word64``                             ``dry::word64`` (type alias for ``std::uint64_t``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C++
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C++
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C++
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

.. seealso::

   `Changelog <https://github.com/dryproject/drylib.cpp/blob/master/CHANGES.rst>`__ on GitHub

   `Arto's Notes re: C++ <http://ar.to/notes/cxx>`__
