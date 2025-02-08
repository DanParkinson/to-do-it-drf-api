from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    '''
    Serializer for the Category model.
    - Ensures the owner field is read-only.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'created_at']