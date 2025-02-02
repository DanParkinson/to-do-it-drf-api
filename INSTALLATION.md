# Installation

Here you can follow all of the steps to build your environment to produce this work. 

## Setting up the repo

1. Navigate to the [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template)
2. Click **use this template** and **create a new repository**
3. Clone the Repository

## Backend 

1. Install Django 

    Django 3.2.4 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4

```python
pip3 install django==3.2.4
```

2. Create the django project 

    Remember the dot at the end to make sure it is in the top directory.

```python
django-admin startproject drf_api .
```

3. Create an **env.py** file in the top directory.

    In the env.py file import os

```python
import os 

```

4. In settings.py, underneath **from pathlib import path**

    Add the following:

```python
import os

if os.path.exists('env.py'):
    import env
```

