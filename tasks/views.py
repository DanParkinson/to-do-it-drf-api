# rest_framework
from rest_framework import generics
# permissions
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
# functionality
from rest_framework.views import APIView
from rest_framework.response import Response
# server requests
from django.shortcuts import get_object_or_404
# serializers
from .serializers import TaskSerializer
# models
from .models import Task
from categories.models import Category
# filters
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import filter_tasks_by_priority, filter_tasks_by_status


class TaskListView(generics.ListCreateAPIView):
    '''
    API view for listing and creating tasks.
    - Users can only view their own tasks.
    - Users must be authenticated to access.
    - Users can only assign categories they own.
    - Supports text search by title and description.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['priority', 'status']
    ordering_fields = ['priority', 'due_date', 'status']
    search_fields = ['title', 'description', 'category']

    def get_queryset(self):
        '''
        Returns only active (non-archived) belonging to the logged in user
        Supports filtering by priority.
        '''
        queryset = Task.objects.filter(owner=self.request.user, is_archived=False)

        task_ids = self.request.query_params.get("ids")
        if task_ids:
            task_ids = [int(id) for id in task_ids.split(",")]
            queryset = queryset.filter(id__in=task_ids)

        queryset = filter_tasks_by_priority(queryset, self.request)
        queryset = filter_tasks_by_status(queryset, self.request)
        return queryset

    def perform_create(self, serializer):
        """
        Assigns 'Uncategorized' if no category is provided.
        """
        user = self.request.user
        category = serializer.validated_data.get("category", None)

        if category is None or not Category.objects.filter(id=category.id, owner=user).exists():
            category = Category.objects.get(owner=user, name="Uncategorized")

        serializer.save(owner=user, category=category)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view for retrieving, updating, and deleting a task.
    - Users can only access their own tasks
    - Only the task owner can edit or delete
    '''
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer

    def get_queryset(self):
        '''
        Returns only tasks belonging to the logged in user.
        returns 404 for none-owner as the task is not in the queryset.
        not a 403 forbidden.
        '''
        return Task.objects.filter(owner=self.request.user)

    def get_object(self):
        '''
        Ensures users can only update/delete their own tasks.
        Prevents unauthorized users from seeing the task.
        '''
        queryset = self.get_queryset()
        # if task isnt found return 404
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        # ensures 'IsOwnerOrReadOnly' is obeyed
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        '''
        Automatically archive tasks when marked as 'Completed'
        Automatically unarchive tasks when changed from 'Completed'
        '''
        task = self.get_object()
        new_status = self.request.data.get("status")

        # If the new status is "Completed", archive the task
        if new_status == "Completed":
            serializer.save(is_archived=True)
        # If the status is changed from "Completed", unarchive the task
        elif task.status == "Completed" and new_status != "Completed":
            serializer.save(is_archived=False)
        else:
            serializer.save()


class ArchivedTaskListView(generics.ListAPIView):
    '''
    API view for listing only archived (completed) tasks.
    - Users can only view their own archived tasks.
    - Tasks marked as 'Completed' are automatically moved here.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        '''
        Returns only archived (completed) tasks belonging to the logged-in user.
        '''
        return Task.objects.filter(owner=self.request.user, is_archived=True)
