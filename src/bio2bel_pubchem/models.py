# -*- coding: utf-8 -*-

"""PubChem database model"""

from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

TABLE_PREFIX = 'pubchem'
COMPOUND_TABLE_NAME = '{}_compound'.format(TABLE_PREFIX)
SUBSTANCE_TABLE_NAME = '{}_substance'.format(TABLE_PREFIX)
SUBSTANCEXREF_TABLE_NAME = '{}_substancexref'.format(TABLE_PREFIX)
COMPOUND_SUBSTANCE_TABLE_NAME = '{}_compound_substance'.format(TABLE_PREFIX)

compound_substance = Table(
    COMPOUND_SUBSTANCE_TABLE_NAME,
    Base.metadata,
    Column('compound_id', Integer, ForeignKey('{}.id'.format(COMPOUND_TABLE_NAME)), primary_key=True),
    Column('substance_id', Integer, ForeignKey('{}.id'.format(SUBSTANCE_TABLE_NAME)), primary_key=True)
)


class Compound(Base):
    """Represents a compound"""
    __tablename__ = COMPOUND_TABLE_NAME

    id = Column(Integer, primary_key=True)

    compound_id = Column(Integer, nullable=False, unique=True, index=True)
    inchi = Column(Text, nullable=True)

    mesh = Column(Text, doc='MeSH term')

    substances = relationship('Substance', secondary=compound_substance, backref=backref('compounds'))


class Substance(Base):
    """Represents a substance"""
    __tablename__ = SUBSTANCE_TABLE_NAME

    id = Column(Integer, primary_key=True)

    substance_id = Column(Integer, nullable=False, unique=True, index=True)


class SubstanceXref(Base):
    """Manages cross references"""
    __tablename__ = SUBSTANCEXREF_TABLE_NAME

    id = Column(Integer, primary_key=True)

    substance_id = Column(Integer, ForeignKey('{}.id'.format(SUBSTANCE_TABLE_NAME)))
    substance = relationship('Substance', backref=backref('xrefs'))

    source = Column(Text, doc='The name of the source of this substance')
    identifier = Column(Text, doc='The identifier of this substance in its source')
