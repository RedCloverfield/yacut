from random import choices

from flask import flash, render_template, redirect

from yacut import app, db
from settings import SYMBOLS_FOR_SHORT_ID
from .constants import Messages
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if (short := form.custom_id.data):
        if URLMap.query.filter_by(short=short).first():
            flash(Messages.ID_ALREADY_EXISTS)
            return render_template('index.html', form=form)
    else:
        short = get_unique_short_id()
    db.session.add(
        URLMap(
            original=form.original_link.data,
            short=short
        )
    )
    db.session.commit()
    return render_template('index.html', form=form, short=short)


@app.route('/<string:short>', methods=['GET'])
def redirect_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404().original
    return redirect(url, code=302)


def get_unique_short_id():
    short = ''.join(choices(SYMBOLS_FOR_SHORT_ID, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_unique_short_id()
    return short
