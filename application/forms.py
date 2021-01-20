from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class ExerciseForm(FlaskForm):
    """Exercise form"""
    date = DateField('Date')
    name = StringField('Name')
    sets = IntegerField('Sets')
    reps = StringField('Reps')
    weight = FloatField('Weight (lbs)')
    rest = FloatField('Rest (mins)')
    notes = TextAreaField('Notes')
    submit = SubmitField('Submit')
