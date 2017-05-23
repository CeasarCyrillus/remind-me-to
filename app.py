from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/action", methods=["POST"])
def action():
	msg = request.form["msg"]
	return render_template("index.html", msg=msg)