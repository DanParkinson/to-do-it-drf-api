from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .models import Category
from .serializers import CategorySerializer
from drf_api.permissions import IsOwnerOrReadOnly
from tasks.models import Task


class CategoryListView(generics.ListCreateAPIView):
    """
    API view for listing and creating categories.
    - Users can only view their own categories.
    - Users must be authenticated.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter] 
    search_fields = ["name"] 

    def get_queryset(self):
        """
        Returns only categories belonging to the logged-in user.
        Creates an 'Uncategorized' category if missing.
        """
        user = self.request.user
        queryset = Category.objects.filter(owner=user)

        # Ensure "Uncategorized" exists
        if not queryset.filter(name="Uncategorized").exists():
            Category.objects.create(owner=user, name="Uncategorized")

        return queryset

    def perform_create(self, serializer):
        """
        Automatically assigns the logged-in user as the category owner.
        """
        serializer.save(owner=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view for retrieving, updating, and deleting categories.
    - Users can only modify their own categories.
    - If a category is deleted, all associated tasks are also deleted
    '''
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Returns only categories belonging to the logged-in user.
        """
        return Category.objects.filter(owner=self.request.user)
      
    def perform_destroy(self, instance):
        """
        Deletes all tasks linked to the category before deleting the category itself.
        """
        Task.objects.filter(category=instance).delete()  # Delete all associated tasks
        instance.delete()  # Delete the category