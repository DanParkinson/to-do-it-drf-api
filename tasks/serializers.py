from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    '''
    Serializer for the Task model.
    - Ensures owner details are read-only.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        '''
        Meta class to specify the model and fields to include in the serialization.
        '''
        model = Tasks
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'due_date',
        ]