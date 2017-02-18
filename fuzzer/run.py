from SimpleWebSocketServer import SimpleWebSocketServer
from ullyeo import parser, handler


if __name__ == '__main__':
    port = 8787
    server = SimpleWebSocketServer('', port, handler.BaseHandler)
    server.serveforever()
