#!/usr/bin/python3
""" generates a .tgz archive from the web_static folder """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compress before sending """
    dt = datetime.now().strftime('%Y%M%d%H%M%S')
    try:
        local('mkdir -p versions')
        path = 'versions/web_static_{}.tgz'.format(dt)
        local('tar -czvf {} web_static/'.format(path))
        return path
    except Exception:
        return None
