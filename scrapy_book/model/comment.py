from . import BaseModel
from peewee import *

class Comment(BaseModel):
    id = BigIntegerField()
    from_id = BigIntegerField()
    book_id = BigIntegerField()
    content = TextField()
    review_rank = IntegerField()
    create_time = TimestampField()
    modify_time = TimestampField()
