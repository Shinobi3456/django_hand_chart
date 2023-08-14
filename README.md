

# Как сделать свою страницу в Django Admin c покером и куртизанками?

Этот репозиторий содержит примеры кода для статьи.

## Содержание

* [Установка](#установка)
* [Настройка](#настройка)
* [Запуск тестов](#запуск-тестов)
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


## Getting Started

- [ ] [Python =>3.9](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)

- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/Shinobi3456/testFunBox.git
```

2. Check into the cloned repository
```
$ cd testFunBox
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Configure Redis configuration in `TestFunBox/settings.py`

5. Start the Django API
```
$ python manage.py runserver
```

6. Run tests
```
$ python manage.py test
```

7. Send requests to post `http://localhost:8000/api/visited_links`

Request data:
```json
{
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "https://funbox.ru",
        "https://stackoverflowdsfsdfds.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}
```

Response Success

```json
{
    "status": "ok"
}
```

Response Error

```json
{
    "status": "error"
}
```
error - this is the error text