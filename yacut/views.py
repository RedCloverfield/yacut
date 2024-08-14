from random import choice

from flask import flash, render_template, redirect

from yacut import app, db
from .forms import URLForm
from .models import URLMap
from settings import SYMBOLS_FOR_SHORT_ID


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        if (short_id := form.custom_id.data):
            if URLMap.query.filter_by(short=short_id).first():
                flash('Предложенный вариант короткой ссылки уже существует')
                return render_template('index.html', form=form)
        else:
            short_id = get_unique_short_id()
        db.session.add(
            URLMap(
                original=form.original_link.data,
                short=short_id
            )
        )
        db.session.commit()
        return render_template('index.html', form=form, short_id=short_id)
    return render_template('index.html', form=form)


@app.route('/<string:short_id>/', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404().original
    return redirect(url, code=302)


def get_unique_short_id():
    short_id = ''
    for i in range(6):
        short_id += choice(SYMBOLS_FOR_SHORT_ID)
    if URLMap.query.filter_by(short=short_id).first():
        get_unique_short_id()
    return short_id
