# -*- coding: utf-8 -*-

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from bio2bel.utils import get_connection
from bio2bel_pubchem.constants import MODULE_NAME
from bio2bel_pubchem.models import Base, Compound, Substance
from bio2bel_pubchem.parser import get_cid_inchi_df, get_cid_mesh_df

log = logging.getLogger(__name__)


class Manager(object):
    def __init__(self, connection=None):
        self.connection = get_connection(MODULE_NAME, connection=connection)
        self.engine = create_engine(self.connection)
        self.session_maker = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.session = self.session_maker()
        self.create_all()
        self.compounds = {}
        self.substances = {}

    def create_all(self, check_first=True):
        """Create tables"""
        log.info('create tables in {}'.format(self.engine.url))
        Base.metadata.create_all(self.engine, checkfirst=check_first)

    def drop_all(self, check_first=True):
        """Create tables"""
        log.info('dropping tables in {}'.format(self.engine.url))
        Base.metadata.drop_all(self.engine, checkfirst=check_first)

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


if __name__ == '__main__':
    logging.basicConfig(level=20)
    log.setLevel(20)
    m = Manager('mysql+mysqldb://root@localhost/pybel?charset=utf8')
    m.create_all()
    m.populate_cid_mesh()
