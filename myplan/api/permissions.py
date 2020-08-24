from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """
    def has_object_permission(self, request, view, obj):
        try:
            if obj.user == request.user:
                return True
            return False
        except:
            return False
