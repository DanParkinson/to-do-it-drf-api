from rest_framework import serializers
from .models import Category
from tasks.models import Task


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    - Shows the task count for each category.
    - Ensures only the category owner can access it.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    task_count = serializers.SerializerMethodField()
    task_ids = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'owner',
            'task_count',
            'task_ids',
            'created_at'
        ]

    def get_task_count(self, obj):
        """Returns the number of tasks in this category"""
        return Task.objects.filter(category=obj, is_archived=False).count()

    def get_task_ids(self, obj):
        '''
        Returns a list of task IDs for this category
        '''
        request = self.context.get('request')
        return list(
            Task.objects.filter(
                category=obj,
                owner=request.user
            ).values_list('id', flat=True))
