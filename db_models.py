import sqlite3
from peewee import *
import os
from playhouse.db_url import connect

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = 'DB'
db = PostgresqlDatabase(DATABASE)



#All Models need Meta class and correct DB setup
#That's why they inherit it from the BaseModel
class Base_model(Model):
	class Meta:
		database = db

class User(Base_model):
	#Name
	msg = CharField()
	time = CharField()
	email = CharField()

def init_db():
	try:
		db.create_tables([User])
	except:
		raise
	db.connect()

def create_msg(msg, email, days):
	time = time.time()
	time += days*86400000 #Convert days to miliseconds
	User.create(email=email, msg=msg, time=time)

def get_user(email):
	user = User.get(User.email == email)
	return user
init_db()