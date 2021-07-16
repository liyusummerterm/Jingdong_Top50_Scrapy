from . import BaseModel
from peewee import *

class Address(BaseModel):
    id = BigIntegerField()
    user_id = BigIntegerField()
    province = CharField()
    city = CharField()
    district = CharField()
    county = CharField()
    street = CharField()
    detailed_address = TextField()
    phone_number = CharField()
    receiver_name = CharField()
    

