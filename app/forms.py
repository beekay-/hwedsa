from flask.ext.wtf import Form
from wtforms import validators, TextField, PasswordField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import EmailField, TelField, IntegerField, DecimalField, DateField

class EmailForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    telephone = TelField('Phone (optional)', [validators.Length(min=0, max=15)], id="telephone-number")
    name = TextField('Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    baraat = BooleanField('Baraat')
    walima = BooleanField('Walima')
    numguests = SelectField('Total Number of Guests', choices=[('1','1'), ('2','2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),  ('8', '8')])
    comments = TextAreaField('Comments', [validators.DataRequired(), validators.Length(min=10, max=5000)])
