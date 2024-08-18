# Проект асинхронного парсинга информации о PEP
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
Ключевые возможности сервиса:

* генерация коротких ссылок и их связь с исходными длинными ссылками;
* переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:

* обязательного для длинной исходной ссылки;
* необязательного для пользовательского варианта короткой ссылки.

## Стэк используемых технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.1.x/)
[![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)](https://jinja.palletsprojects.com/en/3.1.x/)
[WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
[SQLAlchemy](https://www.sqlalchemy.org/)

## Разворачивание проекта
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RedCloverfield/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Обновить пакетный менеджер pip и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Файл .env
Пример файла .env c переменными окружения, необходимыми для запуска проекта.
Файл необходимо создать в корневой папке проека.
    
```
FLASK_APP=yacut
FLASK_DEBUG=1 (0 - для отключения режима разработчика)
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR-SECRET-PROJECT_KEY
```

## Запуск проекта
Запуск проекта осуществляется следующей командой

```
flask run
```

## Автор проекта
[Ефимов Станислав](https://github.com/RedCloverfield)