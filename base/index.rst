.. index:: module: base

****
base
****

.. only:: html

   .. contents::
      :local:
      :backlinks: entry
      :depth: 2

Description
-----------

.. dry:module:: base

   Base library & types.

Modules
-------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Module
     - Summary

   * - :doc:`simd <simd/index>`
     - Single instruction, multiple data (SIMD) types and operations.

Types
-----

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Type
     - Summary

   * - :doc:`any <any>`
     - Any value. All other types are subtypes of ``any``.

   * - :doc:`bit <bit>`
     - Bit (zero or one).

   * - :doc:`bool <bool>`
     - Boolean (``true`` or ``false``).

   * - :doc:`char <char>`
     - Character (21-bit Unicode code point).

   * - :doc:`complex <complex>`
     - Complex number (arbitrary size).

   * - :doc:`datum <datum>`
     - Datum.

   * - :doc:`error <error>`
     - Error.

   * - :doc:`float <float>`
     - Floating-point number (native size).

   * - :doc:`float16 <float16>`
     - Floating-point number (16-bit half-precision).

   * - :doc:`float32 <float32>`
     - Floating-point number (32-bit single-precision).

   * - :doc:`float64 <float64>`
     - Floating-point number (64-bit double-precision).

   * - :doc:`function <function>`
     - Function.

   * - :doc:`int <int>`
     - Integer number (native size).

   * - :doc:`int8 <int8>`
     - Integer number (8-bit).

   * - :doc:`int16 <int16>`
     - Integer number (16-bit).

   * - :doc:`int32 <int32>`
     - Integer number (32-bit).

   * - :doc:`int64 <int64>`
     - Integer number (64-bit).

   * - :doc:`int128 <int128>`
     - Integer number (128-bit).

   * - :doc:`integer <integer>`
     - Integer number (arbitrary size).

   * - :doc:`interval <interval>`
     - Interval.

   * - :doc:`list <list>`
     - List.

   * - :doc:`map <map>`
     - Map.

   * - :doc:`matrix <matrix>`
     - Matrix (a 2D tensor).

   * - :doc:`nat <nat>`
     - Natural number (native size).

   * - :doc:`natural <natural>`
     - Natural number (arbitrary size).

   * - :doc:`none <none>`
     - The empty type. No other types are subtypes of ``none``.

   * - :doc:`number <number>`
     - Number.

   * - :doc:`optional <optional>`
     - Optional value.

   * - :doc:`predicate <predicate>`
     - Predicate function.

   * - :doc:`quantity <quantity>`
     - Quantity.

   * - :doc:`rational <rational>`
     - Rational number (arbitrary size).

   * - :doc:`real <real>`
     - Real number (arbitrary size).

   * - :doc:`result <result>`
     - Result value.

   * - :doc:`scalar <scalar>`
     - Scalar (a 0D tensor).

   * - :doc:`seq <seq>`
     - Sequence.

   * - :doc:`set <set>`
     - Set.

   * - :doc:`string <string>`
     - String.

   * - :doc:`symbol <symbol>`
     - Symbol.

   * - :doc:`tensor <tensor>`
     - Tensor.

   * - :doc:`tuple <tuple>`
     - Compound type of a fixed number of terms.

   * - :doc:`type <type>`
     - Type.

   * - :doc:`unit <unit>`
     - Unit of measurement.

   * - :doc:`vector <vector>`
     - Vector (a 1D tensor).

   * - :doc:`word <word>`
     - Machine word (native size).

   * - :doc:`word8 <word8>`
     - Machine word (8-bit).

   * - :doc:`word16 <word16>`
     - Machine word (16-bit).

   * - :doc:`word32 <word32>`
     - Machine word (32-bit).

   * - :doc:`word64 <word64>`
     - Machine word (64-bit).

.. toctree::
   :caption: Symbols
   :hidden:

   any
   bit
   bool
   char
   complex
   datum
   error
   float
   float16
   float32
   float64
   function
   int
   int8
   int16
   int32
   int64
   int128
   integer
   interval
   list
   map
   matrix
   nat
   natural
   none
   number
   optional
   predicate
   quantity
   rational
   real
   result
   scalar
   seq
   set
   string
   symbol
   tensor
   tuple
   type
   unit
   vector
   word
   word8
   word16
   word32
   word64

.. toctree::
   :caption: Modules
   :hidden:

   simd <simd/index>
