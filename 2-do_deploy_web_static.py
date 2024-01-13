#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import run, env, put
from os.path import exists

env.hosts = ['52.73.245.246', '54.146.73.137']


def do_deploy(archive_path):
    """ do_deploy function """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1].split('.')[0]
        path_to = f"/data/web_static/releases/{archive_name}"
        symlink = "/data/web_static/current"

        put(archive_path, '/tmp/')
        run(f"mkdir -p {path_to}")
        run(f"tar -xzf /tmp/{archive_name}.tgz -C {path_to}/")
        run(f"rm /tmp/{archive_name}.tgz")
        run(f"mv {path_to}/web_static/* {path_to}/")
        run(f"rm -rf {path_to}/web_static")
        run(f"rm -rf {symlink}")
        run(f"ln -s {path_to}/ {symlink}")

        print("New version deployed!")
        return True
    except Exception:
        return None
