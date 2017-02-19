from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Fuzzing(Base):
    __tablename__ = 'fuzzings'
    id = Column(Integer, primary_key=True,)

    def __repr__(self):
        return '<FuzzingTest("%d")>' % (self.id)

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    fuzzing_id = Column(Integer, ForeignKey("fuzzings.id"))
    fuzzing = relationship("Fuzzing", foreign_keys=[fuzzing_id])
    
    request_id = Column(Integer,)

    method = Column(String,)
    url = Column(String,)
    request_body = Column(String,)

    status = Column(Integer, default=0)
    
    def __init__(self, fuzzing_id, request_id, url, method, request_body=''):
        self.fuzzing_id = fuzzing_id
        self.request_id = request_id
        self.url = url
        self.method = method
        self.request_body = request_body

    def __repr__(self):
        return "<Request('%d', '%d', '%d')>" % (self.id, self.fuzzing_id, self.request_id)