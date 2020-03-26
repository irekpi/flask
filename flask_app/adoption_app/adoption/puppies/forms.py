from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Pupp:')
    submit = SubmitField('Add PuP')


class DelForm(FlaskForm):
    id = IntegerField('ID of pup to remove')
    submit = SubmitField('Remove Pup')