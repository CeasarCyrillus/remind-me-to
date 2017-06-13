import sqlite3
from peewee import *
import os
db = SqliteDatabase("messeges.db")

#All Models need Meta class and correct DB setup
#That's why they inherit it from the BaseModel
class Base_model(Model):
	class Meta:
		database = db

class Msg(Base_model):
	#Name
	msg = CharField()
	time = CharField()
	email = CharField()

def init_db():
	try:
		os.remove("messeges.db") #Clears db every time
		db.create_tables([Msg])
	except:
		print("Restarted DB")
	db.connect()

def create_msg(msg, email, days):
	time = time.time()
	time += days*86400000 #Convert days to miliseconds
	Msg.create(email=email, msg=msg, time=time)

def get_user(email):
	user = Msg.get(Msg.email == email)
	msg = user.msg
	return msg