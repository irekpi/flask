from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Pupp:')
    submit = SubmitField('Add PuP')


class DelForm(FlaskForm):
    id = IntegerField('ID of pup to remove')
    submit = SubmitField('Remove Pup')


class OwnerForm(FlaskForm):
    name = IntegerField('Name of the owner')
    pup_id = IntegerField('The id of a puppy')
    submit = SubmitField('Add and owner')
