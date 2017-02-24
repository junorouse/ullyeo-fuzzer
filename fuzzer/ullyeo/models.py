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
    request_header = Column(String, default='')
    response_header = Column(String, default='')
    request_body = Column(String,)

    status = Column(Integer, default=0)

    def __init__(self, fuzzing_id, request_id, url, method, status=0, request_body='', request_header='', response_header=''):
        self.fuzzing_id = fuzzing_id
        self.request_id = request_id
        self.url = url
        self.method = method
        self.status = status
        self.request_body = request_body
        self.request_header = request_header
        self.response_header = response_header

    def __repr__(self):
        return "<Request('%s', '%s', '%s', '%s')>" % (self.fuzzing_id, self.fuzzing_id, int(self.status), self.request_id)


class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class AttackSuccess(Base):
    __tablename__ = 'attack_successes'
    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey('requests.id'))
    request = relationship('Request', foreign_keys=[request_id])
    module_id = Column(Integer, ForeignKey('modules.id'))
    module = relationship('Module', foreign_keys=[module_id])
    """
    payload
    {
        a.request.url
        a.request.headers
        a.request.body
    }
    """
    payload = Column(String)

    def __init__(self, request_id, module_id, payload):
        self.request_id = request_id
        self.module_id = module_id
        self.payload = payload
