#!/usr/bin/python3
""" This module defines a class to manage - db storage """


class DBStorage:
    """Create the mysql db engine"""
    __engine = None
    __session = None
