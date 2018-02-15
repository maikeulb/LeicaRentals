from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.sqlalchemy.fields import QuerySelectField
from app.model import Lens


class LensForm(FlaskForm):
    name = StringField('Enter lens name', validators=[DataRequired()])
    release_date = DateField('Enter lens release_date', validators=[DataRequired()])
    stock = IntegerField('Enter lens stock', validators=[DataRequired()])
    format = QuerySelectField('Select lens format', query_factory=choice_query, 
                                get_label='name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

def choice_query():
    return Lens.query
