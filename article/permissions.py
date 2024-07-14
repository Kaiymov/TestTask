from rest_framework import permissions


class IsSubscriber(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'FW'


class NotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'AU'


class IsAuthorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.author == request.user)