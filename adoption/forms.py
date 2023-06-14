from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, Length


class AddPetForm(FlaskForm):
    name = StringField("Name")
    species = SelectField("Species", choices=[
                          ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age of Pet", choices=[
                      (str(i), str(i)) for i in range(31)])
    notes = StringField("Notes about Pet")
    available = RadioField("Available?", choices=[('1', 'Yes'), ('0', 'No')])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    notes = StringField("Notes about Pet")

    available = RadioField("Available?", choices=[('1', 'Yes'), ('0', 'No')])
