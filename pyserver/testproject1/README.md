Inside project directory, create a new django project

`django-admin startproject testproject1`

cd to django project testproject1. To run the server

`python3 manage.py runserver`

The server is accessible in the browser under the url `127.0.0.1:8000`

TO apply settings

`python manage.py migrate`

To create a superuser with admin privileges

`python manage.py createsuperuser`

Run and login to the server `127.0.0.1:8000/admin`

# 1. Test Application

Go to django project root and create a new application. To generate a default folder structure for a Django app.

`python manage.py startapp testapp1`

Edit models.py inside app folder. Add a test class
```python
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
```
Now add the app name under `INSTALLED_APPS` in django projects settings.py

Make migrations and apply those migrations

`python manage.py makemigrations`

`python manage.py migrate`

Run the above two codes in conjunction everytime we make changes to models.py

Add the class in `admin.py` inside appfolder and resister it

`from .models import Product`

`admin.site.register(Product)`

To add data manually, login the admin server and add data under Product in testapp1. To add the data using script, run

```python
from testapp1.models import Product
# lists all products
Product.object.sall()
Product.objects.create(title='new title', description='new description', summary='new summary')
```

To start over the app, delete all data from migrations excluding `__init__.py` and make changes to the apps `models.py`. Also delete the default sqlite3 database. Make and apply migrations. Create the superuser again, since we have deleted all the data from the database.

# 2. Application Pages 

`python manage.py startapp pages`

Insert app name inside `settings.py`.

Edit `views.py` inside app folder to define functions for various urls/pages.

```python
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Welcome to Django Server!</h1>")
```

Edit `urls.py` inside project root directory.

```python
from django.urls import path
from pages import views
```
Append `path('', views.home_view, name='home'))`

To view a page based on a template, create a templates folder in the project root directory. Create a home.html file inside the folder.
Add template folder location inside the list `TEMPLATE['DIRS']` in `settings.py`. The home url now uses the template home.html. Run `127.0.0.1:8000\home`.

To render some data to the server, create a new html template `about.html` that displays two context varibles. See  `about.html`.
We define our view as
```python
def about_view(request, *args, **kwargs):
    my_context = {"name" : "jason", "id" : 72}
    return render(request, "about.html", my_context)
```

Add the view to the path and run the server `127.0.0.1:8000\about`