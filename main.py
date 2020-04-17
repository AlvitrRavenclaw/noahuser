from yaml import safe_load
from fastapi import FastAPI

from app import include_routers
from extensions import init_extensions

app = FastAPI()
include_routers(app)

with open('config.yaml') as fs:
    conf: dict = safe_load(fs)
    init_extensions(conf)




