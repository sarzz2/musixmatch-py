musixmatch module for python
=============================
.. image:: https://img.shields.io/pypi/v/musixmatch-py?color=blue
   :target: https://pypi.python.org/pypi/musixmatch-py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/musixmatch-py?color=orange
   :target: https://pypi.python.org/pypi/musixmatch-py
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/pypi/dm/musixmatch-py
   :target: https://pypi.org/project/musixmatch-py/
   :alt: PyPI downloads
.. image:: https://readthedocs.org/projects/musixmatch-py/badge/?version=latest
   :target: https://musixmatch-py.readthedocs.io/en/latest/
   :alt: Documentation Status
.. image:: https://img.shields.io/github/license/sarzz2/musixmatch-py?color=brightgreen
   :alt: License: MIT
.. image:: https://img.shields.io/discord/847486943440797766.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2
   :target: https://discord.gg/3kmWTqx3
   :alt: Discord support server

Pythonic wrapper for the undocumented `musixmatch-py <https://www.musixmatch-py.com/>`_ API.


Installation
------------

**Python 3.6 or higher is required.**

Run the following command:

.. code:: sh

    pip install musixmatch-py



Getting Started
----------------
.. code:: python3

    from musixmatch.main import Musixmatch
    auth = Musixmatch("Your_musixmatch-API-key")
    auth.search_track("Hello")

For list of all functions see documentation


Contribute
----------

- `Source Code <https://github.com/sarzz2/musixmatch-py>`_
- `Issue Tracker <https://github.com/sarzz2/musixmatch-py/issues>`_


Support
-------

If you are having issues, please let me know by joining the discord support server at https://discord.gg/3kmWTqx3

License
-------

The project is licensed under the MIT license.

Links
------

- `PyPi <https://pypi.org/project/musixmatch-py/>`_
- `Documentation <https://musixmatch-py.readthedocs.io/en/latest/API.html#album>`_
- `Discord support server <https://discord.gg/8HgtN6E>`_