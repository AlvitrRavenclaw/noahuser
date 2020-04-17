from typing import List

from fastapi import APIRouter
from bson.objectid import ObjectId

from .schema import LoginEntry
from .entity import Auth


api_auth = APIRouter()


@api_auth.post('/login')
def login(entry: LoginEntry) -> dict:
    Auth(user_id=ObjectId(), token='hahaha').save()
    return {'success': True}


@api_auth.get('/check')
def check() -> dict:
    objects: List[Auth] = Auth.objects
    return {'item': objects[0].to_mongo().to_dict()}
