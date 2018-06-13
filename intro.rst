************
Introduction
************

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

Rationale
=========

- Reduces the cognitive load of frequently switching between different
  programming languages.

- Enables network effects to cross different libraries as well as different
  languages.

- Facilitates code generation for multiple target languages.

Features
========

- Provides predictable package naming across language ecosystems.

- Respects local naming and coding conventions.

Design
======

Naming
------

Module Naming
^^^^^^^^^^^^^

- Modules are organized in a hierarchy, with their names separated by
  slashes (``/``), just as in :term:`URLs <URL>` and on Unix file systems.
  For example, the module ``text/utf8`` is a submodule of the top-level
  module ``text``.
  When mapped to a target language, the module hierarchy and module names
  are transformed accordingly. For example, ``text/utf8`` becomes the
  namespace ``dry::text::utf8`` in C++, the class ``dry.text.UTF8`` in Java,
  and the module ``DRY::Text::UTF8`` in OCaml.

Type Naming
^^^^^^^^^^^

- Types are named in all lowercase, with individual words separated by
  hyphens (``-``). For example, ``process-group``.
  This is sometimes called `Lisp case`_.
  When mapped to a target language, these names adhere to predominant local
  naming conventions. For example, ``trim-left`` becomes ``process_group`` in
  C++ (`snake case`_) and ``ProcessGroup`` in Java (upper `camel case`_).

Term Naming
^^^^^^^^^^^

- Terms (constants and functions) and variables are also named in all lowercase, with
  individual words separated by hyphens (``-``). For example, ``trim-left``.
  When mapped to a target language, these names adhere to predominant local
  naming conventions. For example, ``trim-left`` becomes ``trim_left()`` in
  C++ (`snake case`_) and ``trimLeft()`` in Java (lower `camel case`_).

- Predicate functions end with a question mark (``?``). For example, ``blank?``.
  When mapped to a target language, predicate names adhere to local naming
  conventions and omit the question mark in case it isn't permitted by the
  language syntax. For example, ``blank?()`` in Ruby, but ``is_blank()`` in
  C++ and ``isBlank()`` in Java.

.. _Lisp case:  https://softwareengineering.stackexchange.com/q/104468
.. _snake case: https://en.wikipedia.org/wiki/Snake_case
.. _camel case: https://en.wikipedia.org/wiki/Camel_case

See Also
========

.. seealso::

   `In Search of Silver Bullets for Polyglots <https://speakerdeck.com/bendiken/in-search-of-silver-bullets-for-polyglots-at-pivorak-33>`__ at Speaker Deck
      The slide deck for `@bendiken`_'s talk on the motivation for the project

   `In Search of Silver Bullets for Polyglots <https://www.youtube.com/watch?v=VXg6qYKxIUw>`__ at YouTube
      The video recording of `@bendiken`_'s talk on the motivation for the project

.. _@bendiken: https://github.com/bendiken
