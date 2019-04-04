from application import app
from flask import render_template

@app.route("/", defaults={"path": ''})
def index(path):
    return render_template("index.html")