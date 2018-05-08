Bio2BEL PubChem |build| |coverage| |documentation|
==================================================
This repository has multiple goals, most importantly: mapping between MeSH, PubChem, and standard chemical identifiers.
Currently, this information is scattered and incredibly difficult to access. First the following resources are
available:

Data
----
- ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/README-Extras
    - Map to MeSH with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-MeSH
    - Map to Substance with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-SID.gz
    - Map to InChI with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz
- ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/README-Extras
    - Map to MeSH with ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-MeSH
    - Map to other databases with ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-Map.gz

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_pubchem`` can be installed easily from `PyPI <https://pypi.python.org/pypi/bio2bel_pubchem>`_ with
the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_pubchem

or from the latest code on `GitHub <https://github.com/bio2bel/pubchem>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/pubchem.git@master

Setup
-----
PubChem can be downloaded and populated from either the Python REPL or the automatically installed command line
utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_pubchem
    >>> pubchem_manager = bio2bel_pubchem.Manager()
    >>> pubchem_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    bio2bel_pubchem populate

.. |build| image:: https://travis-ci.org/bio2bel/pubchem.svg?branch=master
    :target: https://travis-ci.org/bio2bel/pubchem
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-pubchem/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/pubchem/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_pubchem.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/pubchem/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/pubchem?branch=master
    :alt: Coverage Status

.. |climate| image:: https://codeclimate.com/github/bio2bel/pubchem/badges/gpa.svg
    :target: https://codeclimate.com/github/bio2bel/pubchem
    :alt: Code Climate

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_pubchem.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_pubchem.svg
    :alt: MIT License
