from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer

from .models import Profile

class ProfileListView(generics.ListAPIView):
    '''
    Generalised Profile list view
    List all profiles
    No create view as profile creation handled by django signals in models.py
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    '''
    Generalised Profile list view for get, update
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
