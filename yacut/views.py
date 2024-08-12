from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from .models import URLMap

SYMBOLS_FOR_SHORT_ID = ascii_lowercase + ascii_uppercase + digits


def get_unique_short_id():
    short_id = ''
    for i in range(6):
        short_id += choice(SYMBOLS_FOR_SHORT_ID)
    short_url = f'http://127.0.0.1:5000/{short_id}'
    if URLMap.query.filter_by(short=short_url).first():
        get_unique_short_id()
    return short_id
