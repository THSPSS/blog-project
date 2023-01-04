from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)
from wtforms.validators import input_required,length,DataRequired,email
from wtforms.widgets import PasswordInput

class MyForm(FlaskForm):
    emailField = StringField('email', validators=[input_required(),
                                           length(min=6),DataRequired(),email()])
    passwordField = StringField('password',widget=PasswordInput(hide_value=False),validators=[DataRequired(),length(min=8)])
    submit = SubmitField(label='Log In')