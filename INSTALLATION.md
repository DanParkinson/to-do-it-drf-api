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

---

### Filtering

1. Install Django filters

```python
pip install django-fliters
```

2. Add to installed apps **django_filters** in settings.py

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'django_filters',

]
```

3. Update dependincies file:

```python
pip freeze > requirements.txt
```

---

### Django rest authentication

1. Install Django rest authentication

```python
pip3 install dj-rest-auth==2.1.9
```

2. Add to installed apps **rest_framework.authtoken** and **dj_rest_auth** in settings.py

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rest_framework.authtoken',
'dj_rest_auth',

]
```

3. add to main urls
   '''python
   path('dj-rest-auth/', include('dj-rest-auth.urls')),
   '''

4. migrate the database

```python
python manage.py makemigrations
python manage.py migrate
```

. Update dependincies file:

```python
pip freeze > requirements.txt
```

5. install allauth

'''python
django-allauth==0.54.0
'''

6. in settings.py installed apps, add:

'''python
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'''

7. add underneath installed apps:

'''python
SITE_ID=1
'''

8. add to main urls:

'''python
path(
'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
),
'''

### JWT tokens

1. install:

'''python
pip install djangorestframework-simplejwt==5.2.2
'''

2. in env.py

'''python
os.environ['DEV']='1'
'''

3. in settings .py add

'''python
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [(
'rest_framework.authentication.SessionAuthentication'
if 'DEV' in os.environ
else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
)],
'DATETIME_FORMAT': '%d %b %Y',
}

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
'''

4. Create a serializers.py file in the drf_api folder and add:

'''python
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CurrentUserSerializer(UserDetailsSerializer):
profile_id = serializers.ReadOnlyField(source='profile.id')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id'
        )

'''

5. Underneath your JWT tokens in settings.py add:

'''python
REST_AUTH_SERIALIZERS = {
'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
'''

6. migrate the database

```python
python manage.py makemigrations
python manage.py migrate
```
