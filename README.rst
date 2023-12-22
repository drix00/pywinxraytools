pyWinxrayTools
==============

Overview
========

Python interface to read and write WinX-Ray files.
http://montecarlomodeling.mcgill.ca/software/winxray/winxray.html


.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |coveralls|
    * - package
      - |
        |

.. |docs| image:: https://readthedocs.org/projects/pywinxraytools/badge/?version=latest
    :target: https://pywinxraytools.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/drix00/pywinxraytools.svg?branch=master
    :target: https://travis-ci.org/drix00/pywinxraytools
    :alt: Travis-CI Build Status

.. |coveralls| image:: https://coveralls.io/repos/github/drix00/pywinxraytools/badge.svg?branch=master
    :target: https://coveralls.io/github/drix00/pywinxraytools?branch=master
    :alt: Coveralls Coverage Status


.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/drix00/pywinxraytools?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pytestbot/pywinxraytools

.. |requires| image:: https://requires.io/github/drix00/pywinxraytools/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/drix00/pywinxraytools/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pywinxraytools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pywinxraytools

.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/pywinxraytools.svg
    :target: https://anaconda.org/conda-forge/pywinxraytools

.. |commits-since| image:: https://img.shields.io/github/commits-since/drix00/pywinxraytools/v2.7.1.svg
    :target: https://github.com/drix00/pywinxraytools/compare/v2.7.1...master
    :alt: Commits since latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/pywinxraytools.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pywinxraytools

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pywinxraytools.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pywinxraytools

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pywinxraytools.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pywinxraytools

.. end-badges


Development
===========

In the *winxraytools folder*, run to install the project in develop mode

.. code:: shell

   pip install -e .

Build the documentation:

.. code-block:: console

    $ cd docs
    $ make html

Add or modify the API documentation:

.. code-block:: console

    $ cd docs
    $ sphinx-apidoc -o api -e -f -P ../winxraytools
    $ make html

Before committing your modification.

In the *winxraytools folder*, run the tests:

.. code-block:: console

    $ pytest -v

check the code style:

.. code-block:: console

    $ pycodestyle .
    $ pyflakes .


To do
-----

.. todolist::
