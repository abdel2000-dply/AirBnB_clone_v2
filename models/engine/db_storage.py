'''
#!/usr/bin/python3
""" This module defines a class to manage - db storage - for hbnb clone """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Create the mysql db engine"""
    __engine = None
    __session = None
'''