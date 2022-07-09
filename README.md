# api_final
API для сервиса агрегатора отзывов о фильмах.
## Установка
1. Клонируем репозиторий и переходим в него:
```
git clone ********

cd api_final_yatube
```
2. Создаем виртуальное окружение и активируем его:
```
python3 -m venv env

source env/bin/activate
```
3.Устанавливаем зависимости:
```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4.Выполняем миграции:
```
python3 manage.py migrate
```
5.Запускаем проект:
```
python3 manage.py runserver
```
## Завершаем настройку
Создаём пользователя и получаем токен на эндпоинте:
```
/auth/jwt/create/
```
## Чтобы просмотреть список эндпоинтов переходим по адресу
```
http://127.0.0.1:8000/redoc
```
