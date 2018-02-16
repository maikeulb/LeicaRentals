from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField('Birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    membership_type_id = SelectField('Membership Plan', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
