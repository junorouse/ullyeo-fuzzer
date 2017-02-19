from pprint import pprint

from SimpleWebSocketServer import WebSocket
from .parser import BaseParser
from .models import Request

from ullyeo.db import Session
from ullyeo.models import Request


class BaseHandler(WebSocket):
    def handleMessage(self):
        request = BaseParser(self.data)

        type = request.type
        url = request.url
        method = request.method
        s = Session()
        if type == 'Request':
            # do request
            try:
                request_body = str(request.detail['requestBody'])
                r = Request(1, request.detail['requestId'], url, method, request_body)
                s.add(r)
                s.commit()
                print (request.type),
                print (request.detail['method']),
                pprint (request_body)
            except KeyError as e:
                print (e)
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
