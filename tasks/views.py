# rest_framework
from rest_framework import generics
# permissions
from rest_framework.permissions import IsAuthenticated
from drf_api.permissions import IsOwnerOrReadOnly
#functionality
from rest_framework.views import APIView
from rest_framework.response import Response
#serializers
from .serializers import TaskSerializer
#models
from .models import Tasks

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
        return Tasks.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        '''
        Returns only tasks belonging to the logged-in user.
        '''
        serializer.save(owner=self.request.user)
    
    

