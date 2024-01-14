#!/usr/bin/python3
""" Deletes out-of-date archives """
from fabric.api import local, run, env
from datetime import datetime
import os

env.hosts = ['52.73.245.246', '54.146.73.137']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        return

    if number < 0:
        return

    number = 1 if number == 0 else number + 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -f {{}}".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number))
