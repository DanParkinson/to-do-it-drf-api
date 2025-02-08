from rest_framework import serializers
from .models import Task
from categories.models import Category


class TaskSerializer(serializers.ModelSerializer):
    '''
    Read-only serializer for retrieving task data.
    - Ensures users can only see and assign their own categories.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(), 
        allow_null=True,
        required=False,
    )

    class Meta:
        '''
        Meta class to specify the model and fields to include in the serialization.
        '''
        model = Task
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'category',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'due_date',
        ]
    
    def __init__(self, *args, **kwargs):
        '''
        Filter category choices based on the logged in user
        '''
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            self.fields['category'].queryset = Category.objects.filter(owner=request.user)
