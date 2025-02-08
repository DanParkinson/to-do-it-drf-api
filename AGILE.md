# AGILE

After a few false starts, I reflected on the challenges of previous attempts and restructured my approach to focus on clarity and efficiency. This new plan ensures a more organized workflow and faster progress.

---

## **Sprint 1: Setting Up the Repo and README**

The first sprint focuses on setting up the repository and documenting the project structure, goals, and design decisions.

### **Tasks**

- [x] Set up the GitHub repository.
- [x] Perform design thinking exercise for features to include in the project.
- [x] Mock up the initial database design and document it in the README.
- [x] List and link technologies used in the README.

---

## **Sprint 2: Initial Backend Setup**

In this sprint, the backend will be set up using Django, focusing on core functionality for user and task management. Key objectives include configuring the project, installing necessary tools, and building the `Profiles`, `Tasks`, `Categories` models. Django Rest Framework (DRF) will be used to create API endpoints, ensuring proper authentication and authorization.

Additional features such as task filtering, search functionality, and user authentication using JWT tokens will be implemented. Unit tests will be written to verify that both the `Profiles`, `Tasks`, `Categories` resources function as expected. Finally, preparations will be made for deployment in Sprint 3, including pagination, root route setup, and improved datetime formatting.

---

#### **🔹 Project Setup**

- [x] Install Django.
- [x] Create the Django project.
- [x] Add Django Rest Framework (DRF).
- [x] Run the server and append allowed hosts to configuration.

#### **🔹 Profiles App**

- [x] Create the `Profiles` app.
- [x] Create `Profile` model.
- [x] Create `ProfileListView`.
- [x] Create `ProfileSerializer`.
- [x] Create `Profile` URLs.
- [x] Create `IsOwnerOrReadOnly` permission in `drf_api.permissions.py`.
- [x] Create `ProfileDetailView` for update and retrieve.
- [x] Add Django Rest authentication URLs.

#### **🔹 User Authentication**

- [x] User authorization for login/logout, update, and retrieve profiles.

#### **🔹 Tasks App**

- [x] Create the `Tasks` app.
- [x] Create `Task` model.
- [x] Create `TaskListView`.
- [x] Create `TaskSerializer`.
- [x] Create `Task` URLs.
- [x] Create `TaskDetailView` for update, retrieve, and delete.
- [x] Write unittests for task resource.

#### **🔹 Categories App**

- [x] Create the `Categories` app.
- [x] Create `Category` model.
- [x] Create `CategoryListView`.
- [x] Create `CategorySerializer`.
- [x] Create `Category` URLs.
- [x] Create `CategoryDetailView` for update, retrieve, and delete.

#### **🔹 Task Filtering & Functionality**

- [ ] Users can filter tasks by `priority`, `status`, or `category`.
- [ ] Users can order tasks by priority and due date
- [ ] Tasks whose due date is in the past should automatically change status to `overdue` (Research needed before implementation).

#### **🔹 Testing & Features**

- [ ] Run tests to check that the `Profiles` resource works as expected.
- [x] Run tests to check that the `Tasks` resource works as expected.
- [ ] Run tests to check that the `Categories` resource works as expected.
- [ ] Run tests to check that filtering and search works as expected.
- [ ] Add a search function.

#### **🔹 Authentication & Deployment Preparation**

- [ ] Install Django authentication and JWT tokens.
- [ ] Prepare for deployment in Sprint 3:
  - Add pagination.
  - Add a `root_route`.

---

## **Sprint 3 : Deployment**

Deployment of the backend, ensuring all endpoints function correctly in production.

- Documented in [DEPLOYMENT.md](DEPLOYMENT.md).

---

## **Sprint 4: Testing and Feedback**

This sprint will focus on testing the backend thoroughly and gathering feedback for improvements.

### **Tasks**

- [ ] Write unit tests for API endpoints.
- [ ] Conduct integration testing with mock frontend requests.
- [ ] Document any issues and fixes during testing.
- [ ] Optimize database queries for performance.
- [ ] Gather feedback from peers or testers on API functionality.

---

## **Sprint 5: Final Adjustments**

The final sprint will involve making adjustments to improve the backend before the frontend integration.

### **Tasks**

- [ ] Review and optimize API response formats.
- [ ] Ensure proper error handling for all endpoints.
- [ ] Document API usage for frontend developers.
- [ ] Finalize README and API documentation.
