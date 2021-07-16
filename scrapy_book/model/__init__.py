from peewee import *

db = MySQLDatabase("system_design", host="gointo.icu", port=3306, user="root",
                   password="nxA5VNjoK4x4ATQ3HRXbgkoBhXH4k2FM")


class BaseModel(Model):
    class Meta:
        database = db
