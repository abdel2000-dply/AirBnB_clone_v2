#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import env_storage
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity table"""
    __tablename__ = 'amenities'
    if env_storage == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
