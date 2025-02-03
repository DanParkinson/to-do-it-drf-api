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

In this sprint, the backend will be set up using Django. Key objectives include configuring the project, installing necessary tools, and building the `Profiles` model. Django Rest Framework will be added to handle API endpoints for user and task management.

### **Tasks**
- [x] Install Django.
- [x] Create the Django project.
- [x] Run the server and append allowed hosts to configuration.
- [x] Create the `Profiles` app.
- [x] Create the `Profiles` model, use Django signals.
- [x] Add Django Rest Framework (DRF).
- [x] User authorization for login/logout, update and retrieve profiles.
- [] Create the `Task` resource.
- [] Users can create/edit/delete tasks.
- [] Users can filter by priority/status/due date/category.
- [] Run tests to check the profile resource works as expected.
- [] Run tests to check the task resource works as expected.
- [] Tasks whose due date is in the past will change status to overdue - Will be done at a later date after researching it.
- [] Create the `Categories` resource.
- [] Add search function.
- [] Install Django auth and JWT tokens.
- [] Prepare for deployment in Sprint 3. Adding pagination and root_route. Datetime fields nicely rendered.

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

