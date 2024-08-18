import os
from string import ascii_letters, digits


SYMBOLS_FOR_SHORT_ID = ascii_letters + digits
SHORT_ID_PATTERN = f'^[{SYMBOLS_FOR_SHORT_ID}]*$'


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
