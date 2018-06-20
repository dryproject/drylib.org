.. index:: module: logic

*****
logic
*****

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Description
-----------

.. dry:module:: logic

   Logical operations.

Functions
---------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Function
     - Summary

   * - :doc:`and <and>`
     - Logical conjunction operation.

   * - :doc:`nand <nand>`
     - Alternative denial operation. Equivalent to ``(not (and ...))``.

   * - :doc:`nor <nor>`
     - Joint denial operation. Equivalent to ``(not (or ...))``.

   * - :doc:`not <not>`
     - Logical complement operation.

   * - :doc:`or <or>`
     - Logical disjunction operation.

   * - :doc:`xnor <xnor>`
     - Logical biconditional operation.

   * - :doc:`xor <xor>`
     - Exclusive disjunction operation.

.. toctree::
   :caption: Symbols
   :hidden:

   and
   nand
   nor
   not
   or
   xnor
   xor
