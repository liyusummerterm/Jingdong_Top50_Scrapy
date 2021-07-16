from . import BaseModel
from peewee import *
import datetime

class Order(BaseModel):
    id = BigIntegerField()
    book_id = BigIntegerField()
    seller_id = BigIntegerField()
    buyer_id = BigIntegerField()
    buyer_addr = BigIntegerField()
    seller_addr = BigIntegerField()
    price = DecimalField()
    payment = IntegerField()
    status = IntegerField()
    create_time = TimestampField(default=datetime.datetime.now())
    modify_time = TimestampField(default=datetime.datetime.now())