from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from datetime import date

class TaskListTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', password='password123')

        self.task1 = Task.objects.create(
            owner=self.user1,
            title="Task 1",
            description="First task description",
            status="Pending",
            priority="High",
            due_date=date(2024, 2, 15)
        )
        self.task2 = Task.objects.create(
            owner=self.user1,
            title="Task 2",
            description="Second task description",
            status="In Progress",
            priority="Medium",
            due_date=date(2024, 3, 1)
        )
        self.task3 = Task.objects.create(
            owner=self.user2,
            title="Task 3",
            description="third task description",
            status="Completed",
            priority="Low",
            due_date=date(2025, 3, 1)
        )

    # ------ General Task List & Detail Tests -----

    def test_retrieve_task_list(self):
        '''
        Ensure a logged in user can retrieve their task list 
        '''
        self.client.login(username="testuser1", password="password123")
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_retrieve_specific_task_with_ownership(self):
        '''
        User can retreive a task that belongs to them
        '''
        self.client.login(username='testuser1', password='password123')
        response =self.client.get(f'/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_specific_task_without_ownership(self):
        '''
        User cannot retrieve another users task
        '''
        self.client.login(username='testuser1', password='password123')
        response = self.client.get(f'/tasks/{self.task3.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    # ------ Task Creation ----- 
    
    def test_Successful_Task_Creation(self):
        '''
        Logged in user can create a task
        '''
        self.client.login(username='testuser1', password='password123')

        task_data = {
            "title": "New Task",
            "description": "This is a test task.",
            "status": "Pending",
            "priority": "Medium",
            "due_date": "2024-04-01"
        }

        response = self.client.post('/tasks/', task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Task.objects.count(), 4)
        new_task = Task.objects.get(title='New Task')
        self.assertEqual(new_task.owner, self.user1)
        self.assertEqual(new_task.description, "This is a test task.")
        self.assertEqual(new_task.status, "Pending")
        self.assertEqual(new_task.priority, "Medium")
        self.assertEqual(str(new_task.due_date), "2024-04-01")
    
    def test_task_creation_invalid_data(self):

        self.client.login(username='testuser1', password='password123')

        task_data = {
            "title": "",
            "description": "This is a test task.",
            "status": "Pending",
            "priority": "Medium",
            "due_date": "2024-04-01"
        }

        response = self.client.post(f'/tasks/', task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_task_ownership_on_creation(self):
        '''
        Ensure that the owner of a newly created task is automatically set to the logged-in user.
        '''
        self.client.login(username='testuser1', password='password123')

        task_data = {
        "title": "Owned Task",
        "description": "Task should be owned by testuser1.",
        "status": "Pending",
        "priority": "High",
        "due_date": "2024-04-10"
        }

        response = self.client.post('/tasks/', task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Task.objects.count(), 4)
        new_task = Task.objects.get(title="Owned Task")
        self.assertEqual(new_task.owner, self.user1)
    
    def test_unauthenticated_task_creation(self):
        '''
        Ensure that unauthenticated users cannot create tasks.
        '''
        task_data = {
            "title": "Unauthorized Task",
            "description": "This task should not be created.",
            "status": "Pending",
            "priority": "Low",
            "due_date": "2024-04-15"
        }

        response = self.client.post('/tasks/', task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Task.objects.count(), 3)

    # ------ Task Update ----- 
    
    def test_update_own_task_valid_data(self):
        '''
        A user can update their own task
        '''
        self.client.login(username='testuser1', password='password123')

        update_data = {
        "title": "Updated Task Title",
        "description": "This task has been updated.",
        "status": "Completed",
        "priority": "High",
        "due_date": "2024-05-01"
        }

        response = self.client.put(f'/tasks/{self.task1.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Updated Task Title")
        self.assertEqual(self.task1.description, "This task has been updated.")
        self.assertEqual(self.task1.status, "Completed")
        self.assertEqual(self.task1.priority, "High")
        self.assertEqual(str(self.task1.due_date), "2024-05-01")
    
    def test_update_own_task_invalid_data(self):
        '''
        A user cannot update a task with invalid data
        '''
        self.client.login(username='testuser1', password='password123')

        update_data = {
        "title": "",
        "description": "Invalid update attempt",
        "status": "wrong",
        "priority": "wrong",
        "due_date": "wrong"
        }

        response = self.client.put(f'/tasks/{self.task1.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.task1.refresh_from_db()
        self.assertNotEqual(self.task1.description, "Invalid update attempt")
        self.assertNotEqual(self.task1.status, "wrong")
        self.assertNotEqual(self.task1.priority, "wrong")
        self.assertNotEqual(str(self.task1.due_date), "wrong")
    
    def test_cannot_update_owner_field(self):
        '''
        Ensure users cannot change ownership. Other fields will still be updated.
        '''
        self.client.login(username='testuser1', password='password123')

        update_data = {
        "title": "Ownership Update Attempt",
        "description": "Trying to change the owner field.",
        "status": "In Progress",
        "priority": "Medium",
        "due_date": "2024-05-20",
        "owner": self.user2.id
        }

        response = self.client.put(f'/tasks/{self.task1.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.owner, self.user1)
        self.assertEqual(self.task1.description, "Trying to change the owner field.")
    
    def test_unauthorized_task_update(self):
        '''
        Ensure that a user cannot update a task they do not own.
        '''
        self.client.login(username='testuser2', password='password123')

        update_data = {
            "title": "Unauthorized Update",
            "description": "This should not be allowed.",
            "status": "Completed",
            "priority": "Medium",
            "due_date": "2024-06-01"
        }

        response = self.client.put(f'/tasks/{self.task1.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.task1.refresh_from_db()

        self.assertNotEqual(self.task1.title, "Unauthorized Update")
        self.assertNotEqual(self.task1.description, "This should not be allowed")
        self.assertNotEqual(self.task1.status, "Completed")
        self.assertNotEqual(self.task1.priority, "Medium")
        self.assertNotEqual(str(self.task1.due_date), "2024-06-01")
    
    # ------ Task Delete ----- 

    def test_successful_task_deletion(self):
        '''
        Ensure that a task owner can delete their own task successfully.
        '''
        self.client.login(username='testuser1', password='password123')
        response = self.client.delete(f'/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task1.id)
    
    def test_unauthorized_task_deletion(self):
        '''
        Ensure a user cannot delete another user's task.
        '''
        self.client.login(username='testuser2', password='password123')
        response = self.client.delete(f'/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        task_exists = Task.objects.filter(id=self.task1.id).exists()
        self.assertTrue(task_exists)

    def test_unauthenticated_task_deletion(self):
        '''
        Ensure that unauthenticated users cannot delete any task.
        '''
        response = self.client.delete(f'/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        task_exists = Task.objects.filter(id=self.task1.id).exists()
        self.assertTrue(task_exists)

    # ------ edge cases ----- 
    
    def test_non_existent_task_retrieval(self):
        '''
        Ensure that retrieving a non-existent task returns 404 Not Found.
        '''
        self.client.login(username='testuser1', password='password123')
        non_existent_task_id = 9999
        response = self.client.get(f'/tasks/{non_existent_task_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_update_non_existent_task(self):
        '''
        Ensure that attempting to update a non-existent task returns 404 Not Found.
        '''
        self.client.login(username='testuser1', password='password123')
        non_existent_task_id = 9999
        update_data = {
            "title": "Updated Task",
            "description": "Trying to update a task that does not exist.",
            "status": "Completed",
            "priority": "High",
            "due_date": "2024-06-10"
        }

        response = self.client.put(f'/tasks/{non_existent_task_id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TaskFilteringTests(APITestCase):
    '''
    Tests for filtering tasks by priority, status, and due date sorting.
    '''

    def setUp(self):
        '''
        Create test users and tasks.
        '''
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        self.task1 = Task.objects.create(
            owner=self.user, title="Task 1", priority="High", status="Pending", due_date=date(2024, 2, 10)
        )
        self.task2 = Task.objects.create(
            owner=self.user, title="Task 2", priority="Medium", status="In Progress", due_date=date(2024, 3, 15)
        )
        self.task3 = Task.objects.create(
            owner=self.user, title="Task 3", priority="Low", status="Completed", due_date=date(2024, 4, 1)
        )
    
    def test_filter_by_priority_valid(self):
        '''
        Users can filter tasks by valid priority (High, Medium, Low).
        '''
        response = self.client.get('/tasks/?priority=High')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Task 1")
    
    def test_filter_by_status_valid(self):
        '''
        Users can filter tasks by valid status (Pending, In Progress, Completed, Overdue).
        '''
        response = self.client.get('/tasks/?status=Pending')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Task 1")
    
    def test_filter_by_priority_and_status(self):
        '''
        Users can filter by both priority and status together.
        '''
        response = self.client.get('/tasks/?priority=High&status=Pending')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Task 1")
    
    def test_filter_by_status_and_sort_by_due_date(self):
        '''
        Users can filter by status and sort by due date.
        '''
        response = self.client.get('/tasks/?status=Pending&ordering=due_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Task 1")
    
    def test_sort_tasks_by_earliest_due_date(self):
        '''
        Users can sort tasks in ascending order of due date.
        '''
        response = self.client.get('/tasks/?ordering=due_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Task 1")
        self.assertEqual(response.data[2]['title'], "Task 3")
    
    def test_sort_tasks_by_latest_due_date(self):
        '''
        Users can sort tasks in descending order of due date.
        '''
        response = self.client.get('/tasks/?ordering=-due_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Task 3")
        self.assertEqual(response.data[2]['title'], "Task 1")










        
