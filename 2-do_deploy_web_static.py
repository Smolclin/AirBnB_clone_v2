#!/usr/bin/python3
''' script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy '''

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.236.52.43', '54.237.96.155']


def do_deploy(archive_path):
    ''' distribut an archive to web servers'''
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_exit = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}[1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

    def deploy():
        ''' Creates and distributes archive to the web server'''
        archive_path = do_pack()
        if archive_path is None:
            return False
        return do_deploy(archive_path)