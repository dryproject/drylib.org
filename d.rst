:tocdepth: 1

.. index:: pair: D; language
.. highlight:: d

************
DRYlib for D
************

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Getting Started
===============

Prerequisites
-------------

- `DMD <https://en.wikipedia.org/wiki/D_(programming_language)>`__ 2.080+

Installation
------------

TODO

Library Usage
-------------

::

   import dry = drylib;

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    D
   ====================================== ======================================
   ``base``                               ``drylib`` (package)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               TODO
   ``media``                              TODO
   ``meta``                               TODO
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               TODO
   ``text/ascii``                         TODO
   ``text/printf``                        TODO
   ``text/utf8``                          TODO
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    D
   ====================================== ======================================
   ``bool``                               ``dry.Bool`` (type alias for ``bool``)
   ``char``                               ``dry.Char`` (type alias for ``dchar``)
   ``complex``                            ``dry.Complex`` (type alias for ``creal``)
   ``float``                              ``dry.Float`` (type alias for ``real``)
   ``float32``                            ``dry.Float32`` (type alias for ``float``)
   ``float64``                            ``dry.Float64`` (type alias for ``double``)
   ``int``                                ``dry.Int`` (type alias for ``long`` or ``int``)
   ``int8``                               ``dry.Int8`` (type alias for ``byte``)
   ``int16``                              ``dry.Int16`` (type alias for ``short``)
   ``int32``                              ``dry.Int32`` (type alias for ``int``)
   ``int64``                              ``dry.Int64`` (type alias for ``long``)
   ``int128``                             ``dry.Int128`` (type alias for ``cent``)
   ``integer``                            ``dry.Integer`` (type alias for ``std.bigint.BigInt``)
   ``natural``                            ``dry.Natural`` (type alias for ``dry.Integer``)
   ``rational``                           ``dry.Rational`` (struct)
   ``real``                               ``dry.Real`` (struct)
   ``word``                               ``dry.Word`` (type alias for ``ulong`` or ``uint``)
   ``word8``                              ``dry.Word8`` (type alias for ``ubyte``)
   ``word16``                             ``dry.Word16`` (type alias for ``ushort``)
   ``word32``                             ``dry.Word32`` (type alias for ``uint``)
   ``word64``                             ``dry.Word64`` (type alias for ``ulong``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    D
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    D
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    D
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: D <http://ar.to/notes/d>`__
