from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CustomerForm(FlaskForm):
    first_name = StringField('Enter customer name', validators=[DataRequired()])
    last_name = StringField('Enter customer name', validators=[DataRequired()])
    date_of_birth = DateField('Enter customer birthdate', validators=[DataRequired()])
    is_subscribed = BooleanField('Enter if subscribed', validators=[DataRequired()])
    membership_type_id = SelectField('Enter membership type', validators=[DataRequired()])
    submit = SubmitField('Submit')
