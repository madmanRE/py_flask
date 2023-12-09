from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    find = StringField()
    submit = SubmitField("Искать")
