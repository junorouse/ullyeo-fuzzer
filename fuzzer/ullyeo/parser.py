from json import loads

class BaseParser(object):
    
    def __init__(self, detail: str=""):
        """init parser

        Keyword arguments:
        detail -- chrome request's detail parrt (default "")
        """
        self.status = 0
        self.detail = loads(detail)['Details']