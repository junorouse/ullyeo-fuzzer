from time import time
from base64 import b64encode
from os import system
from json import loads
from hashlib import sha1
from pprint import pprint
from urllib.parse import urlparse

from flask import Flask, request, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db' +\
                                        str(int(time())) + '.sqlite3'
ws = SocketIO(app)
db = SQLAlchemy(app)

from .models import AttackSuccess, Site, Module

sites = []


@app.route('/')
def main():
    a = Module.query.get(1)
    sites = Site.query.all()
    sites_tmp = []

    for site in sites:
        tmp = {}
        tmp['host'] = site.host
        s = sha1()
        s.update(tmp['host'].encode("utf-8"))
        tmp['vuln_count'] = AttackSuccess.query.filter_by(hash=s.digest()).count()
        sites_tmp.append(tmp)

    return render_template('index.html', sites=sites_tmp)


@app.route('/detail/<site_name>')
def detail(site_name):
    results_tmp = []
    s = sha1()
    s.update(site_name.encode("utf-8"))

    results = db.session.query(AttackSuccess.module_id, func.count(AttackSuccess.module_id)).group_by(AttackSuccess.module_id).all()
    for result in results:
        m = Module.query.get(result[0])
        results_tmp.append({
            'id': result[0],
            'name': m.name,
            'count': result[1],
        })

    return render_template('detail.html', detail_site_host=site_name,
                           results=results_tmp)


@app.route('/detail/<site_name>/<module_id>')
def detail_attack(site_name, module_id):
    s = sha1()
    s.update(site_name.encode("utf-8"))
    results = AttackSuccess.query.filter_by(hash=s.digest(), module_id=module_id).all()
    m = Module.query.get(module_id)
    detail_module = {
        'id': module_id,
        'name': m.name,
    }
    return render_template('detail_module.html', results=results,
                           detail_site_host=site_name,
                           detail_module=detail_module)


@app.route('/success', methods=['POST'])
def success():
    """
    post parm:
    (stringify json) payload
    (string) response_data
    (int) module_id
    :return: None
    """
    module_id = request.form['module_id']
    url = request.form['url']
    r_type = request.form['r_type']
    attack_query = request.form['attack_query']
    body = request.form['body']
    request_headers = request.form['request_headers']
    response_headers = request.form['response_headers']
    response_body = request.form['response_body']
    response_status = request.form['response_status']
    url_tmp = urlparse(url)
    host = url_tmp.netloc
    s = sha1()
    s.update(host.encode("utf-8"))

    w = AttackSuccess(module_id=module_id,
                      url=url, r_type=r_type, attack_query=attack_query, body=body,
                      request_headers=request_headers,
                      response_headers=response_headers,
                      response_body=response_body,
                      response_status=response_status,
                      hash=s.digest())
    print(w)
    db.session.add(w)
    db.session.commit()
    return '9ood'


@ws.on('connect')
def ws_connect():
    pass


@ws.on('disconnect')
def ws_disconnect():
    pass


@ws.on("request")
def ws_request(message):
    """
    :param message: chrome request object
    :return:
    """
    global sites

    r = loads(message)
    url = urlparse(r['url'])
    host = url.netloc
    try:
        assert sites.index(host) is not None
    except ValueError as e:
        # site attack
        sites.append(host)
        s = Site(host=host)
        db.session.add(s)
        try:
            db.session.commit()
        except IntegrityError:
            pass

    # module attack
    system('/Users/pace/.virtualenvs/fuz/bin/python handling_module.py "%s" &' % (b64encode(message.encode("utf-8")).decode("utf-8")))
