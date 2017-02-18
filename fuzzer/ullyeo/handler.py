from pprint import pprint

from SimpleWebSocketServer import WebSocket
from .parser import BaseParser

class BaseHandler(WebSocket):
    def handleMessage(self):
        request = BaseParser(self.data)
        pprint (request.detail['url'])

    def handleConnected(self):
       print (self.address, 'connected')

    def handleClose(self):
       print (self.address, 'closed')
