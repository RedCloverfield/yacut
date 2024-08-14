from flask import jsonify, request, url_for

from yacut import app, db
from .constants import Messages
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import SYMBOLS_FOR_SHORT_ID


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(Messages.BLANK_REQUEST_BODY)
    if data.get('url') is None:
        raise InvalidAPIUsage(Messages.BLANK_URL_FIELD)
    if custom_id := data.get('custom_id'):
        if len(custom_id) > 16:
            raise InvalidAPIUsage(Messages.INCORRECT_ID_FIELD_VALUE)
        for symbol in custom_id:
            if symbol not in SYMBOLS_FOR_SHORT_ID:
                raise InvalidAPIUsage(Messages.INCORRECT_ID_FIELD_VALUE)
    else:
        custom_id = get_unique_short_id()
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(Messages.ID_ALREADY_EXISTS)
    db.session.add(
        URLMap(
            original=data.get('url'),
            short=custom_id
        )
    )
    db.session.commit()
    short_link = url_for('redirect_view', short_id=custom_id, _external=True)
    return jsonify({'url': data.get('url'), 'short_link': short_link}), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    if url := URLMap.query.filter_by(short=short_id).first():
        return jsonify({'url': url.original}), 200
    raise InvalidAPIUsage(Messages.ID_NOT_FOUND, 404)
