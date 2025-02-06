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
    
    def retrieve_specific_task_with_ownership(self):
        '''
        User can retreive a task that belongs to them
        '''
        self.client.login(username='testuser1', password='password123')
        response =self.client.get(f'/tasks/{self.task1.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def retrieve_specific_task_without_ownership(self):

        self.client.login(username='testuser1', password='password123')
        response = self.client.get(f'/tasks/{self.task3.id}')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
