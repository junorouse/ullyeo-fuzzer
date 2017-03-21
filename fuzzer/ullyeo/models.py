from hashlib import sha1

from .handling_app import db


class Fuzzing(db.Model):
    __tablename__ = 'fuzzings'
    id = db.Column(db.Integer, primary_key=True,)

    def __repr__(self):
        return '<FuzzingTest("%d")>' % (self.id)


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    module = db.relationship('Module', foreign_keys=[module_id])
    fuzzing_id = db.Column(db.Integer, db.ForeignKey("fuzzings.id"))
    fuzzing = db.relationship("Fuzzing", foreign_keys=[fuzzing_id])

    request_id = db.Column(db.Integer,)

    method = db.Column(db.String,)
    url = db.Column(db.String,)
    request_header = db.Column(db.String, default='')
    response_header = db.Column(db.String, default='')
    request_body = db.Column(db.String,)

    status = db.Column(db.Integer, default=0)

    def __init__(self, fuzzing_id, request_id, url, method, status=0,
                 request_body='', request_header='', response_header=''):
        self.fuzzing_id = fuzzing_id
        self.request_id = request_id
        self.url = url
        self.method = method
        self.status = status
        self.request_body = request_body
        self.request_header = request_header
        self.response_header = response_header

    def __repr__(self):
        return "<Request('%s', '%s', '%s', '%s')>" %\
               (self.fuzzing_id, self.fuzzing_id,
                int(self.status), self.request_id)


class Module(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class AttackSuccess(db.Model):
    __tablename__ = 'attack_successes'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    module = db.relationship('Module', foreign_keys=[module_id])

    url = db.Column(db.String)
    r_type = db.Column(db.String)
    r_method = db.Column(db.String)
    attack_query = db.Column(db.String)
    body = db.Column(db.String)
    request_headers = db.Column(db.String)

    response_headers = db.Column(db.String)
    response_body = db.Column(db.String)
    response_status = db.Column(db.Integer)

    hash = db.Column(db.String)

    def __init__(self, module_id, url, r_type, r_method,
                 attack_query, body, request_headers, response_headers,
                 response_body, response_status, hash):
        self.module_id = module_id
        self.url = url
        self.r_type = r_type
        self.r_method = r_method
        self.attack_query = attack_query
        self.body = body
        self.request_headers = request_headers
        self.response_headers = response_headers
        self.response_body = response_body
        self.response_status = response_status
        self.hash = hash


class Site(db.Model):
    __tablename__ = 'sites'
    hash = db.Column(db.String(20), primary_key=True, unique=True)
    host = db.Column(db.String)

    def __init__(self, host):
        s = sha1()
        s.update(host.encode("utf-8"))
        self.hash = s.digest()
        self.host = host
