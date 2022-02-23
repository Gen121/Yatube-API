from rest_framework import permissions


class AuthorOrReadOnnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        # request.method in permissions.SAFE_METHODS
        return True
