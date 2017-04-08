#!/USR/BIN/PYTHON
from flask import Flask
import sys

# APP SETTINGS
app = Flask(__name__)
app.config["DEBUG"] = True
app.config.from_object("config")

# CSRF PROTECT AND ASSETS
from flask_wtf.csrf import CsrfProtect
csrf = CsrfProtect(app)

from app import views
