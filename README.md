# To-Do-It

## INTRODUCTION

The **To-Do-It API** is a backend service built with **Django REST Framework (DRF)** that powers a task management system. This API allows users to create, update, delete, and organize tasks efficiently. With built-in authentication, categorization, and filtering, it provides a robust solution for personal task management.

### Key Features

| Feature                     | Description                                                                     |
| --------------------------- | ------------------------------------------------------------------------------- |
| **User Authentication**     | Secure user registration, login, and token-based authentication.                |
| **Task Management**         | Create, update, delete, and track tasks.                                        |
| **Task Status & Due Dates** | Mark tasks as pending, in-progress, or completed, with optional due dates.      |
| **Task Categorization**     | Organize tasks using categories for better management.                          |
| **Filtering & Queries**     | Retrieve tasks based on status, category, or due date.                          |
| **RESTful API Design**      | Follows RESTful principles for seamless integration with frontend applications. |

This API serves as the backend for the **To-Do-It** application, which will be used alongside a frontend built with **React and Bootstrap**.

For further details, refer to the **API Documentation** and **Installation Workflow** sections.

## Table of Contents

- [Introduction](#introduction)
- [User Stories](#user-stories)
- [API Documentation](#api-documentation)
  - [Authentication Endpoints](#authentication-endpoints)
  - [Task Endpoints](#tasks-endpoints)
  - [Category Endpoints](#categories-endpoints)
  - [Filters and Queries](#filters-and-queries)
  - [Response Format](#response-format)
- [Database Design](#database-design)
  - [Model Usage](#model-usage)
  - [User Model](#user-model)
  - [Profile Model](#profile-model)
  - [Category Model](#category-model)
  - [Task Model](#task-model)
  - [Relationships](#relationships)
- [Frameworks, Libraries & Tools Used](#frameworks-libraries--tools-used)
  - [Backend Frameworks](#backend-frameworks)
  - [Authentication & Security](#authentication--security)
  - [Database & Storage](#database--storage)
  - [Task Management & Filtering](#task-management--filtering)
  - [Middleware & Server](#middleware--server)
  - [Other Dependencies](#other-dependencies)
- [Prerequisites](#prerequisites)
  - [Software Requirements](#1-software-requirements)
  - [Python Dependencies](#2-python-dependencies)
  - [API Keys and Environment Variables](#3-api-keys-and-environment-variables)
  - [Development Tools](#4-development-tools)
  - [Browser Compatibility](#5-browser-compatibility)
- [Installation Workflow](installation.md)
- [Development Workflow](#development-workflow)
- [Testing Workflow](testing.md)
- [Deployment](deployment.md)
- [Known Issues](#known-issues)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)

--

## User Stories

Full user story documentation will be found on the frontend repository. A list of user story functionality relating to the backend are present here:

### User Authentication & Profile Management

- **As a user, I want to register an account,** so that I can use the task management system.
- **As a user, I want to log in and receive an authentication token,** so that I can securely access my tasks.
- **As a user, I want to log out,** so that my session is properly ended.
- **As a user, I want to retrieve my profile details,** so that I can view my account information.
- **As a user, I want my profile to be automatically created when I sign up,** so that I don’t have to manually create one.

---

### Task Management

- **As a user, I want to create a task,** so that I can keep track of things I need to do.
- **As a user, I want to update my task,** so that I can modify details if needed.
- **As a user, I want to delete my task,** so that I can remove completed or irrelevant tasks.
- **As a user, I want to see only my own tasks,,** so that my tasks remain private.
- **As a user, I want to assign a task to a category,** so that I can organize my tasks better.
- **As a user, I want to set a due date for a task,** so that I know when it needs to be completed.
- **As a user, I want tasks sorted by due date,** so that I can see which tasks need urgent attention.

---

### Task Filtering & Search

- **As a user, I want to filter tasks by priority,** so that I can focus on high-priority tasks.
- **As a user, I want to filter tasks by status (Pending, In Progress, Completed, Overdue),** so that I can manage progress.
- **As a user, I want to search for tasks by title or description,** so that I can quickly find what I need.
- **As a user, I want to sort tasks by due date,** so that I can see upcoming deadlines first.

---

### Category Management

- **As a user, I want to create categories,** so that I can group similar tasks together.
- **As a user, I want to update my categories,** so that I can rename or modify them.
- **As a user, I want to delete my categories,** so that I can remove unused ones.
- **As a user, I want to see only my own categories,** so that my task organization remains private.
- **As a user, I want to assign a task to one of my categories,** so that I can keep related tasks together.
- **As a user, I should not be able to assign tasks to another user’s category,** so that data remains secure.

---

## API DOCUMENTATION

The **To-Do-It API** provides a structured and efficient way to manage tasks. It is built using Django REST Framework (DRF) and follows RESTful API principles. This API allows users to authenticate, create and manage tasks, assign tasks to users, and filter them based on different criteria.

The API is structured into multiple endpoints for different functionalities:

### Profiles Endpoints

| Method | Endpoint          | Description            | view name |
| ------ | ----------------- | ---------------------- | --------- |
| GET    | `/profiles/`      | List all profiles      | LIST      |
| POST   | `/profiles/`      | Create a new profile   | LIST      |
| GET    | `/profiles/{id}/` | Retrieve profile by id | DETAIL    |
| PUT    | `/profiles/{id}/` | Update a profile by id | DETAIL    |
| DELETE | `/profiles/{id}/` | Delete a profile by id | DETAIL    |

### Tasks Endpoints

| Method | Endpoint       | Description           | view name |
| ------ | -------------- | --------------------- | --------- |
| GET    | `/tasks/`      | Retrieve all tasks    | LIST      |
| POST   | `/tasks/`      | Create a new task     | LIST      |
| GET    | `/tasks/{id}/` | Retrieve task details | DETAIL    |
| PUT    | `/tasks/{id}/` | Update a task         | DETAIL    |
| DELETE | `/tasks/{id}/` | Delete a task         | DETAIL    |

### Categories Endpoints

| Method | Endpoint            | Description                              |
| ------ | ------------------- | ---------------------------------------- |
| GET    | `/categories/`      | Retrieve all categories for the user.    |
| POST   | `/categories/`      | Create a new category.                   |
| GET    | `/categories/<id>/` | Retrieve details of a specific category. |
| PUT    | `/categories/<id>/` | Update a category.                       |
| DELETE | `/categories/<id>/` | Delete a category.                       |

### Filters and Queries

| Filter      | Description               | Example                           |
| ----------- | ------------------------- | --------------------------------- |
| `?status`   | Filter tasks by status.   | `/api/tasks/?status=completed`    |
| `?priority` | Filter tasks by priority. | `/api/tasks/?priority=high`       |
| `?category` | Filter tasks by category. | `/api/tasks/?category=work`       |
| `?due_date` | Filter tasks by due date. | `/api/tasks/?due_date=2025-01-15` |

### Response Format

All API responses are in JSON format. Example response for retrieving tasks:

```json
{
  "id": 1,
  "owner": "John Doe",
  "title": "Complete project",
  "description": "Finalize the API documentation",
  "status": "in_progress",
  "priority": "high",
  "category": {
    "id": 2,
    "name": "Work"
  },
  "due_date": "01 Feb 2026",
  "created_at": "30 Jan 2026",
  "updated_at": "31 Jan 2026"
}
```

## Database Design

Entity Relationship Diagrams help to visualize database architecture before creating models in Django. Understanding the relationships between different tables can save time recoding later in the project.

### Model Usage

| Model        | Usage                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| **User**     | Django’s built-in authentication system, managing users and their permissions.                                 |
| **Profile**  | Extends the User model to store additional user information like bio and location.                             |
| **Category** | Groups tasks for better organization, allowing users to categorize their tasks (e.g., Work, Personal).         |
| **Task**     | The central model of the app, representing individual tasks with details like status, priority, and deadlines. |

### **User Model**

| Field              | Type                   | Constraints                 | Description                                              |
| ------------------ | ---------------------- | --------------------------- | -------------------------------------------------------- |
| `id`               | AutoField              | Primary Key, Auto-increment | Unique identifier for each user.                         |
| _(default fields)_ | _(Provided by Django)_ |                             | Default fields like `username`, `email`, and `password`. |

### **Profile Model**

| Field        | Type                | Constraints                          | Description                                   |
| ------------ | ------------------- | ------------------------------------ | --------------------------------------------- |
| `id`         | AutoField           | Primary Key, Auto-increment          | Unique identifier for each profile.           |
| `owner`      | OneToOneField(User) | Foreign Key (User), Required, Unique | Links the profile to a single user.           |
| `name`       | CharField(255)      | Optional                             | User’s full name.                             |
| `created_at` | DateTimeField       | Auto-generated                       | Timestamp when the profile was created.       |
| `updated_at` | DateTimeField       | Auto-updated                         | Timestamp when the profile was last modified. |

### **Category Model**

| Field        | Type             | Constraints                  | Description                                  |
| ------------ | ---------------- | ---------------------------- | -------------------------------------------- |
| `id`         | AutoField        | Primary Key, Auto-increment  | Unique identifier for each category.         |
| `name`       | CharField(255)   | Required                     | Name of the category (e.g., Work, Personal). |
| `owner`      | ForeignKey(User) | Foreign Key (User), Required | Links category to the user who created it.   |
| `created_at` | DateTimeField    | Auto-generated               | Timestamp when the category was created.     |

### **Task Model**

| Field         | Type                 | Constraints                      | Description                                                     |
| ------------- | -------------------- | -------------------------------- | --------------------------------------------------------------- |
| `id`          | AutoField            | Primary Key, Auto-increment      | Unique identifier for each task.                                |
| `owner`       | ForeignKey(User)     | Foreign Key (User), Required     | Links task to the user who created it.                          |
| `title`       | CharField(255)       | Required                         | Short title of the task.                                        |
| `description` | TextField            | Optional                         | Detailed description of the task.                               |
| `category`    | ForeignKey(Category) | Foreign Key (Category), Optional | Links task to a specific category. Can be null.                 |
| `status`      | CharField(choices)   | Required                         | Task status (`Pending`, `In Progress`, `Completed`, `Overdue`). |
| `priority`    | CharField(choices)   | Required                         | Priority level (`Low`, `Medium`, `High`).                       |
| `due_date`    | DateField            | Optional                         | Deadline for task completion.                                   |
| `created_at`  | DateTimeField        | Auto-generated                   | Timestamp when the task was created.                            |
| `updated_at`  | DateTimeField        | Auto-updated                     | Timestamp when the task was last modified.                      |

### Relationships

- **Users** create **tasks** and categorize them using **categories**.
- **Profiles** store additional user-related information.
- **Tasks** belong to **categories**, which help users **organize and filter** them efficiently.

This **structured database design** ensures **data integrity, scalability, and optimized task management** within the To-Do-It API.

---

## Frameworks, Libraries & Tools Used

Below is a list of the frameworks, libraries, and tools used in the **To-Do-It API**. Also see requirements.txt.

### **Backend Frameworks**

| Name                            | Version | Description                                                   |
| ------------------------------- | ------- | ------------------------------------------------------------- |
| **Django**                      | 3.2.4   | High-level Python web framework for rapid development.        |
| **Django REST Framework (DRF)** | 3.12.4  | Toolkit for building Web APIs in Django.                      |
| **dj-rest-auth**                | 2.1.9   | Provides authentication endpoints, including JWT integration. |

### **Authentication & Security**

| Name                              | Version | Description                                  |
| --------------------------------- | ------- | -------------------------------------------- |
| **djangorestframework_simplejwt** | 5.4.0   | JSON Web Token (JWT) authentication for DRF. |
| **oauthlib**                      | 3.2.2   | Library for OAuth 1 and OAuth 2 protocols.   |
| **requests-oauthlib**             | 2.0.0   | OAuth support for `requests` library.        |

### **Database & Storage**

| Name                | Version | Description                                       |
| ------------------- | ------- | ------------------------------------------------- |
| **dj-database-url** | 0.5.0   | Enables configuration of the database from a URL. |
| **psycopg2**        | 2.9.10  | PostgreSQL database adapter for Python.           |
| **sqlparse**        | 0.5.3   | SQL parsing library used by Django.               |

### **Task Management & Filtering**

| Name              | Version | Description                                  |
| ----------------- | ------- | -------------------------------------------- |
| **django-filter** | 24.3    | Filtering support for Django models.         |
| **django-cron**   | 0.6.0   | Allows scheduled background tasks in Django. |

### **Middleware & Server**

| Name                    | Version | Description                                                   |
| ----------------------- | ------- | ------------------------------------------------------------- |
| **django-cors-headers** | 4.6.0   | Middleware for handling Cross-Origin Resource Sharing (CORS). |
| **gunicorn**            | 23.0.0  | WSGI server for deploying Django applications.                |

### **Other Dependencies**

| Name           | Version | Description                                          |
| -------------- | ------- | ---------------------------------------------------- |
| **asgiref**    | 3.8.1   | ASGI utilities for Django async support.             |
| **pytz**       | 2024.2  | Time zone library for Python.                        |
| **setuptools** | 75.8.0  | Tool for packaging and distributing Python projects. |

---

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

## Installation Workflow

This process has been documented separately in [INSTALLATION.md](INSTALLATION.md)

## Development Workflow

This process has been documented separately in [AGILE.md](AGILE.md)

## Testing Workflow

- This process has been documented separately in [TESTING.md](TESTING.md)
- Python Vaildation is documented here [VALIDATION.md](VALIDATION.md)

## Deployment

This process has been documented separately in [DEPLOYMENT.md](DEPLOYMENT.md)

## Known Issues

## Future Enhancements

## Credits
