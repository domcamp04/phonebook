from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class user_info_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    