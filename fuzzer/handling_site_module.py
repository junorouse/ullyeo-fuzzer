import importlib
from json import loads
from base64 import b64decode
import sys

import gevent.monkey
gevent.monkey.patch_all()
import gevent

import config
from os import getpid
from requests import post


def fetch(module):
    global host
    m = importlib.import_module('site_modules.'+module)
    m.go(host)


def asynchronous():
    threads = []
    for module in config.SITE_MODULE_LIST:
        threads.append(gevent.spawn(fetch, module[1]))
    gevent.joinall(threads)


host = sys.argv[1]
host = b64decode(host).decode("utf-8")

pid = getpid()

data = {
    'host': host,
    'pid': str(pid),
}

post('http://localhost:8787/add', data=data)

asynchronous()

post('http://localhost:8787/delete', data=data)
