from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TokenForm(FlaskForm):
    token = StringField("API Access Token", validators=[DataRequired()])
    rememberMe = BooleanField("Remember Me")
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    query = StringField("Search")
    submit = SubmitField("Search")