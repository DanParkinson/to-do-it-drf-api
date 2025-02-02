# Installation

Here you can follow all of the steps to build your environment to produce this work. 

## Setting up the repo

1. Navigate to the [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template).
2. Click **use this template** and **create a new repository**.
3. Clone the Repository.

---

## Backend

1. Install Django.

    Django 3.2.4 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4.

```python
pip3 install django==3.2.4
```

2. Create the django project.

    Remember the dot at the end to make sure it is in the top directory.

```python
django-admin startproject drf_api .
```

3. Create an **env.py** file in the top directory.

    In the env.py file import os.

```python
import os 

```

4. In settings.py, underneath **from pathlib import path**.

    Add the following:

```python
import os

if os.path.exists('env.py'):
    import env
```

5. Runserver and append url to allowed hosts.

```python
python manage.py runserver
```

---

### Creating Profiles app

1. Create your app and add to settings.py in installed apps:

```python
python manage.py startapp profiles
```

2. Create your Profile model, set up Django Signals, and add your profile import to admin.py.

3. Migrate the database with:

```python
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser to access the admin panel and everything is set up correctly.

```python
python manage.py createsuperuser
```

5. Run the server:

    In the browser URL append /admin/ to access the admin panel.

    Login with your superuser credentials.

```python 
python3 manage.py runserver
```

6. Create dependincies file:

```python
pip freeze > requirements.txt
```

7. add, commit, and push your code to the main branch

---

### Django Rest Framework

1. Install Django Rest Framework.

```python
pip install djangorestframework==3.12.4
```

2. Add to installed apps **rest_framework** in settings.py

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rest_framework',

'profiles',
]
```

3. Update dependincies file:

```python
pip freeze > requirements.txt
```
