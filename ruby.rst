:tocdepth: 1

.. index:: pair: Ruby; language
.. highlight:: ruby

***************
DRYlib for Ruby
***************

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Getting Started
===============

Prerequisites
-------------

- `Ruby <https://en.wikipedia.org/wiki/Ruby_(programming_language)>`__ 2.5+

Installation
------------

https://rubygems.org/gems/drylib

To install the library locally, execute:

.. code-block:: bash

   $ gem install drylib

To uninstall the library, execute:

.. code-block:: bash

   $ gem uninstall drylib

Library Usage
-------------

To load the library, do::

   require 'drylib'

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Ruby
   ====================================== ======================================
   ``base``                               ``DRY`` (module)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``DRY::Math`` (module)
   ``media``                              TODO
   ``meta``                               ``DRY::Meta`` (module)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``DRY::Text`` (module)
   ``text/ascii``                         ``DRY::Text::ASCII`` (module)
   ``text/printf``                        ``DRY::Text::Printf`` (module)
   ``text/utf8``                          ``DRY::Text::UTF8`` (module)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Ruby
   ====================================== ======================================
   ``bool``                               ``DRY.Bool(x)`` (function)
   ``char``                               ``DRY.Char(c)`` (function), ``DRY::Char`` (class)
   ``complex``                            ``DRY.Complex(r,i)`` (function), ``DRY::Complex`` (class)
   ``float``                              ``DRY.Float(r)`` (function)
   ``float32``                            ``DRY.Float32(r)`` (function)
   ``float64``                            ``DRY.Float64(r)`` (function)
   ``int``                                ``DRY.Int(z)`` (function)
   ``int8``                               ``DRY.Int8(z)`` (function)
   ``int16``                              ``DRY.Int16(z)`` (function)
   ``int32``                              ``DRY.Int32(z)`` (function)
   ``int64``                              ``DRY.Int64(z)`` (function)
   ``int128``                             ``DRY.Int128(z)`` (function)
   ``integer``                            ``DRY.Integer(z)`` (function)
   ``natural``                            ``DRY.Natural(n)`` (function)
   ``rational``                           ``DRY.Rational(n,d)`` (function), ``DRY::Rational`` (class)
   ``real``                               ``DRY.Real(r)`` (function), ``DRY::Real`` (class)
   ``word``                               ``DRY.Word(n)`` (function)
   ``word8``                              ``DRY.Word8(n)`` (function)
   ``word16``                             ``DRY.Word16(n)`` (function)
   ``word32``                             ``DRY.Word32(n)`` (function)
   ``word64``                             ``DRY.Word64(n)`` (function)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Ruby
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Ruby
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Ruby
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: Ruby <http://ar.to/notes/ruby>`__
