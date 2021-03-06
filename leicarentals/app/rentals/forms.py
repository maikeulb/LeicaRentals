from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RentalForm(FlaskForm):
    customer = StringField('Enter customer name', validators=[DataRequired()])
    lens = StringField('Enter lens', validators=[DataRequired()])
