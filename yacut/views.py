from http import HTTPStatus

from flask import flash, render_template, redirect, url_for

from yacut import app
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        url = URLMap.create(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        return render_template(
            'index.html',
            form=form,
            short=url.short,
            short_url=get_short_url(url.short)
        )
    except RuntimeError as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_view(short):
    url = URLMap.get(short, return_error=True).original
    return redirect(url, code=HTTPStatus.FOUND)


def get_short_url(short):
    return url_for('redirect_view', short=short, _external=True)
