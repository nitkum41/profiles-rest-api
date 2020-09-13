from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit own profile"""

    def has_object_permission(self,request,view,obj):
        """check user trying to update profile"""

        if request.method in permissions.SAFE_METHODS: #like saving
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """allow users to update own status"""

    def has_object_permission(self,request,view,obj):
        """check user is trying to update status"""
        if request.method in permissions.SAFE_METHODS: #like saving
            return True
        return obj.user_profile.id == request.user.id
