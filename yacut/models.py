from datetime import datetime
from random import choices
import re

from settings import SYMBOLS_FOR_SHORT_ID, SHORT_ID_PATTERN
from yacut import db
from .constants import (
    Messages, ORIGINAL_LINK_LENGTH, SHORT_ID_LENGTH, MAX_ATTEMPTS)
from .error_handlers import InvalidAPIUsage


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGTH), nullable=False)
    short = db.Column(db.String(SHORT_ID_LENGTH), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get(short, return_error=False):
        if return_error:
            return URLMap.query.filter_by(short=short).first_or_404()
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_unique_short_id():
        for i in range(MAX_ATTEMPTS):
            short = ''.join(choices(SYMBOLS_FOR_SHORT_ID, k=6))
            if not URLMap.get(short):
                return short
        raise RuntimeError(Messages.GENERATION_ERROR)

    @staticmethod
    def create(original, short, api_validation=False):
        if short:
            if api_validation:
                if (
                    len(short) > SHORT_ID_LENGTH or not
                    re.match(SHORT_ID_PATTERN, short)
                ):
                    raise InvalidAPIUsage(Messages.INCORRECT_ID_FIELD_VALUE)
                if URLMap.get(short):
                    raise InvalidAPIUsage(Messages.ID_ALREADY_EXISTS)
        else:
            short = URLMap.get_unique_short_id()
        url = URLMap(original=original, short=short)
        db.session.add(url)
        db.session.commit()
        return url
