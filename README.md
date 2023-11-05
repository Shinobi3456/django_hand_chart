![django1.jpg](static/django1.png)
# Как сделать свою страницу в Django Admin с выразительной Hand Chart?

Этот репозиторий содержит примеры кода для статьи.

## Содержание

* [Установка](#установка)
* [Настройка](#настройка)
* [Лицензия](#лицензия)


## Установка
Для запуска примеров вам понадобится установить:

* [Python 3.x](#установка-python-3x)
* [Установка зависимостей проекта](#установка-зависимостей-проекта)


### Установка Python 3.x
Скачайте и установите Python 3.x с официального сайта https://www.python.org/downloads/


### Установка зависимостей проекта

Выполните следующую команду в командной строке:

Для Mac/Linux
````bash
pip install -r requirements.txt
````

Для Windows
````bash
python3 -m  pip install -r requirements.txt
````


## Настройка

1. Скачайте репозиторий
2. В файле DjangoHandChart/settings.py в переменной DATABASES - укажите ваши данные для доступа к БД
3. Применить миграции к БД (перед первым запуском)
```
$ python manage.py migrate
```

4. Создать супер пользователя:

```
$ python manage.py createsuperuser
```

5. Запускаем проект
```
$ python manage.py runserver
```

## Лицензия

Этот код распространяется под лицензией MIT. См. LICENSE для получения подробной информации.
