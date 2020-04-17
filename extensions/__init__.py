from .db import init_db


def init_extensions(conf: dict):
    init_db(conf.get('mongodb'))
