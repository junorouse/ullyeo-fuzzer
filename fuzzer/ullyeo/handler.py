from pprint import pprint

from SimpleWebSocketServer import WebSocket
from .parser import BaseParser

class BaseHandler(WebSocket):
    def handleMessage(self):
        request = BaseParser(self.data)

        type = request.type
        if type == 'Request':
            # do request
            try:
                request_body = request.detail['requestBody']
                print (request.type),
                print (request.detail['method']),
                pprint (request_body)
            except KeyError as e:
                pass
            pass
        elif type == 'SendHeaders':
            # do send headers
            request_headers = request.detail['requestHeaders']
            pass
        elif type == 'Received':
            # do received
            response_headers = request.detail['responseHeaders']
            pass
        elif type == 'Body':
            # do body
            pass
        elif type == 'Completed':
            # do complted
            response_headers = request.detail['responseHeaders']
            pass

        
    def handleConnected(self):
       print (self.address, 'connected')

    def handleClose(self):
       print (self.address, 'closed')
