.. index:: pair: Go; language
.. highlight:: go

*************
DRYlib for Go
*************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- `Go <https://en.wikipedia.org/wiki/Go_(programming_language)>`__
  1.9+ (due to use of type aliases)

Installation
------------

.. code-block:: bash

   $ go get github.com/dryproject/drylib.go

Library Usage
-------------

To import the library, do::

   import "github.com/dryproject/drylib.go"

Reference
=========

Modules
-------

======================================= ========================================
DRY                                     Go
======================================= ========================================
TODO                                    TODO
======================================= ========================================

Module ``base``
---------------

======================================= ========================================
DRY                                     Go
======================================= ========================================
``bool``                                ``dry.Bool`` (type alias for ``bool``)
``char``                                ``dry.Char`` (type alias for ``rune``)
``complex``                             ``dry.Complex`` (struct)
``float``                               ``dry.Float`` (type alias for ``float64``)
``float32``                             ``dry.Float32`` (type alias for ``float32``)
``float64``                             ``dry.Float64`` (type alias for ``float64``)
``int``                                 ``dry.Int`` (type alias for ``int``)
``int8``                                ``dry.Int8`` (type alias for ``int8``)
``int16``                               ``dry.Int16`` (type alias for ``int16``)
``int32``                               ``dry.Int32`` (type alias for ``int32``)
``int64``                               ``dry.Int64`` (type alias for ``int64``)
``int128``                              ``dry.Int128`` (type alias for ``dry.Integer``)
``integer``                             ``dry.Integer`` (struct)
``natural``                             ``dry.Natural`` (type alias for ``dry.Integer``)
``rational``                            ``dry.Rational`` (struct)
``real``                                ``dry.Real`` (struct)
``word``                                ``dry.Word`` (type alias for ``uint``)
``word8``                               ``dry.Word8`` (type alias for ``uint8``)
``word16``                              ``dry.Word16`` (type alias for ``uint16``)
``word32``                              ``dry.Word32`` (type alias for ``uint32``)
``word64``                              ``dry.Word64`` (type alias for ``uint64``)
======================================= ========================================

Module ``math``
---------------

======================================= ========================================
DRY                                     Go
======================================= ========================================
TODO                                    TODO
======================================= ========================================

Module ``text``
---------------

======================================= ========================================
DRY                                     Go
======================================= ========================================
TODO                                    TODO
======================================= ========================================

See Also
========

- `Arto's Notes re: Go <http://ar.to/notes/go>`__
