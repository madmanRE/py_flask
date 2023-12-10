from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from forms import SearchForm
from hh_parser import hendler
import time
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.getcwd(), "hh_parser.db"
)
db = SQLAlchemy(app)


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f"<skills for {self.title}>"


with app.app_context():
    db.create_all()


def create_skills(title, text, img):
    try:
        s = Skills(title=title, description=text, image=img)
        db.session.add(s)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        print(f"Ошибка добавления в базу данных: {err}")


@app.route("/answer/", methods=["POST", "GET"])
def answer():
    if request.method == "POST":
        query = request.form.get("find").lower()

        skills = Skills.query.filter_by(title=query).first()

        if skills:
            print("Есть в БД")
            skill_list = " ".join(
                list(map(lambda s: s.split(":")[0], skills.description.split()))
            )
            return render_template(
                "pages/answer.html", skills=skills, skill_list=skill_list
            )
        else:
            print("Нет в БД")
            title, description, img = hendler.main(query)
            description_text = " ".join(
                [f"{elem[0]}:{elem[1]}" for elem in description]
            )
            create_skills(title, description_text, img)
            skills = Skills.query.filter_by(title=query).first()

            if skills:
                skill_list = " ".join(
                    list(map(lambda s: s.split(":")[0], skills.description.split()))
                )
                return render_template(
                    "pages/answer.html", skills=skills, skill_list=skill_list
                )
            else:
                return "Ошибка при добавлении в базу данных"


@app.route("/tips/")
def tips():
    return render_template("pages/tips.html")


@app.route("/")
def index():
    return render_template("pages/index.html")


if __name__ == "__main__":
    app.run()
