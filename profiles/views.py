from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
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
    Users cannot access other users' profiles.

    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        '''
        Restricts the profile retrieval to only the logged-in user.
        '''
        return Profile.objects.filter(owner=self.request.user)

    def get_object(self):
        '''
        Returns only the profile that belongs to the logged-in user.
        If the user tries to access another profile, it returns 404.
        '''
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj
