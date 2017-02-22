from SimpleWebSocketServer import SimpleWebSocketServer
from ullyeo import handler
from ullyeo.db import engine, Session
from ullyeo.models import Base, Fuzzing, Module


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    port = 8787
    f = Fuzzing()
    m = Module()
    m.id = 1
    m.name = "bsqli on idx"

    s = Session()
    s.add(f)
    s.add(m)
    s.commit()

    server = SimpleWebSocketServer('', port, handler.BaseHandler)
    server.serveforever()

    print("BYE")
