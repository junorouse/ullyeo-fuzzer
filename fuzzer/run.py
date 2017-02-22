from SimpleWebSocketServer import SimpleWebSocketServer
from ullyeo import parser, handler
from ullyeo.db import engine, Session
from ullyeo.models import *


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    port = 8787
    f = Fuzzing()

    s = Session()
    s.add(f)
    s.commit()

    server = SimpleWebSocketServer('', port, handler.BaseHandler)
    server.serveforever()

    print("BYE")
