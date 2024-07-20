## Запуск
## Создать в корневой папке папку с именем base
##Создать вирутальное окружение и утсановить Django и CorsHeadders
```
python -m venv venv
venv/Scripts/activate
python -m pip install django
python -m pip install django-cors-headers
```
Выполнить миграции
```
python manage.py makemigraions
python manage.py migrate
```
Переходиим в корневую папку, где содержится manage.py
```
python manage.py runserver
```
