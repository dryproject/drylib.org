:tocdepth: 1

.. index:: pair: Common Lisp; language
.. highlight:: common-lisp

**********************
DRYlib for Common Lisp
**********************

.. contents::
   :local:
   :backlinks: entry
   :depth: 2

Getting Started
===============

Prerequisites
-------------

- a `Common Lisp <https://en.wikipedia.org/wiki/Common_Lisp>`__
  implementation with
  `ASDF <https://common-lisp.net/project/asdf/>`__ 3.1+

Installation
------------

To install DRYlib on a host with ASDF 3, clone this source repository into
some standard directory where ASDF looks for systems; for example:

.. code-block:: bash

   $ mkdir -p ~/.local/share/common-lisp/source/
   $ cd ~/.local/share/common-lisp/source/
   $ git clone https://github.com/dryproject/drylib.lisp.git drylib

See also
`Configuring ASDF
<https://common-lisp.net/project/asdf/asdf/Configuring-ASDF.html#Configuring-ASDF>`__
in the ASDF manual.

Library Usage
-------------

To load (and compile, if necessary) the DRYlib system, do::

   (asdf:require-system :drylib)

On many Common Lisp implementations, ASDF hooks into the ``cl:require``
facility and you can simply say::

   (require :drylib)

See also
`Using ASDF
<https://common-lisp.net/project/asdf/asdf/Using-ASDF.html#Using-ASDF>`__
in the ASDF manual.

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Common Lisp
   ====================================== ======================================
   ``base``                               ``dry`` (package)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``dry/math`` (package)
   ``media``                              TODO
   ``meta``                               ``dry/meta`` (package)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``dry/text`` (package)
   ``text/ascii``                         ``dry/text/ascii`` (package)
   ``text/printf``                        ``dry/text/printf`` (package)
   ``text/utf8``                          ``dry/text/utf8`` (package)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Common Lisp
   ====================================== ======================================
   ``bool``                               ``dry:bool`` (type with members ``true`` and ``false``)
   ``char``                               ``dry:char`` (type alias for ``character``)
   ``complex``                            ``dry:complex`` (type constrainted by ``complexp``)
   ``float``                              ``dry:float`` (type disjunction of ``dry:float{32,64}``)
   ``float32``                            ``dry:float32`` (type alias for ``single-float``)
   ``float64``                            ``dry:float64`` (type alias for ``double-float``)
   ``int``                                ``dry:int`` (type alias for ``fixnum``)
   ``int8``                               ``dry:int8`` (type alias for ``signed-byte 8``)
   ``int16``                              ``dry:int16`` (type alias for ``signed-byte 16``)
   ``int32``                              ``dry:int32`` (type alias for ``signed-byte 32``)
   ``int64``                              ``dry:int64`` (type alias for ``signed-byte 64``)
   ``int128``                             ``dry:int128`` (type alias for ``signed-byte 128``)
   ``integer``                            ``dry:integer`` (type alias for ``signed-byte``)
   ``natural``                            ``dry:natural`` (type constrainted by ``nonnegativep``)
   ``rational``                           ``dry:rational`` (type constrainted by ``rationalp``)
   ``real``                               ``dry:real`` (type disjunction of ``dry:{rational,float}``)
   ``word``                               ``dry:word`` (type alias for ``dry:word64``)
   ``word8``                              ``dry:word8`` (type alias for ``unsigned-byte 8``)
   ``word16``                             ``dry:word16`` (type alias for ``unsigned-byte 16``)
   ``word32``                             ``dry:word32`` (type alias for ``unsigned-byte 32``)
   ``word64``                             ``dry:word64`` (type alias for ``unsigned-byte 64``)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Common Lisp
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Common Lisp
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    Common Lisp
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

- `Arto's Notes re: Common Lisp <http://ar.to/notes/common-lisp>`__
