from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit or delete it.
    - Read-only (GET, HEAD, OPTIONS) requests are allowed for everyone.
    - Write permissions (POST, PUT, PATCH, DELETE) are only allowed for the owner of the object.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Check if the request should be allowed based on:
        1. If the request method is a SAFE_METHOD (read-only), allow it.
        2. If it's a write operation, allow only if the requesting user is the owner of the object.
        '''
        # Allows read only access for any user
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Allows write access to owner
        return obj.owner == request.user