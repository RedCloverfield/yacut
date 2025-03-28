from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .models import URLMap
from . import api_views, error_handlers, views