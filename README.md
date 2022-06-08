# Yatube-API

## Описание

RESTful веб-сервис социальной сети Yatube с аутентификацией и авторизацией, персональными лентами, комментариями и подпиской на авторов.

## Как запустить проект в Dev режиме:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gen121/Yatube-API.git
```

```
cd Yatube-API
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

В целях безопасности SECRET_KEY проекта размещен в окружении,
для работы с которым используется библиотека python-dotenv.
Для этого в проекте в директории /Yatube-API/yatube_api необходимо 
создать файл .env с ключом:

```
SECRET_KEY=you_shall_not_pass_for_example
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
