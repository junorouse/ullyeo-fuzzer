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


class AttackSuccess(db.Model):
    __tablename__ = 'attack_successes'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'))
    request = db.relationship('Request', foreign_keys=[request_id])
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    module = db.relationship('Module', foreign_keys=[module_id])
    """
    payload
    {
        a.request.url
        a.request.headers
        a.request.body
    }
    """
    payload = db.Column(db.String)
    response_data = db.Column(db.String)

    def __init__(self, request_id, module_id, payload, response_data):
        self.request_id = request_id
        self.module_id = module_id
        self.payload = payload
        self.response_data = response_data  # status, headers, text
