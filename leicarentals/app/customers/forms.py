from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField, EmailField


class CustomerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(),
                                                    Email()])
    newsletter = BooleanField('Newsletter')
    date_of_birth = DateField(
        'Birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    membership_type_id = SelectField(
        'Membership Plan', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
