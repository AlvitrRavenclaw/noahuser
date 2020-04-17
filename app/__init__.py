from fastapi import FastAPI

from app.auth.api import api_auth


def include_routers(app: FastAPI):
    app.include_router(api_auth, prefix='/auth')
