========
ropemode
========

|Build status badge| 

.. |Build status badge| image:: https://github.com/python-rope/ropemode/actions/workflows/test.yml/badge.svg
   :target: https://github.com/python-rope/ropemode/actions/workflows/test.yml
   :alt: Build Status

Library for common functionality between ropevim_ and ropemacs_.
See also rope_.

.. _ropevim: https://github.com/python-rope/ropevim
.. _rope: https://github.com/python-rope/rope
.. _ropemacs: https://github.com/python-rope/ropemacs

Users should not install this package directly, but either
ropevim_ or ropemacs_ instead.


Contributing
============


The following sets up a development environment and run the tests:

.. code:: bash

   pip install -e .
   pip install -r test_requirements.txt
   pytest


Special Thanks
==============

Many thanks the following people:

- Ali Gholami Rudi (`@aligrudi`_) for initially creating the initial rope,
  ropemode project and most of Rope's code
