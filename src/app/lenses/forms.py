from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from app.models import Lens


def choice_query():
    return Lens.query

class LensForm(FlaskForm):
    name = StringField('Enter lens name', validators=[DataRequired()])
    release_date = DateField('Enter lens release_date', format='%Y-%m-%d', validators=[DataRequired()])
    stock = IntegerField('Enter lens stock', validators=[DataRequired()])
    format_id = SelectField('Select lens format', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
