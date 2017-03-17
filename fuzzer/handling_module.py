import importlib
from json import loads
from base64 import b64decode
import sys

import gevent.monkey
gevent.monkey.patch_all()
import gevent

import config


def fetch(module):
    global message
    m = importlib.import_module('modules.'+module)
    m.go(message)


def asynchronous():
    threads = []
    for module in config.MODULE_LIST:
        threads.append(gevent.spawn(fetch, module))
    gevent.joinall(threads)


x = sys.argv[1]
x = b64decode(x).decode("utf-8")
message = loads(x)
asynchronous()