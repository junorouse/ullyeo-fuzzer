import importlib
from json import loads
from base64 import b64decode
import sys

import gevent.monkey
gevent.monkey.patch_socket()
import gevent

from requests import post

import config


def fetch(module):
    global message
    m = importlib.import_module('modules.'+module)
    m.go()

    url = 'http://localhost:8787/success'
    data = {
        'request_id': 1,
        'module_id': 1,
        'payload': '',
        'response_data': '',
    }
    post(url, data=data)
    return 'a'


def asynchronous(message):
    threads = []
    for module in config.MODULE_LIST:
        threads.append(gevent.spawn(fetch, module))
    gevent.joinall(threads)


message = loads(sys.argv[1])
asynchronous(message)