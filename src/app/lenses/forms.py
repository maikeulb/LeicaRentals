from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class LensForm(FlaskForm):
    name = StringField('Lens Model', validators=[DataRequired()])
    release_date = DateField('Lens Release_Date', format='%Y-%m-%d', validators=[DataRequired()])
    number_in_stock = IntegerField('Stock No.', validators=[DataRequired()])
    format_id = SelectField('Lens format', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
