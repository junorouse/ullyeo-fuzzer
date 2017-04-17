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
    global message
    m = importlib.import_module('modules.'+module)
    m.go(message)


def asynchronous():
    threads = []
    print("\033[91m>--------------------------------------------------------------------------------------<\033[37m")
    for module in config.MODULE_LIST:
        print("\033[36m"+module[1]+"\033[37m")
        threads.append(gevent.spawn(fetch, module[1]))
    gevent.joinall(threads)


x = sys.argv[1]
x = b64decode(x).decode("utf-8")
host = sys.argv[2]
host = b64decode(host).decode("utf-8")
pid = getpid()

data = {
    'host': host,
    'pid': str(pid),
}

post('http://localhost:8787/add', data=data)

message = loads(x)
asynchronous()

post('http://localhost:8787/delete', data=data)
