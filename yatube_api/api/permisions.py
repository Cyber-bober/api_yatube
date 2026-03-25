from rest_framework import permissions
from posts.models import Post, Comment

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает изменение только автору объекта.
    Для остальных — только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS всегда разрешены
        if request.method in permissions.SAFE_METHODS:
            return True

        
        if isinstance(obj, Post):
            return obj.author == request.user
        elif isinstance(obj, Comment):
            return obj.author == request.user
        return False
