from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import (
    DataRequired, Length, Optional, ValidationError, Regexp)

from settings import SHORT_ID_PATTERN
from .constants import Messages, ORIGINAL_LINK_LENGTH, SHORT_ID_LENGTH
from .models import URLMap


LONG_LINK_MESSAGE = 'Длинная ссылка'
SHORT_LINK_MESSAGE = 'Ваш вариант короткой ссылки'
CREATE_OBJECT_MESSAGE = 'Создать'


class URLForm(FlaskForm):
    original_link = URLField(
        label=LONG_LINK_MESSAGE,
        validators=[
            DataRequired(message=Messages.REQUIRED_FIELD),
            Length(max=ORIGINAL_LINK_LENGTH)
        ])
    custom_id = URLField(
        label=SHORT_LINK_MESSAGE,
        validators=[
            Regexp(
                regex=SHORT_ID_PATTERN,
                message=Messages.INCORRECT_ID_FIELD_VALUE
            ),
            Length(max=SHORT_ID_LENGTH),
            Optional()
        ])
    submit = SubmitField(label=CREATE_OBJECT_MESSAGE)

    def validate_custom_id(form, field):
        if URLMap.get(field.data):
            raise ValidationError(Messages.ID_ALREADY_EXISTS)
