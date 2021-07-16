from . import BaseModel
from peewee import *

class BookPicture(BaseModel):
    class Meta:
        table_name = 'book_picture'
    id = BigIntegerField()
    book_id = BigIntegerField()
    pic_url = CharField()
    width = IntegerField()
    length = IntegerField()
    format = CharField()
    index = IntegerField()