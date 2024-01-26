#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity table"""
    __tablename__ = 'amenities'
    if storage_t == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
