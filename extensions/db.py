from pymongo import MongoClient
from mongoengine import connect


def init_db(conf: dict) -> MongoClient:
    return connect(**conf)
