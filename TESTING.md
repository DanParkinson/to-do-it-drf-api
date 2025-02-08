# Testing

## Tasks

#### ** General Task List & Detail Tests**

- [x] **Retrieve Task List**: Users can retrieve only their own task list.
- [x] **Retrieve a Specific Task with ownership**: Users can retrieve a task that belongs to them.
- [x] **Retrieve a Specific Task without ownership**: Users cannot retrieve another user's task (`404 Not Found`).

#### ** Task Creation**

- [x] **Successful Task Creation**: Logged-in users can create tasks with valid data.
- [x] **task creation invalid data**: Task creation fails with invalid or missing data (`400 Bad Request`).
- [x] **Task Ownership on creation**: Task is automatically assigned to the logged-in user upon creation.
- [x] **Unauthenticated Task Creation**: Unauthenticated users cannot create tasks (`403 Forbidden`).

#### ** Task Update**

- [x] **update own task valid data**: Task owners can update their own tasks.
- [x] **update own task invalid data**: Updating a task with invalid data should fail (`400 Bad Request`).
- [x] **cannot update owner field**: Task owners cannot update the `owner` field.
- [x] **Unauthorized Task Update**: Users cannot update another user's task (`404 Not Found`).

#### ** Task Deletion**

- [x] **Successful Task Deletion**: Task owners can delete their own tasks.
- [x] **Unauthorized Task Deletion**: Users cannot delete another user's task (`404 Not Found`).
- [x] **Unauthenticated Task Deletion**: Unauthenticated users cannot delete any task (`403 FORBIDDEN`).

#### ** Edge Cases**

- [x] **Non-existent Task Retrieval**: Retrieving a non-existent task should return `404 Not Found`.
- [x] **Non-existent Task Update/Delete**: Attempting to update or delete a non-existent task should return `404 Not Found`.

---
