from ullyeo.models import *
from ullyeo.db import engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)