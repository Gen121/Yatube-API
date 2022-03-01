# Yatube_api

## Описание

RESTful веб-сервис социальной сети Yatube с аутентификацией и авторизацией, персональными лентами, комментариями и подпиской на авторов.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация

После запуска сервера доступна в браузере по ссылке 

```
http://127.0.0.1:8000/redoc/
```
