from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from time import time
from db_models import *
app = Flask(__name__)
init_db()
@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/save_msg", methods=["POST"])
def save_msg():
	msg = request.form.get("msg")
	days = request.form.get("days")
	email = request.form.get("email")
app.run(debug=True)