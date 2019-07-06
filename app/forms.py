from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class second_game_form(FlaskForm):
    text = StringField(validators = [DataRequired()])
    submit = SubmitField('Проверить')
