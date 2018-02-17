from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class LensForm(FlaskForm):
    name = StringField('Model', validators=[DataRequired()])
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[DataRequired()])
    number_in_stock = IntegerField('No. In Stock', validators=[DataRequired()])
    format_id = SelectField('Format', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
