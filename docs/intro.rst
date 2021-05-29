.. currentmodule:: musixmatch

.. _intro:

Introduction
============

This is the documentation for musixmatch-py, a library for Python to aid
in creating applications that utilise the undocumented musixmatch API.

Prerequisites
-------------

**Python 3.6 or higher is required.**


.. _installing:

Installing
-----------

You can get the library directly from PyPI:

.. code:: sh

    pip install musixmatch-py


Getting Started
----------------
.. code:: python3

    from musixmatch.main import Musixmatch
    auth = Musixmatch("Your_musixmatch-API-key")
    auth.search_track("Hello")

For list of all functions see documentation
