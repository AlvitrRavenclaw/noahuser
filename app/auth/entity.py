from datetime import datetime

from bson.objectid import ObjectId
from mongoengine import Document
from mongoengine import ObjectIdField, StringField, DateTimeField


class Auth(Document):
    user_id = ObjectIdField()
    token = StringField()
    created_at = DateTimeField(default=datetime.now)

    def to_dict(self) -> dict:
        return {
            'id': self.user_id,
            'token': self.token
        }
