from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from wtforms.sqlalchemy.fields import QuerySelectField
from app.model import MembershipType


class CustomerForm(FlaskForm):
    first_name = StringField('Enter customer name', validators=[DataRequired()])
    last_name = StringField('Enter customer name', validators=[DataRequired()])
    date_of_birth = DateField('Enter customer birthdate', validators=[DataRequired()])
    membership_type = QuerySelectField('Select membership type', query_factory=choice_query, 
                                       get_label='name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

def choice_query():
    return MembershipType.query
