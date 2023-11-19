#!/usr/bin/python3
"""
A python file for class city
"""
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base, State


class City(Base):
    """
    Class city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
