``pyisbn``
==========

A module for working with 10- and 13-digit ISBNs
------------------------------------------------

Introduction
------------

``pyisbn`` is a `GPL v3`_ licensed module for working with various book
identification numbers.  It includes functions for conversion,
verification and generation of checksums.  It also includes basic
classes for representing ISBNs as objects.

Requirements
------------

``pyisbn`` does not depend on any modules that aren't included in
Python_'s standard library, and as such should run with Python 2.4 or
newer [#]_.  If ``pyisbn`` doesn't work with the version of Python you
have installed, drop me a mail_ and I'll endeavour to fix it.

The module have been tested on many UNIX-like systems, including Linux,
Solaris and OS X, but it should work fine on other systems too.  The
module contains a large collection of ``doctest`` tests that can be run
with ``./setup.py test_code``.  The examples in this file can be tested
with ``./setup.py test_doc``.

.. [#] The module may work with older Python versions, but it has only
       been tested with v2.4 and above.

Example
-------

The simplest way to show how ``pyisbn`` works is by example, and here
goes:

.. code-block:: pycon

    >>> import pyisbn
    >>> Permutation_City = "1-85798-218-5"
    >>> pyisbn.validate(Permutation_City)
    True
    >>> pyisbn.convert(Permutation_City)
    '9781857982183'
    >>> print("ISBN %s" % Permutation_City)
    ISBN 1-85798-218-5

or to process ISBNs using the object pattern use:

.. code-block:: pycon

    >>> Permutation_City = pyisbn.Isbn10("1-85798-218-5")
    >>> Permutation_City.validate()
    True
    >>> Permutation_City.convert()
    '9781857982183'
    >>> print(Permutation_City)
    ISBN 1-85798-218-5

All independent functions contain hopefully useful docstrings with
``doctest``-based examples.  The ``html/`` directory contains the
preprocessed epydoc_ output for reference.

API Stability
-------------

API stability isn't guaranteed across versions, although frivolous
changes won't be made.

When ``pyisbn`` 1.0 is released the API will be frozen, and any
changes which aren't backwards compatible will force a major version
bump.

Hacking
-------

Patches are most welcome, but I'd appreciate it if you could follow the
guidelines below to make it easier to integrate your changes.  These are
guidelines however, and as such can be broken if the need arises or you
just want to convince me that your style is better.

    * `PEP 8`_, the style guide, should be followed where possible.
    * While support for Python versions prior to v2.4 may be added in
      the future if such a need were to arise, you are encouraged to use
      v2.4 features now.
    * All new classes and methods should be accompanied by new
      ``doctest`` examples, and epydoc_'s epytext formatted descriptions
      if at all possible.
    * Tests *must not* span network boundaries, see ``test.mock`` for
      workarounds.
    * ``doctest`` tests in modules are only for unit testing in general,
      and should not rely on any modules that aren't in Python's
      standard library.
    * Functional tests should be in the ``doc`` directory in
      reStructuredText_ formatted files, with actual tests in
      ``doctest`` blocks.  Functional tests can depend on external
      modules, but they must be Open Source.

New examples for the ``doc`` directory are as appreciated as code
changes.

Bugs
----

If you find a bug don't hesitate to drop me a mail_ preferably including
a minimal testcase, or even better a patch!

.. _GPL v3: http://www.gnu.org/licenses/
.. _Python: http://www.python.org/
.. _epydoc: http://epydoc.sourceforge.net/
.. _mail: jnrowe@gmail.com
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html

..
    :vim: set ft=rst set ts=4 sw=4 et:
