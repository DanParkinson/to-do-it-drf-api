# Testing

## Automated tests

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

# Manual Testing

## **Table of Contents**

### 1. Profile & User Data

- [1.1 Retrieve Profile Details](#11-retrieve-profile-details)
- [1.2 Retrieve Another User’s Profile (Unauthorized)](#12-retrieve-another-users-profile-unauthorized)

### 2. Task Management

- [2.1 Create a Task](#21-create-a-task)
- [2.2 Unauthorized Task Creation](#22-unauthorized-task-creation)
- [2.3 Update a Task](#23-update-a-task)
- [2.4 Unauthorized Task Update](#24-unauthorized-task-update)
- [2.5 Delete a Task](#25-delete-a-task)
- [2.6 Unauthorized Task Deletion](#26-unauthorized-task-deletion)

### 3. Task Filtering & Search

- [3.1 Filter by Priority](#31-filter-by-priority)
- [3.2 Filter by Status](#32-filter-by-status)
- [3.3 Search by Title or Description](#33-search-by-title-or-description)
- [3.4 Sorting by Due Date](#34-sorting-by-due-date)

### 4. Category Management

- [4.1 Create a Category](#41-create-a-category)
- [4.2 Unauthorized Category Creation](#42-unauthorized-category-creation)
- [4.3 Assign a Task to a Category](#43-assign-a-task-to-a-category)
- [4.4 Restrict Category Access](#44-restrict-category-access)
- [4.5 Delete a Category](#45-delete-a-category)
- [4.6 Unauthorized Category Deletion](#46-unauthorized-category-deletion)

# Manual Testing for Database & Backend Functionality

## 1. Profile & User Data

### 1.1 Retrieve Profile Details

- **Test Scenario:** A logged-in user can retrieve their profile.
- **Steps to Perform:**
  1. Log in.
  2. Send a `GET` request to `/profiles/{id}/`
- **Expected Outcome:** The user sees their profile details.

![1.1](readme_assets\manual_testing\1.1.png)

### 1.2 Retrieve Another User’s Profile (Unauthorized)

- **Test Scenario:** A user **cannot** retrieve another user’s profile.
- **Steps to Perform:**
  1. Log in as User A.
  2. Try to access `/profiles/{id}/` of User B.
- **Expected Outcome:** `404 Not Found` response.

![1.2](readme_assets\manual_testing\1.2.png)

---

## 2. Task Management

### 2.1 Create a Task

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

### 2.2 Unauthorized Task Creation

- **Test Scenario:** A user **cannot** create a task without being logged in.
- **Steps to Perform:**
  1. Logout.
  2. Send a `POST` request to `/tasks/` with valid task data.
- **Expected Outcome:** `403 Forbidden` response.

![2.2](readme_assets\manual_testing\2.2.png)

### 2.3 Update a Task

- **Test Scenario:** Users should be able to update their own tasks.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/{task_id}/` and send a `PUT` request.
  3. Modify title, description, or other fields.
- **Expected Outcome:** Task updates successfully.

![2.3](readme_assets\manual_testing\2.3.png)

### 2.4 Unauthorized Task Update

- **Test Scenario:** Users **cannot** update another user's task.
- **Steps to Perform:**
  1. Log in as User A.
  2. Attempt to update User B’s task via `/tasks/{task_id}/`.
- **Expected Outcome:** `404 Not Found` response.

- Update attempt

![2.4.1](readme_assets\manual_testing\2.4.1.png)

- Task not updated

![2.4.2](readme_assets\manual_testing\2.4.2.png)

### 2.5 Delete a Task

- **Test Scenario:** Users should be able to delete their own tasks.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/{task_id}/` and send a `DELETE` request.
- **Expected Outcome:** Task is deleted.

  ![2.5](readme_assets\manual_testing\2.5.png)

### 2.6 Unauthorized Task Deletion

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

## 3. Task Filtering & Search

### 3.1 Filter by Priority

- **Test Scenario:** Users can filter tasks by `"Low"`, `"Medium"`, or `"High"`.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?priority=Medium`.
- **Expected Outcome:** Only Medium-priority tasks are returned.

![3.1](readme_assets\manual_testing\3.1.png)

### 3.2 Filter by Status

- **Test Scenario:** Users can filter tasks by `"Pending"`, `"Completed"`, etc.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?status=In-Progress`.
- **Expected Outcome:** Only In Progress tasks are returned.

![3.2](readme_assets\manual_testing\3.2.png)

### 3.3 Search by Title or Description

- **Test Scenario:** Users can search for tasks by keywords.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?search=New`.
- **Expected Outcome:** Tasks containing "new" in title or description are returned.

![3.3](readme_assets\manual_testing\3.3.png)

### 3.4 Sorting by Due Date

- **Test Scenario:** Users can sort tasks by due date.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/tasks/?ordering=due_date`.
- **Expected Outcome:** Tasks appear in ascending order of due date.

![3.4](readme_assets\manual_testing\3.4.png)

## 4. Category Management

### 4.1 Create a Category

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

### 4.2 Unauthorized Category Creation

- **Test Scenario:** A user **cannot** create a category without being logged in.
- **Steps to Perform:**
  1. Logout.
  2. Send a `POST` request to `/categories/` with valid category data.
- **Expected Outcome:** `403 Forbidden` response.

![4.2](readme_assets\manual_testing\4.2.png)

### 4.3 Assign a Task to a Category

- **Test Scenario:** Users can assign a task to one of their own categories.
- **Steps to Perform:**
  1. Log in.
  2. Create a task and assign it to an existing category.
- **Expected Outcome:** Task is linked to the correct category.

![4.3](readme_assets\manual_testing\4.3.png)

### 4.4 Restrict Category Access

- **Test Scenario:** Users **cannot** access another user's category.
- **Steps to Perform:**
  1. Log in as User A.
  2. Try to access `/categories/{category_id}/` of User B.
- **Expected Outcome:** `404 Not Found` response.

![4.4](readme_assets\manual_testing\4.4.png)

### 4.5 Delete a Category

- **Test Scenario:** Users should be able to delete their own categories.
- **Steps to Perform:**
  1. Log in.
  2. Go to `/categories/{category_id}/` and send a `DELETE` request.
- **Expected Outcome:** The category is deleted.

- Delete attempt

![4.5.1](readme_assets\manual_testing\4.5.1.png)

- Task not Deleted

![4.5.2](readme_assets\manual_testing\4.5.2.png)

### 4.6 Unauthorized Category Deletion

- **Test Scenario:** Users **cannot** delete another user's category.
- **Steps to Perform:**
  1. Log in as User A.
  2. Attempt to delete User B’s category via `/categories/{category_id}/`.
- **Expected Outcome:** `404 Not Found` response.

![4.6](readme_assets\manual_testing\4.6.png)
