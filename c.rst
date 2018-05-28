:tocdepth: 1

.. index:: pair: C; language
.. highlight:: c

************
DRYlib for C
************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- a `C11 <https://en.wikipedia.org/wiki/C11_(C_standard_revision)>`__ compiler
  (Clang or GCC recommended)

Installation
------------

TODO

Library Usage
-------------

::

   #include "drylib.h"

Design Principles
=================

- All exported public symbols are prefixed with ``dry_``.

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C
   ====================================== ======================================
   ``base``                               ``<dry.h>`` (header file)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``<dry/math.h>`` (header file)
   ``media``                              TODO
   ``meta``                               ``<dry/meta.h>`` (header file)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``<dry/text.h>`` (header file)
   ``text/ascii``                         ``<dry/text/ascii.h>`` (header file)
   ``text/printf``                        ``<dry/text/printf.h>`` (header file)
   ``text/utf8``                          ``<dry/text/utf8.h>`` (header file)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C
   ====================================== ======================================
   ``bool``                               ``dry_bool_t`` (type alias for ``_Bool``)
   ``char``                               ``dry_char_t`` (type alias for ``uint32_t``)
   ``complex``                            ``dry_complex_t`` (struct)
   ``float``                              ``dry_float_t`` (type alias for ``double``)
   ``float32``                            ``dry_float32_t`` (type alias for ``float``)
   ``float64``                            ``dry_float64_t`` (type alias for ``double``)
   ``int``                                ``dry_int_t`` (type alias for ``long``)
   ``int8``                               ``dry_int8_t`` (type alias for ``int8_t``)
   ``int16``                              ``dry_int16_t`` (type alias for ``int16_t``)
   ``int32``                              ``dry_int32_t`` (type alias for ``int32_t``)
   ``int64``                              ``dry_int64_t`` (type alias for ``int64_t``)
   ``int128``                             ``dry_int128_t`` (type alias for ``__int128``)
   ``integer``                            ``dry_integer_t`` (struct)
   ``natural``                            ``dry_natural_t`` (type alias ``dry_integer_t``)
   ``rational``                           ``dry_rational_t`` (struct)
   ``real``                               ``dry_real_t`` (struct)
   ``word``                               ``dry_word_t`` (type alias for ``uint64_t`` or ``uint32_t``)
   ``word8``                              ``dry_word8_t`` (type alias for ``uint8_t``)
   ``word16``                             ``dry_word16_t`` (type alias for ``uint16_t``)
   ``word32``                             ``dry_word32_t`` (type alias for ``uint32_t``)
   ``word64``                             ``dry_word64_t`` (type alias for ``uint64_t``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    C
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: C <http://ar.to/notes/c>`__
