:tocdepth: 1

text/ascii/empty?
=================

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Description
-----------

.. dry:function:: text/ascii/empty?

   Checks if a string is empty (has length zero).

Implementations
---------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Language
     - Declaration

   * - :doc:`C++ </cpp>`
     - ``bool dry::text::ascii::empty(const dry::string& string)``

   * - :doc:`Go </go>`
     - ``// TODO``

   * - :doc:`Java </java>`
     - ``boolean dry.text.ASCII.isEmpty(dry.String string)``

   * - :doc:`OCaml </ocaml>`
     - ``DRY.Text.ASCII.is_empty : DRY.String.t -> DRY.Bool.t``

Examples
--------

C++
^^^

.. code-block:: c++

   bool result = dry::text::ascii::empty(string);

Go
^^

.. code-block:: go

   // TODO

Java
^^^^

.. code-block:: java

   boolean result = dry.text.ASCII.isEmpty(string);

OCaml
^^^^^

.. code-block:: ocaml

   let result = DRY.Text.ASCII.is_empty(string) in ...
