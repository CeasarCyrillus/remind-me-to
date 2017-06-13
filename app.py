from flask import Flask
from flask import render_template
from flask import request
from time import time
from db_models import *
app = Flask(__name__)
init_db()
@app.before_request
def before_request():
	try:
		db.connect()
	except:
		print("Already open")

@app.after_request
def after_request(response):
	db.close()
	return response

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/save_msg", methods=["POST"])
def save_msg():
	msg = request.form.get("msg")
	days = request.form.get("days")
	email = request.form.get("email")
	create_msg(msg, email, days)