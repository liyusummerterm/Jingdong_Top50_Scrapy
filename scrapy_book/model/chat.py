from peewee import *
from . import BaseModel

class Chat(BaseModel):
    id = BigIntegerField()
    from_id = BigIntegerField()
    to_id = BigIntegerField()
    content = TextField()
    create_time = TimestampField()
    modify_time = TimestampField()