from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    term1 = StringField('Term1', validators=[DataRequired()])
    term2 = StringField('Term2', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
