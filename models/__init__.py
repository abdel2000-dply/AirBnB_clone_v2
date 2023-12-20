#!/usr/bin/python3
""" __init__ module """

from os import environ


storage = ''
env_storage = environ.get('HBNB_TYPE_STORAGE')
if env_storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()