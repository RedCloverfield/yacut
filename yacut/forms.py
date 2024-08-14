from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from .constants import Messages


class URLForm(FlaskForm):
    original_link = URLField(
        label='Длинная ссылка',
        validators=[DataRequired(message=Messages.REQUIRED_FIELD)])
    custom_id = URLField(
        label='Ваш вариант короткой ссылки',
        validators=[Length(1, 16), Optional()]
    )
    submit = SubmitField(label='Создать')
