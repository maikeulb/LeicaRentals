from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import MembershipType

    
def choice_query():
    return MembershipType.query

class CustomerForm(FlaskForm):
    first_name = StringField('Enter customer name', validators=[DataRequired()])
    last_name = StringField('Enter customer name', validators=[DataRequired()])
    date_of_birth = DateField('Enter customer birthdate', format='%Y-%m-%d', validators=[DataRequired()])
    membership_type = QuerySelectField('Select membership type', query_factory=choice_query,
                                       get_label='name', validators=[DataRequired()])
    submit = SubmitField('Submit')
