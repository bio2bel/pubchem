# -*- coding: utf-8 -*-

import logging

from bio2bel import AbstractManager
from tqdm import tqdm

from bio2bel_pubchem.constants import MODULE_NAME
from bio2bel_pubchem.models import Base, Compound, Substance, SubstanceXref
from bio2bel_pubchem.parser import get_cid_inchi_df, get_cid_mesh_df

log = logging.getLogger(__name__)


class Manager(AbstractManager):
    """Manager for Bio2BEL PubChem."""

    module_name = MODULE_NAME
    flask_admin_models = [Compound, Substance, SubstanceXref]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.compounds = {}
        self.substances = {}

    @property
    def _base(self):
        return Base

    def is_populated(self):
        """Check if the database is already populated."""

    def count_compounds(self) -> int:
        """Count the number of compounds in the database."""
        return self._count_model(Compound)

    def count_substances(self) -> int:
        """Count the number of substances in the database."""
        return self._count_model(Substance)

    def count_substance_cross_references(self) -> int:
        """Count the number of cross references for substances in the database."""
        return self._count_model(SubstanceXref)

    def summarize(self):
        """Returns a summary of the contents of the database.

        :rtype: dict[str,int]
        """
        return dict(
            compounds=self.count_compounds(),
            substances=self.count_substances(),
            substance_cross_references=self.count_substance_cross_references(),
        )

    def get_or_create_compound(self, compound_id, **kwargs):
        if compound_id in self.compounds:
            return self.compounds[compound_id]

        compound = self.session.query(Compound).filter(Compound.compound_id == compound_id).one_or_none()

        if compound is None:
            compound = Compound(
                compound_id=compound_id,
                **kwargs
            )
            self.compounds[compound_id] = compound

        return compound

    def get_or_create_substance(self, substance_id, **kwargs):
        if substance_id in self.substances:
            return self.substances[substance_id]

        substance = self.session.query(Substance).filter(Substance.substance_id == substance_id).one_or_none()

        if substance is None:
            substance = Substance(
                substance_id=substance_id,
                **kwargs
            )
            self.substances[substance_id] = substance

        return substance

    def populate_cid_inchis(self, url=None):
        log.info('downloading inchis')
        df = get_cid_inchi_df(url=url)

        log.info('populating inchis')
        for _, (compound_id, inchi, inchi_key) in tqdm(df.iterrows(), desc='inchis', total=len(df.index)):
            compound = self.get_or_create_compound(compound_id)
            compound.inchi = inchi
            compound.inchi_key = inchi_key
            self.session.add(compound)

        self.session.commit()

    def populate_cid_mesh(self, url=None):
        log.info('downloading cid-mesh mapping')
        df = get_cid_mesh_df(url=url)

        log.info('populating cid-mesh mapping')
        for _, (compound_id, mesh) in tqdm(df.iterrows(), desc='cid-mesh', total=len(df.index)):
            compound = self.get_or_create_compound(compound_id)
            compound.mesh = mesh
            self.session.add(compound)

        self.session.commit()

    def populate(self, cid_mesh_url=None, inchis_url=None):
        self.populate_cid_mesh(url=cid_mesh_url)
        self.populate_cid_inchis(url=inchis_url)
