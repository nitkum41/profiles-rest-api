from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit own profile"""

    def has_object_permission(self,request,view,obj):
        """check user trying to update profile"""

        if request.method in permissions.SAFE_METHODS: #like saving
            return True
        return obj.id == request.user.id
