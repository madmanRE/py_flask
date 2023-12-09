from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("answer/", methods=["post", "get"])
def answer(text="Все ок!"):
    return f"<p>{text}</p>"


@app.route("/")
def hello_world():
    return render_template("pages/index.html")


if __name__ == "__main__":
    app.run()
