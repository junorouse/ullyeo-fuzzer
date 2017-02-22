from json import loads


class BaseParser(object):
    def __init__(self, detail: str=""):
        """init parser

        Keyword arguments:
        detail -- chrome request's detail parrt (default "")
        """
        self.tmp = loads(detail)
        self.type = self.tmp['Type']  # Request, Completed
        self.detail = self.tmp['Details']
        self.id = self.detail['requestId']
        self.url = self.detail['url']
        self.method = self.detail['method']

        if self.type == 'Request':
            # handle request headers
            pass
        elif self.type == 'Completed':
            # handle response headers
            pass
