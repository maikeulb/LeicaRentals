from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class RentalsForm(FlaskForm):
    name = StringField('Enter lens name', validators=[DataRequired()])
    release_date = DateField('Enter lens release_date', validators=[DataRequired()])
    format_id = SelectField('Enter lens format', validators=[DataRequired()])
    stock = IntegerField('Enter lens stock', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditRentalsForm(FlaskForm):
    name = StringField('Enter lens name', validators=[DataRequired()])
    release_date = DateField('Enter lens release_date', validators=[DataRequired()])
    format_id = SelectField('Enter lens format', validators=[DataRequired()])
    stock = IntegerField('Enter lens stock', validators=[DataRequired()])
    submit = SubmitField('Submit')
