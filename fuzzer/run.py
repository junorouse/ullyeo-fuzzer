from SimpleWebSocketServer import SimpleWebSocketServer
from ullyeo import parser, handler
from ullyeo.db import Session
from ullyeo.models import Fuzzing


if __name__ == '__main__':
    port = 8787
    f = Fuzzing()
    s = Session()
    s.add(f)
    s.commit()
    server = SimpleWebSocketServer('', port, handler.BaseHandler)
    server.serveforever()
