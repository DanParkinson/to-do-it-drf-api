# Testing

## Automated tests

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

---

## Task Filtering Tests

### Filtering by Priority

- [x] **Filter by Priority (Valid Option)**: Users can filter tasks by `"Low"`, `"Medium"`, or `"High"`.

### Filtering by Status

- [x] **Filter by Status (Valid Option)**: Users can filter tasks by `"Pending"`, `"In Progress"`, `"Completed"`, or `"Overdue"`.

### Combining Filters

- [x] **Filter by Priority & Status Together**: Users can combine priority and status filters in a single request.
- [x] **Filter by Status & Sorting by Due Date**: Users can filter tasks by status and sort by `due_date`.

### Sorting by Due Date

- [x] **Sort Tasks by Earliest Due Date**: Sorting tasks in ascending order of due date (`?ordering=due_date`).
- [x] **Sort Tasks by Latest Due Date**: Sorting tasks in descending order of due date (`?ordering=-due_date`).

---

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

#### Edge Cases

- [x] **Non-existent Task Retrieval**: Retrieving a non-existent task should return `404 Not Found`.
- [x] **Non-existent Task Update/Delete**: Attempting to update or delete a non-existent task should return `404 Not Found`.

---

## Manual Testing
