# To-Do-It API

## Introduction

The **To-Do-It API** is a backend service built using **Django REST Framework (DRF)**, designed to support a **task management system**. It provides a structured and efficient way for users to **create, organize, and manage tasks**.

This API follows **RESTful principles** and integrates with a frontend built using **React**. It enables users to **authenticate**, categorize tasks, filter tasks by priority or due date, and track progress efficiently.

### Key Features

| Feature                     | Description                                                                     |
| --------------------------- | ------------------------------------------------------------------------------- |
| **User Authentication**     | Secure user registration, login, and token-based authentication.                |
| **Task Management**         | Create, update, delete, and track tasks.                                        |
| **Task Status & Due Dates** | Mark tasks as **pending, in-progress, or completed**, with optional due dates.  |
| **Task Categorization**     | Organize tasks using categories for better management.                          |
| **Filtering & Queries**     | Retrieve tasks based on **status, category, or due date**.                      |
| **RESTful API Design**      | Follows RESTful principles for seamless integration with frontend applications. |

This API serves as the backend for the **To-Do-It** application, allowing users to effectively manage their productivity.

---

## Table of Contents

- [Introduction](#introduction)
- [Project Goals](#project-goals)
- [User Stories](#user-stories)
- [API Documentation](#api-documentation)
  - [Authentication Endpoints](#authentication-endpoints)
  - [Task Endpoints](#task-endpoints)
  - [Category Endpoints](#category-endpoints)
  - [Filters and Queries](#filters-and-queries)
  - [Response Format](#response-format)
- [Database Design](#database-design)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [User Model](#user-model)
  - [Profile Model](#profile-model)
  - [Category Model](#category-model)
  - [Task Model](#task-model)
- [Frameworks, Libraries & Tools](#frameworks-libraries--tools)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup & Configuration](#setup--configuration)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Tests](#automated-tests)
  - [Known Issues & Bug Fixes](#known-issues--bug-fixes)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

---

## Project Goals

The **To-Do-It API** provides a **structured and efficient** backend for managing personal tasks. It is designed to help users organize their workload, set priorities, and track progress effectively.

### **Primary Objectives**

1. **Enable seamless task management** – Allow users to create, update, and delete tasks efficiently.
2. **Improve personal productivity and organization** – Provide categorization, due dates, and priority levels to help users stay on track.
3. **Ensure secure user authentication** – Implement a robust authentication system using JWT for protected API access.
4. **Support task filtering and searching** – Allow users to retrieve tasks based on status, priority, due date, or category.
5. **Follow RESTful API best practices** – Ensure smooth integration with frontend applications.
6. **Scalable architecture** – Use Django and PostgreSQL to support future enhancements.

### **Target Users**

- **Individuals** who want to track and manage their personal tasks.
- **Students & professionals** looking for a structured way to organize their work.
- **Anyone seeking a simple, intuitive personal task management system.**

The API is built for **personal use only**, ensuring that tasks remain private and accessible only to the authenticated user.

---

## User Stories

The **To-Do-It API** is designed to help users efficiently manage their personal tasks. The following user stories outline the core functionalities available in the system.

### **User Authentication & Profile Management**

- **As a user, I want to register an account,** so that I can access my personal task manager.
- **As a user, I want to log in and receive an authentication token,** so that I can securely access my tasks.
- **As a user, I want to log out,** so that my session is properly ended.
- **As a user, I want to retrieve my profile details,** so that I can view my account information.
- **As a user, I want my profile to be automatically created when I sign up,** so that I don’t have to manually create one.

---

### **Task Management**

- **As a user, I want to create a task,** so that I can keep track of things I need to do.
- **As a user, I want to update my task,** so that I can modify details if needed.
- **As a user, I want to delete my task,** so that I can remove completed or irrelevant tasks.
- **As a user, I want to see only my own tasks,** so that my tasks remain private.
- **As a user, I want to set a due date for a task,** so that I know when it needs to be completed.
- **As a user, I want tasks to be automatically archived when completed,** so that my task list stays organized.

---

### **Task Categorization**

- **As a user, I want to create categories,** so that I can group similar tasks together.
- **As a user, I want to update my categories,** so that I can rename or modify them.
- **As a user, I want to delete my categories,** so that I can remove unused ones.
- **As a user, I want to assign tasks to a category,** so that I can organize my tasks better.
- **As a user, I should not be able to assign tasks to another user’s category,** so that my task organization remains private.

---

### **Task Filtering & Searching**

- **As a user, I want to filter tasks by priority,** so that I can focus on high-priority tasks.
- **As a user, I want to filter tasks by status (Pending, In Progress, Completed, Overdue),** so that I can manage progress.
- **As a user, I want to search for tasks by title or description,** so that I can quickly find what I need.
- **As a user, I want to sort tasks by due date,** so that I can see upcoming deadlines first.

---

### **Security & Access Control**

- **As a user, I should only be able to access my own tasks and categories,** so that my data remains private.
- **As a user, I should receive an error when trying to access another user’s tasks or categories,** so that unauthorized access is prevented.

---

## API Documentation

The **To-Do-It API** follows **RESTful API principles** and provides endpoints for **user authentication, task management, category organization, and profile handling**.

All endpoints require **JWT authentication**, except for registration and login.

## **Authentication Endpoints**

The API uses **JWT token authentication**. Users must log in to obtain a token and include it in requests.

| Method | Endpoint                       | Description                 | Auth Required? |
| ------ | ------------------------------ | --------------------------- | -------------- |
| POST   | `/dj-rest-auth/login/`         | Log in & receive token.     | ❌ No          |
| POST   | `/dj-rest-auth/logout/`        | Log out & invalidate token. | ✅ Yes         |
| POST   | `/dj-rest-auth/registration/`  | Register a new user.        | ❌ No          |
| POST   | `/dj-rest-auth/token/refresh/` | Refresh access token.       | ✅ Yes         |

### **Example Login Request**

```json
{
  "username": "john_doe",
  "password": "mypassword"
}
```

## **Profile Endpoints**

Each user has a **Profile** created automatically upon registration. Users can update **only their own profile**.

| Method | Endpoint          | Description                     | Authentication Required? |
| ------ | ----------------- | ------------------------------- | ------------------------ |
| GET    | `/profiles/`      | List all profiles (Admin only). | ✅ Yes                   |
| GET    | `/profiles/{id}/` | Retrieve a specific profile.    | ✅ Yes                   |
| PUT    | `/profiles/{id}/` | Update profile details.         | ✅ Yes                   |

### **Example Profile Request**

```json
{
  "id": 1,
  "owner": "john_doe",
  "name": "John Doe",
  "created_at": "01 Feb 2025"
}
```

## **Task Endpoints**

Users can create, update, delete, and retrieve their own **tasks**.  
Supports **filtering and searching** for easier task management.

### **Available Endpoints**

| Method | Endpoint       | Description                          | Authentication Required? |
| ------ | -------------- | ------------------------------------ | ------------------------ |
| GET    | `/tasks/`      | List all tasks (supports filtering). | ✅ Yes                   |
| POST   | `/tasks/`      | Create a new task.                   | ✅ Yes                   |
| GET    | `/tasks/{id}/` | Retrieve task details.               | ✅ Yes                   |
| PUT    | `/tasks/{id}/` | Update task details.                 | ✅ Yes                   |
| DELETE | `/tasks/{id}/` | Delete a task.                       | ✅ Yes                   |
| GET    | `/archive/`    | List archived (completed) tasks.     | ✅ Yes                   |

### **Example Task Request**

```json
{
  "id": 1,
  "owner": "john_doe",
  "title": "Complete API Documentation",
  "description": "Finalize the API documentation for deployment.",
  "category": {
    "id": 2,
    "name": "Work"
  },
  "status": "In Progress",
  "priority": "High",
  "due_date": "01 Feb 2025",
  "created_at": "01 Feb 2025",
  "updated_at": "01 Feb 2025",
  "is_archived": false
}
```

## **Category Endpoints**

Users can create, update, delete, and retrieve their own **categories**.  
Each user can only access their own categories.

### **Available Endpoints**

| Method | Endpoint            | Description                       | Authentication Required? |
| ------ | ------------------- | --------------------------------- | ------------------------ |
| GET    | `/categories/`      | List all categories for the user. | ✅ Yes                   |
| POST   | `/categories/`      | Create a new category.            | ✅ Yes                   |
| GET    | `/categories/{id}/` | Retrieve details of a category.   | ✅ Yes                   |
| PUT    | `/categories/{id}/` | Update a category name.           | ✅ Yes                   |
| DELETE | `/categories/{id}/` | Delete a category & its tasks.    | ✅ Yes                   |

```json
{
  "id": 1,
  "owner": "john_doe",
  "name": "Work",
  "created_at": "01 Feb 2025"
},
```

## **Database Design**

The **To-Do-It API** uses a relational database model to store user accounts, tasks, and categories.  
Each user manages **their own tasks and categories**, ensuring privacy.

---

### **Database Models Overview**

| Table        | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| `users`      | Stores registered users with authentication details.            |
| `profiles`   | Extends user data with additional profile information.          |
| `tasks`      | Stores user-created tasks with status, priority, and due dates. |
| `categories` | Groups tasks for better organization.                           |

---

### **Relationships**

- **Each user has one profile.** _(1-to-1 relationship)_
- **Each user can have multiple categories.** _(1-to-many)_
- **Each user can have multiple tasks.** _(1-to-many)_
- **Each task can belong to one category.** _(many-to-1)_

---

### **Entity Relationship Diagram (ERD)**

Below is the **ERD** visualizing these relationships:

![Entity Relationship Diagram](readme_assets\ERD\ERD.png)

## **Frameworks, Libraries & Dependencies**

The **To-Do-It API** is built using **Django REST Framework (DRF)** and various third-party libraries to enhance functionality, security, and database management.

### **Core Backend Frameworks**

| Library                         | Version | Description                                    |
| ------------------------------- | ------- | ---------------------------------------------- |
| **Django**                      | 3.2.4   | High-level Python web framework.               |
| **Django REST Framework (DRF)** | 3.12.4  | Toolkit for building RESTful APIs in Django.   |
| **Gunicorn**                    | 23.0.0  | WSGI server for deploying Django applications. |

---

### **Authentication & Security**

| Library                           | Version | Description                                        |
| --------------------------------- | ------- | -------------------------------------------------- |
| **dj-rest-auth**                  | 2.1.9   | Provides authentication endpoints, including JWT.  |
| **django-allauth**                | 0.54.0  | Handles user authentication, registration.         |
| **djangorestframework-simplejwt** | 5.2.2   | Implements JWT-based authentication.               |
| **cryptography**                  | 44.0.0  | Secure cryptographic functions for authentication. |

---

### **Database & ORM**

| Library             | Version | Description                                       |
| ------------------- | ------- | ------------------------------------------------- |
| **dj-database-url** | 0.5.0   | Configures database from an environment variable. |
| **psycopg2**        | 2.9.10  | PostgreSQL database adapter for Python.           |
| **sqlparse**        | 0.5.3   | SQL parsing and formatting utility for Django.    |

---

### **Filtering & Query Optimization**

| Library           | Version | Description                                  |
| ----------------- | ------- | -------------------------------------------- |
| **django-filter** | 2.4.0   | Enables filtering support for Django models. |

---

### **CORS & API Requests Handling**

| Library                 | Version | Description                                     |
| ----------------------- | ------- | ----------------------------------------------- |
| **django-cors-headers** | 3.13.0  | Handles Cross-Origin Resource Sharing (CORS).   |
| **requests**            | 2.32.3  | Allows making HTTP requests.                    |
| **requests-oauthlib**   | 2.0.0   | OAuth authentication support for API requests.  |
| **urllib3**             | 2.3.0   | Advanced HTTP client for handling API requests. |

---

### **Timezones & Date Handling**

| Library    | Version | Description                                       |
| ---------- | ------- | ------------------------------------------------- |
| **pytz**   | 2025.1  | Timezone library for Django.                      |
| **tzdata** | 2024.2  | Timezone support data for working with timezones. |

---

### **Development & Dependency Management**

| Library        | Version  | Description                                 |
| -------------- | -------- | ------------------------------------------- |
| **pipenv**     | 2024.4.0 | Virtual environment and dependency manager. |
| **setuptools** | 75.6.0   | Package management for Python projects.     |
| **virtualenv** | 20.28.0  | Isolated Python environment management.     |

---

## **Installation**

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## Prerequisites

Before running this project, ensure you have the following installed on your system:

### **1. Software Requirements**

- **Python 3.11.6**: Required for running Django and related dependencies.
- **Node.js 16+**: Needed for React and frontend dependencies.
- **PostgreSQL**: Database system for production (optional during development).
- **Git**: For version control and managing the project repository.

### **2. Python Dependencies**

Install the following Python packages (you can also use the provided `requirements.txt` file):

- Django
- Django Rest Framework (DRF)
- Django Allauth
- Gunicorn
- Psycopg2
- Whitenoise

### **3. API Keys and Environment Variables**

You’ll need to configure the following environment variables in a `.env` file:

- `SECRET_KEY`: Django secret key.
- `DEBUG`: Set to `True` during development and `False` in production.
- `DATABASE_URL`: Connection string for the PostgreSQL database (e.g., `postgres://USER:PASSWORD@HOST:PORT/DB_NAME`).

### **4. Development Tools**

Make sure you have the following tools installed:

- **Visual Studio Code**: Recommended IDE for development.
- **Postman**: For testing API endpoints.
- **GitHub Desktop** _(optional)_: For managing Git repositories with a GUI.

### **5. Browser Compatibility**

- The app is optimized for modern browsers, including:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge

---

## Development Workflow

# AGILE

After a few false starts, I reflected on the challenges of previous attempts and restructured my approach to focus on clarity and efficiency. This new plan ensures a more organized workflow and faster progress.

## **Sprint 1: Setting Up the Repo and README**

The first sprint focuses on setting up the repository and documenting the project structure, goals, and design decisions.

### **Tasks**

- [x] Set up the GitHub repository.
- [x] Perform design thinking exercise for features to include in tshe project.
- [x] Mock up the initial database design and document it in the README.
- [x] List and link technologies used in the README.

## **Sprint 2: Initial Backend Setup**

In this sprint, the backend will be set up using Django, focusing on core functionality for user and task management. Key objectives include configuring the project, installing necessary tools, and building the `Profiles`, `Tasks`, `Categories` models. Django Rest Framework (DRF) will be used to create API endpoints, ensuring proper authentication and authorization.

Additional features such as task filtering, search functionality, and user authentication using JWT tokens will be implemented. Unit tests will be written to verify that both the `Profiles`, `Tasks`, `Categories` resources function as expected. Finally, preparations will be made for deployment in Sprint 3, including pagination, root route setup, and improved datetime formatting.

#### ** Project Setup**

- [x] Install Django.
- [x] Create the Django project.
- [x] Add Django Rest Framework (DRF).
- [x] Run the server and append allowed hosts to configuration.

#### ** Profiles App**

- [x] Create the `Profiles` app.
- [x] Create `Profile` model.
- [x] Create `ProfileListView`.
- [x] Create `ProfileSerializer`.
- [x] Create `Profile` URLs.
- [x] Create `IsOwnerOrReadOnly` permission in `drf_api.permissions.py`.
- [x] Create `ProfileDetailView` for update and retrieve.
- [x] Add Django Rest authentication URLs.

#### ** User Authentication**

- [x] User authorization for login/logout, update, and retrieve profiles.

#### ** Tasks App**

- [x] Create the `Tasks` app.
- [x] Create `Task` model.
- [x] Create `TaskListView`.
- [x] Create `TaskSerializer`.
- [x] Create `Task` URLs.
- [x] Create `TaskDetailView` for update, retrieve, and delete.
- [x] Write unittests for task resource.

#### ** Categories App**

- [x] Create the `Categories` app.
- [x] Create `Category` model.
- [x] Create `CategoryListView`.
- [x] Create `CategorySerializer`.
- [x] Create `Category` URLs.
- [x] Create `CategoryDetailView` for update, retrieve, and delete.

#### ** Task Filtering & Functionality**

- [x] Users can filter tasks by `priority`, `status`, or `category`.
- [x] Users can order tasks by priority and due date
- [ ] Tasks whose due date is in the past should automatically change status to `overdue` (Research needed before implementation).
- [x] Tasks text search throguh `title` and `description`

#### ** Testing & Features**

- [ ] Run tests to check that the `Profiles` resource works as expected.
- [x] Run tests to check that the `Tasks` resource works as expected.
- [x] Run tests to check that the `Categories` resource works as expected.
- [x] Run tests to check that filtering and search works as expected.
- [x] Add a search function.

#### ** Authentication & Deployment Preparation**

- [x] Install Django authentication and JWT tokens.
- [x] Prepare for deployment in Sprint 3:
  - Add pagination.
  - Add a `root_route`.

## **Sprint 3 : Deployment**

### Creating a Database with PostgreSQL (Code Institute)

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

### Preparing for Deployment

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

## Testing Workflow

### Automated tests

All automated tests are documented here. All passed.

#### General Task List & Detail Tests

- [x] **Retrieve Task List**: Users can retrieve only their own task list.
- [x] **Retrieve a Specific Task with ownership**: Users can retrieve a task that belongs to them.
- [x] **Retrieve a Specific Task without ownership**: Users cannot retrieve another user's task (`404 Not Found`).

#### Task Creation

- [x] **Successful Task Creation**: Logged-in users can create tasks with valid data.
- [x] **task creation invalid data**: Task creation fails with invalid or missing data (`400 Bad Request`).
- [x] **Task Ownership on creation**: Task is automatically assigned to the logged-in user upon creation.
- [x] **Unauthenticated Task Creation**: Unauthenticated users cannot create tasks (`403 Forbidden`).

#### Task Update

- [x] **update own task valid data**: Task owners can update their own tasks.
- [x] **update own task invalid data**: Updating a task with invalid data should fail (`400 Bad Request`).
- [x] **cannot update owner field**: Task owners cannot update the `owner` field.
- [x] **Unauthorized Task Update**: Users cannot update another user's task (`404 Not Found`).

#### Task Deletion

- [x] **Successful Task Deletion**: Task owners can delete their own tasks.
- [x] **Unauthorized Task Deletion**: Users cannot delete another user's task (`404 Not Found`).
- [x] **Unauthenticated Task Deletion**: Unauthenticated users cannot delete any task (`403 FORBIDDEN`).

## Task Filtering Tests

- [x] **Filter by Priority (Valid Option)**: Users can filter tasks by `"Low"`, `"Medium"`, or `"High"`.
- [x] **Filter by Status (Valid Option)**: Users can filter tasks by `"Pending"`, `"In Progress"`, `"Completed"`, or `"Overdue"`.
- [x] **Filter by Priority & Status Together**: Users can combine priority and status filters in a single request.
- [x] **Filter by Status & Sorting by Due Date**: Users can filter tasks by status and sort by `due_date`.

## Sorting by Due Date

- [x] **Sort Tasks by Earliest Due Date**: Sorting tasks in ascending order of due date (`?ordering=due_date`).
- [x] **Sort Tasks by Latest Due Date**: Sorting tasks in descending order of due date (`?ordering=-due_date`).

## Category Tests

### Category Retrieval

- [x] **Retrieve Category List**: Users can retrieve only their own categories.
- [x] **Retrieve a Specific Category (Owned)**: Users can retrieve a category they created.
- [x] **Retrieve a Specific Category (Not Owned)**: Users cannot retrieve another user's category (`404 Not Found`).

### Category Creation

- [x] **Successful Category Creation**: Users can create a category with valid data.
- [x] **Category Creation Invalid Data**: Category creation fails with invalid data (`400 Bad Request`).
- [x] **Unauthenticated Category Creation**: Unauthenticated users cannot create categories (`403 Forbidden`).

### Category Update

- [x] **Update Own Category**: Users can update their own category.
- [x] **Update Category Invalid Data**: Updating a category with invalid data should fail (`400 Bad Request`).
- [x] **Unauthorized Category Update**: Users cannot update another user’s category (`404 Not Found`).

### Category Deletion

- [x] **Successful Category Deletion**: Users can delete their own categories.
- [x] **Unauthorized Category Deletion**: Users cannot delete another user’s category (`404 Not Found`).
- [x] **Unauthenticated Category Deletion**: Unauthenticated users cannot delete categories (`403 Forbidden`).

### Task-Category Relationship

- [x] **Task Belongs to a Valid Category**: A task must be assigned to an existing category owned by the user.
- [x] **Cannot Assign Task to Another User’s Category**: Users cannot create a task with a category that belongs to another user (`400 Bad Request`).
- [x] **Category Deletion Also Unlinks Tasks**: If a category is deleted, ensure tasks linked to it are handled correctly (e.g., set `null`, or cascade delete).

## Edge Cases

- [x] **Non-existent Task Retrieval**: Retrieving a non-existent task should return `404 Not Found`.
- [x] **Non-existent Task Update/Delete**: Attempting to update or delete a non-existent task should return `404 Not Found`.

## Manual Testing

### **Table of Contents**

#### 1. Profile & User Data

- [1.1 Retrieve Profile Details](#11-retrieve-profile-details)
- [1.2 Retrieve Another User’s Profile (Unauthorized)](#12-retrieve-another-users-profile-unauthorized)

#### 2. Task Management

- [2.1 Create a Task](#21-create-a-task)
- [2.2 Unauthorized Task Creation](#22-unauthorized-task-creation)
- [2.3 Update a Task](#23-update-a-task)
- [2.4 Unauthorized Task Update](#24-unauthorized-task-update)
- [2.5 Delete a Task](#25-delete-a-task)
- [2.6 Unauthorized Task Deletion](#26-unauthorized-task-deletion)

#### 3. Task Filtering & Search

- [3.1 Filter by Priority](#31-filter-by-priority)
- [3.2 Filter by Status](#32-filter-by-status)
- [3.3 Search by Title or Description](#33-search-by-title-or-description)
- [3.4 Sorting by Due Date](#34-sorting-by-due-date)

#### 4. Category Management

- [4.1 Create a Category](#41-create-a-category)
- [4.2 Unauthorized Category Creation](#42-unauthorized-category-creation)
- [4.3 Assign a Task to a Category](#43-assign-a-task-to-a-category)
- [4.4 Restrict Category Access](#44-restrict-category-access)
- [4.5 Delete a Category](#45-delete-a-category)
- [4.6 Unauthorized Category Deletion](#46-unauthorized-category-deletion)

## Manual Testing for Database & Backend Functionality

### 1. Profile & User Data

#### 1.1 Retrieve Profile Details

- **Test Scenario:** A logged-in user can retrieve their profile.
- **Steps to Perform:**
  1. Log in.
  2. Send a `GET` request to `/profiles/{id}/`
- **Expected Outcome:** The user sees their profile details.

![1.1](readme_assets\manual_testing\1.1.png)

#### 1.2 Retrieve Another User’s Profile (Unauthorized)

- **Test Scenario:** A user **cannot** retrieve another user’s profile.
- **Steps to Perform:**
  1. Log in as User A.
  2. Try to access `/profiles/{id}/` of User B.
- **Expected Outcome:** `404 Not Found` response.

![1.2](readme_assets\manual_testing\1.2.png)

---

### 2. Task Management

#### 2.1 Create a Task

- **Test Scenario:** Users should be able to create a task.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/` and send a `POST` request with:
     ```json
     {
       "title": "New Task",
       "description": "Test task",
       "priority": "High",
       "status": "Pending",
       "due_date": "10-02-2024",
       "category": "<valid_category_id>"
     }
     ```
- **Expected Outcome:** The task is created and assigned to the user.

![2.1](readme_assets\manual_testing\2.1.png)

#### 2.2 Unauthorized Task Creation

- **Test Scenario:** A user **cannot** create a task without being logged in.
- **Steps to Perform:**
  1. Logout.
  2. Send a `POST` request to `/tasks/` with valid task data.
- **Expected Outcome:** `403 Forbidden` response.

![2.2](readme_assets\manual_testing\2.2.png)

#### 2.3 Update a Task

- **Test Scenario:** Users should be able to update their own tasks.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/{task_id}/` and send a `PUT` request.
  3. Modify title, description, or other fields.
- **Expected Outcome:** Task updates successfully.

![2.3](readme_assets\manual_testing\2.3.png)

#### 2.4 Unauthorized Task Update

- **Test Scenario:** Users **cannot** update another user's task.
- **Steps to Perform:**
  1. Log in as User A.
  2. Attempt to update User B’s task via `/tasks/{task_id}/`.
- **Expected Outcome:** `404 Not Found` response.

- Update attempt

![2.4.1](readme_assets\manual_testing\2.4.1.png)

- Task not updated

![2.4.2](readme_assets\manual_testing\2.4.2.png)

#### 2.5 Delete a Task

- **Test Scenario:** Users should be able to delete their own tasks.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/{task_id}/` and send a `DELETE` request.
- **Expected Outcome:** Task is deleted.

  ![2.5](readme_assets\manual_testing\2.5.png)

#### 2.6 Unauthorized Task Deletion

- **Test Scenario:** Users **cannot** delete another user's task.
- **Steps to Perform:**
  1. Log in as User A.
  2. Attempt to delete User B’s task via `/tasks/{task_id}/`.
- **Expected Outcome:** `404 Not Found` response.

- Delete attempt

![2.6.1](readme_assets\manual_testing\2.6.1.png)

- Task not Deleted

![2.6.2](readme_assets\manual_testing\2.6.2.png)

---

### 3. Task Filtering & Search

#### 3.1 Filter by Priority

- **Test Scenario:** Users can filter tasks by `"Low"`, `"Medium"`, or `"High"`.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?priority=Medium`.
- **Expected Outcome:** Only Medium-priority tasks are returned.

![3.1](readme_assets\manual_testing\3.1.png)

#### 3.2 Filter by Status

- **Test Scenario:** Users can filter tasks by `"Pending"`, `"Completed"`, etc.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?status=In-Progress`.
- **Expected Outcome:** Only In Progress tasks are returned.

![3.2](readme_assets\manual_testing\3.2.png)

#### 3.3 Search by Title or Description

- **Test Scenario:** Users can search for tasks by keywords.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?search=New`.
- **Expected Outcome:** Tasks containing "new" in title or description are returned.

![3.3](readme_assets\manual_testing\3.3.png)

#### 3.4 Sorting by Due Date

- **Test Scenario:** Users can sort tasks by due date.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?ordering=due_date`.
- **Expected Outcome:** Tasks appear in ascending order of due date.

![3.4](readme_assets\manual_testing\3.4.png)

### 4. Category Management

#### 4.1 Create a Category

- **Test Scenario:** Users should be able to create a category.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/categories/` and send a `POST` request with:
     ```json
     {
       "name": "New Category"
     }
     ```
- **Expected Outcome:** The category is created.

![4.1](readme_assets\manual_testing\4.1.png)

#### 4.2 Unauthorized Category Creation

- **Test Scenario:** A user **cannot** create a category without being logged in.
- **Steps to Perform:**
  1. Logout.
  2. Send a `POST` request to `/categories/` with valid category data.
- **Expected Outcome:** `403 Forbidden` response.

![4.2](readme_assets\manual_testing\4.2.png)

#### 4.3 Assign a Task to a Category

- **Test Scenario:** Users can assign a task to one of their own categories.
- **Steps to Perform:**
  1. Log in.
  2. Create a task and assign it to an existing category.
- **Expected Outcome:** Task is linked to the correct category.

![4.3](readme_assets\manual_testing\4.3.png)

#### 4.4 Restrict Category Access

- **Test Scenario:** Users **cannot** access another user's category.
- **Steps to Perform:**
  1. Log in as User A.
  2. Try to access `/categories/{category_id}/` of User B.
- **Expected Outcome:** `404 Not Found` response.

![4.4](readme_assets\manual_testing\4.4.png)

#### 4.5 Delete a Category

- **Test Scenario:** Users should be able to delete their own categories.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/categories/{category_id}/` and send a `DELETE` request.
- **Expected Outcome:** The category is deleted.

- Delete attempt

![4.5.1](readme_assets\manual_testing\4.5.1.png)

- Task not Deleted

![4.5.2](readme_assets\manual_testing\4.5.2.png)

#### 4.6 Unauthorized Category Deletion

- **Test Scenario:** Users **cannot** delete another user's category.
- **Steps to Perform:**
  1. Log in as User A.
  2. Attempt to delete User B’s category via `/categories/{category_id}/`.
- **Expected Outcome:** `404 Not Found` response.

![4.6](readme_assets\manual_testing\4.6.png)

## Validation

# Python Validation

Code errors and style issues were detected using the Pylance linter in VSCode and immediately fixed throughout development. All files containing custom Python code were then validated using the Code Institute Python Linter:

## Categories App

- `categories/admin.py`: no errors found
- `categories/models.py`: no errors found
- `categories/serializers.py`: no errors found
- `categories/urls.py`: no errors found
- `categories/views.py`: no errors found
- `categories/tests.py`: no errors found

## Tasks App

- `tasks/admin.py`: no errors found
- `tasks/models.py`: no errors found
- `tasks/serializers.py`: no errors found
- `tasks/urls.py`: no errors found
- `tasks/views.py`: no errors found
- `tasks/filters.py`: no errors found
- `tasks/tests.py`: no errors found

## Profiles App

- `profiles/admin.py`: no errors found
- `profiles/serializers.py`: no errors found
- `profiles/urls.py`: no errors found
- `profiles/views.py`: no errors found
- `profiles/permissions.py`: no errors found
- `profiles/utils.py`: no errors found

## Known Issues

## Future Enhancements

## **Future Enhancements**

The **To-Do-It API** is designed to be scalable and extendable. Below are some planned future improvements:

### **1. Task Collaboration (Multi-User Support)**

- Allow users to **assign tasks to others** (e.g., family members, team members).
- Implement **shared task lists** for better team management.
- Introduce **task commenting** for discussions.

### **2. Task Reminders & Notifications**

- Add **email or push notifications** for task due dates.
- Implement **automated daily/weekly task summaries**.
- Allow users to set **recurring reminders**.

### **3. Advanced Filtering & Sorting**

- Add **custom filtering options** (e.g., filter by task importance).
- Implement **date-range filtering** for better task scheduling.
- Improve **sorting logic** (e.g., sort by progress level).

### **4. Enhanced Authentication & Security**

- Implement **two-factor authentication (2FA)** for added security.
- Add **OAuth support** (Google, GitHub, Facebook login).
- Improve **password recovery/reset options**.

### **5. User Dashboard & Insights**

- Provide users with **task completion statistics**.
- Display **task trends over time** (e.g., most productive days).
- Introduce **productivity scoring** based on completed tasks.

### **6. Mobile API Support**

- Optimize API responses for **mobile-friendly integration**.
- Develop **a dedicated mobile app** using React Native or Flutter.
- Implement **offline task management** with automatic sync.

### **7. AI-Powered Task Suggestions**

- Use **AI to suggest task priorities** based on deadlines.
- Implement **smart categorization** based on task descriptions.
- Introduce **AI-generated productivity tips**.

### **8. Integration with Third-Party Apps**

- Sync tasks with **Google Calendar & Outlook**.
- Allow **Slack or Discord notifications** for task updates.
- Provide **Zapier integration** for workflow automation.

## **Conclusion**

These enhancements will **improve user experience, productivity, and security**, making **To-Do-It** a **powerful** and **versatile** task management tool.

## **Credits**

The **To-Do-It API** was built using **Django REST Framework** and several third-party libraries to provide a scalable and efficient task management system. The following resources and contributors helped shape this project:

---

### **1. Frameworks & Libraries**

- **[Django](https://www.djangoproject.com/)** – High-level Python web framework.
- **[Django REST Framework](https://www.django-rest-framework.org/)** – API toolkit for building RESTful services.
- **[dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)** – Authentication system for Django.
- **[django-filter](https://django-filter.readthedocs.io/en/stable/)** – Filtering support for DRF.
- **[PostgreSQL](https://www.postgresql.org/)** – Open-source relational database.
- **[Gunicorn](https://gunicorn.org/)** – WSGI server for deploying Django applications.
- **[Heroku](https://www.heroku.com/)** – Cloud platform for deploying web applications.

---

### **2. Learning & Documentation Resources**

- **[Django Official Docs](https://docs.djangoproject.com/en/stable/)** – Official Django documentation.
- **[Django REST Framework Docs](https://www.django-rest-framework.org/)** – Official API documentation.
- **[Stack Overflow](https://stackoverflow.com/)** – Help with debugging and optimizing API calls.
- **[Code Institute](https://codeinstitute.net/)** – Learning materials and best practices for Django projects.

---

### **3. Tutorials & Articles**

- **[Real Python](https://realpython.com/)** – In-depth Django REST tutorials.
- **[TestDriven.io](https://testdriven.io/)** – API testing and best practices.
- **[Mozilla Developer Network (MDN)](https://developer.mozilla.org/)** – General web development references.
- **[Help with Django Signals](https://stackoverflow.com/questions/68029704/about-sender-instance-created-kwargs-parameter-how-its-assigned)** - understanding how to create a category on user creation
- **[Help with custom filtering logic](https://www.youtube.com/watch?v=3Gi-w4Swge8)** - for combining filtering and sorting logic
- **[Help with custom filtering logic](https://tech.serhatteker.com/post/2022-03/django-rest-filtering-tutorial-part-1/)** - A series on custom filtering logic in django

---

### **4. Special Thanks**

A huge thanks to **everyone who contributed** to this project, directly or indirectly.  
This includes **mentors, developers, and the open-source community** for their valuable insights and knowledge.

---

## **Contributions**

If you would like to **contribute** to the project, feel free to:

1. **Fork the repository** on GitHub.
2. **Submit a pull request** with proposed changes.
3. **Report issues or suggest enhancements** via GitHub Issues.

Your feedback and contributions help make **To-Do-It** even better! 🚀

---
