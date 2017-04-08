from app import app
from flask import render_template, render_template_string, send_from_directory, make_response, jsonify, request, redirect, url_for, flash
from app import csrf
import time
import random
import os

from forms import ContactForm
from flask_mail import Message
from flask_mail import Mail
mail = Mail(app)

@app.route("/")
def hello():
    return "Hello World!"
