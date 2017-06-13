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
	if request.method == "GET":
		return render_template("index.html")
	elif request.method == "POST":
		return "POST"
app.run(debug=True)