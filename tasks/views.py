# rest_framework
from rest_framework import generics
# permissions
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
#functionality
from rest_framework.views import APIView
from rest_framework.response import Response
# server requests
from django.shortcuts import get_object_or_404
#serializers
from .serializers import TaskSerializer
#models
from .models import Task

class TaskListView(generics.ListCreateAPIView):
    '''
    API view for listing and creating tasks.
    - Users can only view their own tasks.
    - Users must be authenticated to access.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        '''
        Returns only tasks belonging to the logged in user
        '''
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        '''
        Returns only tasks belonging to the logged-in user.
        '''
        serializer.save(owner=self.request.user)

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
        returns 404 for none-owner as the task is not in the queryset. not a 403 forbidden.
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