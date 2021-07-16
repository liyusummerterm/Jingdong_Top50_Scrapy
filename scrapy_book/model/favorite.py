from . import BaseModel
from peewee import *

class Favorite(BaseModel):
    id = BigIntegerField()
    user_id = BigIntegerField()
    book_id = BigIntegerField()