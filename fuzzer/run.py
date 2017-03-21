from ullyeo.handling_app import app, ws, db
from ullyeo.models import *

if __name__ == '__main__':
    db.create_all()
    m = Module(1, 'bsqli on idx')
    db.session.add(m)
    db.session.commit()
    ws.run(app, port=8787)
