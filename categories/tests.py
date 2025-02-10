from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Category
from tasks.models import Task
from datetime import date


class CategoryTests(APITestCase):
    '''
    Tests for category creation, retrieval, updating, and deletion.
    '''

    def setUp(self):
        '''
        Create test users and categories.
        '''
        self.user1 = User.objects.create_user(
            username="user1",
            password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="password123"
        )

        self.client.login(username="user1", password="password123")

        # Create categories for both users
        self.category1 = Category.objects.create(
            owner=self.user1,
            name="Work"
        )
        self.category2 = Category.objects.create(
            owner=self.user1,
            name="Personal"
        )
        self.category3 = Category.objects.create(
            owner=self.user2,
            name="Finance"
        )

    # ** Category Retrieval**

    def test_retrieve_category_list(self):
        '''
        Users can retrieve only their own categories.
        '''
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_specific_category_owned(self):
        '''
        Users can retrieve a category they created.
        '''
        response = self.client.get(f'/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Work")

    def test_retrieve_specific_category_not_owned(self):
        '''
        Users cannot retrieve another user's category (should return 404).
        '''
        response = self.client.get(f'/categories/{self.category3.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ** Category Creation**

    def test_create_category_successful(self):
        '''
        Users can create a category with valid data.
        '''
        response = self.client.post('/categories/', {"name": "Health"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 4)

    def test_create_category_invalid_data(self):
        '''
        Creating a category with missing name should fail.
        '''
        response = self.client.post('/categories/', {"name": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthenticated_category_creation(self):
        '''
        Unauthenticated users cannot create categories (403 Forbidden).
        '''
        self.client.logout()
        response = self.client.post('/categories/', {"name": "Education"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ** Category Update**

    def test_update_own_category(self):
        '''
        Users can update their own categories.
        '''
        response = self.client.put(
            f'/categories/{self.category1.id}/',
            {"name": "Updated Work"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, "Updated Work")

    def test_update_category_invalid_data(self):
        '''
        Updating a category with invalid data should fail.
        '''
        response = self.client.put(
            f'/categories/{self.category1.id}/',
            {"name": ""}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_category_not_owned(self):
        '''
        Users cannot update another user's category (should return 404).
        '''
        response = self.client.put(
            f'/categories/{self.category3.id}/',
            {"name": "Unauthorized Update"}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ** Category Deletion**

    def test_delete_own_category(self):
        '''
        Users can delete their own categories.
        '''
        response = self.client.delete(f'/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Category.objects.filter(
                id=self.category1.id
            ).exists())

    def test_delete_category_not_owned(self):
        '''
        Users cannot delete another user's category (should return 404).
        '''
        response = self.client.delete(f'/categories/{self.category3.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_category_deletion(self):
        '''
        Unauthenticated users cannot delete categories (403 Forbidden).
        '''
        self.client.logout()
        response = self.client.delete(f'/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ** Task-Category Relationship**


class TaskCategoryTests(APITestCase):
    '''
    Tests for ensuring tasks are correctly linked to categories.
    '''

    def setUp(self):
        '''
        Create test users, categories, and tasks.
        '''
        self.user1 = User.objects.create_user(
            username="user1",
            password="password123"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="password123"
        )

        self.client.login(username="user1", password="password123")

        # Create categories
        self.category1 = Category.objects.create(
            owner=self.user1,
            name="Work"
        )
        self.category2 = Category.objects.create(
            owner=self.user1,
            name="Personal"
        )
        self.category3 = Category.objects.create(
            owner=self.user2,
            name="Finance"
        )

        # Create tasks linked to categories
        self.task1 = Task.objects.create(
            owner=self.user1,
            title="Task 1",
            category=self.category1,
            due_date=date(2024, 2, 10)
        )
        self.task2 = Task.objects.create(
            owner=self.user1,
            title="Task 2",
            category=self.category2,
            due_date=date(2024, 3, 15)
        )

    def test_create_task_with_valid_category(self):
        '''
        Users can create a task with a category they own.
        '''
        response = self.client.post('/tasks/', {
            "title": "New Task",
            "category": self.category1.id,
            "due_date": "2024-04-01"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_create_task_with_invalid_category(self):
        '''
        Users cannot create a task with a category they do not own.
        '''
        response = self.client.post('/tasks/', {
            "title": "Invalid Task",
            "category": self.category3.id,
            "due_date": "2024-04-01"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task_with_valid_category(self):
        '''
        Users can update a task to a category they own.
        '''
        response = self.client.put(f'/tasks/{self.task1.id}/', {
            "title": "Updated Task",
            "category": self.category2.id,
            "due_date": "2024-02-10"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.category, self.category2)

    def test_update_task_with_invalid_category(self):
        '''
        Users cannot update a task to another user's category.
        '''
        response = self.client.put(f'/tasks/{self.task1.id}/', {
            "title": "Updated Task",
            "category": self.category3.id,
            "due_date": "2024-02-10"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.category, self.category1)

    def test_delete_category_with_tasks(self):
        '''
        If a category is deleted,
        tasks linked to it should be handled correctly.
        '''
        response = self.client.delete(f'/categories/{self.category1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if task1 still exists
        # and has its category removed (set to null)
        self.task1.refresh_from_db()
        # Ensure category was removed but task still exists
        self.assertIsNone(self.task1.category)
