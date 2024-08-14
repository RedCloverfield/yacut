import os
from string import ascii_lowercase, ascii_uppercase, digits


SYMBOLS_FOR_SHORT_ID = ascii_lowercase + ascii_uppercase + digits


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
