from flask.ext.wtf import Form
from wtforms import validators, TextField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import EmailField, TelField, IntegerField, DecimalField, DateField

class ContactForm(Form):
    email = EmailField('Email (required)', [validators.DataRequired()])
    telephone = TelField('Phone (optional)', [validators.Length(min=0, max=16)], id="telephone-number")
    homeaddress = TextField('', [validators.Length(min=10, max=50)])
    postalcode = TextField('', [validators.Length(min=0, max=8)])
    # servicetype = SelectField('Service Type', choices=[('Insulation','Insulation'), ('Windows and Doors','Windows and Doors'), ('HVAC', 'HVAC')])
    houseID = IntegerField('')
    city = TextField('')
    firstName = TextField('Name', id="first-name")

class EmailForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    telephone = TelField('Phone (optional)', [validators.Length(min=0, max=15)], id="telephone-number")
    name = TextField('Name', [validators.DataRequired(), validators.Length(min=2, max=50)])
    comments = TextAreaField('Comments', [validators.DataRequired(), validators.Length(min=10, max=5000)])

class DataForm(Form):
    startDate = DateField('2015/10/15', [validators.optional()])
    endDate = DateField('2015/10/30', [validators.optional()])
    energyUseGJ = DecimalField('October Natural Gas Use', [validators.optional()])
    houseAge = IntegerField('Year of Construction', [validators.optional()])
    houseArea = IntegerField('House Area', [validators.optional()])
    energuideRating = IntegerField('EnerGuide Rating', [validators.optional()])
    indoorTemp = IntegerField('Night Thermostat Setting', [validators.optional()])
    roofMaterial = TextField('Roof Material', [validators.optional()])
    address = TextField('', [validators.optional()])
    houseID = IntegerField('')
    # city = TextField('')

class LoginForm(Form):
    # Login form fields
    username = TextField('username', validators=[DataRequired()], id='username')
    access_code = PasswordField('access_code', validators=[DataRequired()])
