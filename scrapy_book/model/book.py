from . import BaseModel
from peewee import *

class Book(BaseModel):
    id = BigIntegerField()
    owner_id = BigIntegerField()
    book_name = CharField()
    author = CharField()
    isbn = CharField()
    press = CharField()
    price = DecimalField()
    description = TextField()
    status = IntegerField()
    category_id = IntegerField()
