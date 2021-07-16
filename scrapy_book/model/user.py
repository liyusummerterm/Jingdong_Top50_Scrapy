from . import BaseModel
from peewee import *


class User(BaseModel):
    id = BigIntegerField()
    default_address = BigIntegerField()
    username = CharField()
    password = CharField()
    is_verified = BooleanField()
    real_name = CharField()
    university = CharField()
    student_id = CharField()
    major = CharField()
    phone_number = CharField()
    avatar_url = CharField()
    default_payment = IntegerField()
    edu_email = CharField()
