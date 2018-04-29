# -*- coding: utf-8 -*-

"""Testing constants and utilities for Bio2BEL PubChem."""

import os

from bio2bel.testing import AbstractTemporaryCacheClassMixin

from bio2bel_pubchem import Manager

#: Base path for the tests directory.
dir_path = os.path.dirname(os.path.realpath(__file__))

#: Path to the mock resources directory.
resources_path = os.path.join(dir_path, 'resources')


class TemporaryCacheClassMixin(AbstractTemporaryCacheClassMixin):
    """A concrete :class:`bio2bel.testing.AbstractTemporaryCacheClassMixin` for Bio2BEL PubChem."""

    Manager = Manager
