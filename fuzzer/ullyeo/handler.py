from pprint import pprint

from SimpleWebSocketServer import WebSocket
from .parser import BaseParser
from .models import Request

from ullyeo.db import Session
from ullyeo.models import Request


class BaseHandler(WebSocket):
    def handleMessage(self):
        try:
            request = BaseParser(self.data)

            request_type = request.type
            request_url = request.url
            request_method = request.method
            request_id = request.id

            s = Session()
            if request_type == 'Request':
                # do request
                request_body = ''
                try:
                    request_body = str(request.detail['requestBody'])
                except Exception as e:
                    pass
                finally:
                    r = Request(1, request_id, request_url, request_method, request_body=request_body)
                    s.add(r)
                    s.commit()
            elif request_type == 'SendHeaders':
                # do send headers
                # filter by fuzzing id
                request_headers = ''
                try:
                    request_headers = str(request.detail['requestHeaders'])
                except Exception as e:
                    pass
                finally:
                    r = Request(1, request_id, request_url, request_method, status=1, request_header=request_headers)
                    s.add(r)
                    s.commit()
            elif request_type == 'Received':
                # do received
                # response_headers = request.detail['responseHeaders']
                pass
            elif request_type == 'Body':
                # do body
                pass
            elif request_type == 'Completed':
                # do completed
                response_headers = ''
                try:
                    response_headers = str(request.detail['responseHeaders'])
                except Exception as e:
                    pass
                finally:
                    r = Request(1, request_id, request_url, request_method, status=4, response_header=response_headers)
                    s.add(r)
                    s.commit()
        except Exception as e:
            print (e)
            exit(0)


    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')
