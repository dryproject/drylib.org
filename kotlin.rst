:tocdepth: 1

.. index:: pair: Kotlin; language
.. highlight:: kotlin

*****************
DRYlib for Kotlin
*****************

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Getting Started
===============

Prerequisites
-------------

- Kotlin 1.2+

Installation
------------

TODO

Library Usage
-------------

::

   import dry.*

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Kotlin
   ====================================== ======================================
   ``base``                               ``dry`` (package)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                *N/A*
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``dry.math`` (package)
   ``media``                              TODO
   ``meta``                               ``dry.meta`` (package)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``dry.text`` (package)
   ``text/ascii``                         ``dry.text.ascii`` (package)
   ``text/printf``                        ``dry.text.printf`` (package)
   ``text/utf8``                          ``dry.text.utf8`` (package)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Kotlin
   ====================================== ======================================
   ``bool``                               ``dry.Bool`` (type alias for ``kotlin.Boolean``)
   ``char``                               ``dry.Char`` (type alias for ``kotlin.Char``) (FIXME)
   ``complex``                            ``dry.Complex`` (data class)
   ``float``                              ``dry.Float`` (type alias for ``kotlin.Double``)
   ``float32``                            ``dry.Float32`` (type alias for ``kotlin.Float``)
   ``float64``                            ``dry.Float64`` (type alias for ``kotlin.Double``)
   ``int``                                ``dry.Int`` (type alias for ``kotlin.Int``)
   ``int8``                               ``dry.Int8`` (type alias for ``kotlin.Int``)
   ``int16``                              ``dry.Int16`` (type alias for ``kotlin.Int``)
   ``int32``                              ``dry.Int32`` (type alias for ``kotlin.Int``)
   ``int64``                              ``dry.Int64`` (type alias for ``kotlin.Long``)
   ``int128``                             ``dry.Int128`` (type alias for ``kotlin.Long``) (FIXME)
   ``integer``                            ``dry.Integer`` (type alias for ``java.math.BigInteger``)
   ``natural``                            ``dry.Natural`` (type alias for ``dry.Integer``)
   ``rational``                           ``dry.Rational`` (data class)
   ``real``                               ``dry.Real`` (type alias for ``java.math.BigDecimal``)
   ``word``                               ``dry.Word`` (type alias for ``kotlin.Long``)
   ``word8``                              ``dry.Word8`` (type alias for ``kotlin.Long``)
   ``word16``                             ``dry.Word16`` (type alias for ``kotlin.Long``)
   ``word32``                             ``dry.Word32`` (type alias for ``kotlin.Long``)
   ``word64``                             ``dry.Word64`` (type alias for ``kotlin.Long``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Kotlin
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Kotlin
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Kotlin
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

.. seealso::

   `Changelog <https://github.com/dryproject/drylib.kt/blob/master/CHANGES.rst>`__ on GitHub

   `Arto's Notes re: Kotlin <http://ar.to/notes/kotlin>`__
