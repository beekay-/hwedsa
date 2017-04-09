from app import app
from flask import render_template, send_from_directory, make_response, request, redirect, url_for, flash
from app import csrf
import time
import os

from forms import ContactForm
from flask_mail import Message
from flask_mail import Mail
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")
