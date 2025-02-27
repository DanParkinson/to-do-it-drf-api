from rest_framework import generics, status
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

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


class DeleteAccountView(APIView):
    """
    Allows a logged-in user to permanently delete their account.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "Your account has been deleted."}, status=status.HTTP_204_NO_CONTENT)
