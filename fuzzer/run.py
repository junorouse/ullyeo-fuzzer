from pathlib import Path

from ullyeo.handling_app import app, ws, db
from ullyeo.models import *
from config import MODULE_LIST

if __name__ == '__main__':
    db_sqlite3 = Path("ullyeo/databases/db.sqlite3")
    if not db_sqlite3.is_file():
        print("Create database file.")
        db.create_all()

    for module in MODULE_LIST:
        m = Module(module[0], module[1])
        db.session.add(m)
        try:
            db.session.commit()
            print("Add module %d - %s" % (module[0], module[1]))
        except:
            pass

    ws.run(app, port=8787)
