from ullyeo.handling_app import app, ws, db
from ullyeo.models import *

if __name__ == '__main__':
    db.create_all()
    ws.run(app, port=8787)
