#!/usr/bin/python3
''' script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean'''

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.236.52.43', '54.237.96.155']


def local_clean(number=0):
    ''' local clean'''
    fd_list = local('ls -1t versions', capture=True)
    fd_list = fd_list.split('\n')
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(fd_list[n:]))
    for i in fd_list[n:]:
        local('rm versions/' + i)


def remote_clean(number=0):
    '''This is for Remote clean'''
    fd_list = run('ls -1t /data/web_static/releases')
    fd_list = fd_list.split('\r\n')
    print(fd_list)
    n = int(number)
    if n in (0, 1):
        n = 1
    print(len(fd_list[n:]))
    for i in fd_list[n:]:
        if i is 'test':
            continue
        run('rm -rf /data/web_static/releases/' + i)


def do_clean(number=0):
    '''The fabric script that deletes out of dates archive'''
    local_clean(number)
    remote_clean(number)
