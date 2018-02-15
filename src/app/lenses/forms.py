from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from app.models import Lens


def choice_query():
    return Lens.query

class LensForm(FlaskForm):
    name = StringField('Enter lens name', validators=[DataRequired()])
    release_date = DateField('Enter lens release_date', format='%Y-%m-%d', validators=[DataRequired()])
    stock = IntegerField('Enter lens stock', validators=[DataRequired()])
    format = QuerySelectField('Select lens format', query_factory=choice_query,
                                get_label='name', validators=[DataRequired()])
    submit = SubmitField('Submit')
