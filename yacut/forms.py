from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        label='Длинная ссылка',
        validators=[DataRequired(message='Это поле обязательно для заполнения')]
    )
    custom_id = URLField(
        label='Ваш вариант короткой ссылки',
        validators=[Length(1, 16, message='Длина короткой ссылки не должна превышать 16 символов'), Optional()]
    )
    submit = SubmitField()
