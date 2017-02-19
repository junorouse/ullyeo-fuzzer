from json import loads

class BaseParser(object):
    def __init__(self, detail: str=""):
        """init parser

        Keyword arguments:
        detail -- chrome request's detail parrt (default "")
        """
        self.tmp = loads(detail)
        self.detail = self.tmp['Details']
        self.type = self.tmp['Type']