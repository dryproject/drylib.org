********************************
Frequently Asked Questions (FAQ)
********************************

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ut felis
ac risus ullamcorper placerat fermentum eu est. Praesent viverra lacus in
sapien volutpat, a mollis libero hendrerit. Mauris varius, lorem eu pulvinar
volutpat, dolor ligula rhoncus libero, eget porta nunc nisl sit amet est.
Donec eget lectus quis massa varius vulputate molestie eget mauris. In augue
eros, placerat ut erat sed, consectetur ultrices erat. Nunc erat elit,
mollis eget tempor eu, egestas a nisl. In congue sit amet leo et ornare.
Suspendisse justo turpis, dictum luctus purus id, viverra commodo justo.
Pellentesque fringilla sagittis arcu, eu gravida nisl imperdiet at. Nunc
facilisis nulla ut tristique malesuada. Nulla odio neque, aliquet
ullamcorper augue sed, blandit fringilla sapien.

Design Principles
=================

Why is there no ``null`` / ``nil`` value and type?
--------------------------------------------------

The null reference has been called the costliest mistake in computer
science. Its inventor, none other than `Tony Hoare`_, has termed it his
"billion-dollar mistake":

   I call it my billion-dollar mistake. It was the invention of the null
   reference in 1965. At that time, I was designing the first comprehensive
   type system for references in an object oriented language (ALGOL W). My
   goal was to ensure that all use of references should be absolutely safe,
   with checking performed automatically by the compiler. But I couldn't
   resist the temptation to put in a null reference, simply because it was
   so easy to implement. This has led to innumerable errors,
   vulnerabilities, and system crashes, which have probably caused a billion
   dollars of pain and damage in the last forty years.

   -- Tony Hoare, QCon London (2009)

.. _Tony Hoare: https://en.wikipedia.org/wiki/Tony_Hoare

Why are the data structures immutable by default?
-------------------------------------------------

TODO

Numeric Tower
=============

TODO

Supported Languages
===================

Are there any plans to support C#/Erlang/F#/Haskell/Racket/Swift?
-----------------------------------------------------------------

Yes, eventual support for these languages is planned.

Are there any plans to support Objective-C?
-------------------------------------------

There are no plans for explicit Objective-C support, but :doc:`c` can
certainly be used from Objective-C code.
