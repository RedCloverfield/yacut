from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from flask import flash, render_template

from yacut import app, db
from .forms import URLForm
from .models import URLMap

SYMBOLS_FOR_SHORT_ID = ascii_lowercase + ascii_uppercase + digits


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url:
            if URLMap.query.filter_by(short=short_url).first():
                flash('Предложенный вариант короткой ссылки уже существует')
                return render_template('index.html', form=form)
        else:
            short_url = get_unique_short_id()
        db.session.add(URLMap(
            original=form.original_link.data,
            short=short_url)
        )
        db.session.commit()
    return render_template('index.html', form=form)


def get_unique_short_id():
    short_id = ''
    for i in range(6):
        short_id += choice(SYMBOLS_FOR_SHORT_ID)
    short_url = f'http://127.0.0.1:5000/{short_id}'
    if URLMap.query.filter_by(short=short_url).first():
        get_unique_short_id()
    return short_id
