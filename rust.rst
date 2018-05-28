:tocdepth: 1

.. index:: pair: Rust; language
.. highlight:: rust

***************
DRYlib for Rust
***************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- `Rust <https://en.wikipedia.org/wiki/Rust_(programming_language)>`__ 1.26+

Installation
------------

TODO

Library Usage
-------------

::

   extern crate drylib as dry;

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Rust
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
   DRY                                    Rust
   ====================================== ======================================
   ``bool``                               ``dry::Bool`` (type alias for ``bool``)
   ``char``                               ``dry::Char`` (type alias for ``char``)
   ``complex``                            ``dry::Complex`` (struct)
   ``float``                              ``dry::Float`` (type alias for ``dry::Float64``)
   ``float32``                            ``dry::Float32`` (type alias for ``f32``)
   ``float64``                            ``dry::Float64`` (type alias for ``f64``)
   ``int``                                ``dry::Int`` (type alias for ``isize``)
   ``int8``                               ``dry::Int8`` (type alias for ``i8``)
   ``int16``                              ``dry::Int16`` (type alias for ``i16``)
   ``int32``                              ``dry::Int32`` (type alias for ``i32``)
   ``int64``                              ``dry::Int64`` (type alias for ``i64``)
   ``int128``                             ``dry::Int128`` (type alias for ``dry::Integer``)
   ``integer``                            ``dry::Integer`` (struct)
   ``natural``                            ``dry::Natural`` (type alias for ``dry::Integer``)
   ``rational``                           ``dry::Rational`` (struct)
   ``real``                               ``dry::Real`` (struct)
   ``word``                               ``dry::Word`` (type alias for ``usize``)
   ``word8``                              ``dry::Word8`` (type alias for ``u8``)
   ``word16``                             ``dry::Word16`` (type alias for ``u16``)
   ``word32``                             ``dry::Word32`` (type alias for ``u32``)
   ``word64``                             ``dry::Word64`` (type alias for ``u64``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Rust
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Rust
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Rust
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: Rust <http://ar.to/notes/rust>`__
