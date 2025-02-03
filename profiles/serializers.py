from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serializer for the Profile model
    - Converts Profile instances into JSON data for API responses
    - Ensures certain fields are read only and creates custom fields
    '''
    # Read-only field: Displays the owner's username instead of their user ID
    owner = serializers.ReadOnlyField(source='owner.username')
    # Custom field: Indicates if the logged-in user is the owner of the profile
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Custom method to determine if the logged-in user owns the profile.
        - Accesses the request from serializer context.
        - Compares the logged-in user (`request.user`) with the profile owner (`obj.owner`).
        - Returns True if the user is the owner, otherwise False.
        """
        request = self.context['request']
        return request.user  == obj.owner

    class Meta:
        '''
        Meta class to specify the model and fields to include in the serialization.
        '''
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'name', 'created_at', 'updated_at',
        ]