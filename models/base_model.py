#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
from os import getenv
import uuid
from models import storage
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time_format = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel(Base):
    """A base class for all hbnb models"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'your_table_name'  # Replace 'your_table_name' with your actual table name
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if getenv("HBNB_TYPE_STORAGE") != "db":
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(val, time_format)
                elif key != '__class__':
                    setattr(self, key, val)
            if not hasattr(self, 'id'):
                self.id = str(uuid.uuid4())
            if not hasattr(self, 'created_at'):
                self.created_at = datetime.now()
            if not hasattr(self, 'updated_at'):
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        if getenv("HBNB_TYPE_STORAGE") == "db":
            dictionary.pop('_sa_instance_state', None)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.strftime(time_format)
        dictionary['updated_at'] = self.updated_at.strftime(time_format)
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
