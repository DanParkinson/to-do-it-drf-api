from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer
from drf_api.permissions import IsOwnerOrReadOnly

class CategoryListView(generics.ListCreateAPIView):
    """
    API view for listing and creating categories.
    - Users can only view their own categories.
    - Users must be authenticated.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Returns only categories belonging to the logged-in user.
        """
        return Category.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assigns the logged-in user as the category owner.
        """
        serializer.save(owner=self.request.user)
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view for retrieving, updating, and deleting categories.
    - Users can only modify their own categories.
    '''
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Returns only categories belonging to the logged-in user.
        """
        return Category.objects.filter(owner=self.request.user)