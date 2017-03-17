from time import time
from base64 import b64encode
from os import system
from json import loads
from pprint import pprint
from urllib.parse import urlparse

from flask import Flask, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db' +\
                                        str(int(time())) + '.sqlite3'
ws = SocketIO(app)
db = SQLAlchemy(app)

from .models import AttackSuccess, Site

sites = []


@app.route('/')
def main():
    # TODO: implement graphic view
    return 'hello'


@app.route('/success', methods=['POST'])
def success():
    """
    post parm:
    (stringify json) payload
    (string) response_data
    (int) module_id
    :return: None
    """
    request_id = request.form['request_id']
    module_id = request.form['module_id']
    payload = request.form['payload']
    response_data = request.form['response_data']
    w = AttackSuccess(request_id=request_id, module_id=module_id,
                      payload=payload, response_data=response_data)
    db.session.add(w)
    db.session.commit()
    return '9ood'


@ws.on('connect')
def ws_connect():
    pass


@ws.on('disconnect')
def ws_disconnect():
    pass


@ws.on("request")
def ws_request(message):
    """
    :param message: chrome request object
    :return:
    """
    global sites

    r = loads(message)
    url = urlparse(r['url'])
    host = url.netloc
    try:
        assert sites.index(host) is not None
    except ValueError as e:
        # site attack
        sites.append(host)
        s = Site(host=host)
        db.session.add(s)
        try:
            db.session.commit()
        except IntegrityError:
            pass

    # module attack
    system('python handling_module.py "%s" &' % (b64encode(message.encode("utf-8")).decode("utf-8")))
