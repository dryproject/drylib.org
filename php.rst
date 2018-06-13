:tocdepth: 1

.. index:: pair: PHP; language
.. highlight:: php

**************
DRYlib for PHP
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

- `PHP <https://en.wikipedia.org/wiki/PHP>`__
  7.1+ with the `BCMath <https://php.net/manual/en/book.bc.php>`__
  extension (``--enable-bcmath``)

Installation
------------

Installation with Composer
^^^^^^^^^^^^^^^^^^^^^^^^^^

https://packagist.org/packages/dryproject/drylib

To install the library in your project, execute::

   $ composer require dryproject/drylib=dev-master

Alternatively, manually add it as a requirement in your project's
``composer.json`` file::

   {
     "require": {
       "dryproject/drylib": "dev-master"
     }
   }

Installation without Composer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ``drylib.php`` file available in your project by either adding this
source code repository as a Git submodule or just directly importing the
file into your project.

Library Usage
-------------

Usage with Composer
^^^^^^^^^^^^^^^^^^^

To load the library, do::

   require 'vendor/autoload.php';

Usage without Composer
^^^^^^^^^^^^^^^^^^^^^^

To load the library, do::

   require_once 'drylib.php';

Design Principles
=================

Reference
=========

Modules
-------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    PHP
   ====================================== ======================================
   ``base``                               ``dry`` (namespace)
   ``bits``                               TODO
   ``code``                               *N/A*
   ``crypto``                             TODO
   ``data``                               TODO
   ``ffi``                                TODO
   ``geo``                                TODO
   ``io``                                 TODO
   ``lang``                               TODO
   ``logic``                              TODO
   ``math``                               ``dry\math`` (namespace)
   ``media``                              TODO
   ``meta``                               ``dry\meta`` (namespace)
   ``net``                                TODO
   ``qty``                                TODO
   ``std``                                TODO
   ``sys``                                TODO
   ``text``                               ``dry\text`` (namespace)
   ``text/ascii``                         ``dry\text\ascii`` (namespace)
   ``text/printf``                        ``dry\text\printf`` (namespace)
   ``text/utf8``                          ``dry\text\utf8`` (namespace)
   ``time``                               TODO
   ``util``                               TODO
   ====================================== ======================================

Module ``base``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    PHP
   ====================================== ======================================
   ``bool``                               ``dry\bool($x)`` (function)
   ``char``                               ``dry\char($c)`` (function)
   ``complex``                            ``dry\complex($r,$i)`` (function), ``dry\Complex`` (class)
   ``float``                              ``dry\float($r)`` (function)
   ``float32``                            ``dry\float32($r)`` (function)
   ``float64``                            ``dry\float64($r)`` (function)
   ``int``                                ``dry\int($z)`` (function)
   ``int8``                               ``dry\int8($z)`` (function)
   ``int16``                              ``dry\int16($z)`` (function)
   ``int32``                              ``dry\int32($z)`` (function)
   ``int64``                              ``dry\int64($z)`` (function)
   ``int128``                             ``dry\int128($x)`` (function)
   ``integer``                            ``dry\integer($z)`` (function), ``dry\Integer`` (class)
   ``natural``                            ``dry\natural($n)`` (function)
   ``rational``                           ``dry\rational($n,$d)`` (function), ``dry\Rational`` (class)
   ``real``                               ``dry\real($r)`` (function), ``dry\Real`` (class)
   ``word``                               ``dry\word($n)`` (function)
   ``word8``                              ``dry\word8($n)`` (function)
   ``word16``                             ``dry\word16($n)`` (function)
   ``word32``                             ``dry\word32($n)`` (function)
   ``word64``                             ``dry\word64($n)`` (function)
   ====================================== ======================================

Module ``math``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    PHP
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``meta``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    PHP
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

Module ``text``
---------------

.. table::
   :widths: 50 50

   ====================================== ======================================
   DRY                                    PHP
   ====================================== ======================================
   TODO                                   TODO
   ====================================== ======================================

See Also
========

.. seealso::

   `Changelog <https://github.com/dryproject/drylib.php/blob/master/CHANGES.rst>`__ on GitHub
      The comprehensive version history and release notes for DRYlib for PHP.

   `Arto's Notes re: PHP <http://ar.to/notes/php>`__
      Miscellaneous notes on PHP.
