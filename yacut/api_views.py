from flask import jsonify, request, url_for

from yacut import app, db
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json(silent=True)
    db.session.add(
        URLMap(
            original=data.get('url'),
            short=data.get('custom_id')
        )
    )
    db.session.commit()
    short_link = url_for('redirect_view', short_id=data.get('custom_id'), _external=True)
    return jsonify({'url': data.get('url'), 'short_link': short_link}), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    url = URLMap.query.filter_by(short=short_id).first().original
    return jsonify({'url': url}), 200
