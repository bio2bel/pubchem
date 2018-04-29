Bio2BEL PubChem
===============
This repository has multiple goals, most importantly: mapping between MeSH, PubChem, and standard chemical identifiers.
Currently, this information is scattered and incredibly difficult to access. First the following resources are
available:

- ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/README-Extras
    - Map to MeSH with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-MeSH
    - Map to Substance with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-SID.gz
    - Map to InChI with ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz
- ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/README-Extras
    - Map to MeSH with ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-MeSH
    - Map to other databases with ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-Map.gz

Installation
------------
:code:`pip3 install git+https://github.com/bio2bel/pubchem.git`

Command Line Interface
----------------------
After installing, run with either:

- :code:`python3 -m bio2bel_pubchem` or
- :code:`bio2bel_pubchem`

See ``--help`` for the list of commands, which include database population and a web interface for viewing its contents.
