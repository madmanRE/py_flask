from flask import Flask
from flask import render_template
from flask import request
from forms import SearchForm
from hh_parser import hendler
import time
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/answer/", methods=["post", "get"])
def answer():
    if request.method == "POST":
        query = request.form.get("find").lower()
        ready = hendler.main(query)
        return render_template("pages/answer.html")


@app.route("/example/")
def example():
    return render_template("pages/example.html")


@app.route("/")
def index():
    return render_template("pages/index.html")


if __name__ == "__main__":
    app.run()
