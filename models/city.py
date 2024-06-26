#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.place import Place
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete-orphan',
                              backref="cities")

    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
