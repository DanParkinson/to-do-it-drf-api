from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tasks
from datetime import date

class TaskListTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', password='password123')

        self.task1 = Tasks.objects.create(
            owner=self.user1,
            title="Task 1",
            description="First task description",
            status="Pending",
            priority="High",
            due_date=date(2024, 2, 15)
        )
        self.task2 = Tasks.objects.create(
            owner=self.user1,
            title="Task 2",
            description="Second task description",
            status="In Progress",
            priority="Medium",
            due_date=date(2024, 3, 1)
        )
        self.task3 = Tasks.objects.create(
            owner=self.user2,
            title="Task 3",
            description="third task description",
            status="Completed",
            priority="Low",
            due_date=date(2025, 3, 1)
        )

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
    
    def test_task_creation_authorised(self):
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

        self.assertEqual(Tasks.objects.count(), 4)
        new_task = Tasks.objects.get(title='New Task')
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

        self.assertEqual(Tasks.objects.count(), 4)
        new_task = Tasks.objects.get(title="Owned Task")
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
        self.assertEqual(Tasks.objects.count(), 3)



        
