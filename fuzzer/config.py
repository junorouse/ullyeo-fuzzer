from ullyeo.models import Base
from ullyeo.db import engine

MODULE_LIST = [
    'bsqli_on_idx'
]

if __name__ == '__main__':
    Base.metadata.create_all(engine)
