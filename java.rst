.. index:: pair: Java; language
.. highlight:: java

***************
DRYlib for Java
***************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- Java SE 8+

- Gradle 4.6+

Installation
------------

TODO

Library Usage
-------------

::

   import dry.*;

Design Principles
=================

- No dependencies on anything else, for anything.

The Interfaces
--------------

- **Immutability:**
  All objects are immutable (``final``) after construction.

- **Null safety:**
  No methods ever accept ``null`` arguments, nor do they return ``null``.
  Constructors check their arguments and throw a ``NullPointerException`` if
  passed a ``null`` value; as a consequence, no fields can be ``null``.

- **Thread safety:**
  Due to immutability, it is safe to cache and reuse object instances and to
  freely share them between threads.

The Implementation
------------------

- All local variables are declared immutable (``final``) by default, except
  for variables that actually are mutated in the method body (no qualifier).

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Java
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
   DRY                                    Java
   ====================================== ======================================
   ``bool``                               ``dry.Bool`` (class)
   ``char``                               ``dry.Char`` (class)
   ``complex``                            ``dry.Complex`` (interface)
   ``float``                              ``dry.Float`` (interface)
   ``float32``                            ``dry.Float32`` (class)
   ``float64``                            ``dry.Float64`` (class)
   ``int``                                ``dry.Int`` (class)
   ``int8``                               ``dry.Int8`` (class)
   ``int16``                              ``dry.Int16`` (class)
   ``int32``                              ``dry.Int32`` (class)
   ``int64``                              ``dry.Int64`` (class)
   ``int128``                             ``dry.Int128`` (class)
   ``integer``                            ``dry.Integer`` (interface)
   ``natural``                            ``dry.Natural`` (class)
   ``number``                             ``dry.Number`` (interface)
   ``rational``                           ``dry.Rational`` (interface)
   ``real``                               ``dry.Real`` (interface)
   ``symbol``                             ``dry.Symbol`` (interface)
   ``word``                               ``dry.Word`` (interface)
   ``word8``                              ``dry.Word8`` (class)
   ``word16``                             ``dry.Word16`` (class)
   ``word32``                             ``dry.Word32`` (class)
   ``word64``                             ``dry.Word64`` (class)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Java
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Java
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Java
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: Java <http://ar.to/notes/java>`__
