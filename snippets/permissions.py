from rest_framework import permissions

"""custom permissions should be placed a permission file like this"""
class IsOwnerOrReadOnly(permissions.BasePermission):
    """ only allow owners of snippet to edit it"""

    def ha_object_permissions(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user