from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from time import time

engine = create_engine('sqlite:///databases/db'+str(int(time()))+'.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
