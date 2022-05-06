# Booking System based on Django and Postgres

## Steps involved

### 0. Initial Setup

Create and activate a python virtual environment inside the project directory.

Copy requirements.txt into project directory and install the required packages using

`pip install -r requirements.txt --upgrade`

Inside project directory, create a new django project

`django-admin startproject booking_system`

Make changes to **settings.py** to include the setup the postgres database.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookingdb',
        'USER': 'testuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

Additionally, remove the line `SECRET_KEY = '<your secret key>'` and paste it to **__init__.py**. Add the following imports to **settings.py**.

```python
from booking_system import SECRET_KEY
import os
```

Append `'django.contrib.postgres'` to **INSTALLED_APPS**.

Insert `os.path.join(BASE_DIR,"templates")` inside the list `TEMPLATES['DIR']`. Also create a new folder **templates** inside the project directory.

Make and apply migrations before running the server.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

If a superuser is not available, create one using

`python manage.py createsuperuser`

### 1. Base1 version

In this version, we create a simple room booking system. We create two similar postgres tables that stores available rooms and booked rooms. The user is able to search available rooms in a building on a day. The user can use this information to book/cancel an available/already booked room. When a room is booked, it is no longer available. It becomes available again, if the booking is cancelled. See images/base1*.png.

Create an app **roomsapp** and append the app name to `INSTALLED_APPS` in **settings.py**.

`python manage.py startapp roomsapp`

Edit **models.py**, **admin.py**, **urls.py**, **views.py**. Copy html templates to **templates** directory.

Make and apply migrations before running the server. Login to admin user and insert data to Tables **Available**. 

`127.0.0.1:8000/search` returns the rooms based on date and building name.

`127.0.0.1:8000/booking` books a room for a day.

`127.0.0.1:8000/cancel` cancels a room on a day.
