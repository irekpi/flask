from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField


class OwnerForm(FlaskForm):
    name = StringField('Name of the owner')
    pup_id = IntegerField('The id of a puppy')
    submit = SubmitField('Add and owner')