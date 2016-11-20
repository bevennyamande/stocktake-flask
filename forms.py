from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class ProductCountForm(FlaskForm):
    counted = IntegerField('Count for ', validators=[DataRequired()])