from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CustomerForm(FlaskForm):
    first_name = StringField('Enter customer name', validators=[DataRequired()])
    last_name = StringField('Enter customer name', validators=[DataRequired()])
    date_of_birth = DateField('Enter customer birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    membership_type = SelectField('Select membership type', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
