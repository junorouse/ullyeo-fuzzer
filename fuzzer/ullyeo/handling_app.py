from time import time

from flask import Flask, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db' +\
                                        str(int(time())) + '.sqlite3'
ws = SocketIO(app)
db = SQLAlchemy(app)

from .models import AttackSuccess


@app.route('/')
def main():
    """
    @TODO: implement graphic view
    """
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
    return 'fuck'


@ws.on('connect')
def ws_connect():
    pass


@ws.on('disconnect')
def ws_disconnect():
    pass


@ws.on("request")
def ws_request(message):
    print('request come')
