from peewee import * 
import os

db = SqliteDatabase(os.path.join(os.path.dirname(__file__), "data/csa_data.db"))

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    class Meta:
        db_table = "Users"

    id = PrimaryKeyField(unique=True)
    user_id = IntegerField() # tg id
    status = TextField()



