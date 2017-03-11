from time import time

from flask import Flask, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db'+str(int(time()))+'.sqlite3'
ws = SocketIO(app)
db = SQLAlchemy(app)

@app.route('/')
def main():
    return 'hello'


@app.route('/success', methods=['POST'])
def success():
    """
    post parm:
    (json) request_data
    (string) response_data
    (int) module_id
    """
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
