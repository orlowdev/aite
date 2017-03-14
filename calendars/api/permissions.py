from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Only the owner is allowed to execute this action"
    safe_methods = ['PUT', 'GET']

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.calendar.user == request.user
