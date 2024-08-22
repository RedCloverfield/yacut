from http import HTTPStatus

from flask import jsonify, request

from yacut import app
from .constants import Messages
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_short_url


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(Messages.BLANK_REQUEST_BODY)
    original = data.get('url')
    if not original:
        raise InvalidAPIUsage(Messages.BLANK_URL_FIELD)
    url = URLMap.create(original, data.get('custom_id'), api_validation=True)
    return jsonify(
        {'url': url.original, 'short_link': get_short_url(url.short)}
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_link(short):
    if url := URLMap.query.filter_by(short=short).first():
        return jsonify({'url': url.original}), HTTPStatus.OK
    raise InvalidAPIUsage(Messages.ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
