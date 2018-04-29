# -*- coding: utf-8 -*-

"""SQLAlchemy models for Bio2BEL PubChem."""

from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

from .constants import MODULE_NAME

Base = declarative_base()

COMPOUND_TABLE_NAME = f'{MODULE_NAME}_compound'
SUBSTANCE_TABLE_NAME = f'{MODULE_NAME}_substance'
SUBSTANCEXREF_TABLE_NAME = f'{MODULE_NAME}_substancexref'
COMPOUND_SUBSTANCE_TABLE_NAME = f'{MODULE_NAME}_compound_substance'

compound_substance = Table(
    COMPOUND_SUBSTANCE_TABLE_NAME,
    Base.metadata,
    Column('compound_id', Integer, ForeignKey(f'{COMPOUND_TABLE_NAME}.id'), primary_key=True),
    Column('substance_id', Integer, ForeignKey(f'{SUBSTANCE_TABLE_NAME}.id'), primary_key=True)
)


class Substance(Base):
    """Represents a substance."""

    __tablename__ = SUBSTANCE_TABLE_NAME

    id = Column(Integer, primary_key=True)

    substance_id = Column(Integer, nullable=False, unique=True, index=True)


class SubstanceXref(Base):
    """Manages cross references."""

    __tablename__ = SUBSTANCEXREF_TABLE_NAME

    id = Column(Integer, primary_key=True)

    substance_id = Column(Integer, ForeignKey(f'{SUBSTANCE_TABLE_NAME}.id'))
    substance = relationship(Substance, backref=backref('xrefs'))

    source = Column(Text, doc='The name of the source of this substance')
    identifier = Column(Text, doc='The identifier of this substance in its source')


class Compound(Base):
    """Represents a compound."""

    __tablename__ = COMPOUND_TABLE_NAME

    id = Column(Integer, primary_key=True)

    compound_id = Column(Integer, nullable=False, unique=True, index=True)
    inchi = Column(Text, nullable=True)
    inchi_key = Column(Text, nullable=True)

    mesh = Column(Text, doc='MeSH term')

    substances = relationship(Substance, secondary=compound_substance, backref=backref('compounds'))
