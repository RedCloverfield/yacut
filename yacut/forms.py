from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from .constants import Messages, ORIGINAL_LINK_LENGTH, SHORT_ID_LENGTH

LONG_LINK = 'Длинная ссылка'
SHORT_LINK = 'Ваш вариант короткой ссылки'
CREATE_OBJECT = 'Создать'


class URLForm(FlaskForm):
    original_link = URLField(
        label=LONG_LINK,
        validators=[
            DataRequired(message=Messages.REQUIRED_FIELD),
            Length(max=ORIGINAL_LINK_LENGTH)
        ])
    custom_id = URLField(
        label=SHORT_LINK,
        validators=[Length(max=SHORT_ID_LENGTH), Optional()]
    )
    submit = SubmitField(label=CREATE_OBJECT)
