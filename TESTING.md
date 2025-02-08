# Testing

## Tasks

#### ** General Task List & Detail Tests**

- [x] **Retrieve Task List**: Users can retrieve only their own task list.
- [x] **Retrieve a Specific Task**: Users can retrieve a task that belongs to them.
- [x] **Unauthorized Task Access**: Users cannot retrieve another user's task (`404 Not Found`).

#### ** Task Creation**

- [x] **Successful Task Creation**: Logged-in users can create tasks with valid data.
- [x] **Failed Task Creation**: Task creation fails with invalid or missing data (`400 Bad Request`).
- [x] **Task Ownership**: Task is automatically assigned to the logged-in user upon creation.
- [x] **Unauthenticated Task Creation**: Unauthenticated users cannot create tasks (`403 Forbidden`).

#### ** Task Update**

- [x] **Successful Task Update**: Task owners can update their own tasks.
- [x] **Failed Task Update**: Updating a task with invalid data should fail (`400 Bad Request`).
- [x] **Prevent Changing Ownership**: Task owners cannot update the `owner` field.
- [x] **Unauthorized Task Update**: Users cannot update another user's task (`404 Not Found`).

#### ** Task Deletion**

- [ ] **Successful Task Deletion**: Task owners can delete their own tasks.
- [ ] **Unauthorized Task Deletion**: Users cannot delete another user's task (`404 Not Found`).
- [ ] **Unauthenticated Task Deletion**: Unauthenticated users cannot delete any task (`401 Unauthorized`).

#### ** Edge Cases**

- [ ] **Non-existent Task Retrieval**: Retrieving a non-existent task should return `404 Not Found`.
- [ ] **Non-existent Task Update/Delete**: Attempting to update or delete a non-existent task should return `404 Not Found`.

---
