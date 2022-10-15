from peewee import *


db = PostgresqlDatabase(
    'db', user='postgres', password='12345678',
    host='localhost', port=5432
)


class Users(Model):
    id = IntegerField()
    code = TextField(default='ru')

    class Meta:
        database = db
        db_table = 'Users'


class Languages(Model):
    code = TextField()
    meet = TextField()
    name = TextField()
    lang = TextField()
    reg = TextField()
    sec = TextField()
    user = TextField()
    about = TextField()
    help = TextField()

    class Meta:
        database = db
        db_tables = 'Languages'


def Create():
    return db.create_tables([Users, Languages], safe=True)


def Register(user):
    if Users.select(id).where(id=user):
        return Select()

    Users.insert(id=user).execute()


def SelectUser(user):
    Users.select(id).where(id=user)