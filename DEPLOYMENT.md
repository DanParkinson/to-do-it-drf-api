# Deployment Process

## Creating a Database with PostgreSQL (Code Institute)

To set up the external database for your project, follow these steps:

1. **Access Code Institute's PostgreSQL Service**:

   - Use your student email to log in to Code Institute's PostgreSQL service.

2. **Create a New Database**:

   - Once logged in, you will receive an email containing your database URL and credentials.
   - Note down these details as they will be needed later in your project.

3. **Configure the Database in Heroku**:

   - Log in to your Heroku account at [Heroku](https://www.heroku.com/).
   - Create a new Heroku app:
   - Click on **New** and select **Create App**.
   - Provide a name for your app and click **Create App**.

4. **Add Config Vars in Heroku**:

   - Navigate to the **Settings** tab of your Heroku app.
   - In the **Config Vars** section, add a new variable:
   - Key: `DATABASE_URL`
   - Value: `<Your PostgreSQL database URL>`

5. **Install PostgreSQL Dependencies**:

   Open your terminal and install the necessary packages:

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

6. **Update `settings.py` for Database Configuration**:

   Import the required packages in `settings.py`:

   ```python
   import dj_database_url
   import os
   ```

   Update the `DATABASES` setting to handle both development and production environments:

   ```python
   if 'DEV' in os.environ:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   else:
   DATABASES = {
       'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
   }
   ```

7. **Add the Database URL to `env.py` (for local development)**:

   In your `env.py` file, add the following:

   Ensure the URL is added as a string with quotes.

   ```python
   os.environ['DATABASE_URL'] = "<Your PostgreSQL database URL>"
   ```

8. **Test the Connection**:
   Temporarily add a `print('connected')` statement under the `DATABASES` configuration in `settings.py` to verify the connection:

   If connected successfully, a message will appear, and migrations will not be applied.

   ```python
   print('connected')
   ```

   Run the following command to test the connection:

   ```bash
   python3 manage.py makemigrations --dry-run
   ```

9. **Remove the Debugging Print Statement**:

   Once confirmed, remove the `print('connected')` line from `settings.py`.

10. **Apply Migrations**:

    Migrate your database models to the new PostgreSQL database:

    ```bash
    python3 manage.py migrate
    ```

11. **Create a Superuser**:

    Create a superuser for accessing the admin panel of your new database:

    ```bash
    python3 manage.py createsuperuser
    ```

12. **Verify the Database Setup**:

    Log in to the Django admin panel and ensure the database is properly configured.

---

## Preparing for Deployment

1. **Install Gunicorn and Other Dependencies**:

   Install Gunicorn for serving your application and other required packages:

   ```bash
   pip3 install gunicorn django-cors-headers==3.13.0
   ```

   Update your `requirements.txt` file:

   ```bash
   pip freeze --local > requirements.txt
   ```

2. **Create a Procfile**:

   Create a file named `Procfile` (no file extension) in the root of your project.

   Add the following lines to the `Procfile`:

   ```plaintext
   release: python manage.py makemigrations && python manage.py migrate
   web: gunicorn drf_api.wsgi
   ```

3. **Update `ALLOWED_HOSTS` and Middleware**:

   In your `settings.py`, update `ALLOWED_HOSTS` to include your Heroku app’s URL:

   ```python
   ALLOWED_HOSTS = [
     'project-5-to-do-app.herokuapp.com',
     'localhost',
   ]
   ```

   Add `corsheaders` to your `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
     ...
     'corsheaders',
     ...
   ]
   ```

   Add `CorsMiddleware` to the top of your `MIDDLEWARE` list:

   ```python
   MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
   ]
   ```

4. **Configure CORS**:

   Add the following to your `settings.py`:

   ```python
   CORS_ALLOW_CREDENTIALS = True

   if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
   else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https:\/\/.*\.codeinstitute-ide\.net$",
     ]
   ```

5. **JWT Authentication and Security Updates**:

   To enable cross-platform deployment and prevent cookie blocking, add the following to `settings.py`:

   ```python
   JWT_AUTH_COOKIE = 'my-app-auth'
   JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
   JWT_AUTH_SAMESITE = 'None'
   ```

   Replace the `SECRET_KEY` value in `settings.py` with the following:

   ```python
   SECRET_KEY = os.getenv('SECRET_KEY')
   ```

   Update `env.py` with a new `SECRET_KEY`:

   ```python
   os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")
   ```

   Ensure the `DEBUG` value is dynamically set based on the environment:

   ```python
   DEBUG = 'DEV' in os.environ
   ```

6. **Set Environment Variables in Heroku**:

- Go to the **Settings** tab in your Heroku app and add the following `Config Vars`:
- `SECRET_KEY`: Your project’s secret key.
- `CLOUDINARY_URL`: Your Cloudinary URL.

7. **Deploy to Heroku**:

- Push your changes to GitHub.
- Link your Heroku app to your GitHub repository.
- Deploy your branch manually or enable automatic deploys.

8. **Final Configuration for Cross-Origin and Development**:

   Add the `CLIENT_ORIGIN_DEV` variable for Gitpod’s dynamic URLs:

   ```python
   if 'CLIENT_ORIGIN_DEV' in os.environ:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https:\/\/.*\.codeinstitute-ide\.net$",
     ]
   ```

9. **Verify the Deployment**:

- Open your Heroku app and ensure everything is working as expected.

10. **Handle Debugging**:

    If you encounter issues, use the following command to check logs:

    ```bash
    heroku logs --tail --app project-5-to-do-app
    ```

---
