
class Messages():
    ID_ALREADY_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
    REQUIRED_FIELD = 'Это поле обязательно для заполнения'
    BLANK_REQUEST_BODY = 'Отсутствует тело запроса'
    BLANK_URL_FIELD = '"url" является обязательным полем!'
    INCORRECT_ID_FIELD_VALUE = 'Указано недопустимое имя для короткой ссылки'
    ID_NOT_FOUND = 'Указанный id не найден'


class Statuses():
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_ERROR = 500


ORIGINAL_LINK_LENGTH = 500
SHORT_ID_LENGTH = 16
