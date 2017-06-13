import sqlite3
from peewee import *
import os
from playhouse.db_url import connect
#Choose what DB to be used, for debugging purp.
def get_db():
	db_url = os.environ.get("DATABASE_URL")
	if db_url:
		db = connect(db_url)
		print("Using postgres")
	else:
		database = 'sqlite.db'
		db = SqliteDatabase(database)
	return db
#init db conn
db = get_db()
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
		print("Database up and running")
	db.connect()

def create_msg(msg, email, days):
	time = time.time()
	time += days*86400000 #Convert days to miliseconds
	User.create(email=email, msg=msg, time=time)

def get_user(email):
	try:
		user = User.get(User.email == email)
	except:
		return False
	return user
init_db()