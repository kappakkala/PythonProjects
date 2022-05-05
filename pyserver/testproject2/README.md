# Django postgres integration

Inside project directory, create a new django project

`django-admin startproject testproject2`

cd to projectdirectory

`pip install django psycopg2`

Change `DATABASES['default']` inside `settings.py` to include postgres settings.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
Create a postgres database and a user for that database.

Make and apply migrations

`python manage.py makemigrations`

`python manage.py migrations`

Create a superuser. The user info can be seen inside the table `auth_user`

`python manage.py createsuperuser`

Add `'django.contrib.postgres'` to `INSTALLED_APPS` in settings.py.

Create an app and add it to `settings.py`.

`python manage.py startapp pgapp`

Edit `models.py`

```python
class Rooms(models.Model):
    buildings = models.CharField(max_length=10)
    rooms = models.CharField(max_length=10)
```

Edit `admin.py`

```python
from .models import Rooms
admin.site.register(Rooms)
```

Make and apply migrations. Add data to rooms by logging into `127.0.0.1:8000/admin`. Check table contents using pgadmin4.

Add a template for endpoint `/home`. Edit `views.py` from appfolder and `urls.py` from project folder.

Add templates path to `settings.py`.

Create a new `forms.py` inside app folder. Configure `models.py` , `urls.py` to update url endpoints.

Set up `/home` to display data from postgres table

Set up `/base1` to display a dropdown menu and form field.

Set up `/base2` 

Preview of 127.0.0.1:8000/base2

![alt text](./images/get_base2.png?raw=true "127.0.0.1:8000/base2")

Query selection based on field of type string

![Query selection1 127.0.0.1:8000/base2](./images/post_building_base2.png?raw=true "127.0.0.1:8000/base2")

Query selection based on field of type date

![Query selection2 127.0.0.1:8000/base2](./images/post_date_base2.png?raw=true "127.0.0.1:8000/base2")

Set up `/base3`

Set up `/contact` 
