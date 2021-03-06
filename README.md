# API_YATUBE
## Добро пожаловать на страницу API_YATUBE
Это API для социальной сети.
Оно имеет базовые функции социальной сети:
  1. Пользователи могут создавать посты
  2. Пользователи могут создавать сообщества
  3. Пользователи могут подписываться/отписываться друг на друга
  4. Пользователи могут читать избранных авторов

Для установки API на сервер или на свой компьютер, клонируйте этот репозиторий и выполните:
### 1. Установку виртуального окружения:
Выполните команду в терминале
```
python3 -m venv venv
```
### 2. Активируйте вируальное окружение:
Выполните команду в терминале
```
source venv/bin/activate
```
### 3. Установите зависимости:
Выполните команду в терминале
```
pip install -r requirements.txt
```
### 4. После установки всех зависимостей, необходимо создать миграции:
```
python manage.py makemigrations
```
### 5. Далее произвести саму миграцию:
```
python manage.py migrate
```
### 6. Создадим суперпользователя командой:
```
python manage.py createsuperuser
```
### 7. Для запуска севера, выполните:
```
python manage.py runserver
```
После удачного запуска сервера в терминале вы увидите выод примерно такого содержания:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 06, 2021 - 11:27:01
Django version 3.1.7, using settings 'yatube_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Переходим по ссылке http://127.0.0.1:8000/redoc/ где находим документацию по методам API

# Аутентификация по JWT-токену

Для того, чтобы успешно производить запросы к API нужно получить токен авторизованного пользователя и передавать его в запросе.
Для авторизации и получения токена пройдите по сслыке http://127.0.0.1:8000/api/v1/token/
Отправьте POST запрос с заполнеными полями: *username* и *password*. При успешной авторизации пользователя в ответ получите JSON такого вида:
``` json
{
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4NzEyODUzNSwianRpIjoiNzRmMDhkOGEwODQ4NGEzYjgyZmM4MDRhMTQ3ZTEyZmIiLCJ1c2VyX2lkIjoxfQ.GW7Obcvy2TWgsEI5lqSx9BC1mxk0WnsywBHrXScs7bI",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3MDQyNDM1LCJqdGkiOiI5ZmNjMWE5YTM5NDQ0Y2Q4OWJlOGFlOGRlYWQxNDE0ZSIsInVzZXJfaWQiOjF9.ZkEdzDN5pNgYToDRJq1CKHjIglK1ir1fhnfcXkmziuk"
}
```

Приятной работы с API!
