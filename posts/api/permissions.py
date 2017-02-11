from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "Only the owner is allowed to execute this action"
    safe_methods = ['GET', 'PUT']

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
