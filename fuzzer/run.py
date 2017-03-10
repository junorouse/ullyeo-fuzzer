from pprint import pprint
from flask import Flask
from flask_socketio import SocketIO

from json import loads

app = Flask(__name__)
ws = SocketIO(app)
port = 8787


@app.route('/')
def main():
    return 'hello'


@ws.on('connect')
def connect():
    pass


@ws.on('disconnect')
def disconnect():
    pass


@ws.on("request")
def request(message):
    pprint(loads(message))

if __name__ == '__main__':
    ws.run(app, port=port)
