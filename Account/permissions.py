from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    print('request.user.role')
    """
    Custom permission to only allow admins to access.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.name == 'Admin'

class IsCustomerUser(permissions.BasePermission):
    """
    Custom permission to only allow customers to access.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role.name == 'Customer'
    
class CanRetrieveAdminAPI(permissions.BasePermission):
    """
    Custom permission to allow customers to retrieve admin-related APIs but not modify (POST/PUT/DELETE).
    """

    def has_permission(self, request, view):
        # Allow GET requests for admin-related APIs
        if request.method == 'GET' and request.user.is_authenticated :
            return True
        return False